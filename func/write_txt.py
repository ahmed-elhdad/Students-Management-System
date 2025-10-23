from func.convert_to_json import convert_to_json
def write_txt(path,txt):
    try:
            
        json_txt=convert_to_json(txt)
        with open(path,'w') as f:
            f.truncate(0)
            f.write(json_txt)
    except Exception as e:
        print("Error: ",e)