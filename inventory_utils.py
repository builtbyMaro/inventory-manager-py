import json

def write_file(file_path, data):
    with open(file_path, "w") as data_base:
        json.dump(data, data_base, indent=4)
    
def read_file(file_path) -> dict:
    try:
        with open(file_path, "r") as data_base:
            return json.load(data_base)

    except json.JSONDecodeError:
        return {}