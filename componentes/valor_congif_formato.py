import json
data = {
    "estructura_primaria":{
    "fonot_color":{
        'menu_color':[
            1,1,1,1
        ],
        'string_color':{
                "noche": [1,1,1,1],
                "dia": [0,0,0,1]
            },
        'centro_card':{
                "color":[1,1,1,1],
                "font_size": "dp(12)",
                "img": ""
            },
    
    },
    "User":{
        "User":{
            "contraceña":"Brandon ALi Gutierrez",
            "User": "_2D",
            "Toquen_utentificacion": "ksjkjfdkaljfdlakjlkfdjasdfafs",
            },
        "Datos_extra":{
            "primer_nombre":"Brandon",
            "segundo_nombre":"ALi",
            "primer_apellido": "Gutierrez",
            "segundo_apellido":"",
        },
        "compras":{
            "activo":False,
            "moneda": "$",
            "nivel":[1,2,3],
            "precio_total":20,
            "Acesso":{
                "gratis":True, 
                "medio":False, 
                "total": False
                }
        }
    
    }
    
    }
}
   
with open('componentes/myfile.json', 'w')as j:
    json.dump(data,j)