"""
(C) 2008-2009, Red Hat Inc.
Michael DeHaan <michael.dehaan AT gmail>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301  USA
"""


import time


def register() -> str:
    """
    The mandatory Cobbler module registration hook.
    """
    # this pure python trigger acts as if it were a legacy shell-trigger, but is much faster.
    # the return of this method indicates the trigger type
    return "/var/lib/cobbler/triggers/install/post/*"


def run(api, args, logger) -> int:
    """

    :param api: This parameter is unused currently.
    :param args: An array of three elements. Type (system/profile), name and ip. If no ip is present use a ``?``.
    :param logger: This parameter is unused currently.
    :return: Always 0
    """
    # FIXME: make everything use the logger, no prints, use util.subprocess_call, etc

    objtype = args[0]   # "system" or "profile"
    name = args[1]      # name of system or profile
    ip = args[2]        # ip or "?"

    with open("/var/log/cobbler/install.log", "a+") as fd:
        fd.write("%s\t%s\t%s\tstop\t%s\n" % (objtype, name, ip, time.time()))

    return 0
