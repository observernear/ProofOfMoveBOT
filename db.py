import requests


res = requests.post(url='https://proofofmove.ru/api', json={'tg_id': 5064842218})
print(res.json())