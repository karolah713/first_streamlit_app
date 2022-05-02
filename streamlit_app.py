import streamlit
import pandas

streamlit.title("My Mom\'s New Healthy Diner")
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Bluberry Oatmeal')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.title("🍌🍓 Build your Own Fruit Smoothie 🥝🍇")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


#put a pick list so customer can pick the fruit he want to include
streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))

# display the table on the page
streamlit.dataframe(my_fruit_list)
