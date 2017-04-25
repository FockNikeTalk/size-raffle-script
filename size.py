import requests
from random import getrandbits
url = 'http://size-client-resources.s3.amazonaws.com/assets/pages/yeezyRaffle/app-raffle.html'
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

print("Size? Raffle made by @Fockniketalk")		   

# CHANGE THESE VALUES
def main(limit):
    for i in range(1, limit):
        email = 'youremail+{}@gmail.com'.format(getrandbits(40)) # put your email in for your email
        payload = {
            'name': 'Mark dark', # put your first and last name here 
            'address': 'cooklane 2', # put your adress here
            'postcode': 'sm71aa', # put your zipcode here
            'telephone': '12345678910', # ' put your phonenumber here without spaces, for example 12345678910
            'email': 'test@gmail.com', # put your email here
            'shoeSize': '9', # put ONE shoe size, like 10, 9 1/2, etc.
            'store': 'London', # put store here
        }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    main(1000000)
