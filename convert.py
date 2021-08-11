import streamlit as st
import numpy as np
import time
from PIL import Image, ImageEnhance
import cv2



def convert_page():
    st.markdown("<h1 style='text-align: center; color: white;'>Image Convertor App using Python</h1>", unsafe_allow_html=True)
    #st.markdown("<h4 style='text-align: center; color:grey;'></h4>", unsafe_allow_html=True)
    st.write('')

    st.markdown('___')


    file_image = st.file_uploader("Upload your Photos", type=['jpeg','jpg','png'])
    
    
    
            
    enhance_type = st.sidebar.radio("Enhance Type",["Original","Invert","Gray-Scale","Contrast","Blurring",'Pencil Sketch'])
    if file_image is None:
        st.warning("You haven't uploaded any image file")
    if file_image is not None:
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.03)
            progress.progress(i+1)
        progress.empty()
        input_img = Image.open(file_image)
        new_width  = 640
        new_height = 400
        input_img = input_img.resize((new_width, new_height), Image.ANTIALIAS)
        st.write("**Input Photo**")
        st.image(input_img, use_column_width=True)
    
    if enhance_type == 'Invert':
        new_img = np.array(input_img.convert('RGB'))
        img = cv2.cvtColor(new_img,1)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img_inv = cv2.bitwise_not(gray)	
        st.image(img_inv)
    elif enhance_type == 'Gray-Scale':
	    new_img = np.array(input_img.convert('RGB'))
	    img = cv2.cvtColor(new_img,1)
	    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)	
	    st.image(gray)
    elif enhance_type == 'Contrast':
	    c_rate = st.sidebar.slider("Contrast",0.5,3.5)
	    enhancer = ImageEnhance.Contrast(input_img)
	    img_output = enhancer.enhance(c_rate)
	    st.image(img_output)
    elif enhance_type == 'Blurring':
        new_img = np.array(input_img.convert('RGB'))
        blur_rate = st.sidebar.slider("Brightness",0.5,3.5)
        img = cv2.cvtColor(new_img,1)
        blur_img = cv2.GaussianBlur(img,(11,11),blur_rate)
        st.image(blur_img)
    elif enhance_type == 'Pencil Sketch':
        new_img = np.array(input_img.convert('RGB'))
        img = cv2.cvtColor(new_img,1)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img_inv = cv2.bitwise_not(gray)
        img_smooth = cv2.GaussianBlur(img_inv, (5, 5), 0, 0)
        img_smooth_inv = 255 - img_smooth
        img_final = cv2.divide(gray, img_smooth_inv, scale=256.0)
        st.image(img_final)

    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.markdown('___')
    st.markdown("<h4 style='text-align: center; color:grey;'>Made with ❤️ by Zahid Shaikh</h4>", unsafe_allow_html=True)
    
    st.sidebar.markdown("\n\n[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/zahidshaikh10101)")
    st.sidebar.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zahid-shaikh-7s8a6a/)")
    st.sidebar.markdown("[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/zahids786/?hl=en)")

        #st.spinner()
        #with st.spinner(text='Uploading Image'):
            #time.sleep(2)  
        
        
        #convert = (
        #'Pencil sketch image',
        #'RGB_scale image',
        #'Gray_scale image',
        #'Invert the Image',
        #'Blur the Image',
        #)
        #convertor = st.selectbox("Convert To", convert)
        

        #if convertor == 'RGB_scale image':
            #st.spinner()
            #with st.spinner(text='Converting Image'):
                #time.sleep(3)  
 
            #img_rgb = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
            #st.write("**Input Photo**")
            #st.image(img_rgb, use_column_width=True)

        
        #final_sketch = pencilsketch(np.array(input_img))
        #st.write("**Output Pencil Sketch**")
        #st.image(final_sketch, use_column_width=True)