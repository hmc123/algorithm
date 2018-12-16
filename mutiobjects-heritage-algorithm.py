# muti-genetic-algorithm
# -*- coding:utf-8 -*-

import math
import random

seed_N = int(input("please input init_seed count:"))
tolerance_N= int(input("please input tolenance number:"))  
variate_amount=int(input("please input how many variate in this calculation?"))
variate_bound=[]
for i in range(0,variate_amount):
    lower_bound=int(input("please input lower_bound"+str(i)+":"))
    upper_bound=int(input("please input upper_bound"+str(i)+":"))
    slice_N= (upper_bound-lower_bound)*10**tolerance_N
    bin_N = len(str(bin(slice_N)))-2
    variate_bound.append((lower_bound,upper_bound,slice_N,bin_N))


def fitness_func(x1,x2):
    ##x1 and x2 belong to [lower_bound,upper_bound]
    fx =x1**2+x2**3
    return fx

def translate(bin_x,lower_bound,upper_bound,bin_N):                                   
    ##bin_x shall be a string type, input a binary and retrun a decimal number
    fx = lower_bound+int(str(bin_x),2)*(upper_bound-lower_bound)/(2**bin_N-1)
    return fx

def init_seed(seed_N,variate_amount,variate_bound):                                  
    ##initialization seeds, which size=seed_N 
    seed = []
    for i in range(0,seed_N):
        a =[]
        for j in range(0,variate_amount):
            b=''
            for k in range(0,variate_bound[j][3]):    ##variate[j][3]=bin_N of variate[j]
                b = b+str(random.randint(0,1))
            a.append(b)
        seed.append(a)
    return seed



if __name__=='__main__':
    print(init_seed(seed_N,variate_amount,variate_bound))

