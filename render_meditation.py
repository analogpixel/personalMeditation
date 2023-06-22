#!/usr/bin/env python

from yaml import load, FullLoader
import sys
import hashlib
import os
from elevenlabs import set_api_key, generate, save
from pydub import AudioSegment

set_api_key("elevenlabs_key_here")

fileName = sys.argv[1]
data = load(open(fileName,"r"), Loader=FullLoader )
title = fileName.split('.')[0].strip()

def render_say(text):
    text = text.strip()
    hash_object = hashlib.sha256()
    hash_object.update(text.encode('utf-8'))
    hash_hex = hash_object.hexdigest()

    if not os.path.exists('.cache'):
        os.mkdir('.cache')

    filename = f".cache/{hash_hex}.mp3"

    if not os.path.exists( filename):
        audio = generate(
                text = text,
                voice = "Bella",
                model = "eleven_monolingual_v1"
                )
        save(audio, filename)

    return filename


for meditation in data['meditation']:
    duration = meditation['duration']
    description = meditation['description']

    # create the segment everything will be layered ontop of
    meditation_audio = AudioSegment.silent(duration= duration * 60 * 1000 )

    print(duration, description)
    
    for section in meditation['section']:
        section_time = float(section['time'])
        if 'say' in section:
            filename = render_say( section['say'] )
            sound1 = AudioSegment.from_file(filename)

            if 'play_gain' in section:
                play_gain = int( section['play_gain'])
                sound1 = sound1 + play_gain 

            sound1 = sound1.fade_in(duration=500)
            meditation_audio = meditation_audio.overlay(sound1, position=section_time * 60 * 1000 )
        if 'play' in section:

            sound1 = AudioSegment.from_file( section['play'].strip() )
            if 'play_gain' in section:
                play_gain = int( section['play_gain'])
                sound1 = sound1 + play_gain 

            meditation_audio = meditation_audio.overlay(sound1, position=section_time * 60 * 1000)

    meditation_audio = meditation_audio.fade_out(duration=10000) 
    meditation_audio = meditation_audio.fade_in(duration=5000) 
    meditation_audio.export(f"meditations_output/{title}.mp3", format="mp3")

