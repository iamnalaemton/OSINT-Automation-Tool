import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
import whois
import socket

# Function to perform OSINT on the target domain
def perform_osint():
    target = domain_entry.get()
    if not target:
        messagebox.showerror("Error", "Please enter a domain.")
        return

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Starting OSINT for: {target}\n\n")

    try:
        # WHOIS Information
        output_text.insert(tk.END, "Fetching WHOIS information...\n")
        whois_data = whois.whois(target)
        output_text.insert(tk.END, f"Registrar: {whois_data.registrar}\n")
        output_text.insert(tk.END, f"Creation Date: {whois_data.creation_date}\n")
        output_text.insert(tk.END, f"Expiration Date: {whois_data.expiration_date}\n\n")

        # IP Address Lookup
        output_text.insert(tk.END, "Fetching IP address...\n")
        ip_address = socket.gethostbyname(target)
        output_text.insert(tk.END, f"IP Address: {ip_address}\n\n")

        # Geolocation of IP
        output_text.insert(tk.END, "Fetching geolocation of IP address...\n")
        geo_response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        geo_data = geo_response.json()
        output_text.insert(tk.END, f"City: {geo_data.get('city', 'N/A')}\n")
        output_text.insert(tk.END, f"Region: {geo_data.get('region', 'N/A')}\n")
        output_text.insert(tk.END, f"Country: {geo_data.get('country', 'N/A')}\n")
        output_text.insert(tk.END, f"Organization: {geo_data.get('org', 'N/A')}\n\n")

        # Subdomain Enumeration
        output_text.insert(tk.END, "Fetching subdomains (using hackertarget)...\n")
        subdomains_response = requests.get(f"https://api.hackertarget.com/hostsearch/?q={target}")
        if subdomains_response.status_code == 200:
            subdomains = subdomains_response.text.splitlines()
            output_text.insert(tk.END, "Subdomains found:\n")
            for sub in subdomains:
                output_text.insert(tk.END, f"- {sub.split(',')[0]}\n")
        else:
            output_text.insert(tk.END, "Failed to fetch subdomains.\n")

    except Exception as e:
        output_text.insert(tk.END, f"Error during OSINT: {e}\n")

# GUI Setup
root = tk.Tk()
root.title("OSINT Automation Tool")
root.geometry("600x600")

# Domain Input
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Enter Target Domain:").pack(side=tk.LEFT)
domain_entry = tk.Entry(frame, width=30)
domain_entry.pack(side=tk.LEFT, padx=5)

# Start Button
start_button = tk.Button(root, text="Start OSINT", command=perform_osint)
start_button.pack(pady=10)

# Output Display
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=30)
output_text.pack(pady=10)

# Run the application
root.mainloop()
