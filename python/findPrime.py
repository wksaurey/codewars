from typing import List
from datetime import datetime

def find_primes_sextuplet(sum_limit: int) -> List[int]:
    p = 2
    deltaNums = [0, 4, 6, 10, 12, 16]
    result = []
    while(True):
        result = []
        for index in range(len(deltaNums)):
            if is_prime(p+deltaNums[index]):
                result.append(p+deltaNums[index])
            else:
                break
            if len(result) == len(deltaNums):
                print(result)
                if(sum_of(result) >= sum_limit):
                    return result
                else:
                    break
        p = get_prime(p+1)
        print(p, end='\r')

def sum_of(values: List[int]) -> int:
    result = 0
    for value in values:
        result += value
    return result

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


start = datetime.now()
print(find_primes_sextuplet(2000000))
end = datetime.now()
print(f'Program run in {end-start}')