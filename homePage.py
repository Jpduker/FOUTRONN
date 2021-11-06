import streamlit as st
import numpy as np


def show_homePage():
    battery = (
        "Premium Tall Tubular Battery",
        "Economical Battery Series,150Ah",

    )
    ups = (
        "Pure Sine Wave Inverters",
        "Hybrid Solar UPS"

    )
    solar = (
        "Roof Top Ongrid Solar",
        "Prakash Solar Water Heater "
    )
    battery = st.selectbox("BATTRIES", battery)
    ups = st.selectbox("UPS", ups)
    solar = st.selectbox("Solar", solar)

    Price = st.button("Calculate Price")
    if Price:
        x = np.array([battery, ups, solar])
        if battery == "Premium Tall Tubular Battery":
            st.write("The price of Premium Tall Tubular Battery is Rs. 16,750")
        else:
            st.write("The price of Economical Battery Series,150Ah is Rs. 14,750")
        if ups == "Pure Sine Wave Inverters":
            st.write("The price of Pure Sine Wave Inverters is Rs. 6,750")
        else:
            st.write("The price of Hybrid Solar UPS is Rs. 8,750")
        if solar == "Roof Top Ongrid Solar":
            st.write("Contact directly")
        else:
            st.write("The pirce of Prakash Solar Water Heater is Rs. 29,700")
