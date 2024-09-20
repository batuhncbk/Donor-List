import tkinter as tk
from tkinter import messagebox
import os

# Bağış verilerini dosyadan oku
def load_donations():
    donations = {}
    if os.path.exists("donations.txt"):
        with open("donations.txt", "r") as f:
            for line in f:
                name, amount = line.strip().split(":")
                donations[name] = float(amount)
    return donations

# Bağış verilerini dosyaya yaz
def save_donations(donations):
    with open("donations.txt", "w") as f:
        for name, amount in donations.items():
            f.write(f"{name}:{amount}\n")

# Bağış ekle veya güncelle
def add_data():
    name = name_entry.get().strip()
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir bağış miktarı girin.")
        return

    if not name:
        messagebox.showerror("Hata", "Geçerli bir isim girin.")
        return

    if amount <= 0:
        messagebox.showerror("Hata", "Bağış miktarı pozitif olmalıdır.")
        return

    if name in donations:
        donations[name] += amount
    else:
        donations[name] = amount

    save_donations(donations)
    total_donation = donations[name]
    messagebox.showinfo("Bilgi", f"{name} adlı bağışçının toplam bağış miktarı: {total_donation} TL")
    update_total_donations()
    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# Bağışçının toplam bağışını göster
def show_donor_total():
    name = name_entry.get().strip()
    if name in donations:
        total_donation = donations[name]
        messagebox.showinfo("Bilgi", f"{name} adlı bağışçının toplam bağış miktarı: {total_donation} TL")
    else:
        messagebox.showinfo("Bilgi", f"{name} adlı bağışçı bulunamadı.")
    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# Toplam bağışları güncelle
def update_total_donations():
    total_donation = sum(donations.values())
    total_donation_label.config(text=f"Toplam Bağış: {total_donation:.2f} TL")

# GUI oluştur
root = tk.Tk()
root.title("Bağış Yönetimi")
root.geometry("300x180")
root.config(bg="#f2f2f2")  # Soft background color
root.resizable(False, False)

# Bağış verilerini yükle
donations = load_donations()

# Ana çerçeve
main_frame = tk.Frame(root, bg="#f2f2f2")
main_frame.pack(padx=20, pady=20)

# İsim ve bağış miktarı girişi
tk.Label(main_frame, text="Bağışçı Adı:", bg="#f2f2f2").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(main_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(main_frame, text="Bağış Miktarı:", bg="#f2f2f2").grid(row=1, column=0, padx=10, pady=5)
amount_entry = tk.Entry(main_frame)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

# Butonlar
add_button = tk.Button(main_frame, text="Veri Ekle", command=add_data, bg="#4CAF50", fg="white")
add_button.grid(row=2, column=0, padx=10, pady=10)

total_donor_button = tk.Button(main_frame, text="Toplam Bağışçı", command=show_donor_total, bg="#008CBA", fg="white")
total_donor_button.grid(row=2, column=1, padx=10, pady=10)

# Toplam bağış etiketi
total_donation_label = tk.Label(main_frame, text="Toplam Bağış: 0.00 TL", bg="#f2f2f2")
total_donation_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Toplam bağışları başlatırken güncelle
update_total_donations()

# Enter tuşuyla veri ekleme
root.bind('<Return>', lambda event: add_data())

# GUI döngüsünü başlat
root.mainloop()
