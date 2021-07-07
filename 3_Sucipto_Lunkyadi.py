from itertools import product
from random import randint
'''
here 0 == head, 1 == tail
'''
def petersburg(m):
    total = 0 #total winnings
    counter = 1 #how many tosses until we get a tail (we always start with 1, can't get a tail with 0 tosses)
    tails = 0 #how many tails we had
    while tails < m:
        b = randint(0,1)
        if b == 0:
            counter += 1
        else:
            total += 2**counter
            counter = 1
            tails += 1
    return total/m



def main():
    print("{:20}{:9}".format('','Average Payout ($)'))
    print("{:20}{:.3f}".format('100 experiments',petersburg(100)))
    print("{:20}{:.3f}".format('10000 experiments',petersburg(10000)))
    print("{:20}{:.3f}".format('1000000 experiments',petersburg(1000000)))
    
if __name__ == '__main__':
    main()