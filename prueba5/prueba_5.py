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
        line = line.strip()
        lineParts = line.split(" ")

        maxWeight = int(lineParts[1])
        cows = zip(map(int, lineParts[2].split(",")), map(int, lineParts[3].split(",")))
        numberOfCows = len(cows)

        # 0 to maxWeight columns
        # 0 to numberOfCows - 1 rows
        dynamicTable = [[0 for w in range(maxWeight + 1)] for j in range(numberOfCows + 1)]

        for j in range(1, numberOfCows + 1):
            currentWeight, currentMilk = cows[j-1]
            for w in range(1, maxWeight + 1):
                if currentWeight > w:
                    dynamicTable[j][w] = dynamicTable[j - 1][w]
                else:
                    dynamicTable[j][w] = max(dynamicTable[j - 1][w], 
                                             dynamicTable[j - 1][w - currentWeight] + currentMilk) #"""

        print dynamicTable[numberOfCows][maxWeight]

if __name__ == '__main__':
    main()
