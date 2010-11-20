"""
Base 62 Converter  v1.0
=======================

Takes a base 10 int or long and compresses it, using a 'base62' notation
which is an alphabet of the digits 0-9, the characters a-z and the characters
A-Z (and vice versa).  Can be used for example to reduce the length of or
obfuscate primary key values held in URLs.

Usage:
  >>> from Base62NumericConverter import Base62NumericConverter
  >>> c = Base62NumericConverter()
  >>> c.convert_base10_to_base62(28365423)
  '1V18P'
  >>> c.convert_base62_to_base10('1V18P')
  28365423
  >>> c.convert_base62_to_base10('454Fkjuceh287fy2euhf4f8F')
  685278132068474486425787053445629667052677L
=================

Copyright (c) 2010 Mark Henwood

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import re
class Base62NumericConverter:
    """Converts NUMBERS to and from a 'base62' notation, i.e. uses digits 0 thru 9,
       letters a thru z to denote place values of 10 thru 36, and letters
       A thru Z to denote place values of 37 thru 62.
       
       For example:  1523 (base 10) = 'oz' (base 62)
    """
    
    charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    charset_re = re.compile('^[0-9a-zA-Z]+$')
    
    def convert_base10_to_base62(self, value):
        """Converts an int or long numeric value to 'base62'."""
        
        if value.__class__ != int and value.__class__ != long:
            raise TypeError('Supplied param must be an int or a long')
        
        if value < 0:
            raise ValueError('Supplied param must be positive')
        
        # Special case
        if value == 0:
            return '0'
        
        # Find out number of columns in answer
        current_power = 0
        while (62 ** current_power) <= value:
            current_power = current_power + 1
        
        # We start with one less than that
        column = current_power - 1
        result = ''
        while column >= 0:
            col_value = 62 ** column            
            this_col = value / col_value # returns int or long            
            result = result + self.charset[this_col]            
            value = value - (this_col * col_value)            
            column -= 1
        
        return result
    
    
    def convert_base62_to_base10(self, value):
        """Converts a 'base62' string value to an int or long."""
        
        if value.__class__ != str:
            raise TypeError('Supplied param must be a string')
        
        if not self.charset_re.match(value):
            raise ValueError('Supplied param can only use chars 0-9, a-z and A-Z')
        
        current_power = len(value) - 1
        result = 0
        
        for char in value:
            result += (62 ** current_power) * self.charset.find(char)
            current_power -= 1
        
        return result
    
