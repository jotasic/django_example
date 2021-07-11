import requests
def client():
    data = {
        'username':'admin2',
        'email' : 'test@rest.com',
        'password1' : 'passowrd1234',
        'password2' : 'passowrd1234'
    }

    response = requests.post('http://localhost:8000/api/rest-auth/registration/', data=data)

    print('Status Code : ', response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == '__main__' :
    client()