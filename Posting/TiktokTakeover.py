from scrapeImages import ScrapeImages
from Poster import Upload
from deezNuts import ChrisNolan
import os
import time
import random
import re




def main():
    searchTerms = " today travel beautiful photography epic"
    places = [
        "Guatape, Colombia",
        "Oia, Greece",
        "Bibury, England",
        "Gimmelwald, Switzerland",
        "Alberobello, Italy",
        "Shibam, Yemen",
        "Chefchaouen, Morocco",
        "Monsanto, Portugal",
        "Bergen, Norway",
        "Göltürkbükü, Turkey",
        "Tasiilaq, Greenland",
        "Telč, Czech Republic",
        "Giethoorn, Netherlands",
        "Zermatt, Switzerland",
        "Manhattan, USA (Montana)",
        "Mittenwald, Germany",
        "Český Krumlov, Czech Republic",
        "Portofino, Italy",
        "Santorini, Greece",
        "Bagnone, Italy",
        "Sapa, Vietnam",
        "Positano, Italy",
        "Hallim, South Korea",
        "Peratallada, Spain",
        "Mürren, Switzerland",
        "Göynük, Turkey",
        "Lavenham, England",
        "Manuel Antonio, Costa Rica",
        "Atrani, Italy",
        "Shirakawa, Japan",
        "Óbidos, Portugal",
        "Lauterbrunnen, Switzerland",
        "Kotor, Montenegro",
        "Eze, France",
        "Ko Phi Phi, Thailand"
    ]
    for place in places:
        makeSuccess(place, searchTerms=searchTerms)
        time.sleep(random.randint(3,6))

def makeSuccess(query:str, searchTerms:str):
    hashtags = "#beauty #place #holiday #discover #home #travel #photography #design #tiktok #black #video #follow #sunset #instacool #lifestyle #beautiful #art #family #amazing #me #eblackandwhite #picoftheday #nature #cool #summer #swag #behappy #fun #photooftheday #transgirl #life #livemoment #nofilter #sun  #pretty #winspiration #photo"
    hashtags = "#" + query.replace(" ", "")  + " " + hashtags
    description = f"Would you stay here in {query}? " + hashtags
    if not ScrapeImages(query + searchTerms):
        return
    
    imgFiles = os.listdir("images\\")
    for i in range(len(imgFiles)):
        imgFiles[i] = "images\\" + imgFiles[i]
    imgFiles = [("worldPreview.mp4", 5)] + imgFiles

    chris = ChrisNolan(targetTime=20, fps=25)
    chris.yeetInToAVid(imgFiles, audioPath="basedSound.mp3", saveName="joe.mp4")
    try:
        Upload("joe.mp4", description)
    except:
        print("failed to upload a video.")

if(__name__ == "__main__"):
    main()