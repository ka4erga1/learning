def main():
    e = []
    r = 0
    q = int(input())
    for i in range(q):
        e.extend(list(map(int, input().split())))
        r += (e[i*2] / 100) * (e[i*2+1] / 100)
    for i in range(q):
        a = ((e[i * 2] / 100) * (e[i * 2 + 1] / 100)) / r
        print(a)

if __name__ == "__main__":
    main()