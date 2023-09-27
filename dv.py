import pandas as pd
import streamlit as st
df = pd.DataFrame(
{
    'sr.no' : [1,2,3,4,5],
    'gender' : ['m','f','f','m','m'],
    'weights' : [50,55,60,70,75],
    'heights' : [5.5,5.7,5.8,5.9,6.2]
})


st.table(df)
st.scatter_chart(df)
st.line_chart(df)