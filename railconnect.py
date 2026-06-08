import tkinter as tk
from tkinter import messagebox, font, ttk
from datetime import datetime
import random
import re

# --- DESIGN PALETTE ---
BG_MAIN = "#020617"      
BG_CARD = "#1e293b"      
ACCENT_CYAN = "#22d3ee"    
ACCENT_ROSE = "#f43f5e"    
TEXT_MAIN = "#ffffff"    
TEXT_DIM = "#94a3b8"     
TERMINAL_GREEN = "#4ade80"  
TICKET_GOLD = "#f59e0b"    

stations = [
    "Delhi (NDLS)", "Mumbai (CSTM)", "Kolkata (HWH)", "Chennai (MAS)",
    "Bengaluru (SBC)", "Hyderabad (SC)", "Ahmedabad (ADI)", "Pune (PUNE)",
    "Bhopal (BPL)", "Nagpur (NGP)", "Lucknow (LKO)", "Patna (PNBE)",
    "Jaipur (JP)", "Amritsar (ASR)", "Guwahati (GHY)", "Vellore (VLR)",
    "Coimbatore (CBE)", "Madurai (MDU)", "Varanasi (BSB)", "Surat (ST)"
]

station_coords = {
    "Delhi (NDLS)": (28.6, 77.2), "Mumbai (CSTM)": (19.0, 72.8), "Kolkata (HWH)": (22.5, 88.3),
    "Chennai (MAS)": (13.0, 80.2), "Bengaluru (SBC)": (12.9, 77.5), "Hyderabad (SC)": (17.3, 78.4),
    "Ahmedabad (ADI)": (23.0, 72.5), "Pune (PUNE)": (18.5, 73.8), "Bhopal (BPL)": (23.2, 77.4),
    "Nagpur (NGP)": (21.1, 79.0), "Lucknow (LKO)": (26.8, 80.9), "Patna (PNBE)": (25.5, 85.1),
    "Jaipur (JP)": (26.9, 75.7), "Amritsar (ASR)": (31.6, 74.8), "Guwahati (GHY)": (26.1, 91.7),
    "Vellore (VLR)": (12.9, 79.1), "Coimbatore (CBE)": (11.0, 76.9), "Madurai (MDU)": (9.9, 78.1),
    "Varanasi (BSB)": (25.3, 83.0), "Surat (ST)": (21.1, 72.8)
}

def calculate_network_distance(src, dest):
    if src not in station_coords or dest not in station_coords:
        return 550
    c1, c2 = station_coords[src], station_coords[dest]
    deg_dist = ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)**0.5
    return max(120, int(deg_dist * 110 * 1.25))

# --- FIXED INDIAN RAILWAYS EXPRESS ROUTE MAPS ---
trains_db = [
    # Delhi Connections
    {"no": 12951, "name": "Mumbai Tejas Rajdhani", "src": "Delhi (NDLS)", "dest": "Mumbai (CSTM)"},
    {"no": 12952, "name": "Mumbai Tejas Rajdhani ", "src": "Mumbai (CSTM)", "dest": "Delhi (NDLS)"},
    {"no": 12302, "name": "Howrah Kolkata Rajdhani", "src": "Delhi (NDLS)", "dest": "Kolkata (HWH)"},
    {"no": 12301, "name": "Howrah Kolkata Rajdhani Return", "src": "Kolkata (HWH)", "dest": "Delhi (NDLS)"},
    {"no": 12616, "name": "Grand Trunk Express", "src": "Delhi (NDLS)", "dest": "Chennai (MAS)"},
    {"no": 12615, "name": "Grand Trunk Express Return", "src": "Chennai (MAS)", "dest": "Delhi (NDLS)"},
    {"no": 22692, "name": "Bengaluru Rajdhani Express", "src": "Delhi (NDLS)", "dest": "Bengaluru (SBC)"},
    {"no": 22691, "name": "Bengaluru Rajdhani Express Return", "src": "Bengaluru (SBC)", "dest": "Delhi (NDLS)"},
    {"no": 12724, "name": "Telangana Express", "src": "Delhi (NDLS)", "dest": "Hyderabad (SC)"},
    {"no": 12723, "name": "Telangana Express Return", "src": "Hyderabad (SC)", "dest": "Delhi (NDLS)"},
    {"no": 12958, "name": "Swarna Jayanti Rajdhani", "src": "Delhi (NDLS)", "dest": "Jaipur (JP)"},
    {"no": 12957, "name": "Swarna Jayanti Rajdhani Return", "src": "Jaipur (JP)", "dest": "Delhi (NDLS)"},
    {"no": 12014, "name": "Amritsar Shatabdi Express", "src": "Delhi (NDLS)", "dest": "Amritsar (ASR)"},
    {"no": 12013, "name": "Amritsar Shatabdi Express Return", "src": "Amritsar (ASR)", "dest": "Delhi (NDLS)"},
    {"no": 12418, "name": "Prayagraj Humsafar Express", "src": "Delhi (NDLS)", "dest": "Varanasi (BSB)"},
    {"no": 12417, "name": "Prayagraj Humsafar Express Return", "src": "Varanasi (BSB)", "dest": "Delhi (NDLS)"},
    {"no": 12001, "name": "Bhopal Shatabdi Express", "src": "Delhi (NDLS)", "dest": "Bhopal (BPL)"},
    {"no": 12002, "name": "Bhopal Shatabdi Express Return", "src": "Bhopal (BPL)", "dest": "Delhi (NDLS)"},
    {"no": 12430, "name": "Lucknow Rajdhani Superfast", "src": "Delhi (NDLS)", "dest": "Lucknow (LKO)"},
    {"no": 12429, "name": "Lucknow Rajdhani Superfast Return", "src": "Lucknow (LKO)", "dest": "Delhi (NDLS)"},
    {"no": 12394, "name": "Sampoorna Kranti Express", "src": "Delhi (NDLS)", "dest": "Patna (PNBE)"},
    {"no": 12393, "name": "Sampoorna Kranti Express Return", "src": "Patna (PNBE)", "dest": "Delhi (NDLS)"},
    {"no": 15632, "name": "Guwahati Rajdhani Express", "src": "Delhi (NDLS)", "dest": "Guwahati (GHY)"},
    {"no": 15631, "name": "Guwahati Rajdhani Express Return", "src": "Guwahati (GHY)", "dest": "Delhi (NDLS)"},

    # Mumbai Connections
    {"no": 12123, "name": "Deccan Queen Express", "src": "Mumbai (CSTM)", "dest": "Pune (PUNE)"},
    {"no": 12124, "name": "Deccan Queen Express Return", "src": "Pune (PUNE)", "dest": "Mumbai (CSTM)"},
    {"no": 12922, "name": "Flying Ranee Double Decker", "src": "Mumbai (CSTM)", "dest": "Surat (ST)"},
    {"no": 12921, "name": "Flying Ranee Double Decker Return", "src": "Surat (ST)", "dest": "Mumbai (CSTM)"},
    {"no": 12934, "name": "Karnavati Superfast Express", "src": "Mumbai (CSTM)", "dest": "Ahmedabad (ADI)"},
    {"no": 12933, "name": "Karnavati Superfast Express Return", "src": "Ahmedabad (ADI)", "dest": "Mumbai (CSTM)"},
    {"no": 12105, "name": "Vidarbha Superfast Express", "src": "Mumbai (CSTM)", "dest": "Nagpur (NGP)"},
    {"no": 12106, "name": "Vidarbha Superfast Express Return", "src": "Nagpur (NGP)", "dest": "Mumbai (CSTM)"},
    {"no": 11019, "name": "Konark Intercity Express", "src": "Mumbai (CSTM)", "dest": "Hyderabad (SC)"},
    {"no": 11020, "name": "Konark Intercity Express Return", "src": "Hyderabad (SC)", "dest": "Mumbai (CSTM)"},
    {"no": 16381, "name": "Jayanti Janata Express", "src": "Mumbai (CSTM)", "dest": "Chennai (MAS)"},
    {"no": 16382, "name": "Jayanti Janata Express Return", "src": "Chennai (MAS)", "dest": "Mumbai (CSTM)"},
    {"no": 11301, "name": "Udyan Express", "src": "Mumbai (CSTM)", "dest": "Bengaluru (SBC)"},
    {"no": 11302, "name": "Udyan Express Return", "src": "Bengaluru (SBC)", "dest": "Mumbai (CSTM)"},
    {"no": 12112, "name": "Bhopal Garib Rath", "src": "Mumbai (CSTM)", "dest": "Bhopal (BPL)"},
    {"no": 12111, "name": "Bhopal Garib Rath Return", "src": "Bhopal (BPL)", "dest": "Mumbai (CSTM)"},

    # Kolkata Connections
    {"no": 12841, "name": "Coromandel Express", "src": "Kolkata (HWH)", "dest": "Chennai (MAS)"},
    {"no": 12842, "name": "Coromandel Express Return", "src": "Chennai (MAS)", "dest": "Kolkata (HWH)"},
    {"no": 12259, "name": "Kolkata Patna Duronto", "src": "Kolkata (HWH)", "dest": "Patna (PNBE)"},
    {"no": 12260, "name": "Kolkata Patna Duronto Return", "src": "Patna (PNBE)", "dest": "Kolkata (HWH)"},
    {"no": 12345, "name": "Saraighat Express", "src": "Kolkata (HWH)", "dest": "Guwahati (GHY)"},
    {"no": 12346, "name": "Saraighat Express Return", "src": "Guwahati (GHY)", "dest": "Kolkata (HWH)"},
    {"no": 12222, "name": "Howrah Pune Duronto", "src": "Kolkata (HWH)", "dest": "Pune (PUNE)"},
    {"no": 12221, "name": "Howrah Pune Duronto Return", "src": "Pune (PUNE)", "dest": "Kolkata (HWH)"},
    {"no": 12834, "name": "Howrah Ahmedabad Express", "src": "Kolkata (HWH)", "dest": "Ahmedabad (ADI)"},
    {"no": 12833, "name": "Howrah Ahmedabad Express Return", "src": "Ahmedabad (ADI)", "dest": "Kolkata (HWH)"},
    {"no": 12801, "name": "Purushottam Superfast", "src": "Kolkata (HWH)", "dest": "Varanasi (BSB)"},
    {"no": 12802, "name": "Purushottam Superfast Return", "src": "Varanasi (BSB)", "dest": "Kolkata (HWH)"},

    # Chennai Connections
    {"no": 12609, "name": "Lalbagh Shatabdi Express", "src": "Chennai (MAS)", "dest": "Bengaluru (SBC)"},
    {"no": 12610, "name": "Lalbagh Shatabdi Express Return", "src": "Bengaluru (SBC)", "dest": "Chennai (MAS)"},
    {"no": 12673, "name": "Cheran Superfast Express", "src": "Chennai (MAS)", "dest": "Coimbatore (CBE)"},
    {"no": 12674, "name": "Cheran Superfast Express Return", "src": "Coimbatore (CBE)", "dest": "Chennai (MAS)"},
    {"no": 12635, "name": "Vaigai Intercity Express", "src": "Chennai (MAS)", "dest": "Madurai (MDU)"},
    {"no": 12636, "name": "Vaigai Intercity Express Return", "src": "Madurai (MDU)", "dest": "Chennai (MAS)"},
    {"no": 22605, "name": "Vellore Intercity Express", "src": "Chennai (MAS)", "dest": "Vellore (VLR)"},
    {"no": 22606, "name": "Vellore Intercity Express Return", "src": "Vellore (VLR)", "dest": "Chennai (MAS)"},
    {"no": 12759, "name": "Charminar Express", "src": "Chennai (MAS)", "dest": "Hyderabad (SC)"},
    {"no": 12760, "name": "Charminar Express Return", "src": "Hyderabad (SC)", "dest": "Chennai (MAS)"}
]

berth_map = {1: "Lower", 4: "Lower", 2: "Middle", 5: "Middle", 3: "Upper", 6: "Upper", 7: "Side Lower", 0: "Side Upper"}

class RailConnectApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RailConnect Master Grid")
        self.root.geometry("620x760") 
        self.root.configure(bg=BG_MAIN)
        self.available_trains = []
        self.setup_ui()

    def setup_ui(self):
        # --- HEADER BANNER ---
        header = tk.Frame(self.root, bg=BG_MAIN, pady=10)
        header.pack(fill="x")
        tk.Label(header, text="RAILCONNECT MASTER GRID", font=("Impact", 26), fg=ACCENT_CYAN, bg=BG_MAIN).pack()
        tk.Label(header, text="PASSENGER METRICS AND EXPRESS DATA GRID SYSTEM", font=("Consolas", 9), fg=TEXT_DIM, bg=BG_MAIN).pack()

        # --- CARD FRAME (INPUT LAYOUT) ---
        card_frame = tk.Frame(self.root, bg=BG_CARD, padx=20, pady=12, highlightbackground="#334155", highlightthickness=1)
        card_frame.pack(pady=5, padx=35, fill="x")

        # Select Station Nodes
        tk.Label(card_frame, text="SOURCE HUB STATION:", fg=TEXT_DIM, bg=BG_CARD, font=("Consolas", 10, "bold")).grid(row=0, column=0, sticky="w", pady=4)
        self.source_var = tk.StringVar()
        self.source_cb = ttk.Combobox(card_frame, textvariable=self.source_var, values=stations, state="readonly", width=25)
        self.source_cb.grid(row=0, column=1, sticky="e", pady=4, padx=(15, 0))

        tk.Label(card_frame, text="TARGET DESTINATION :", fg=TEXT_DIM, bg=BG_CARD, font=("Consolas", 10, "bold")).grid(row=1, column=0, sticky="w", pady=4)
        self.dest_var = tk.StringVar()
        self.dest_cb = ttk.Combobox(card_frame, textvariable=self.dest_var, values=stations, state="readonly", width=25)
        self.dest_cb.grid(row=1, column=1, sticky="e", pady=4, padx=(15, 0))

        # Departure Date Input
        tk.Label(card_frame, text="DEPARTURE TIMING  :", fg=TEXT_DIM, bg=BG_CARD, font=("Consolas", 10, "bold")).grid(row=2, column=0, sticky="w", pady=4)
        inner_date_frame = tk.Frame(card_frame, bg=BG_MAIN, highlightbackground="#475569", highlightthickness=1)
        inner_date_frame.grid(row=2, column=1, sticky="e", pady=4)
        
        self.date_entry = tk.Entry(inner_date_frame, bg=BG_MAIN, fg=TEXT_MAIN, insertbackground="white", relief="flat", font=("Consolas", 11), width=18, justify="center")
        self.date_entry.pack(side="left", padx=4, pady=2)
        self.date_entry.insert(0, datetime.now().strftime("%d/%m/%Y")) # Sets default using / separator
        tk.Label(inner_date_frame, text="DD/MM/YYYY", fg=TEXT_DIM, bg=BG_MAIN, font=("Consolas", 8, "bold")).pack(side="right", padx=6)

        # Berth Layer Preference
        tk.Label(card_frame, text="BERTH VECTOR LAYER:", fg=TEXT_DIM, bg=BG_CARD, font=("Consolas", 10, "bold")).grid(row=3, column=0, sticky="w", pady=4)
        self.seat_pref = tk.StringVar()
        self.seat_cb = ttk.Combobox(card_frame, textvariable=self.seat_pref, values=["Lower Berth", "Middle Berth", "Upper Berth", "Side Lower", "Side Upper"], state="readonly", width=25)
        self.seat_cb.grid(row=3, column=1, sticky="e", pady=4, padx=(15, 0))
        self.seat_cb.current(0)

        # Passenger Standard Input Blocks
        tk.Label(card_frame, text="PASSENGER NAME    :", fg=TEXT_DIM, bg=BG_CARD, font=("Consolas", 10, "bold")).grid(row=4, column=0, sticky="w", pady=4)
        self.name_entry = tk.Entry(card_frame, bg=BG_MAIN, fg=TEXT_MAIN, insertbackground="white", relief="flat", font=("Consolas", 10), width=27, highlightthickness=1, highlightbackground="#475569")
        self.name_entry.grid(row=4, column=1, sticky="e", pady=4)
        self.name_entry.insert(0, "")

        tk.Label(card_frame, text="PASSENGER AGE     :", fg=TEXT_DIM, bg=BG_CARD, font=("Consolas", 10, "bold")).grid(row=5, column=0, sticky="w", pady=4)
        self.age_entry = tk.Entry(card_frame, bg=BG_MAIN, fg=TEXT_MAIN, insertbackground="white", relief="flat", font=("Consolas", 10), width=27, highlightthickness=1, highlightbackground="#475569")
        self.age_entry.grid(row=5, column=1, sticky="e", pady=4)
        self.age_entry.insert(0, "")

        # --- SEARCH ENGINES BUTTON PANEL ---
        btn_frame = tk.Frame(self.root, bg=BG_MAIN)
        btn_frame.pack(pady=8, padx=35, fill="x")

        tk.Button(btn_frame, text="SEARCH TRAINS", command=self.search_trains, 
                  bg=ACCENT_CYAN, fg=BG_MAIN, font=("Arial", 12, "bold"), 
                  activebackground=TERMINAL_GREEN, relief="flat", cursor="hand2", pady=6).pack(fill="x", pady=2)

        # --- INTERACTIVE OUTPUT GRID OVERVIEW ---
        self.list_container = tk.Frame(self.root, bg=BG_MAIN)
        self.list_container.pack(pady=5, padx=35, fill="x")
        
        tk.Label(self.list_container, text="ACTIVE VERIFIED COUPLING MATCHES", fg=ACCENT_CYAN, bg=BG_MAIN, font=("Consolas", 10, "bold")).pack(anchor="w", pady=(2, 2))
        
        self.train_list = tk.Listbox(self.list_container, width=65, height=6, bg=BG_CARD, fg=TEXT_MAIN, 
                                     selectbackground=ACCENT_CYAN, selectforeground=BG_MAIN, 
                                     font=("Consolas", 10), relief="flat", highlightthickness=1, highlightbackground="#334155")
        self.train_list.pack(fill="x", pady=2)

        self.book_btn = tk.Button(self.list_container, text="PROCEED TO BOOK TICKET", command=self.validate_and_checkout, 
                                  bg=TERMINAL_GREEN, fg=BG_MAIN, font=("Arial", 11, "bold"), 
                                  activebackground=TICKET_GOLD, relief="flat", cursor="hand2", pady=6)
        self.book_btn.pack(fill="x", pady=4)

    def parse_flexible_date(self, date_str):
        # Normalizes dates split by /, \, or . into an explicit clean string segment
        clean_date = re.sub(r'[\\/.]', '', date_str).strip()
        try:
            parsed_d = datetime.strptime(clean_date, "%d%m%Y")
            return parsed_d.strftime("%d-%m-%Y")
        except ValueError:
            return None

    def search_trains(self):
        src, dest, date_str = self.source_var.get(), self.dest_var.get(), self.date_entry.get().strip()
        
        if not src or not dest:
            messagebox.showerror("Terminal Error", "Please specify both Origin and Target Destination nodes.")
            return
        if src == dest:
            messagebox.showerror("Mapping Exception", "Origin and Destination stations cannot be structural mirrors.")
            return
        
        formatted_date = self.parse_flexible_date(date_str)
        if not formatted_date:
            messagebox.showerror("Format Error", "Travel date format deviation! Match layout patterns like DD/MM/YYYY, DD\\MM\\YYYY, or DD.MM.YYYY.")
            return

        self.train_list.delete(0, tk.END)
        self.available_trains = [t for t in trains_db if t["src"] == src and t["dest"] == dest]

        for t in self.available_trains:
            self.train_list.insert(tk.END, f" #{t['no']} | {t['name'].ljust(33)} | Express Track Line")
        
        if self.available_trains:
            self.train_list.selection_set(0)
        else:
            messagebox.showwarning("Routing Absence", f"No explicit line indexed for {src} to {dest}.\nTry major routes like Delhi (NDLS) to Mumbai (CSTM).")

    def validate_and_checkout(self):
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        date_str = self.date_entry.get().strip()
        selection = self.train_list.curselection()

        if not name or not age:
            messagebox.showerror("Manifest Missing", "Passenger details empty! Please assign Name and Age values.")
            return
        if not age.isdigit() or int(age) <= 0 or int(age) > 120:
            messagebox.showerror("Validation Error", "Invalid parameter layout: Please write a valid numerical Age.")
            return
        
        formatted_date = self.parse_flexible_date(date_str)
        if not formatted_date:
            messagebox.showerror("Date Error", "Invalid tracking timestamp mapping layout configuration.")
            return
            
        if not selection:
            messagebox.showerror("Selection Deficit", "No index channel selected. Hit 'SEARCH TRAINS' and choose a line module.")
            return

        selected_train = self.available_trains[selection[0]]
        self.trigger_payment_gateway(selected_train, name, age, formatted_date)

    def trigger_payment_gateway(self, selected_train, passenger_name, passenger_age, travel_date):
        src, dest = self.source_var.get(), self.dest_var.get()
        distance = calculate_network_distance(src, dest)
        fare = 120 + int(distance * 1.90)

        pay_win = tk.Toplevel(self.root)
        pay_win.title("Secure Payment Gateway Interface")
        pay_win.geometry("450x440")
        pay_win.configure(bg=BG_CARD)
        pay_win.resizable(False, False)
        pay_win.transient(self.root)
        pay_win.grab_set()

        top_banner = tk.Frame(pay_win, bg="#0f172a", pady=10)
        top_banner.pack(fill="x")
        tk.Label(top_banner, text="SECURE TRANSACTION PORTAL", font=("Consolas", 12, "bold"), fg=ACCENT_CYAN, bg="#0f172a").pack()

        amt_frame = tk.Frame(pay_win, bg=BG_MAIN, padx=15, pady=8, highlightbackground="#334155", highlightthickness=1)
        amt_frame.pack(pady=10, padx=25, fill="x")
        tk.Label(amt_frame, text=f"PASSENGER: {passenger_name.upper()} ({passenger_age} Yrs)", font=("Consolas", 9, "bold"), fg=ACCENT_CYAN, bg=BG_MAIN).pack(anchor="w")
        tk.Label(amt_frame, text=f"TRAIN ENGINE: #{selected_train['no']} - {selected_train['name']}", font=("Consolas", 9), fg=TEXT_DIM, bg=BG_MAIN).pack(anchor="w", pady=2)
        tk.Label(amt_frame, text=f"TOTAL PAYABLE: ₹{fare}.00", font=("Consolas", 13, "bold"), fg=TERMINAL_GREEN, bg=BG_MAIN).pack(anchor="w", pady=(2,0))

        input_frame = tk.Frame(pay_win, bg=BG_CARD)
        input_frame.pack(pady=5, padx=25, fill="x")

        tk.Label(input_frame, text="SELECT METHOD:", font=("Consolas", 9, "bold"), fg=TEXT_DIM, bg=BG_CARD).grid(row=0, column=0, sticky="w", pady=5)
        method_var = tk.StringVar(value="CARD")
        
        def toggle_inputs():
            if method_var.get() == "CARD":
                lbl_1.config(text="CARD NUMBER:")
                lbl_2.config(text="EXPIRY / CVV:")
                ent_1.delete(0, tk.END); ent_1.insert(0, "")
                ent_2.delete(0, tk.END); ent_2.insert(0, "")
            else:
                lbl_1.config(text="VPA / UPI ID:")
                lbl_2.config(text="PIN :")
                ent_1.delete(0, tk.END); ent_1.insert(0, "")
                ent_2.delete(0, tk.END); ent_2.insert(0, "")

        r_card = tk.Radiobutton(input_frame, text="Credit/Debit", variable=method_var, value="CARD", bg=BG_CARD, fg=TEXT_MAIN, selectcolor=BG_MAIN, activebackground=BG_CARD, activeforeground=TEXT_MAIN, font=("Consolas", 9), command=toggle_inputs)
        r_card.grid(row=0, column=1, padx=5, sticky="w")
        r_upi = tk.Radiobutton(input_frame, text="UPI Interface", variable=method_var, value="UPI", bg=BG_CARD, fg=TEXT_MAIN, selectcolor=BG_MAIN, activebackground=BG_CARD, activeforeground=TEXT_MAIN, font=("Consolas", 9), command=toggle_inputs)
        r_upi.grid(row=0, column=2, padx=5, sticky="w")

        lbl_1 = tk.Label(input_frame, text="CARD NUMBER:", font=("Consolas", 9, "bold"), fg=TEXT_DIM, bg=BG_CARD)
        lbl_1.grid(row=1, column=0, sticky="w", pady=10)
        ent_1 = tk.Entry(input_frame, bg=BG_MAIN, fg=TEXT_MAIN, relief="flat", font=("Consolas", 10), insertbackground="white", highlightthickness=1, highlightbackground="#475569")
        ent_1.grid(row=1, column=1, columnspan=2, sticky="ew", pady=10, ipady=3)

        lbl_2 = tk.Label(input_frame, text="EXPIRY / CVV:", font=("Consolas", 9, "bold"), fg=TEXT_DIM, bg=BG_CARD)
        lbl_2.grid(row=2, column=0, sticky="w", pady=10)
        ent_2 = tk.Entry(input_frame, bg=BG_MAIN, fg=TEXT_MAIN, relief="flat", font=("Consolas", 10), insertbackground="white", highlightthickness=1, highlightbackground="#475569")
        ent_2.grid(row=2, column=1, columnspan=2, sticky="ew", pady=10, ipady=3)

        toggle_inputs()

        status_lbl = tk.Label(pay_win, text="[ AWAITING AUTHENTICATION SECURE PACKET ]", font=("Consolas", 8), fg=TEXT_DIM, bg=BG_CARD)
        status_lbl.pack(pady=8)

        def run_processing():
            btn_action.config(state="disabled", text="PROCESSING VIA NPCI...")
            stages = [
                ("CONNECTING BANK ECOSYSTEM...", ACCENT_CYAN),
                ("VERIFYING GATEWAY CAPTURE...", TICKET_GOLD),
                ("TRANSACTION SETTLED SUCCESSFULLY!", TERMINAL_GREEN)
            ]
            
            def update_stage(idx):
                if idx < len(stages):
                    status_lbl.config(text=f"» {stages[idx][0]}", fg=stages[idx][1])
                    pay_win.after(700, lambda: update_stage(idx + 1))
                else:
                    pay_win.destroy()
                    self.book_ticket(selected_train, distance, fare, passenger_name, passenger_age, travel_date)

            update_stage(0)

        btn_action = tk.Button(pay_win, text=f"AUTHORIZE PAYMENT • ₹{fare}.00", command=run_processing,
                               bg=TERMINAL_GREEN, fg=BG_MAIN, font=("Arial", 10, "bold"), relief="flat", cursor="hand2", pady=8)
        btn_action.pack(fill="x", padx=25, pady=5)

    def book_ticket(self, selected_train, distance, fare, name, age, travel_date):
        src, dest = self.source_var.get(), self.dest_var.get()
        pnr = random.randint(4810000000, 4999999999)
        coach, seat = f"A{random.randint(1, 4)}", random.randint(1, 64)
        berth = berth_map[seat % 8]

        popup = tk.Toplevel(self.root)
        popup.title(f"Manifest Token Confirmation - PNR {pnr}")
        popup.geometry("550x380")
        popup.configure(bg=BG_CARD)
        popup.resizable(False, False)
        popup.transient(self.root)

        top_bar = tk.Frame(popup, bg=TICKET_GOLD, pady=8)
        top_bar.pack(fill="x")
        tk.Label(top_bar, text="IR-RAILCONNECT BOARDING PASS (PAID)", font=("Consolas", 12, "bold"), fg=BG_MAIN, bg=TICKET_GOLD).pack()

        body = tk.Frame(popup, bg=BG_CARD, padx=22, pady=12)
        body.pack(fill="both", expand=True)

        tk.Label(body, text=f"{src.split(' ')[0].upper()}  ➔  {dest.split(' ')[0].upper()}", font=("Verdana", 14, "bold"), fg=ACCENT_CYAN, bg=BG_CARD).pack(anchor="w", pady=(0, 2))
        
        info_frame = tk.Frame(body, bg=BG_CARD)
        info_frame.pack(fill="x", pady=8)

        display_name = selected_train['name']
        if len(display_name) > 22: display_name = display_name[:20] + ".."

        details = [
            ("PNR TRANSIT NO:", pnr, "TRAVEL DATE:", travel_date),
            ("TRAIN ENGINE:", f"#{selected_train['no']}", "ASSIGNED LINE:", display_name),
            ("COACH / UNIT:", f"{coach} / SEAT {seat}", "BERTH SECTOR:", berth),
            ("PASSENGER NAME:", name.upper(), "PASSENGER AGE:", f"{age} YRS"),
            ("DISTANCE RUN:", f"{distance} KM", "METRIC FARE :", f"₹{fare}.00 [PAID]")
        ]

        for r, (lbl1, val1, lbl2, val2) in enumerate(details):
            tk.Label(info_frame, text=lbl1, font=("Consolas", 9, "bold"), fg=TEXT_DIM, bg=BG_CARD).grid(row=r, column=0, sticky="w", pady=4)
            tk.Label(info_frame, text=val1, font=("Consolas", 9), fg=TEXT_MAIN, bg=BG_CARD).grid(row=r, column=1, sticky="w", padx=(5, 12), pady=4)
            tk.Label(info_frame, text=lbl2, font=("Consolas", 9, "bold"), fg=TEXT_DIM, bg=BG_CARD).grid(row=r, column=2, sticky="w", pady=4)
            tk.Label(info_frame, text=val2, font=("Consolas", 9), fg=TEXT_MAIN, bg=BG_CARD).grid(row=r, column=3, sticky="w", pady=4)

        deco_frame = tk.Frame(body, bg=BG_MAIN, height=35, pady=5)
        deco_frame.pack(fill="x", pady=(10, 0))
        
        barcode_str = "|||||| | |||| || ||||||| || |||| |||| |||| | |||| || ||" 
        tk.Label(deco_frame, text=barcode_str, font=("Courier New", 11), fg=TEXT_DIM, bg=BG_MAIN).pack()

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TCombobox", fieldbackground=BG_MAIN, background=ACCENT_CYAN, foreground=TEXT_MAIN, arrowcolor=ACCENT_CYAN)
    style.map("TCombobox", fieldbackground=[("readonly", BG_MAIN)], foreground=[("readonly", TEXT_MAIN)])
    
    app = RailConnectApp(root)
    root.mainloop()
