Controller  : fpd_app.py 

				Mappings:
				----------
				Way1:
				-------
					@my_app.route("/api/createFPD", methods=['POST'])
					def create_fpd():
						.....
						

				Way2:  Partial mapping at package level 
				-------
					my_app.register_blueprint(devScAssist, url_prefix="/api/support")
					
					my_app.register_blueprint(fai, url_prefix="/api/fai")
									
									fai/fai_app.py
										fpd_fai.add_url_rule('/firstArticleMaster',
															 'generate FAI', 
															 get_fai_by_fpd, 
															 methods=['POST']
															 )
												 
					
					my_app.register_blueprint(fpd, url_prefix="/api/fpd")


					http://localhost:5050/api/fai/firstArticleMaster
				
				Way3:  versioning/fpd/urls.py
			    ------

Controller2: versioning/fai/controller/fai.py 
Controller3: versioning/fpd/controller/fpd.py 




 
> versioning.fpd.controller.fpd.py   > views.py
		def general_file_upload():
	
	
general_file_upload():
-------------------------	
	UI ---file data ----->    controller   ---> Service + DAO    -----> Database	
							  fpd.py            file_hanlder.py
						 
create_fpd():
-----------------
	UI      ------ >    Controller         Service + DAO   ---->  Databbase
	UI       ------>     fpd.py      --->  crate_fpd.py
												CreateFPD
						  
						  
						  
						  
						  
						  
						  
						  
						  
						  
						  



fpd_app.pyexcel
------------------
@fpd_app.route("/api/isFpdNameAvailable",methods=['POST'])
def is_fpd_name_available():

fai_api.py
----------
fpd_fai.add_url_rule('/firstArticleMaster','generate FAI', get_fai_by_fpd, methods=['POST'])





	
Flask monolithic:
--------------------
- reamd.MD           ==> project setup
- requirements.txt
- 



virtual environment advantnages usage
> pip install -r requirements.txt

C:\Users\madhu>pip install chardet
Requirement already satisfied: chardet in c:\users\madhu\appdata\local\programs\python\python36\lib\site-packages (3.0.4)



Request URL : "/api/createFPD",
Request method ='POST'

fpd_app.py ==> Controller
create_fpd.py ==> Service+DAO



'''
Request URL : http://paytm.com/api/createFPD
Request Method:POST
Payload : {'base_part_name':100,
           'fpd_part_name':'B13_PythonTraining_123_MadhuNettem',
           'base_part_version':'abc',
           }
'''
@fpd_app.route("/api/createFPD",methods=['POST'])
def create_fpd():
    # 1. Receives request from UI*
    req = request.json
    env = get_env_from_origin(request)
    # 2. Extract the data*
    if "base_part_name" not in req and "base_part_version" not in req:
        req['base_part_name'] = req['fpd_part_name'][:8]
        req['base_part_version'] = req['fpd_part_name'][8:]

    fpd_obj = CreateFPD(req)

    # 3. Perform server side validations
    # 4.2. send exception message to UI
    if not fpd_obj.is_valid_fpd_name():
        return jsonify({"status": "failure", 'message': "Fpd name is already exist"})
    '''
    is_valid_fpd = fpd_obj.is_valid_fpd_name()
    if not is_valid_fpd:
        msg = {"status": "failure", 'message': "Fpd name is already exist"}
        return jsonify(msg)
    '''
    if not fpd_obj.is_valid_part_version():
        return jsonify({"status": "failure", 'message': "Fpd part version is already exist"})
    if not fpd_obj.is_valid_fpd_version():
        return jsonify({"status": "failure", 'message': "Fpd version is already exist".format(req['fpd_name'])})

    # 4.1. pass data to service layer
    response = fpd_obj.save()
    # 13. Receive the data from Service, and send to UI
    return jsonify(response)



    def save(self):
        """  
  request param :{"fpd_name":"FPD_Chirag_531",
                  "fpd_part_name":"17-14459-01",
                  "fpd_ver":"V1.2",
                  "release_date":"2018-8-10",
                  "fpd_type":"HW",
                  "fpd_hierarchy":{"bu":"PABU",
                                   "pf":"ASR900",
                                   "item_name":"NCS4200-1T16G-PS",
                                   "item_type":"PID",
                                   "project_name":"Celeborn"
                                   },
                  "details":{"cpn_raw_name":"16-100373-01",
                             "reference":"",
                             "description":"IC-EEPROM-S,I2C ,ASR900, Celeborn IM  , U67",
                             "cardname":"PCA,MBRD,Celeborn,ASR900 16 port GE C-SFP + 1 port SFP+ IM with MACsec",
                             "part17_ver":"IC-EEPROM-S,I2C,16Kb,400kHz,1.8 to5.5 V,SO8,-40 to 85 C"
                             },
                  "approvers":[{"phase":"Initiate",
                                "approver":"cdaas",
                                "approver_name":"",
                                "manager_id":""
                                }
                                ]
            }
"""
        # todo check for unique fpd name .And if name is same then versioning  ?
        # 5. Receives the data from Controller
        fpd_data = self.request
        # self.info("Data received from ui : ",fpd_data['fpd_name'])
        # 6. Implement business logic for the given requirement
        fpd_data['fpd_status'] = 'Draft'
        fpd_data['current_phase'] = 'Unit Testing'

        if fpd_data['initiator'] == fpd_data['user_id']:
            fpd_data["initiator_name"]= fpd_data['uploader_name']
            fpd_data["default_accessible_to"] = [fpd_data['user_id']]
        else:
            fpd_data["initiator_name"] = ExternalApi().get_user_details(user=fpd_data['initiator'])[0]['cn']
            fpd_data["default_accessible_to"] = [fpd_data['initiator'], fpd_data['user_id']]
        fpd_data["accessible_to"] = []
        fpd_data['version_assigned_by_PE'] = ""
        fpd_data['build_number'] = ""
        fpd_data['revision']=""
        fpd_data['component']=""
        fpd_data['skipped'] = []
        fpd_data['mfg_implementation'] = "cut in"
        fpd_data['created_by'] = fpd_data['user_id']
        fpd_data['created_date'] = datetime.utcnow()
        fpd_data['last_updated_by'] = fpd_data['user_id']
        fpd_data['last_updated_date'] = datetime.utcnow()
        fpd_data['offset_changed'] = False

        str_date = fpd_data.get('release_date', "")
        str_date = get_current_date("%Y-%m-%d") if str_date=="" else str_date
        fpd_data['release_date'] = datetime.strptime(str_date, "%Y-%m-%d")

        # todo fetch only active workflow
        fpd_data['workflow'] = {
            # todo fetch workflow_id from jbpm api
            "workflow_id": 1,
            "approvers": fpd_data.get('approvers',[]),
            "ios_data": [],
            "source_code": [],
            TEST_LOG_DB_KEY["Unit Testing"]: [],
            TEST_LOG_DB_KEY["Qualification EDVT/DT"]: [],
        }
        try:
            del fpd_data['approvers']
        except Exception:
            pass
        # 7 8 9 10 11
        mongo.collection.insert(fpd_data)

        # 12. Receive the data from DAO , perform other operations on data and return the response to Controller
        if fpd_data['_id']:
            return fpd_data
        return False