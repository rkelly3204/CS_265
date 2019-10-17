#!/usr/bin/env python3
#Ryan Kelly
#12/3/2018
#Assignment 3

import sys
import datetime

# Client class
#This class stores all the relvent information about the clients read from the file
#ie. ID,Name, Date, W or D, amount of each transaction
#This class also keeps a log of all the transaction history for all the transactions

class Client:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.balance = 0.0
        self.history = []

    #Returns name
    def getName(self):
        return self.name

    #Returns id
    def getID(self):
        return self.id

    #Returns balance
    def getBalance(self):
        return self.balance

    #Returns History
    def getHistory(self):
        return self.history

    #Creates a new Transaction
    def newTransaction(self, date, type, amount): #parm date ,type, amount
        if type == "W": #Type represents whether you withdrew "W" or deposited "D"
            type = "withdrawal"
            self.balance = self.balance - amount #Calculates the total balance

        else:
            type = "deposit"
            self.balance = self.balance + amount #Calculatest the total balance
        transactionLog = date + " " + type + " $" + str(amount) # Keeps a log of all transactions for Account history
        self.history.append(transactionLog)


def printClientMenu(clientList): #Generic client Menu grows when you add new clients
    counter = 1
    for client in clientList:
        print(counter, ")", client.getName(), client.getID())
        counter += 1
    print("q)uit")

def writeLineToFile(line): #Writes to a file
    file = open("ACCT_LIST", "a+")
    file.write("\n")
    file.write(line) #Writes a new line
    file.close()

def Menu(clientList):
#Standard vairable output
    Switch = True
    Error_Msg = "Incorrect Input. Now Exiting"
    choice_Num = "Enter choice =>"
    id_prompt = "Enter ID =>"
    name_prompt = "Enter account holder name =>"
    type_prompt = "Enter the transaction type ('w' or 'd') =>"
    amount_prompt = "Enter amount for transaction =>"

    #Basic Error Handling
    if len(sys.argv) < 2:
            print(Error_Msg)
            sys.exit()
    # Basic Error Handling
    elif sys.argv[1] in ('-i','-h','-t','-q'): #Only valid input
            usr_Input = sys.argv[1] # Takes command line arguments and sets them equal to usr_Input
    else:
            print(Error_Msg)
    #While loop to select the type of function to be used
    while Switch:
        #If the user inputs the command line argument of -i then my program will return account number, name and balance of the desiered client in the file
        if usr_Input == "-i":
            print("Info")
            print("----")
            printClientMenu(clientList) # Prints a list of current clients in the file
            usr_action= input(choice_Num) #Usr input of the

            if usr_action == "q":
                Switch = False;

            else:
                #Have to add some error handling here
                if int(usr_action ) > len(clientList):
                 print(Error_Msg)
                else:
                 choosenClient = clientList[int(usr_action)-1] #selects the given client that was selected by user input
                 print("account #: " + str(choosenClient.getID())) #Prints account ID
                 print("name: " + str(choosenClient.getName()))#Prints name
                 print("balance: " + str(choosenClient.getBalance())) #Prints Balance

        #If the user inputs the command line argument of -h then my program will return the account history of certain client that was selected
        elif usr_Input == "-h":
            print("History")
            print("-------")
            printClientMenu(clientList) # Prints a list of current clients in the file
            usr_action = input(choice_Num)# usr defined input

            if usr_action == "q":
                Switch = False; #Quits the program

            else:

                if int(usr_action ) > len(clientList):
                 print(Error_Msg)
                else:
                    choosenClient = clientList[int(usr_action) - 1] #Choose the selected client
                    history = choosenClient.getHistory() #grabs the client history then prints

                    for i in history:
                         print(i)
        # If the user inputs the command line argument of -t then my program will allow you to create an account or add a transaction to an existing account
        elif usr_Input == "-t":
            print("Transaction")
            print("-----------")
            printClientMenu(clientList) #Prints a list of current clients in the file
            print("n)ew Account")
            usr_action = input(choice_Num) # Takes the usr input
            now = datetime.datetime.now() #The current date and time and puts into a variable named now
            dayPadding = ""
            monthPadding = ""

            if now.day < 10:
                dayPadding = "0"

            if now.month < 10:
                monthPadding = "0"

            date = str(now.year - 2000) + monthPadding + str(now.month) + dayPadding + str(now.day)

            if usr_action == "q":
                Switch = False;

            # Creates a new transaction
            elif usr_action == "n":
                id = input(id_prompt) #usr created id number
                found = False
                for client in clientList: #Checks to see if the usr ID is already in use
                    if id == client.getID():
                        found = True
                        print("\n--Error account with that ID already exists--\n")

                if not found: #if not then prints usr input statments to fill out the requried info for the transaction to take place
                    name = input(name_prompt) #usr input name
                    type = str(input(type_prompt)).upper() #usr input the type
                    amount = float(input(amount_prompt)) #usr input amount
                    newClient = Client(id, name)
                    clientList.append(newClient)
                    clientList[len(clientList) - 1].newTransaction(date, type, amount)
                    transactionLine = str(id) + ":" + str(name) + ":" + str(date) + ":" + type + ":" + str(amount) #Transaction data
                    writeLineToFile(transactionLine)
            else:
                # Have to add some error handling here
                if int(usr_action) > len(clientList):
                    print(Error_Msg)
                else:
                    type = input(type_prompt) #usr input
                    amount = float(input(amount_prompt)) #usr Input
                    choosenClient = clientList[int(usr_action) - 1]
                    choosenClient.newTransaction(date, type, amount)
                    transactionLine = str(choosenClient.getID()) + ":" + str(choosenClient.getName()) + ":" \
                                  + str(date) + ":" + type + ":" + str(amount)
                writeLineToFile(transactionLine) #Writes the new input to the file

        elif usr_Input == "-?":
            0;

#Main function
def main():
    File_Name = 'ACCT_LIST' # Name of the file
    File_Open = open(File_Name, 'r')
    file_DATA = File_Open.read().splitlines() # Read the file and then splits the lines
    File_Open.close()
    clientList = []

    for line in file_DATA:
        transaction = line.split(":") # split lines on the ":"
        found = False

        #Gets each of client of the clientList
        for client in clientList:
            if transaction[0] == client.getID():
                client.newTransaction(transaction[2], transaction[3], float(transaction[4]))
                found = True

        if not found:
            newClient = Client(transaction[0], transaction[1])
            clientList.append(newClient)
            clientList[len(clientList)-1].newTransaction(transaction[2], transaction[3], float(transaction[4]))

    Menu(clientList)

#Calls the main function
if __name__ == "__main__":
    main()
