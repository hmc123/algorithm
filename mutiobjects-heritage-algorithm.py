# muti-genetic-algorithm
# -*- coding:utf-8 -*-

import math
import random


result = []
seed_N = int(input("please input init_seed count:"))
tolerance_N= int(input("please input tolenance number:"))  
variate_amount=int(input("please input how many variate in this calculation ?"))
variate_bound=[]
for i in range(0,variate_amount):
    lower_bound=int(input("please input lower_bound"+str(i)+":"))
    upper_bound=int(input("please input upper_bound"+str(i)+":"))
    slice_N= (upper_bound-lower_bound)*10**tolerance_N
    bin_N = len(str(bin(slice_N)))-2
    #variate_bound.append((lower_bound,upper_bound,slice_N,bin_N))ce_N)))-2
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

##轮盘赌
def roulette(seed):
    ##calculate cumulation probablity of every seed,result will be like this:[]
    # object_values=[]
    # for i in seed:
    #     a=fitness_func(translate(i[0],variate_bound[0][0],variate_bound[0][1],variate_bound[0][3]),translate(i[1],variate_bound[1][0],variate_bound[1][1],variate_bound[1][3]))
    #     object_values.append(a)
    temp=end_judge(seed)
    object_values=temp[0]

    cumulation_probablity=[]
    cumulation = sum(object_values) ##calculate the sum of all the fintness
    b=0
    for j in object_values:
        b=b+j/cumulation  ##calculate cumculation probablity
        cumulation_probablity.append(b)
    
    dad_seed=[]
    for k in range(0,seed_N):
        c=random.random()
        for p in cumulation_probablity:  ## base on random number deciding which seed will be heritaged 
            if c<=p:
                dad_seed.append(seed[cumulation_probablity.index(p)])
                break

    return dad_seed

def intersect(dad_seed):
    son_seed=[]

    couple_pick=list(range(0,seed_N))
    random.shuffle(couple_pick)  ## geting a order present which two neighbor will be couple
    
               
    for i in range(0,seed_N//2):
        son_a=[]
        son_b=[]   
        for j in range(variate_amount):
            bin_N = variate_bound[j][3]
            intersect_point = random.randint(1,bin_N)  ##generate the point that present location of intersection
            a = dad_seed[couple_pick[2*i]][j][0:intersect_point] + dad_seed[couple_pick[2*i+1]][j][intersect_point:bin_N]
            b = dad_seed[couple_pick[2*i+1]][j][0:intersect_point] + dad_seed[couple_pick[2*i]][j][intersect_point:bin_N]
            
            mutation = random.random()  
            if mutation<=0.1:
                x = random.randint(0,bin_N-1)
                if random.randint(0,1)==1:
                    a = a[0:x]+str((int(a[x])+1)%2)+a[x+1:bin_N]
                else:
                    b = b[0:x]+str((int(b[x])+1)%2)+b[x+1:bin_N]
                print("变异出现!!!")
            son_a.append(a)
            son_b.append(b)            
        son_seed.append(son_a)
        son_seed.append(son_b)
    return son_seed

def end_judge(seed):
    global result 
    object_values=[]
    x=[]
    for i in seed:
        xi=[]
        for j in range(variate_amount):
            xi.append(translate(i[j],variate_bound[j][0],variate_bound[j][1],variate_bound[j][3]))
            #xi=[translate(i[0],variate_bound[0][0],variate_bound[0][1],variate_bound[0][3]),translate(i[1],variate_bound[1][0],variate_bound[1][1],variate_bound[1][3])]
        x.append(xi)

        object_values.append(fitness_func(xi[0],xi[1]))
    result = [object_values,x]
    return result




if __name__=='__main__':
    count = 0
    a = init_seed(seed_N,variate_amount,variate_bound)
    
    while count < 1000:
        a = intersect(roulette(a))
        count = count + 1
        print(count,'\n')
    
    print('迭代',count,'次得到解')
    for i in range(len(result[0])):
        #for j in range(variate_amount):
        print(result[1][i],'--->',result[0][i])
