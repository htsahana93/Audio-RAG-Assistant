import os, json
import joblib
import pandas as pd
import requests
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed", json = {
        "model" : 'bge-m3',
        "input" : text_list
    })

    embeddings = r.json()['embeddings']
    return embeddings

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json = {
        "model" : 'llama3.2',
        "prompt" : prompt,
        "stream" : False
    })

    response = r.json()
    print(response)
    return response

df = joblib.load('embeddings.joblib')

incoming_query = input('Ask a Question: ')
question_embeddings = create_embeddings([incoming_query])[0]

'''print(np.vstack(df['embeddings'].values))
print(np.vstack(df['embeddings'].values).shape)'''

similarity = cosine_similarity(np.vstack(df['embedding'].values), [question_embeddings]).flatten()
#print(similarity)
top_result = 5
max_inx = similarity.argsort()[::-1][0:top_result]
#print(max_inx)
new_df = df.loc[max_inx]
print(new_df[['title', 'number', 'text']])

prompt = f''' you are an audio assistant which answers questions using audio segments.

you are given multiple audio chunks extracted from audio files
each chunk contains:
title(audio_name),number(audio_number),text,start,end,spoken text

relevent data:
{new_df[["title","number","text","start","end",]].to_json(orient="records")}

------------------------------------------------------------------------------

user question:
{incoming_query}

your task:
-understand the question
-find which audio segments contains the answers
-mention the audio title or number- Understand the **meaning and intent** of the user's question
- Look for transcript segments that are **semantically related**, not just exact word matches
- Use related ideas, explanations, or context from the audio if available
-mention the exact timestamp range
-answer clearly in natural human language 
-guide the user to listen to specific part of the audio

You are a helpful assistant.
'''

with open('prompt.txt',"w") as f:
    f.write(prompt)

response = inference(prompt)['response']    
#print(response)

with open('response.txt', "w") as f:
    f.write(response)

