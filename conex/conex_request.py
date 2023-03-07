
from ast import Pass
import requests
import os


from time import sleep
from threading import Thread
import requests
import json


class Request:
    threads = []
    bariables_progres = [
        "grupo","selec_animal_grupo","Menu_items","Lista","Informacion_final","type_nivel","Store_List_Categoria"#1
        ]
    menos_data_variable = ["Grupo",
                               "MenuButton",
                               "Lista_De_Animales",
                               ]
    #,"selec_animal_grupo","Menu_items","Lista","Informacion_final","type_nivel","Store_List_Categoria"
    direccion_request = "http://127.0.0.1:8000/" 
    request_data= str() #se refiere ala direcion que se dirigira la peticion
    request_urls = None
    opc_peticion= "get"

    
    varial_update= {"actualizar":False, "Intentos":1, }
    
  
    def __init__(self):
        super(Request, self).__init__()
        for a in  self.menos_data_variable :
            if not os.path.exists(os.path.join("componentes")): os.makedirs(os.path.join("componentes"))  
            if not os.path.exists(os.path.join("Source_apk",str(a))): os.makedirs(os.path.join("Source_apk",str(a)))   
        self.nucleo_threads()
        
    def request_mult_save(self, data,type):
            sleep(0.001)
            self.format_type = "componentes/"+ type + ".json"
            if type == "Store_List_Categoria":
                self.str_json(self.format_type,data )
            else:
                
                self.str_json(self.format_type,data )
            
    def str_json(self,a,e):
        
        from pathlib import Path
        import os
        #print(".este es {}.\n yo soy {}".format(a,e))
        try:
            for img in e.json():
               name_Image= self.name_Image(img['foto'])
        except:
            pass
        
        with open(a, "w")as j:
            json.dump(e.json(), j)
       
    
    def nucleo_threads(self): 
        fileupdate = "componentes/actualizer.json"
        
        try:
            updatate_list = (json.loads(open(fileupdate).read() ))["actualizar"]
        except:
            updatate_list = False
        if os.path.isfile(fileupdate) != True or updatate_list == True :
            
            try:
                update = json.loads(open("componentes/actualizer.json").      read())
                try:
                    s = update['actualizar']
                    true_v = s
                except:
                    true_v=True
            except:
                with open("componentes/actualizer.json", "w")as j:
                    json.dump(self.varial_update, j)
            for request_data_peticion in self.bariables_progres:
                try:
                    """print("......")
                    print(request_data_peticion)"""
                    direccion = requests.get(self.direccion_request+ str(request_data_peticion))
                    
                    if direccion.status_code != 200:
                        pass
                    else:
                        t= Thread(target = self.request_mult_save, args =(direccion,request_data_peticion,))
                        self.threads.append(t) # type: ignore
                    t.start()# type: ignore
                except:
                    self.Errors()
            
            for t in self.threads:
                t.join()
                
            
        else: 
            pass
    def bariable_local(self):
        pass
        
    def metodos(self, type_peticion):
        """
            Perfil 'no' debe aparecer dentro de esta 
            yamada encontrar una solucion mas biable
        """
        
        try:
            file = "componentes/"
            grupo =                 json.loads(open( file + "grupo.json").                  read())
            selec_animal_grupo =    json.loads(open( file + "selec_animal_grupo.json").     read())
            Menu_items =            json.loads(open( file + "Menu_items.json").             read())
            Lista =                 json.loads(open( file + "Lista.json").                  read())
            Informacion_final =     json.loads(open( file + "Informacion_final.json").      read())
            type_nivel =            json.loads(open( file + "type_nivel.json").             read())
            Store_List_Categoria =  json.loads(open( file + "Store_List_Categoria.json").   read())
            Perfil =                json.loads(open( file + "Perfil.json").                 read())
            
        
            
            if type_peticion == "Group":
                
                return grupo
            elif type_peticion == "selec_animal_grupo":
                return selec_animal_grupo
            elif type_peticion == "Menu_items":
                return Menu_items
            elif type_peticion == "Lista":
                return Lista
            elif type_peticion == "Informacion_final":
                return Informacion_final
            elif type_peticion == "type_nivel":
                return type_nivel
            elif type_peticion == "Store_List_Categoria":
                return Store_List_Categoria  
            elif type_peticion == "Perfil":
                return Perfil
        except:
            return {}
  
    def Post_request(self,objecto, data={} ):
        """
        objecto // hace referencia a los objetos de la lista ejm: Grupo, Lista extre otros 
        data // obtine la informacion como un json
        """
        url_post = self.direccion_request + str(objecto)
        post_r=requests.post(url_post, data =data)
        return post_r.status_code
    def Put_request(self,objecto=str(),id=int(), data={} ):
        url_post = self.direccion_request + str(objecto)+str("/") + str(id)
        Put_r=requests.put(url_post, data =data)
        return Put_r.status_code
    def Delete(self,objecto=str(),id=int(), data={} ):
        url_post = self.direccion_request + str(objecto)+str("/") + str(id)
        del_r=requests.delete(url_post)
        return del_r.status_code
        
    def Errors(self):
        return {}

    def name_Image(self,url):
        #os.makedirs(os.path.join('Fotos', img['foto']))
        protocol_type= "Source_apk"+url
        url_image = requests.get(self.direccion_request+url).content     
        for e in self.menos_data_variable:
            
            with open(protocol_type, 'wb') as handle:
                handle.write(url_image)
        print(protocol_type)
        
        return protocol_type
        
        

"""
c = Request()
json_prueva ={"nombre": "Historia4", "activo": True, "PGRUPO": 1, "Id_Categoria": None}
c.Delete("Lista",2)
print(c.metodos("grupo"))

"""
