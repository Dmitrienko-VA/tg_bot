import requests
import datetime
from pprint import pprint
from config import ow_token


def get_weather(city, ow_token):
    try:
        req = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={ow_token}&units=metric"
        )
        data = r.json()
        temp = data["main"]["temp"]
        print(f"Температура: {temp}C°\n")

    except Exception as ex:
        print(ex)
        print("Я не знаю такого города(((")


def main():
    city = input("Жду название города: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()

