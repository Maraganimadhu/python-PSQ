import random
class Account:
    lst=[]
    def create(self):
        dic={}
        dic["name"] = input("enter a name of the person")
        # dic["accountno"] = int(input("enter acount number"))
        dic["accountno"]=random.randint(100000000000,999999999999)
        dic["balance"] = float(input("enter your balance "))
        dic["phone"]=int(input("enter a phone number"))
        dic["age"]=int(input("enter age "))
        print("dear customer your account created succusfylly\nYOUR ACCOUNT NUMBER IS:",dic["accountno"])
        self.lst.append(dic)
    def Check_Balance(self):
        flage=True
        acno = int(input("enter acount number to check balance "))
        for i in self.lst:
            temp=i["accountno"]
            if temp==acno:
                    flage= False
                    if ((i["balance"]>0 and i["balance"]<=500)):
                        print("dear customer your balance is very low plz disposite min balance 500")
                    else:
                        print(f"dear customer your account number is:",i["accountno"],"\nyour balance is",i["balance"])
        if flage:
                print("dear customer you entered wrong account no")
    def Diposite(self):
        # self.name=name=input("enter a name of the person")
        flags=True
        acno=int(input("enter acount number"))
        balance_dp=int(input("enter your balance "))
        for i in self.lst:
            temp=i["accountno"]
            if temp==acno:
                flags=False
                if (i["balance"]>0):
                    i["balance"]+=balance_dp
                else:
                    print("enter amount is invalid")
        if flags:
                print("invalide acno")
    def Withdraw(self):
        acno=int(input("enter acount number"))
        amount=int(input("enter amount you want to withdraw"))
        flags=True
        for i in self.lst:
            if i["accountno"]==acno:
                flags=False
                if((i["balance"]>0 and i["balance"]<=500) or (i["balance"]-amount)<500):
                    print(f"your balance is minim ",i["balance"],"so you cant with draw amount")

                else:
                    i["balance"]=i["balance"]-amount
                    print(f"dear custor you debited amount is:{amount} \n your courrent balance is:",i["balance"])
        if flags:
            print("dear customer entered account no is invalid")

    def Delete_acoount(self):
        acno = int(input("enter acount number"))
        for i in self.lst:
            j=0
            if i["accountno"]==acno:
                res=input("you want to delete your account conform agin if yes enter Y/y onther wise N/n")
                if res=='y' or res=='Y':
                    self.lst.pop(j)
                    print("account was deleted ")
                    break
            j+=1
    def Detailes(self):
        flags=True
        acno=int(input("enter your account no to show the details of the customer"))
        for i in self.lst:
            if i["accountno"]==acno:
                flags=False
                print("dear customer your detals is")
                print("Name:",i["name"])
                print("Account number:",i["accountno"])
                print("Phone",i["phone"])
                print("Balance",i["balance"])
                print("Age",i["age"])
        if flags:
            print("enterd account number invalid")

    def Customers_list(self):
        for i in self.lst:
            print("-------------------------------------------------")
            print("Name:",  i["name"])
            print("Account number:", i["accountno"])
            print("Phone", i["phone"])
            print("Balance", i["balance"])
            print("Age", i["age"])
            print()

customer=Account()

while (True):
    i=int(input(("enter number\n 1 to ctrate  account \n 2 for check balance \n 3 for diposite \n 4 for withdraw amount \n 5 for details\n 6 for customers details \n 7 for delete account  \n to exit 0")))
    if i==1:
        customer.create()
    elif i==2:
        customer.Check_Balance()
    elif i==3:
        customer.Diposite()
    elif i==4:
        customer.Withdraw()
    elif i==5:
        customer.Detailes()

    elif i==6:
        customer.Customers_list()
    elif i==7:
        id2=12345678
        id1=int(input("enter manage id to delete account"))
        if id2==id1:
            customer.Delete_acoount()

    elif i==0:
        break
    else:
        print("enter valide number")

