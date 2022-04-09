tx = input("Text to say >>> ")
tx = repr(tx)

import os
import platform

syst = platform.system()
if syst == 'Linux' and platform.linux_distribution()[0] == "Ubuntu":
    os.system('spd-say %s' % tx)
elif syst == 'Windows':
    os.system('PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(%s);"' % tx)
elif syst == 'Darwin':
    os.system('say %s' % tx)
else:
    raise RuntimeError("Operating System '%s' is not supported" % syst)