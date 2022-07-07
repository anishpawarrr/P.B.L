import streamlit as st
import pytesseract as pyt
import cv2
import time
import winsound

#Laptop
st.set_page_config(
    page_title="Using Laptop"
)
pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
st.title("Scaning using laptop's camera")
framewindow = st.image([])
state_dict = {'AD': 'ANDHRA PRADESH', 'AP': 'ARUNACHAL PRADESH', 'AS': 'ASSAM', 'BR': 'BIHAR', 'CG': 'CHHATTISGARH', 'DL': 'DELHI', 'GA': 'GOA', 'GJ': 'GUJARAT', 'HR': 'HARYANA', 'HP': 'HIMACHAL PRADESH', 'JK': 'JAMMU AND KASHMIR', 'KL': 'KERALA', 'LD': 'LAKSHADWEEP ISLANDS', 'MP': 'MADHYA PRADESH', 'MH': 'MAHARASHTRA', 'MN': 'MANIPUR', 'ML': 'MEGHALAYA', 'MZ': 'MIZORAM', 'NL': 'NAGALAND', 'OD': 'ODISHA', 'PY': 'PONDICHERRY', 'PB': 'PUNJAB', 'RJ': 'RAJASTHAN', 'SK': 'SIKKIM', 'TN': 'TAMIL NADU', 'TS': 'TELANGANA', 'TR': 'TRIPURA', 'UP': 'UTTAR PRADESH', 'UK': 'UTTARAKHAND', 'WB': 'WEST BENGAL', 'AN': 'ANDAMAN AND NICOBAR', 'CH': 'CHANDIGARH', 'LA': 'LADAKH', 'DN': 'DADAR AND NAGAR HAVELI'}
video = cv2.VideoCapture(0)
noplate = []
backuplist = []
x = None
but = None
statename = None
clickbutton = st.button("👉 Click here to scan")

while True:
    got_frame, frame = video.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    framewindow.image(frame)
    if not got_frame:
        st.write("Error 404 frame not found 👀")
        break
    if clickbutton:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video.release()
        break

x = pyt.image_to_string(frame)
st.write('Scanned text :-')
st.write(x)
x = x.replace(' ', '')
x = x.replace('\n', '')
x = x.replace(',', '.')
f = open('History.csv', 'a+')
f.write(f"{x}, {time.ctime()} \n")
f.close()
