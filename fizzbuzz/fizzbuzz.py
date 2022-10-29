from collections import OrderedDict


from fizzbuzz.fizzbuzz_exceptions import NegativeIntegerException, NonIntegerException
class FizzBuzzGenerator(object):

    def __init__(self, replacements: OrderedDict = None):
        """
        Construct a generator that will return FizzBuzz terms. Takes as input a dictionary of replacements with
        integers as keys and strings as values. Positive integers are generated, starting with 1. For each key in the
        dictionary of replacements, the value of that key is returned if the integer is a multiple of the key. If the
        integer is a multiple of multiple keys, the string is the relevant values concatenated in the order of the
        keys in the dictionary. If the integer is not a multiple of any keys, the string representation of the
        integer is returned instead.

        :param replacements: OrderedDict of which numbers to replace with letters. Defaults to {3:'Fizz', 5:'Buzz'}.
        """
        for k in replacements.keys():
            if k != int(k):
                raise NonIntegerException
            if k < 1:
                raise NegativeIntegerException
        self._replacements = replacements
        self._position = 0
