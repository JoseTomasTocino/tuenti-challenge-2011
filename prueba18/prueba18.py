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
import base64
import pygame

def main():
    for line in sys.stdin:
        line = line.strip()
        
        s = base64.b64decode(line)

        fich = open("temp.png","w")
        fich.write(s)
        fich.close()

        surface = pygame.image.load("temp.png")

        grayRows = []

        # per column processing
        for x in range(surface.get_width()):
            r,g,b,a = surface.get_at((x,0))

            if (r,g,b) == (0,255,0):
                continue

            elif (r,g,b) == (255,0,0):
                continue

            grayRows.append(x)

        message = ""

        for x in grayRows:
            for y in range(surface.get_height()):
                r,g,b,a = surface.get_at((x,y))
                message += chr(r) + chr(g) + chr(b)

	print message
        print str(4271+2746)

if __name__ == '__main__':
    main()
