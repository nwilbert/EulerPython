
## combinatorical functions

def factorial(n, stop=1):
    """Factorial of n.

    stop -- Cutoff the factors at this number (default 1).

    Examples:
        >>> factorial(0)
        1
        >>> factorial(2)
        2
        >>> factorial(3)
        6
        >>> factorial(5)
        120
        >>> factorial(5,4)
        5
        >>> factorial(4,2)
        12
    """
    product=1
    while n>stop:
        product*=n
        n-=1
    return product

def choose(n, k):
    """Binomial coefficient 'n choose k'.

    Examples:
        >>> choose(3,1)
        3
        >>> choose(10,3)
        120
    """
    return factorial(n, (n-k)) // factorial(k)


## bit field functions

def get_bit(number, n):
    """Return the nth bit (from the left) of the given integer.

    n can be arbitrarily large.

    Examples:
        >>> get_bit(1, 0)
        1
        >>> get_bit(8, 3)
        1
        >>> get_bit(8, 2)
        0
        >>> get_bit(7, 2)
        1
    """
    return (number >> n) % 2

def count_one_bits(number):
    """Return the number of bits with value 1 in the given number.

    Examples:
        >>> count_one_bits(0)
        0
        >>> count_one_bits(1)
        1
        >>> count_one_bits(3)
        2
        >>> count_one_bits(7)
        3
        >>> count_one_bits(8)
        1
    """
    n = 0
    while number:
        n += number % 2
        number >>= 1
    return n

