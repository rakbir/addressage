from tkinter import Tk, Frame, Label, messagebox
from tkinter.tix import *
from tkinter.ttk import *
from classes.ipv4info import *
from classes.ipv6info import *
from ipaddress import AddressValueError, IPv4Network, IPv6Network

class MainMenu(Frame):
    def __init__(self, master=None):
        super().__init__(master)
       
        self.master=master
        self.master.title('Adressage')
        self.master.minsize(500,250)
        self.pack(expand=YES)
        self.configure()

    def configure(self):
            Label(self, text="ADRESSAGE IPv4 - IPv6", font=('Arial',20)).pack()

            self.champAdresse=LabelEntry(self)
            self.champAdresse.label['text']="adresse_ip/préfixe:"
            self.champAdresse.label['font']=('Helvetica',10)
            self.champAdresse.entry.setvar(name='ip')
            self.champAdresse.label['font']=('Helvetica',10)
            self.champAdresse.entry['width']=40
            self.champAdresse.entry['borderwidth']=2
            self.champAdresse.pack()

            self.choix=IntVar()
            self.choix.set('1')
            modes=[
                ("IPv4",1),
                ("IPv6",2)
            ]
            for text, value in modes:
                Radiobutton(self, text=text, variable =self.choix, value=value).pack()

            Button(self, text="valider",font=("Helvetica", 10), width=7,borderwidth=3, command=self.affichageResultat).pack()
            

    def affichageResultat(self):
        adresse=self.champAdresse.entry.get()
        try:
            if self.choix.get()==1:
                network={'address':adresse,'network':IPv4Network(adresse, False)}
                root=Tk()
                frame=Ipv4AddressInfo(network,root)
            else:
                network={'address':adresse,'network':IPv6Network(adresse, False)}
                root=Tk()
                frame=Ipv6AddressInfo(network,root)
        except AddressValueError:
            messagebox.showwarning("erreur", "veuillez-entrer une adresse valide")
        finally:
            self.champAdresse.entry.delete(0,adresse.__len__())