# Carpool
A mobile app for VIT-AP students to schedule rides and find co-travelers going to similar destinations like airports or bus stations. It matches users with others traveling within 500m and ±30 minutes of scheduled time. Secure sign-up with student email and phone. Built using Flutter and Python backend.

🚖 VIT-AP Ride Sharing App (Mobile App)
A mobile application designed specifically for students of VIT-AP University to help them find and coordinate rides with fellow students traveling to common locations such as airports, railway stations, and bus stops. The app ensures secure sign-up, intelligent ride matching, and helps users connect with co-travelers.

📱 Features
Secure Sign-Up

Only allows official student emails (@vitapstudent.ac.in)

Phone number validation and password-based login

Schedule a Ride

Users select their current location, destination, date, and time

Predefined trusted locations (e.g., VIT-AP campus, Vijayawada Airport)

Smart Matching System

Finds students with similar destinations (within 500 meters)

Matches rides ±30 minutes of scheduled time on the same date

If a match is found, the contact number is shared

If no match, the ride is stored to match with future users

User Privacy

Only matched users can view each other's contact information

🛠 Tech Stack
Layer	Technology
Frontend	Flutter (Dart)
Backend	FastAPI (Python)
Database	SQLite or Firebase
Authentication	Custom / Firebase Auth
Matching Logic	Haversine Distance + Time Matching
Hosting (optional)	Render / Railway / Firebase Functions

📍 Predefined Locations (Current/Destination)
VIT-AP (College Campus)

Vijayawada Airport

VIT-AP Bus Stop

Vijayawada Bus Station

Vijayawada Railway Station

🔒 Matching Conditions
Destination within 500 meters (based on coordinates)

Time ±30 minutes

Same scheduled date

Destination ≠ Current Location

🚧 Future Improvements
OTP-based verification using Twilio or Firebase

Real-time location sharing using Google Maps API

Push notifications for matched rides

In-app chat between matched users

Admin dashboard for ride analytics


