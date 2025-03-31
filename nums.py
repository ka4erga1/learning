class Solution(object):
    def mergeKLists(self, lists):
        f = len(lists)
        a = 0
        c = []
        g = 0
        b = lists[0][0]
        if f == 0:
            return lists
        elif len(lists[0]) == 0:
            return lists[0]
        while True:
            if b > lists[a][0]:
                b = lists[a][0]
            if a == f - 1:
                for num in lists:
                    d = lists[g].count(b)
                    for i in range(d):
                        c.append(b)
                        lists[g].remove(b)
                        if len(lists[g]) == 0:
                            lists.pop(g)
                            f -= 1
                    g += 1
                a = 0
                if len(lists) == 0:
                    return c
                elif len(lists) == 1:
                    while len(lists[0]) != 0:
                        c.append(lists[0][0])
                        lists[0].pop(0)
                    return c
                b = lists[0][0]
            a += 1
            g = 0

    print(mergeKLists(1, [[1,4,5],[1,3,4],[2,6],[6,9],[1,2]]))