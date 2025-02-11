import requests

def create_jobs():
    print("Creating jobs")
    url = "https://google.com"
    response = requests.get(url)
    print(response.text)

