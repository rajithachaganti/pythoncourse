mongodb : 
------------
Mysql postgresql =>  Table         RECORD
Mongodb          ==> Collection    Document



{
    "_id" : ObjectId("5d258607f9c8e56192c77e5e"),
    "active_epe" : [ 
        "nmadhu"
    ],
    "base_part_name" : "17-14466",
    "fpd_part_name" : "17-14466-01",
    "last_updated_date" : ISODate("2019-08-13T06:37:40.885Z"),
    "software_type" : "FIRMWARE",
    "fpd_name" : "FAI_TEST_1",
    "mfg_implementation" : "Cut in",
    "fpd_status" : "Approved",
    "fpd_ver" : "v1.0",
    "user_id" : "nmadhu",
    "initiator_name" : "Mohammad Muhsin",
    "current_phase" : "Testing",
    "workflow" : {
        "unit_test_logs" : [ 
            {
                "testplanname" : "as",
                "urllink" : "fdsa",
                "tests" : "SWDE",
                "testowner" : "nmadhu",
                "formatted" : "07-15-2019",
                "comments" : "",
                "label" : "Unit Testing",
                "eta" : {
                    "label" : "",
                    "value" : {
                        "date" : {
                            "year" : 2019,
                            "day" : 15,
                            "month" : 7
                        }
                    },
                    "dateFormat" : "yyyy-mm-dd"
                },
                "test_files" : [ 
                    {
                        "uploaded_date_utc" : ISODate("2019-07-10T06:31:43.971Z"),
                        "file_upload" : true,
                        "file_id" : "626c058aa2dc11e993230050",
                        "file_size" : "0.047 KB",
                        "file_location" : "ftp://pcam-dev-app-01:2121/DevSCFtpServer/res/home/Software/FPD/Logs/626c058aa2dc11e993230050fil_upload.bin",
                        "file_name" : "fil_upload.bin",
                        "uploaded_by" : "nmadhu",
                        "is_active" : "Y",
                        "uploaded_date" : "07/10/2019 T02:31:43",
                        "file_md5" : "eba33de1ce09a35eba54b5fd8140db4e"
                    }
                ],
                "test_comments" : "",
                "test_status" : "pass",
                "updated_date" : ISODate("2019-07-10T06:31:46.684Z")
            }
        ],
		
        "workflow_id" : 1,
        "edvt_test_logs" : [ 
            {
                "testplanname" : "fsa",
                "urllink" : "saf",
                "tests" : "EDVT",
                "testowner" : "Guest",
                "formatted" : "07-15-2019",
                "comments" : "",
                "label" : "Qualification EDVT/DT",
                "eta" : {
                    "label" : "",
                    "value" : {
                        "date" : {
                            "year" : 2019,
                            "day" : 15,
                            "month" : 7
                        }
                    },
                    "dateFormat" : "yyyy-mm-dd"
                }
            }
        ],
        "source_code" : [],
        "ios_data" : [],
        "fpd_images" : [ 
            {
                "uploaded_date_utc" : ISODate("2019-07-10T06:30:52.613Z"),
                "file_name" : "fil_upload.bit",
                "file_size" : "0.047 KB",
                "is_active" : "Y",
                "uploaded_date" : "07/10/2019 T02:30:52",
                "file_md5" : "eba33de1ce09a35eba54b5fd8140db4e",
                "file_id" : "4335e5e6a2dc11e992910050",
                "uploaded_by" : "nmadhu",
                "size" : 48.0,
                "extension" : "bit",
                "file_location" : "ftp://pcam-dev-app-01:2121/DevSCFtpServer/res/home/Software/FPD/4335e5e6a2dc11e992910050fil_upload.bit"
            }, 
            {
                "uploaded_date_utc" : ISODate("2019-08-13T06:21:08.265Z"),
                "file_name" : "FW%3a_FPD_Code_Setup.zip",
                "file_size" : "212.00 KB",
                "is_active" : "Y",
                "uploaded_date" : "08/13/2019 T11:51:08",
                "file_md5" : "7a64b457dfe048f0a9efb12817aa8ef8",
                "file_id" : "7fad27c0bd9211e9883a185e",
                "uploaded_by" : "pparambi",
                "size" : 217092.0,
                "extension" : "zip",
                "file_location" : "ftp://pcam-dev-app-01:2121/DevSCFtpServer/res/home/Software/FPD/7fad27c0bd9211e9883a185eFW%3a_FPD_Code_Setup.zip"
            }, 
            {
                "uploaded_date_utc" : ISODate("2019-08-13T06:31:22.048Z"),
                "file_name" : "FW%3a_FPD_Code_Setup.zip",
                "file_size" : "212.00 KB",
                "is_active" : "Y",
                "uploaded_date" : "08/13/2019 T12:01:22",
                "file_md5" : "7a64b457dfe048f0a9efb12817aa8ef8",
                "file_id" : "ed7b6540bd9311e99414185e",
                "uploaded_by" : "pparambi",
                "size" : 217092.0,
                "extension" : "zip",
                "file_location" : "ftp://pcam-dev-app-01:2121/DevSCFtpServer/res/home/Software/FPD/ed7b6540bd9311e99414185eFW%3a_FPD_Code_Setup.zip",
                "zip_files" : [ 
                    "FPD Scope Environment.docx"
                ]
            }, 
            {
                "uploaded_date_utc" : ISODate("2019-08-13T06:37:40.412Z"),
                "file_name" : "README.md",
                "file_size" : "1.26 KB",
                "is_active" : "Y",
                "uploaded_date" : "08/13/2019 T12:07:40",
                "file_md5" : "c062cabd1ed6863492a58bae71fdfae2",
                "file_id" : "d6863580bd9411e98c13185e",
                "uploaded_by" : "pparambi",
                "size" : 1291.0,
                "extension" : "md",
                "file_location" : "ftp://pcam-dev-app-01:2121/DevSCFtpServer/res/home/Software/FPD/d6863580bd9411e98c13185eREADME.md",
                "zip_files" : []
            }
        ]
    },
    "created_by" : "nmadhu",
    "engineering_manager" : "fantony",
    "details" : {
        "sw_backword_compatability_comments" : "",
        "requested_eta" : "2019-7-15",
        "hw_backword_compatability" : "Y",
        "critical_warnings" : false,
        "reference" : "U7",
        "optional_test" : [],
        "bug_fixes" : "N",
        "board_version" : "73-18247-03",
        "diag_backword_compatability_comments" : "",
        "change_in_register_spec" : "N",
        "cardname" : "PCA,MBRD,Celeborn,ASR900 16 port GE C-SFP + 1 port SFP+ IM with MACsec",
        "notification_period" : "7",
        "cpn_raw_name" : "15-13375-01",
        "cdc_review" : "",
        "priority" : "S3",
        "diag_backword_compatability" : "Y",
        "cdets_number" : [ 
            {
                "priority" : "S3",
                "type" : "Bug Fixes",
                "number" : "212"
            }
        ],
        "sw_and_diags_approved" : "N",
        "known_issues" : "",
        "unconstrained_report" : true,
        "clocking_constraints" : false,
        "description" : "IC-LIN,VREG,QFN40,TPS40422,DUAL DC/DC,PMBUS SYNCHRONOUS BUCK CNTLR,Pb-FREE",
        "location_map_and_xml" : false,
        "part17_ver" : "IC-Programmed Device,VREG,QFN40,TPS40422,DUAL DC/DC,PMBUS SYNCHRONOUS BUCK CNTLR,Pb-FREE, Coleborn,U7",
        "unit_testing_details" : "",
        "hw_backword_compatability_comments" : "",
        "summary" : "212",
        "sw_backword_compatability" : "Y"
    },
    "revision" : "-01",
    "skipped" : [ 
        "Qualification EDVT/DT", 
        "Qualification QA"
    ],
    "accessible_to" : [],
    "component" : "17-14466-01",
    "base_part_version" : "01",
    "version_assigned_by_PE" : "17-14466-01",
    "last_updated_by" : "pparambi",
    "build_number" : "32",
    "progress_step" : 1,
    "initiator" : "nmadhu",
    "fpd_hierarchy" : {
        "project_name" : "Celeborn",
        "item_type" : "TAN",
        "item_name" : "68-100995-01",
        "bu" : "PABU",
        "assembly_name" : "68-100995-01",
        "pf" : "ASR900"
    },
    "uploader_name" : "Mohammad Muhsin",
    "release_date" : ISODate("2019-07-10T00:00:00.000Z"),
    "new_ver" : false,
    "offset_changed" : false,
    "default_accessible_to" : [ 
        "nmadhu"
    ],
    "created_date" : ISODate("2019-07-10T06:30:31.028Z"),
    "fpd_type" : "HW",
    "epe" : [ 
        "nmadhu"
    ],
    "init_approver" : [ 
        {
            "name" : "",
            "roles" : "epe/Initiator/Creator",
            "cecid" : "nmadhu",
            "stages" : [ 
                {
                    "mandatory" : false,
                    "enabled" : true,
                    "name" : "Unit Testing"
                }, 
                {
                    "mandatory" : true,
                    "enabled" : true,
                    "name" : "Unit Testing QA"
                }, 
                {
                    "mandatory" : false,
                    "enabled" : true,
                    "name" : "Qualification EDVT/DT"
                }, 
                {
                    "mandatory" : true,
                    "enabled" : true,
                    "name" : "Qualification QA"
                }, 
                {
                    "mandatory" : true,
                    "enabled" : true,
                    "name" : "Production Release"
                }
            ],
            "type" : "",
            "deletable" : false
        }
    ],
    "fpd_id" : "5d258607f9c8e56192c77e5e",
    "last_approver_status" : "Approved",
    "correlationId" : "5d258697f9c8e56193bf72ce"
}