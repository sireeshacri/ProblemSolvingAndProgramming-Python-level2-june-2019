# Function to check if number is prime
def PrimeorNot(n):
    flag = 1
    if n == 2:
        return True
    for i in range(2,n//2 + 1):
        if n % i == 0:
            flag = 0
            return False
    if flag == 1:
        return True
    
#n = int(input())
#PrimeorNot(n)


# Is Special Number or not

def SpecialNum(num):
    count = 0
    
    for i in range(1,T+1):
        #count = 0
        if num%i==0:
           
            if isPrime(i):
                count=count+1
    if(count>=pcount):
        return "YES"
    else:
        return "NO"
            
        
def isPrime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if(c==2):
        return True
    else:
        return False
            