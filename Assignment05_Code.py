#Assignment 5
#Author = Jeremy Rabbe
#Date = Nov 12, 2018


# Step 1 - Load data from a file
# When the program starts, load each "row" of data
# in "ToDo.txt" into a python Dictionary.
# Add the each dictionary "row" to a python list "table"


#Define the objects used
objFileName = open("C:\_PythonClass\Assignment05\Todo.txt", "r") #Used to be "a" for append
strData = ""
dicRow = {}
lstTable = []
RowNumb = 0

#Create a loop for each line in the .txt file and assign a row number
for line in objFileName:
    RowNumb += 1
    strData = line.split(",")
    dicRow = {"ID": RowNumb, "Task":strData[0], "Priority":strData[1].strip("\n")}
    lstTable.append(dicRow)



# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Your current ToDo list consists of the following", "\n", lstTable)
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newTask = input("What is your new Task?: ")
        newPriority = input("What is the priority? (high/med/low) ")
        newRow = {"ID": RowNumb + 1, "Task": newTask, "Priority": newPriority}
        lstTable.append(newRow)
        continue

    # Step 5 - Remove a new item to the list/Table
    elif (strChoice == '3'):
        RemoveTask = int(input("Which task would you like to remove? (Please type ID): ")) - 1
        print("\nOkay,",lstTable[RemoveTask]["Task"]," has been deleted.")
        del lstTable[RemoveTask]
        continue

    # Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        FileSave = input("Would you like to save this file? (Y/N) ")
        if(FileSave.lower() == "y"):
            objFileNew = open("C:\_PythonClass\Assignment05\Todo.txt", "a")
            objFileNew.write(str(lstTable))
            objFileNew.close()
            print("Data has been saved to ToDo.txt")
            continue
        else:
            continue

    elif (strChoice == '5'):
        break  # and Exit the program

