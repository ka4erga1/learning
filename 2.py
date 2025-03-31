import collections

def find_unique_digits(num):
    
    counter = collections.Counter(num)
    
    un = [digit for digit, count in counter.items() if count == 1]
    
    return len(un)


n = int(input())
num = list(map(int, input().split()[0:n]))


print(find_unique_digits(num))