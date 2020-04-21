import requests
import json

BASE_URL = 'localhost:9091/'

print("\n")
#일반 get request
response = requests.get(BASE_URL + 'userList/v1.0')
data = response.json()
print("1. 유저리스트 조회 : ", data['check'])

#일반 post request에 params 세팅 후 전송
params = {'key1' : 'value1',
          'key2' : 'value2'}
response = requests.post(BASE_URL + 'userInfo/v1.0/post', params)
data = response.json()
print("2. 유저정보 업데이트 is : ", data['check'])

#PUT 헤더와 파라미터 세팅
header = {
    "accept" : "application/json",
    "Content-Type" : "application/json;charset=UTF-8"
}
params = {'key1' : 'value1',
          'key2' : 'value2'}
response = requests.put(BASE_URL + 'userInfo/v1.0/put', headers = header, data = json.dumps(params))
data = response.json()
print("3. 유저정보 저장 is : ", data['check'])

#GET 요청 파라미터 추가 타입
response = requests.get(BASE_URL + 'userDetail/v1.0/get/' + str(userList['response'][0]['userSeq']))
data = response.json()
print("4. 유저상세조회 is : ", data['check'])

#GET 요청 파라미터 세팅 타입
params = {'key1' : 'value1',
          'key2' : 'value2'}
response = requests.get(BASE_URL + 'stock/v1.0/list', params=params)
data = response.json()
print("5. 유저특성조회 is : ", data['check'])