from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        toml_dict = toml.loads(content)

        #print(toml_dict)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(toml_dict.get("tool").get("poetry").get("name"), 
            toml_dict.get("tool").get("poetry").get("description"), 
            toml_dict.get("tool").get("poetry").get("dependencies"), 
            toml_dict.get("tool").get("poetry").get("dev-dependencies"))
