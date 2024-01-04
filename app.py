import gradio as gr
import requests

"""
    Get your API key from https://makersuite.google.com/app/apikey 
"""

API_KEY = "" #Enter your API key
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}".format(API_KEY=API_KEY)


def processor(input):

    payload = {
        "contents":[
            {
                "parts":[
                    {
                        "text": "Make a joke from the following statement," + input
                    }
                ]
            }
        ]
    }

    response = requests.post(API_URL,json=payload)

    return response.json()['candidates'][0]['content']['parts'][0]['text']

"""
    We have used the gradio framework,
    Full documentation visit https://www.gradio.app/
"""

inputs = gr.Textbox(lines=2, placeholder="Eg: Tell me a coffee shop joke",label="Input Text")
outputs = gr.Textbox(label="Joke(s) Generated")
title = "Joke Generator App"

app = gr.Interface(fn=processor,inputs=inputs,outputs="text",title=title)
app.launch(share=True)
