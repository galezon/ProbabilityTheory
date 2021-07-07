import math
import matplotlib.pyplot as plt

dice_prob = [0.35,0.10,0.05,0.05,0.15,0.30]

def sum2(a,b):
    res = create_zeroes(len(a) + len(b))
    i = 1
    j = 1
    for i in range(1 , len(a) + 1 ):
        for j in range(1 , len(b) + 1):
            res[i+j-1] += a[i-1]*b[j-1]
    return res
    
def create_zeroes(length=6):
    zer = [0]
    return zer*length

def sumx(prob,amount):
    if amount == 1:
        return prob
    else:
        count = 2
        a = sum2(prob,prob)
        while count < amount:
            a = sum2(a,prob)
            count += 1
        return a
    
def imp(prob,amount):
    a = sumx(prob,amount)
    avg = 0
    for count in range( len(a)):
        avg += a[count]*(count+1)
    avg2 = 0
    for count in range( len(a)):
        avg2 += a[count]*((count+1)**2)
    var = avg2 - (avg**2)
    return[avg,avg2,var]

def nor_dis(prob,amount):
    a = [i for i in range( 1 , len(sumx(prob,amount)) + 1 )]
    b = imp(prob,amount)
    sd = b[2]**(0.5)
    res = []
    for i in a:
        res.append( (math.pi**(-0.5*( (i - b[0]) / sd )**2 )) / (sd * ((2*math.pi)**0.5) ) )
    return res
    

def main():
    plt.subplots(figsize=(12,15))
    plt.subplot(4,2,1)
    plt.plot([i for i in range(1,6*1 + 1)],sumx(dice_prob,1))
    plt.ylabel('Probability)')
    plt.xlabel('Sum')
    plt.subplot(4,2,2)
    plt.plot([i for i in range(1,6*2 + 1)],sumx(dice_prob,2))
    plt.ylabel('Probability)')
    plt.xlabel('Sum')
    plt.subplot(4,2,3)
    plt.plot([i for i in range(1,6*3 + 1)],sumx(dice_prob,3))
    plt.ylabel('Probability)')
    plt.xlabel('Sum')
    plt.subplot(4,2,4)
    plt.plot([i for i in range(1,6*4 + 1)],sumx(dice_prob,4))
    plt.ylabel('Probability)')
    plt.xlabel('Sum')
    plt.subplot(4,2,(5,6))
    plt.plot([i for i in range(1,6*10 + 1)],sumx(dice_prob,10))
    plt.ylabel('Probability)')
    plt.xlabel('Sum')
    plt.subplot(4,2,(7,8))
    plt.plot([i for i in range(1,6*20 + 1)],sumx(dice_prob,20),[i for i in range(1,6*20 + 1)],nor_dis(dice_prob,20))
    plt.ylabel('Probability)')
    plt.xlabel('Sum')
    plt.suptitle('1,2,3,4,10,20 dices')
    plt.plot()

if __name__ == '__main__':
    main()
