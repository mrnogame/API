import streamlit as st 
import os
from dotenv import load_dotenv
import requests
import numpy as np



def main():
 load_dotenv('.env')
api_key : str = os.getenv('API_KEY')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'



st.title('WEATHER PREVISION')

city = st.text_input('Enter the city')
result = requests.get(url.format(city, api_key))     




json['main']['temp']




   








if __name__ == "__main__":
    main()




