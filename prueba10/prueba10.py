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
    numberCombos = int(sys.stdin.readline())
    comboList = []

    for i in range (numberCombos):
        comboKeys = set(sys.stdin.readline().strip().split(" "))
        comboAction = sys.stdin.readline().strip()
        comboList.append((comboAction, comboKeys))

    numberTests = int(sys.stdin.readline())
    for i in range(numberTests):
        testKeys = set(sys.stdin.readline().strip().split(" "))
        matchingCombos = [combo for combo in comboList if combo[1] == testKeys]
        print matchingCombos[0][0]        

if __name__ == '__main__':
    main()
