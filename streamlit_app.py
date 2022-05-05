import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title("My Mom\'s New Healthy Diner")
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Bluberry Oatmeal')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.title("🍌🍓 Build your Own Fruit Smoothie 🥝🍇")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#Choose the Fruit Name Column as the Index
my_fruit_list = my_fruit_list.set_index('Fruit')

#put a pick list so customer can pick the fruit he want to include
fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the table on the page
streamlit.dataframe(fruits_to_show)

#create the reapeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
  fruitvice_response = requests.get("https://www.fruityvice.com/api/fruit/" + this_fruit_choice)
  fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())
  returned fruitvice_normalized

#NewcSelection to display fruitvice api response
streamlit.header('Fruitvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input("What fruit would you like information about?")
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()

# don't run anything past here while troubleshoot
streamlit.stop()

# import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
add_my_ftuit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanka for adding ', add_my_ftuit)

my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")


