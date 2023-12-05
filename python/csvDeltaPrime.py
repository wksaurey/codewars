def main():
    primeCount = 100
    primes = [get_prime()]
    for index in range(primeCount):
        primes.append(get_prime(primes[-1]+1))
    print(primes)

# return a prime number greater than or equal to the input
def get_prime(num: int = 2) -> int:
    if is_prime(num):
        return num
    return get_prime(num+1)

# return true if input is prime, false otherwise
def is_prime(num: int) -> bool:
    isPrime = True
    for denom in range(2, num):
        if num%denom == 0:
            isPrime = False
            break
    return isPrime

if __name__ == '__main__':
    main()