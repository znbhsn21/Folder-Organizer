import os
from pathlib import Path
import shutil

folder_path = '/Users/zenab/OneDrive/Random'

os.chdir('/Users/zenab/OneDrive/Random')

pic_path = '/Users/zenab/OneDrive/Random/Images'
vid_path = '/Users/zenab/OneDrive/Random/Videos'
aud_path = '/Users/zenab/OneDrive/Random/Audio'
doc_path = '/Users/zenab/OneDrive/Random/Documents'
arc_path = '/Users/zenab/OneDrive/Random/Archives'
others = 'Users/zenab/OneDrive/Random/Others'

for files in os.listdir(folder_path):
    if(os.path.isfile(files)):
        path_object = Path(files)
        ext = path_object.suffix
        if ext == '.png' or ext == '.jpg' or ext == '.jpeg' or ext == '.gif' or ext == '.bmp':
            shutil.move(files, pic_path)
        elif ext == '.mp4' or ext == '.avi' or ext == '.mov' or ext == '.mkv':
            shutil.move(files, vid_path)
        elif ext == '.mp3' or ext == '.wav' or ext == '.aac':
            shutil.move(files, aud_path)
        elif ext == '.pdf' or ext == '.docx' or ext == '.doc' or ext == '.txt' or ext == 'xlsx' or ext == 'pptx':
            shutil.move(files, doc_path)
        elif ext == '.zip' or ext == '.rar' or ext == '.7z' or ext == '.tar' or ext == 'gz':
            shutil.move(files, arc_path)
        else:
            shutil.move(files, others)

print(os.listdir('/Users/zenab/OneDrive/Random/'))