import streamlit as st

st.title("Calci- A CALCULATOR")
st.subheader("+-*/% here!")

st.markdown("INPUT")
num1=st.number_input('Enter the first number..',  value=0, step=1,format="%d")
num2=st.number_input('Enter the Second number..', value=0, step=1,format="%d")
choice=st.selectbox("Select your Operation:",['Addition','Subtraction','Multiplication','Division','Modulus'])

st.markdown("OUTPUT")
while True:
    if choice=="Addition":
        res=num1+num2
        st.write("The ",choice," of ",num1," and ",num2, " is ",res)
        break

    elif choice=="Subtraction":
        res=num1-num2
        st.write("The ",choice," of ",num1," and ",num2, " is ",res)
        break

    elif choice=="Multiplication":
        res=num1*num2
        st.write("The ",choice," of ",num1," and ",num2, " is ",res)
        break

    elif choice=="Division":
        if num2==0:
            exp = ZeroDivisionError("Trying to divide by Zero")
            st.exception(exp)
            st.write("Please Don't enter 0 at second place.")
            break
        else:
            res=num1/num2
            st.write("The ",choice," of ",num1," and ",num2, " is ",res)
            break

    elif choice=="Modulus":
        if num2==0:
            exp = ZeroDivisionError("Trying to find modulus by Zero")
            st.exception(exp)
            st.write("Please Don't enter 0 at second place.")
            break
        else:
            res=num1%num2
            st.write("The ",choice," of ",num1," and ",num2, " is ",res)
            break
        

    else:
        st.write("Please choose your operation")