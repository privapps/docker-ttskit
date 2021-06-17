#!/usr/bin/python3

##############################################
# File: /workspace/__input__.txt contains text need to be convert
# File: /workspace/__voice__.txt is optional with number only, which indicate which voice to use
# File: /workspace/__out__.wav is the one will be generated
##############################################                                                                                                                                                            
import ttskit, sys

def getVoice(default_val = 24) -> int:
    try:
        with open('/workspace/__voice__.txt', 'rt') as f:
            lines = f.readlines()
        num = int(''.join(lines))
        return num if num > 0 and num <= 30 else default_val
        return num
    except Exception:
        return default_val

with open('/workspace/__input__.txt', 'rt') as f:
    lines = f.readlines()
wav=ttskit.tts(' '.join(lines),audio=str(getVoice()))

file_name='/workspace/__out__.wav'
with open(file_name, "wb") as f:
    f.write(wav)