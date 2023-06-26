
import requests

target_input = input("Target url:")
def make(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

with open ("wordlist.txt","r") as wordlist:
    for word in wordlist:
        word = word.strip()
        url ="http://" + word + "." + target_input
        response = make(url)
        if response is not None:#or if reponse:
            print("Found subdomain -->" + url)
