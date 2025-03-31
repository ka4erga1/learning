import math
def main():
    for i in range(int(input())):
        e = []
        r = 0
        w = int(input())
        e.extend(list(map(int, input().split())))
        a = w - 1
        s = 0
        q = math.inf
        for i in range(int(math.comb(w, 2))):
            for t in range(r, w - 1):
                if q > e[r] ^ e[t + 1]:
                    q = e[r] ^ e[t + 1]
                s += 1
                if s == a:
                    r += 1
                    a -= 1
                    s = 0

                

        print(q)

if __name__ == '__main__':
    main()