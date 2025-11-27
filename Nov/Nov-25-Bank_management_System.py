print("Bank Mannagement System : \n")
import random as rad
accounts={} # num : acc{bal:000,name:xyz,}


class BMS:
    
    
    def create(self,num,acc_name,bal):
        
        
        acc={
            "acc_num":num,
            "Name":acc_name,
            "Balance":bal
        }
        accounts[num]=acc
        print("Account Created Successfully ...\n")

    def display(self,num):
        if num in accounts:
            print(accounts[num])
        else:
            print("Account Not Found...\n")

    def deposit(self,num,amount):
        if num in accounts:
            accounts[num]["Balance"]+=amount
            print("Add Amount Successfully in Account\n")
        else:
            print("Account Not Found \n")

bms=BMS()


print("1.Create Account")
print("2.View Account Details")
print("3.Exit")
while True:
    try:
        choose=int(input("Enter Your choice :"))
    except ValueError:
        print("Choose The correct Num ")
        print("1.Create Account")
        print("2.View Account Details")
        print("3.Exit")
        continue
    match choose:
        case 1:
            acc_num=rad.randint(1111,9999)
            acc_name=input("Enter the Account Holder Name :")
            bal=int(input("Enter the balance :"))
            print("Account Num : ",acc_num)
            print("Account Holder Name : ",acc_name)
            print("Account Balance : ",bal)
            bms.create(acc_num,acc_name,bal)
        case 2:
            try:
                num=int(input("Enter Account Num:"))
                bms.display(num)
            except ValueError:
                print("Enter Appropriate Account Number :")
            continue

        case 3:
            try: 
                acc_num=int(input("Enter the account Num :"))
                if acc_num not in accounts:  
                    print("account Not found")
                    continue
                amount=int(input("Enter the Amount for deposit :"))
                if amount <= 0:
                    raise ValueError
                bms.deposit(acc_num,amount)
            except ValueError:
                print("Enter the Correct amount :")

            
