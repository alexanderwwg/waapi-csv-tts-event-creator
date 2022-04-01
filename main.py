from waapi import WaapiClient, CannotConnectToWaapiException
import os, pandas as pd, argparse
parser = argparse.ArgumentParser(description="Used to auto-fill notes in the Wwise Hierarchy.")
parser.add_argument('id', metavar='GUID', nargs='?', help="One guid of the form {01234567-89ab-cdef-0123-4567890abcde}. The script retrieves the current selected if no GUID specified.")

args = parser.parse_args()

# change the directory to local or to wherever you need it
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

# they are arrays for me to use in Waapi.
for x in names:
    print(x)
for x in line:
    print(x)


try:
    #connect to waapi
    client = WaapiClient()
    # NOTE: the client must be manually disconnected when instantiated in the global scope

except CannotConnectToWaapiException:

    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

else:

    # Callback function with a matching signature.

    # Signature (*args, **kwargs) matches anything, with results being in kwargs.

    def on_name_changed(*args, **kwargs):

        obj_type = kwargs.get("object", {}).get("type")

        old_name = kwargs.get("oldName")

        new_name = kwargs.get("newName")

        print("Object '{}' (of type '{}') was renamed to '{}'\n".format(old_name, obj_type, new_name))

        client.disconnect()


    handler = client.subscribe("ak.wwise.core.object.nameChanged", on_name_changed, {"return": ["type"]})

    print("Subscribed 'ak.wwise.core.object.nameChanged', rename an object in Wwise")