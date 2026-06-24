import json

def write_file(file_path, data):
    try:
        with open(file_path, "w") as data_base:
            json.dump(data, data_base, indent=4)
            return True
    except Exception:
        return False
    
def read_file(file_path):
    try:
        with open(file_path, "r") as data_base:
            return json.load(data_base)

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):
        return []