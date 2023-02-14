from tkinter import Tk, Frame, Label, messagebox
from tkinter.tix import *
from tkinter.ttk import *
from classes.ipv4info import *
from classes.ipv6info import *
from ipaddress import AddressValueError, NetmaskValueError, IPv4Network, IPv6Network

class MainMenu(Frame):
    def __init__(self, master=None):
        super().__init__(master)
       
        self.master.title('IP Info')
        self.master.minsize(500,250)
        self.pack(expand=YES)
        self.configure()

    def configure(self):
            Label(self, text="Calcul adresses IP", font=('Arial',20)).pack()

            self.champAdresse=LabelEntry(self)
            self.champAdresse.label['text']="adresse_ip/préfixe:"
            self.champAdresse.label['font']=('Helvetica',10)
            self.champAdresse.entry['width']=40
            self.champAdresse.entry['borderwidth']=2
            self.champAdresse.pack()

            self.choixVersion=IntVar()
            self.choixVersion.set('1')
            versions=[
                ("IPv4",1),
                ("IPv6",2)
            ]
            for text, value in versions:
                Radiobutton(self, text=text, variable =self.choixVersion, value=value).pack()

            Button(self, text="valider",font=("Helvetica", 10), width=7,borderwidth=3, command=self.affichageResultat).pack()
            

    def affichageResultat(self):
        adresse=self.champAdresse.entry.get()
        try:
            network={'address':adresse}
            if self.choixVersion.get()==1: 
                network['network']=IPv4Network(adresse, False)
                Ipv4AddressInfo(network,Tk())
            else:
                network['network']=IPv6Network(adresse, False)
                Ipv6AddressInfo(network,Tk())
            self.champAdresse.entry.delete(0,adresse.__len__())
        except AddressValueError:
            messagebox.showwarning("Adresse invalide", "veuillez-entrer une adresse valide")
        except NetmaskValueError:
             messagebox.showwarning("Masque invalide", "Le masque de sous-réseau est invalide")
            
