import algorithm as des
import tkinter as tk
import tkinter.font as tkFont
import os.path
import numpy as np
from pathlib import Path
import algorithm

# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class App:
    def __init__(self,window):

        self.v = tk.IntVar()
        self.knapsack = des.Knapsack()
        self.canvas = Canvas(
            window,
            bg="#FFFFFF",
            height=561,
            width=665,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            274.0,
            41.5,
            image=self.entry_image_1
        )
        self.  klucz_publiczny = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.  klucz_publiczny.place(
            x=60.0,
            y=34.0,
            width=410.0,
            height=18.0
        )

        self.canvas.create_text(
            27.0,
            9.0,
            anchor="nw",
            text="Klucz publiczny ",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))

        entry_bg_2 = self.canvas.create_image(
            143.0,
            291.5,
            image=self.entry_image_2
        )
        self. sciezka_odczytu_tekst_jawny = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.sciezka_odczytu_tekst_jawny.place(
            x=29.0,
            y=283.0,
            width=225.0,
            height=18.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            143.0,
            398.0,
            image=self.entry_image_3
        )
        self.  tekst_jawny = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self. tekst_jawny.place(
            x=29.0,
            y=320.0,
            width=225.0,
            height=158.0
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            492.0,
            403.0,
            image=self.entry_image_4
        )
        self.   kryptogram = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.  kryptogram.place(
            x=379.0,
            y=323.0,
            width=225.0,
            height=158.0
        )

        self.canvas.create_text(
            25.0,
            259.0,
            anchor="nw",
            text="Ścieżka odczytu pliku z tekstem jawnym",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            493.0,
            291.5,
            image=self.entry_image_5
        )
        self. sciezka_odczytu_kryptogram = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.sciezka_odczytu_kryptogram.place(
            x=380.0,
            y=285.0,
            width=210.0,
            height=17.0
        )

        self.canvas.create_text(
            375.0,
            259.0,
            anchor="nw",
            text="Ścieżka odczytu pliku z kryptogramem",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        entry_bg_6 = self.canvas.create_image(
            142.0,
            529.5,
            image=self.entry_image_6
        )
        self. sciezka_zapisu_tekst_jawny = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self. sciezka_zapisu_tekst_jawny.place(
            x=29.0,
            y=522.0,
            width=220.0,
            height=17.0
        )

        self.canvas.create_text(
            24.0,
            497.0,
            anchor="nw",
            text="Ścieżka zapisu pliku z tekstem jawnym",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_7.png"))
        entry_bg_7 = self.canvas.create_image(
            492.0,
            529.5,
            image=self.entry_image_7
        )
        self. sciezka_zapisu_kryptogram = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self. sciezka_zapisu_kryptogram.place(
            x=380.0,
            y=521.0,
            width=220.0,
            height=17.0
        )

        self.canvas.create_text(
            374.0,
            497.0,
            anchor="nw",
            text="Ścieżka zapisu pliku z kryptogramem",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_text(
            27.0,
            34.0,
            anchor="nw",
            text="a’",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.entry_image_8 = PhotoImage(
            file=relative_to_assets("entry_8.png"))
        entry_bg_8 = self.canvas.create_image(
            274.0,
            91.5,
            image=self.entry_image_8
        )
        self. klucz_prywatny_a = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.klucz_prywatny_a.place(
            x=59.0,
            y=82.0,
            width=430.0,
            height=21.0
        )

        self.canvas.create_text(
            27.0,
            59.0,
            anchor="nw",
            text="Klucz prywatny ",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_text(
            27.0,
            84.0,
            anchor="nw",
            text="a",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.entry_image_9 = PhotoImage(
            file=relative_to_assets("entry_9.png"))
        entry_bg_9 = self.canvas.create_image(
            135.5,
            121.5,
            image=self.entry_image_9
        )
        self.klucz_prywatny_M = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.klucz_prywatny_M.place(
            x=59.0,
            y=113.0,
            width=155.0,
            height=19.0
        )

        self.canvas.create_text(
            27.0,
            114.0,
            anchor="nw",
            text="M",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.entry_image_10 = PhotoImage(
            file=relative_to_assets("entry_10.png"))
        entry_bg_10 = self.canvas.create_image(
            196.5,
            188.5,
            image=self.entry_image_10
        )
        self.plik_z_kluczem = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.plik_z_kluczem.place(
            x=119.0,
            y=180.0,
            width=157.0,
            height=19.0
        )

        self.canvas.create_text(
            26.0,
            181.0,
            anchor="nw",
            text="Plik z kluczem",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.entry_image_11 = PhotoImage(
            file=relative_to_assets("entry_11.png"))
        entry_bg_11 = self.canvas.create_image(
            340.5,
            121.5,
            image=self.entry_image_11
        )
        self. klucz_prywatny_W = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.  klucz_prywatny_W.place(
            x=264.0,
            y=113.0,
            width=155.0,
            height=19.0
        )

        self.canvas.create_text(
            233.0,
            114.0,
            anchor="nw",
            text="W",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self. generuj_klucze_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.generuj_klucze,
            relief="flat"
        )
        self.generuj_klucze_button.place(
            x=26.0,
            y=143.0,
            width=174.0,
            height=27.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.generuj_klucz_publiczny_button = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.generuj_klucz_publiczny,
            relief="flat"
        )
        self.generuj_klucz_publiczny_button.place(
            x=216.0,
            y=144.0,
            width=180.0,
            height=27.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.odczytaj_klucz_publiczny_button = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.odczytaj_klucz_publiczny,
            relief="flat"
        )
        self.odczytaj_klucz_publiczny_button.place(
            x=182.0,
            y=207.0,
            width=154.0,
            height=27.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.odczytaj_klucz_prywatny_button = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.odczytaj_klucz_prywatny,
            relief="flat"
        )
        self. odczytaj_klucz_prywatny_button.place(
            x=500.0,
            y=207.0,
            width=152.0,
            height=27.0
        )

        self. button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.   zapisz_klucz_prywatny_button = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.zapisz_klucz_prywatny,
            relief="flat"
        )
        self.  zapisz_klucz_prywatny_button.place(
            x=348.0,
            y=207.0,
            width=145.0,
            height=27.0
        )

        self. button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.   deszyfruj_button = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.deszyfruj,
            relief="flat"
        )
        self.  deszyfruj_button.place(
            x=281.0,
            y=418.0,
            width=68.0,
            height=27.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self. szyfruj_button = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.szyfruj,
            relief="flat"
        )
        self.szyfruj_button.place(
            x=289.0,
            y=366.0,
            width=52.0,
            height=27.0
        )

        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.zapisz_klucz_publiczny_button = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=self.zapisz_klucz_publiczny,
            relief="flat"
        )
        self. zapisz_klucz_publiczny_button.place(
            x=26.0,
            y=207.0,
            width=145.0,
            height=27.0
        )

        self.  plikRadio = tk.Radiobutton(
            borderwidth=0,
            highlightthickness=0,
            # command=deszyfruj,
            relief="flat",
            variable=self.v,
            value=0,
            text="plik",
            background="white"

        )
        self.plikRadio.place(
            x=281.0,
            y=285.0,
            width=68.0,
            height=27.0
        )

        self.tekstRadio = tk.Radiobutton(
            borderwidth=0,
            highlightthickness=0,
            # command=szyfruj,
            relief="flat",
            variable=self.v,
            value=1,
            text="tekst",
            background="white"
        )
        self.tekstRadio.place(
            x=289.0,
            y=320.0,
            width=52.0,
            height=27.0
        )

    def generuj_klucze(self):
        self.klucz_prywatny_M.delete("1.0", tk.END)
        self.klucz_prywatny_a.delete("1.0", tk.END)
        self.klucz_prywatny_W.delete("1.0", tk.END)
        self.klucz_publiczny.delete("1.0", tk.END)

        self.knapsack.generate_keys()
        self.klucz_prywatny_M.insert(tk.END,self.knapsack.m_string)
        self.klucz_prywatny_a.insert(tk.END,self.knapsack.a_string)
        self.klucz_prywatny_W.insert(tk.END,self.knapsack.w_string)
        self.klucz_publiczny.insert(tk.END,self.knapsack.a_prim_string)

    def generuj_klucz_publiczny(self):
        a = self.klucz_prywatny_a.get("1.0", tk.END)
        m = self.klucz_prywatny_M.get("1.0", tk.END)
        w = self.klucz_prywatny_W.get("1.0", tk.END)
        try:
            a_prime = algorithm.generate_public_key(a , m, w)
            self.klucz_publiczny.delete("1.0", tk.END)
            self.klucz_publiczny.insert(tk.END, a_prime)
        except Exception as e:
            self.display_error(str(e))
    def zapisz_klucz_publiczny(self):
        sciezka =  self.plik_z_kluczem.get("1.0", tk.END)
        sciezka = sciezka[:-1]
        tekst = self.klucz_publiczny.get("1.0", tk.END)
        tekst = tekst[:-1]
        with open(sciezka, 'w', encoding="utf-8") as file:
            file.write(tekst)

    def odczytaj_klucz_publiczny(self):
        sciezka =  self.plik_z_kluczem.get("1.0", tk.END)
        sciezka = sciezka[:-1]
        if not os.path.exists(sciezka):
            self.display_error("Nie można odnaleźć wskazanego pliku.")
        else:
            with open(sciezka, 'r', encoding="utf-8") as file:
                tekst = file.read()
        self.klucz_publiczny.delete("1.0", tk.END)
        self.klucz_publiczny.insert( tk.END, tekst)

    def zapisz_klucz_prywatny(self):
        sciezka =  self.plik_z_kluczem.get("1.0", tk.END)
        sciezka = sciezka[:-1]
        a = self.klucz_prywatny_a.get("1.0", tk.END)
        a = a[:-1]
        m = self.klucz_prywatny_M.get("1.0", tk.END)
        m = m[:-1]
        w = self.klucz_prywatny_W.get("1.0", tk.END)
        w = w[:-1]
        with open(sciezka, 'w', encoding="utf-8") as file:
            file.write(a+"\n")
            file.write(m+"\n")
            file.write(w)


    def odczytaj_klucz_prywatny(self):
        sciezka =  self.plik_z_kluczem.get("1.0", tk.END)
        sciezka = sciezka[:-1]
        if not os.path.exists(sciezka):
            self.display_error("Nie można odnaleźć wskazanego pliku.")
        else:
            with open(sciezka, 'r', encoding="utf-8") as file:
                tekst = file.readlines()
        self.klucz_prywatny_a.delete("1.0", tk.END)
        self.klucz_prywatny_a.insert( tk.END, tekst[0])
        self.klucz_prywatny_M.delete("1.0", tk.END)
        self.klucz_prywatny_M.insert( tk.END, tekst[1])
        self.klucz_prywatny_W.delete("1.0", tk.END)
        self.klucz_prywatny_W.insert( tk.END, tekst[2])

    def szyfruj(self):
        isText = self.v.get()

        if isText:
            try:
                tekst = self.tekst_jawny.get("1.0", tk.END)[:-1]
                szyfr = self.knapsack.encrypt(tekst, isText)

                self.kryptogram.delete("1.0", tk.END)
                self.kryptogram.insert(tk.END, szyfr)
            except Exception as e:
                self.display_error(str(e))
        else:
            try:
                odczyt =self.sciezka_odczytu_tekst_jawny.get("1.0", tk.END)[:-1]
                zapis = self.sciezka_zapisu_kryptogram.get("1.0", tk.END)[:-1]

                with open(odczyt, 'rb') as file:
                    file_content = file.read()
                szyfr = self.knapsack.encrypt(file_content, isText)
                with open(zapis, 'wb') as file:
                    file.write(szyfr)
            except Exception as e:
                self.display_error(str(e))

    def deszyfruj(self):
        isText = self.v.get()

        if isText:
            try:
                szyfr = self.kryptogram.get("1.0", tk.END)[:-1]
                tekst = self.knapsack.decrypt(szyfr, isText)

                self.tekst_jawny.delete("1.0", tk.END)
                self.tekst_jawny.insert(tk.END, tekst)
            except Exception as e:
                self.display_error(str(e))
        else:
            try:
                odczyt = self.sciezka_odczytu_kryptogram.get("1.0", tk.END)[:-1]
                zapis = self.sciezka_zapisu_tekst_jawny.get("1.0", tk.END)[:-1]

                with open(odczyt, 'rb') as file:
                    file_content = file.read()
                szyfr = self.knapsack.decrypt(file_content, isText)
                with open(zapis, 'wb') as file:
                    file.write(szyfr)
            except Exception as e:
                self.display_error(str(e))



    def display_error(self, error_message):
        error_window = tk.Toplevel()
        error_window.title("Błąd")
        tk.Label(error_window, text="Napotkano błąd:").pack(pady=(10, 0))
        tk.Label(error_window, text=error_message).pack(pady=(0, 10))
        tk.Button(error_window, text="OK", command=error_window.destroy).pack(pady=(0, 10))
        error_window_width = 420  # Domyślna szerokość okna
        error_window_height = 100  # Domyślna wysokość okna
        screen_width = error_window.winfo_screenwidth()
        screen_height = error_window.winfo_screenheight()
        x = (screen_width - error_window_width) // 2
        y = (screen_height - error_window_height) // 2
        error_window.geometry(f"{error_window_width}x{error_window_height}+{x}+{y}")
        error_window.focus()

window = Tk()
window.geometry("665x561")
window.configure(bg="#FFFFFF")
window.title("Knapsack")

app = App(window)

window.resizable(False, False)
window.mainloop()