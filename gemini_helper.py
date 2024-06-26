import os
import google.generativeai as genai
from google.cloud import texttospeech
from dotenv import load_dotenv
from gtts import gTTS

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """
The user is blind, So You have to give proper description of that picture.
Use english language to answer the blind user.
"""

client = texttospeech.TextToSpeechClient()


def read_image(image_data):
    model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')
    response = model.generate_content([image_data, prompt])
    text_to_speech(response.text)
    return response.text


# def text_to_speech(text, language='en'):
#     tts = gTTS(text=text, lang=language)
#     tts.save("description.mp3")

def text_to_speech(text, language='en-US'):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code=language,
        name="en-US-Studio-O",
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        speaking_rate=1
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open("description.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

