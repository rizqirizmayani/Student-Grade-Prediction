import streamlit as st
import pandas as pd
import pickle

#[theme]
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

st.title("Do you qualified to join The Government's New Program?")

# import model
model = pickle.load(open("M2P1_model.pkl", "rb"))

st.write('Insert feature to predict')

# user input
school_setting = st.selectbox(label='School Location', options=['Rural','Suburban','Urban'])
school_type = st.selectbox(label='School Type', options=['Non-public','Public'])
teaching_method = st.selectbox(label='Teaching Method', options=['Experimental','Standard'])
lunch = st.selectbox(label='Lunch', options=['Does not qualify', 'Qualifies for reduced/free lunch'])
gender = st.selectbox(label='Gender', options=['Female','Male'])

# convert into dataframe
data = pd.DataFrame({'school_setting': [school_setting],
                'school_type': [school_type],
                'teaching_method': [teaching_method],
                'lunch':[lunch],
                'gender': [gender]})

# model predict
clas = model.predict(data).tolist()[0]

# interpretation
if st.button('Predict'):
    st.write('Classification Result: ')
    if clas == 1:
        st.text("Qualified to Join The Program")
    else:
        st.text("Does't Qualified to Join The Program")