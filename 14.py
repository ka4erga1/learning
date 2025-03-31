import sys
alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():

    b = input().split()
    for i in range(int(input())):
        c = input()
        for _ in range(len(b)):
            p = 0
            n = alf.index(list(c)[0])
            m = n
            if len(b[_]) == len(c):
                if c in b:
                    print(c)
                    break
                else:
                    while p != 14:
                        if list(b)[_][0] == alf[n]:
                            j = s4et(p, list(c), "+", b[_])
                            break
                        elif list(b)[_][0] == alf[m]:
                            j = s4et(p, list(c), "-", b[_])
                            break
                        p += 1
                        n += 1
                        if n > 25:
                            n = 0
                        m -= 1
                        if m < 0:
                            m = 25
                    if j != None:
                        print(j)
                        break

def s4et(num, slo, zn, ish):
    if zn == "+":
        for letter in slo:
            b = alf.index(letter) + num
            if b == 26:
                b = 0
            elif b > 26:
                b -= 26
            slo = list(map(lambda x: x.replace(letter, alf[b]), slo))
            slo = "".join(slo)
            if slo in ish:
                break
        if slo in ish:
            return slo
        else:
            return None
    elif zn == "-":
        for letter in slo:
            b = alf.index(letter) - num
            if b < 0:
                b = 26 - abs(b)
            slo = list(map(lambda x: x.replace(letter, alf[b]), slo))
            slo = "".join(slo)
        if slo in ish:
            return slo
        else:
            return None

if __name__ == '__main__':
    main()