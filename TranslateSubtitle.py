from cmath import e
from pdb import line_prefix
from googletrans import Translator
import threading 
from multiprocessing.dummy import Pool as ThreadPool
import os

lock = threading.Lock()
translator = Translator()

def copyTranslation(lines, new_lines, src):  
    with open(src, "wb") as f:  
        for pos in range(0, len(lines), 4):      
            f.write("{}".format(lines[pos]).encode("utf8"))
            f.write("{}".format(lines[pos + 1]).encode("utf8"))
            f.write("{}".format(new_lines[int(pos / 4)]).encode("utf8"))
            f.write("{}".format(lines[pos + 3]).encode("utf8"))

def translateLine(line):
    translation = translator.translate(line, dest='es')
    return translation.text


def translateSubtitle(src):
    lines_to_read = open(src, "r")  
    lines = [line.replace('\n', '') for line in lines_to_read]
    selected_lines = [lines[pos] for pos in range(2, len(lines), 4)]

    with ThreadPool(os.cpu_count()) as p:
        new_lines = p.map(func=translateLine,iterable=selected_lines) 
        p.close() 
        p.join()
    copyTranslation(lines, new_lines, src[:src.index('.srt')] + '_es.srt')