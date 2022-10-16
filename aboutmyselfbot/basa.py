import json

class Singleton (type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Basa(metaclass=Singleton):
    def __init__(self, basa: str):
        self.url = basa

    def user_in(self, user: str) -> bool:
        with open(self.url, "r") as file: basa = json.load(file)
        if user in basa:

            return True
        return False

    def make_new(self, user: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa.update({user : {
        "body" : {
            "title" : None,
            "description" : None,
            "url" : None,
            "color" : 11110385
        },
        "author" : {
            "title" : None,
            "url" : None,
            "icon" : None
        },
        "images" : {
            "url" : None,
            "thumbnail" : None
        },
        "footer" : {
            "title" : None,
            "time" : None,
            "icon" : None
        }
        }})
        with open("basa.json", "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_title(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["body"]["title"] = mean

        with open("basa.json", "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_description(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["body"]["description"] = mean

        with open("basa.json", "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_url(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["body"]["url"] = mean

        with open("basa.json", "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_color(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["body"]["color"] = mean

        with open("basa.json", "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_author(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["author"]["title"] = mean

        with open("basa.json", "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))
    
    def set_author_url(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["author"]["url"] = mean

        with open("basa.json", "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_author_icon(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["author"]["icon"] = mean

        with open("basa.json", "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_image_thumbnail(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["images"]["thumbnail"] = mean

        with open("basa.json", "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_image(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["images"]["url"] = mean

        with open("basa.json", "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_footer(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["footer"]["title"] = mean

        with open("basa.json", "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_time(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["footer"]["time"] = mean

        with open("basa.json", "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_footer_icon(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["footer"]["icon"] = mean

        with open("basa.json", "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))



    def get_title(self, user: str): 
        with open(self.url, "r") as file: basa = json.load(file)
        return basa[user]["body"]["title"]

    def get_description(self, user: str): 
        with open(self.url, "r") as file: basa = json.load(file)
        return basa[user]["body"]["description"]

    def get_url(self, user: str): 
        with open(self.url, "r") as file: basa = json.load(file)
        return basa[user]["body"]["url"]

    def get_color(self, user: str): 
        with open(self.url, "r") as file: basa = json.load(file)
        return basa[user]["body"]["color"]

    def get_author(self, user: str): 
        with open(self.url, "r") as file: basa = json.load(file)
        return basa[user]["author"]["title"]
    
    def get_author_url(self, user: str): 
        with open(self.url, "r") as file: basa = json.load(file)
        return basa[user]["author"]["url"]

    def get_author_icon(self, user: str): 
        with open(self.url, "r") as file: basa = json.load(file)
        return basa[user]["author"]["icon"]

    def get_image_thumbnail(self, user: str): 
        with open(self.url, "r") as file: basa = json.load(file)
        return basa[user]["images"]["thumbnail"]

    def get_image(self, user: str): 
        with open(self.url, "r") as file: basa = json.load(file)
        return basa[user]["images"]["url"]

    def get_footer(self, user: str): 
        with open(self.url, "r") as file: basa = json.load(file)
        return basa[user]["footer"]["title"]

    def get_time(self, user: str): 
        with open(self.url, "r") as file: basa = json.load(file)
        return basa[user]["footer"]["time"]

    def get_footer_icon(self, user: str): 
        with open(self.url, "r") as file: basa = json.load(file)
        return basa[user]["footer"]["icon"]

    def clear_all(self, user: str):
        with open(self.url, "r") as file: basa = json.load(file)
        del basa[user]
        with open("basa.json", "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))
