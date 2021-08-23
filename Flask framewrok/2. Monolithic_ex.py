Flask
-----------
project - service/application
		  Flask - monolithic service
				- micro services
		  
		  Djagno- single application
				  mulitple applications
				  
		  
		  
		  
- monolithic      - 1 single service                - MVC framework
- micro services  - multiple services (5 services*) - MVC, EBI


	API Call:
	---------
		Request URL    :   www.paytm.com/api/v1/signup
		Request Method :   POST, GET, PUT, DELETE						
		Payload        :  {username,pssword,mobile,mailid}
	
	Client --> Server
	
	


SDLC phases:
-------------
Req Gathering - Product owner, Sprint planning meeting
Analysis      - Functional/Technical analysis
Design        - 
Development
Testing
Production


Story: Find length of string


Project setup document:
-----------------------
Step1 : README.md file
Step2 : python -m pip install -r requirements.txt
Step3 : python fpd_app.py
		You will see a message reagarding app deployment in server
		


UI --->   Controller      Service + DAO      Mongodb 
           fpd_app.py     fpd.py
		   

CAlCULATOR PROGRAM:
========================
API CALL:
-----------
Request URL    : http://localhost.com:4000/add
Request Method : POST
Payload        : {"argument1":10,
                  "argument2":20
				  }

Response:  Success: {'answer': 100}
		   Format issue: Error message
		   Data issue: {'answer': "Enter input as numbers"}
		   
		   
Multiplication:
--------------
Request URL   : http://127.0.0.1:4000/multiply
Request Method: POST
	 Payload  : {"argument1":"10",
				 "argument2":"20"
				}

MVC Architecture:
===================
			

MVC Architecture:
------------------ 
		 Model      - DAO Classes <---- Database(Create Models)
		 View       - UI   
		 Controller - Controller
		              Service
		
		UI   -> Controller  -> Service -> DAO   -> DB
		View    Controller                Model 




View          Controller             Model
----------------------------------------------- 
UI  --> Controller  --> Service    --> DAO        --> DB

Controller -> 1.  Receive data(json to dict) from Frontend(UI)
			  2.  Perform server side validations
			  3.  Process the data to service layer
			 11.  Receives response from service,sends to UI

Service    -> 4.  Receives data from controller layer
              5.  Implement business logic as per funtionality
			  6.  Call DAO layer and pass data to perform db ops
			  9.  Perform data processing on db results
			  10. Send final data to controller layer
			  
DAO        -> 7. Receive the data from service layer and perfrom db query
			  8.  Send response to  service layer 
			  
			  
UI ----->    Controller     ---->    Service         ----->   DAO    ----> Database
   API Call  fpd_app.py             			create_fpd.py
				create_fpd():           				CreateFPD
															save()

