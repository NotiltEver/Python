import tkinter as tk
import psutil
import os

# Funktion för att hämta tillgängligt RAM-minne
def get_available_memory():
    mem = psutil.virtual_memory()
    available_mem = mem.available / (1024 ** 3)  # Konverterar till GB
    return round(available_mem, 2)

# Funktion för att uppdatera RAM-status i GUI:t
def update_memory_label():
    available_mem = get_available_memory()
    memory_label.config(text=f"Tillgängligt RAM-minne: {available_mem} GB")
    root.after(1000, update_memory_label)  # Uppdaterar varje sekund

# Funktion för att rensa cache (endast för Linux-system)
def clear_cache():
    try:
        os.system('sync; echo 3 > /proc/sys/vm/drop_caches')
        status_label.config(text="Cache rensad!", fg="green")
    except Exception as e:
        status_label.config(text=f"Fel vid rensning: {str(e)}", fg="red")

# Skapar GUI-fönstret
root = tk.Tk()
root.title("RAM-Monitor och Cache Rensare")

# Skapar och placerar etiketter och knappar
memory_label = tk.Label(root, text=f"Tillgängligt RAM-minne: {get_available_memory()} GB", font=("Helvetica", 14))
memory_label.pack(pady=20)

clear_button = tk.Button(root, text="Rensa Cache", command=clear_cache, font=("Helvetica", 12))
clear_button.pack(pady=10)

status_label = tk.Label(root, text="", font=("Helvetica", 12))
status_label.pack(pady=10)

# Uppdatera RAM-status varje sekund
update_memory_label()

# Starta GUI-loop
root.mainloop()
