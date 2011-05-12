
zero_to_twenty = ["zero", "one", "two", "three", "four", "five", "six", "seven",
                 "eight", "nine", "ten", "eleven", "twelve", "thirteen",
                 "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                 "nineteen"]
ten_to_hundred= [None, "ten", "twenty", "thirty", "forty", "fifty", "sixty",
                 "seventy", "eighty", "ninety"]
two_digit_compounds = [None, ]
baseten_postfixes = [None, None, None, "hundred", "thousand"]

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
        'one hundred'
        >>> textual_number(199)
        'one hundred and ninety-nine'
        >>> textual_number(411)
        'four hundred and eleven'
        >>> textual_number(1000)
        'one thousand'
    """
    digits = [int(d) for d in str(n)]
    last_two = digits[-1]
    if len(digits) > 1:
        last_two += 10 * digits[-2]
    # deal with first two digits
    if n == 0:
        s = zero_to_twenty[0]
    elif last_two == 0:
        s = ""
    elif 0 < last_two < 20:
        s = zero_to_twenty[last_two]
    else:
        s = ten_to_hundred[digits[-2]]
        if digits[-1]:
            s += "-" + zero_to_twenty[digits[-1]]
    # deal with third digit
    if n >= 100 and digits[-3]:
        if s:
            s = " and " + s
        s = zero_to_twenty[digits[-3]] + " " + baseten_postfixes[3] + s
    # fourth digit
    if n == 1000:
        s = zero_to_twenty[1] + " " + baseten_postfixes[4]
    return s

if __name__ == "__main__":
    count = 0
    for i in range(1000):
        count += len(textual_number(i+1).replace(" ", "").replace("-", ""))
    print count
