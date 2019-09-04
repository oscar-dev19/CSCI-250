'''
A script that simulates the classic towers of hanoi with three rods.
Author: Oscar Lopez.
'''
import sys

def hanoi_towers(n, fromRod, toRod):
    if n == 1:
        print("Move disk from %s to rod %s"%(fromRod, toRod))
        return
    unusedRod = (6 - fromRod - toRod)
    hanoi_towers(n-1, fromRod, unusedRod)
    print("Move disk from %s to rod %s"%(fromRod, toRod))
    hanoi_towers(n-1, unusedRod, toRod)
    return

""" Main Program """


if len(sys.argv) < 4:
    print('''
          ERROR: Must pass in 3 arguments:
          1: number of discs(int)
          2: Initial Rod (int)
          3: Last Rod (int)
          ''')
    sys.exit()
discs = int(sys.argv[1])
initialRod = int(sys.argv[2])
lastRod = int(sys.argv[3])
hanoi_towers(discs,initialRod,lastRod)
