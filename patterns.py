# num=int(input("enter n * n materix number"))
# arr=[[0]*num]*num
# # print(len(arr))
# k=1
# for i in range(0,num):
#     # print("sdfghjk")
#     for j in range(0,i+1):
#         if i==j:
#             arr[i][j]=k
#             k+=1
#
#         else:
#             if (i>j):
#                 arr[i][j]=arr[i-1][j]+num-(i-j)
#     # # print(j,"outer")
#
# for i in range(num):
#     for j in range(i+1):
#         print(arr[i][j] ,end=" ")
#     print()
#
# def sorting(arr):
#      for i in range(len(arr)):
#           for j in range(i,len(arr)):
#                if(arr[i]>arr[j]):
#                     temp=arr[i]
#                     arr[i]=arr[j]
#                     arr[j]=temp
#      return arr
# print(sorting([1,5,8,9,3,5,2,4]))
# from tokenize import endpats
from cgitb import small

# n=6
# c=n//2
# for i in range(1,n,2):
#     c-=1
#     print(c*' ',i*"*",c*" ")
# c=0
# for j in range(i-2,0,-2):
#     c += 1
#     print(c*" ",j*"*",c*" ")

# def fun(i):
#     print(i)
#     i+=1
#     if (i<=10):
#         fun(i)
# fun(1)

# # bubblesort
# arr=[5,1,7,2,4,3,6]
# for i in range(len(arr)):
#     for j in range(i+1):
#        if  arr[i]<arr[j]:
#            arr[i],arr[j]=arr[j], arr[i]
# print(arr)
#
# a=[5,1,4,3,2,7,6]
# max=a[0]
# max1=a[0]
# max2=a[0]
# for i in a:
#     if i> max:
#         max2=max1
#         max1=max
#         max=i
# print(max2)
# n=6
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print("*" , end=" ")
#         else:
#             print(" " ,end=" ")
#         print()
#
# row=5
# for i in range(row):
#     s=""
#     for j in range(row):
#         if j==0 or i==j or i==row-1:
#             # print("*",end=" ")
#             s+="*"
#         else:
#             # print(" ",end=' ')
#             s+=" "
#     print(s)
# *
# **
# * *
# *  *
# *****
#

# row=5
# for i in range(row):
#     s=""
#     for j in range(row):
#         if i==0 or j==0 or j==row-1 or i==row-1:
#             s+=" *"
#         else:
#             s+="  "
#     print(s)

#  * * * * *
#  *       *
#  *       *
#  *       *
#  * * * * *

# rows=5
# for row in range(rows):
#     str=""
#     for col in range(rows):
#         if (row+col)%2:
#             str+=" X"
#         else:
#             str+=" O"
#     print(str)
#  O X O X O
#  X O X O X
#  O X O X O
#  X O X O X
#  O X O X O

# rows=5
# c=0
# for row in range(rows):
#     str=""
#     for col in range(rows):
#         if col==0 or row==col or row==rows-1:
#             str+=chr(97+c)
#             c+=1
#         else:
#             str+=" "
#     print(str)
# a
# bc
# d e
# f  g
# hijkl

# rows=6
# space=rows
# for row in range(rows):
#     # str=""
#     # for col in range(rows):
#     print((space-row)*" ",row*"*")
#
#       *
#      **
#     ***
#    ****
#   *****






# row=4
# c=1
# for i in range(1,row+1):
#     if i%2==0:
#         print("_"*(row-c) ,end=" ")
#         for a in range(1,row+1):
#             print(row+a,end=" ")
#         print()
#         c+=1
#     else:
#         print("_"*(row-c) ,end=" ")
#         for a in range(1,row+1):
#             print(i*c, end=" ")
#         c+=1
#
# a,b=0,1
# c=a+b
# for i in range(10):
#     print(a)
#     a=b
#     b=c
#     c=a+b


# def validate(num):
#     return (num%2==0:"even",'false')
# validate(12)
#
# arr=[23,34,56,78,21,45,23,32,91]
# for i in range(len(arr)-1):
#     f=arr[i]%10
#     s=arr[i+1]%10
#     print(arr[i],arr[i+1],f,s)
#     if f>s:
#         arr[i],arr[i+1]=arr[i+1],arr[i]
#         print(arr[i],arr[i+1])
# print(arr)

# def fun(n):
#     print(n)
#     if n>=1:
#         fun(n-1)
# fun(10)

# def start(n):
#     if n<=10:
#         print(n)
#         start(n+1)
# start(1)

# max1 = 0
# max2 = 0
# max3 = 0
# for i in arr:
#     if max1<i:
#         print(max1,i)
#         max3=max2
#         max2=max1
#         max1=i
#         # print(max1,max2,max3)
# print(max3)







# task

# lst=[1,2,3,4,5,6,7,8,9]
# num=int(input("enter a number"))
#
# def fun(arr,num):
#     lst1=[]
#     lst2=[]
#     arr.sort()
#     for i in range(len(arr)):
#         if arr[i]<num:
#             lst1.append(arr[i])
#         else:
#             lst2.append(arr[i])
#     return lst2+lst1
# print(fun(lst,num))

# lst1=[1,2,3,4,5,6]
# lst2=[4,5,6,7,9]
# both=lst1+lst2
# result=[]
# for i in both:
#     if i not in result:
#         result.append(i)
# print(result)

# lst=[2,1,3,4,7,5,9,8,6]
# for i in range(len(lst)):
#     for j in range(i+1):
#         if lst[i]<lst[j]:
#             temp=lst[i]
#             lst[i]=lst[j]
#             lst[j]=temp
# print(lst)

# str="bmamadhum"
# app=[]
# rept=[]
# for i in str:
#     app.append(i)
# # print(app)
# c=0
# for i in str:
#     c=0
#     for j in range(len(str)):
#         if i==str[j]:
#             c=c+1
#     if c>=2:
#         rept.append(i)
#
# # print(rept)
# flage=False
# res=""
# for i in str:
#     if(i not in rept):
#         res=i
#         flage=True
#         break
#     if flage:
#         break
#
# print(res)
#


# word count
# arr_wordes="hello every one this is madhu maragani from 37r batch in 10k coders"
# lst=arr_wordes.split(" ")
# print(len(lst))

# or

# count=0
# for i in arr_wordes:
#     if i==" ":
#         count+=1
# print(count)


# or
# temp=""
# wordes_lst=[]
# for i in arr_wordes:
#     temp += i
#     if i==" ":
#         temp=" "
#
#     wordes_lst.append(temp)
# print(wordes_lst)

# str=input("enter a string")
# lst=[]
# for i in str:
#     lst.append(i)
# def first_non(lst):
#     coutn=0
#     for j in str:
#         c=lst.count(j)
#         if(c==1):
#             print(j)
#             break
#
# first_non(lst)
#
# num=1863721
# max1=0
# max2=0
# while(num!=0):
#      rem=num%10
#      if rem>max1:
#             max2=max1
#             max1=rem
#
#      num=num//10

# print(max2)

# num=[1,3,2,4,5,8,7,6]
# max=0
# max1=0
# for i in num:
#     if max1<i:
#         max1=i
#         max = max1
# print(max)
# class Student:
#     def __init__(self,name,s1,s2,s3):
#         self.name=name
#         self.s1=s1
#         self.s2=s2
#         self.s3=s3
#         self.avg=(self.s1+self.s2+self.s3)/3
#         print(f"avardge of {self.name} is {self.avg}")
# s1=Student("madhu",60,70,50)

# num=55550
# temp=str(num)
# thousands=0
# five=0
# rem=0
# while(num!=0):
#     if num>1000:
#         thousands=int(temp[0:len(temp)-3:])
#         num=num-(thousands*1000)
#         # print(num)
#     elif num>500 and num<1000:
#         five=five+1
#         num=num-500
#
#     elif num<500:
#         rem=num
#         num=num-rem
#         # print(num,rem)
# print(f"\nthousndes:\t{thousands}\nfivehundereds:\t{five}\nremaing:\t{rem}")
#
# list=[[1,2,3],[4,5,6],[7,8,9]] #non digonal return
# # # for i in range(len(list)):
# # #     for j in range(len(list)):
# # #         if (i!=j):
# # #             print(list[i][j])
# lst=[list[i][j]  for i in range(len(list)) for j in range(len(list)) if(i!=j)]
# print(lst)

num=162354

def fun(num ,max1,max2):
    print(num,max1,max2)
    if num>=1:
        rem=num%10
        # print(rem)
        if rem>max1:
            max2=max1
            max1=rem
            # print(max1,max2,rem)
        if max1>rem and rem>max2:
            max2=rem
        num=num//10
        fun(num,max1,max2)
    print(max2)
fun(num,0,0)
