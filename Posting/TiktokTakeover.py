from scrapeImages import ScrapeImages
from Poster import Upload
from deezNuts import ChrisNolan
import os

def main():
    places = ["manhattan", "boston", "edmonton", "vancouver", "calgary", "melbourne", "las vegas", "los angeles"]
    for place in places:
        makeSuccess(place)

def makeSuccess(query:str):
    hashtags = "#beauty #place #holiday #discover #home #travel #photography #design #tiktok #black #video #follow #sunset #instacool #lifestyle #beautiful #art #family #amazing #me #eblackandwhite #picoftheday #nature #cool #summer #swag #behappy #fun #photooftheday #transgirl #life #livemoment #nofilter #sun  #pretty #winspiration #photo"
    hashtags = "#" + query.replace(" ", "")  + " " + hashtags
    description = f"Would you stay here in {query}? " + hashtags
    ScrapeImages(query)
    imgFiles = os.listdir("images\\")
    for i in range(len(imgFiles)):
        imgFiles[i] = "images\\" + imgFiles[i]
    
    chris = ChrisNolan(targetTime=20, fps=25)
    chris.yeetInToAVid(imgFiles, audioPath="basedSound.mp3", saveName="joe.mp4")

    Upload("joe.mp4", description)

if(__name__ == "__main__"):
    main()