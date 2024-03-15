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

#The visuals
st.subheader('Tak for at du ville svare på mit spørgeskema.')
st.subheader("Click på knappen under for at gå til spørgeskemaet.")

text2 = "Click på knappen under for at gå til spørgeskemaet."

St.write("# "text2)
#st.write("# "+str(st.session_state["number_input_1"]))

         
st.link_button("Til spørgeskema", "https://survey.au.dk/LinkCollector?key=VC8ZRNUQUN16")
