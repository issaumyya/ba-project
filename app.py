import pandas as pd
import plotly.graph_objects as go
import numpy as np
import streamlit as st

def calculate_predicted_cost(a, b, c, d, e, f, g, h, i, j):
    reg_cost = 1549.807 + 3.283*a - 242.085*b + 136.226*c + 162.281*d - 135.645*e + 86.832*f - 77.341*g + 2.623 * h + 57.640*i - 61.544*j
    return reg_cost
def main():
    st.title('Property Cost Prediction')

    # Input variables
    carpet_sq_feet = st.number_input('Carpet Sq Feet', min_value=0.0, step=0.01)
    negotiable = st.radio('Negotiable (Yes or No)', ('Yes', 'No'))
    ready_to_move = st.radio('Ready to Move (Yes or No)', ('Yes', 'No'))
    bedrooms_num = st.slider('Number of Bedrooms', 1, 10, 1)
    bathroom = st.slider('Number of Bathrooms', 1, 5, 1)
    facing_west = st.checkbox('Facing West')
    facing_north_west = st.checkbox('Facing North West')
    travel_time_minutes = st.number_input('Travel Time (in minutes)', min_value=0)
    new = st.radio('New (Yes or No)', ('Yes', 'No'))
    facing_north = st.checkbox('Facing North')

    # Convert radio and checkbox inputs to binary
    negotiable_binary = 1 if negotiable == 'Yes' else 0
    ready_to_move_binary = 1 if ready_to_move == 'Yes' else 0
    facing_west_binary = 1 if facing_west else 0
    facing_north_west_binary = 1 if facing_north_west else 0
    new_binary = 1 if new == 'Yes' else 0
    facing_north_binary = 1 if facing_north else 0

    # Calculate predicted cost
    predicted_cost = calculate_predicted_cost(carpet_sq_feet, negotiable_binary, ready_to_move_binary, bedrooms_num,
                                              bathroom, facing_west_binary, facing_north_west_binary,
                                              travel_time_minutes, new_binary, facing_north_binary)

    # Display predicted cost
    st.subheader('Predicted Cost of Property:')
    st.write(predicted_cost)
if __name__ == "__main__":
    main()
