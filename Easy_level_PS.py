##---------------------------------------------->easy level<---------------------------------------------

# 1 Create a function that takes two numbers as arguments and returns their sum.

# def sum(num1,num2):
#     return num1+num2
# a=int(input("enter a numbers "))
# b=int(input("enter a numbers "))
# resule=sum(a,b)
# print("the sum of two numbers is",resule)


# 2 Write a function that takes an integer minutes and converts it to seconds.

# def scondes(min):
#     return min*60
# min=int(input('enter a number of min'))
# if(min>0):
#     print("the given no of min if ",min,'secondes are ',(scondes(min)))
# else:
#     print("please enter valid number ")


#3  Create a function that takes a number as an argument, increments the number by +1 and returns the result.


# def incrementer(num):
#     return num+1
# num=int(input('enter a number'))
# print(incrementer(num))

# 4 Create a function that takes the age in years and returns the age in days.

# year=int(input("enter a number "))
# def days(year):
#     non_leap=0
#     leap=0
#     if(year<=0):
#         print("enter positive number")
#         exit
#     for i in range(1,year+1):
#         if(i%4):
#             non_leap+=1
#         else:
#             leap+=1
#     return ((leap*366)+(non_leap*365))
# result=days(year)
# print(result)
        
# 5 sbi Create a function that takes voltage and current and returns the calculated power.

# def power(v,i):
#     print("power is",(v*i))

# while(True):
#     v=int(input("enter  voltage"))
#     i=int(input("enter a current value"))
#     if(v>1 and i>1):
#         power(v,i)
#         break
#     else:
#         print("enter valide input")


# # 6   Write a function that returns the string "something" joined with a space " " and the given argument a.
# def something(b):
#   som='somthing'
#   som=som+' '+(str(b))
#   print(som)
# st=input("enter a number")
# something(st)
# #  enter a numbermadhu
# # somthing madhu

# # 7 Create a function that takes two arguments. Both arguments are integers, a and b. Return true if one of them is 10 or if their sum is 10.
# def checker(num1,num2):
#      lst=[num1,num2,(num1+num2)]
#      if 10 in lst:
#           res=1
#      else:
#           res=0
#      return res

# num1=int(input("ente r a number"))
# num2=int(input("ente r a number"))
# a=checker(num1,num2)
# if(a):
#      print("true")
# else:
#      print("false")

# ente r a number12
# ente r a number13
# false
# PS C:\Users\Lenovo\OneDrive\Desktop\DS> & C:/Users/Lenovo/AppData/Local/Programs/Python/Python312/python.exe c:/Users/Lenovo/OneDrive/Desktop/DS/pe.py
# ente r a number10
# ente r a number12
# true
# PS C:\Users\Lenovo\OneDrive\Desktop\DS> & C:/Users/Lenovo/AppData/Local/Programs/Python/Python312/python.exe c:/Users/Lenovo/OneDrive/Desktop/DS/pe.py
# ente r a number5
# ente r a number10
# true
# PS C:\Users\Lenovo\OneDrive\Desktop\DS> & C:/Users/Lenovo/AppData/Local/Programs/Python/Python312/python.exe c:/Users/Lenovo/OneDrive/Desktop/DS/pe.py
# ente r a number5
# ente r a number5
# true

# 8 Create a function that takes two strings as arguments and returns either true or false depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.

# def depending(str1,str2):
#      temp1=0
#      for i in str1:
#          if i.isalpha:
#               temp1+=1
#      temp2=0
#      for i in str2:
#          if i.isalpha():
#               temp2+=1
#      if(temp1==temp2):
#           res="true"
#      else:
#           res="false"
#      return res
# str1=input("enter string")
# str2=input("enter 2nd string")
# print(depending(str1,str2))

# enter stringmadhu
# enter 2nd stringmadhu
# true
# enter stringmadhu
# enter 2nd stringmaragani
# false

# 9 Create a function that takes a name and returns a greeting in the form of a string. Don't use a normal function, use an arrow function.
# grating=lambda name:f"hello,{name}!"
# print(grating("madhu"))
# hello,madhu!

# 10) Create a function that takes an array of 10 numbers (between 0 and 9) and returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555).
# def arr_pn(numbers):
#        return f"({numbers[0]}{numbers[1]}{numbers[2]}) {numbers[3]}{numbers[4]}{numbers[5]}-{numbers[6]}{numbers[7]}{numbers[8]}{numbers[9]}"

# a = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
# phone_number = arr_pn(a)
# print(phone_number)

# 11.Create a function that returns an array of strings sorted by length in ascending order.
# Example:
# sortByLength(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]

# def sorting(arr):
#      for i in range(len(arr)):
#           for j in range(len(arr)):
#                if(arr[i]<arr[j]):
#                     temp=arr[i]
#                     arr[i]=arr[j]
#                     arr[j]=temp
#      return arr
# arr=['a','ccc','eeeee','dddd','bb']
# print(sorting(arr))

# ['a', 'bb', 'ccc', 'dddd', 'eeeee']


# # 12 Create a function that takes an array of arrays with numbers. Return a new (single) array with the largest numbers of each.
# Example:
# findLargestNums([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]) ➞ [7, 90, 2]

# def arrey(arr):
#     lst=[]
#     max=0
#     for i in arr:
#         i.sort()
#         lst.append(i[-1])
#     return lst
# arr=[[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]
# print(arrey(arr))

# ##[7, 90, 2]
            
# 13 Create a function that takes an array of numbers and returns the second largest number.
# Example:
# secondLargest([10, 40, 30, 20, 50]) ➞ 40

# def arrey(arr):
#     for i in arr:
#         arr.sort()
#     return arr[-2]
# arr=[10, 40, 30, 20, 50]
# print('2nd largest number',arrey(arr))
# # 2nd largest number 40

# # 14 Create a function that takes an array of items, removes all duplicate items and returns a new array in the same sequential order as the old array (minus duplicates).
# Example:
# removeDups([1, 0, 1, 0]) ➞ [1, 0]
# # removeDups(["The", "big", "cat"]) ➞ ["The", "big", "cat"]

# def Remove_duplicates(arr):
#     lst=[]
#     for i in arr:
#         if i not in lst:
#             lst.append(i)
#     return lst
# # arr=[1, 0, 1, 0]
# arr=["The", "big", "cat"]
# print(Remove_duplicates(arr))
# ['The', 'big', 'cat']
# [1, 0]

# # 15 Create a function that takes an array of integers as an argument and returns a unique number from that array. All numbers except unique ones have the same number of occurrences in the array.
# Example:
# findSingleNumber([2, 2, 2, 3, 4, 4, 4]) ➞ 3
 
# def findSingleNumber(arr):
#     lst=[]
#     for i in arr:
#         j=arr.count(i)
#         if j==1:
#             lst.append(i)
#     return lst
# arr=[2, 2, 2, 3, 4, 4, 4]
# print(findSingleNumber(arr))
# #[3]


# 16 Create a function that takes two strings as arguments and returns the number of times the first string (the single character) is found in the second string.
# Example:
# charCount("c", "Chamber of secrets") ➞ 1
# def charCount(ch,str):
#     print(str)
#     c=0
#     for i in str:
        # if ch==i:  # ch in str
#             c+=1
#     return c
# ch="e"
# str1="Chamber of secrets"
# print(charCount(ch,str1))
# # 3

# 17 Create a function that takes a string and returns the number (count) of vowels contained within it.
# Example:
# countVowels("Celebration") ➞ 5

# def countVowels(str1):
#     vlist=['A','E','I','O','U','i','e','a','o','u']
#     count=0
#     for i in str1:
#         if i in vlist:
#             count+=1
#     return count
# ch="Celebration"
# print(countVowels(ch))

##  5

# 18 Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa.
# Example:
# reverseCase("Happy Birthday") ➞ "hAPPY bIRTHDAY"

# def reverseCase(str1):
#     a=''
#     for i in str1:
#         if i==i.upper():
#             a+=(i.lower())
#         else:
#             a+=(i.upper())
#     return a
# ch="Happy Birthday"
# print(reverseCase(ch))
# #hAPPY bIRTHDAY

# 19 Take one integer n, loop till n and pass each value to a function, create a function that takes one integer parameter, and multiply with 2 in every integer.
	# Input:      n=5
	# 		Output:   2 4 6 8 10
 
# def double(num):
#      lst=[x*2 for x in range(1,num+1)]
#      return lst
# print(double(5))
# #  [2, 4, 6, 8, 10]



#20 Create Function that will take one parameter and return type of the data.
		
			# Input:       500
			# Output:     Integer
			# Input:       Coding
			# Output:    String
# def type_of(str):
#     type1=type(str).__name__
#     if type1=='int':
#         print("Integer")
#     elif type1=='str':
#         print("String")
    
# ch="string"
# print(type(ch))
# type_of(ch)
        
# #21Program to find greatest of three numbers(using ternary operator).
			# Input:  4 8 2
			# Output: 8 is greatest
# def grater(a,b,c):
#     print(a if(a>b and b>c) else b if(b>c and b>a) else c)
# grater(1,3,2)
# # 3

#22 C Program to find factorial of number.
			# Input: n=5
# 			Output: 120
# 			Explanation: 5 x 4 x 3 x 2 x 1 = 120

#include<stdio.h>
#int main(){
#     int a=5:
#         product=1
#         for(int i=1;i<=n,n++){
#             product*=i
#         }
#     return product;
# }


# # 23 babbul sort
# C Program to arrange numbers in ascending order
# 			Input: [2,3,1,5,4]
# 			Output: [1,2,3,4,5]


# 24 Print Patter using loop.

			# 1
			# 1 2
			# 1 2 3
			# 1 2 3 4
  			# 1 2 3 4 5
# def pattern(num):
#     for i in range(1,num+1):
#         for j in range(1,i+1):
#             print(j,end=' ')
#         print()
        
# pattern(5)
# 1 
# 1 2 
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# 25 C Program to Calculate the Power of a Number(using loop only).
			# Input: n=5, p=3
			# Output: 5 ^ 3 = 125
			# Explanation: 5 x 5 x 5 = 125
   
   
# def Calculate(num,pow):
#     product=num
#     for i in range(1,pow):
#          product*=num
                
#     return product
# print(Calculate(5,4))
# # #625
    
# 26 Program to Check Whether a Number is Prime or Not
			# Input: 9
			# Output: 9 is not a prime no
			# Input: 7
			# Output : 7 is a prime no
# aledy we done at

#27 Program to find LCM of two numbers using while loop
			# Input: 15 50
			# Output: Lcm of 15 and 50 is 150.
   
# ip1=15
# ip2=12
# max=ip1 if (ip1>ip2) else ip2

# while True:
#     if(max%ip1==0 and max%ip2==0):
#         print("lcm is:",max)
#         break
#     max+=1
# # lcm is: 60


# 28Program to Display Characters from A to Z Using Loop with count.
			# Output: A1 B2 C3 D4 E5 F6 ……. Z26
#
# for i in range(1,27):
#        print(chr(64+i),i ,end="  ")
# #   A 1  B 2  C 3  D 4  E 5  F 6  G 7  H 8  I 9  J 10  K 11  L 12  M 13  N 14  O 15  P 16  Q 17  R 18  S 19  T 20  U 21  V 22  W 23  X 24  Y 25  Z 26    #    
       
# 29 Program to find a missing number
	# Input:  n=5(length of array), arr= [5,3,1,4]
	# 		Output: 2 is missing
# arr= [5,3,1,4]
# n=5
# lst=[]
# for i in range(1,n+1):
#     lst.append(i)
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if (arr[i]<arr[j]):
#             temp=arr[i]
#             arr[i]=arr[j]
#             arr[j]=temp
# print(arr,lst)
# for k in range(len(arr)):
#     if(arr[k]!=lst[k]):
#         print(lst[k])
#         break
#     else:
#         print("matched")
## 2


#  30 Program to count vowels and consonants in a given String.
			# Input: i am ram
			# Output: 3 vowels 3 consonants.

# str=input("enter a string")
# vlst=['A','E','I','O','U','a','e','i','o','u']
# c=0
# v=0
# str1=str.replace(" ",'')
# for i in str1:
#     if i in vlst:
#         v+=1
#     else:
#         c=c+1
# print("vowels are",v,'consonents')
# enter a stringmadhu maragani
# vowels are 6 consonents 


# 31 program to insert  the elements of an array for specific index.
			# Input: [1,2,3,4,5,7,8,9,10] , index=5
			# Output: [1,2,3,4,5,6,78,9,10]

# arr=[1,2,3,4,5,7,8,9,10]
# index=5
# arr[index]=6
# print(arr)
# [1, 2, 3, 4, 5, 6, 8, 9, 10]

# 32 everse a number using while Loop
			# Input: 123
			# Output: 321
# num=123
# num1=str(num)
# i=len(num1)-1
# a=''
# while(i>=0):
#     a+=num1[i]
#     i=i-1
# print(a)
    ## 321
    
 # 33  Count occurrence of number:
			# Input: [1,6,3,1,5,9,7,2,1,9,3,7,8,9,10] , no find=7
			# Output: 7 present 2 times.
# arr=[1,6,3,1,5,9,7,2,1,9,3,7,8,9,10]
# no=7
# count=0
# for i in arr:
#     if i==no:
#         count+=1
# print('count of given ',no,' number is',count)
# count of given  7  number is 2

# #  ----------------->nearest prime number<---------------------------------
# num=int(input("enter a number"))
# def is_prime(num):
#     c=1
#     if(num>2):
#         for i in range(2,num):
#             if num%i==0:
#                 c=0
#                 break
#     else:
#         print("enter greater then 2 number")
#     return c

# if is_prime(num):
#     print(num)
# else:
#     lower_number=num-1
#     higher_number=num+1  
#     while(True):
#         if lower_number>2 and is_prime(lower_number):
#             print(lower_number)
#             break
#         if higher_number>0 and is_prime(higher_number):
#             print(higher_number)
#             break
#         lower_number-=1
#         higher_number+=1
        
        # enter a number6
        #  5