import math

def cb(x,y):
    import math
    if y > x:
        raise ValueError
    a = math.factorial(x) / math.factorial(y)
    b = a / math.factorial(x-y)
    return b

class Drv():
    name = "Discrete random variable"
    def __init__(self,xk=[0],pk=[1]):
        self.xk = xk
        self.pk = pk
        
    def pdf(self,k):
        index = 0
        for i in self.xk:
            if i == k:
                return self.pk[index]
            index += 1
        return 0
        
    def cdf(self,k):
        sum = 0
        index = 0
        while index < k:
            sum += self.pdf(index)
            index += 1
        return sum
    
    def e(self):
        sum = 0
        for i in range(len(self.xk)):
            sum += self.xk[i]*self.pk[i]
        return sum
    
    def is_nonneg(self):
        if min(self.xk) < 0:
            return False
        return True
    
    def reweighting(self):
        self.is_nonneg()
        if max(self.xk) == 0:
            return False
        res = []
        e = self.e()
        for i in range( len(self.xk)):
            res.append(self.xk[i]*self.pk[i]/e)
        return Drv(self.xk,res)
        
    def __repr__(self):
        xk = self.xk
        pk = self.pk
        n = len(xk)
        x = '' . join(['('+str(xk[i]) + ',' + str(pk[i]) + ') '
                      for i in range(min(n, 10))])
        if n > 10:
            x += '...'
        return self.name + ": " + x
        

class Binomial(Drv):
    """
    Class for binomial random variable derives from Drv.
    Parameters needed: n, p.
    """

    name = "Binomial random variable"

    def __init__(self, n=1, p=1):
        self.n = n
        self.p = p
        result = []
        k = 0
        while k <= n:
            result.append(cb(n,k)*(p**k)*((1-p)**(n-k)))
            k += 1
        super().__init__([i for i in range(n+1)], result) # inheritance

    def e(self):
        return self.n*self.p
    def is_nonneg(self):
        return True


class Uniform(Drv):
    """
    Class for a uniform random variable derives from Drv.
    n is the number a values (which are 1,2,...,n).
    """

    name = "Uniform random variable"

    def __init__(self, n=1):
        self.n = n
        super().__init__([i for i in range(1,n+1)], [1/n]*n)

    def e(self):
        """
        Return the expected value of the uniform random variable.
        """
        return (sum(self.xk)/self.n)

    def is_nonneg(self):
        return True

class Geometric(Drv):
    """
    Class for a geometric random variable with infinit values (1, 2, 3,...)
    The parameter p is from the interval [0, 1].
    """
    
    name = "Geometric random variable"
    
    def __init__(self, p=1):
        self.p = p
        self.xk = [k for k in range(1,11)] + ['...']
        res = []
        for i in range(1,11):
            res.append( ( (1-self.p)**(i-1) ) * (self.p) )
        self.pk = res + ['...']
        super().__init__(self.xk,self.pk)

    def pdf(self, x):
        return (( (1-self.p)**(x-1) ) * (self.p) )

    def cdf(self, x):
        i = 1
        sum = 0
        while i < x :
            sum += self.pdf(i)
            i += 1
        return sum
    
    def e(self):
        return 1/self.p
        pass
    
    def is_nonneg(self):
        return True

    def reweighting(self):
        # we do not implement this method
        raise NotImplementedError(
            "reweighting is not implemented for geometric variable!")
