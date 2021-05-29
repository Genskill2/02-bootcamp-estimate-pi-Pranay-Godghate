import math
import unittest
import random  

def wallis(n): #declaring wallis function
    pi=1
    for i in range(1,n): #loop which works n times
        pi*=(4*n*n)/(4*n*n-1) #wallis formula 
    return (2*pi)
def monte_carlo(n):
    c=0
    for i in range(1,n): 
        x=random.random() #this will generate a random value between [0,1)
        y=random.random() #this will generate a random value between [0,1)
        dist=math.sqrt(math.pow(x,2)+math.pow(y,2)) #gives distance between point(0,0) and (x,Y)
        if dist<1:
            c=c+1 #to count number of darts in circle
    pi=(4*c)/n
    return pi
    

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()

