input_feature = st.text_input('What is your name?')

pregnancies1= st.slider('How many times have you been pregnant?', 
  min_value=0, 
  max_value=10, 
  value=0, 
  step=1)

pregnancies2 = st.selectbox('How many times have you been pregnant?', 
  options=[0,1,2,3,4,5,6,7,8,9,10], 
  index=0)

pregnancies3= st.number_input('How many times have you been pregnant?', 
  min_value=0, 
  max_value=10, 
  value=0, 
  step=1)

with st.form(key='columns_in_form'):
  input_feature = st.text_input('What is your name?')
  submitted = st.form_submit_button('Submit')

if submitted:
  st.text(input_feature)