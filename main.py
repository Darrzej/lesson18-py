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

st.write(books_df.head())

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 book titles!")
    top_title = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_title)

with col2:
    st.subheader("Top 10 book authors!")
    top_authors = books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)  

st.subheader("genre Distribution")
fig = px.pie(books_df, names="Genre", title='Most liked Genre 2009-2022', color="Genre",
             color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig) 

st.subheader("Top 15 Authors")
top_authors = books_df['Author'].value_counts().head(15).reset_index()
top_authors.columns=['Author','Count']

figg = px.bar(top_authors, x='Count', y='Author', orientation='h',
              title='Top 15 Authors',
              labels={'Count': 'Counts of Books Published','Author':'Author'},
              color='Count', color_continuous_scale=px.colors.sequential.Plasma
              )

st.plotly_chart(figg)


# df = pd.DataFrame({
#     'Name': ['Hivzi', 'Klajdi', 'Alphonso'],
#     'Age': [5, 69, 21],
#     'City': ['New York', 'Banula', 'Malisheve']

# })

# st.write(df)