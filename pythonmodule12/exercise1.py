import requests.exceptions
requestURL="https://api.chucknorris.io/jokes/random"
def get_random_chuck_noris_joke():
    try:
        response=requests.get(requestURL).json()
        print(response['value'])
    except requests.exceptions.RequestException as e:
        print(f"Something is wrong: {e}")
def main():
    command=input("If you want to see a joke about Chuck Norris, then press 1, otherwise 0. ")
    while command=="1":
        get_random_chuck_noris_joke()
        print("-----------------")
        command=input("If you want to see a joke about Chuck Norris, then press 1, otherwise 0. ")
if __name__=="__main__":
    main()