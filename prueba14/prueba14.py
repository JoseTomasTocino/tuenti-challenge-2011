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
import re
import pygame.image

def main():
    surface = pygame.image.load("trabaja.bmp")    
    surfaceWidth = surface.get_width()

    for line in sys.stdin:
        lineAnalysis = re.match('([RGB])([0-9]+)', line.strip())

        channel = [i for i, x in enumerate(['R', 'G', 'B']) if x == lineAnalysis.group(1)][0]
        vertical = int(lineAnalysis.group(2))
        
        sumPixels = 0
        
        for i in range(surfaceWidth):
            sumPixels += surface.get_at((i, vertical))[channel] 

        print sumPixels + 1
    
if __name__ == '__main__':
    main()
