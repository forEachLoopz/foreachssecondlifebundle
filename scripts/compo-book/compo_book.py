#!/usr/bin/python3
import os
import customtkinter as ctk
import platform
import cpuinfo
import psutil
import subprocess

# Fonction pour convertir la taille de la RAM en Go
def convert_to_gb(size_in_bytes):
    return size_in_bytes / (1024 ** 3)

# Fonction pour obtenir les informations sur la carte graphique
def get_gpu_info():
    try:
        output = subprocess.check_output(["lshw", "-C", "display"]).decode("utf-8")
        return output
    except Exception as e:
        print("Erreur lors de la récupération des informations sur la carte graphique :", e)
        return "N/A"

# Création de la fenêtre principale
app = ctk.CTk()
app.geometry("500x500")
ctk.set_appearance_mode("dark")
app.title("Compo Book")

# Cadre principal
frame = ctk.CTkFrame(master=app)

# Informations générales
label = ctk.CTkLabel(frame, text="Informations système")
label.configure(font=("Arial", 14, "bold"))
label.pack()

# Numéro de série
serial_number = platform.node()
serial_number_label = ctk.CTkLabel(frame, text=f"Numéro de série : {serial_number}")
serial_number_label.pack()

# Système d'exploitation
os_info = platform.platform()
os_label = ctk.CTkLabel(frame, text=f"Système d'exploitation : {os_info}")
os_label.pack()

# Informations sur le processeur
label = ctk.CTkLabel(frame, text="Processeur :")
label.configure(font=("Arial", 12, "bold"))
label.pack()

processor_info = "N/A"
try:
    processor_info = cpuinfo.get_cpu_info()["brand_raw"]
except Exception as e:
    processor_info = "N/A"
    print("Erreur lors de la récupération des informations sur le processeur:", e)
processor_label = ctk.CTkLabel(frame, text=processor_info)
processor_label.pack()

# Informations sur la RAM
label = ctk.CTkLabel(frame, text="Mémoire vive (RAM) :")
label.configure(font=("Arial", 12, "bold"))
label.pack()

ram_installed = "N/A"
ram_usage_label = ctk.CTkLabel(frame, text="Utilisation de la RAM : ")
ram_installed_label = ctk.CTkLabel(frame, text="RAM installée : ")
label.pack()

def update_ram_info():
    global ram_installed
    global ram_usage_label
    try:
        # Exécute la commande et récupère la sortie
        ram_info = os.popen("sudo dmidecode -t memory | grep -i size").read()
        # Convertit la sortie en Go
        ram_installed_gb = convert_to_gb(sum(map(int, [line.split()[1] for line in ram_info.splitlines()])))
        ram_installed_label.configure(text=f"RAM installée : {ram_installed_gb:.2f} Go")
    except Exception as e:
        print("Erreur lors de la récupération des informations sur la RAM :", e)

    try:
        ram_usage = psutil.virtual_memory().percent
        ram_usage_label.configure(text=f"Utilisation RAM : {ram_usage}%")
    except Exception as e:
        print("Erreur lors de la récupération de l'utilisation de la RAM :", e)
    app.after(1000, update_ram_info)

update_ram_info()

# Informations sur la carte graphique
label = ctk.CTkLabel(frame, text="Carte graphique :")
label.configure(font=("Arial", 12, "bold"))
label.pack()

gpu_info = get_gpu_info()
gpu_label = ctk.CTkLabel(frame, text=gpu_info.splitlines()[0])  # Récupère seulement la première ligne
gpu_label.pack()

# Cadre de numéro de série et composants
frame.pack(pady=20, padx=60, fill="both", expand=True)
app.mainloop()
