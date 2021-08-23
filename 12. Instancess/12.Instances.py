INSTANCES :
===========
Class - instance /
        object /
		ref. variable 

Python Code, Database: instances  

GITHUB:
-----------
main
  - development
      - 34533_featurebranch_1
	  - 65432_featurebracnh_2

clone the feature branch into local system


Python  ===> Local  --> DEV  --> TEST/QA  --> UAT/Staging --> PRODUCTION
Database ==>        DEV      --> TEST/QA  --> UAT/Staging --> PRODUCTION
                            DEV           --> UAT         --> PRODUCTION
									DEV/TEST/QA           --> PRODUCTION

flask   ==>  Local  --> DEV --> Staging --> Production   versioning/mongodb.py
database ==>       DEV      --> Staging  --> Production 





Scenarios :   XXX II. Local  --> PRODUCTION      
			     III. Local  --> DEV/Staging/Testing/QA  --> PRODUCTION
			      IV. Local  --> DEV -> Testing  --> PRODUCTION
			       V. Local  --> DEV  --> TEST/QA  --> UAT/Staging --> PRODUCTION

Local instance : http://127.0.0.1:5555/    127.0.0.1 or localhost or 0.0.0.0
				 As a developer  1. Will perform code changes in local system
								 2. Performs application testing in local system

Code changes : UI, Backend(Python)

REQ:   Update employee information
----------------------------------
1. Create feature branch in github   main/development/ 32424_Update_emp_info
2. Clone into local system, deploy and check for any issues/errors
3. Do functional/technical analysis for ticket 
4. Implement Design
5. As part of development,do code changes in the respective module .py file 
6. Redeploy the appication in local instance(environment) and test thoroughly using Postman/GUI
7. If everything working fine, push code to feature branch 
8. Give Build*(Docker,Bamboo etc.,) using build tools for feature branch 
9. If build is success 
				- Deploy the feature branch code to "DEV" instance, 
				  restart server in DEV instance
				- Test the functionality again in DEV instance 
10. Deploy the code to TEST instance. 
			    - Testing team will do testing and given apporval
				- Testing team will do testing and raises defects* (Repeat 5 to 10)
11. Deploy the code to UAT instance (Client approval)
12. Deploy the code to PRODUCTION instance 

Instaces:
---------------
Local instance - DEV - TEST - UAT - PROD **
Local instance - DEV - Staging - PROD
Local instance - DEV - Test/QA - PROD
Local instance - Staging - PROD

Local: http://localhost:5000/   or http://127.0.0.1:5000/
DEV  : http://dev.calculator.com or http://192.18.43.23:5000/
TEST : http://test.calculator.com or http://192.18.43.24:5000/ 
UAT  : http://uat.calculator.com  or http://192.18.43.25:5000/
PROD : http://prod.calculator.com  or http://calculator.com

credentials will be provided
Live url : http://calculator.com


SDLC Process:
-------------
Waterfall, V Model, Prototype model 

Agile, Scrum methodology

1. Requiment Gathering
2. Analysis Functional/Technical
3. Design 
4. Development
5. Testing
6. Production/Deployment


JIRA tool  <==> Story** - Ticket* - Requirement - Incident - Serivce Reuest(SR) 

 

1. Requiment Gathering: Product Owner 
						Story Jira ticket 
   Bitbucket Jira,GIT,Confluence 
   
   Sprint duration : 1 week,2 weeks**, 3 weeks,4 weeks 
   Sprint planning meeting:  story 1 2 3 5  points 
   
   Sprint 11 : 16-Aug-21(MON) 29-Aug-21(SUN)  10 Days
   3-Jun-21  : Sprint planning meeting - 1 HOUR
							- Story points discussion 
			
   100 stories
   5 Members 20 stories : product owner prioritizes the stories
   Poker game : 
   KT Process - domain knowledge,project setup 
   5 developers - 
   
   Story : 32423 : Truename change for entity
					   Dev1:   2
					   Dev2:   3
					   Dev3:   5 * - Why ?
					   Dev4:   2
					   Dev5:   1 * - Why ?
   
   points : 1 - 1-2 Days
			2 - 2-3 Days 
			3 - 5 Days
			5 - 10 Days 
			
  Story : 432423 : Modify name of user with full name in home page 
   Dev1:   1
   Dev2:   1
   Dev3:   2
   Dev4:   1
   Dev5:   1   
   
   each developer  should get 5 points for one sprint 
   Dev1 : 1 2 3 
   Dev2 : 3 3 
   Dev3 : 1 1 2 2 
   Dev4 : 3 2 1 
   
   20 stories - points - decided  
   
   
Monday morning:
-----------------
GITHUB  2 types of workflows:
------------------------------
F_Calculator
 - main
	- development
		- 3234_Name_change
		- 2322_Delete_user
		....

F_Calculator
 - main
	- development
		- fork the repository

	
	
Clone feature branch code into local system
		
		
2 Week Sprint:
------------------
Tickets will be assigned to respective developers
Through jira we can access tickets
Day1: - Go through story description,confirm the repository 
      - create feature branch under development branch
	  - clone into local system
	  - Open in pycharm, first deploy the application(python app.py) and 
		check whether it is working properly or not
	  - Prepare the API** - Request URL : /api/v1/namechange (http://localhost:5050)
							Request Method: POST
							Payload: {'userid':'mnettem','MadhuSudhanNettem'}
	  - Do code changes* (framework rules),
	  - Then test the new functionality through postman in local system
	  - Implement test cases(unit testing*),execute them and make sure all cases are success
	  - Github feature branch(git status,diff,add,commit,push).Push the code
	  - Bitbucket - GIT,Jira,Bamboo
		 - Deploy the feature branch changes to DEV instance
		   - As a backend developer,give build for feature brach
		   - If build is success,
		       - Then deploy code changes to DEV instance
			   - Restarts the server automatically
		9. If build is success 
						- Deploy the feature branch code to "DEV" instance 
						- Test the functionality again in DEV instance 
		10. Deploy the code to TEST instance. 
						- Testing team will do testing
		11. Deploy the code to UAT instance (Client approval)
		12. Deploy the code to PRODUCTION instance 





