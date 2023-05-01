import math
import random
import mysql.connector as sql

db = sql.connect(host="127.0.0.1", user="root", passwd="samimiri123", database="bank_management")

if db.is_connected():
    print("SUCCESSFULLY CONNECTED TO THE BANK....")
else:
    print("CHECK YOUR CONNECTION AGAIN")

mycur = db.cursor()


def main():
    print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
    print("1.CREATE ACCOUNT")
    print("2.Show Account Details")
    print("3.CHECK BALANCE")
    print("4.DEPOSIT")
    print("5.WITHDRAW")
    print("6.DELETE ACCOUNT")
    print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
    choice = input("Enter the action wanted: ")
    if choice == '1':
        CreateAcc()
    elif choice == '2':
        AccDetails()
    elif choice == '3':
        CheckBalance()
    elif choice == '4':
        Deposit()
    elif choice == '5':
        Withdraw()
    elif choice == '6':
        DeleteAccount()

def CreateAcc():
    n = input('Enter Your Name: ')
    acn = input('Enter the Account Number: ')
    dob = input('Enter Your Date OF birth: ')
    addie = input('Enter your Address: ')
    cn = input('Enter your contact number: ')
    bal = input('Enter Opening Balance: ')
    data1 = (n, acn, addie, dob, cn, bal)
    data2 = (n, acn, bal)
    sql1 = 'Insert into account (Name, AccNo, Address, DOB, ContactNo, OpeningBal) values (%s, %s, %s, %s, %s, %s)'
    sql2 = 'Insert into amount values (%s, %s, %s)'
    print(f'sql1, {sql1}')
    print(f'sql1, {len(dob)}')
    mycur.execute(sql1, data1)
    mycur.execute(sql2, data2)
    db.commit()
    print("Data entered successfully")
    main()



def Deposit():
    amount = int(input("Enter the amount you would like to deposit: "))
    acn = input('Enter the Account Number: ')
    a = 'select balance from amount where AccNo = %s '
    data = (acn,)
    mycur.execute(a, data)
    result = mycur.fetchone()
    t = result[0] + amount
    sql = 'update amount set balance = %s where AccNo = %s '
    d = (t, acn)
    mycur.execute(sql, d)
    db.commit()
    print("Deposit made successfully")
    main()

def Withdraw():
    amount = int(input("Enter the amount you would like to withdraw: "))
    acn = input('Enter the Account Number: ')
    a = 'select balance from amount where AccNo = %s '
    data = (acn,)
    mycur.execute(a, data)
    result = mycur.fetchone()
    t = result[0] - amount
    sql = 'update amount set balance = %s where AccNo = %s '
    d = (t, acn)
    mycur.execute(sql, d)
    db.commit()
    print("Withdrawal made successfully")
    main()

def CheckBalance():
    acn = input('Enter the Account Number: ')
    a='select * from amount where AccNo=%s'
    data=(acn,)
    mycur.execute(a,data)
    result = mycur.fetchone()
    print("Balance for account:",acn, "is", result[-1])
    main()

def AccDetails():
    acn = input('Enter the Account Number: ')
    a='select * from account where AccNo=%s'
    data=(acn,)
    mycur.execute(a,data)
    result = mycur.fetchone()
    try:
        print(f'Name,{result[0]},')
        print(f'AccNo,{result[1]}')
        print(f'Address,{result[2]}')
        print(f'DOB,{result[3]}')
        print(f'ContactNo,{result[4]}')
        print(f'OpeningBal,{result[5]}')
    except:
        print("Account Not Found")
    main()


def DeleteAccount():
    acn = input('Enter the Account Number: ')
    sql1='delete from account where AccNo=%s'
    sql2='delete from amount where AccNo=%s'
    data=(acn,)
    mycur.execute(sql1,data)
    mycur.execute(sql2,data)
    db.commit()
    print("Account deleted successfully")
    main()



main()