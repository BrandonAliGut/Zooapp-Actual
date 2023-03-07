from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from typing import Union
from colorpicker.colorpicker import MDColorPicker

from conex.Save_json import str_json



class Config_color_personal(Screen):
    text_color = [1,1,1,1]
    
    def __init__(self):
        super().__init__()
        self.type_object = str()
        
    
    
    def open_color_picker(self, object_a="menu"):
            color_picker = MDColorPicker(size_hint=(0.45, 0.85))
            color_picker.open()
            if object_a == "menu":
                self.type_object = "menu"
            elif object_a == "Swipe":
                self.type_object = "Swipe"
            elif object_a == "text_color":
                self.type_object = "text_color"
            color_picker.bind(
                on_select_color=self.on_select_color,
                on_release=self.get_selected_color,
            )

    def menu_update(self, color: list) -> None:
        self.ids.toolbar.md_bg_color = color
        value_data= {"type":"toolbar", "md_bg_color":color }
        str_json("toolbar",value_data)
        
    def Swipe(self, color: list) -> None:
        self.ids.box_swipe.md_bg_color = color
        value_data= {"type":"box_swipe", "md_bg_color":color }
        str_json("box_swipe",value_data)
        
    def text_color_rgb(self, color: list) -> None:
        self.text_color = color
        value_data= {"type":"md_label_text", "md_bg_color":color }
        str_json("text_color",value_data)

    def get_selected_color(
        self,
        instance_color_picker: MDColorPicker,
        type_color: str,
        selected_color: Union[list, str],
    ):
        if self.type_object=="menu":
            self.menu_update(selected_color)# type: ignore
        elif self.type_object=="Swipe":
            self.Swipe(selected_color)# type: ignore
        elif self.type_object=="text_color":
            self.text_color_rgb((selected_color[:-1] + [1]))# type: ignore

    def on_select_color(self, instance_gradient_tab, color: list) -> None:
        '''Called when a gradient image is clicked.'''
 
