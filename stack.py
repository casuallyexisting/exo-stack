from videoEngine.inference_final import main as vd
from vocalEngine.vox import generate
from inputEngine.stt import stt
import AVController as av
from threading import Thread
import socket
import warnings
import time
import torch
import json

# Load Config File
cfg = json.load(open("config.json"))

## system vars.
avLock = False
HOST = "127.0.0.1"
PORT = 25077

# Init.
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

# Function Definitions
def inputEngine():
    print('Listening...')
    response = stt()
    if response:
        return response
    else:
        raise RuntimeError('The input engine has encountered an error.')

def processEngine(data_in):
    print('processing data in core...')
    sock = socket.socket()
    sock.connect((HOST, PORT))
    outbound_message = 'STACK://' + data_in
    sock.sendall(outbound_message.encode('utf-8'))
    data = sock.recv(16384)
    ai_response = data.decode()
    sock.close()
    return ai_response

def vocalEngine(data_in):
    print('Vocalizing data...')
    generate(cfg['vocal_reference'], data_in, cfg['vocal_output'])

def videoEngine(data_in):
    global avLock
    avLock = True
    print('Visualizing data...')
    av.playFile(vd(cfg['video_checkpoint'], cfg['video_reference'], data_in))
    avLock = False

def idle():
    global avLock
    while True:
        if not avLock:
            avLock - True
            av.playFile(cfg['video_reference'], False)
            avLock = False

# Main Thread
if __name__ == '__main__':
    if cfg['audio_only'] == 0:
        Thread(target=idle).start()
    while True:
        input = inputEngine()
        input = processEngine(input)
        vocalEngine(input)
        torch.cuda.empty_cache()
        time.sleep(1)
        if cfg['audio_only'] == 0:
            videoEngine(cfg['vocal_output'])
            torch.cuda.empty_cache()
        else:
            av.audioHeadless(cfg['vocal_output'])
        time.sleep(3)
