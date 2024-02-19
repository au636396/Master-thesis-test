import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to my eksperiment!

## popup
"""

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #7CE1EE;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #6DCDDA;
    color:#ffffff;
    }
</style>""", unsafe_allow_html=True)




#adding themning (i hope)
primaryColor="#7CE1EE"
secondaryColor="7CEE80"
#backgroundColor="#FFFFFF"
#secondaryBackgroundColor="#F0F2F6"
#textColor="#262730"
#font="sans serif"


button1 = st.button("Accepter alle", type="primary")
st.write(button1)

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #7CE1EE;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #6DCDDA;
    color:#ffffff;
    }
</style>""", unsafe_allow_html=True) 

button2 = st.button("Afvis alle", type="secondary")
st.write(button2)


num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
