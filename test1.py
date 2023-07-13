import streamlit as st


#To reduce the padding in the top
st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)

#Header File
style = "<style>h2 {text-align: center;}</style>"
st.markdown(style, unsafe_allow_html=True)
st.columns(3)[1].header("I/P Reputation Checker and Geo Location")

st.divider()

