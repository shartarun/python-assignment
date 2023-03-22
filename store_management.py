#fire question are you enter a new invoice


#for customerInvoiceIndex in range (10000):

#customer file in  
def customerinvoice():
            customerInvoiceFile=open("customer_invoice.csv", 'a+')

            customerInvoiceNumbers=0
            #print(firstAskToUser)
            #take input from user
            customerName=input("enter a customer name")
            customerMobileNumber=input("enter a customer mobile number")
            for index in open("customer_invoice.csv", 'r'):
                if customerInvoiceNumbers != (customerInvoiceNumbers[index]):
                    print(customerInvoiceNumbers)
                
            #customerInvoiceNumbers +=  1
            #ocustomerInvoiceNumber=customerInvoiceNumbers

            customerInvoiceFile.write("\n" + str(customerInvoiceNumbers) +"," + customerName +","+  str(customerMobileNumber))  
            
            customerInvoiceFile.close()

    firstAskToUser=input("Do you enter a invoice yes or no") 
    

    if (firstAskToUser=="yes"):
        
        def customerinvoice():
            customerInvoiceFile=open("customer_invoice.csv", 'a+')

            customerInvoiceNumbers=0
            #print(firstAskToUser)
            #take input from user
            customerName=input("enter a customer name")
            customerMobileNumber=input("enter a customer mobile number")
            for index in open("customer_invoice.csv", 'r'):
                if customerInvoiceNumbers != (customerInvoiceNumbers[index]):
                    print(customerInvoiceNumbers)
                
            #customerInvoiceNumbers +=  1
            #ocustomerInvoiceNumber=customerInvoiceNumbers

            customerInvoiceFile.write("\n" + str(customerInvoiceNumbers) +"," + customerName +","+  str(customerMobileNumber))  
            
            customerInvoiceFile.close()


    else:
        print("no")
        break

    customerinvoice()
