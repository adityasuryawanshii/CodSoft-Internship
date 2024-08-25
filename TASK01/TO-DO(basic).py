#To-Do List Task
##Importing libraries
import streamlit as st

if 'tasks' not in st.session_state:
    st.session_state.tasks=[]

st.title("Hammer - To_Do List")

import os

def Savenexit(file_path,task):
    with open(file_path, "w") as file:
        for i in task:
            file.write(f"(i)\n")

def showtask(task):
    if not task:
        print("No Task found!")
    else:
        for i in task:
            print(f"{i}.{task}")
    

def Addtask(task,newtask):
    task.append(newtask)
    print("Task Added Successfully!")

def updatetask(tasks,index,UpdatedTask):
    if 1<=index<=len(tasks):
        tasks[index]=UpdatedTask
        print("Task Updated Successfully!")
    else:
        print("Please enter valid Index!")

def deletetask(task,index):
    if 1<=index<=len(task):
        deletetask=task.pop(index)
        print(f"task '{deletetask}' Task deleted Successfully!")
    else:
        print("Invaild Index to Delete task")
    






def load_task_from_file(file_path):
    tasks = []
    if os.path.exists(file_path):
       with open(file_path, "r") as file:
        task=file.read().splitlines()
    return tasks


    


def main():
    file_path="ToDO lIst Using Python.txt"
    task= load_task_from_file(file_path)
    while True:
        print("To-DO lIST ")
        print("1.Show Tasks")
        print("2.Add Tasks")
        print("3.Update Tasks")
        print("4.Delete Tasks")
        print("5.Save and Exit")
        choice=int(input("Enter your Choice:"))
        if choice==1:
            showtask(task)
        elif choice==2:
            newtask=input("Add your planning/Task")
            Addtask(task,newtask)
        elif choice ==3:
            index=int(input("Enter the index of the task you want to update"))
            UpdatedTask=input("Enter the updated task here")
            updatetask(task,index,UpdatedTask)
        elif choice==4:
            index=int(input("Enter index of the task you want to delete"))
            deletetask(task,index)
        elif choice==5:
            Savenexit(file_path,task)
            print("Task Saved!, Exiting...")
            break
        else:
            print("Please enter a valid choice!")
if __name__ == "__main__":
    main() 