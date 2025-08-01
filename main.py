import requests





response=requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json"
)
##url yanlis yazilirsa response 404 hatasi gelir
##200 ler gelirse okeydir
##300 ler baska yerlere yonlendirendir
##500 ler sunucu hatasi
"""
if response.status_code==200:
    for crypto in response.json():
        print(crypto["price"])  ##currency yazarsak tum coinleri gosterir,price yazarsak fiyatlari
"""

def get_crypto_data():
    response=requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json"
)
    if response.status_code==200:
        return response.json()


crypto_response = get_crypto_data()
user_input = input("Enter you crypto currency: ")
x=0
for crypto in crypto_response:
    x += 1
    print(x)
    if crypto["currency"] == user_input:
        print(crypto["price"])
        break

##BİRDEN FAZLA İSLEM YAPTİRMA (SENKRON CALİSTİRMA)




"https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json"




