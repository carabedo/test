import requests as rq

url='https://7pyngmccwa.execute-api.us-east-1.amazonaws.com/default/apitest?q=pan lactal'

data=rq.get(url).json()

for x in data:
    print(x)
