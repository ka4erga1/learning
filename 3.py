import math
def main():
    l = 0
    a,b = map(int, input().split())
    if b < a:
        a, b = b, a
    n = b / a
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(int(n // i))
    
    if int(len(divisors)) % 2 == 0:
        g = int(len(divisors)/2)
    else:
        g =int(len(divisors))
    for i in range(int(g)):
        c = 0
        if math.gcd(divisors[i*2]*a,divisors[i*2+1]*a) == a:
            c += 1
        if math.lcm(divisors[i*2]*a,divisors[i*2+1]*a) == b:
            c += 1
        if c == 2:
            l += 1
    return print(l*2)


if __name__ == '__main__':
    main()