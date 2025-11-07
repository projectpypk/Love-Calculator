import streamlit as st
import random
import os

# ---- Developer Password ----
   # change this to your password

# ---- App Title ----
st.set_page_config(page_title="Love Calculator 💘", page_icon="💘")
st.title("💞 Love Calculator 💞")

# ---- User Input ----
your_name = st.text_input("Your Name")
partner_name = st.text_input("Partner's Name")

if st.button("Calculate Love 💖"):
    if your_name and partner_name:
        # Calculate a simple love score
        score = (sum(ord(c) for c in (your_name + partner_name)) % 100) + 1
        st.success("✅ Your love result has been processed successfully!")

        # Developer section
        st.markdown("---")
        st.write(f"{your_name}❤️{partner_name}")
        st.write(f"💌 Love Score: {score}%")
        file_path =r"love_data.txt"

        with open(file_path, "a") as f:
            f.write(f"User: {your_name}, Partner: {partner_name}, Love: {score}%\n")

        st.success(f"Data saved to '{file_path}' ✅")

    else:
        st.warning("Please enter both names!")

