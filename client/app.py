from dotenv import load_dotenv
import streamlit as st
import requests
import os

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")

def handleResponse(status_code, onSuccessMessage, onErrorMessage):
    if status_code == 200:
        st.success(onSuccessMessage)
    else:
        st.error(onErrorMessage)

def listUsers():
    users_response = requests.get(f"http://backend:8000/users")
    if users_response.status_code == 200:
        users = users_response.json()
        st.write("Users in the database:")
        for user in users:
            st.write(f"ID:{user['id']} Name: {user['name']}, Email: {user['email']}")
    else:
        st.error("Failed to fetch users.")

def onSubmitCreateUser(userName, userEmail):
    
    response = requests.post(f"http://backend:8000/user", json={"name": userName, "email": userEmail})

    handleResponse(response.status_code, "User created successfully!", "Failed to create user.")


def onSubmitDeleteUser(userID):
    
    response = requests.delete(f"http://backend:8000/user/{userID}")

    handleResponse(response.status_code, "User deleted successfully!", "Failed to delete user.")

st.title("Your Stack is fully configured!🚀")

st.write("Test here the connection to the database:")

with st.form("create_user"):
    st.write("Create User")
    userName = st.text_input("Username")
    userEmail = st.text_input("Email")
    submitCreateUser = st.form_submit_button("Create User")

with st.form("delete_user"):
    st.write("Delete User")
    userID = st.text_input("ID")
    submitDeleteUser = st.form_submit_button("Delete User")

if submitCreateUser:
    onSubmitCreateUser(userName, userEmail)
    listUsers()

if submitDeleteUser:
    onSubmitDeleteUser(userID)
    listUsers()

if not submitCreateUser and not submitDeleteUser:
    listUsers()


