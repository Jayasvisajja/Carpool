import streamlit as st
from database import create_tables, add_user, add_ride, get_all_rides, get_user_phone
from utils import validate_email, validate_phone, haversine, time_within_30min, location_coords

create_tables()

st.title("🚕 VIT-AP Ride Sharing App")

menu = st.sidebar.selectbox("Choose Action", ["Sign Up", "Schedule Ride"])

if menu == "Sign Up":
    st.subheader("Create Account")

    email = st.text_input("Enter VIT AP Email")
    phone = st.text_input("Enter 10-digit Phone Number")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):
        if not validate_email(email):
            st.error("Invalid VIT AP Email ID")
        elif not validate_phone(phone):
            st.error("Invalid Phone Number")
        elif not password:
            st.error("Password cannot be empty")
        else:
            try:
                add_user(email, phone, password)
                st.success("Account created successfully!")
            except:
                st.error("Account already exists!")

elif menu == "Schedule Ride":
    st.subheader("Schedule a Ride")

    email = st.text_input("Enter your registered VIT AP Email")
    if validate_email(email):
        current = st.selectbox("Select Current Location", list(location_coords.keys()))
        destination = st.selectbox("Select Destination", list(location_coords.keys()))
        date = st.date_input("Date")
        time = st.time_input("Time")

        if current == destination:
            st.warning("Current location and destination cannot be the same.")
        elif st.button("Find Matches"):
            rides = get_all_rides()
            dest_lat, dest_lon = location_coords[destination]
            matched = []

            for ride in rides:
                r_email, _, r_destination, r_date, r_time, r_lat, r_lon = ride

                if r_email == email:
                    continue  # skip self

                if r_destination != destination or str(r_date) != str(date):
                    continue

                dist = haversine(dest_lat, dest_lon, r_lat, r_lon)
                if dist <= 500 and time_within_30min(time.strftime("%H:%M"), r_time):
                    matched.append(r_email)

            if matched:
                st.success("Found matching riders:")
                for m in matched:
                    phone = get_user_phone(m)
                    st.write(f"📱 Phone: {phone}")
            else:
                cur_lat, cur_lon = location_coords[current]
                add_ride(email, current, destination, str(date), time.strftime("%H:%M"), dest_lat, dest_lon)
                st.info("No match found. Ride added to future pool.")
    else:
        st.warning("Enter a valid VIT AP email to continue.")
