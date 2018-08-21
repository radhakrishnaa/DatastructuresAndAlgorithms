import time

def sumOfPrime(n):

    start_time = time.time()
     
    prime = [True for i in range(n+1)]
    p = 2
    sum = 0
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
     
    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            sum += p
    print("--- %s seconds ---" % (time.time() - start_time))
    return sum
 
# driver program
if __name__=='__main__':
    n = int(input("enter n "))
    print "Following is the sum of prime numbers smaller",
    print "than or equal to", n
    s = sumOfPrime(n)
    print(s)
