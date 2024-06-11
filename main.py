import streamlit as st
from funct import readings,writings

todos = readings()


def add_todo():
    todo = st.session_state["newtodo"] +"\n"
    todos.append(todo)
    writings(todos)

writings(todos)
print(todos)
st.title("My to do app")
st.subheader("This is my todo app")
st.write("This app is made to increase your productivity")



for todo in todos:
    st.checkbox(todo)
st.text_input(label="", placeholder="Add new Todo...........", on_change=add_todo, key="newtodo")



print(todos)
