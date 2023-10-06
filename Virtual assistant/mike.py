import pyttsx3
import pyaudio
import websockets
import json
import asyncio
import base64
engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hello! Faizan!       are     you       doing    ok?")
engine.runAndWait()