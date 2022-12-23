import math

def isPerfectSquare(num):
    s =int(math.sqrt(num))
    return s*s == num

def isFibonacciNumber(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

while True:
    a = input("Enter the number you want to check : ")
    
    if a=="":
        print("No input")
        
        break
    
    else:
        n=int(a)
        if  (isFibonacciNumber(n) == True):
            print(n,"is a fibonacci number.")
        else:
            print(n," is not a fibonacci number.")
