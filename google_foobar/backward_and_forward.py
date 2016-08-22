def baseN(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
	return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
	
def answer(n):
    def bases(num):
        start = 2
        while True:
            yield (start, baseN(num, start))
            start += 1
    for base, repr in bases(n):
        if repr == repr[::-1]:
			return base