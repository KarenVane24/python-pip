import requests

def get_categories():
    r=requests.get("https://api.escuelajs.co/api/v1/categories") #conectarse a un servicio web y utilizar los datos
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories=r.json()
    for category in categories:
        print(category["name"])