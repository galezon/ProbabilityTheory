from random import randint

def determine(x):
    '''this code determines who wins/loses/draws for each fight'''
    atk_l = 0
    def_l = 0
    atk = x[0:3]
    deff = x[3:]
    atk.sort()
    deff.sort()
    if atk[-1] > deff[-1]:
        def_l += 1
    else:
        atk_l += 1
    if atk[-2] > deff[-2]:
        def_l += 1
    else:
        atk_l += 1
'''if defender wins'''
    if atk_l > def_l:
        return 0
'''if it's a draw'''
    if atk_l == def_l:
        return 1
'''if attacker wins'''
    if atk_l < def_l:
        return 2
        

def simulate(n):
    '''
    this code simulates (meaning unconsistent result everytime it is run)
    '''
    atk_win = 0
    drw = 0
    deff_win = 0
    for _ in range(n):
        rolls = [randint(1,6),randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
        result = determine(rolls)
        if result == 0:
            deff_win += 1
        elif result == 1:
            drw += 1
        elif result == 2:
            atk_win += 1
    return [atk_win/n,deff_win/n,drw/n]

def probability():
    atk_win = 0
    deff_win = 0
    draw = 0
    counter = 0
    '''generate the sample space'''
    sample_space = ([a,b,c,d,e] for a in range(1,7) for b in range(1,7) for c in range(1,7) for d in range(1,7) for e in range(1,7))
    for i in sample_space:
        result = determine(i)
        if result == 0:
            deff_win += 1
        elif result == 1:
            draw += 1
        elif result == 2:
            atk_win += 1
        counter += 1
    return [atk_win/counter,deff_win/counter,draw/counter]


def main():
    a = simulate(1000)
    b = simulate(1000000)
    c = probability()
    print("{:20}{:9}{:9}{:9}".format('','Attacker','Defender','Draw'))
    print("{:20}{:.5f}{:.5f}{:.5f}".format('1000 experiments',a[0],a[1],a[2]))
    print("{:20}{:.5f}{:.5f}{:.5f}".format('1000000 experiments',b[0],b[1],b[2]))
    print("{:20}{:.5f}{:.5f}{:.5f}".format('Probability',c[0],c[1],c[2]))

if __name__ == "__main__":
    main()
