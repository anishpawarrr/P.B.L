import time
import streamlit as st

#Home
st.set_page_config(page_title="O.C.R")
st.header('O.C.R')
st.subheader('About our Project')
'''In the running world, there is a growing demand for the software system to recognise characters in computer system when 
information is scanned through number plates due to the ever increasing amount of vehicles. These days, there is a need to 
store information about vehicles for safety and legal concerns. Thus our need is to develop a character recognition software 
system to perform documentation from a physical format to a computer processable format. There are multiple techniques which 
can help us solve this problem, but we have chosen Optical Character Recognition System (O.C.R.)
The conversion of number plates to electronic format is an ongoing task in traffic and security management institutes. 
From our problem statement we can introduce the necessity to optical character Recognition in mobile electronic devices 
such as cell phones , digital cameras to acquire images and recognise them as a part of number plate recognition and validation.
Incase a vehicle gets stolen or is unauthorised, the traffic police can use their database of registered vehicles to 
track down the vehicle, or penalise the person driving the unauthorised vehicle'''

st.subheader("About us")
st.write('We are a team of five aspiring students of Pune Institute of Computer Technology :-')

#st.text(#code)
st.write('1. Anish Pawar')
st.write('2. Atharva Zodpe')
st.write('3. Piyush Agarwal')
st.write('4. Parth Dawande')
st.write('5. Kaustubh Joshi')

#report
x = '''Anish Pawar\n
Mail id: anishpurupawar@gmail.com\n
Parth Dawande\n
Mail id: parth.dawande@gmail.com\n
Piyush Agarwal\n
Mail id: piyush.agarwal24.pa@gmail.com\n
Atharva Zodpe\n
Mail id: aazodpe@gmail.com\n
Kaustubh Joshi\n
Mail id: knj.1507@hotmail.com'''
st.subheader('Contact us:-')
st.write(x)
