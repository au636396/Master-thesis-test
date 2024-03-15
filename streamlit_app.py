import pandas as pd
import streamlit as st
import random
import gspread
import gspread_dataframe as gd
import base64
from st_btn_group import st_btn_group

### condition number meaning:
# 1 = Left, same   
# 2 = Left, diffrent
# 3 = Right, same
# 4 = Rigth, diffrent 

# initializing secction with a random number, used for picking a condition
if "condition" not in st.session_state:
    st.session_state["condition"] = random.randint(1,4)

#------------------------ Saving the data --------------
gc = gspread.service_account(filename='~/.config/gspread/service_account.json')   #cornnects to API

#-------------------------- active one you want to "turn on" tracing 
#olddata = gc.open("MasterThesisDataLog").worksheet("ark") # spesifies the sheet
#pdolddata = gd.get_as_dataframe(olddata)  #imports it as a pd dataframe 

#---------------------------- adding baground pictue--------------------------------------------------------
# function that add a bacgournd picture 
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('generic_website.png')

#-------------------deifnng the way the buttons and container looks ---------------------------------------------------
#con1
buttons1 = [
    {"label": "Accepter alle", "value": "accepter1", "style": {"backgroundColor": "lightgreen",  "color": "black", },
    },
    {"label": " Afvis alle ",  "value": "afvis1", "style": {"backgroundColor": "lightgreen",  "color": "black", },
    },
]
#con 2
buttons2 = [
    {"label": "Accepter alle", "value": "accepter2", "style": {"backgroundColor": "lightgreen", "color": "black", },
    },
    {"label": " Afvis alle ",  "value": "afvis2", "style": { "color": "black", },
    },
]
#con 3
buttons3 = [
    {"label": " Afvis alle ",  "value": "afvis3", "style": { "backgroundColor": "lightgreen", "color": "black", },
    },
    {"label": "Accepter alle", "value": "accepter3", "style": {"backgroundColor": "lightgreen", "color": "black", },
    },
]
#con 4
buttons4 = [
    {"label": " Afvis alle ",  "value": "afvis4", "style": { "color": "black", },
    },
    {"label": "Accepter alle", "value": "accepter4", "style": {"backgroundColor": "lightgreen", "color": "black", },
    },
]


#making the container baggruound white
css_body_container = f'''
<style>
    [data-testid="stVerticalBlock"] {{
    background-color: #FFFFFF;
    }}
</style>
'''
st.markdown(css_body_container,unsafe_allow_html=True)


#-------------------------------------------------- making the text and buttons apier ------------------------
# defining the colums the buttons and text will apier in
col1, col2, col3 = st.columns([1,4,1])

# makeing the buttons show up depending on condition
if st.session_state.condition == 1:  # con 1
    with col2:
            with st.container():
                st.image('cookies_text.png')
                button_cliked = st_btn_group(buttons=buttons1, gap_between_buttons = 45, size='default', align ='center')
elif st.session_state.condition == 2:  # con 2
    with col2:
            with st.container():
                st.image('cookies_text.png')
                button_cliked = st_btn_group(buttons=buttons2, gap_between_buttons = 45, size='default', align ='center')
elif st.session_state.condition == 3:  # con 3
    with col2:
            with st.container():
                st.image('cookies_text.png')
                button_cliked = st_btn_group(buttons=buttons3, gap_between_buttons = 45, size='default', align ='center')
elif st.session_state.condition == 4:  # con 4
    with col2:
            with st.container():
                st.image('cookies_text.png')
                button_cliked = st_btn_group(buttons=buttons4, gap_between_buttons = 45, size='default', align ='center')
else:
    st.write("An error has occurred, please reload the page!")


#--------------- traking the button click ---------------
## take the button input and puts it in the new row dataframe, only after a buttons has been pressed
if button_cliked == 'afvis1':
        new_row = pd.DataFrame(["afvis1"], columns=['button']) 
elif button_cliked == 'accepter1':
        new_row = pd.DataFrame(["accepter1"], columns=['button']) 
elif button_cliked == 'afvis2':
        new_row = pd.DataFrame(["afvis2"], columns=['button']) 
elif button_cliked == 'accepter2':
        new_row = pd.DataFrame(["accepter2"], columns=['button']) 
elif button_cliked == 'afvis3':
        new_row = pd.DataFrame(["afvis3"], columns=['button']) 
elif button_cliked == 'accepter3':
        new_row = pd.DataFrame(["accepter3"], columns=['button']) 
elif button_cliked == 'afvis4':
        new_row = pd.DataFrame(["afvis4"], columns=['button']) 
elif button_cliked == 'accepter4':
        new_row = pd.DataFrame(["accepter4"], columns=['button']) 

#show data frame if it exxists if not print not yet
try: st.dataframe(new_row) 
except NameError: print("not yet")

#st.dataframe(new_row)   #!!! remove this before experiment launch
#newdata = pd.concat([pdolddata, new_row])    # adding the new row from above at the end of the data
#gd.set_with_dataframe(olddata, newdata)    #this should ad the new data to the gsheet

### this needs to be fixed
#show button with link to surevery only after a button has been cliked 
if button_cliked == 'afvis1' or == 'accepter1' or == 'afvis2' or == 'accepter2' or == 'afvis3' or == 'accepter3' or == 'afvis4' or == 'accepter4':
        st.link_button("Go to survey", "https://survey.au.dk/LinkCollector?key=VC8ZRNUQUN16")
