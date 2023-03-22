#take input from user of ip
ipaddress = input("enter a ip address")
#check the len of ip
lenofIp=len(ipaddress)
#print(lenofIp)
#if user give 8 digit ip
if(lenofIp==8):
    print(ipaddress[0:3],".",ipaddress[3:6],".",ipaddress[6:7],".",ipaddress[7:8])
#if user give 7 digit ip

elif(lenofIp==7):
    print(ipaddress[0:3],".",ipaddress[3:5],".",ipaddress[5:6],".",ipaddress[6:7])
#if user give 6 digit ip

elif(lenofIp==6):
    print(ipaddress[0:3],".",ipaddress[3:4],".",ipaddress[4:5],".",ipaddress[5:6])



