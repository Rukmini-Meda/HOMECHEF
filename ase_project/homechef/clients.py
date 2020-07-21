import requests


# url="http://127.0.0.1:8000/authapi/"
# response=requests.post(url,data={'username':'team30','password':'django30'})

# print(response.text)
URL="http://127.0.0.1:8000"

def get_data():
    url=f"{URL}/Vendor1/homechef/"
    token="b8cfa007006a530a111b75b997051dbb085d4f2c"
    header={'Authorization':f'Token {token}'}
    response=requests.get(url,headers=header)
    vendors_data=(response.json())
    for each in vendors_data:
        print(each)

get_data()