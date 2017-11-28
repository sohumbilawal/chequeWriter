###############################################################################
#Code written by Sohum Bilawal Joshi on 11/27/2017
#Edit/ Version history:
    #Sohum Bilawal Joshi 11/27/2017
    #...
###############################################################################
#Please keep the line(s) above as they are, and you can ONLY add your own name
#and date stamp after you have made changes to it.
#DO NOT delete the name of the previous contributor(s).
#Use the code responsibly, and for academic purposes ONLY.
#Not for commercial use or monetary benefit of any users without prior consent.
#Thank you.
###############################################################################

#This program takes as input a dollar amount in numerical format
#(float). The program essentially “reads the numbers” and outputs a
#string of the numbers in word form. This is akin to a check writer
#(where you need an amount in both numbers and words), and thus the name.

amount = float(input("Please enter the amount in numbers: $")) # take input in numeric form with type float
amount = float(format(amount, '0.2f')) # modify numeric input to round up to only 2 decimal places
#print(amount, type(amount))

strAmt = str(amount) # change type of modified float to string for easy modification
#print(strAmt, type(strAmt))

# print(len(strAmt))

# 3 lists of possible outcomes. Can be used both for before and after decimal work
units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
theTeens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["Zero", "Ten", "Twenty","Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninty"]

powers = ["Hundred", "Thousand", "Million", "Billion", "Trillion"]
# Go through string and get two parts: before decimal (befDec) and after decimal (aftDec)
printer = []

n = 0
for n in range(0, len(strAmt)):
    if strAmt[n] == ".":
        befDec = strAmt[0:n]
        aftDec = strAmt[n+1:]
        #print(befDec, aftDec)

# len is 1 and index 0 is 0

# Logic to pick pieces of lists up depending on length, and then value of the number
# Create concatenated string called centsPrint to later add to dollarPrint and create a full output

if len(aftDec) == 1:
    if int(aftDec[0]) == 0:
        centsPrint = " and "+ units[int(aftDec[0])] + " cents"
    elif int(aftDec[0]) != 0:
        centsPrint = " and " + tens[int(aftDec[0])] + " cents"
    else:
        print("Error with code")

if len(aftDec) == 2:
    if int(aftDec[0]) == 0 and int(aftDec[1]) == 1:
        centsPrint = " and " + units[int(aftDec[1])] + " cent"
    elif int(aftDec[0]) == 0:
        centsPrint = " and " + units[int(aftDec[1])] + " cents"
    elif int(aftDec[0]) == 1:
        centsPrint = " and " + theTeens[int(aftDec[1])] + " cents"
    elif int(aftDec[0]) != 0 and int(aftDec[0]) != 1:
        centsPrint = " and " + tens[int(aftDec[0])] + " " + units[int(aftDec[1])] + " cents"
    elif int(aftDec[0]) != 0 and int(aftDec[0]) != 1 and int(aftDec[1]) == 0:
        centsPrint = " and " + tens[int(aftDec[0])] + " cents"
    else:
        print("Error with code with length 2")

printer.insert(0, centsPrint)

#print(centsPrint)

if len(befDec) == 0:
    dollarPrint = "Zero dollars"

    printer.insert(0,dollarPrint)
    #print(dollarPrint, centsPrint)

if len(befDec) == 1 and int(befDec[0]) == 1:
    dollarPrint = units[int(befDec[0])] + " dollar"
    printer.insert(0,dollarPrint)

elif len(befDec) == 2 and int(befDec[0]) == 1:
    dollarPrint = theTeens[int(befDec[1])] + " dollars"
    printer.insert(0,dollarPrint)

elif len(befDec) == 2:
    dollarPrint = tens[int(befDec[0])] + " " + units[int(befDec[1])] + " dollars"
    printer.insert(0,dollarPrint)

else:

    i = 0
    for n in range(0, int(len(befDec)/3)):
        prn1 = befDec[len(befDec)-((3*n)+3):len(befDec)-(3*n)]
        #print(prn1)
        tens1 = prn1[1:]
        #print("The tens piece", tens1)
        if i == 0:
            if int(tens1[0]) == 0 and int(tens1[1]) == 1:
                dollarPrint = " and " + units[int(tens1[1])] + " dollar"
            elif int(tens1[0]) == 0:
                dollarPrint = " and " + units[int(tens1[1])] + " dollars"
            elif int(tens1[0]) == 1:
                dollarPrint = " and " + theTeens[int(tens1[1])] + " dollars"
            elif int(tens1[0]) != 0 and int(tens1[0]) != 1 and int(tens1[1]) == 0:
                dollarPrint = " and " + tens[int(tens1[0])] + " dollars"
            elif int(tens1[0]) != 0 and int(tens1[0]) != 1:

                dollarPrint = " and " + tens[int(tens1[0])] + " " + units[int(tens1[1])] + " dollars"
            else:
                print("Error with code with length 2")

            printer.insert(0,dollarPrint)

        elif i != 0:
            if int(tens1[0]) == 0 and int(tens1[1]) == 1:
                dollarPrint = " and " + units[int(tens1[1])] + " " + powers[int(i)] + " "
            elif int(tens1[0]) == 0:
                dollarPrint = " and " + units[int(tens1[1])] + " " + powers[int(i)] + " "
            elif int(tens1[0]) == 1:
                dollarPrint = " and " + theTeens[int(tens1[1])] + " " + powers[int(i)] + " "
            elif int(tens1[0]) != 0 and int(tens1[0]) != 1:
                dollarPrint = " and " + tens[int(tens1[0])] + " " + units[int(tens1[1])] + " " + powers[int(i)] + " "
            elif int(tens1[0]) != 0 and int(tens1[0]) != 1 and int(tens1[1]) == 0:
                dollarPrint = " and " + tens[int(tens1[0])] + " " + powers[int(i)] + " "
            else:
                print("Error with code with length 2")

            printer.insert(0,dollarPrint)


        hund1 = prn1[0]
        #print("The hundreds piece", hund1)
        #if int(hund1[0]) == 0:
        #    dollarPrint2 = units[int(hund1[0])] + " hundred"
        if int(hund1[0]) != 0:
            dollarPrint2 = units[int(hund1[0])] + " hundred"
        else:
            dollarPrint2 = ""

        #print(dollarPrint2, dollarPrint) #Printing here!

        print("i is equal to:", i)
        printer.insert(0,dollarPrint2)
        i += 1

subPow = len(befDec) % 3
#if subPow != 0:
#    i += 1

if subPow == 1:
    prn2 = befDec[0:subPow]

    extraNum = units[int(prn2[0])] + " " + powers[int(i)] + " "

    #print(extraNum, powers[i])

    #print(extraNum, powers[i+1], dollarPrint2, dollarPrint) #Printing here!
    printer.insert(0,extraNum)

    #if int(prn2[0]) == 0:
    #    extraNum = " and " + units[int(prn2[0])] + powers[int(i+1)]
    #elif int(prn2[0]) != 0:
    #    extraNum = " and " + tens[int(aftDec[0])] + powers[int(i+1)]
    #else:
    #    print("Error with code")

elif subPow == 2:
    prn2 = befDec[0:subPow]

    #extraNum = tens[int(prn2[0])] + " " + units[int(prn2[1])] + " " + powers[int(i+1)]

    if int(prn2[0]) == 1: #Must keep for teens
        extraNum = theTeens[int(prn2[1])] + " " + powers[int(i)] + " "
    elif int(prn2[0]) != 0 and int(prn2[0]) != 1: #What happens when the format is not 0 or 1 at [0]
        extraNum = tens[int(prn2[0])] + " " + units[int(prn2[1])] + " " + powers[int(i)] + " "
    elif int(prn2[0]) != 0 and int(prn2[0]) != 1 and int(prn2[1]) == 0:
        extraNum = tens[int(prn2[0])] + " " + powers[int(i)] + " "
    else:
        print("Error with code with length 2")

    #print(extraNum, powers[i+1], dollarPrint2, dollarPrint) #Printing here!
    printer.insert(0,extraNum)

else:
    printOutput = ""
    for n in range(0, len(printer)):
        printOutput = printOutput + printer[n]
    print(printOutput)
    #print(dollarPrint2, dollarPrint) #Printing here!

printOutput = ""
for n in range(0, len(printer)):
    printOutput = printOutput + printer[n]
print(printOutput)
#print(dollarPrint3, dollarPrint2, dollarPrint) #Printing here!

#print(len(befDec))
#print(powers[i])

#power = int(len(befDec) / 3)
#subPow = int(len(befDec) % 3)

#print(power, subPow)
#print(powers[power + subPow])

#if len(befDec) < 3:



#if subPow != 0:
#    for n in range(0, power + 1):
#        #print(powers[n])
#        print("Printing power + 1")
#
#elif subPow == 0:
#    for n in range(0,power):
#        #print(powers[n])
#        print("Printing power")

#if len(befDec) == 1:
#    if int(befDec[0]) == 1:
#        dollarPrint = units[int(befDec[0])] + " dollar"
#
#    else:
#        dollarPrint = units[int(befDec[0])] + " dollars"
