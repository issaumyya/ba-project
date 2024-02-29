import streamlit as st

def calculate_predicted_cost(a, b, c, d, e, f, g, h, i, j):
    reg_cost = 1549.807 + 3.283*a - 242.085*b + 136.226*c + 162.281*d - 135.645*e + 86.832*f - 77.341*g + 2.623 * h + 57.640*i - 61.544*j
    return reg_cost

def main():
    st.title('House Predictions in Central Mumbai')

    # Input variables layout in two columns
    col1, col2 = st.columns(2)

    with col1:
        carpet_sq_feet = st.number_input('Carpet Sq Feet', min_value=0.0, step=0.01)
        negotiable = st.radio('Negotiable', ('Yes', 'No'))
        ready_to_move = st.radio('Ready to Move', ('Yes', 'No'))
        bedrooms_num = st.slider('Number of Bedrooms', 1, 10, 1)
    
    with col2:
        facing_direction = st.radio('Facing Direction', ('North', 'NorthEest', 'West'))
        travel_time_minutes = st.number_input('Travel Time (in minutes) from Marine Drive', min_value=0)
        new = st.radio('New', ('Yes', 'No'))
        bathroom = st.slider('Number of Bathrooms', 1, 5, 1)

    # Convert radio inputs to binary
    negotiable_binary = 1 if negotiable == 'Yes' else 0
    ready_to_move_binary = 1 if ready_to_move == 'Yes' else 0
    new_binary = 1 if new == 'Yes' else 0

    # Convert facing direction to binary
    facing_north_binary = 1 if facing_direction == 'North' else 0
    facing_north_eest_binary = 1 if facing_direction == 'NorthEest' else 0
    facing_west_binary = 1 if facing_direction == 'West' else 0

    # Calculate predicted cost
    predicted_cost = calculate_predicted_cost(carpet_sq_feet, negotiable_binary, ready_to_move_binary, bedrooms_num,
                                              bathroom, facing_west_binary, facing_north_eest_binary,
                                              travel_time_minutes, new_binary, facing_north_binary)

    # Display predicted cost
    st.subheader('Predicted Cost of Property:')
    st.write('₹ {:.2f}'.format(predicted_cost))

    st.text("By Group 1")

if __name__ == "__main__":
    main()
