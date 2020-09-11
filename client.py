import requests
r =requests.get('http://127.0.0.1:5000/', params={
    'sentence': "I charge it at night and skip taking the cord with me because of the good battery life.",
    'aspect': "cord",
    'start': 41,
    'end': 45
})

print(r.text)