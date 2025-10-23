import json
def convert_to_json(txt):
    if txt=="" or txt is None:
        return 'no txt'
    json_txt=json.dumps(txt)
    return json_txt