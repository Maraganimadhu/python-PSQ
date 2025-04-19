"""Easy:  Write a program to print the sum of the digits in the number.
Testcase1 : 101
Output : 2
Explanation : Sum of the digits in the number 1+0+1 = 2, Answer is 2.
Testcase1 : 567
Output : 18
Explanation : Sum of the digits in the number 5+6+7 = 18, Answer is  18.
"""
from flatbuffers.flexbuffers import String

# from tensorflow.python.keras.backend import is_placeholder

# def sum_digites(num):
#     sum=0
#     while(num!=0):
#         rem=num%10
#         num=num//10
#         sum+=rem
#     return sum
# print(sum_digites(567))

''' Write a program to print reverse of the given number.  
Testcase1 : 721  
Output : 127  
Explanation : Reverse of the number 721 is 127.  
Testcase1 : 765  
Output : 567  
Explanation : Reverse of the number 765 is 567.  '''
# def rever_number(num):
#     temp=0
#     while(num!=0):
#         rem=num%10
#         temp=temp*10+rem
#         num = num//10
#     return temp
# print(rever_number(765))


'''Write a program to print factorial of the number.  
Testcase1 : 3  
Output : 6  
Explanation : Factorial of the number 3 is 3*2*1 = 6.  
Testcase1 : 4  
Output : 24  
Explanation : Factorial of the number 4 is 4*3*2*1 = 24. 
• Write a program to print middle character(s) in the given string or '''
# def factorial(num):
#     product=1
#     for i in range(1,num+1):
#         product*=i
#     return product
# print(factorial(4))


'''Write a program to print middle character(s) in the given string or 
number.  
Testcase1 : Wonder  
Output : nd  
Explanation : The middle characters in the given word Wonder is nd.  
Testcase1 : World  
Output : r  
Explanation : The middle character in the given word World is r.  Test Case 1 : 6969  
Output : 96  
Explanation : The middle character in the given number 6969 is 96. 
'''

# def middle_char_instring(str):
#     len1=len(str)//2
#     if len(str)%2==0:
#         print(str[len1-1]+str[len1])
#     else:
#         print(str[len1])
# middle_char_instring("696")

'''Write a program to check whether the sum of digits in the number except  
first digit and digit is equal to the sum of first digit and last digit of that  number. If both the sums are equal then print equal otherwise print not  equal  
Testcase1 : 75547  
Output : equal  
Explanation : In the given number 7557, first digit and last digit sum  that is sum(7,7)=14 is equal to sum of remaining numbers that is  sum(5,5,4) = 14. So both sums are equal.  
Testcase1 : 765  
Output : not equal  
Explanation : Sum(7,5)=12 and Sum(6)=6, both sums are not equal.  
'''
# def isequal(num):
#     str1=str(num)
#     sumofl=0
#     sumom=int(0)
#     sumofl+=int(str1[0])
#     sumofl+=int(str1[-1])
#     for i in range(1,len(str1)-1):
#         sumom+=int(str1[i])
#
#     if sumom==sumofl:
#         print("equal")
#     else:
#         print("not equal")
# isequal(75547)

'''Write a program to check whether the digits in-between the first and last  
digit are less than first and last digit, if yes then print true, otherwise print  false.  
Testcase1 : 1672  
Output : false
Explanation : The middle digits 6,7 are not less than first digit 1 and  last digit 7 .  
Testcase1 : 84719  
Output : true  
Explanation : The middle digits 4,7,1 are less than first digit 8 and last  digit 9 .  
'''
# def istrue(num):
#     num_str=str(num)
#     fd=num_str[0]
#     ld=num_str[-1]
#     c=False
#     for i in range(1,len(num_str)-2):
#         if num_str[i]<fd and num_str[i]<ld:
#             c=True
#     if c:
#         print("TRUE")
#     else:
#         print("False")
# istrue(1672)
#
'''Write a program to print the vowels in the given string in reverse order.  
Testcase1 : Helloworld  
Output : ooe  
Explanation : Vowels in the given string Helloworld are e,o,o . The  reverse order of eoo is ooe.  
Testcase1 : JackspArrow  
Output : oAa  
Explanation : Vowels in the given string JackspArrow are a,A,o . The  reverse order of aAo is oAa.  
'''
# def vowels_reverse(string):
#     string=string[::-1]
#     res=''
#     voul_list=['a','e','i','o','u','A','E','I','O','U']
#     for i in string:
#         if i in voul_list:
#             res+=i
#     return res
# print(vowels_reverse("Helloworld"))
'''Write a program to print the vowels in the given string and repeated  vowel should be printed only single time.  
Testcase1 : Helloworld  
Output : eo  
Explanation : Vowels in the given string Helloworld are e,o,o . The  single vowels among them are eo .  

Testcase1 : Jacksparrow  
Output : ao  
Explanation : Vowels in the given string Helloworld are a,a,o . Among  them a is repeated more than once, so consider it for one time , result is  ao.
'''
# def vowels_unique(string):
#     res=''
#     voul_list=['a','e','i','o','u','A','E','I','O','U']
#     for i in string:
#         if i in voul_list:
#             if i not in res:
#                 res+=i
#     return res
# print(vowels_unique("Helloworld"))

'''Write a program to print the string after removing the duplicate characters  in the string.  
Testcase1 : madam  
Output : d  
Explanation : In the given string madam, the duplicates are m,a. After  removing m’s and a’s from the given string we formed a new string d.  
Testcase1 : donkey  
Output : donkey  
Explanation : In the given string there is no duplicate character.  
'''
# def unique(string):
#     uni=''
#     for i in string:
#         if string.count(i)==1:
#             uni+=i
#     return uni
# print(unique("donkey"))

'''• Write a program to convert all the upper case letters in the given string to  lower case letter and vice versa.  
Testcase1 : JohnWick  
Output : jOHNwICK  
Explanation : All the upper case letters changed to lower case and vise  versa.  
Testcase1 : Korean  
Output : kOREAN  
Explanation : All the upper case letters changed to lower case and vise  versa.  
'''
'methgod1'
# def up_to_low(string):
#     result_string=''
#     for i in string:
#         if i.isupper():
#             result_string+=i.lower()
#         else:
#             result_string+=i.upper()
#     return result_string
# print(up_to_low("JohnWick"))
"method2"
# def low_to_up(string):
#     result_string=''
#     for i in string:
#         chr1=ord(i)
#         if chr1>=65 and chr1<=90:
#             result_string+=chr(chr1+32)
#         else:
#             result_string+=chr(chr1-32)
#     return result_string
# print(low_to_up("maDHU"))

'''Write a program to print all the Upper case letters in the string in reverse  order and then followed by the lower case letters .  
Testcase1 : NumberOne  
Output : ONumberne  
Explanation : In the given string NumberOne, Uppercase letters are N,O.  The reverse order of them are ON next it is followed by lowe case letters  (umberne). So final string is ONumberne.
Testcase1 : ClassLeader  
Output : LClasseader  
Explanation : In the given string ClassLeader, Uppercase letters are C,L.  The reverse order of them are LC next it is followed by lowe case letters  (lasseader). So final string is LClasseader. 

'''
# def upper_first(string):
#
#     up=''
#     low=''
#     for i in string:
#         if i.isupper():
#             up+=i
#         else:
#             low+=i
#     up=up[::-1]
#     return up+low
# print(upper_first("ClassLeader"))
"----------------------------------------------------->Array-Based Questions :<------------------------"

'''Find the Largest Element in an Array 
Problem: Write a function to return the largest number in an array. 
Testcase 1: 
Input: [3, 1, 4, 1, 5, 9] 
Output: 9 
Explanation: 
In the array [3, 1, 4, 1, 5, 9], the largest number is 9. 
'''
'mathod1'
# def largestnumber_inarry(arr):
#     max=arr[0]
#     for i in arr:
#         if max<i:
#             max=i
#     return max
# print(largestnumber_inarry([3, 1, 4, 1, 5, 9]))
"method 2"
# def method2(arr):
#     arr.sort()
#     print(arr[-1])
# method2([3, 1, 4, 1, 5, 9])

'''Find the Second Largest Element 
Problem: Write a function to return the second largest number in an array. 
Testcase 1: 
Input: [3, 1, 4, 1, 5, 9] 
Output: 5 
Explanation: 
In the array [3, 1, 4, 1, 5, 9], the second largest number after 9 is 5. 
'''
# def second_large(arr):
#     arr.sort()
#     return arr[-2]
# print(second_large([3, 1, 4, 1, 5, 9]))

'''Sum of All Elements 
Problem: Write a function that returns the sum of all elements in an array. 
Testcase 1: 
Input: [1, 2, 3, 4] 
Output: 10
Explanation: 
The sum of the elements 1 + 2 + 3 + 4 = 10. 
'''
# def sum_arry(arr):
#     sum=arr[0]
#     for i in range(1,len(arr)):
#         sum+=arr[i]
#     return sum
# print(sum_arry([1, 2, 3, 4]))
'''Remove Duplicates from an Array 
Problem: Write a function to remove duplicate values from an array. 
Testcase 1: 
Input: [1, 2, 2, 3, 4, 4, 5] 
Output: [1, 2, 3, 4, 5] 
Explanation: 
The duplicates 2 and 4 are removed from the array, leaving [1, 2, 3,  4, 5]. 
'''
"method1"
# def remove_duplicate(lst):
#     unique=[]
#     for i in lst:
#         if i not in unique:
#             unique.append(i)
#     return unique
# print(remove_duplicate([1, 2, 2, 3, 4, 4, 5]))
"method2"
# def unique(lst):
#     return list(set(lst))
# print(unique([1, 2, 2, 3, 4, 4, 5]))

'''Check if Array is Sorted 
Problem: Write a function to check if an array is sorted in ascending  order.  
Testcase 1: 
Input: [1, 2, 3, 4, 5] 
Output: true 
Explanation: 
The array [1, 2, 3, 4, 5] is sorted in ascending order. 
'''
# def so(arr):
#     temp=arr
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             if arr[i]>arr[j]:
#                 temp=arr[i]
#                 arr[i]=arr[j]
#                 arr[j]=temp
#
#     if temp is arr:
#         print("True")
#     else:
#         print("False")
#     print(temp,arr)
#
# so([1, 2, 3, 4, 5] )

'''Reverse an Array 
Problem: Write a function to reverse the elements in an array. 
Testcase 1: 
Input: [1, 2, 3, 4, 5] 
Output: [5, 4, 3, 2, 1] 
Explanation: 
The array [1, 2, 3, 4, 5] is reversed to [5, 4, 3, 2, 1].
'''
# def arr_reverse(arr):
#     lst=list()
#     for i in range(len(arr)-1,-1,-1):
#         lst.append(arr[i])
#     return lst
# print(arr_reverse([1, 2, 3, 4, 5]))
'''Remove Falsy Values 
Problem: Write a function that removes all falsy values from an array.  Falsy values include false, 0, "", null, undefined, and NaN. 
Testcase 1: 
Input: [0, 1, false, 2, '', 3] 
Output: [1, 2, 3] 
'''
# def remove(arr):
#     falsy=["",0,"null","false"]
#     result_list=[]
#     for i in arr:
#         if i not in falsy:
#             result_list.append(i)
#     return result_list
# print(remove([0, 1, "false", 2, '', 3]))
'''Find Unique Elements 
Problem: Write a function to find the unique elements in an array  (elements that appear only once). 
Testcase 1: 
Input: [1, 2, 2, 3, 4, 4, 5] 
Output: [1, 3, 5] 
Explanation: 
The unique elements that appear only once in the array are 1, 3, and 5. 
'''
# def unique(arr):
#     result=[]
#     for i in arr:
#         if arr.count(i)==1:
#             result.append(i)
#     return result
# print(unique([1, 2, 2, 3, 4, 4, 5]))

'''Sum of Even Numbers 
Problem: Write a function that returns the sum of all even numbers in an  array. 
Testcase 1: 
Input: [1, 2, 3, 4, 5] 
Output: 6 
Explanation:
The even numbers in the array are 2 and 4. Their sum is 2  '''
# def sum_even(arr):
#     sum=0
#     for i in arr:
#         if i%2==0:
#             sum+=i
#     return sum
# print(sum_even([1, 2, 3, 4, 5] ))
"---------------------------------------->String-Based Questions<---------------------"
'''Reverse a String : 
Question: Write a function to reverse a given string.
Testcase: "hello"
Output: "olleh"
Explanation: The reverse of the string "hello" is "olleh". Each character's order is reversed.
'''
# def reverse_string(string):
#     return string[::-1]
# print(reverse_string("hello"))

'''Check if a String is a Palindrome
Question: Write a function to check if a given string is a palindrome.
Testcase: "racecar"
Output: true
Explanation: A palindrome is a string that reads the same forward and backward. Since "racecar" is the same in both directions, the output is '''

# def is_Palindrome(string):
#     temp=""
#     for i in range(len(string)-1,-1,-1):
#         temp+=string[i]
#     if temp==string:
#         print("True")
#     else:
#         print("False")
#
# is_Palindrome("madam")
'''Count Vowels in a String
Question: Write a function to count the number of vowels in a given string.
Testcase: "hello world"
Output: 3
Explanation: The vowels in "hello world" are 'e', 'o', and 'o'. Thus, the total count of vowels is 3.
'''
# def count_vowels(string):
#     vowels=['a','e','i','o','u']
#     cout=0
#     for i in string:
#         if i in vowels:
#             cout+=1
#     return cout
# print(count_vowels("hello world"))
'''Remove Vowels from a String
Question: Write a function to remove all vowels from a given string.
Testcase: "hello world"
Output: "hll wrld"
Explanation: After removing the vowels 'e', 'o', and 'o' from "hello world", we are left with "hll wrld".
'''
# def remove_vouls(string):
#     vowels=['a','e','o','i','u']
#     temp_string=''
#     for i in string:
#         if i not in vowels:
#             temp_string+=i
#     return temp_string
# print(remove_vouls("hello world"))

'''Convert String to Title Case
Question: Write a function that converts a string to title case (capitalize the first letter of each word).
Testcase: "hello world"
Output: "Hello World"
Explanation: The first letter of each word is capitalized, resulting in "Hello World".
'''
# def titles(string):
#     list_string=string.split(" ")
#     result=''
#     for i in list_string:
#         for j in range(len(i)):
#             if j==0:
#                 if i[j].islower():
#                     result+=i[j].upper()
#             else:
#                 result+=i[j]
#         result+=" "
#     return result
# print(titles("hello world"))
'''Convert String to Number
Question: Write a function to convert a string to a number (without using parseInt or Number).
Testcase: "123"
Output: 123
Explanation: The string "123" is converted to the number 123.'''
# def typ(string):
#     return int(string)
# print(typ("123"))
'''
Check if String Contains Only Digits
Question: Write a function to check if a string contains only numeric digits.
Testcase: "12345"
Output: true
Explanation: The string "12345" consists only of digits, so the result is true.
'''

# def check_isdigit(String):
#     c=True
#     for i in String:
#         if i.isalpha():
#             c=False
#             break
#     return c
# print(check_isdigit("1234"))

'''Count Occurrences of a Character
Question: Write a function that counts the occurrences of a specific character in a string.
Testcase: "hello world", "l"
Output: 3
Explanation: The character 'l' appears 3 times in the string "hello world".
'''
# def Count_Occurrences(string):
#     con=[]
#     for i in string:
#         con.append(string.count(i))
#     con.sort()
#     for i in string:
#         if con[-1]==string.count(i):
#             print(con[-1],i)
#             break
# Count_Occurrences("hello world")

"---------------------------------------------->Object-Based Questions<------------------------"
'''Convert Array to Object
Question: Write a function that converts an array of key-value pairs into an object.
Testcase: [["name", "Alice"], ["age", 25]]
Output: {name: "Alice", age: 25}
Explanation: The key-value pairs in the array are converted into properties of an object. "name" maps to "Alice", and "age" maps to 25.
'''
# def arry_to_object(lst):
#     dec=dict()
#     for i in lst:
#         dec[i[0]]=i[1]
#     return dec
# print(arry_to_object([["name", "Alice"], ["age", 25]]))
'''Merge Two Objects
Question: Write a function that merges two objects, giving priority to the properties of the second object in case of conflict.
Testcase: {a: 1, b: 2}, {b: 3, c: 4}
Output: {a: 1, b: 3, c: 4}
Explanation: The property b in the second object overrides the property b in the first object, resulting in {a: 1, b: 3, c: 4}.
'''
# def merge_obj(obj1,obj2):
#     obj1.update(obj2)
#     return obj1
# print(merge_obj({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
'''Count Object Properties
Question: Write a function that returns the number of properties in an object.
Testcase: {a: 1, b: 2, c: 3}
Output: 3
Explanation: The object {a: 1, b: 2, c: 3} has 3 properties, so the output is 3.
Get Object Keys
Question: Write a function that returns an array of all the keys in an 
'''
# def obj(obj1):
#     return len(obj1)
# print(obj({'a': 1, 'b': 2}))
'''Get Object Keys
Question: Write a function that returns an array of all the keys in an object.
Testcase: {a: 1, b: 2, c: 3}
Output: ["a", "b", "c"]
Explanation: The keys of the object are "a", "b", and "c", so the function returns an array of these keys.

'''
# def keysofdict(obj):
#     keys=[]
#     for i in obj:
#         keys.append(i)
#     return keys
# print(keysofdict({'a': 1, 'b': 2}))
'''
Get Object Values
Question: Write a function that returns an array of all the values in an object.
Testcase: {a: 1, b: 2, c: 3}
Output: [1, 2, 3]
Explanation: The values of the object are 1, 2, and 3, so the function returns an array of these values.
'''

# def valuesoddict(obj):
#     values=[]
#     for i in obj:
#         values.append(obj[i])
#     return values
# print(valuesoddict({'a': 1, 'b': 2}))

'''Check if Object is Empty
Question: Write a function to check if an object is empty (i.e., has no properties).
Testcase: {}
Output: true
Explanation: Since the object has no properties, the function returns true.
'''
# def checks(obj):
#     if len(obj)==0:
#         return True
#     else:
#         return False
# print(checks({}))

"---------------------------------------------------->MEDIUM<--------------------------------------------------"
''' 1
Write a program that takes a string, string should be of even length. Divide the string into two equals parts, check the number of vowels in both the parts of the string. If both parts of string have same number of vowels then return true otherwise return false.

Testcase1	:  rebels
Output     	:  true
Explanation 	:  Given sring rebels divided into two parts, reb and els. In both parts vowels count is same that is 1(e is presented in both the parts) so it returns true.

Testcase2	:  apples
Output     	:  true

Testcase1	:  mars
Output     	:  false
'''
# def test(string):
#     if len(string)%2==0:
#         fpart=''
#         spart=''
#         vowel=['a','e','i','o','u']
#         for i in range(len(string)):
#             if i<len(string)/2:
#                fpart+=string[i]
#             else:
#                 spart+=string[i]
#         # print(fpart,spart)
#     fvc=0
#     svc=0
#     for i in vowel:
#         if i in fpart:
#             fvc+=1
#         if i in spart:
#             svc+=1
#     # print(fvc,svc)
#     if fvc==svc:
#         print("True")
#     else:
#         print("Flase")
#
# test("apples")
#





