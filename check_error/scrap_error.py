import requests

def check_if_error(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            print("It's ok")
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else:", err)

    if response.status_code == 200:
        return 200


if __name__ == "__main__":
    url = input("Enter url: ")
    check_if_error(url)
