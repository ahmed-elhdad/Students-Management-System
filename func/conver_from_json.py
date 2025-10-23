import json
def conver_fom_json(path):
    try:
        with open(path,'r') as f:
            txt=f.read()
            python_txt=json.loads(txt)
            return python_txt
    except Exception as e:
        raise e
