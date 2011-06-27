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
import pprint

def main():
    for line in sys.stdin:
        elements = line.strip().split(" ")
        elements = [x for x in elements if x != ""]

        numberOfPlanets = int(elements[0])
        earthIndex = int(elements[1])
        atlantisIndex = int(elements[2])

        """
        print "NumberOfPlanets", numberOfPlanets
        print "EarthIndex", earthIndex
        print "AtlantisIndex", atlantisIndex
        # """

        distances = [[None for x in range (numberOfPlanets + 1)] for y in range (numberOfPlanets + 1)]

        for i in range(numberOfPlanets + 1):
            distances[i][i] = 0

        for i in range (3, len(elements)):            
            index1, index2, distance = map(int, elements[i].split(","))
            
            distances[index1][index2] = distance 
            
        paths = distances[:]

        minDist = 0

        # Floyd algorithm
        for k in range(numberOfPlanets + 1):
            for i in range(numberOfPlanets + 1):
                for j in range(numberOfPlanets + 1):
                    try:
                        dt = paths[i][k] + paths[k][j]
                    except:
                        continue

                    if paths[i][j] == None and dt != None:
                        paths[i][j] = dt
                    elif paths[i][j] > dt:
                        paths[i][j] = dt


        calcDistance = paths[earthIndex ][atlantisIndex]

        # Detects negative cycles
        for i in range(numberOfPlanets + 1):
            if paths[i][i] < 0:
                calcDistance = None
                

        if calcDistance  == None:
            print "BAZINGA"
        else:
            print 25000 + calcDistance - minDist
            


if __name__ == '__main__':
    main()
