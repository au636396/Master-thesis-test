import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

#GithubIcon {
  visibility: hidden;
}

####### this does nothing
# initializing with a random number
if "rn" not in st.session_state:
    st.session_state["rn"] = random.randint(1,100)

st.write('st.session_state.rn') # this doesnt work and i don't know why- !!! investigate, code from here: https://discuss.streamlit.io/t/randomly-generate-a-number-and-save-this-number-and-user-input/20615/4
############

#top text
"""
# Welcome to my eksperiment!

## Do you want cookies?
"""

col1, col2 = st.beta_columns([1,1])

st.write(st.session_state.condition)
st.write("hello")

with col1:
    button1 = st.button("Accepter alle", type="primary")
st.write(button1)

with col2:
    button2 = st.button("Avfis alle", type="primary")
st.write(button2)







###### the old pre-build stuff
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
