1. Install below requirements
    > python -m pip install requirements.txt
2. Deploy the application using below command
    > python app.py
       
API Calls: Access these calls from postman

1. Save the data 

Request URL : http://127.0.0.1:5444/api/v1/datapart 
    Method  : POST 
    Payload : {
                "userId": 101,
                "title" : "Madhu Nettem Software Engineer",
                "body" : "Sample Data"
            }
            
2. Retrieve the data 

Request URL : http://127.0.0.1:5444/api/v1/datapart 
    Method  : GET 

3. Update the data 
4. Delete the data 
