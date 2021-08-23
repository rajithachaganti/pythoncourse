Build and Deployment process :
=============================
Bitbucket (Git,Bamboo,Jira,Confluence)                                 + Docker
-------------------------------------------------------------------------------------------------------------------------------
1. Clone central repo feature branch into local system                 1.Same
2. Import into IDE like Eclipse,Pycharm								   2.Same 
3. Do project setup                                                    3.Same 
4. Do code changes as per requirement                                  4.Create latest DOCKER image,and run docker-compose yaml file    
    4.1 Start server locally => python manage.py runserver(django)		       > docker-compose up 
	                         => python app.py (flask)
5. Through postman test the functionality                              5. Through postman test the functionality
      5.1. Test the service individually                                     5.1. Test the service individually(Optional)
      5.2*.Perfrom integration testing by running and deploying              5.2. Create docker images locally for the respective service with latest tag
		   all services                                                      5.3. Modify docker-compose file service with latest tag
		   (This step is not required if we have Docker setup)   			 5.4  Restart the server ... docker-compose down ---> docker-compose up
6. Push the code to github feature branch,                             6. Create new Docker image with latest tag and push to docker hub      
7. MB *:Give build for the same(will generate with new build #)        7. Inform DEVOPS team about latest image fo the respective service 
   AB* :After git push,will trigger jenkins build automatically     
8. Deploy the latest build to DEV/TEST/UAT/PROD as per requirement        DEVOPS team will give build for same,and deploys to DEV/TEST/UAT instances
9. Create Pull Request to merge feature branch with "development"      8. Check the functionality in DEV instance
10.Peers(peer review) will review the code and gives comments
11.After code refactoring/Fixing Code review comments,
   peers will give approval.
12.Merge the feature branch code to development branch


