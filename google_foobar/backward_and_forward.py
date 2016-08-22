"""
====================
Backward and forward
====================

The sign outside reads: Name no one man.

"Escape. We must escape." Staring at the locked door of his cage, Beta Rabbit, spy and brilliant mathematician, has a revelation.
"Of course! Name no one man - it's a palindrome! Palindromes are the key to opening this lock!"

To help Beta Rabbit crack the lock, write a function answer(n) which returns the smallest positive integer
base b, at least 2, in which the integer n is a palindrome. The input n will satisfy "0 <= n <= 1000."

"""
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
