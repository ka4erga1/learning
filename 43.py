import sys

def main():
    wd = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    f, s = input().split()
    f = int(f)
    v = [[]]
    for i in range(wd.index(s)):
        v[0].append("..")
    q = 0
    x = 1
    while f != 0:
        if len(v[q]) != 7:
            if x <10:
                v[q].append('.' + str(x))
                x += 1
            else:
                v[q].append(str(x))
                x += 1
            f -= 1
        else:
            v.append([])
            q += 1
            if x <10:
                v[q].append('.' + str(x))
                x += 1
            else:
                v[q].append(str(x))
                x += 1
            f -= 1
    for item in v:
        print(*item)
if __name__ == '__main__':
    main()