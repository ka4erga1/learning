import sys
import itertools
import datetime

def main():
    b = []
    flag = "OK"
    for i in range(int(input())):
        a = input().split()
        if a[0] == "APPOINT":
            b.append(a[1:])
            if len(b) == 1:
                print("OK")
            else:
                for pair in itertools.combinations(b, 2):
                    hm1 = pair[0][1]
                    hm2 = pair[1][1]
                    if pair[0][0] == pair[1][0]:
                        vr1 = datetime.datetime.strptime(hm1, "%H:%M")
                        vr2 = datetime.datetime.strptime(hm2, '%H:%M')
                        vr3 = vr1 + datetime.timedelta(minutes=int(pair[0][2]))
                        vr4 = vr2 + datetime.timedelta(minutes=int(pair[1][2]))
                        vr1, vr2 = vr1.strftime('%H:%M'), vr2.strftime('%H:%M')
                        vr3,vr4 = datetime.datetime.strftime(vr3,'%H:%M'), datetime.datetime.strftime(vr4,'%H:%M')
                        if vr1 < vr2 < vr3 or vr2 < vr1 <vr4 or vr1 < vr4 < vr3 or vr2 < vr3 < vr4:
                            flag = "FAIL"
                            break
                        else:
                            flag = "OK"
                if flag == "OK":
                    print(flag)
                else:
                    print(flag)
                    print(*b[len(b)-1][4:])
                    b.pop(len(b)-1)
        elif a[0] == "PRINT":
            b.sort()
            for i in range(len(b)):
                if b[i][0] == a[1] and b[i].count(a[2]) != 0:
                    print(*b[i][1:3],*b[i][4:])

if __name__ == '__main__':
    main()