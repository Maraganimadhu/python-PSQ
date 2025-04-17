# Write a program to print the sum of the digits in the number.

def sum_digites(num):
    sum=0
    while(num!=0):
        rem=num%10
        num=num//10
        sum+=1
    return sum
print(sum_digites(153))
