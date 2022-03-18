from cgitb import text
from turtle import left
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time 
st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

left_column, right_column = st.columns(2) 
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ1')
expander.write('問い合わせ1の内容の回答')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ2の内容の回答')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ3の内容の回答')
#text = st.text_input('あなたの趣味を教えて下さい。')
#condistion = st.slider('あなたの今の調子は？', 0, 50, 100)

#'コンディション:', condistion
#'あなたの趣味は、', text, 'です。'

#if st.checkbox('Show Image'):
#   img = Image.open('12.PNG')
#   st.image(img, caption='mukashinoyatu', use_column_width=True)





















