"comprehension"

"extract the each  ele in nested list"
# num_list=[[1,2,3],[4,5,6],[7,8,9]]
# num=[ele for i in num_list for ele in i]
# print(num)
"output: [1, 2, 3, 4, 5, 6, 7, 8, 9]"

"find the max values in nested list"
# max_val=[max(i) for i in num_list]
# print(max_val)
"output:[3, 6, 9] "

"LCM"
# n1=6        #6,12,18,24,30,36,42,48,54,60.........
# n2=10       #10,20,30,40,50,60................

# def lcm(n1,n2):
#     big=max(n1,n2)
#     small=min(n1,n2)
#     if (big%small==0):
#         print(f"lcm of {n1} and {n2} is:{small}")
#     else:
#         temp=big
#         while True:
#             if temp%big==0 and temp%small==0:
#                  print(f"lcm of {n1} and {n2} is:{temp}")
#                  break
#             temp+=big
# lcm(n1,n2)

"output :lcm of 6 and 10 is:30 "
"HCF/GCD"
"higest comman factor " "gratest common divisior"

# def GCF(n1,n2):
#     big,small=max(n1,n2),min(n1,n2)
#     if big%small==0:
#          print(f"hcf of {n1} and {n2} is:{small}")
#     else:
#         for i in range(small,0,-1):
#             if n1%i==0 and n2%i==0:
#                  print(f"lcm of {n1} and {n2} is:{i}")
#                  break
# GCF(2,20)
# " optput: hcf of 2 and 20 is:2"





# "bubble sort"
# "without temp variable "

# num=[1,4,6,8,9,0,7,5,2,3]
# for i in range(len(num)):
#     for j in range(i+1,len(num)):
#         if num[i]<num[j]:
#             num[i]=num[i]+num[j]
#             num[j]=num[i]-num[j]
#             num[i]=num[i]-num[j]
# print(num)
"op:[9, 8, 7, 6, 5, 4, 3, 2, 1, 0] "

# "with temp variable "

# num=[1,4,6,8,9,0,7,5,2,3]
# for i in range(len(num)):
#     for j in range(i+1,len(num)):
#         if num[i]<num[j]:
#             temp=num[i]
#             num[i]=num[j]
#             num[j]=temp
# print(num)

"remove duplicates"
# num=[1,2,3,4,5,4,2,3,3,3,7,8,9,7]
# unique=[]

# for i in num:
#     if i not in unique:
#         unique.append(i)
# print(unique)
# "op:[1, 2, 3, 4, 5, 7, 8, 9]"
# "using set datatype we can extarct unique values"
# uniq=list(set(num))
# print(uniq)
# "op:[1, 2, 3, 4, 5, 7, 8, 9]"

# Python Today's Task
#TASK -1 program to separate odd & even elements from list 
#TASK -2 program to separate unique elements from list and add "*" at EOL

# num=[1, 2, 3, 4, 5, 7, 8, 9]
# even=[]
# odd=[]
# for i in num:
#     if i%2:
#         odd.append(i)
#     else:
#         even.append(i)
# print(f"even:{even} odd:{odd}")
"op:even:[2, 4, 8] odd:[1, 3, 5, 7, 9]"

"find out the unique and no duplicate represent with * end of list "

# num=[1,2,3,4,5,4,2,3,3,3,7,8,9,7]
# uniq=[]
# dup=[]
# for i in num:
#     if i not in uniq:
#         uniq.append(i)
#     else:
#         dup.append("*")
# print(uniq+dup)
# "op:[1, 2, 3, 4, 5, 7, 8, 9, '*', '*', '*', '*', '*', '*']"

# dect1={'a':1,'b':2}
# # dect2=dect1
# # if dect1==dect2:
# #     print("true")
# sum=0
# for i in dect1:
#     sum+=dect1[i]
# print(sum)


# 16-04-2025

"scope"
"the posiible to access value or varible "
"3 types"
"1 local--->within the block {within the fun only we can access }"
# def fun():
#     a=10
# print(a)
"2 Enclosed "
"within in the block we access val or var "


"zip method"
