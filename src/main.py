from functools import partial as _
import os
from art import *
from ncoreparser import *
import json


class configFile:
    def __init__(self, path): 
        self.checkExistenceOfConfigFile(path)
        self.configJSON = json.loads(open(path).read())
        #self.__getattr__ = self.configJSON.__getitem__
                
    def checkExistenceOfConfigFile(self, path):
        configMissingError = "Oh no! The config file is missing!" \
            "Please create one with the name 'config.json'"
        assert os.path.isfile(path), configMissingError    
        
    def __getattr__(self, item):
        return self.configJSON[item]

class streamingTorrentClient:
    def __init__(self, path, mediaPlayer):
        self.path = path
        self.mediaPlayer = "--"+mediaPlayer.lower()
    def play(self):
        os.system(f"webtorrent {self.mediaPlayer} {self.path}")

def setupMovierDir():
    if not os.path.exists("/tmp/movier"): os.mkdir("/tmp/movier") 
    if len(os.listdir("/tmp/movier")):
        os.remove(f"/tmp/movier/{os.listdir('/tmp/movier')[0]}")

clear = _(print, "\033[H\033[J")

def renderLogo():
    tprint("MovieR", font = "random")
    print("Welcome to MovieR!\n")

def main():
    config = configFile("config.json")
    
    client = Client()
    client.open(*config.login.values())

    try:    
        client.download(
            sorted(
                client.search(
                    pattern = input("Enter search query!\n> "),
                    type = SearchParamType.HD_HUN,
                    number = 3,
                    sort_by = ParamSort.SEEDERS,
                    sort_order = ParamSeq.DECREASING
                ),
                key = (lambda torrent: torrent["size"]),
                reverse = True
            )[0],
            "/tmp/movier/"
        )
    except IndexError:
        print("No results for your query! :C")
        quit(1)

    client.close()
    
    streamingTorrentClient(f"/tmp/movier/{os.listdir('/tmp/movier')[0]}", config.mediaPlayer).play()

if __name__ == "__main__":
    clear()
    setupMovierDir()
    renderLogo()
    main()
    clear()