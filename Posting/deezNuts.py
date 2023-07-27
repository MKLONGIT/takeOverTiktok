from moviepy.editor  import *
import math


class ChrisNolan:

    vidSize = (1080,1920)
    def __init__(self, targetTime = 20, fps = 24):
        self.targetTime = targetTime
        self.fpsRussia = fps
        self.audioPath = "schpoddyfei\\gg.mp3"
        self.vidPath = "vidCon\\test.mp4"

    def yeetInToAVid(self, images:list, audioPath=None, saveName:str = "balls"):
        self.vidPath = saveName
        self.audioPath = audioPath
        clips = []
        numberOfImages = len(images)
        individualLen = math.floor(self.targetTime / numberOfImages)
        t = 0
        actualMaxTime = numberOfImages * individualLen
        daSize = self.vidSize
        colorthing = ColorClip(size=daSize, color=(0,0,0), ismask=False).set_start(0).set_duration(actualMaxTime).set_pos(("center","center"))
        clips.append(colorthing)

        for i in range(numberOfImages):
            theImage = images[i]
            clip = ImageClip(theImage).set_start(t).set_duration(individualLen).set_pos(("center","center")).resize(width=self.vidSize[0])
            clips.append(clip)
            t += individualLen


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


    def testDaShit(self):
        imagineallthepeople = os.listdir("imagineallthepeople\\")

        lesImages = []

        for image in imagineallthepeople:
            lesImages.append("imagineallthepeople\\" + image)

        self.yeetInToAVid(lesImages)