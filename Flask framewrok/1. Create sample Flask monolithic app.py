Flask - monolithic
	  - micro services
	  

Flask Monolithic application:
=============================
with MVC Design pattern

GUI   --request->                   Python                        ---> DATABASE

					-->  Controller -->  Service --> DAO     <---
      <-response-   <--             <--          <--         <---

VIEW                          CONTROLLER            MODEL
-----                         ----------            -----

View 	     - GUI
Controller   - Controller+Service
Model        - DAO 


CLIENT    				<------->     SERVER
			
GUI 								  Remote machine where our app got deployed
	Browser*
	Postman tool*
	Curl command
	Swagger tool



# Get all employees info 

/getallemps



API Call:
---------
GET :
------
Request URL    : www.xyz.com/api/v1/emp_ops/101
Request Method : GET


POST:
-----
Request URL    : www.xyz.com/api/v1/get_data
Request Method : POST
Payload        : {username:'Mnettem',
                  pssword,
				  mobile,
				  mailid
				 }


Code walkthrough:
-----------------
Step1 : Check "README.md" file
        Provides instructions to seup the project in local system  
		(OR)
	    Separate word document(10 pages) installation steps
	
Step2 : Go through "requirements.txt"
        Pyhton Software(builtin) + 
		External libraries*   (site-packages folder)
		aniso8601 : Logical behavior. Parse a time, get a datetime.time. Parse a date, get a datetime.date. UTC offset represented as fixed-offset tzinfo. Parser separate from representation
		Flask **
		Flask-APScheduler
		Flask-Compress
		Flask-Cors*
		Flask-HTTPAuth*
		Flask-Mail
		flask-profiler
		Flask-PyMongo*
		Flask-RESTful**
		Flask-SQLAlchemy*
		Flask-Triangle		
		pyexcel
		pymongo**
		pytz
		requests**
		SQLAlchemy

Step3 : Install respective libraries using below command
		> python -m pip install -r requirements.txt

Step4 : Create app.py and configure sample program

Step3 : Find starting point the application 
        python module name(.py file) : Which helps to deploy the service
		
		> python app.py 
		================
			C:\Users\madhu\AppData\Local\Programs\Python\Python36\python.exe C:/Users/madhu/git_projects/Batch_17/B17_Flask_Sample/app.py
			 * Serving Flask app "app" (lazy loading)
			 * Environment: production
			   WARNING: This is a development server. Do not use it in a production deployment.
			   Use a production WSGI server instead.
			 * Debug mode: on
			 * Restarting with stat
			 * Debugger is active!
			 * Debugger PIN: 287-867-620
			 * Running on http://localhost:4000/ (Press CTRL+C to quit)
		
		
Open browser and enter below url :
-----------------------------------
http://localhost:4000/

Observe the response

http://localhost:5433/                      --> Hello World.Welcome to Python world.
http://localhost:5433/getlen/'Hello World'  --> Hello World <--> 11
http://localhost:5433/getallnumbers         --> {'7406900500':32,.....}
	
