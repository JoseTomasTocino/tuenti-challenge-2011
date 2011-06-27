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
import codecs

def calcPrice(sourceString, targetString, pAdd, pRemove, pSwap):

    numCols = len(sourceString) + 1
    numRows = len(targetString) + 1

    # This is an implementation of the Levenshtein Distance
    distMatrix = [[0 for x in range(numCols)] for y in range(numRows)]

    for i in range(numRows):
        distMatrix[i][0] = i 

    for j in range(numCols):
        distMatrix[0][j] = j 

    for i in range(1, numRows):
        for j in range(1, numCols):
            if sourceString[j - 1] == targetString[i - 1]:
                distMatrix[i][j] = distMatrix[i-1][j-1]
            else:
                distMatrix[i][j] = min(
                    [distMatrix[i - 1][j] + pAdd,
                     distMatrix[i][j - 1] + pRemove,
                     distMatrix[i - 1][j - 1] + pSwap])

    return distMatrix[numRows - 1][numCols - 1]


def main():

    for line in codecs.getreader('utf-8')(sys.stdin):
        lineParts = line.split(" ")
        pAdd, pRemove, pSwap = map(int, lineParts[2].split(","))

        s1 = lineParts[0].strip()
        s2 = lineParts[1].strip()

        print calcPrice(s1,s2, pAdd, pRemove, pSwap)

if __name__ == '__main__':
    main()
