from nose.tools import raises, with_setup

from Base62NumericConverter import Base62NumericConverter

def setup():
    global converter
    converter = Base62NumericConverter()

@with_setup(setup)
def test_base10_to_base62():
    assert converter.convert_base10_to_base62(0) == '0'
    assert converter.convert_base10_to_base62(28365423) == '1V18P'

@with_setup(setup)
def test_base62_to_base10():
    assert converter.convert_base62_to_base10('0') == 0
    assert converter.convert_base62_to_base10('AAb') == 140627
    
@with_setup(setup)
def test_equivalence():
    for base10 in (1, 10, 432, 47685768):
        base62 = converter.convert_base10_to_base62(base10)
        assert converter.convert_base62_to_base10(base62) == base10

@raises(TypeError)
@with_setup(setup)
def test_typeerror_string():
    """base10 -> base62 must reject strings."""
    converter.convert_base10_to_base62('fail')

@raises(TypeError)
@with_setup(setup)
def test_typeerror_float():
    """base10 -> base62 must reject floats."""
    converter.convert_base10_to_base62(1.2)

@raises(ValueError)
@with_setup(setup)
def test_sign():
    """base10 -> base62 must reject negative numbers."""

    converter.convert_base10_to_base62(-10)
    