import gradio as gr
import speech_recognition as sr
import pyttsx3
import cv2

def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data)

def text_to_speech(text, voice='default'):
    engine = pyttsx3.init()
    # You would select voice parameters based on 'voice' input
    voices = engine.getProperty('voices')
    if voice == 'realistic':
        engine.setProperty('voice', voices[1].id)  # example realistic voice, adjust as needed
    engine.say(text)
    engine.runAndWait()
    return text

def chat_function(input_text, audio_input, voice_option):
    if audio_input:
        response_text = transcribe_audio(audio_input)
    else:
        response_text = input_text

    # Here, you could further process response_text to create chat logic
    
    # Convert text to speech
    text_to_speech(response_text, voice_option)
    
    return response_text


# Define Gradio Interface
iface = gr.Interface(
    fn=chat_function,
    inputs=[
        gr.Textbox(label="Text Input"),
        gr.Audio(label='Audio Input', type='filepath'),
        gr.Radio(label="Voice Option", choices=['default', 'realistic'])

    ],
    outputs=gr.Textbox(label="Response Text", type='auto')
)

if __name__ == "__main__":
    iface.launch()
