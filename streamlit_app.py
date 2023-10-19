from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
Streamlit application to take the input value and return the top cases related to that section
"""


# Define a function to process the input string
def process_string(input_string):
    
    return input_string.split()

# Streamlit app content
def main():
    st.title("Retrieve top cases relevant to the IPC Section")
    
    # Create an input widget for the user to enter a string
    user_input = st.text_input("Enter Your Section: ")

    if st.button("Process"):
        if user_input:
            # Call the processing function
            processed_result = process_string(user_input)
            st.write("Relevant Cases:")
            st.write(processed_result)
        else:
            st.warning("Please enter a string to process.")

if __name__ == "__main__":
    main()
