#!/usr/bin/python3

##############################################
# File: /workspace/__input__.txt contains text need to be convert
# File: /workspace/__voice__.txt is optional with number only, which indicate which voice to use
# File: /workspace/__out__.wav is the one will be generated
##############################################                                                                                                                                                            
import ttskit, sys, os

text = os.environ["INPUT_TEXT"]
voice = os.environ["INPUT_VOICE"]
wave_path = os.environ["INPUT_CONTENT"]

def getVoice(default_val = 24) -> int:
    try:
        num = int(voice)
        return num if num > 0 and num <= 30 else default_val
        return num
    except Exception:
        return default_val

		
wav=ttskit.tts(text,audio=str(getVoice()))

with open(wave_path, "wb") as f:
    f.write(wav)