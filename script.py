# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 22:00:57 2019

@author: Utob
"""
"""
import numpy as np
import matplotlib.pyplot as plt
import math
"""
def collatz (n):
     
     int(n)
     if n == 1:
          print("1")
          return 0
     else:
          print(str(int(n)))
          if n % 2 == 0:
               n = n / 2
          else:
               n = (n*3 + 1)
          collatz(n)

def collatz_counter (n):
     
     int(n)
     count = 0
     while n != 1:
          if n % 2 == 0:
               n = n / 2
          else:
               n = (n*3 + 1)/2
          count += 1
     return count

def prime_check (n):
     int (n)
     i = 2
     while i < n/2:
          if n % i == 0:
               return False
          i += 1
     return True

def collatz_loop_checker(x,y,n):
     """
     this program takes in x and y in the form of x * n + y and finds loops in their collatz 
     iteration up to a given n
     """
     int(x)
     int(y)
     int(n)
     test = list(range(3,n))
     loop_index = list()
     if (x + y) % 2 != 0 or x == y:
          return "these two numbers dont form a collatz pair"
     for num in test:
          i = num
          result = list()
          for j in range(1,500):
               result.append(int(i))
               if i % 2 == 0:
                    i = i / 2
               else:
                    i = x * i + y
               if i == 1:
                    break
               if j == 99 and i > 2:
                    loop_index.append([str(num) + " exhausted the search range"])
                    break
               if int(i) in result:
                    result.append(int(i))
                    loop_index.append(result[result.index(i):])
                    break
     return loop_index

def custom_collatz (x, y, n):
     int(x)
     int(y)
     int(n)
     if n == 1:
          print("1")
          return 0
     else:
          print(str(int(n)))
          if n % 2 == 0:
               n = n / 2
          else:
               n = (n * x + y)
          custom_collatz(x, y, n)

def prime_factorisation (n):
     factors = list()
     while n != 1:
          for i in range (2,n+1):
               count = 0
               while n % i == 0:
                    count += 1
                    n /= i
               if count != 0:
                    factors.append([i,count])
     return factors

def oddcollatz (n):
     
     int(n)
     if n == 1:
          print("1")
          return 1
     else:
          if n % 2 == 0:
               n = n / 2
          else:
               print(str(int(n)))
               n = (n*3 + 1)
          oddcollatz(n)
     
def ot_calc (n):
     int(n)
     ot = prime_factorisation(n)
     if ot[0][0] == 2:
          ot = ot[1:]
     numtype = 0
     numorder = 0
     for i in range(0,len(ot)):
          numtype += 1
          numorder += ot[i][1]
     return [numtype , numorder]
          
def oddcollatz_counter (n):
     
     int(n)
     count = 0
     while n != 1:
          if n % 2 == 0:
               n = n / 2
          else:
               n = (n*3 + 1)/2
               count += 1
     return count

def heads_or_tails (n):
     """
     this program outputs turn left for every division event and
     turn right for every mul. event
     """
     int(n)
     while n != 1:
          if n % 2 == 0:
               n = n / 2
               print(str(n)+"  : turn left")
          else:
               n = (n*3 + 1)
               print(str(n)+"  : turn right")

heads_or_tails(27)
     







"""
pelimewow = list()
x = list(range(3, 2500, 2))

AT = list()
IJ = list()
average = 0
totalnumbers = 0
for i in range(1,100):
     for j in range(i, 100):
          AT.append([0, 0])
          IJ.append([i,j])

for k in x:
     print(str(k) + " : " + str(ot_calc(k)) + " : " + str(oddcollatz_counter(k)))
     y = IJ.index(ot_calc(k))
     AT[y][0] += 1
     AT[y][1] += oddcollatz_counter(k)

print("*"*50)
print("*"*50)

for i in AT:
     if i != [0,0]:
          y = AT.index(i)
          print(IJ[y], end = " : ")
          print(i, end = " : ")
          print(i[1]/i[0])
          if i[0] > 100:
               plt.bar(str(IJ[y]) +", " + str(i[0]),i[1]/i[0])
plt.xlabel('type and order')
plt.ylabel('average stoppage time')
plt.title("average stoppage time for different orders and types")
plt.show()
print("*"*50)
print("*"*50)

for i in range(1,13):
     for j in range(i, 15):
          average = 0
          totalnumbers = 0
          for k in x:
                    if ot_calc(k) == [i,j]:
                         print(str(k) + " : " + str(ot_calc(k)) + " : " + str(oddcollatz_counter(k)))
                         totalnumbers += 1
                         average += oddcollatz_counter(k)
                         x.remove(k)
                    else:
                         print(str(k) + " : " + str(ot_calc(k)) + "NOPE")
          if totalnumbers != 0:
               pelimewow.append([[i , j] , totalnumbers, average/totalnumbers])

for i in pelimewow:
     print(i)
     plt.bar(str(i[0]),i[2])
plt.xlabel('type and order')
plt.ylabel('average stoppage time')
plt.title("average stoppage time for different orders and types")
plt.show()






file = open('C:\\Users\\Utob\\Desktop\\Text Files\\allprimes.txt','r')

for i in x:
     num = file.readline()
     num = num.split()
     y = int(num[0])
     print(i)
     plt.plot(y,collatz_counter(y), 'bo')

plt.xlabel('number')
plt.ylabel('no. of iterations')

plt.title("Iterations to reach 1, primes in red")

plt.show()
"""
