#heritage arthmetic
# -*- coding: utf-8 -*-
import math
import random

lower_bound=int(input("please input lower_bound:"))
upper_bound=int(input("please input upper_bound:"))
tolerance_N= int(input("please input tolenance number:"))
seed_N = int(input("please input init seed count:"))
slice_N= (upper_bound-lower_bound)*10**tolerance_N
bin_N = len(str(bin(slice_N)))-2

def fitness_func(x):                                     #fitness function
    fx = x+10*math.sin(5*x)+7*math.cos(4*x)
    return fx

def translate(bin_x):                                   #bin_x shall be a string type
    fx = lower_bound+int(str(bin_x),2)*(upper_bound-lower_bound)/(2**bin_N-1)
    return fx

def init_seed(seed_N):                                  #initialization seed
    seed = []
    for i in range(0,seed_N):
        a =''
        for j in range(0,bin_N):
            a = a+str(random.randint(0,1))
        seed.append(a)
    return seed

def sort_select(seed):
    seed_value = []
    for i in seed: 
        seed_value.append((i,fitness_func(translate(i))))
    seed_value=sorted(seed_value,key=lambda x:x[1],reverse = True)   #sorted by fitness value
    n = (seed_N//4)*2                                     #only half of seed_N will be selected
    print(seed_value[0:n])
    return seed_value[0:n]

def end_judge(seed_value):
    sum =0
    for i in range(0,seed_value.__len__()-1):
        sum = sum+abs(seed_value[i][1]-seed_value[i+1][1])
    if sum<=1/10**tolerance_N:
        return True
    else:
        return False



def intersect(seed_value):
    seed=[]
    for p in range(0,seed_value.__len__()):
        seed.append(seed_value[p][0])

    for k in range(0,seed_N-seed_value.__len__()):
        i = random.randint(0,seed_value.__len__()-1)
        j = random.randint(0,seed_value.__len__()-1)
        m = random.randint(1,bin_N)
        n = bin_N-m

        mutation = random.random()
        if mutation>=0.2:
            a = seed_value[i][0][0:m]+seed_value[j][0][m:m+n]
        else:
            a = seed_value[i][0][0:m]+seed_value[j][0][m:m+n]
            x = random.randint(0,bin_N-1)
            a = a[0:x]+str((int(a[x])+1)%2)+a[x+1:m+n]
            print("变异出现!!!")
        seed.append(a)
    return seed

if __name__=='__main__':
    kk=sort_select(init_seed(seed_N))
    count=0
    if end_judge(kk)==True:
        count=count+1
    else:
        while end_judge(kk)==False:
            count=count+1
            kk=sort_select(intersect(kk))
    print('迭代',count,'次得到解','x=',translate(kk[0][0]),' y=',kk[0][1])


    
