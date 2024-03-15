import streamlit as st

#removing the side bar, header, and footer
st.set_page_config(initial_sidebar_state="collapsed")

css='''
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)

col1, col2, col3 = st.columns([2,1,2])
#The visuals
st.write("##### "+"Tak for at du ville svare på mit spørgeskema.")
st.write("##### "+"Click på knappen under for at gå til spørgeskemaet.")
st.write()
with col2:
    st.link_button("**Til spørgeskema**", "https://survey.au.dk/LinkCollector?key=VC8ZRNUQUN16")
