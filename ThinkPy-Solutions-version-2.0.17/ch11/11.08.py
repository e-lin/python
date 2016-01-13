#
# Exercise 8
# Exponentiation of large integers is the basis of common algorithms
# for public-key encryption. Read the Wikipedia page on the RSA algorithm
# (http://en.wikipedia.org/wiki/RSA_(algorithm)) and write functions to
# encode and decode messages.
#
# Reference: http://code.activestate.com/recipes/578838-rsa-a-simple-and-easy-to-read-implementation/
#
def get_primes(start, stop):
    """Return a list of prime numbers in range(start, stop)"""
    if start >= stop:
        return []

    primes = [2]

    for n in range(3, stop+1, 2):
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)

    while primes and primes[0] < start:
        del primes[0]

    return primes


def are_relatively_prime(a, b):
    """Two numbers are relatively prime if they share no comment factors,
    i.e., there is no integers(except 1) that devides both"""
    for n in range(2, min(a,b)+1):
        if a % n == b % n == 0:
            return False
    return True


def make_key_pair(length):
    """Create a public-private key make_key_pair

    The key pair is generated from two random prime numbers. The argument length
    specifies the bit length of the number n shared between the two keys: the
    higherm the better. """

    if length < 4:
        raise ValueError('cannot generate a ley of length less than 4(got {!r})'.format(length)) # !r means repr()

    # 1st step: find a number 'n' which is the product of two numbers p and q.
    # n must have the number of bits specified by 'length', therefore it must
    # be in range(n_min, n_max+1)
    # i.e., for 4 bits length. 1<<(4-1) = 8, whereas (1<<4)-1 = 15. So the range
    # of 4 bits would be 8 to 15.
    n_min = 1 << (length-1)
    n_max = (1 << length) - 1

    # The key is stronger if p and q have similar bit length. We choose two prime numbers
    # in range(start, stop), so that the difference of bit length is at most 2.
    start = 1 << (length // 2 -1) # // means floor division, i.e., 5//2 = 2, 3.5//2 = 1.0
    stop = 1 << (length //2 +1)
    primes = get_primes(start, stop)

    # Now we have a list of prime number candidates, randomly select two so that their
    # product is in range(n_min, n_max+1)




if "__main__" == __name__:
    print make_key_pair(5)

