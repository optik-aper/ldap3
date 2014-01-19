"""
Created on 2014.01.06

@author: Giovanni Cannata

Copyright 2014 Giovanni Cannata

This file is part of python3-ldap.

python3-ldap is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

python3-ldap is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with python3-ldap in the COPYING and COPYING.LESSER files.
If not, see <http://www.gnu.org/licenses/>.
"""
from os import linesep


class Attribute(object):
    def __init__(self, key):
        self.key = key
        self.name = None
        self.values = None
        self.syntax = None
        self.multi = None


def __repr__(self):
    if not self.multi:
        r = self.name + ': ' + str(self.values)
    else:
        r = self.name + ': ' + str(self.values[0])
        if len(self.values > 1):
            filler = ' ' * (len(self.name) + 2)
            for value in self.values[1:]:
                r += linesep + filler + value

    return r


def __str__(self):
    return self.__repr__()
