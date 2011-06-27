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
from Crypto.Cipher import DES
import pyDes
import operator

class bcolors:
    ROJO = '\033[01;31m'
    VERDE = '\033[01;32m'
    AZUL = '\033[01;34m'
    AMARILLO = '\033[01;33m'
    ENDC = '\033[0m'

def offsetStr(s, offs):
    acc = ""
    for c in s:
        c1 = (ord(c) + offs) % 256
        acc += chr(c1)
        
    return acc

def binToStr(msg):
    characters = []
    offset = 8
    
    for i in range(0, len(msg), offset):
        num = int(msg[i:i+offset],2)
        characters.append(chr(num))

    return "".join(characters)

def strToBin(msg):
    characters = list(msg)
    target = ""
    for char in characters:
        target += "%08d" % int(bin(ord(char))[2:])

    assert len(target) % 8 == 0
    return target

def charFreq(msg):
    f = {}
    for c in msg:
        if c not in f:
            f[c] = 0
        f[c] += 1

    return f

def printable(c):    
    if ord(c) > 31 and ord(c) < 127:
        return c
    else:
        return " "

from itertools import izip, cycle

def xor_crypt_string(data, key):
    salida = ""
    keyPos = 0

    avance = 0
    for i,c in enumerate(data):
        avance = ord(c)
        salida += chr(ord(c) ^ ord(key[keyPos]))
        keyPos += avance
        keyPos %= len(key)
    
    return salida
    #return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))



def xor_string(data, key):
    target = ""
    for i in range(0, len(data), 8):
        target += xor_crypt_string(data[i:i+8], key)

    return target

def pStr(msg):
    if len([x for x in map(ord, list(msg)) if x < 32 or x > 126]) == 0:
        return True
    else:
        return False

def pBin(msg):
    f = ""
    for i,c in enumerate(msg):
        f += c
        if (i+1) % 8 == 0:
            f += " "
    print f

def complemento_uno(s):
    salida = ""
    for i in range(0, len(s), 8):
        fragmento = s[i:i+8]
        nuevoFragmento = ""

        while fragmento[0] == "0":
            fragmento = fragmento[1:]

        for c in fragmento:
            nuevoFragmento += "0" if c == "1" else "1"

        while len(nuevoFragmento) != 8:
            nuevoFragmento = "0" + nuevoFragmento
    
        salida = salida + nuevoFragmento

    return salida

        

################################333################################################################################
################################333################################################################################
def main():
    for line in sys.stdin:
        line = line.strip()

        debug = True
        printWeirdos = False
        usePyCrypto = True

        if debug:
            print
            print bcolors.ROJO + "## After loading" + bcolors.ENDC
            print line
            print

        s1 = base64.decodestring(line)

        if debug:
            print bcolors.ROJO + "## After base64-decoding" + bcolors.ENDC
            print bcolors.AZUL + str(len(s1)) + " characters" + bcolors.ENDC
            if pStr(s1):
                print s1
            else:
                print "Not printed"
            print
        
        possiblePasswords = []
        possiblePasswords = ["tuenti\0\0"]
        
        for pid, us in enumerate(possiblePasswords):
            
            xor_us = "tuenti"

            print bcolors.AMARILLO + 'Using password "' + us + '" ' + str(pid) + bcolors.ENDC

            ###############################
            ## DES DECIPHER

            #obj = DES.new(us, DES.MODE_ECB)
            obj = pyDes.des(us, pyDes.ECB)
            s2 = obj.decrypt(s1)

            if debug:
                print bcolors.ROJO + "## After DES deciphering" + bcolors.ENDC
                print bcolors.AZUL + str(len(s2)) + " characters" + bcolors.ENDC
                if pStr(s2):
                    print s2
                else:
                    print "Not printed"
                print

            # Cadena a binario
            s3 = strToBin(s2)

            pBin(s3)
            

            # Complemento a uno
            s4 = complemento_uno(s3)


            if debug:
                print bcolors.ROJO + "## After one's complement - binary" + bcolors.ENDC
                print bcolors.AZUL + str(len(s4)) + " characters" + bcolors.ENDC        
                if pStr(s4):
                    pBin(s4)
                else:
                    print "Not printed"                        
                print

            # Binario a cadena
            s5 = binToStr(s4)

            if debug:
                print bcolors.ROJO + "## After one's complement - string" + bcolors.ENDC
                print bcolors.AZUL + str(len(s5)) + " characters" + bcolors.ENDC        
                if pStr(s5):
                    print s5
                else:
                    print "Not printed"
                print

            #################################
            ## XOR
            print "STRING TO XOR"
            print ">" , map(str, map(ord, s5)) , "<"
            s6 = xor_crypt_string(s5, xor_us)

            if debug:
                print bcolors.ROJO + "## After xor decryption" + bcolors.ENDC
                print bcolors.AZUL + str(len(s6)) + " characters" + bcolors.ENDC
                if not pStr(s6):
                    print s6
                else:
                    print "Not printed"
                print

            ff = charFreq(s6)
            sorted_x = sorted(ff.iteritems(), key=operator.itemgetter(1))

            print "Min char:", min(map(ord, s6))
            print "Max char:", max(map(ord, s6))

            for i in xrange(96):
                print bcolors.VERDE + "Offset: ", i , bcolors.ENDC
                string = map(lambda x: ((ord(x) + i - 32) % 96) + 32, s6)
                print ''.join(map(chr,string))
               
if __name__ == '__main__':
    main()
