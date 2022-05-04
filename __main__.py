import subprocess,os, pandas as pd, argparse

from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

from tkinter.filedialog import askopenfilename

user_input = askopenfilename()

if os.path.exists (user_input):
    name, extension = os.path.splitext(user_input)
    if extension == ".csv":
        pass
else: exit()

# use pandas to read and output a list for me
fileName = pd.read_csv(user_input, usecols = [1])
names = list(fileName.values.flatten())
dialogue = pd.read_csv(user_input, usecols = [2])
line = list(dialogue.values.flatten())

pathList = []

script_dir = os.path.dirname(os.path.realpath(__file__))
speak_script_path = os.path.join(script_dir, 'speak.ps1')


filePath = os.path.join(os.path.dirname(os.path.realpath(__file__)) + "\export")
pathExists = os.path.exists(filePath)
if not pathExists:
    os.makedirs(filePath)

for item in names:
    wav_file = os.path.join(filePath, item ) + ".wav"
    print(wav_file)
    subprocess.check_output(["powershell.exe", '-executionpolicy', 'bypass', '-File', speak_script_path, wav_file, line[names.index(item)]])
    pathList.append(wav_file)

# Audio File    Object Path     Object Type     Notes   Event
dfList = []

# Change the DF List appending stuff as necessary!
for item in pathList:
    dfList.append([item,
                   "\Actor-Mixer Hierarchy\Default Work Unit\<Actor-Mixer>VO\\" +  names[pathList.index(item)],
                  "Sound Voice",
                  line[pathList.index(item)],
                  "\Events\Default Work Unit\VO\\" + names[pathList.index(item)] + "@Play"])

df = pd.DataFrame(dfList, columns=["Audio File", "Object Path", "Object Type", "Audio Source Notes", "Event"])


df.to_csv("wwiseImport.tsv", index=False, sep="\t", na_rep ='')
csvPath = os.path.join(script_dir + "\wwiseImport.tsv")

try:
    with WaapiClient() as client:
        args = {
            "importLanguage": "English(US)",
            "importOperation": "useExisting",
            "importFile": csvPath
        }
        client.call("ak.wwise.core.audio.importTabDelimited", args)

except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

except Exception as e:
    print(str(e))