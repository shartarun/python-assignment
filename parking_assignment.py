#bike parking assignment
Bike_number=[]
Bike_Entry_Time=[]
Bike_Exit_Time=[]
Total_Hours=[]
Total_Payment=[]
Cash_Recived=[]
Total_Money_at_the_end=[]
Bike_Charge_per_hour=20
Exit_Bike=0
TotalHours=0
Total_Bike_Enter=0
Exit_Bike_Index_Value=0


for parkingProble in range(1000):
    asking_for_entry_or_exit=input("is this entry, exit or end of the day y/n/d")
    if(asking_for_entry_or_exit=="y"):
        #ask user to enter a bike Number
        Bike_numbers=input("enter a bike number")
        Bike_number.append(Bike_numbers)
        #ask user to enter a bike entry time
        Bike_Entry_Times=input("enter a bike entry time")
        Bike_Entry_Time.append(Bike_Entry_Times)
        #ask user to enter a bike exit time
        Bike_Exit_Times=input("enter your  exit time")
        Bike_Exit_Time.append(Bike_Exit_Times)

        #Total_Hours =Bike_Exit_Time[0] - Bike_Entry_Times[0]
        #print(Bike_number)
       # print(Bike_Entry_Time[0])
        #print(Bike_Exit_Time)
        
        
        
    elif asking_for_entry_or_exit=="n":

        Exit_Bike=input("enter a exit bike number")

       # print(Bike_number[parkingProblell] )
        if Exit_Bike in Bike_number:
            Exit_Bike_Index_Value=Bike_number.index(Exit_Bike)
            print(Exit_Bike_Index_Value)
            Bike_entryTime=Bike_Entry_Time[Exit_Bike_Index_Value]
            Bike_exitTime=Bike_Exit_Time[Exit_Bike_Index_Value]
            Total_Hour=int(Bike_exitTime) - int(Bike_entryTime)
            Total_Hour*=Bike_Charge_per_hour
            print(Total_Hour)
        

            

                
        #for Bike_Search in range(3):
            
         #   if Exit_Bike==Bike_number[Bike_Search]:
          #       #print(Bike_Search)
              #  Bike_entryTime=Bike_Entry_Time[Exit_Bike_Index_Value]
              #  Bike_exitTime=Bike_Exit_Time[Exit_Bike_Index_Value]
              #  Total_Hour=int(Bike_exitTime) - int(Bike_entryTime)
              #  Total_Hour*=Bike_Charge_per_hour
              # print(Total_Hour)
    else:
        TotalBikes=len(Bike_number)
        print(TotalBikes)
        for total_entry_hours in range(TotalBikes):
            total_bike_entry_time=Bike_Entry_Time[total_entry_hours]
            total_bike_exit_time=Bike_Exit_Time[total_entry_hours]
            Total_hours_per_bike=int(total_bike_exit_time)-int(total_bike_entry_time)
            TotalHours +=Total_hours_per_bike
            if total_entry_hours==2:
                
                print("Total Parking Hours for Today ", TotalHours)
                TotalHours *=20
                print("Total Payment of Today is ", TotalHours)
                collect=int(input("how much cash given today"))
                check=TotalHours-collect 
                print(" Today Total Payment is missing ",check)
                break
        break       