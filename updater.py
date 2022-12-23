def checkUpdates():
    import requests,json;from main import getVersion
    NewVersionUrl = "https://pastebin.com/raw/rBeWpLuR"
    updatePackageParams = json.loads(requests.get(NewVersionUrl).text)
    if getVersion() < updatePackageParams['newVersion']:
        with open("main.py", "wb")as f:f.write(requests.get(updatePackageParams['download']).content)
        return True
    else:return False

# Instructions:

# 1
# Make a pastebin where the information will be stored. example:
# {
# 	"newVersion": 1.1,
# 	"download": "https://URL/main.py"
# }
# NOTE: "download" should ONLY contain the main.py which the local one should be replaced with.

# 2
# add /raw/ between pastebin.com and the paste code: https://pastebin.com/raw/CODE

# 3
# Set up the versions in main.py

# 4
# Add updater.py and the code from main.py inside your python script then run the code