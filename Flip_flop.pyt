def palind(r):
    e = len(r) -1
    s=0
    while(s<0):
        if (r[s] != r[e]):
            return False
        s+=1
        e-=1
    return True


r = (7, 8, 9, 9, 8, 7)

if (palind(r)):
    print("The tuple is Flip-Flop")
else:
    print("Tuple is not Flip-Flop")