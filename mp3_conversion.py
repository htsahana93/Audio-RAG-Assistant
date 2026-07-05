import os
import json
import subprocess

os.makedirs("audioss", exist_ok=True) 

files = os.listdir("audios")
for file in files:
    if file.endswith(".mp3"):
        base = os.path.splitext(file)[0]
        name , number = base.rsplit("-",1)
        #print(name,number)
        subprocess.run(["ffmpeg", "-i", f"audios/{file}",f"audioss/{name}_{number}.mp3"])
