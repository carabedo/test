import requests as rq

url='https://7pyngmccwa.execute-api.us-east-1.amazonaws.com/default/apitest'

data={'q':'pan lactal'}
data=rq.get(url)
print(data)