#Take input from user how many cars come
cars=input("enter the total number of cars enter today")
#How many hours they parked
totalCarsParkingHours=input("enter the total car parking hours")
#take input from user how many bikes come
bikes=input("enter the total numbers of Bike enter today")
#how many hours the bikes parked
totalBikesParkingHours=input("enter the total bikes parking hours")
#calulating the money of cars parking
carsParkingMoney=int(cars)*int(totalCarsParkingHours)*50
#calulating the money of bikes parking
bikesParkingMoney=int(bikes)*int(totalBikesParkingHours)*10 
#adding the total money of cars and bikes parking
adding=carsParkingMoney+bikesParkingMoney
#showing details total details 
print("total cars=", cars)
print("total cars hours=", totalCarsParkingHours)
print("total bikes=", bikes)
print("total cars hours=", totalBikesParkingHours)

#show the total money 
print("Total Money",adding)
#how much we recived
recivedPayment=int (input("total money we recived"))
#checking the total money we recived 

if(adding == recivedPayment):
  print("succesful")
   
else:
    print("Missmatch=",adding-recivedPayment)
    
