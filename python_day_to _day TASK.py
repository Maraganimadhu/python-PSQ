# # Task : -------------->DAY 3<-----------------------------------------
# # 1. Write a program that checks if numbers in the range -10 to 260 are interned by Python. 
# def range_fun(val):
#     if(val>-10 and val<260):
#         print("The given number  is within range only")
#     else:
#         print("the given number is not within range")
# val=int(input("enter a number "))
# range_fun(val)

 
# # 2. Write a Python program that: 
# # Takes two numbers as input 
# # ● Asks the user for an operation (+, -, *, /, //, %, **) 
# # ● Performs the operation and prints the result 
 
# def cali():
#     n1=int(input("enter first number"))
#     n2=int(input("enter second number"))
#     optr=input("enter a operator to form action")
#     if(optr=="+"):
#         print(n1,optr,n2,"=",(n1+n2))
#     elif(optr=="-"):
#         print(n1,optr,n1,"=",(n1-n2))
#     elif(optr=="*"):
#         print(n1,optr,n2,"=",(n1*n2))
#     elif(optr=="/"):
#         if(n2!=0):
#             print(n1,optr,n2,"=",(n1/n2))
#         else:
#             print("divide by zero not possible try again later")
#     elif(optr=="//"):
#         if(n2!=0):
#             print(n1,optr,n2,"=",(n1//n2))
#         else:
#             print("divide by zero not possible try again later")
#     elif(optr=='%'):
#         print(n1,"%",n2,"=",n1%n2)
#     elif(optr=="**"):
#         print(n1,optr,n2,"=",n1**n2)
#     else:
#         print(" invalid oprater ")
# cali()


# #3. Write a program to check Leap Year.

# year=int(input('enter a year'))
# if((year%4==0 and year%100 !=0) or year%400==0):
#     print("leap year")
# else:
#     print("non leap year")

# #  -------------->DAY 4<-----------------------------------------

# #1. Write a program to print the sum of the digits of a given number.

# arr=str(int(input()))
# sum=0
# for i in arr:
#     sum+=int(i)
# print(sum)

# ----------------------->prime number <---------------------
# num=int(input("enter a number"))
# if(num<0):
#     print("enter a positive number")
# elif(num==1):
#     print("the given number 1 so we can't deside is prime or not")
# else:
#     c=True
#     for i in range(2,num):
#            if(num%i==0):
#             c=False
#             break
    
#     if(c):
#         print(num,"prime number")
#     else:
#         print(num,"not a prime")
 # given number is plidrone or not 
 
# num=int(input())#121
# temp=num
# res=0  
# while(num!=0):
#     rem=num%10
#     res=res*10+rem
#     print(res)
#     num=num//10
# if(temp==res):
#     print("palindrome")
# else:
#     print("not")
    
# #nearest prime for a given number
# def fun_prime(num):             # to find prime or not funtion
#     c=True
#     for i in range(2,num):
#         if(num%i==0):        
#             c=False
#             break
#     return c
# num=int(input("enter number"))                    #enter user value
# if(fun_prime(num)):                               #the given value is prime or not
#     print("for given number",num,"prime number")
# else:                                             #to get nearest prime -- and ++ number 
#     low=num-1
#     high=num+1
#     while(True):
#         if(fun_prime(high)):
#             print("for given number ",num,"nearest prime is",high)
#             break
#         elif(fun_prime(low)):
#             print("for given number ",num,"nearest prime is",low)
#             break    
#         high+=1
#         low-=1
# num=int(input(("enter a number")))
# sum=0
# while(num!=0):
#     last=num%10
#     sum+=last
#     num=num//10
# print(sum)
            
# num=int(input())
# for i in range(num):
#     print((num-1)*"*")   

# for i in range(1,4):
#     print(i*"*")
# num=int(input("enter a number"))
# for i in range(1,num+1):
#     if(i%2):
#         print(i*"*")
#     else:
#         print(i*"/")

# num=int(input("enter a number"))
# for i in range(num):
#     for j in range(num-1):
#         print("*" ,end=" ")
#     print()

# num=int(input("enter a number"))
# for i in range(1,num):
#     for j in range(1,i+1):
#         print("*" ,end=" ")
#     print()

# num=int(input("enter a number"))
# for i in range(num-1,0,-1):
#     for j in range(i):       
#         print("*" ,end=" ")
#     print()
# slice
# p="ram"
# print(p[0:10])

# "string reverse"
# str="madhu maragani"
# # print(str[::-1])
# l=str.replace(" ","")
# print(str)
# print(l)
# str1="{(Ram charan,})"
# str2=str1.strip("{(,)}")
# print(str2)
# str="madhu maragani"
# vol="aeiou"
# temp=""
# vo=""
# for i in str:
#     if(i in vol):
#         vo+=i
#     else:
#         temp+=i
# print(temp+vo)
# "output: mdh mrgnauaaai "
# ------------------------->day 5<-------------------
# """1. Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.
# Input: N=5    Output: 15
# Explanation: 1+2+3+4+5=15"""
# # num=int(input("enter a number"))
# # sum=0
# # for i in range(1,num+1):
# #     sum+=i
# # print(sum)
# 'output: enter a number5    15'

# '''2. Problem Statement: Find all factors of a number or find all distinct divisors of a natural
# number.
# Input: n = 6    Output: 1,2,3,6
# Explanation: 6 is divisible by 1,2,3,6'''
# num=int(input("enter a number"))
# for i in range(1,num+1):
#     if num%i==0:
#         print(i ,end=" ")
# '''output:
# enter a number6
# 1 2 3 6 '''
'''Write a program to count the number of words in a given string. 
○ “Ram Charan” → 2 
○ “Prabhas” → 1'''

# def no_of_words(sent):
#     sent=sent.split(" ")
#     print(len(sent))
# no_of_words("hiii hello everyone")

# d = [
#      {
#      "name":{"firstName":"Ram","secondName":"kumar"},
#      "mobile":234536,
#      "age":21
#      },
#      {
#      "name":{"firstName":"siva","secondName":"ram"},
#      "mobile":3487536,
#      "age":42
#      }
#      ]
# # print(d)
# for i in d:
#     if(i["age"]==21):
#         print(i["name"]["firstName"])
        
"dictonary problems"
employee_list = [
    {
        "name": "Sarah Johnson",
        "age": 32,
        "email": "sarah.j@example.com",
        "country": "United States",
        "role": "Software Engineer",
        "doj": "2021-03-15",
        "phone": "+1-555-123-4567"
    },
    {
        "name": "Miguel Rodriguez",
        "age": 8,
        "email": "miguel.r@example.com",
        "country": "Spain",
        "role": "UX Designer",
        "doj": "2022-06-10",
        "phone": "+34-555-987-6543"
    },
    {
        "name": "Aisha Patel",
        "age": 35,
        "email": "aisha.p@example.com",
        "country": "India",
        "role": "Product Manager",
        "doj": "2020-01-20",
        "phone": "+91-555-234-5678"
    },
    {
        "name": "Jun Liu",
        "age": 19,
        "email": "jun.l@example.com",
        "country": "China",
        "role": "Data Scientist",
        "doj": "2022-11-05",
        "phone": "+86-555-345-6789"
    },
    {
        "name": "Emma Wilson",
        "age": 11,
        "email": "emma.w@example.com",
        "country": "Canada",
        "role": "CTO",
        "doj": "2018-09-12",
        "phone": "+1-555-456-7890"
    },
    {
        "name": "Mohammed Al-Farsi",
        "age": 33,
        "email": "mohammed.a@example.com",
        "country": "UAE",
        "role": "Marketing Specialist",
        "doj": "2021-07-22",
        "phone": "+971-555-567-8901"
    },
    {
        "name": "Ingrid Johansson",
        "age": 27,
        "email": "ingrid.j@example.com",
        "country": "Sweden",
        "role": "Backend Developer",
        "doj": "2023-02-14",
        "phone": "+46-555-678-9012"
    },
    {
        "name": "Takashi Yamamoto",
        "age": 18,
        "email": "takashi.y@example.com",
        "country": "Japan",
        "role": "Systems Architect",
        "doj": "2019-11-30",
        "phone": "+81-555-789-0123"
    },
    {
        "name": "Sophia Mbeki",
        "age": 31,
        "email": "sophia.m@example.com",
        "country": "South Africa",
        "role": "HR Manager",
        "doj": "2020-08-17",
        "phone": "+27-555-890-1234"
    },
    {
        "name": "Carlos Oliveira",
        "age": 16,
        "email": "carlos.o@example.com",
        "country": "Brazil",
        "role": "Frontend Developer",
        "doj": "2023-05-09",
        "phone": "+55-555-901-2345"
    }
]

# # name_list=[]
# for i in employee_list:
#     if i['age']>=18:
#         print(i)
    
        




