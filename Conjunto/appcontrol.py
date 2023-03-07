"""
appzoon es un contendor de parametros funcionales para el programa.
almacenan direcciones y estructuras de codigos especificos 
"""
from conex.conex_request import Request
import os
import json

def url_patterns(path,method=None,id=None):
    request_data= Request()
    #print(request_data.metodos("Group"))
    if "GET":
        return request_data.metodos(path)

class Data:
    def __init__(self):
        super(Data,self).__init__()
        self.data_json= json()
        initial_Config = [
                {
                    "config":[
                        {
                            "theme_style":"Light",
                            "accent_hue":"500",
                            "primary_palette":"Blue",
                            "primary_hue":"500",
                            "primary_light_hue":"200",
                            "primary_dark_hue":"700"
                            
                        }
                        
                    ],
                    "color_all":[
                        {
                        }
                        
                    ]
                }
            ]
             
    def json_patterns(self):
        pass
    def confirmar(self):
        if not os.path.exists(os.path.join("DataZooApp/style")):
            os.makedirs(os.path.join("DataZooApp/style"))
            self.crear()
            return True
        else:
            return False  
    def crear(self):
        with open("DataZooApp/style/config_principal.json", "w")as j:
            json.dump(self.initial_Config, j)
        
    def get(self):
        if self.list_v:
            for a in self.data_json:
                asd=a["config"]
                for ad in asd:
                    print(ad['accent_hue'])
                
    def list_v(self):
        if self.confirmar():
            self.data_json = json.loads(open("./DataZooApp/style/config_principal.json").read())
            return self.data_json  
        else:
            return False
    