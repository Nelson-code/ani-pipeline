import requests
url="https://accounts.spotify.com/api/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Data for the POST request
data = {
    "grant_type": "client_credentials",
    "client_id": "<your clien_id>",
    "client_secret": "<your client_secret>"
}
# POST call
response=requests.post(url,headers=headers,data=data)
response.json()