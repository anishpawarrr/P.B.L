import streamlit as st
import pytesseract as pyt
import cv2
import time
import winsound

st.set_page_config(
    page_title="Using Mobile"
)
pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
s2 = st.text_input("Enter IP address")
s3 = st.text_input("Enter Port number")
vid = cv2.VideoCapture('http://' + s2 + ':' + s3 + '/video')
#vid = cv2.VideoCapture('http://192.168.16.153:8080/video')
x = None
st.title("Scaning using Mobile's camera")
framewindow = st.image([])
clickbutton = st.button('👉 Click here to scan')

while True:
    got_frame, frame = vid.read()

    if not got_frame:
        st.write("Error 404 frame not found 👀")
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    framewindow.image(frame)

    if clickbutton:
        x = pyt.image_to_string(frame)
        vid.release()
        break

st.write('Scanned text :-')
st.write(x)
x = x.replace(' ', '')
x = x.replace('\n', '')
x = x.replace(',', '.')
f = open('History.csv', 'a+')
f.write(f"{x}, {time.ctime()} \n")
f.close()
