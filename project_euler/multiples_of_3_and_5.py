n = 999
num1 = 3
num2 = 5

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def lcm(x, y):
    return (x*y)//gcd(x, y)

def sum(number, n):
    d = n//number
    sum = number * (d * (d+1)) // 2
    return sum

req_sum = sum(num1, n) + sum(num2, n) - sum(lcm(num1, num2), n)

print req_sum



# def sum(n, k):
#     d = n // k
#     return k * (d * (d+1)) // 2
#
# def euler1(n):
#     return sum(n, 3) + sum(n, 5) - sum(n, 15)
#
#
# N = 1000
# x = euler1(N - 1)
# print x
