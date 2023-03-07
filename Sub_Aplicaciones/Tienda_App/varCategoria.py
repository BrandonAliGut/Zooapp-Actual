from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder


from kivymd.uix.swiper import MDSwiper
from kivy.clock import Clock
from kivy.properties import StringProperty, DictProperty




Builder.load_file("./Sub_Aplicaciones/Tienda_App/T_Categoria.kv")
Builder.load_file("./Sub_Aplicaciones/Tienda_App/Categoria/Informacion.kv")


   
class Categoria_store(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Categoria_Card_Button(MDCard):
    Color_line = []
    Precio  = StringProperty()
    

class Button_C(MDCard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.C_button)
        
    def C_button(self, *args) -> None:
        for i in range(20):
            self.Button = Categoria_Card_Button()
            self.Button.Color_line = [1,0,0,1]
            self.Button.Precio = str(i)
            self.ids["scroll_view_C"].add_widget(self.Button)
            
            

# informacion ___clase especial 
class Informacion(MDCard):
  
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.start_init_self)
    def start_init_self(self, *args):
        pass
        
        