import json 

class InvalidConfigError(Exception):
    "invalid config"

def load_config(file_path):
        try:

            with open(file_path, "r") as file:
                loaded_data = json.load(file)

                list_keys = list(loaded_data.keys())

                for i in range(0, len(list_keys)):
                    if list_keys[i] != "mode" and list_keys[i] != "database_url" and list_keys[i] != "api_key":
                        raise InvalidConfigError("invalid config")
                    
                if loaded_data["mode"] == "production" or loaded_data["mode"] == "debug":
                    pass
                else:
                    raise InvalidConfigError("invalid config")
                print(loaded_data)

        except FileNotFoundError:
             print("File not found.")
        except json.decoder.JSONDecodeError:
             print("Json decode error.")
        except InvalidConfigError:
             print("Invalid config error.")
 

load_config("config.json")


