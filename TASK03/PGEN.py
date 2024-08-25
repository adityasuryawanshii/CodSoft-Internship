import streamlit as st
import random
import string

st.title("<PGEN>")
st.subheader("A Strong Password Generator for you (1234@$xxxxxxxx)")

st.markdown("INPUT")
length=st.number_input("Enter your desire length of password",format="%d",value=0,step=1)
st.header("Choices consists")
st.subheader("Low- Only Number based password")
st.subheader("Medium- Number and Alphabetical Characters")
st.subheader("High- Number, Alphabetical character, and One Special Characters")
st.subheader("UltraHigh- Number, Alphabetical character, and Random Special Characters")
Level=st.selectbox("Enter your level of Strong password",["Low","Medium","High","UltraHigh"])

if Level=="Low":
    if st.button("Generate"):
        p=""
        for i in range(0,length):
            random_number = random.randint(1, 9)
            p=p+str(random_number)
        st.write("Generated Password : ")
        st.success(p)


elif Level=="Medium":
    if st.button("Generate"):
        p=""
        for i in range(0,length//2):
            random_char = random.choice(string.ascii_letters)
            p=p+random_char
        for i in range(0,length//2):
            random_number = random.randint(1, 9)
            p=p+str(random_number)
        st.write("Generated Password : ")
        st.success(p)
elif Level=="High":
    if st.button("Generate"):
        p=""
        for i in range(0,length//2):
            random_char = random.choice(string.ascii_letters)
            p=p+random_char

        for i in range(0,length//2):
            if i==1:
                special_characters = string.punctuation
                random_special_char = random.choice(special_characters)
                p=p+str(random_special_char)
                continue
            random_number = random.randint(1, 9)
            p=p+str(random_number)
            

        st.write("Generated Password : ")
        st.success(p)
        
elif Level=="UltraHigh":
    if st.button("Generate"):
        p=""
        for i in range(1,length//3):
            random_number = random.randint(1, 9)
            p=p+str(random_number)
        for i in range(1,length//3):
            random_char = random.choice(string.ascii_letters)
            p=p+random_char
            
        for i in range(0,length-len(p)):
            special_characters = string.punctuation
            random_special_char = random.choice(special_characters)
            p=p+str(random_special_char)
            

            
            

        st.write("Generated Password : ")
        st.success(p)
        

    