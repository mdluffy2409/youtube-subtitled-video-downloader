import os

cwd = os.getcwd()

def getVideo(yt, title):
    try: 
        yt.streams.filter(progressive=True,file_extension='mp4').order_by(
            'resolution').desc().first().download(os.path.join(cwd, "Files", title))
    except: 
        print("Some Error!") 