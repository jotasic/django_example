import requests
def client():
    #credentials = {'username':'admin', 'password' : '1'}
    token_h = 'Token d90f568c35e1eb5650ca3980181e16049f655bd0'
    headers  = {'Authorization' : token_h}
    response = requests.get('http://localhost:8000/api/profiles/', headers=headers)

    print('Status Code : ', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__' :
    client()