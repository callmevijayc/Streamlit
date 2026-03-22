import streamlit as st
import datetime

# Define clear function
def clear_form():
    st.session_state["name"] = ""
    st.session_state["dob"] = datetime.date.today()
    st.session_state["gender"] = "Male"
    st.session_state["options"] = []
    st.session_state["option"] = "Python"
    st.session_state["skills"] = 4

# Initialize session state for all widgets
if "name" not in st.session_state:
    st.session_state["name"] = ""
if "dob" not in st.session_state:
    st.session_state["dob"] = datetime.date.today()
if "gender" not in st.session_state:
    st.session_state["gender"] = "Male"
if "options" not in st.session_state:
    st.session_state["options"] = []
if "option" not in st.session_state:    
    st.session_state["option"] = "Python"
if "skills" not in st.session_state:
    st.session_state["skills"] = 4

st.title("Employee Profile ") ## This line sets the title of the app
st.write("This app demonstrates various Streamlit widgets.") ## This line writes a message to the app

# Text Input Widget 
name = st.text_input("Enter your name:", key="name") ## This line creates a text input widget for the user to enter their name

dob = st.date_input("Select your date of birth:", key="dob") ## This line creates a date input widget for the user to select their date of birth

gender = st.radio(
    "Select your gender",
    ["Male", "Female", "Other"],
    key="gender"
)

# Multiselect Widget
options = st.multiselect("Select Technologies: (Multiple)", ["Python", "Java", "JavaScript", "C++","React","Node.js"], key="options") ## This line creates a multiselect widget for the user to select their favorite fruits

# Selectbox Widget
option = st.selectbox("Choose current working area:", ["Python", "Java", "JavaScript", "C++","React","Node.js"], key="option") ## This line creates a selectbox widget for the user to choose a color

# Slider Widget
skills = st.slider("Select technical skills level :", 1, 10, 4, key="skills") ## This line creates a slider widget for the user to select their height


col1, col2 = st.columns(2)


with col1:
   if st.button("Submit"): ## This line creates a submit button and checks if it is clicked
    if name: ## This line checks if the user has entered a name
     st.write(f"Hello, {name}!") ## This line greets the user by name   
    if dob: ## This line checks if the user has selected a date of birth
     st.write(f"Your date of birth is: {dob}") ## This line displays the selected date of birth
    if gender: ## This line checks if the user has
     st.write(f"You selected: **{gender}**") ## This line displays the selected gender
    if options: ## This line checks if the user has selected any technologies
     st.write(f"You selected: {', '.join(options)}") ## This line displays the selected technologies
    if option: ## This line checks if the user has selected a working area
     st.write(f"You selected: {option}") ## This line displays the selected working area
     if skills: ## This line checks if the user has selected a skill level
      st.write(f"Your skill level is: {skills}") ## This line displays the selected skill level 
     st.write("Form submitted!") ## This line displays a message when the form is submitted

with col2:
    #clear button
    st.button("Clear", on_click=clear_form) ## This line creates a clear button that calls clear_form when clicked
      
 
