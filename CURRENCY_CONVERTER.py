import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests

# Get live exchange rates using an API
def fetch_live_rates():
    api_key = 'Fetch your API key from https://www.exchangerate-api.com/'
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data['result'] == 'success':
        return data['conversion_rates']
    else:
        messagebox.showerror("API Error", "Failed to fetch live exchange rates.")
        return None

# Update global rates_vs_usd with live data
live_rates = fetch_live_rates()
if live_rates:
    rates_vs_usd = live_rates



# A rough reference for currency conversion 
rates_vs_usd = {
    'USD': 1.0,
    'EUR': 0.85,
    'INR': 83.12,
    'JPY': 156.35,
    'GBP': 0.76
}

# Function to convert currency
def convert_currency():
    try:
        raw_input = amount_entry.get()
        amount = float(raw_input)  # Converting string input to float 
        source_curr = from_dropdown.get()
        target_curr = to_dropdown.get()

    
        # Convert source amount to USD first 
        usd_amount = amount / rates_vs_usd[source_curr]

        # USD to target currency
        converted = usd_amount * rates_vs_usd[target_curr]

        # Show the result (Note: rounding to 2 decimal places)
        result_display.config(text=f"{amount:.2f} {source_curr} = {converted:.2f} {target_curr}")

    except ValueError:
        # Happens if input isn't a valid number — probably someone typed text in the amount field
        messagebox.showerror("Invalid Input", "Try entering a number for the amount.")

# --- GUI Setup ---

app = tk.Tk()
app.title("💱 Srinjoy's Currency Converter")
app.geometry("400x400")
app.resizable(width=False, height=False)

# Load image 
bg_image = Image.open("C:/Users/User/Documents/download.jpg")#put ur custom image file name here
bg_image = bg_image.resize((400, 400))#same size as your app window
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Label to hold the background
bg_label = tk.Label(app, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # fill the entire window

# Heading of tab
tk.Label(app, text="Currency Converter", font=("Arial", 16, "bold")) \
    .grid(row=0, column=0, columnspan=2, pady=12)

# Input field for amount
tk.Label(app, text="Amount:") \
    .grid(row=1, column=0, padx=10, sticky="e")

amount_entry = tk.Entry(app, width=22,)
amount_entry.grid(row=1, column=1, padx=10, pady=4, sticky="w")

#Dropdown for source currency 
from_label = tk.Label(app, text="From:",)
from_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

from_dropdown = ttk.Combobox(app, values=list(rates_vs_usd.keys()), state="readonly")
from_dropdown.grid(row=2, column=1, padx=10, pady=10, sticky="w")
from_dropdown.current(0)  # Default to USD

#Dropdown for target currency 
to_label = tk.Label(app, text="To:",)
to_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

to_dropdown = ttk.Combobox(app, values=list(rates_vs_usd.keys()), state="readonly")
to_dropdown.grid(row=3, column=1, padx=10, pady=10, sticky="w")
to_dropdown.current(1)  # Default to EUR

# Convert Button
convert_btn = tk.Button(app, text="Convert", command=convert_currency, fg="black")
convert_btn.grid(row=4, column=0, columnspan=2, pady=10)

# Result display
result_display = tk.Label(app, text="", font=("Arial", 12), fg="#000000")
result_display.grid(row=5, column=0, columnspan=5, pady=12, sticky="nsew")


# Start the event loop
app.mainloop()
