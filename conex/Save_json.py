import json
def str_json(type,data):
    name = "./componentes/style_windows/"+ type + ".json"
    with open(name, "w")as j:
        json.dump(data, j)
    