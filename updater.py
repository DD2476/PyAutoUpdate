def checkUpdates():
    import requests,json;from main import getVersion
    NewVersionUrl = "https://pastebin.com/raw/rBeWpLuR"
    updatePackageParams = json.loads(requests.get(NewVersionUrl).text)
    if getVersion() < updatePackageParams['newVersion']:
        with open("main.py", "wb")as f:f.write(requests.get(updatePackageParams['download']).content)
        return True
    else:return False