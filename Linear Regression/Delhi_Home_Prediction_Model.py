
#Import all the required libraries

import pickle
import numpy as np
import streamlit as st

# Insert the model file

loaded_model = pickle.load(open('C:/Users/amany/Desktop/Project_1/final_trained_model.sav','rb'))

global list_of_location
list_of_location = ['Area', 'BHK', 'Bathroom', 'Furnishing', 'Alaknanda', 'Budh Vihar',
       'Budh Vihar Phase 1', 'Chhattarpur', 'Chhattarpur Enclave Phase2',
       'Chittaranjan Park',
       'Common Wealth Games Village, Commonwealth Games Village 2010',
       'Commonwealth Games Village 2010',
       'DDA Flats Sarita Vihar, Sarita Vihar, Mathura Road',
       'DDA Lig Flats, Narela',
       'DLF Capital Greens, New Moti Nagar, Kirti Nagar',
       'Dilshad Colony, Dilshad Garden', 'Geetanjali Enclave, Malviya Nagar',
       'Godrej South Estate, Okhla', 'Govindpuri Extension, Kalkaji',
       'Hauz Khas', 'Hauz Khas Enclave, Hauz Khas',
       'J R Designers Floors, Rohini Sector 24',
       'Kailash Colony, Greater Kailash', 'Kalkaji', 'Karol Bagh',
       'Lajpat Nagar', 'Lajpat Nagar 2', 'Lajpat Nagar 3', 'Laxmi Nagar',
       'Maharani Bagh, New Friends Colony', 'Mahavir Enclave',
       'Mahavir Enclave Part 1', 'Malviya Nagar', 'Mehrauli', 'Narela',
       'Narmada Apartment, Alaknanda', 'New Friends Colony',
       'New Manglapuri, Sultanpur', 'New Moti Nagar, Kirti Nagar',
       'Nilgiri Apartment, Alaknanda', 'Others', 'Paschim Vihar',
       'Patel Nagar East, Patel Nagar', 'Patel Nagar West',
       'Project Commonwealth Games Village 2010, Commonwealth Games Village 2010',
       'Punjabi Bagh West', 'Rohini Sector 23', 'Rohini Sector 24',
       'Safdarjung Enclave', 'Saket', 'Shahdara', 'Sheikh Sarai Phase 1',
       'Sukhdev Vihar, Okhla', 'Sultanpur', 'The Amaryllis, Karol Bagh',
       'The Leela Sky Villas, Patel Nagar', 'Uttam Nagar', 'Vasant Kunj',
       'Vasundhara Enclave', 'Yamuna Vihar, Shahdara']

def price_prediction_model(input_data):

    input_data_array = np.asarray(input_data)

    index_of_location = -1
    for i in list_of_location:
        if i == input_data_array[-1]:
            break
        index_of_location += 1

    x = np.zeros(len(list_of_location))
    x[0] = input_data_array[0]
    x[1] = input_data_array[1]
    x[2] = input_data_array[2]
    x[3] = input_data_array[3]
    x[index_of_location] = 1

    predicted_value = loaded_model.predict([x])[0]

    return "Your property price is " + str(predicted_value/100000) + " lakhs rupees."

def main():

    st.title("Delhi Home Price Prediction")

    # Get all the input fields

    Area = st.text_input("Area(in sqft)")
    BHK = st.text_input("BHK")
    Bathroom = st.text_input("No. Of Bathrooms")
    Furnishing  =st.text_input("(Unfurnished:0),(semi-furnished:1),(fully-furnished:2)")
    Location = st.text_input("Enter the Given Location")
    st.write(list_of_location)

    rupees = ""

    if st.button("Submit"):
        rupees = price_prediction_model([int(Area),
                                         int(BHK),
                                         int(Bathroom),
                                         int(Furnishing),
                                         Location])

    st.success(rupees)


if __name__ == '__main__':
    main()

