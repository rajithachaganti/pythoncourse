import requests
'''
client - our python program    <------->     server - reqres.in

'''



url = 'https://reqres.in'  # hdfcbank.com

def list_users():
    print("---------Get all users information-----------")
    # Prepare API CALL    f_url get
    suf = '/api/users?page=2'
    f_url = url+suf
    data = requests.get(f_url)  # Web service call
    print(data.json())
    data = data.json()
    for key, val in data.items():
        print(key, val)
        if key == 'data':
            for record in val:
                print(record)

def get_single_user(u_id):
    print("---------Get single user information-----------")
    suf = '/api/users/'+str(u_id)
    f_url = url+suf
    data = requests.get(f_url)
    print(data.json())
    data = data.json()
    for key, val in data.items():
        print(key, val)
        if key == 'data':
            for key,val in val.items():
                print(key,"-----",val)

def create_user():
    print("---------Create user-----------")
    suf = '/api/users/'
    f_url = url+suf
    user_info = {"name": "Madhu Nettem",
                 "job": "Software Engineer",
                 "loc": "Bangalore"}
    resp = requests.post(f_url, data=user_info)
    print(resp, resp.json())



if __name__ == '__main__':
    list_users()
    get_single_user(10)
    create_user()
