from sys import maxsize

#def fibonacci(n):

 #   if n == 1:
  #      return 1
   # elif n == 2:
    #elif n > 2:
     #   return fibonacci(n - 1) + fibonacci(n - 2)
#
#for i in range(1,11):
 #   print(i,";", fibonacci(i))
#optimizing the code
#creating  a dictionary it contains {key: value}
cache = {}

value = 0 #variable

def fib2(n):
    if n in cache:
        return cache[n] #return position in cache
    if n == 1 or n == 2: #base case
        value = 1
    elif n >2:
        value = fib2(n-1) + fib2(n-2)

    cache[n] = value

    return value

#for i in range (1,500):
 #   print(f"{i} Term: { fib2(i)}")

from functools import lru_cache
#L -> last
#R -> Recently
#u -> used
@lru_cache(maxsize=1000) #decorating using overload
def fib1(n):

    if n == 1 or n == 2 :
        return 1
    elif n > 2:
        return fib1(n-1) + fib1(n-2)

for i in range (1,10000):
    print(i,":",fib1(i))