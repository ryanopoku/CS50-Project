import time
import sys

def save_file_double():
        newfile1 = input ("Enter the name of the file")
        finalbill1 = str(int(doubcost))
        encfile1 = open(newfile1+".txt" , "w")
        encfile1.write("This is your total bill without vat GBP\n")
        encfile1.write(finalbill1)
        print ("Your bill will be saved to a word document named",newfile1,".txt")
        encfile1.close()


def save_file_single():
        newfile = input ("Enter the name of the file")
        without_vat = str(int(sincost))
        encfile = open(newfile+".txt" , "w")
        encfile.write("This is your total bill without vat GBP")
        encfile.write(without_vat)

        with_vat = str(int(total_single))
        encfile.write("\n This is your total bill with vat GBP")
        encfile.write(with_vat)
        encfile.write("\n VAT Rate is 20% \n")

        num_nights = str(int(n))
        encfile.write("\n Number of nights you will stay for:")
        encfile.write(num_nights)

        chos_room = str(int(room))
        encfile.write("\n Room Number:")
        encfile.write(chos_room)

        print ("Your bill will be saved to a word document named",newfile,".txt")
        encfile.close()



def MainMenu():
    print("***************************MAIN MENU*******************************")
    print("Welcome to the guest house, please select an option below")
    print("1. Book a room")
    print("2. View a room")
    print("3. Show Prices")
    print("4. Exit Program")
    choice= input("Please enter an option number now.")
    return choice #returns the user's choice

def space():
    print(" ")

def password():
    password = "hotel"
    enterpass = input("Enter password")

    while password != enterpass:
        print ("Password Incorrect, please try again"),
        enterpass = input("Enter password")

    if enterpass == password:
        print("Password Correct")

def exit_program():
    print("Exiting Program now....")
    time.sleep(1)
    pause_program()
    sys.exit()
    space()

def pause_program():
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")


def breakfast_double():
    breakfast1=input("Would you like breakfast?").lower()
    if breakfast1=="yes":
        print("Breakfast costs 5GBP per person")
        break_cost1=5*n #calcualtes the total cost of breakfast by multiplying by number of nights
        doubcost = 45*n+break_cost1 # calculates the total cost of breakfast,nights and room costs

    if breakfast1=="no":
        doubcost=45*n
        print("You have not added breakfast")
    space()
    return doubcost




def breakfast_single():
    breakfast=input("Would you like breakfast?").lower()
    if breakfast=="yes":
        print("Breakfast costs 5GBP per person")
        break_cost=5*n #calcualtes the total cost of breakfast by multiplying by number of nights
        sincost = 30*n+break_cost # calculates the total cost of breakfast,nights and room costs

    if breakfast=="no":
        sincost=30*n
        print("You have not added breakfast")
    space()
    return sincost


def number_nights():
    while True:
        try:
            n=int(input("How many nights would you like to stay? Between 1 and 7 nights."))
            if n>=1 and n<=7:
                space()
                print("You will stay for",n,"nights")
                break
            print("Please enter a valid number of nights")
        except Exception:
            print("Please enter a number")
    space()
    return n


def vat_single():
    vatcost=sincost/100*20
    total_single=sincost+vatcost
    print("The total cost without vat is GBP",sincost)
    space()
    print("The total cost including vat is GBP",total_single)
    space()
    return total_single

def vat_double():
    vatcost1=doubcost/100*20
    total_double=doubcost+vatcost1
    print("The total cost without vat is GBP",doubcost)
    space()
    print("The total cost including vat is GBP",total_double)
    space()
    return total_double



def show_prices():
    print("Prices are GBP30 for a single room")
    print("Prices are GBP45 for a double room")
    print("You can only book for 1 to 7 nights.")
    space()


def single_room_search():
    single_room = [1,2,3,4]

    single = False
    while single == False:
        print("Single rooms are numbered 1-4")
        space()
        room = int(input("Enter a room number"))
        if room in single_room:
            single_room.remove(room)
            print("You have selected room",room)
            chosen_room=room
            space()
            single=True
            space()
            print("the current rooms left are",single_room)
        else:
            print("Please enter a valid room number")
        return room


def double_room_search():
    double_room = [5,6,7]

    double = False
    while double == False:
        print("Double rooms are numbered 5-7")
        space()
        room1 = int(input("Enter a room number"))
        if room1 in double_room:
            double_room.remove(room1)
            print("You have selected room",room1)
            space()
            double=True
            space()
            print("the current rooms left are",double_room)
        else:
            print("Please enter a valid room number")
            print("Please enter a valid room number")


#MAIN PROGRAM-------------------------------------------------------------------
MainMenuLoop = True
while MainMenuLoop == True:
#Calls the MAIN MENU function and catches the return
    password()
    choice=MainMenu()
    if choice in ("1", "2", "3", "4"):
         break
    else:
        print ("You have chosen an invalid option try again")


if choice == "1":
        space()
        print ("You have selected option 1 to book a room")


        isValid = False

        while isValid== False:
            room_type=input("What room type would you like? Single or Double").lower()

            if room_type in ("single","double"):
                isValid = True
            else:
                print(room_type,"Is an invalid choice")


        if room_type=='single':
            print ("You have selected a single room")
            space()
            room=single_room_search()
            n=number_nights()
            sincost=breakfast_single()

            newspaper=input("Would you like to add a newspaper at cover price?").lower()
            if newspaper == "yes":
                print("Newspaper is 50p at cover price")
                space()
                news= 0.5
                total_cost=sincost+news
            if newspaper == "no":
                space()
                print("You haven't added a newspaper")

            total_single=vat_single()
            save_file_single()




        if room_type=='double':
            print ("You have selected a double room")
            doubcost = 45
            space()
            double_room_search()
            n=number_nights()
            doubcost=breakfast_double()

            newspaper1=input("Would you like to add a newspaper at cover price?").lower()
            if newspaper1 == "yes":
                print("Newspaper is 50p at cover price")
                space()
                news1= 0.5
                total_cost1=doubcost+news1
            if newspaper1 == "no":
                space()
                print("You haven't added a newspaper")

            vat_double()
            save_file_double()



if choice == "2":
        space()
        print ("You have seleced option 2 to view a room")

if choice == "3":
        space()
        print ("You have selected option 3 to show prices")
        show_prices()



if choice == "4":
        space()
        print ("You have selected option 4 to exit program")
        exit_program()