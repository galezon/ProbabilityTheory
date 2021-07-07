from random import randint

def set_doors():
    l = ['g','g','g']
    a = randint(0,2)
    l[a] = 'c'
    return l

def player_first_choice():
    '''
    this code returns an integer that is the player's choice
    '''
    first = randint(0,2)
    return first

def host_show_goat(l,first):
    '''
    this code removes the player's choice(integer) from the possible pool of choices
    '''
    possibilities = [0,1,2]
    possibilities.remove(first)
    '''
    this code is for when the player chose a goat, we want to find out which other door is the goat for the host to return as another integer
    '''
    if l[first] == 'g':
        a = l.index('c')
        possibilities.remove(a)
        return possibilities[0]
    if l[first] == 'c':
        a = randint(0,1)
        return possibilities[a]
        
        

def monty_hall():
    '''
    this code calculates frequency of winning for all choices
    '''
    count_keep = 0
    count_change = 0
    count_same_prob = 0
    i = 0
    while i < 1000:
        poss = [0,1,2]
        l = set_doors()
        first = player_first_choice()
        host = host_show_goat(l,first)
        if l[first] == 'c':
            count_keep += 1
        poss.remove(host)    #remove goat shown by the host, so the elements of the list are for keeping or changing
        a = randint(0,1)
        same = poss[a]
        if l[same] == 'c':
            count_same_prob += 1
        poss.remove(first)    #remove player's first choice, so only element in the list is for changing
        if l[poss[0]] == 'c':
            count_change += 1
        i += 1
    return [count_keep/1000,count_change/1000,count_same_prob/1000]

def main():
    a = monty_hall()
    print("{:37}{:10}{:12}{:12}".format('','Keep Door','Change Door','Same Chance'))
    print("{:37}{:7}{:10}{:13}".format('Relative Frequency (1000 simulations)',a[0],a[1],a[2]))

if __name__ == '__main__':
    main()
