"print a table 1 to 20"
def tables(num):
    for i in range(1,num+1):
        for j in range(11):
            print(f"{i} * {j}\t=\t{i*j}")

        print("----------------------------------")
num=int(input("enter a number upto tables u want"))
tables(num)