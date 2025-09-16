import pandas as pd
import streamlit as st
import plotly.express as px

books_df = pd.read_csv('file.csv')
st.title('Best selling books!')
st.write('These are the best books from 2009 to 2022')
st.subheader('Here are the statistics')
total_books = books_df.shape[0]
unique_title = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1,col2,col3,col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique title", unique_title)
col3.metric("Average rating", average_rating)
col4.metric("Average price", average_price)


# df = pd.DataFrame({
#     'Name': ['Hivzi', 'Klajdi', 'Alphonso'],
#     'Age': [5, 69, 21],
#     'City': ['New York', 'Banula', 'Malisheve']

# })

# st.write(df)