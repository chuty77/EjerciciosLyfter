def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primer_filter(lista):
    primes = []
    for number in lista:
        if prime_number(number):
            primes.append(number)
    return primes


original_list = [2, 10, 15, 13, 78, 108, 67]
result = primer_filter(original_list)
print(result) 
