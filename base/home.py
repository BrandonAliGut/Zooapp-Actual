
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.floatlayout import FloatLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivy.uix.modalview import ModalView
from kivy.properties import OptionProperty,BooleanProperty,ObjectProperty,NumericProperty,StringProperty
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.animation import Animation
from kivymd.uix.button import MDIconButton

from kivy.clock import Clock
class Card(MDCard):
    sources = StringProperty()
class BarraMovil(MDBoxLayout):
    tema = StringProperty()
    
class StoreTemas(Screen):
    pass
class Configuracion(Screen):
    def __init__(self,**kw):
        super(Configuracion, self).__init__(**kw)
        self.dialog_s= None
        self.oscuro = False
        self.ative_click = True
        
    def modify_class(self):
        self.click = SoundLoader.load('soundclic/click_uorli.mp3')
        self.click.volume = 0.2
        self.click.seek(0.2)
        Clock.schedule_once(lambda dt: self.click.play(),0.1)
        if self.ative_click == True:
            self.ids.select_true.active = True
            self.ids.oneLinetext.text = "Modo Claro"
            self.ids.icon_t.icon = "moon-waning-crescent"
            
            self.ative_click = False
        else:
            self.ids.select_true.active = False 
            self.ids.oneLinetext.text = "Modo Oscuro"
            self.ids.icon_t.icon = "white-balance-sunny"
            
            self.ative_click = True
            
class GridOpcMenu(Screen):
    radius= [0,0,0,20]
    def __init__(self, **kw):
        super(GridOpcMenu,self).__init__(**kw)
        
class DConfig_menu(Screen):
    radius= [0,0,0,20]
    
    
class ExtaConfig_data:
    self= None
    def __ini__(self):
        super(ExtaConfig_data,self).__init__()
        
    
        
class Config_menu(MDBoxLayout, ThemableBehavior,ExtaConfig_data):
    auto_dismiss = BooleanProperty(True)
    pos_hint= {'right': 1,'center_y': 0.5}
    _is_open = BooleanProperty(False)
    __events__ = ('on_pre_open', 'on_open', 'on_pre_dismiss', 'on_dismiss')
    _window = ObjectProperty(allownone=True, rebind=True)
    _anim_alpha = NumericProperty(0)
    _touch_started_inside = None
    _anim_duration = NumericProperty(.1)
    elevation= dp(0)
    
    
    def __init__(self,**kwargs):
        self._parent = None
        super(Config_menu,self).__init__(**kwargs)
        self.call_expand_button = True
        Clock.schedule_once(lambda dt: self.addWidget(),0.1)
        self.click = SoundLoader.load('soundclic/click_uorli.mp3')
        self.click.volume = 0.2
        
        
    def color(self, a,b,c,d):
        list_c = a/255,b/255,c/255, d
        
        return list(list_c)
    def call_expand(self):
        Clock.schedule_once(lambda dt: self.click.play(),0.1)
        def call_center_acive(size,color,radio):
            self.radius = radio
            a,b,c,d = color
            self.size_hint= size
            self.md_bg_color= self.color(a,b,c,d)
            self.call_expand_button = False if self.call_expand_button else True
            
        if  self.call_expand_button == True:
            
            call_center_acive((1,1), (6, 131, 241, 0.534),([1,1,1,1]))
            
        else:
            call_center_acive((.8,.8), (213, 213, 218, 0.904),[20,0,0,20])    
    def open(self, *_args, **kwargs):
        """Display the modal in the Window.

        When the view is opened, it will be faded in with an animation. If you
        don't want the animation, use::

            view.open(animation=False)

        """
        from kivy.core.window import Window
        if self._is_open:
            return
        self._window = Window
        self._is_open = True
        self.dispatch('on_pre_open')
        Window.add_widget(self)
        Window.bind(
            on_resize=self._align_center,
            on_keyboard=self._handle_keyboard)
        self.center = Window.center
        self.fbind('center', self._align_center)
        self.fbind('size', self._align_center)
        if kwargs.get('animation', True):
            ani = Animation(_anim_alpha=1., d=self._anim_duration)
            ani.bind(on_complete=lambda *_args: self.dispatch('on_open'))
            ani.start(self)
        else:
            self._anim_alpha = 1.
            self.dispatch('on_open')
    def dismiss(self, *_args, **kwargs):
        """ Close the view if it is open.

        If you really want to close the view, whatever the on_dismiss
        event returns, you can use the *force* keyword argument::

            view = ModalView()
            view.dismiss(force=True)

        When the view is dismissed, it will be faded out before being
        removed from the parent. If you don't want this animation, use::

            view.dismiss(animation=False)

        """
        if not self._is_open:
            return
        
        self.dispatch('on_pre_dismiss')
        if self.dispatch('on_dismiss') is True:
            
            self._anim_alpha = 0
            self._real_remove_widget()
            if kwargs.get('force', False) is not True:
                return
        if kwargs.get('animation', True):
            Animation(_anim_alpha=0., d=self._anim_duration).start(self)
    def _real_remove_widget(self):
        if not self._is_open:
            return
        self._window.remove_widget(self)
        self._window.unbind(
            on_resize=self._align_center,
            on_keyboard=self._handle_keyboard)
        self._is_open = False
        self._window = None
        
    def _handle_keyboard(self, _window, key, *_args):
        
        if key == 27 and self.auto_dismiss:
            self.dismiss()
            return True
    def on_touch_down(self, touch):
        """ touch down event handler. """
        self._touch_started_inside = self.collide_point(*touch.pos)
        if not self.auto_dismiss or self._touch_started_inside:
            super().on_touch_down(touch)
        return True

    def on_touch_move(self, touch):
        """ touch moved event handler. """
        if not self.auto_dismiss or self._touch_started_inside:
            super().on_touch_move(touch)
        return True

    def on_touch_up(self, touch):
        """ touch up event handler. """
        # Explicitly test for False as None occurs when shown by on_touch_down
        if self.auto_dismiss and self._touch_started_inside is False:
            self.dismiss()
        else:
            super().on_touch_up(touch)
        self._touch_started_inside = None
        return True

    def _align_center(self, *_args):
        if self._is_open:
            self.center = self._window.center
    def on_pre_open(self):
        """ default pre-open event handler. """

    def on_open(self):
        """ default open event handler. """
        Clock.schedule_once(lambda dt: self.click.play(),0.1)

    def on_pre_dismiss(self):
        """ default pre-dismiss event handler. """

    def on_dismiss(self):
        """ default dismiss event handler. """
        Clock.schedule_once(lambda dt: self.click.play(),0.1)
        return True
    
    def addWidget(self):
        self.ids.manager_screen_config.add_widget(GridOpcMenu())

    
    
Builder.load_file("./base/kv/home.kv")
class Home(Screen):
     
    def __init__(self):
        super(Home,self).__init__()
        self.menu = None
        self.card = Config_menu()
        self.position = OptionProperty(
        "logaut", options=["login", "logaut"]
        )
        self.position="login"
        self.click = SoundLoader.load('soundclic/click_uorli.mp3')
        self.click.volume = 0.2
    def menu_drop(self):
        if self.menu == None:
            self.menu= MDDropdownMenu(
                position= "top",
                caller = self.ids.account_buton,
                items = self.menu_register(),
                elevation = 0,
                background_color= [240/255, 248/255, 255/255, 0.479], 
                width_mult=1,
            ).open()
            
    def menu_register(self):
        
        position = self.position
        menu_items = []
      
        
        if position == "logaut":
            menu_items.append(
                 {
                "icon": "login",
                "viewclass":"MDIconButton",
                
                "height": dp(56),
                
                "on_release": lambda x="Login": self.menu_callback(x),
            },)
        elif position == "login":
            
            list_items = (
                {
                    "icon": "account",
                    "viewclass":"MDIconButton",
                    "height": dp(56),
                    "on_release": lambda x="perfil": self.menu_callback(x),
                },
                {
                    "icon": "exit-to-app",
                    "viewclass":"MDIconButton",
                    "height": dp(56),
                    "on_release": lambda x="exit": self.menu_callback(x),
                }
            )
            for i in list_items:
                menu_items.append(i)
            
       
            
        
        return menu_items
    
    def menuConfigCard(self):
        Clock.schedule_once(lambda dt: self.click.play(),0.1)
        Clock.schedule_once(lambda dt: self.card.open(),.5)
        
        
        
    def menu_callback(self,x):
        Clock.schedule_once(lambda dt: self.click.play(),0.1)
        if x == "exit":
            self.position = "logaut"
            self.menu = None
       
    def callback2(self):
        print("Right Icon Pressed!")
        
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder


