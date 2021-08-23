Local changes to Local Docker(All modules)	
Go to yaml file path	
		>docker ps -a     (Displays Running images)
		
Stop all docker images	
       >docker stop $(docker ps -aq)

Remove all docker images	
       >docker rm $(docker ps -aq)  OR  
	   >"docker-compose down"    (from same file location)
	   >docker ps -a     => No images

If any volumes missing like kafka postgres	
       >docker volume create --name=postgresql-volume
		docker volume create --name=kafka-volume
		docker volume create --name=cassandra-volume
		docker volume create --name=minio-volume

For manual docker image creation at local	
		C:\Users\user\git\my_service> docker build -t my_service:0.0.4 .

Now run docker image with latest tag	
       >docker-compose up
	   
Go to Browser/Postman	and run
		http://localhost:8080/#/dashboard

docker-compose up     5 TO 10 MINUTES 
docker-compose down


docker-compose up

flask
-----------
10 micro services

2 micro services
REPORTING   : 0.0.6
monintoring : 0.0.5

docker iamge : 0.0.6
               0.0.5
			   
DEV TEST UAT PROD

>python app.py


GITHUB Central repo 