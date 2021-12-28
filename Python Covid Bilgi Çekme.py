print("Covid Vaka Sayısı Görme Uygulamamıza Hoşgeldiniz.")
import requests  #Kullanılacak kütüphane

#API
url = "https://covid-api.mmediagroup.fr/v1/cases"

#datayı distionary olarak çekmek.
response = requests.get(url)
data = response.json()

#Kullanıcıdan ülke almak
country = input("ülke:")
country_data = data[country.title()]["All"] #ülke datasını çekme

#dataların sınıflandırılması ve değişken atama.
population = country_data["population"]
confirmed = country_data["confirmed"]
deaths = country_data["deaths"]

print("Nüfus:",population)
print("Toplam Vaka:", confirmed)
print("Toplam Ölüm:",deaths)