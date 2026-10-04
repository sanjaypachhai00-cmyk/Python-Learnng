#API(Application Programmed Interface)
import requests
def fetch_api():
    url ="https://api.freeapi.app/api/v1/public/randomusers"
    response=requests.get(url)
    data=response.json()
    if data["success"] and "data" in data:
        u_data=data["data"]
        u_name=u_data["login"]["username"]
        return u_name
def main():
    try:
        fetch_api()
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
