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
import datetime
import pprint


ledsPerNumber = [6,2,5,5,4,5,6,4,7,5]

ledChangesStr = ["0011111011",
                 "4043245253",
                 "2101222222",
                 "2010112121",
                 "3012023131",
                 "2121101121",
                 "1111100111",
                 "2032123031",
                 "0000000000",
                 "2021012020"]

ledChanges = []

def timeToListNumbers(t):    
    """ Return a list of digits for the given time """
    return map(int, list("%02d%02d%02d" % (t.hour, t.minute, t.second)))

def countLedsPair(p):
    """ Counts how many leds change from one time to another"""
    t1, t2 = p

    # Get list of digits
    numT1 = timeToListNumbers(t1)
    numT2 = timeToListNumbers(t2)

    numChanges = sum(map(lambda x: ledChanges[x[0]][x[1]], zip(numT1, numT2)))
#    print "Changes from", t1, "to", t2, " => ", numChanges
    return numChanges

def main():
    global ledChanges
    ledChanges = [map(int, list(x)) for x in ledChangesStr]

    for line in sys.stdin:
        secs = int(line)
        currentTime = datetime.datetime(1970,1,1)
        targetTime = currentTime + datetime.timedelta(seconds = secs)

        # Initial led count
        ledCount = 36

        timePairs = []
        
        while currentTime < targetTime:
            timePairs.append((currentTime, currentTime + datetime.timedelta(seconds = 1)))
            currentTime = currentTime + datetime.timedelta(seconds = 1)

        for i in timePairs:
            ledCount += countLedsPair(i)

        print ledCount

if __name__ == '__main__':
    main()
                                
        
