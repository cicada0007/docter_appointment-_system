



listPnt = ["Ramesh", "Suresh", "Gopi", "Varun"] 

def managePatients(): 

	print(""" 

  ----------------------------------------------------------------
 |================================================================| 
 |======== Welcome To Doctor Appoinment Management System ========|
 |============== Srinivas Multispeciality Hospital ===============|
 |================================================================|
  ----------------------------------------------------------------

Enter 1 : To View Patient's List 
Enter 2 : To Add New Patient
Enter 3 : To Search Patient 
Enter 4 : To Remove Patient 
		
		""")
	userInput=int(input("Enter the above option to access the patient list :"))

	
	if(userInput == 1): 
		print("List Patient's\n")  
		for patients in listPnt:
			print(" {}".format(patients))

	elif(userInput == 2): 
		newPnt = input("Enter New Patient: ")
		if(newPnt in listPnt): 
			print("\n This Patient {} Already In The Database".format(newPnt))  
		else:
			listPnt.append(newPnt)
			print("\n New Patient {} Successfully Add \n".format(newPnt))
			for patients in listPnt:
				print(" {}".format(patients))	

	elif(userInput == 3): 
		srcPnt = input("Enter Patient Name To Search: ")
		if(srcPnt in listPnt): 
			print("\n Record Found Of Patient {}".format(srcPnt))
		else:
			print("\n No Record Found Of Patient {}".format(srcPnt)) 

	elif(userInput == 4): 
		rmPnt = input("Enter Patient Name To Remove: ")
		if(rmPnt in listPnt):  
			listPnt.remove(rmPnt)
			print("\n Patient{} Successfully Deleted \n".format(rmPnt))
			for patients in listPnt:
				print(" {}".format(patients))
		else:
			print("\n No Record Found of This Patient {}".format(rmPnt)) 
	 
	elif(userInput < 1 or userInput > 4): 
		print("Please Enter Valid Option")	
						

managePatients()

def runAgain(): 
	runAgn = input("\nwant To Run Again Y/n: ")
	if(runAgn.lower() == 'y'):
		managePatients()
		runAgain()

runAgain()











