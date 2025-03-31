alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c = "zzz"
def s4et(num, slo, zn, ish):
    if zn == "+":
        for letter in slo:
            b = alf.index(letter) + num
            if b == 26:
                b = 0
            elif b > 25:
                b -= 25
            slo = list(map(lambda x: x.replace(letter, alf[b]), slo))
            slo = "".join(slo)
        if slo in ish:
            print(slo)
        else:
            print(1)
    elif zn == "-":
        for letter in slo:
            b = alf.index(letter) - num
            if b > 25:
                b = abs(b)
            slo = list(map(lambda x: x.replace(letter, alf[b]), slo))
            slo = "".join(slo)
        if slo in ish:
            print(slo)
        else:
            print(1)

s4et(1, list(c), "+", "aaa")

     