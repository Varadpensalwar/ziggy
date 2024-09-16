import os
import eel
import sys
import os

# Add the project root directory (ziggy) to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now the import should work
from engine.features import *



from engine.command import *

def start():
    eel.init("www")


    playAssistantSound()

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)