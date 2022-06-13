CSV to TTS TSV Exporter

This program will
1. Ask for a .csv file that reads COLUMN 2(Name of the VO file) and COLUMN 3(Line of the VO file)
2. Generates placeholder VO files using tts
3. Generates a TSV with headers :["Audio File", "Object Path", "Object Type", "Audio Source Notes", "Event"], 
allowing the user to import tab delimited into Wwise immediately.
4. Waapi will import this TSV immediately.
A folder will be made (named export) inside the folder where the exe is run.
A .tsv file (wwiseImport.tsv) will be made inside the folder where the exe is run.
Idea was done and referenced from https://github.com/ak-brodrigue/waapi-python-tools/tree/master/text-to-speech


============================================================
PLEASE READ BEFORE USING:

CSV FORMAT:
--HEADERS--
Index, File Name, Dialogue content

!!!!!! DO NOT LEAVE VALUES BLANK!!! !!!!!!
DO NOT USE SPECIAL CHARACTERS IN YOUR FILE NAME
LIKE !@#$%%^&*().

A good example of a file name can be
VO_NAME_001
=============================================================
INSTRUCTIONS

ENSURE THAT YOU HAVE THESE PATHWAYS IN WWISE
Audio: \Actor-Mixer Hierarchy\Default Work Unit\<Actor-Mixer>VO
Events: \Events\Default Work Unit\VO\ (VO IS A WORK UNIT)
1. Launch CSV-to-TTS-TSV-Exporter.exe
2. It will launch a cmd window- and a pop up will ask you for a file path.
3. Put in a .csv file. There's an example.csv file outside the exe folder you can use.
4. VO files will be generated inside \CSV-to-TTS-TSV-Exporter\export
5. A .tsv file will be generated inside \CSV-to-TTS-TSV-Exporter.
6a. If Wwise is open, it will import all the files created into 
Audio: \Actor-Mixer Hierarchy\Default Work Unit\<Actor-Mixer>VO
Events: \Events\Default Work Unit\VO\ (VO IS A WORK UNIT)
6b. If Wwise is not open, the program will terminate.


