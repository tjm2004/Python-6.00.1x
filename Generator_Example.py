def genPrimes():
    prime_list = []
    maybe_prime = 1
    def check_prime(number):
        for prime in prime_list:
            if number % prime == 0:
                return False
        return True
    while True:
        maybe_prime += 1
        if check_prime(maybe_prime):
            prime_list.append(maybe_prime)
            yield maybe_prime
        