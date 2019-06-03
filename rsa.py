from random import choice

def generate_primes(limit):
    return [i for i in range(2,limit) if 0 not in [i%j for j in range(2,i)]]

def pick_primes(limit, amount):
    primes = generate_primes(limit)
    output = ()
    for _ in range(amount):
        x = choice(primes)
        while x in output:
            x = choice(primes)
        output += (x,)
    return output

def unique_prime_factors(num):
    return [i for i in generate_primes(num) if num % i == 0]

def have_common_element(arr1, arr2):
    for i in arr1:
        for j in arr2:
            if j == i:
                return True
    return False

def rsa():
    p, q = pick_primes(20, 2)
    print(p, q)
    n = p * q
    phi_prod = (p - 1) * (q - 1)
    c = 3
    # while have_common_element(unique_prime_factors(phi_prod), unique_prime_factors(c)):
    while phi_prod % c == 0:
        c += 2

    return c, n, phi_prod

def encrypt(msg, c, n):
    return msg ** c % n

def decrypt(msg, c, n, phi):
    private_key = 0
    while c * private_key % phi != 1:
        private_key += 1
    print(private_key, "pc")
    return msg ** private_key % n


msg = 10
while True:
    c, n, phi = rsa()
    print(c, n, phi)
    print(encrypt(msg, c, n))
    print(decrypt(msg, c, n, phi))
    print("")