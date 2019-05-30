from primes import iter_primes


def print_primes(number):
    print(f"Primes before {number}")
    for index, prime in enumerate(iter_primes(), start=1):
        if prime > number:
            break
        print(f"  {index}. {prime}")


if __name__ == '__main__':
    print_primes(100)
