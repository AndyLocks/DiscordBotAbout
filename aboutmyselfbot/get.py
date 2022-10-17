import json
class Getter:
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
        with open(self.url, "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))