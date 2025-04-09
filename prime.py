# num=int(input("enter n number "))
# c=1
# for i in range(2,num):
#     if(num%i==0):
#         c=0
#         break
# if(c):
#     print("the given number is prime")
# else:
#     print("the given number not a prime")

# duplicate remove
# def rem_duplicate(num):
#     result=''
#     dup=''
#     for i in num:
#         if i not in result:
#             result+=i
#         else:
#             dup+=i

#     return result,dup
# str=input("enter number or string ")
# without_dup,dup=rem_duplicate(str)
# print("without_duplicate",without_dup)
# print("duplicated values",dup)

# # data types
# name='madhu'
# lst=[1,2,3,4,5]
# set1={1,2,3,4,5}
# tuple1=(1,2,3,4,5)
# num=123
# flt=123.4
# comp=(3+2j)
# dict1={'a':1,'b':2,'c':3}
# print(name,type(name))
# print(lst,type(lst))
# print(set1,type(set1))
# print(tuple1,type(tuple1))
# print(num,type(num))
# print(flt,type(flt))
# print(comp,type(comp))
# print(dict1,type(dict1))

# # even or not
# num=int(input('enter a number'))
# if(num%2):
#     print("the given number is odd")
# else:
#     print("the given number is even")

# # operatators
# a,b=10,20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)

# # bitwise operaters
# a=10
# b=4
# print(a&b)
# print(a|b)
# print(a^b)
# print(a>>b)
# print(a<<b)

# # while loop
# num=''
# while(num!='madhu'):
#     num=input("enter valid user")

# num=[1,2,5,7,3,4,9]
# for i in range(len(num)):
#     for j in range(i+1,len(num)):
#         print("is" ,num[j] ,"is garater then",num[i],num[j]>num[i])

# list
# lst=[1,2,3,4,]
# lst2=['car','bus','trin']
# print(lst)
# lst.append(12)
# print(lst)
# print(lst.count(3))
# lst.extend(lst2)
# print(lst)
# print(lst.index(3))
# lst.insert(4,35)
# print("ofter insert",lst)
# print(lst.pop(4)) 
# print(lst.remove(3),lst)
# lst.reverse()
# print(lst)
# lst.sort(reverse=True)
# # print(lst)        
# print(max(lst))
# print(min(lst))
# print(sum(lst))
# print(sum(lst))
# ls1=[x*2 for x in lst]
# print(ls1)



# # feb series
# n=int(input("enter a number"))
# a,b=0,1
# for i in range(1,n):
#     print(a)
#     c=a+b
#     a=b
#     b=c

# arr=[7,6,5,7,3,6,7]
# dec=dict()
# for j in arr:
#     c=0
#     for i in arr:
#         if i==j :
#             c+=1
        
#     if(i>1):
#         print('duplicated number is',j,'no of times',c)
# count dblicate numbers in array

# arr = [2, 3, 2, 4, 5, 3, 3]
# dec={}

# for num in arr:
#     count = 0  
#     for val in arr:
#         if num == val:
#             count += 1
#     if count>1:
#         dec[num]=count
    
#     # if count > 1:  # Only print if it's a duplicate
#     #     print(num, "appears", count, "times")
# print(dec)


# # patterns:
# num=5
# def pattern(num):
#     for i in range(num,0,-1):
#         for j in range(i):
#             print("*",end=' ')
#         print("\n")
# pattern(num)
# # *****
# ****
# ***
# **
# *


# c=0
# for i in range(9,0,-2):
#     c+=1
#     print(c*' ',i*"*",c*" ")
#     *
#    ***
#   *****
#  *******
# *********
# num=int(input("enter a number"))
# def pat(num):
#     for i in range(1,num+1):
#         print("*"*i)
# pat(num)
# *
# **
# ***
# ****
# *****
# lst=list()
# num=int(input("enter number"))
# def feb(num):
#     a,b=0,1
#     for i in range(1,num):
#         lst.append(a)
#         c=a+b
#         a=b
#         b=c

# feb(num)
# print(lst)

# num=input("enter string of numbers")
# odd=0
# even=0
# for i in num:
#     if(i%2):
#         odd+=int(i)
#     else:
#         even+=int(i)
# print('even sum',even)
# print("odd sum",odd)
# print("difference",(even-odd))

# lst=['!','@','#','$','%']
# c=0
# for i in range(5):
#     for j in range(5):
#         if(i==j):
#             print(lst[c],end="")
#             c+=1
#         else:
#             print("*" ,end=" ")
#     print()
# !* * * * 
# * @* * * 
# * * #* *
# * * * $*
# * * * * %

# n=int(input("enter number"))
# c=0
# for i in range(1,n):
#     for j in range(i):
#         c=c+1
#         print(c,end="    ")
# #     print()
# #     enter number5
# # 1    
# # 2    3
# # 4    5    6
# # 7    8    9    10

# n=10
# c=n//2
# for i in range(1,n,2):
#     c=c-1
#     print(c*" ",i*"*",end=" ")
#     print()

#      * 
#     ***
#    *****
#   *******
#  *********

# n=5
# for i in range(1,n+1):
#     c=n-i
#     print(c*" ",end="")
#     for j in range(1,i+1):
#         print(j ,end="")
#     print()

#     1
#    12
#   123
#  1234
# 12345

# n=int(input("enter a even  number"))
# c=n//2
# for i  in range(1,n,2):
#     c-=1
#     print(c*' ',i*'*')
# for i in range(n-1,0,-2):
#     print(c*' ',i*"*")
#     c=c+1
#    *
#     ***
#    *****
#   *******
#  *********
#  *********
#   *******
#    *****
#     ***
#      *

# ------------------------------------------------------------------------------------------------------

# name=input("enter string")
# dec1=dict()
# for n in name:
#     if n.isalpha():
#         ask=int(ord(n))
#     if(ask>=65 and ask<=91):
#         # print(n,'is',ask-64)
#         dec1[n]=ask-64
#     elif(ask>=97 and ask<=123):
#         # print(n,'is',ask-96)
#         dec1[n]=ask-96
#     else:
#         print()
# print(dec1)
# {'M': 13, 'a': 1, 'd': 4, 'h': 8, 'u': 21}


# for i in range(1,27)

# string='abcdefghijklmnopqrstuvwxyz'
# c=0
# dec=dict()
# for i in string:
#     c+=1
#     dec[i]=int(c)
# print(dec)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
# 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 
# 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

# num=5
# def pattern(n):
#     for i in range(1,n+1):
#         c=1
#         for j in range(1,i+1):
    
#             if(j%2==0):
#                 print(chr(96+j) ,end=' ')
#             else:
#                 print(chr(64+c), end=' ')
#                 c=c+2
                
#         print()
# # pattern(num)
# A 
# A b
# A b C 
# A b C d
# A b C d E



'''def pattern(n):
    c=n//2
    b=1
    for i in range(1,n+1,2):
        if(i==1):
            c-=1
            print(c*" ",i*"*",)
        elif(i==n-1):
            print(c*' ',i*"*" )
        else:
            c-=1
            print(c*" ","*",b*" ","*",)
            b+=2         
            
pattern(10)'''

#       *
#     *   *
#    *     *
#   *       *
#   *********

# # removing duplicates in list
# lst=[1,2,3,4,5,6,1,2,3,4,5,6]
# dup=set(lst)
# print(dup)


# var='I am Iron Man'
# print(var)
# upper_count=0
# lower_count=0
# set1=set(var.replace(" ",""))
# print(set1,type(set1))
# for i in set1:
#     if (i==i.upper()):
#         upper_count+=1
#     else:
#         lower_count+=1

# if(upper_count>lower_count):
#     print("upper coiunt",upper_count) 
# else:
#     print("lower",lower_count)
        
# {'a', 'M', 'm', 'r', 'n', 'o', 'I'} <class 'set'>
# lower 5

# str1=input("enter a string mix of upper and lower").replace(' ','')
# vol=['A','E','I','O','U','a','e','i','o','u']
# c=0
# non=0
# set1=set(str1)    #to remove duplicates list converted to set
# for i in set1:
#         if i in vol:
#             c+=1
#             print(i,c)
#         else:
#             non=non+1
#             print("non",i,non)

# if(c>non):
#     print("vowels are mor then constents",c)
# else:
#     print("constents more then vowels",non,'>',c,'is',non)
# # enter a string mix of upper and lowerMAdhu Maragani
# # constents more then vowels 6 > 4 is 6
# WRITE A PROG TO MERGE TWO DICTONARYS
# dict1={'name':'Madhu','branch':'CSE','year':'IV'}
# dict={'age':21,'yoj':2021}
# for var in dict:
#     dict1[var]=dict[var]
# print(dict1)
# {'name': 'Madhu', 'branch': 'CSE', 'year': 'IV', 'age': 21, 'yoj': 2021}

# write a prog to store on dic values in other dict keys and it's values are len of key
# dict1={'name':'Madhu','branch':'CSE','year':'IV'}
# dec=dict()

# for var in dict1:
#     le=len(var)
#     dec[var]=le
# print(dec)


# let try t print dimenod

# num=int(input("enter a number"))

# def dimend(n):
#     if(n%2):     #input shoud be even
#         n=n+1
#     outer_space=n//2
#     inner_space=1
#     for i in range(1,n,2):
#         if(i==1):
#             outer_space-=1
#             print(outer_space*' ',i*'*')
#         # elif(i==n-1):
#         #     outer_space-=1
#         #     print(outer_space*" ",i*'*')
#         else:
#             outer_space-=1
#             print(outer_space*" ","*",inner_space*" ",'*')
#             inner_space+=2
#     n=n-2
#     for j in range(n,0,-2):
#         outer_space+=1
#         inner_space-=2
#         if(j==1):
#             print(outer_space*" ","*")
#             outer_space+=1
#         else:
#             print(outer_space*" ","*",inner_space*" ","*")

        
            
# dimend(num)


# # feb series
# n=int(input("enter a number"))
# lst=list()
# a,b=0,1
# for i in range(n):
#     lst.append(a)
#     c=a+b
#     a=b
#     b=c

# print(lst)
# c=0
# for i in range(1,n//2):
#     for j in range(1,i+1):
#         print(lst[c],end=" ")
#         c+=1
#     print()




# det={'madhu':25,'rakesh':35,'gopi':21,'hari':25,'sanjay':21}
# dup=[]
# for i in det:
#     temp=det[i].value()
#     if temp not in dup:
    
# for i in range(len(det)):
#     for j in det:
         
# def maxof(a,b):
#     res={}
#     if(len(a)>len(b)):
#         res[a]=len(a)
#     else:
#         res[b]=len(b)
#     return res
# print(maxof('madhu','maragani'))

# # {'maragani': 8}

# # 
# def maxof(a,b,c):
#     return(a if a>b and b>c else b if b>a and a>c else c)
# print(maxof(12,13,14))
## 14

# def palam(n):
#     num=str(n)
#     str1=num[::-1]
#     # for i in range(len(num)-1,0,-1):
#     #     str1+num[i]
#     #     print(str1)
#     print(str1)
#     if(num==str1):
#         print('the string is palmdrome',num)
#     else:
#         print("not a plamdrome",num)
# palam(222)
# # the string is palmdrome 222

# def is_prime(lst):
#     sum=0
#     for i in lst:
#         c=1
#         if(i>=2):
#             for n in range(2,i):
#                 if(i%n==0):
#                     c=0
#                     break
#             if(c):
#                 sum=sum+i
#                 print('prime',i)
#     return sum
# lst=[2,3,4,5,6,12,13]
# print(is_prime(lst))            
# # prime 2
# # prime 3
# # prime 5
# # prime 13
# # 23

# # nearest prime number 
# num=int(input('enter a number'))
# def is_prime(num):
#     c=True
#     if num>2:
#         for i in range(2,num):
#             if num%i==0:
#                 c=False
#     return c
# if is_prime(num):
#       print(num)
# else:
#     low_val=num-1
#     high_val=num+1
    
#     while(True):
#         if is_prime(high_val):
#             print(high_val)
#             break
#         if is_prime(low_val):
#             print(low_val)
#             break
#         high_val+=1
#         low_val-=1

      
        
