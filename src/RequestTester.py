import requests
import json

ROOT="http://127.0.0.1:8000/"
POSTS_ENDPOINT="api/news/"

# <editor-fold desc="News">
data = {
    "title": "Nazdaq Stocks are going down after US China trade talks",
    "sentiment": "pn",
    "entities4thisnews": [

        {
            "entity": "US",
        },
        {
            "entity": "China",
        }
        ,
        {
            "entity": "China",
        }
    ]
}


headers = {
    "Content-Type": "application/json",
}
#post
r = requests.post(ROOT+POSTS_ENDPOINT, data=json.dumps(data), headers=headers)
r.text
r.content
r.status_code

#get all
GETALL_endpoint="api/news/"
r = requests.get(ROOT+GETALL_endpoint, headers=headers)
r.status_code
r.content

#get one
GETONE_endpoint="api/news/7"
r = requests.get(ROOT+GETONE_endpoint, headers=headers)
r.status_code
r.content


#PATCH
PATCH_endpoint="api/news/7"

data = {
    "sentiment": "n",
}

r = requests.patch(ROOT+PATCH_endpoint, data=json.dumps(data), headers=headers)
r.status_code
r.content

#DELETE
DELETE_endpoint="api/news/6"
r = requests.delete(ROOT+DELETE_endpoint, headers=headers)
r.status_code
r.text
r.content
# </editor-fold>



ROOT="http://127.0.0.1:8000/"
POSTS_ENDPOINT="prop-posts/"
# <editor-fold desc="POST">
# post a house
data = {
    "type": "LAND",
    "square": 100,
    "buyingprice": 25000,
    "description": "best house",
}

headers = {
    "Content-Type": "application/json",
}
#post
r = requests.post(ROOT+POSTS_ENDPOINT, data=json.dumps(data), headers=headers)
r.text
r.content
r.status_code
# </editor-fold>


# <editor-fold desc="GET with filters">
#testing a filter
ROOT="http://127.0.0.1:8000/"
GETALL_endpoint="prop-posts/?type=&from_timestamp_date=&to_timestamp_date=&min_buyingprice=30000&max_buyingprice=75000"
r = requests.get(ROOT+GETALL_endpoint, headers=headers)
r.status_code
r.content
# </editor-fold>

# <editor-fold desc="POST/PATCH figures">
# testing sending photos
root = "http://127.0.0.1:8000/"
POSTS_ENDPOINT = root + "images/"
img_path1 = r"C:\Users\ashamsa\Desktop\a.jpg"
img_path2 = r"C:\Users\ashamsa\Desktop\b.jpg"

data = {
    "prop_post": 8,
}
headers = {
    # "Content-Type": "application/json",
}

# post
r = requests.post(POSTS_ENDPOINT, data=data, files={'photo': open(img_path1, 'rb')}, headers=headers)

# put
data = {
    "prop_post": 5,
}
POSTS_ENDPOINT = root + "images/4"
r = requests.patch(POSTS_ENDPOINT, data=data, files={'photo': open(img_path1, 'rb')}, headers=headers)
# </editor-fold>


# <editor-fold desc="POST without/with Token">
data = {
    "type": "LAND",
    "square": 100,
    "buyingprice": 25000,
    "description": "house without a token",
}

headers = {
    "Content-Type": "application/json",

}

r = requests.post(ROOT+POSTS_ENDPOINT, data=json.dumps(data), headers=headers)
r.text
r.content
r.status_code


# headers with invalid token
t1="a"
headers = {
    "Content-Type": "application/json",
    "Authorization": "JWT " + t1,
}

r = requests.post(ROOT+POSTS_ENDPOINT, data=json.dumps(data), headers=headers)
r.text
r.content
r.status_code

# getting token
def get_token(username='admin1', password='admin1'):
    AUTH_ENDPOINT = "http://127.0.0.1:8000/token/"

    data = {
        'username': username,
        'password': password
    }
    headers = {
        "Content-Type": "application/json"
    }
    r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
    token = r.json()["token"]

    return token
t1=get_token()
t1

headers = {
    "Content-Type": "application/json",
    "Authorization": "JWT " + t1,
}

r = requests.post(ROOT+POSTS_ENDPOINT, data=json.dumps(data), headers=headers)
r.text
r.content
r.status_code

# </editor-fold>

# <editor-fold desc="user interactions">
#------------- sign in
def get_token(username='admin1', password='admin1'):
    AUTH_ENDPOINT = "http://127.0.0.1:8000/token/"

    data = {
        'username': username,
        'password': password
    }
    headers = {
        "Content-Type": "application/json"
    }
    r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
    token = r.json()["token"]

    return token
t1=get_token()
t1

data = {
    "type": "LAND",
    "square": 100,
    "buyingprice": 25000,
    "description": "just added house",
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "JWT " + t1,
}

r = requests.post(ROOT+POSTS_ENDPOINT, data=json.dumps(data), headers=headers)
r.text
r.content
r.status_code

# ----------change password
ENDPOINT = 'http://127.0.0.1:8000/rest-auth/password/change/'

data = {
    'new_password1': 'sssma502',
    'new_password2': 'sssma502'

}
headers = {
    "Content-Type": "application/json",
    "Authorization": "JWT " + t1
}

r = requests.post(ENDPOINT, data=json.dumps(data), headers=headers)
r.text
r.content

# ----------reset password
ENDPOINT = 'http://127.0.0.1:8000/rest-auth/password/reset/'

data = {
    'email': 'amirshamsa@gmail.com',
}
headers = {
    "Content-Type": "application/json",
}

r = requests.post(ENDPOINT, data=json.dumps(data), headers=headers)
r.text
r.content
#-------------Registration
ENDPOINT = 'http://127.0.0.1:8000/rest-auth/registration/'

data = {
    'username': 'amirshamsa',
    'email': 'amirshamsa@gmail.com',
    'password1': 'jhk1128f',
    'password2': 'jhk1128f'
}
headers = {
    "Content-Type": "application/json",
}
r = requests.post(ENDPOINT, data=json.dumps(data), headers=headers)
r.text
r.content
# </editor-fold>