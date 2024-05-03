import requests

url = "https://gmailnator.p.rapidapi.com/generate-email"

payload = { "options": [1, 2, 3] }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "e29e01c71dmsh698b9b170e3796fp1d1494jsn6b9283b78115",
	"X-RapidAPI-Host": "gmailnator.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())