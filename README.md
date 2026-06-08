# RailConnect 🚄
Tkinter-Based Railway Booking Simulation

## 📖 Overview
RailConnect is a Python project that simulates a railway booking system with a graphical user interface (GUI) built using Tkinter. It models the essential workflow of train reservations in India, including route search, date validation, train selection, seat allotment, fare calculation, and ticket generation. The GUI makes the system more interactive and user-friendly compared to the console version.

## ✨ Features
- **Station Selection**: Dropdown menus for source and destination stations.
- **Date Validation**: Input travel date in DDMMYYYY format; ensures present/future bookings.
- **Train Search**: Displays available trains in a listbox based on selected route.
- **Fare Calculation**: Fixed fare per journey with 5% GST applied.
- **Seat Allotment**: Random seat assignment (1–72) with berth type logic (LB, MB, UB, SL, SU).
- **Mock Payment Gateway**: GUI form for card/PIN entry with simulated delay.
- **Ticket Generation**: Ticket details displayed in a structured window.

## ⚙️ Berth Allotment Logic
Seats are numbered 1–72. Using `seat_number % 8`, berth types are assigned:
- 1 or 4 → Lower Berth (LB)  
- 2 or 5 → Middle Berth (MB)  
- 3 or 6 → Upper Berth (UB)  
- 7 → Side Lower (SL)  
- 0 → Side Upper (SU)  

## 🛠 Prerequisites
- Python 3.6+  
- Tkinter (bundled with Python)  
- Built-in modules: `datetime`, `time`, `random`

## 🚀 How to Run
1. Save the script as `railconnect_gui.py`.
2. Open terminal/command prompt.
3. Navigate to the script directory.
4. Run:
   ```bash
   python railconnect_gui.py


