#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 José Tomás Tocino García <theom3ga@gmail.com>

# Autor: José Tomás Tocino García

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

import sys

def getSubStrings(string, n):
    """ Get all existing substrings of length n within string"""
    strLen = len(string)

    if strLen <= n:
        return [string]

    maxOffset = strLen - n
    listSubstr = []

    for i in range(maxOffset + 1):
        listSubstr.append(string[i:i+n])

    return listSubstr


def searchCommon(leftPart, rightPart):
    if len(leftPart) < len(rightPart):
        leftPart, rightPart = rightPart, leftPart

    for i in reversed(range(len(rightPart) + 1)):
        pieces = getSubStrings(rightPart, i)

        for p in pieces:
            if p in leftPart:
                return p
    

def main():
    for line in sys.stdin:
        leftPart, rightPart = line.strip().split(" ")
        print searchCommon(leftPart, rightPart)

if __name__ == '__main__':
    main()
