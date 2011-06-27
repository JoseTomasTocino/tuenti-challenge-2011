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

def isPrime(n):

    # Neither 0 nor 1 are primes
    if n < 2:
        return False

    if n == 2: 
        return True    

    if n % 2 == 0:
        return False

    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def isEmirp(n):
    rev_n = int(str(n)[::-1])
    return isPrime(n) and isPrime(rev_n) and n != rev_n

def returnEmirps(n):
    return [elem for elem in range(n) if isEmirp(elem)]

def main():
    for entry in sys.stdin:
        print sum(returnEmirps(int(entry.strip())))

if __name__ == '__main__':
    main()
