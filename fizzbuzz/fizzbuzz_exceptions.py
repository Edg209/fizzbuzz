class FizzBuzzException(Exception):
    pass

class NegativeIntegerException(FizzBuzzException, ValueError):
    pass

class NonIntegerException(FizzBuzzException, TypeError):
    pass