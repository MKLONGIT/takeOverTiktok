from moviepy.editor  import *
import math
import os

class ChrisNolan:

    vidSize = (1080,1920)
    def __init__(self, targetTime = 20, fps = 24):
        self.targetTime = targetTime
        self.fpsRussia = fps
        self.audioPath = "schpoddyfei\\gg.mp3"
        self.vidPath = "vidCon\\test.mp4"

    def isPicture(self, string):        
        if type(string) != tuple:
            extension = os.path.splitext(string)[-1]
            if extension == ".png" or extension == ".jpg" or extension == ".jpeg" or extension == ".webp":
                return True
            return False 
    def isVideo(self, string):
        if type(string) == tuple:
            extension = os.path.splitext(string[0])[-1]
            if extension == ".mov" or extension == ".mp4" or extension == ".avi":
                return True
        return False

    def yeetInToAVid(self, images:list, audioPath=None, saveName:str = "balls"):
        self.vidPath = saveName
        self.audioPath = audioPath
        clips = []
        numberOfImages = 0

        # the videos determine the time that is left for images:
        videoTime = 0
        for img in images:
            if self.isVideo(img):
                videoTime += img[1]
            elif self.isPicture(img):
                numberOfImages+=1
        individualLen = math.floor((self.targetTime - videoTime) / numberOfImages)
        t = 0
        actualMaxTime = self.targetTime
        daSize = self.vidSize
        colorthing = ColorClip(size=daSize, color=(0,0,0), ismask=False).set_start(0).set_duration(actualMaxTime).set_pos(("center","center"))
        clips.append(colorthing)

        for i in range(len(images)):
            clip = None
            actualLen = individualLen
            
            if self.isPicture(images[i]):
                theImage = images[i]
                try:
                    clip = ImageClip(theImage).set_start(t).set_duration(individualLen).set_pos(("center","center")).resize(width=self.vidSize[0])
                except:
                    return False
            elif self.isVideo(images[i]):
                clip = VideoFileClip(images[i][0]).set_start(t).set_duration(images[i][1]).set_pos(("center", "center")).resize(width=self.vidSize[0])
                actualLen = images[i][1]
            if clip is not None:
                t += actualLen
                clips.append(clip)


        final = CompositeVideoClip(clips)

        #final.write_videofile(self.vidPath, fps=self.fpsRussia, )

        videoclip = final #VideoFileClip(self.vidPath)
        audioFileThing = AudioFileClip(self.audioPath).set_duration(actualMaxTime)
        audioclip = CompositeAudioClip([audioFileThing])
        videoclip.audio = audioclip
        yeet = self.vidPath.split(".")
        name = yeet[-2]
        #name += "_withAudio"
        audvidPath = name + "."+ yeet[-1]
        videoclip.write_videofile(audvidPath, fps=self.fpsRussia)

        return True


    def testDaShit(self):
        imagineallthepeople = os.listdir("imagineallthepeople\\")

        lesImages = []

        for image in imagineallthepeople:
            lesImages.append("imagineallthepeople\\" + image)

        self.yeetInToAVid(lesImages)