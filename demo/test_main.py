from itertools import islice

from primes import iter_primes


def test_primes():
    primes = islice(iter_primes(), 5)
    assert list(primes) == [2, 3, 5, 7, 11]
