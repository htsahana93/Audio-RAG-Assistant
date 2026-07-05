import os
import json
import whisper

model = whisper.load_model("small")

audios = os.listdir("audioss")

for audio in audios:
    if "_" not in audio or not audio.lower().endswith(".mp3"):
        continue


    base = os.path.splitext(audio)[0]
    title, number = base.rsplit("_", 1)

    #print(title,number)
    result = model.transcribe(audio = f"audioss/{audio}",
                                  task = "translate",
                                  word_timestamps=False,
                                  fp16 = False)
    #print(result)

    chunks = []
    for segment in result['segments']:
        chunks.append({"number" : number, "title" : title , "start" : segment['start'], "end" : segment['end'], "text" : segment['text']})

    chunks_with_data = {"chunks" : chunks, "text" : result['text']}

    os.makedirs("jsons", exist_ok=True)

    with open(f"jsons/{base}.json","w")as f:
        json.dump(chunks_with_data,f)