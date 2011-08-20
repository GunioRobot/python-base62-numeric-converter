Base 62 Converter  v1.0
=======================

Takes a base 10 int or long and compresses it, using a 'base62' notation
which is an alphabet of the digits 0-9, the characters a-z and the characters
A-Z (and vice versa).  Can be used for example to reduce the length of or
obfuscate primary key values held in URLs.

Usage::

  >>> from Base62NumericConverter import Base62NumericConverter
  >>> c = Base62NumericConverter()
  >>> c.convert_base10_to_base62(28365423)
  '1V18P'
  >>> c.convert_base62_to_base10('1V18P')
  28365423
  >>> c.convert_base62_to_base10('454Fkjuceh287fy2euhf4f8F')
  685278132068474486425787053445629667052677L
