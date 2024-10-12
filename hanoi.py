def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print("Moving disk from", fp, "to", tp)

# Initiate the Tower of Hanoi solution with 3 disks
moveTower(3, "A", "B", "C")
