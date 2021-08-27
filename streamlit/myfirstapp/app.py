import streamlit as st

import numpy as np
import pandas as pd
import datetime

st.title('My first app')

st.write('Here is your first attemp at using data to create a table:')
st.write()
df = pd.DataFrame({
    'firstcolumn': [1,2,3,4],
    'secondcolumn': [10,20,30,40]
})

df 

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.area_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76, -122.3],
    columns=['lat','lon']
)

st.map(map_data)

#use checkbox to show and hide specific chart or section

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c']
    )
    chart_data

if st.checkbox('show text'):
    st.write("Hi checkbox")


# use selectbox to choose from a series of options

option = st.selectbox(
    'Which number do you like the most?',
    df['firstcolumn']
)

'You selected: ', option

#Layout
df_menu = pd.DataFrame({'menu': ['Home', 'About', 'Contact']}) 

df_menu

option = st.sidebar.selectbox(
    'Which number do you like the most?',
    df_menu['menu']    
)
'You selected:', option

st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

#streamlit radio

genre = st.radio(
    'What is your favorite movie genre',
    ('Comedy', 'Drama', 'Action', 'Documentary')
)
# if genre == 'Comedy':
st.write('You selected ', genre)

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

number = st.number_input('Insert a number')
st.write('The current number is ', number)


def run_sentiment_analysis(txt):
    if len(txt) < 10:
        return 'negative'
    return 'positive'

txt = st.text_area('Text to analyze', '''
    It was the best of times ''')

st.write('Sentiment:', run_sentiment_analysis(txt))

d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))

st.write('Your birthday is:', d)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
