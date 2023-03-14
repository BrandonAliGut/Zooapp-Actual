from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from base.home import Home
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from base.home  import Configuracion
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from kivy.core.audio import SoundLoader
from Sub_Aplicaciones.ListaAnimal.Lista_Animal import Animal_Add
from Sub_Aplicaciones.Grupos_de_Animales.Grupos import *
from Sub_Aplicaciones.MenuButton.Menuapps import (
                                                    ButtonCard,
                                                    Error
                                                    )
from Conjunto.appcontrol import url_patterns

Builder.load_file("main.kv")
Builder.load_file("./kv/Configuracionapp_kv/configuracion.kv")
Builder.load_file("./kv/Configuracionapp_kv/Tienda_de_temas.kv")
Builder.load_file("./kv/kv_app_groups/grupos.kv")
Builder.load_file("./kv/kv_app_groups/Submenuapp.kv")

from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout


class WindowManager(ScreenManager):
    pass
#Grupos Add all

class Grupos(Screen):
    pass
class Lista_de_animales(Screen):
    pass
class ScreensMenu(Screen):
    def __init__(self,**kv):
        super(ScreensMenu,self).__init__(**kv)
        
    
        
    def comprobar(self):
        if Window.size <= (400,400):
            return 2
        elif Window.size <= (700,700):
            return 3
        elif Window.size >= (700,700) and Window.size <= (800,800):
            return 4
        elif Window.size >= (800,800):
            return 5
    def remove(self, numero = int):
        return numero
    def TextoInformacion(self):
        return 0

class add_callbacks:
    wm = ObjectProperty()
    def __init__(self,**kv):
        super(add_callbacks, self).__init__(**kv)
        self.Perfiles_id = []
        self.source_apk = "Source_apk"
        Clock.schedule_once(lambda dt: self.ItemsDatos("ListEspecie",[]) ,2)
        
    def ItemsDatos(self, Opcion = "", selectData = "", Imagen =None,__datos = None, Datos5 = None, color = "None", *args, **kwargs):
        """
        
        Cada uno delos selectores abren y manipulan cada entrada de datos
        
        
        print("________________________________")
        print(Opcion)
        print(selectData)
        print(Imagen)
        print(__datos)
        print(Datos5)
        print(color)
        print("_________________________________")
        """
        
        if Opcion != "Group":
            print("si")
            Clock.schedule_once(lambda dt: self.click.play(),0.1)
        Clock.schedule_once(lambda dt: self.click.play(),0.1)
        
        
        
        
            
        
         
        self.Opciones = Opcion 
        self.Perfil = url_patterns("Perfil","GET")
        for n in self.Perfil:# type: ignore
            self.Perfiles_id.append(n['ID_DECOMPRA'])
        if self.Opciones=="Group":
            """
            manipula la entrada de datos, con la llamada de la base de datos
            """

            self.grupos( Opcion, selectData, Imagen,__datos, Datos5, color)
               
        elif self.Opciones =="ListEspecie":
            
            Clock.schedule_once(lambda dt: self.Lista_de_Especie(Opcion, selectData, Imagen,__datos, Datos5, color), .5)
            
               
        elif self.Opciones == "MenuIntems":
            
            if Datos5 == "None":
                
                self.Menu_Items(Opcion, selectData, Imagen,__datos, Datos5, color)
            else: 
                if self.returnTrueFalse(Datos5) == True:
                    self.Menu_Items(Opcion, selectData, Imagen,__datos, Datos5, color)
                else:
                    self.cuadro_dialog
                    

        if self.Opciones =="A":#Redirge al screen Final
            
            if color == "None":
                self.Sub_Lista_Menu(option=Opcion,dato1= selectData,dato2=Imagen,dato3= __datos,dato4=Datos5,dato5=color)
            else:
                if self.returnTrueFalse(color) == True:
                    self.Sub_Lista_Menu(option=Opcion,dato1= selectData,dato2=Imagen,dato3= __datos,dato4=Datos5,dato5=color)
                else:
                    self.cuadro_dialog()
                
        elif self.Opciones =="B":#Redirige a la screen Informacion Final
            self.Url_Items("Informacion_final","GET", selectData, Imagen,Opcion, Datos5 )
            self.wn.screens[1].ids["screen_manager"].current = "FCurasyotros"

        elif self.Opciones =="Informacion":#Redirge a screen Lista
                self.busqueda=True
                
                
                if __datos == "None":
                    self.Url_Items("Informacion_final","GET", selectData, Imagen,__datos,Imagen)
                    self.wn.screens[1].ids["screen_manager"].current = "FCurasyotros"
                
                elif self.returnTrueFalse(__datos) == True:
                    self.Url_Items("Informacion_final","GET", selectData, Imagen,__datos,Imagen)
                    self.wn.screens[1].ids["screen_manager"].current = "FCurasyotros"
                elif len(selectData) == 18:
                    
                    self.Berificacion_de_usuario(selectData)
                else:
                 
                    self.cuadro_dialog() 
    def grupos(self,a, b, c,d, e, f):#     grupo             !
        self.MarcadorPositional("Gruposn")
        
        self.busqueda = False
        DATOS_URL_PATH =url_patterns("Group","GET")
        for datos in DATOS_URL_PATH:# type: ignore
            if datos['activo']== True:
                self.Unidad = Lista()
                self.Unidad.properti = str(datos['idGrup'])
                self.Unidad.encavesado = datos['grupo']
                self.Unidad.direccionImagen = self.source_apk+ datos['foto']
                self.wm.screens[0].ids['ImagenAnimals'].add_widget(self.Unidad) 
    def Lista_de_Especie(self,a, b, c,d, e, f):#   lista     !
        self.busqueda=False
        
        self.MarcadorPositional("lista_animal")
        DATOS_URL_PATH = url_patterns("selec_animal_grupo","GET")
        Grupo_path = url_patterns("Group","GET")
        def list():
            
            if compenteDa['activo']== True:
                self.swidgetChildren= Animal_Add()
                self.swidgetChildren.selecespecie = str(compenteDa['idAnimalList'])# selector base
                self.swidgetChildren.especie = compenteDa['AnimalList']
                self.swidgetChildren.ids_CompraCateg = str(compenteDa['Id_Categoria'])
                self.swidgetChildren.imagenSor = self.source_apk+compenteDa['foto']
                self.wm.screens[0].ids['gridlayo'].add_widget(self.swidgetChildren)
                
                self.configo_nivel_categoria(compenteDa,self.swidgetChildren ) 
        
        self.Swipe_update()
        print(b)
        for compenteDa in DATOS_URL_PATH:# type: ignore
            if b == str(compenteDa['PGRUPO']):
                list()
            if b== []:
                id=Grupo_path[0]["idGrup"]
                if str(id)== str(compenteDa['PGRUPO']):
                
                    list()
                
            
            
                
                
                        
                            
        #Llamado anticipado para la pantalla de Lista de Animales
        self.wm.screens[0].ids["screen_manager"].current = "lista_animal"
    def Menu_Items(self,a, b, c,d, e, f):#     a, b, c,d, e, f         !
        
        self.busqueda=False
        self.MarcadorPositional("MenuControl")
        DATOS_URL_PATH= url_patterns("Menu_items","GET")
        
        for Items in DATOS_URL_PATH :# type: ignore
            if b == str(Items['PGRUPO']):
                
                if Items['activo']== True:
                    
                    self.ButtonCard_items = ButtonCard()
                    self.ButtonCard_items.imagen = self.source_apk+ Items['foto'] 
                    self.ButtonCard_items.nombre = Items['titulo']
                    self.ButtonCard_items.opcion = Items['opcion']
                    self.ButtonCard_items.Id_select = str(Items['id_MenuButton'])
                    self.ButtonCard_items.Imgdefaul = d
                    self.ButtonCard_items.type_color = str(Items['Id_Categoria'])
                    self.configo_nivel_categoria(Items,self.ButtonCard_items )
                    self.wm.screens[0].ids['mdlist'].add_widget(self.ButtonCard_items)
        
            """elif b != str(Items['PGRUPO']):
                self.wn.screens[1].ids['mdlist'].add_widget(Error())"""
        
        self.wm.screens[0].ids["screen_manager"].current = "MenuControl"
        """
        controla las direcciones del Menu segun sus datos 
        directo o indirecto
        """
      
    def Swipe_update(self):
        
        self.wm.screens[0].ids["gridlayo"].clear_widgets()
      
        
class Control(add_callbacks):
    wm = ObjectProperty()
    
    def __init__(self,**kv):
        super(Control, self).__init__(**kv)
        self.Perfiles_id = []
        self.source_apk = "Source_apk"
        Clock.schedule_once(lambda dt: self.canviar_navigation(),2)
        self.click = SoundLoader.load('soundclic/click_uorli.mp3')
        self.click.volume = 0.2
        self.click.seek(0.2)
        self._window = Window
        
        Window.bind(on_keyboard=self._handle_keyboard)
        
        
        
    def _handle_keyboard(self, _window, key, *_args, **kwargs):
        print(_args)
        print(kwargs)
        print(key)
        if key == 27 :
            pass
            return True
        
    def canviar_navigation(self):
        DATOS_URL_PATH = url_patterns("grupo","GET")
        print(DATOS_URL_PATH)
        if DATOS_URL_PATH == {}:
            #self.root.current = "Conex_error" # type: ignore
            #self.root.current = "Login_perfil"
            pass
        elif DATOS_URL_PATH != {}:
            self.root_properti()
            #self.root.current = "Store_app"
            self.ItemsDatos("Group",[]) # type: ignore
            #Clock.schedule_once(lambda dt: self.Cambio_de_pantalla("Select"), 2)
            #self.wn.screens[1].ids["screen_manager"].current = "Informacon_Final"
    def root_properti(self):
        self.root.current = "Properpantalla"# type: ignore 
        #Properpantalla Tienda
        #self.Berificacion_de_usuario()#comprobacion de usuario superadministrador
        
    
    #pantallas controladas
    def Cambio_de_pantalla(self, Pantallas):# de pagina de compra y de agregacion de datos
        self.pantalla= Pantallas
        self.click_sound()
        if self.pantalla == "Tienda":
            self.root.current = "Tienda"# type: ignore
        
        #____Pantalla configuracion____#
        elif self.pantalla == "Select":
            self.root.current = "Admin"# type: ignore
            self.wn.screens[2].ids["Screen_add_grupo"].id_grupo = ""
        elif self.pantalla == "Add_grupo":
            self.root.current = "Add_grupo"# type: ignore
        elif self.pantalla == "store_tema":
            self.root.current = "Store_app"# type: ignore
        elif self.pantalla == "Config_color_screen":
            self.root.current = "Config_color_s"# type: ignore
    
    def MarcadorPositional(self,Anterior):
        #Marca las posiciones de las entradas durante el proceso ejecucion no ostente
        #funciona con otros componentes del programa
        self.Regreso_a = Anterior

    def configo_nivel_categoria(self,Items,contextbox):
        self.DATOS_URL_PATH_TYPE= url_patterns("type_nivel","GET")
        if Items['Id_Categoria']!= None:
            for type in self.DATOS_URL_PATH_TYPE:# type: ignore
                
                if Items['Id_Categoria'] == type["id"]:
                    
                    contextbox.ids.colorbox.colors_id = eval(type["Codigo_color"])
                    contextbox.ids.preciobox.text = str(type["Precio"]) + " $"
                    contextbox.ids.preciobox.text = str(type["Precio"]) + " $"
                    contextbox.ids.preciobox.text_color = [1,1,1,1]
                    contextbox.ids.franja_precio.height = dp(35)
                    contextbox.ids.franja_precio.width = dp(100)
    
    def Regresaranincio(self,Opcion):# esa funcion es una copia
        self.InicioRegresar= Opcion
        self.click_sound()
        grids_home = [
            "gridlayo","mdlist","lista_menu","controlID", "ImagenAnimals"
        ]
        
        try:
            self.ButtonCard_items.remove_widget(self.caja_color)# type: ignore
        except :
            pass
        if self.InicioRegresar == "Home":
            self.root.current = "Properpantalla"# type: ignore
            
            self.wm.screens[0].ids["screen_manager"].current = "Gruposn"
            

        if self.InicioRegresar == "InicioDELista":
            self.MarcadorPositional("Gruposn")

            self.wm.screens[0].ids["screen_manager"].current = "Gruposn"

        if self.InicioRegresar == "lista_animal":
            self.wm.screens[0].ids["mdlist"].clear_widgets()
            self.MarcadorPositional("lista_animal")
            self.wm.screens[0].ids["screen_manager"].current = "lista_animal"

        if self.InicioRegresar == "Lista":
            
            self.wm.screens[0].ids["lista_menu"].clear_widgets()
            self.MarcadorPositional("MenuControl")
            if self.busqueda== True:
                
                self.wm.screens[0].ids["screen_manager"].current = self.Regreso_a
                self.busqueda=False
            else:
                self.wm.screens[0].ids["screen_manager"].current = "MenuControl"
            
        if self.InicioRegresar == "InicioFinal":
            self.wm.screens[0].ids["controlID"].clear_widgets()
            
            if self.busqueda== True:
          
                self.wm.screens[0].ids["screen_manager"].current = self.Regreso_a
                self.busqueda=False
            else:
                self.wm.screens[0].ids["screen_manager"].current = "MenuControl"
        if self.InicioRegresar == "all":
            self.wm.screens[0].ids["mdlist"].md_bg_color=0,0,1,1
            
    def click_sound(self):
        Clock.schedule_once(lambda dt: self.click.play(),0.1)

class MyApp(MDApp,Control):
    
    def build(self):

        # Create a list of all screen, loop through it and add it to the screenmanager
        # and return the screenmanager.
        self.wm = WindowManager()
        
        #estilos
        """
        ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo',
        'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green',
        'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange',
        'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        """
        self.theme_cls.theme_style_switch_animation=True
        self.theme_cls.theme_style_switch_animation_duration=.2
        self.theme_cls.theme_style= 'Light'
        self.theme_cls.accent_hue = '700' 
        
        #Title app
        self.title = "ZooApp"
        
        
        screens = [
            Home(),
        ]

        for screen in screens:
            self.wm.add_widget(screen)

        return self.wm
    #config-relations
    def Config_view_class(self,typecurrent=str): 
        Clock.schedule_once(lambda dt: self.click.play(),0.1)
        self.wm.screens[0].card.ids["manager_screen_config"].current = typecurrent
    def return_funcion_color(self):
        def modify_colors(color = []):
            self.wm.screens[0].ids["mdMenuadd"].md_bg_color=color
            self.wm.screens[0].card.ids["screenconfigmenu"].md_bg_color = color
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = "Dark"#['Light', 'Dark']
            modify_colors([30/255, 30/255, 31/255, 0.904])
            
            
            
        else: 
            self.theme_cls.theme_style = "Light"#['Light', 'Dark']
            modify_colors([213/255, 213/255, 218/255, 0.904] )
            
            
            
        
        


if __name__=="__main__":
    MyApp().run()