from kivy.core.window import Window

from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.label import (MDLabel)
from kivy.properties import StringProperty
from Conjunto.appcontrol import url_patterns


class ButtonCard(MDCard):
    imagen = StringProperty()
    nombre = StringProperty()
    opcion = StringProperty()
    Id_select = StringProperty()
    type_color = StringProperty()
    
    def __init__(self):
        super(ButtonCard, self).__init__()
        
    def select_data(self,Opc=""):
        return Opc

class Error(MDLabel):
    pass

    
        
    
