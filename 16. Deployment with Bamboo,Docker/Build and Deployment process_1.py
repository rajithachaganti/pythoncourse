GIT, Jira, Bitbucket , Bamboo
===============================
GIT      : Workflows 
		   Versioning  main --> development --> feature branches --> Local cloning
					   main --> development --> fork repo        --> local cloning
					   
Jira     : Ticket/Stories creation ,tracking
Bamboo   : Build and Deployment 

Local --> DEV --> TEST/QA --> UAT --> PROD




Build and Deployment using Bamboo*
------------------------------------
Step1 : In Sprint planning meeting,story will be assigned (Through Jira)
		Bitbucket -> Jira ticketing tool
		Story dashboard https://www.youtube.com/watch?v=foWlWD__5m4
		
Step2 : First day of sprint,Monday
		Go to respective Jira ticket,and analyse ticket.
Step3 : Create feature branch and clone into local system
Step4 : Peform functional analysis(DEV/TEST instance)  
		 - Existing flow(existing functionality related to current ticket) 
		 - Expected flow(as per ticket)
Step5 : Peform technical analysis(Local pycharm ide code) Technical analysis
		 - Existing flow(existing functionality related to current ticket) 
		 - Expected flow(as per ticket)
		 - Identify the existing API 
Step6 : Design and then start implementing the code
Step7 : Test the code changes locally(Through API tool like postman,swagger)
Step8 : Write unit test cases 
Step9 : Push the code to feature branch(GIT/ Bitbucket)
Step10* : Give build for the same branch(Bamboo).
		  Latest build no will get generated(243)
          BITBUKET, Bamboo -> featurebranch/- Build -- latest build#. 
Step11  : Deploy into DEV instance.
          Test the changes in DEV instance
Step12  : Create PR to merge feature branch to development branch by giving peer names.
Step13  : Merge the feature branch to development branch
		  Restart the build and deployment cycle wrt TEST instance 
		  



Local --> DEV --> TEST --> UAT --> PROD 

development - 256 
	-t1code 257 
	-t2code 258
	-t3code 259
	
			260

--------------------------

https://reqres.in/api/users
POST
{
    "name": "morpheus",
    "job": "leader"
}
		
		