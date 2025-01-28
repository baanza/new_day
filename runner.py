import subprocess
import streamlit as st

st.write("hello world,, there is something running in the background ...⚡")

subprocess.run(['pip', "install", "sqlmodel"])
subprocess.run(["python", "main.py"])