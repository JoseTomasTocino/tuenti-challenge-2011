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

class Parser(object):
    """Parser object for a string. It returns tokens or numbers.
    """
    
    def __init__(self, string):
        self._string = string
        self._index = 0
        
    def __iter__(self):
        return self

    def move(self):
        self._index += 1

    def next(self):
        returnValue = None
        possibleTokens = ['^', '=', '#', '$', '@']

        # If we're too far 
        if self._index >= len(self._string):
            raise StopIteration

        # Quick function to get the current character
        ch = lambda: self._string[self._index]

        # If the current character is a symbol
        if ch() in possibleTokens:

            # Return that symbol
            returnValue = ch()

            # Move to the next character
            self.move()

        # If it's a digit
        elif ch().isdigit():
            
            # Start collecting digits of the number
            numberStr = ch()

            # Move to the next character
            self.move()

            # While we're reading digits
            while ch().isdigit():
                numberStr += ch()
                self.move()

            # Return the whole number
            return int(numberStr)

        # Then, it must be a space or an invalid character
        else:
            # Move to the next character, ignoring it
            self.move()

            # Return the next token
            return self.next()

        return returnValue

class Oper(object):
    """It represents a whole operation, with its type and operands (members)
    """
    
    def __init__(self, operType):
        self._operType = operType
        self._operMembers = []

    def addMember(self, member):
        self._operMembers.append(member)

    def __str__(self):
        s = {"=":"+", "@":"-", "#":"*"}
        if self._operType == "@" and len(self._operMembers) == 1:
            return "- (" + str(self._operMembers[0]) + ")"
        else:
            return "(" + str(self._operMembers[0]) + " " + s[self._operType] + " " + str(self._operMembers[1]) + ")"

    def calc(self):
        memberValues = []

        # Calculate the value of the members
        for member in self._operMembers:
            
            # If it's an operation
            if type(member) is Oper:
                memberValues.append(member.calc())

            # If it's a straight number
            else:
                memberValues.append(member)

        # '=' symbol it's for the sum
        if self._operType == "=":
            return sum(memberValues)

        # '#' symbol is for product
        elif self._operType == "#":
            return reduce(lambda x,y:x*y, memberValues)

        # '@' symbol is for negative single numbers or difference of multiple numbers
        else:
            if len(memberValues) == 1:
                return -memberValues[-1]
            else:
                return reduce(lambda x,y:x-y, memberValues)        

def main():
    """Main function
    """

    for entry in sys.stdin:
        # Strip whitespaces
        entryStr = entry.strip()

        # Check if there's an opening sign for each closing sign
        if entryStr.count("^") != entryStr.count("$"):
            print "BAD ENTRY"
            continue

        # Create new Parser
        parser = Parser(entryStr)

        # Reference to current operation
        currentOper = None

        # Stack of previous operations
        prevOpers = []

        # For each token the parser reads
        for elm in parser:

            # If it's an opening sign
            if elm == "^":

                # If there was an operation loaded, push it into the stack
                if currentOper:
                    prevOpers.append(currentOper)

                # Create new operation for the proper operation type
                currentOper = Oper(parser.next())

            # If it's a closing sign
            elif elm == "$":

                # If there are previous operations in the stack
                if prevOpers:
                    # Add a member the last operation in the stack
                    prevOpers[-1].addMember(currentOper)

                    # Set the current operation to the last one in the stack
                    currentOper = prevOpers.pop()

            # If it's a number
            else:
                # Add it as a member to the current operation
                currentOper.addMember(elm)

        # Print the result of the operation
        print currentOper.calc()

if __name__ == '__main__':
    main()


    
