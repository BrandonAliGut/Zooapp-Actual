from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard




class MDCardScreen(Screen):
    pass
class ImagenField(MDCard):
    Img = StringProperty()
class MDIMACAR(MDCard):
  
    pass
class PaginaCard(MDCard):
    envesado = StringProperty()
    informacion = StringProperty()
    source= StringProperty()
    padre = StringProperty()
    def __init__(self):
        super(PaginaCard, self).__init__()
        
        
