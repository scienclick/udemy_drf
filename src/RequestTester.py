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


#testing a filter
ROOT="http://127.0.0.1:8000/"
GETALL_endpoint="prop-posts/?type=&from_timestamp_date=&to_timestamp_date=&min_buyingprice=30000&max_buyingprice=75000"
r = requests.get(ROOT+GETALL_endpoint, headers=headers)
r.status_code
r.content

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