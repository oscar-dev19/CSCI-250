'''
A script that simulates the classic towers of hanoi with three rods.
Author: Oscar Lopez.
'''
import sys

def hanoi_towers(n, fromRod = 1, toRod = 3):
    if n == 1:
        print("Move disk from %s to rod %s"%(fromRod, toRod))
        return
    unusedRod = (6 - fromRod - toRod)
    hanoi_towers(n-1, fromRod, unusedRod)
    print("Move disk from %s to rod %s"%(fromRod, toRod))
    hanoi_towers(n-1, unusedRod, toRod)
    return

""" Main Program """


if len(sys.argv) < 2:
    print('''
          ERROR: Must pass in 1 argument:
          1: number of discs in the towers of hanoi.
          ''')
    sys.exit()
discs = int(sys.argv[1])
hanoi_towers(discs)
