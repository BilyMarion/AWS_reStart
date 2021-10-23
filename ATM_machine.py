#Python3.10
#UT-8
#ATM machine code
#Initiate a nested dictionary customer
customers={"customer1":{"Username":"Marion","PIN":1234,"Current Balance":258000},
           "customer2":{"Username":"Lucian","PIN":1101,"Current Balance":50000},
           "customer3":{"Username":"George","PIN":8945,"Current Balance":1000000}}

#Initiate two global variables account details and myName
accountDetails={}
myName=""

#Function to display a welcome note
def atmDisplay():
    print("****Welcome to Future Bank****"+"\n"
          "  Kindly insert your ATM card  ")
    return

#Function to loop through the customer dictionary and checks if the two variables (myName,myPin)
#which are user inputs correspond to customerPIN and customerName in the dictionary
def checkCredentials(myName,myPin):
    for i in customers:
        customerPin=customers[i]["PIN"]
        customerName=customers[i]["Username"] 
        if myName==customerName and myPin==customerPin:
            return i
    return False

#Funtion verifies user login credentials 
def loginCredentials():
    global accountDetails 
    global myName
    counter=0
    while counter<3:
        myName=input("Please enter your registered name : ")
        myPin=int(input("You have {} attempts:Please enter your PIN : ".format(3-counter)))

        if (id := checkCredentials(myName,myPin)):
            print("Welcome {}.".format(myName)+" Would you like to:"+"\n"+
            "1.Withdraw{}".format("\n")+
            "2.Deposit "+"\n"+
            "3.Check Balance"+"\n"+
            "4.Exit")
            accountDetails=customers[id]
            break
        else:
            print("Wrong user credentials. Please try again")
            counter+=1
            
        

#Funtion to check account balance
def checkBalance ():
    print ("Would you like to check your balance ?")
    checkBalance=int(input("Enter option 1 or 2: {}".format("\n")+"1.Yes{}".format("\n")+"2.No{}".format("\n")))
    if checkBalance==1:
        print (f'Hi {myName}'+"\n"+
               "Your account balance is : {}".format(accountDetails["Current Balance"])+"\n"+
               "'***Thank you for choosing The Future Bank!***")
        
    else:
            print("***Thank you for choosing The Future Bank!***")
            exit()

#Funtion to print receipt
def printStatement():
    print("Would you like a printed copy of your receipt. Enter Yes/No : ")
    if input()=="Yes":
        print("***THE FUTURE BANK***"+"\n"+
                  "Dear {}".format(myName)+"\n"+
              "Your current balance is: {}".format(accountDetails["Current Balance"])+
              "***Thank you for choosing The Future Bank!***")

    else:
        print("Thank you for choosing The Future Bank")

#Funtion for Withdrawal transaction
def Withdraw ():
 
    counter=0
    while counter<2:
        print("How much would you like to Withdraw : ")
        myAmountToWithdraw=int(input())
        if myAmountToWithdraw>=1000 and myAmountToWithdraw<accountDetails["Current Balance"]:
            accountDetails["Current Balance"]=accountDetails["Current Balance"]-myAmountToWithdraw
            print("You have withdrawn {} from your account".format(myAmountToWithdraw))
            
            counter=counter+1
    
            print("Would you like to make another withdrawal transaction? Enter Yes/No")
            if input()=="Yes":
                print("Please proceed")
            #return True
                        
        elif myAmountToWithdraw==0 and myAmountToWithdraw<1000:
            print("You can only a minimum of Ksh.1000")
        else:
            print("You have entered an invalid amount")
    
    checkBalance()
    printStatement()

#Funtion for Deposit transaction         
def Deposit ():
    
    print("How much would you like to Deposit : ")
    myAmountToDeposit=int(input())
    if myAmountToDeposit>=1000:
        accountDetails["Current Balance"]=accountDetails["Current Balance"]+myAmountToDeposit
        print("You have deposited {} to your account".format(myAmountToDeposit))
        #return True
    else:
        print("You can only deposit a minimum of Ksh.1000")
    checkBalance()
    printStatement()

#Main ATM function        
def myATMmachine():
    atmDisplay()
    loginCredentials()
    myOption=int(input())
    if myOption==1:
        Withdraw()
    elif myOption==2:
        Deposit()
    elif myOption==3:
        checkBalance()
    else:
        print("***Thank you for choosing The Future Bank!***")
        exit()

myATMmachine()


    


    





           
            
                
     
        
   
      






