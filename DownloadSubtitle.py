from youtube_transcript_api import YouTubeTranscriptApi
import os
from TranslateSubtitle import translateSubtitle

cwd = os.getcwd()

def parseLine(i, line, f):
    duration = float(line["start"]) + float(line["duration"])
    f.write("{}\n".format(i + 1).encode("utf8"))
    f.write("{}\n".format(str(line["start"]) + " --> " + str(duration)).encode("utf8"))
    f.write("{}\n\n".format(line["text"]).encode("utf8"))

def getSubtitle(url, title):
    srt = YouTubeTranscriptApi.get_transcript(url) 
    src = os.path.join(cwd, "Files", title, title + '.srt')
    with open(src, "wb") as f:      
        for i in range(len(srt)):
            parseLine(i, srt[i], f)
    translateSubtitle(src)