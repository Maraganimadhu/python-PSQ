"print a table 1 to 20"
def tables(num):
    for table in range(1,num+1):
        for mul in range(11):
            print(f"{table} * {mul}\t=\t{table*mul}")

        print("end of the table :",table)
num=int(input("enter a number upto tables u want"))
tables(num)