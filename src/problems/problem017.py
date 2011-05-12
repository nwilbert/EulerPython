
zero_to_twenty = ["zero", "one", "two", "three", "four", "five", "six", "seven",
                 "eight", "nine", "ten", "eleven", "twelve", "thirteen",
                 "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                 "nineteen"]
ten_to_hundred= [None, "ten", "twenty", "thirty", "forty", "fifty", "sixty",
                 "seventy", "eighty", "ninety"]
base_ten = [None, None, "hundred", "thousand"]

def textual_number(n):
    """Return the textual form of the given number.

    Examples:
        >>> textual_number(0)
        'zero'
        >>> textual_number(2)
        'two'
        >>> textual_number(11)
        'eleven'
        >>> textual_number(35)
        'thirty-five'
        >>> textual_number(90)
        'ninety'
        >>> textual_number(100)
        'one-hundred'
        >>> textual_number(199)
        'one-hundred and ninety-nine'
        >>> textual_number(411)
        'four-hundred and eleven'
        >>> textual_number(1000)
        'one-thousand'
        >>> textual_number(1300)
        'one-thousand and three-hundred'
    """
    s = ""
    rest = n
    for exponent in range(len(base_ten),1,-1):
        digit = rest // 10**exponent
        if digit:
            if s:
                s += " and "
            s += zero_to_twenty[digit] + "-" + base_ten[exponent]
        rest %= 10**exponent
    # deal with first two digits
    if s and rest:
        s += " and "
    elif not s and not rest:
        s += zero_to_twenty[0]
    if rest:
        if 0 < rest < 20:
            s += zero_to_twenty[rest]
        else:
            s += ten_to_hundred[rest // 10]
            rest %= 10
            if rest:
                s += "-" + zero_to_twenty[rest]
    return s

if __name__ == "__main__":
    count = 0
    for i in range(1000):
        count += len(textual_number(i+1).replace(" ", "").replace("-", ""))
    print count
