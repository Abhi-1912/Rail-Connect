# RailConnect 🚄
Console-Based Railway Booking Simulation

## 📖 Overview
RailConnect is a Python-based simulation of a railway booking system. Designed as a student project, it models the essential workflow of train reservations in India. The program demonstrates route search, date validation, train selection, fare calculation, seat allotment, and ticket generation — all within a console interface. It aims to provide a simplified yet realistic view of how railway booking systems operate.

## ✨ Features
- **Route Search**: Search trains between predefined cities (BHOPAL, AMARAVATI, VELLORE, CHENNAI).
- **Date Validation**: Accepts DDMMYYYY format and ensures bookings are for present/future dates.
- **Train Selection**: Displays filtered trains and allows user choice.
- **Fare Calculation**: Fixed fare per journey with 5% GST applied.
- **Seat Allotment**: Random seat assignment with berth type logic based on Indian Railways 8-berth bay.
- **Mock Payment Gateway**: Simulates card/PIN validation and transaction delay.
- **Ticket Generation**: Prints a structured ticket with journey, seat, and payment details.

## ⚙️ Berth Allotment Logic
Seats are numbered 1–72. Using `seat_number % 8`, berth types are assigned:
- 1 or 4 → Lower Berth (LB)  
- 2 or 5 → Middle Berth (MB)  
- 3 or 6 → Upper Berth (UB)  
- 7 → Side Lower (SL)  
- 0 → Side Upper (SU)  

This mimics the standard 8-berth bay layout in Indian Railways coaches.

## 🛠 Prerequisites
- Python 3.6+  
- Built-in modules only: `datetime`, `time`, `random`  

No external dependencies required.

## 🚀 How to Run
1. Save the script as `railconnect_booking.py`.
2. Open terminal/command prompt.
3. Navigate to the script directory.
4. Run:
   ```bash
   python railconnect_booking.py

