bikeNumbers = []
entryTimes = []
exitTimes = []
noOfHours = []
payments = []
totalPayment = 0
for index in range(1000):
    userinput = int(input("Entry(1) /Exit(2)/End of Day(3)"))
    if (userinput == 1):
        print("this is a bike entry")
        bikeNumber = input("Enter the bike number")
        entryTime = int(input("Enter the entry time in 12 hour format"))
        # adding elements into an array
        bikeNumbers.append(bikeNumber)
        entryTimes.append(entryTime)
        noOfHours.append(0)
        exitTimes.append(0)
        payments.append(0)

    elif(userinput == 2):
        print("this is a bike exit")
        # take input as bikenumber
        # exit time
        # find the index for that bike
        # get the entry time
        # calculate the no of hours
        # calculate payment
        # update the array
        # update the sumTotal
    elif(userinput == 3):
        print("End of Day")
        break
print("sum total")
print(bikeNumbers)
