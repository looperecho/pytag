from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3
import os
import shlex


def split_filename(file):
    filename = os.path.basename(file)
    name, ext = os.path.splitext(filename)
    info = name.split(" - ", 1)
    return info


def delete_art(file):
    print("Removing artwork...")
    audio = ID3(file)
    audio.delall("APIC") # Delete every APIC tag (Cover art)
    audio.save() # Save the file
    
    
def set_tags(info, file):
    print("Setting tags...")
    audio = EasyID3(file)
    audio["artist"] = info[0]
    audio["title"] = info[1]
    audio.save()
    
    
def main():
    file_input = input("\nAdd file: ")
    
    try:
        input_tokens = shlex.split(file_input)
    except Exception as e:
        print(f"Error parsing input: {e}")
        return
    if not input_tokens:
        print("No file path provided.")
        return
    file = input_tokens[0]
    
    if os.path.exists(file):
        try:    
            info = split_filename(file)
            print(f"Artist: {info[0]}\nTitle: {info[1]}")
            set_tags(info, file)
            delete_art(file)
            print(f"Done: {info[0]} - {info[1]}\n-----")
        except IOError as e:
            print(f"Error reading file {e}")
    else:
        print("Something went wrong")


if __name__ == '__main__':
    while True:
        main()