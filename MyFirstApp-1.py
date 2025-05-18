# pip install --upgrade langchain langchain-google-genai streamlit
# pip install streamlit

import os
os.environ['GOOGLE_API_KEY'] = 'AIzaSyCTYMstDJnYkDYp1MU2RFo0OO01nLacr6k'

from langchain_google_genai import ChatGoogleGenerativeAI
gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

from langchain import PromptTemplate

fact_template = """Give me top {number_of_key_takeaways} key takeaways from the book {book_name}"""

fact_prompt = PromptTemplate(template = fact_template, input_variable = ["number_of_key_takeaways","book_name"])

from langchain import LLMChain
fact_chain = fact_prompt | gemini_model

import streamlit as st
st.header("Book Summary")

st.subheader("Top takeaways from your favourite book")

book_name = st.text_input("Book name")

number_of_key_takeaways = st.number_input("Number of takeaways",min_value =1,max_value = 20, value = 1, step = 1 )

if st.button("Get the summary"):
    book_summary = fact_chain.invoke({"book_name": book_name, "number_of_key_takeaways" : number_of_key_takeaways, })   
    st.write(book_summary.content)
