
import pandas as pd
import streamlit as st
import os

# import plotly.express as px    


# create container 
header = st.container()
body = st.container()

# there is a function to not load , to use from cache
#  @st.cache

# fill container 
with header:
    st.markdown("<body  background='bg.jpg' >      "  , unsafe_allow_html=True)
      
    st.title("Group Sentiment Analyser")  
    # title for main heading 
    st.subheader("             ")
    

    # st.text("this   w is text ")
    Company_name = st.text_input( 'Company Name ')
    Project_name  = st.text_input( 'Project Name')
    team_name = st.text_input( ' Team Name')
    # text_input_from_ui = st.text_input( 'Type here ....')
    st.markdown("<hr>", unsafe_allow_html=True)
    
st.markdown("<hr>", unsafe_allow_html=True)


with body:
    
    file_a = st.file_uploader("Upload file here"  , type=None, accept_multiple_files=False, key=None, help=None,
     on_change=None, args=None, kwargs=None)
    if file_a is not None :
        with open(os.path.join("uploaded_files",file_a.name),"wb") as f:
            f.write(file_a.getbuffer()) 
        
        st.success("File saved")

    a = st.text_input( ' type here to see below ')
    st.write(' Sentiment analysis report   : ' + str(a)  )




# to use sidebar

# st.sidebar.subheader("Component 1")

# t1 = st.sidebar.text_input("Component 1 name")
# s1 = st.sidebar.slider("Component 1 value")

# st.sidebar.markdown("---")

# st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# st.sidebar.subheader("Component 2")
# t2 = st.sidebar.text_input("Component 2 name")
# s2 = st.sidebar.slider("Component 2")



# streamlit run main.py    --- to run 

# copy data in data folder 

# in part 2 we see how to creat graph with the data set   and also take input 
 

#  part 3 for integratition  -- import functions from the project files and use it 
 # part 4 --- for deployment we need to put code on github and need requrement.txt  
#  