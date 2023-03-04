import requests

user_input = input("Please enter the city: ")

response = requests.get("http://api.openweathermap.org/data/2.5/weather?&q=" + user_input + "&appid=0888d6d73eeb6588a5b5da08f4d32bb9")
res = response.json()

#for result in res.items():
#    print (result)

print(res['main']["humidity"])




#print (res.values())

#headers_value = response.headers.values
#print(headers_value)