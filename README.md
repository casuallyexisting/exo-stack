# Exo Stack

Exo Stack is an audiovisual way to interface with an exo AI, and includes speech-to-text as an input to enable 'conversations' with the AI.

## Installation
- Clone the repository
- Add a (short) video or a picture to the folder
- Add a short audio clip of a voice to the folder
- Edit the config, and set the video and vocal references
- Download the Video Engine checkpoint from [here](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/Eb3LEzbfuKlJiR600lQWRxgBIY27JZg80f7V9jtMfbNDaQ?e=TBFBVW) and put it in the folder 'videoEngine/checkpoints'
- Download the Vocal Engine checkpoints from [here](https://github.com/blue-fish/Real-Time-Voice-Cloning/releases/download/v1.0/pretrained.zip), and extract them here:
```
encoder\saved_models\pretrained.pt
synthesizer\saved_models\pretrained\pretrained.pt
vocoder\saved_models\pretrained\pretrained.pt
```

## Usage
- NOTE: Core has to be running (from the exo repo) for this to connect.
```shell
python stack.py
```

## Contributing
Contributing is greatly appreciated, please contact one of the team members to get started working on the codebase.

## Todo
### Stack
- Fix memory issue, find a way to limit GPU memory usage.
### Vocal Engine
- Update to TF 2
- Fix security vulnerabilities
- Finish properly training the model
### Input Engine
- Find a better (but still free) way to do voice recognition
### Video Engine
- Speed up rendering, find a better sample file to use as the face
