from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder
from kivymd.uix.swiper import MDSwiper
from kivy.clock import Clock
from kivy.properties import StringProperty, DictProperty
from Sub_Aplicaciones.Tienda_App.varCategoria import *
from kivy.core.window import WindowBase


        

class Home_Store(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.screenHome=[
            Button_C(),
            Informacion(),
        ]
        self.selec_button= Button_C()
        self.infor = Informacion()
        Clock.schedule_once(self.F_activacion)
    def F_activacion(self, *args) -> None:
        self.list_butons_categoria()
        
    def list_butons_categoria(self):
        for scr in self.screenHome: self.add_widget(scr)
        

class Store(Screen):
    def __init__(self, **kwargs):
        super(Store, self).__init__()
        self.home_store = Home_Store()
        Clock.schedule_once(self.home)
        
    def home(self, *args, **kwargs):
        
        self.ids['store_pos'].add_widget(self.home_store)
        
        
        
        
        
    
    
    