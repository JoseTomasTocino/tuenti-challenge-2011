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

ledsPerNumber = [6,2,5,5,4,5,6,4,7,5]

def countLedsPair(p):
    """ Count the on leds for a number """
    ledCount = 0

    pStr = "%02d" % p

    firstDigit = int(pStr[0])
    secondDigit = int(pStr[1])

    ledCount = ledsPerNumber[firstDigit] + ledsPerNumber[secondDigit]

    return ledCount

def countLedsTime(t):
    """ Count the on leds for a given time"""
    ledCount = 0
    
    # We're gonna be working with datetime.time objects

    ledCount += countLedsPair(t.hour)
    ledCount += countLedsPair(t.minute)
    ledCount += countLedsPair(t.second)

    return ledCount

def main():
    for line in sys.stdin:
        secs = int(line)
        currentTime = datetime.datetime(1970,1,1)
        targetTime = currentTime + datetime.timedelta(seconds = secs)

        ledCount = 0
        
        while currentTime <= targetTime:
            ledCount += countLedsTime(currentTime)
            currentTime = currentTime + datetime.timedelta(seconds = 1)

        print ledCount        
        
if __name__ == '__main__':
    main()
    

        
