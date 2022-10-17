import json
class Setter:
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
        with open(self.url, "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_title(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["body"]["title"] = mean

        with open(self.url, "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_description(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["body"]["description"] = mean

        with open(self.url, "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_url(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["body"]["url"] = mean

        with open(self.url, "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_color(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["body"]["color"] = mean

        with open(self.url, "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_author(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["author"]["title"] = mean

        with open(self.url, "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))
    
    def set_author_url(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["author"]["url"] = mean

        with open(self.url, "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_author_icon(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["author"]["icon"] = mean

        with open(self.url, "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_image_thumbnail(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["images"]["thumbnail"] = mean

        with open(self.url, "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_image(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["images"]["url"] = mean

        with open(self.url, "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_footer(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["footer"]["title"] = mean

        with open(self.url, "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_time(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["footer"]["time"] = mean

        with open(self.url, "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))

    def set_footer_icon(self, user: str, mean: str):
        with open(self.url, "r") as file: basa = json.load(file)
        basa[user]["footer"]["icon"] = mean

        with open(self.url, "w") as file: file.write(json.dumps(basa, indent=4).replace("\'", "\""))