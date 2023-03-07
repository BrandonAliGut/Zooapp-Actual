from kivy.uix.screenmanager import Screen

from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDIconButton
from kivymd.uix.swiper import MDSwiperItem
from kivy.properties import StringProperty,NumericProperty,ObjectProperty
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import MDGridLayout

from kivy.clock import Clock
Builder.load_file("./kv/kv_app_groups/listaAnimales.kv")

class Animal_Add(MDBoxLayout):
    selecespecie= StringProperty()
    especie= StringProperty()
    imagenSor = StringProperty()
    Imgdefaul = StringProperty()
    items_spacing= 2
    
    ids_CompraCateg =StringProperty()
    
        
class AddButtonAnimal(MDBoxLayout):
    pass     
class Regresar(MDIconButton):
    pass
class Colorbox(MDBoxLayout):
    pass