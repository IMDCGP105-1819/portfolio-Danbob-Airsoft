def remove_dupes (L1, L2):
    e = 0
    while e < len(L1):
        if L1[e] in L2:
            L1.remove(L1[e])
            e-=1
        print (L1)
        e+=1

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dupes(L1,L2)
