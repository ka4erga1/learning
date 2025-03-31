import sys

def main():
    f = input().split()
    elements = list(map(int,input().split()[:int(f[0])]))
    other = list(map(int, input().split()[:int(f[1])]))
    elements = sorted(elements)
    other = sorted(other, reverse=True)
    a = 0
    for i in range(len(elements) if len(elements) < len(other) else len(other)):
        if int(elements[i]) < int(other[i]):
            a += abs(int(elements[i]) - int(other[i]))
        else:
            break
    print(a)


if __name__ == '__main__':
    main()