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

from fordFulkerson import * 

def main():
    for line in sys.stdin:        
        line = line.strip()
        
        lineParts = line.split(" ")
        numberOfStations = int(lineParts[0])
        originStation = lineParts[1]
        targetStation = lineParts[2]

        network = FlowNetwork()
        stationSet = set()

        for i in range(3, len(lineParts)):
            roadParts = lineParts[i].split(",")
            stationSet.add(roadParts[0])
            stationSet.add(roadParts[1])

        for s in stationSet:
            network.add_vertex(s)

        for i in range(3, len(lineParts)):
            roadParts = lineParts[i].split(",")
            network.add_edge(roadParts[0], roadParts[1], int(roadParts[2]))

        print network.max_flow(originStation, targetStation)

if __name__ == '__main__':
    main()
