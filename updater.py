import json,requests,os,sys;from colorama import Fore,Back
class Updater():
    json_url, current_version, optional_update, print_logs = "", 0.069, True, True
    def __init__(self, json_url:str, current_version:float, optional_update:bool, print_logs:bool) -> None:
        Updater.json_url, Updater.current_version, Updater.optional_update, Updater.print_logs=json_url, current_version, optional_update, print_logs
    def CheckUpdates(self):
        meta = json.loads(requests.get(Updater.json_url).text)
        try:lv=meta['latestVersion']
        except:Updater.error(self, "Latest version could not be read");return False
        if Updater.current_version < meta['latestVersion']: return True
        else: return False
    def ApplyUpdate(self):
        meta = json.loads(requests.get(Updater.json_url).text)
        if Updater.CheckUpdates(self):
            if Updater.optional_update:
                if not Updater.AskForConfirmation(self):return
            with open("main.py", "wb") as f:
                if meta['download'].endswith(".py"):
                    try:
                        f.write(requests.get(meta['download']).content)
                        if Updater.print_logs:
                            os.system("cls" if os.name=="nt" else "clear")
                            print(f"{Back.BLUE}Update installed successfully. Please close this window and restart the app.{Back.RESET}")
                    except:
                        Updater.error(self, "Unknown error while writing to `main.py`.");return
                    sys.exit(0)
                else:Updater.error(self, "Download link isn't a valid .PY file!")
    def AskForConfirmation(self):
        g = input("There is a new update available. Do you want to install it? ")
        yes = ['yes', 'y', 'ye', 'yeah', 'yep', 'yup', 'ok', 'sure']
        no = ['no', 'n', 'nope', 'nah']
        if g.lower().strip().replace(" ", "") in yes:
            return True
        elif g.lower().strip().replace(" ", "") in no:
            return False
        else:Updater.AskForConfirmation(self)
    def error(self, text):
        if Updater.print_logs: print(f"{Back.RED}{Fore.WHITE}Could not install update.\nError: {Fore.YELLOW}{text}{Fore.RESET}{Back.RESET}")