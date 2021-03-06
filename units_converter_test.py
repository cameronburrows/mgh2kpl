"""
Unit tests for MPG to KPL units converter 
"""

# import code to be tested
from units_converter import mpg2kpl


def describe_a_units_converter():
    def that_can_convert_mpg_to_kpl():
        """
        Test the mpg2kpl
        """
        assert mpg2kpl(30) == 12.7543
        assert mpg2kpl(10) == 4.2514
