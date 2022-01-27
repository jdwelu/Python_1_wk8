#!/usr/bin/env python3

# Going to make an Error Log program.
# 1.) Define functions for each specific task needed.
# 2.) Create an input/option loop.


# Making a function to read the error log file w/error handling.
def readFile():
    try:
        filepath = input("Please enter the filepath: ")
        # filepath = "error_log.txt" # File is in current working directory.
        print()
        
        fileObject = open(filepath, "r")
        line = fileObject.readline()
        while(line != ""):
            print(line, end="") # Error file spaces are actually read as str.
            line = fileObject.readline()
        fileObject.close()
    except Exception as e:
        print()
        print(" *** ERROR HAS OCCURRED *** ")
        print("Error Type:", type(e))
        print("Error:", e)
        print("Error Arguments:", e.args)

# Calling the readFile() function.
# readFile()


# Creating a function to find "[Error]" in error_log file w/error handling.
def readFileError():
    try:    
        filepath = input("Please enter the filepath: ")
        # filepath = "error_log.txt" # File is in current working directory.
        print()
        
        fileObject = open(filepath, "r")
        line = fileObject.readline()
        while(line != ""):
            if "[error]" in line:
                print(line)
            line = fileObject.readline()
        fileObject.close()
    except Exception as e:
        print()
        print(" *** ERROR HAS OCCURRED *** ")
        print("Error Type:", type(e))
        print("Error:", e)
        print("Error Arguments:", e.args)

# Calling the readFileError() function.
# readFileError()


# Creating a function to find "statistics" in error_log file w/error handling.
def readFileStat():
    try:    
        filepath = input("Please enter the filepath: ")
        # filepath = "error_log.txt" # File is in current working directory.
        print()
        
        fileObject = open(filepath, "r")
        line = fileObject.readline()
        while(line != ""):
            if "statistics" in line:
                print(line)
            line = fileObject.readline()
        fileObject.close()
    except Exception as e:
        print()
        print(" *** ERROR HAS OCCURRED *** ")
        print("Error Type:", type(e))
        print("Error:", e)
        print("Error Arguments:", e.args)

# Calling the readFileStat() function.
# readFileStat()


# Creating a function to find "[info]" in error_log file w/error handling.
def readFileInfo():
    infocount = 0
    infototal = 0
    try:    
        filepath = input("Please enter the filepath: ")
        # filepath = "error_log.txt" # File is in current working directory.
        print()
        
        fileObject = open(filepath, "r")
        line = fileObject.readline()
        while(line != ""):
            if "[info]" in line:
                # print(line)
                infocount = infocount + 1
                # print(infocount)
                # print()
            line = fileObject.readline()
        fileObject.close()
        print("Total number of lines with an '[info]' statement = ", infocount)
    except Exception as e:
        print()
        print(" *** ERROR HAS OCCURRED *** ")
        print("Error Type:", type(e))
        print("Error:", e)
        print("Error Arguments:", e.args)

# Calling the readFileStat() function.
# readFileInfo()


# Creating a function to find Client Address in error_log file w/error handling.
# This is a pretty dirty method of finding the IP, but I couldn't think of any
# other way.
def readFileAddress():
    try:    
        filepath = input("Please enter the filepath: ")
        # filepath = "error_log.txt" # File is in current working directory.
        print()
        
        fileObject = open(filepath, "r")
        line = fileObject.readline()
        while(line != ""):
            if "[info]" in line:
                # Turns each line into a list, assigns to a variable.
                address0 = line.split(" ")
                
                # Address is the 8th element.
                # This further splits the 8th element.
                # This also uses split to strip the "]" out. (Down to 2 elements.)
                address1 = address0[8].split("]")

                # Testing the result.
                # Still have invalid IP entries for the 8th element.
                # print(address1[0])
                # print()

                # Splitting even further, and assigning to another variable.
                address2 = address1[0].split(".")
                
                # IP addresses have 4 numbers. Using len() to test list for IP.
                # Oh, and why not put an extra check in for the numbers too?
                if len(address2) == 4 and address2[0].isdigit() and address2[1].isdigit() and address2[2].isdigit() and address2[3].isdigit():
                    # Printing each element and cocantenating the "." back in.
                    print(address2[0]+"."+address2[1]+"."+address2[2]+"."+address2[3])
                    
            line = fileObject.readline()
        fileObject.close()
    except Exception as e:
        print()
        print(" *** ERROR HAS OCCURRED *** ")
        print("Error Type:", type(e))
        print("Error:", e)
        print("Error Arguments:", e.args)

# Calling the readFileAddress() function
# readFileAddress()




# Start of the main program
print()
print("*****************************************")
print("Welcome to the Python ERROR LOG ANALYZER!")
print("*****************************************")
print()

# Defining the loop condition
# Considered using try and except, but my orginial loop works on (str).
condition = "y"

while condition == "y":
    print()
    print("Please choose one of the following options: ")
    print()
    print(" 1.) Display the entire file for review.")
    print(" 2.) Display lines that contain an '[error]' statement.")
    print(" 3.) Display lines that contain a 'statistics' statement.")
    print(" 4.) Display lines that contain an '[info]' statement.")
    print(" 5.) Display the client IP address for any line that \n     contains an '[info]' statement.")
    print()
    choice = input("Choice: ")
    if choice == "1":
        print()
        readFile()
        print()
        print()
    elif choice == "2":
        print()
        readFileError()
        print()
    elif choice == "3":
        print()
        readFileStat()
        
    elif choice == "4":
        print()
        readFileInfo()
        
    elif choice == "5":
        print()
        readFileAddress()
        print()
    else:
        print()
        print("*** invalid entry ***")
        print()

    print()
    print()
    condition = input("Press 'y' to continue, anything else will exit?: ")







