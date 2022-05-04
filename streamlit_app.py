import streamlit
import pandas


streamlit.title("My Mom\'s New Healthy Diner")
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Bluberry Oatmeal')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.textstreamlit.text('🥑🍞 Avocado Toast')

streamlit.title("🍌🍓 Build your Own Fruit Smoothie 🥝🍇")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#Choose the Fruit Name Column as the Index
my_fruit_list = my_fruit_list.set_index('Fruit')

#put a pick list so customer can pick the fruit he want to include
fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the table on the page
streamlit.dataframe(fruits_to_show)

#NewcSelection to display fruitvice api response
streamlit.header('Fruitvice Fruit Advice!')
fruit_choice = streamlit.text_input("What fruit would you like information about?", "Kiwi")
streamlit.write('The user entered', fruit_choice)

import requests
fruitvice_response = requests.get("https://www.fruityvice.com/api/fruit/" + fruit_choice)


# take the json version of the response and normalize it
fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())
# output it the screen as a table
streamlit.dataframe(fruitvice_normalized)


