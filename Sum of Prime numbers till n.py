#!/usr/bin/env python
# coding: utf-8

# In[1]:


#method:1
    
n=int(input())
prime=[2]
for i in range(3,n+1):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        prime.append(i)
print(sum(prime))


#method:2

n=int(input())

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

s=0 #sum of primes
for i in range(2, n+1):
    if(is_prime(i)):
        s=s+i
print(s)


#method:3

num=int(input())
print(sum(num for num in range(2,n+1)if all(num%i!=0 for i in range(2,num))))


# In[ ]:




