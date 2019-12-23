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
