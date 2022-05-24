import os
import shutil
import time
import logging
from unicodedata import name
#from threading import Thread
#from time import perf_counter
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

## FILL IN BELOW
source_dir = (r"C:\Users\g5g4m\Downloads")
dest_dir_sfx = (r"C:\Users\g5g4m\Music")
dest_dir_music = (r"C:\Users\g5g4m\Music")
dest_dir_video = (r"D:\Videos")
dest_dir_image = (r"C:\Users\g5g4m\OneDrive\Bilder")
dest_dir_pdf = (r"D:\pdf")
dest_dir_zip = (r"D:\zips")
dest_dir_py = (r"D:\Programming-Hacking")
dest_dir_docs = (r"C:\Users\g5g4m\OneDrive\Dokumente")
dest_dir_exe = (r"D:\exe-installers")

### MORE THREADS = MORE FAST ## Not working currently
#
#threads = [Thread(target=move, args=(path, id, filename)) for path in os]
#for thread in threads:
#    thread.start()
#for thread in threads:
#    thread.join()
#
## ADD MORE TYPES

def makeUnique(path):
    filename, extension = os.path.splitext(path)
    counter = 1
    ## IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1
    return path

def move(dest, entry, name):
    file_exists = os.path.exists(dest + "/" + name)
    if file_exists:
        unique_name = makeUnique(name)
        os.rename(entry, unique_name)
    shutil.move(entry,dest) 

class MoverHandler(FileSystemEventHandler):
    ## THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                ## ADD MORE IF STATEMENTS FOR DIFFERENT FILETYPES 
                if name.endswith('.wav') or name.endswith('.mp3'):
                    if entry.stat().st_size < 25000000 or "SFX" in name:
                        dest = dest_dir_sfx
                    else:                       ## Currently not in use both go in the Same directory
                        dest = dest_dir_music 
                    move(dest, entry, name)
                elif name.endswith('.mov') or name.endswith('.mp4') or name.endswith('.mkv'):
                    dest = dest_dir_video
                    move(dest, entry, name)
                elif name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith('.png') or name.endswith('.PNG') or name.endswith('.gif'): # Some images png are in uppercase
                    dest = dest_dir_image
                    move(dest, entry, name)                   
                elif name.endswith('.pdf'): # Add pdfs
                    dest = dest_dir_pdf
                    move(dest, entry, name)
                elif name.endswith('.zip') or name.endswith('.rar') or name.endswith('.xz') or name.endswith('.tar'): ##Zips TODO: unzip them and get them out of theire folders
                    dest = dest_dir_zip
                    move(dest, entry, name)
                elif name.endswith('.py') or name.endswith('.pys') or name.endswith(".js") or name.endswith(".jar") or name.endswith(".log") or name.endswith(".pyc") or name.endswith(".sql"): ##Programming Shit
                    dest = dest_dir_py
                    move(dest, entry, name)
                elif name.endswith('.txt') or name.endswith('.docx'): ## Text Documents
                    dest = dest_dir_docs
                    move(dest, entry, name)
                elif name.endswith('.exe') or name.endswith('.ini'): ## Installers 
                    dest = dest_dir_exe
                    move(dest, entry, name)


print("Ready and working")  ## TODO ADD Check for functionality and status
## NO NEED TO CHANGE BELOW CODE
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()