# contact_book_app.py

import streamlit as st
import csv
import os

# CSV file path
CSV_FILE = "contacts.csv"

# Initialize contact book in session_state
if "contacts" not in st.session_state:
    st.session_state.contacts = {}
    
    # Load existing contacts from CSV file (if available)
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    name, phone = row
                    st.session_state.contacts[name] = phone

st.title("📒 Contact Book")

# Tabs for different actions
tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Contact", "🔍 Search", "🗑️ Delete", "📋 All Contacts"])

# Add Contact
with tab1:
    st.header("Add a New Contact")
    name = st.text_input("Contact Name", key="add_name")
    phone = st.text_input("Phone Number", key="add_phone")

    if st.button("Add Contact"):
        if name and phone:
            if name in st.session_state.contacts:
                st.warning(f"{name} already exists in contacts.")
            else:
                st.session_state.contacts[name] = phone

                # Save to CSV file
                with open(CSV_FILE, mode="a", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([name, phone])

                st.success(f"{name} added successfully!")
        else:
            st.error("Please enter both name and phone number.")

# Search Contact
with tab2:
    st.header("Search Contact")
    search_name = st.text_input("Enter name to search", key="search_name")
    if st.button("Search"):
        if search_name in st.session_state.contacts:
            st.info(f"{search_name}'s number is {st.session_state.contacts[search_name]}")
        else:
            st.error(f"No contact found with the name {search_name}")

# Delete Contact
with tab3:
    st.header("Delete Contact")
    delete_name = st.text_input("Enter name to delete", key="delete_name")
    if st.button("Delete"):
        if delete_name in st.session_state.contacts:
            del st.session_state.contacts[delete_name]

            # Rewrite CSV with updated contacts
            with open(CSV_FILE, mode="w", newline='') as file:
                writer = csv.writer(file)
                for name, phone in st.session_state.contacts.items():
                    writer.writerow([name, phone])

            st.success(f"{delete_name} has been deleted.")
        else:
            st.error(f"No contact named {delete_name} found.")

# View All Contacts
with tab4:
    st.header("All Contacts")
    if st.session_state.contacts:
        for name, phone in st.session_state.contacts.items():
            st.write(f"**{name}**: {phone}")
    else:
        st.info("Your contact book is empty.")
        



        