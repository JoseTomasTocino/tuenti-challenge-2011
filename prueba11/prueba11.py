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
# 02110-1301, USA

import sys

def getFurtherStation(stations, dist):
    return sorted([s for s in stations if s <= dist], key = lambda x: abs(x - dist))[0]

def main():
    numCases = int(sys.stdin.readline())

    for i in range(numCases):
        maxDistPerTank = int(sys.stdin.readline())
        distToTravel = int(sys.stdin.readline())
        numStations = int(sys.stdin.readline())
        
        stations = map(int, sys.stdin.readline().strip().split(" "))

        if distToTravel <= maxDistPerTank:
            print "No stops"
            continue

        traveledSoFar = 0
        chosenStations = []

        while 1:
            nextStation = getFurtherStation(stations, traveledSoFar + maxDistPerTank)
            chosenStations.append(nextStation)
            traveledSoFar = nextStation

            stations = [s for s in stations if s > traveledSoFar]

            if traveledSoFar + maxDistPerTank >= distToTravel:
                break

        print " ".join(map(str,chosenStations))

if __name__ == '__main__':
    main()
