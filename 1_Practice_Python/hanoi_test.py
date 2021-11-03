def moveDisk(fp,tp):
    print("Moving disk from",fp,'to',tp)
    for ea in fp:
        tp.append(ea)

def hanoi(num, fromPeg, toPeg, auxPeg):
    if num >= 1:
        hanoi(num-1, fromPeg, auxPeg, toPeg)
        moveDisk(fromPeg, toPeg)
        hanoi(num-1, auxPeg, toPeg, fromPeg)

hanoi(5,[1,2,3,4,5], [], [])
