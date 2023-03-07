from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
#from kivymd.uix.behaviors import RectangularElevationBehavior

from kivymd.uix.behaviors import CommonElevationBehavior, RectangularRippleBehavior
from kivymd.uix.behaviors.focus_behavior import  FocusBehavior
#from kivymd.uix.behaviors.focus_behavior import FocusBehavior


from kivymd.uix.list import OneLineListItem
from kivy.properties import  StringProperty
from kivymd.uix.boxlayout import MDBoxLayout

class Listas(MDBoxLayout, RectangularRippleBehavior, FocusBehavior):
    n_campo = StringProperty()
    N_grupo = StringProperty()
    data = StringProperty()
    idList = StringProperty()
    ids_CompraCateg = StringProperty()

class DatosItAnimal(Screen):
    Titulo = StringProperty()
    ItemsGrupo = StringProperty()
    Imagen = StringProperty()

class DatosGenerales(MDCard):
    DataTipo = StringProperty()
    Enfermedad= StringProperty()
    selecesEnfermedad = StringProperty()

