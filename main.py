def getVersion():
    return 1.0
def PrintVer():
    print(f"This is the {getVersion()} version!")
    input()
if __name__ == "__main__":
    from updater import Update
    resp = Update()
    print(f"This is version {getVersion()}!\n")
    if resp == True:print("Update installed.\nPress enter to exit.");input()
    else:print("No new updates available.\nPress enter to exit.");input()