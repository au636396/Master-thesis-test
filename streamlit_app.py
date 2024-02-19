import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to my eksperiment!

## popup
"""

#adding themning (i hope)
primaryColor="#7CE1EE"
secondaryColor="7CEE80"
#backgroundColor="#FFFFFF"
#secondaryBackgroundColor="#F0F2F6"
#textColor="#262730"
#font="sans serif"

#test
animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'

#end of test

button1 = st.button("test", type="primary")
st.write(button1)
button2 = st.button("test1", type="secondary")
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
