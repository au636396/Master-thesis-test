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
col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.write("Tak for at du ville hjælpe med mit speciale. Jeg undersøger designet af cookie pop-ups på hjemmesider og hvordan de påvirker adfærd.")
    st.write("Jeg vil gerne stille dig nogle spørgsmål omkring cookie pop-ups og databeskyttelse. Hvis du gerne vil hjælpe mig med det så klik her:")
    st.write()
    st.link_button("**Til spørgeskema**", "https://survey.au.dk/LinkCollector?key=VC8ZRNUQUN16", type="primary")
