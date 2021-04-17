from tkinter import Frame,Label
from tkinter.tix import *

class Ipv6AddressInfo(Frame):
    def __init__(self,address,master=None):
        super().__init__(master)
        self.master=master
        self.getAddressInfo(address)
        self.master.title(address['address'])
        self.master.minsize(700,350)
        self.pack(expand=YES)
        self.show()
    
    def getAddressInfo(self, adresse):
        self.adresse=adresse['address']
        self.network=adresse['network']
        self.nb=self.network.num_addresses

    def show(self):
        self.adresse=Label(self, text=self.adresse, font=('Helvetica',20))
        self.adresse.pack()
        self.abreviation=Label(self, text="Abréviation: {}".format(self.network.compressed), font=('Helvetica', 15))
        self.abreviation.pack()
        self.masque=Label(self, text="Masque : {}".format(self.network.netmask), font=('Helvetica', 15))
        self.masque.pack()
        self.networkAddress=Label(self, text="Adresse réseau : {}".format(self.network.network_address), font=('Helvetica', 15))
        self.networkAddress.pack()
        self.broadcast=Label(self, text="Adresse de diffusion : {}".format(self.network.broadcast_address), font=('Helvetica', 15))
        self.broadcast.pack()
        self.dispos=Label(self, text="Adresses disponibles : {}".format(self.nb-2), font=('Helvetica', 15))
        self.dispos.pack()
        self.first=Label(self, text="1ère adresse : {}".format(self.network.__getitem__ (1)), font=('Helvetica', 15))
        self.first.pack()
        self.last=Label(self, text="dernière adresse: {}".format(self.network.__getitem__ (self.nb-2)), font=('Helvetica', 15))
        self.last.pack()