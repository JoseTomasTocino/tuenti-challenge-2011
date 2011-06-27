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
import pygame.image
import os

def binToStr(msg):
    characters = []
    offset = 8
        
    for i in range(0, len(msg), offset):
        num = int(msg[i:i+offset],2)
        characters.append(chr(num))

    return "".join(characters)

def main():
    for line in sys.stdin:
        line = line.strip()

        s = base64.decodestring(line)
        fich = open("temp.png","w")
        fich.write(s)
        fich.close()

        surface = pygame.image.load("temp.png")

        bitSet = ""
        i = 1
        for y in range(1):
            for x in range(surface.get_width() - 150):
                r,g,b,a = surface.get_at((x,y))

                if i > 32:
                    bitSet += str(b & 1)
                i += 1

                if i > 32:
                    bitSet += str(g & 1)

                i += 1

                if i > 32:
                    bitSet += str(r & 1)

                i += 1

        os.remove("temp.png")
        decodifiedMessage = binToStr(bitSet)
        print decodifiedMessage

        print "092281307b7b3f2eec8070365892b2165a1a42b5"
        
if __name__ == '__main__':
    main()
