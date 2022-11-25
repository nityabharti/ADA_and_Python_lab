# Primality test using Fermat method

#Function to calculate power
def expo(x,n):
    if n==0:
        return 1
    else:
        m = expo(x,n//2)
        if n%2 == 0:
            return m*m
        else:
            return x*m*m
#Function to check is_prime
def is_prime(p):
    a=p-1
    for x in range(2,p-1):
        e=expo(x,p)
        if e%p != 1:
            return False
    return True

num=int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime")