from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
Builder.load_string("""
<Caja_color_box>:
    size_hint_y: None
    height: dp(10)
    orientation:"horizontal"
    padding:[1,]
    spacing: dp(2)
    Colorbox:
        id: colorbox
        colors_id: 0,0,0,0
        colors: self.colors_id
    MDLabel:
        size_hint_y:None
        height: dp(5)
        id: preciobox
        halign: "right"
        text: "" 
        theme_text_color: "Custom"
        text_color: 1,1,1,1
""")
class Colorbox(MDBoxLayout):
    pass
class Caja_color_box(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        """if Items['Id_Categoria']!= None:
            for type in DATOS_URL_PATH_TYPE:
                if Items['Id_Categoria'] == type["id"]:
                    self.caja_color.ids.colorbox.colors = eval(type["Codigo_color"])
                    self.caja_color.ids.preciobox.text = str(type["Precio"]) + " $"
                    self.ButtonCard_items.add_widget(self.caja_color)"""