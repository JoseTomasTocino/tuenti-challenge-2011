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

def main():
    numCases = int(sys.stdin.readline())
    for i in range(numCases):
        numLights = int(sys.stdin.readline())
        numSeconds = int(sys.stdin.readline())

        lightsOn = []

        for i in range(numLights):
            # A light i will get turned on for the first time at the
            # instant i + 1.
            # Even lights will be on at odd times and vice versa

            if numSeconds > i and abs((numSeconds % 2) - (i % 2)) == 1:
                lightsOn.append(str(i))

        if lightsOn:
            print " ".join(lightsOn)
        else:
            print "All lights are off :("

if __name__ == '__main__':
    main()
