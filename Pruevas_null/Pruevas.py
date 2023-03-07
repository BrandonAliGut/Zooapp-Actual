import json
import os
class Data:
    source_data_exit = str()
    data=None
    
    folder="DataZooApp"
    
    folders = "style/"
    
    name_archivo = "config_principal.json"
    
    def __init__(self):
        super(Data,self).__init__()
        
        self.dir_folder= self.folder +"/"+ self.folders
        self.dir_dir_data_source = self.dir_folder + self.name_archivo
        self.data_json= None
        if self.data ==None: self.data = self.initial_Config = [
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
             
    def json_patterns_create(self):
        pass
    
    def confirmar(self):
        if not os.path.exists(os.path.join(self.dir_folder)):
            os.makedirs(os.path.join(self.dir_folder))
            self.crear()
            return True
        else:
            return False  
    
    def crear(self):
        with open(self.dir_dir_data_source, "w")as j:
            json.dump(self.data, j)
    
    def get(self,items1=str(),items2=str(), **kwargs):
        def process(items1="",items2=""):
            def x(items1,items2):
                if items1 !="" and items2 == "":
                    if self.list_v:
                        print("si")
                        for a in self.list_v():
                            d = a[items1] if items1 !="" else a["config"]
                            return d
                
                if items2 !="":
                    print("si extra")
                    if self.list_v:
                        for a in self.list_v():
                            asd=a[items1] if items1 !="" else a["config"]
                            for ad in asd:
                                d= ad[items2] if items1 !="" else ad["accent_hue"]
                                return  d
            def y():
                if self.list_v:
                        for a in self.list_v():
                            asd=a["config"] 
                            for ad in asd:
                                d= ad["accent_hue"] if items1 !="" else "accent_hue"
                                return  d
                            
                            
            if items1!="" or items2!= "":
                return x(items1,items2)
            else:
                print("siis")
                return y()
                
        if len(items1)!=0 or len(items2)!=0:
            return process(items1,items2)
        else:
            return process()
            
    
    def list_v(self,dir=str()):
        self.source_data_exit = dir
        def datajson(dircion=str()):
            def vacio():
                
                self.data_json = json.loads(open(self.dir_dir_data_source).read())
                return self.data_json
            def exists(dircion):
                
                self.data_json = json.loads(open(dircion).read())
                return self.data_json
            if len(dircion) !=0:
                data_=exists(dircion)
                return data_
            else:
                return vacio()
            
        if len(self.source_data_exit) != 0:
            return datajson(dir)
        else:
            if not self.confirmar():
                return datajson()
            else:
                return {}
            
nuevo = Data()
print(nuevo.get("config"))