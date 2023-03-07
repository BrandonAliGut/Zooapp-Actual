import numbers
from tokenize import Number
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.properties import StringProperty, DictProperty
from kivymd.uix.textfield import MDTextField
import base64

Builder.load_file('./kv/Add_grupos.kv')

    
class Add_Grupo(Screen):
    id_grupo = StringProperty()
    def __init__(self):
        super(Add_Grupo, self).__init__()
        self.manager_open = False
        self.Message_error = None
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        
        )
        
        
        
        
    def BuscarImagenMemoria(self):
        self.file_manager.show('C:/Users/admin/Pictures/Imagenes de desarrollo')
        
        self.manager_open = True
    def select_path(self, path):
        self.exit_manager()
        self.ids["ImagenBuscada"].text = path
        self.ids["ImagenObtenida"].source = path
        toast(path)
    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
    def Guardar_datos(self, id_grupo):
        if id_grupo == "":
            if len(self.ids["ImagenBuscada"].text) == 0 or len(self.ids["Nombre_Grupo"].text) == 0:
                if len(self.ids["ImagenBuscada"].text) == 0 and len(self.ids["Nombre_Grupo"].text) == 0:
                    self.MenssageGlobal("Rellene Todos Los Campos")
                elif len(self.ids["ImagenBuscada"].text) == 0: 
                    self.MenssageGlobal("Rellene El Campo imagen ")
                elif len(self.ids["Nombre_Grupo"].text) == 0:
                    self.MenssageGlobal("Debe Rellenar El Campo Grupo")
                
            elif len(self.ids["ImagenBuscada"].text) > 0 or len(self.ids["Nombre_Grupo"].text) > 0:
            
                with  open(str(self.ids["ImagenBuscada"].text), 'rb') as f:
                    image = f.read()
                    encode_byte = base64.b64encode(image)
                    encode_string = encode_byte.decode('utf-8')                                     #variable especial para la el envio de datos
                    image_read = image
                    image_64_encode = base64.b85encode(image_read)
                    image_64_decode = base64.b85encode(image_64_encode) 
                    image_result = open("source/"+ self.ids["Nombre_Grupo"].text +".png" , 'wb')    # create a writable image and write the decoding result
                    image_result.write(image_64_decode)
                    
                    print(image_64_encode)
                    print(image_result)
                    
                    
                self.MenssageGlobal("NUEVO GRUPO CREADO...")
                self.ids["ImagenBuscada"].text = ""
                self.ids["Nombre_Grupo"].text = ""
                self.ids["ImagenObtenida"].source ="./Datos/Imagenes/add_img.png"
                
                
        elif id_grupo != "":
            self.MenssageGlobal("GRUPO ACTUALIZADO...")
            self.ids["ImagenBuscada"].text = ""
            self.ids["Nombre_Grupo"].text = ""
            self.ids["ImagenObtenida"].source ="./Datos/Imagenes/add_img.png"
                
                
            
        
    def MenssageGlobal(self,error):
        self.Message_error  = MDLabel(
                pos_hint={'center_x':.5, 'center_y':.1 },
                size_hint=(1,.1),
                md_bg_color = (0,0,0,.5),
                radius = (20),
                halign= "center",
                text= "{}".format(error),
            )
        self.add_widget(self.Message_error)
        Clock.schedule_once(lambda dt: self.remove_widget(self.Message_error), 1)
    
