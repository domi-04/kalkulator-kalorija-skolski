from tkinter import *

import tkinter.messagebox as msg

root = Tk()
root.title("Kalkulator unosa kalorija")
root.geometry("710x330")
root.resizable(False, False)

# Funkcije:

def kalkulacija():
    try:
        _tezina = int(tezina.get())
        _godine = int(godine.get())
        _visina = int(visina.get())
        _fiz_aktivnost = float(fiz_aktivnost.get())
        _spol = int(spol.get()) # 1 = musko, 2 = zensko

        if (_spol == 1):
            potrebne_kalorije = (66.5 + 13.8*_tezina + 5*_visina - 6.8*_godine) * _fiz_aktivnost
        elif (_spol == 2):
            potrebne_kalorije = (655.1 + 9.6*_tezina + 1.9*_visina - 4.7*_godine) * _fiz_aktivnost

        msg.showinfo("Potrebne kalorije", f"Potrebno je unijeti {potrebne_kalorije:.2f} kalorija")

    except:
        msg.showerror("Pogreska", "Ispunite sva polja ispravno!")

# Definicije elemenata:

tezina = Entry(root, width=18, font=("",12))
godine = Entry(root, width=18, font=("",12))
visina = Entry(root, width=18, font=("",12))

fiz_aktivnost = StringVar()
fiz_aktivnost.set("1.3")

spol = IntVar()
spol.set(1)

slaba_aktivnost = Radiobutton(root, text="Slaba", variable=fiz_aktivnost, value="1.2", font=("",12), pady=5)
normalna_aktivnost = Radiobutton(root, text="Normalna", variable=fiz_aktivnost, value="1.3", font=("",12),pady=5)
intezivna_aktivnost = Radiobutton(root, text="Intezivna", variable=fiz_aktivnost, value="1.4", font=("",12), pady=5)

musko = Radiobutton(root, text="Musko", variable=spol, value=1, font=("",12), pady=5)
zensko = Radiobutton(root, text="Zensko", variable=spol, value=2, font=("",12), pady=5)

naziv = Label(root, text="Kalkulator unosa kalorija", font=("",18), pady=10, padx=10)

text_tezina = Label(root, text="Tezina (kg):", font=("",12), pady=5)
text_visina = Label(root, text="Visina (cm):", font=("",12), pady=5)
text_godine = Label(root, text="Godine:", font=("",12), pady=5)
text_fiz_aktivnost = Label(root, text="Fizicka aktivnost (tijekom dana):", font=("",12), pady=5)

kalkuliraj = Button(root, text="Kalkuliraj!", command=kalkulacija, font=("",12), pady=10)

# Crtanje elemenata u grid:

naziv.grid(row=0)
text_tezina.grid(row=1, sticky=E)
text_visina.grid(row=2, sticky=E)
text_godine.grid(row=3, sticky=E)
text_fiz_aktivnost.grid(row=4, sticky=E)

tezina.grid(row=1, column=1, columnspan=2)
visina.grid(row=2, column=1, columnspan=2)
godine.grid(row=3, column=1, columnspan=2)
slaba_aktivnost.grid(row=4, column=1, sticky=W)
normalna_aktivnost.grid(row=4, column=2, sticky=W)
intezivna_aktivnost.grid(row=4, column=3, sticky=W)

musko.grid(row=5)
zensko.grid(row=5, column=1)

kalkuliraj.grid(row=6, column=3)



root.mainloop()