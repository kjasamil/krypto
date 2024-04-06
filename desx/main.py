import algorithm as des
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("DESX")
        #setting window size
        width=763
        height=625
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_816=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_816["font"] = ft
        GLabel_816["fg"] = "#333333"
        GLabel_816["justify"] = "center"
        GLabel_816["text"] = "Wartość klucza 1"
        GLabel_816.place(x=0,y=10,width=113,height=32)

        GLabel_804=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Wartość klucza 2"
        GLabel_804.place(x=270,y=20,width=119,height=30)

        GLabel_184=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_184["font"] = ft
        GLabel_184["fg"] = "#333333"
        GLabel_184["justify"] = "center"
        GLabel_184["text"] = "Wartość klucza 3"
        GLabel_184.place(x=490,y=20,width=135,height=30)

        self.Klucz1Entry=tk.Entry(root)
        self.Klucz1Entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.Klucz1Entry["font"] = ft
        self.Klucz1Entry["fg"] = "#333333"
        self.Klucz1Entry["justify"] = "center"
        self.Klucz1Entry["text"] = "Klucz_1_text"
        self.Klucz1Entry.place(x=10,y=50,width=240,height=30)

        self.Klucz2Entry=tk.Entry(root)
        self.Klucz2Entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.Klucz2Entry["font"] = ft
        self.Klucz2Entry["fg"] = "#333333"
        self.Klucz2Entry["justify"] = "center"
        self.Klucz2Entry["text"] = "Klucz_2_text"
        self.Klucz2Entry.place(x=270,y=50,width=225,height=30)

        self.Klucz3Entry=tk.Entry(root)
        self.Klucz3Entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.Klucz3Entry["font"] = ft
        self.Klucz3Entry["fg"] = "#333333"
        self.Klucz3Entry["justify"] = "center"
        self.Klucz3Entry["text"] = "Klucz_3_text"
        self.Klucz3Entry.place(x=510,y=50,width=237,height=30)

        self.GenerukKluczButton=tk.Button(root)
        self.GenerukKluczButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.GenerukKluczButton["font"] = ft
        self.GenerukKluczButton["fg"] = "#000000"
        self.GenerukKluczButton["justify"] = "center"
        self.GenerukKluczButton["text"] = "Generuj klucze"
        self.GenerukKluczButton.place(x=10,y=90,width=184,height=30)
        self.GenerukKluczButton["command"] = self.GenerukKluczButton_Fun

        self.ZapiszKluczButton=tk.Button(root)
        self.ZapiszKluczButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.ZapiszKluczButton["font"] = ft
        self.ZapiszKluczButton["fg"] = "#000000"
        self.ZapiszKluczButton["justify"] = "center"
        self.ZapiszKluczButton["text"] = "Zapisz klucze"
        self.ZapiszKluczButton.place(x=430,y=180,width=118,height=30)
        self.ZapiszKluczButton["command"] = self.ZapiszKluczButton_fun

        self.WczytajKluczButton=tk.Button(root)
        self.WczytajKluczButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.WczytajKluczButton["font"] = ft
        self.WczytajKluczButton["fg"] = "#000000"
        self.WczytajKluczButton["justify"] = "center"
        self.WczytajKluczButton["text"] = "Wczytaj klucze"
        self.WczytajKluczButton.place(x=430,y=130,width=117,height=30)
        self.WczytajKluczButton["command"] = self.WczytajKluczButton_fun

        self.SciezkaWczytanieKlucza=tk.Entry(root)
        self.SciezkaWczytanieKlucza["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.SciezkaWczytanieKlucza["font"] = ft
        self.SciezkaWczytanieKlucza["fg"] = "#333333"
        self.SciezkaWczytanieKlucza["justify"] = "center"
        self.SciezkaWczytanieKlucza["text"] = "Ścieżka pliku do wczytania klucza"
        self.SciezkaWczytanieKlucza.place(x=170,y=130,width=219,height=30)

        self.SciezkaZapisuKlucza=tk.Entry(root)
        self.SciezkaZapisuKlucza["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.SciezkaZapisuKlucza["font"] = ft
        self.SciezkaZapisuKlucza["fg"] = "#333333"
        self.SciezkaZapisuKlucza["justify"] = "center"
        self.SciezkaZapisuKlucza["text"] = "Ścieżka pliku do zapisu klucza"
        self.SciezkaZapisuKlucza.place(x=170,y=180,width=221,height=30)

        GLabel_551=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_551["font"] = ft
        GLabel_551["fg"] = "#333333"
        GLabel_551["justify"] = "center"
        GLabel_551["text"] = "Wczytaj klucze z pliku"
        GLabel_551.place(x=0,y=130,width=166,height=30)

        GLabel_114=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_114["font"] = ft
        GLabel_114["fg"] = "#333333"
        GLabel_114["justify"] = "center"
        GLabel_114["text"] = "Zapisz klucze do pliku"
        GLabel_114.place(x=0,y=170,width=155,height=30)



        self.szyfrujButton=tk.Button(root)
        self.szyfrujButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.szyfrujButton["font"] = ft
        self.szyfrujButton["fg"] = "#000000"
        self.szyfrujButton["justify"] = "center"
        self.szyfrujButton["text"] = "Szyfruj"
        self.szyfrujButton.place(x=350,y=400,width=70,height=25)
        self.szyfrujButton["command"] = self.szyfrujButton_fun

        self.DeszyfrujButton=tk.Button(root)
        self.DeszyfrujButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.DeszyfrujButton["font"] = ft
        self.DeszyfrujButton["fg"] = "#000000"
        self.DeszyfrujButton["justify"] = "center"
        self.DeszyfrujButton["text"] = "Deszyfruj"
        self.DeszyfrujButton.place(x=350,y=450,width=70,height=25)
        self.DeszyfrujButton["command"] = self.DeszyfrujButton_fun

        GLabel_279=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_279["font"] = ft
        GLabel_279["fg"] = "#333333"
        GLabel_279["justify"] = "center"
        GLabel_279["text"] = "Otworz plik z tekstem jawnym"
        GLabel_279.place(x=0,y=240,width=180,height=30)

        self.SciezkaPlikuTekstuJawnego=tk.Entry(root)
        self.SciezkaPlikuTekstuJawnego["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.SciezkaPlikuTekstuJawnego["font"] = ft
        self.SciezkaPlikuTekstuJawnego["fg"] = "#333333"
        self.SciezkaPlikuTekstuJawnego["justify"] = "center"
        self.SciezkaPlikuTekstuJawnego["text"] = "Ścieżka pliku z tekstem jawnym"
        self.SciezkaPlikuTekstuJawnego.place(x=10,y=270,width=214,height=30)

        GLabel_288=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_288["font"] = ft
        GLabel_288["fg"] = "#333333"
        GLabel_288["justify"] = "center"
        GLabel_288["text"] = "Otworz plik z szyfrogramem"
        GLabel_288.place(x=380,y=240,width=192,height=30)

        self.SciezkaPlikuSzyfrogramu=tk.Entry(root)
        self.SciezkaPlikuSzyfrogramu["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.SciezkaPlikuSzyfrogramu["font"] = ft
        self.SciezkaPlikuSzyfrogramu["fg"] = "#333333"
        self.SciezkaPlikuSzyfrogramu["justify"] = "center"
        self.SciezkaPlikuSzyfrogramu["text"] = "Ścieżka pliku z szyfogramem"
        self.SciezkaPlikuSzyfrogramu.place(x=390,y=270,width=220,height=30)

        self.ZapiszTekstJawnyButton=tk.Button(root)
        self.ZapiszTekstJawnyButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.ZapiszTekstJawnyButton["font"] = ft
        self.ZapiszTekstJawnyButton["fg"] = "#000000"
        self.ZapiszTekstJawnyButton["justify"] = "center"
        self.ZapiszTekstJawnyButton["text"] = "Zapisz tekst jawny"
        self.ZapiszTekstJawnyButton.place(x=240,y=550,width=114,height=30)
        self.ZapiszTekstJawnyButton["command"] = self.ZapiszTekstJawnyButton_FUn

        self.ZapiszSzyfrogramButton=tk.Button(root)
        self.ZapiszSzyfrogramButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.ZapiszSzyfrogramButton["font"] = ft
        self.ZapiszSzyfrogramButton["fg"] = "#000000"
        self.ZapiszSzyfrogramButton["justify"] = "center"
        self.ZapiszSzyfrogramButton["text"] = "Zapisz szyfrogram"
        self.ZapiszSzyfrogramButton.place(x=620,y=550,width=128,height=30)
        self.ZapiszSzyfrogramButton["command"] = self.ZapiszSzyfrogramButton_fun

        self.SciezkaPlikuTekstuJawnegoDoZapisu=tk.Entry(root)
        self.SciezkaPlikuTekstuJawnegoDoZapisu["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.SciezkaPlikuTekstuJawnegoDoZapisu["font"] = ft
        self.SciezkaPlikuTekstuJawnegoDoZapisu["fg"] = "#333333"
        self.SciezkaPlikuTekstuJawnegoDoZapisu["justify"] = "center"
        self.SciezkaPlikuTekstuJawnegoDoZapisu["text"] = "Ścieżka pliku do zapisu tekstu jawnego"
        self.SciezkaPlikuTekstuJawnegoDoZapisu.place(x=10,y=550,width=222,height=30)

        self.SceizkaPlikuSzyfrogramuDOZapisu=tk.Entry(root)
        self.SceizkaPlikuSzyfrogramuDOZapisu["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.SceizkaPlikuSzyfrogramuDOZapisu["font"] = ft
        self.SceizkaPlikuSzyfrogramuDOZapisu["fg"] = "#333333"
        self.SceizkaPlikuSzyfrogramuDOZapisu["justify"] = "center"
        self.SceizkaPlikuSzyfrogramuDOZapisu["text"] = "Ścieżka pliku do zapisu szyfrogramu"
        self.SceizkaPlikuSzyfrogramuDOZapisu.place(x=400,y=550,width=205,height=30)

        GLabel_932=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_932["font"] = ft
        GLabel_932["fg"] = "#333333"
        GLabel_932["justify"] = "center"
        GLabel_932["text"] = "Zapisz do pliku tekst jawny"
        GLabel_932.place(x=0,y=520,width=170,height=30)

        GLabel_972=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_972["font"] = ft
        GLabel_972["fg"] = "#333333"
        GLabel_972["justify"] = "center"
        GLabel_972["text"] = "Zapisz do pliku szyfrogram"
        GLabel_972.place(x=380,y=520,width=181,height=30)

        self.WczytajTekstjawnyButton=tk.Button(root)
        self.WczytajTekstjawnyButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.WczytajTekstjawnyButton["font"] = ft
        self.WczytajTekstjawnyButton["fg"] = "#000000"
        self.WczytajTekstjawnyButton["justify"] = "center"
        self.WczytajTekstjawnyButton["text"] = "Wczytaj tekst jawny"
        self.WczytajTekstjawnyButton.place(x=240,y=270,width=123,height=30)
        self.WczytajTekstjawnyButton["command"] = self.WczytajTekstjawnyButton_Fun

        self.WczytajSzyfrogramButton=tk.Button(root)
        self.WczytajSzyfrogramButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.WczytajSzyfrogramButton["font"] = ft
        self.WczytajSzyfrogramButton["fg"] = "#000000"
        self.WczytajSzyfrogramButton["justify"] = "center"
        self.WczytajSzyfrogramButton["text"] = "Wczytaj szyfrogram"
        self.WczytajSzyfrogramButton.place(x=620,y=270,width=123,height=30)
        self.WczytajSzyfrogramButton["command"] = self.WczytajSzyfrogramButton_Fun

        self.TekstJawny=tk.Text(root)
        self.TekstJawny["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.TekstJawny["font"] = ft
        self.TekstJawny["fg"] = "#333333"
        self.TekstJawny["relief"] = "sunken"
        self.TekstJawny.place(x=10,y=310,width=301,height=215)

        self.Szyfrogram=tk.Text(root)
        self.Szyfrogram["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.Szyfrogram["font"] = ft
        self.Szyfrogram["fg"] = "#333333"
        self.Szyfrogram["relief"] = "flat"
        self.Szyfrogram.place(x=460,y=310,width=281,height=213)

    def GenerukKluczButton_Fun(self):
        klucze = des.generate_keys()

        self.Klucz1Entry.delete(0, tk.END)
        self.Klucz2Entry.delete(0, tk.END)
        self.Klucz3Entry.delete(0, tk.END)

        self.Klucz1Entry.insert(tk.END, klucze[0])
        self.Klucz2Entry.insert(tk.END, klucze[1])
        self.Klucz3Entry.insert(tk.END, klucze[2])


    def ZapiszKluczButton_fun(self):
        sciezka =  self.SciezkaZapisuKlucza.get()
        klucz1 = self.Klucz1Entry.get()
        klucz2 = self.Klucz2Entry.get()
        klucz3 = self.Klucz3Entry.get()
        klucze = [klucz1+"\n",klucz2+"\n",klucz3]
        with open(sciezka, 'w') as file:
            file.writelines(klucze)




    def WczytajKluczButton_fun(self):
        sciezka =  self.SciezkaWczytanieKlucza.get()

        with open(sciezka, 'r') as file:
            lines = file.readlines()

        self.Klucz1Entry.delete(0, tk.END)
        self.Klucz2Entry.delete(0, tk.END)
        self.Klucz3Entry.delete(0, tk.END)

        self.Klucz1Entry.insert(tk.END, lines[0][:-1])
        self.Klucz2Entry.insert(tk.END, lines[1][:-1])
        self.Klucz3Entry.insert(tk.END, lines[2])



    def szyfrujButton_fun(self):
        try:
            klucz1 = self.Klucz1Entry.get()
            klucz2 = self.Klucz2Entry.get()
            klucz3 = self.Klucz3Entry.get()
            tekst = self.TekstJawny.get("1.0", tk.END)
            tekst = tekst[:-1]
            tekst = des.encrypt(tekst, klucz1, klucz2, klucz3)
            self.Szyfrogram.delete("1.0", tk.END)
            self.Szyfrogram.insert(tk.END, tekst)
        except Exception as e:
            # If an exception occurred, display it in a new window
            self.display_error(str(e))

    def DeszyfrujButton_fun(self):
        try:
            klucz1 = self.Klucz1Entry.get()
            klucz2 = self.Klucz2Entry.get()
            klucz3 = self.Klucz3Entry.get()
            tekst = self.Szyfrogram.get("1.0", tk.END)
            tekst = tekst[:-1]  # Remove the last newline character
            tekst = des.decrypt(tekst, klucz1, klucz2, klucz3)  # Assuming des.decrypt might raise an exception
            self.TekstJawny.delete("1.0", tk.END)
            self.TekstJawny.insert(tk.END, tekst)
        except Exception as e:
            # If an exception occurred, display it in a new window
            self.display_error(str(e))

    def ZapiszTekstJawnyButton_FUn(self):
        sciezka =  self.SciezkaPlikuTekstuJawnegoDoZapisu.get()
        tekst = self.TekstJawny.get("1.0", tk.END)
        tekst = tekst[:-1]
        with open(sciezka, 'w') as file:
            file.write(tekst)

    def ZapiszSzyfrogramButton_fun(self):
        sciezka =  self.SceizkaPlikuSzyfrogramuDOZapisu.get()
        tekst = self.Szyfrogram.get("1.0", tk.END)
        tekst = tekst[:-1]
        with open(sciezka, 'w') as file:
            file.write(tekst)

    def WczytajTekstjawnyButton_Fun(self):
        sciezka =  self.SciezkaPlikuTekstuJawnego.get()
        with open(sciezka, 'r') as file:
            tekst =  file.read()
        self.TekstJawny.delete("1.0", tk.END)
        self.TekstJawny.insert( tk.END, tekst)

    def WczytajSzyfrogramButton_Fun(self):
        sciezka =  self.SciezkaPlikuSzyfrogramu.get()
        with open(sciezka, 'r') as file:
            tekst =  file.read()
        self.Szyfrogram.delete("1.0", tk.END)
        self.Szyfrogram.insert( tk.END, tekst)

    def display_error(self, error_message):
        # This function creates a new window to display the error message
        error_window = tk.Toplevel()  # Create a new top-level window
        error_window.title("Error")
        tk.Label(error_window, text="An error occurred:").pack(pady=(10, 0))
        tk.Label(error_window, text=error_message).pack(pady=(0, 10))
        tk.Button(error_window, text="OK", command=error_window.destroy).pack(pady=(0, 10))
        error_window.focus()

root = tk.Tk()
app = App(root)
root.mainloop()
