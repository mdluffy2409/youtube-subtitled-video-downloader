from googletrans import Translator
import threading 
from multiprocessing.dummy import Pool as ThreadPool
import os

lock = threading.Lock()
translator = Translator()

def copyTranslation(lines, new_lines, src): 
    pos = 0 
    with open(src, "wb") as f:  
        for line in lines:      
            if len(line) > 3 and line.find('-->') == -1:
                f.write("{}".format(new_lines[pos]+'\n').encode("utf8"))
                pos+=1
            else:
                f.write("{}".format(line).encode("utf8"))   

def translateLine(line):
    translation = translator.translate(line, dest='es')
    return translation.text


def translateSubtitle(src):
    lines_to_read = open(src, "r")  
    lines = [line for line in lines_to_read]
    selected_lines = [line for line in lines if len(line) > 3 and line.find('-->') == -1]

    with ThreadPool(os.cpu_count()) as p:
        new_lines = p.map(func=translateLine,iterable=selected_lines) 
        p.close() 
        p.join()
    copyTranslation(lines, new_lines, src[:src.index('.srt')] + '_es.srt')