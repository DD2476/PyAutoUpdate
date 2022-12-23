<div align="center">
  
  # PyAutoUpdate 🎉
  
  > An auto-updater for python code, which fetches the new version from a cloud server.

  [![version](https://img.shields.io/github/v/release/Theta69/PyAutoUpdate?include_prereleases)]()
  [![size](https://img.shields.io/github/languages/code-size/Theta69/PyAutoUpdate)]()
  [![last commit](https://img.shields.io/github/last-commit/Theta69/PyAutoUpdate)]()
  
</div>

# How it works 🤯

> When you run `main.py`, **updater.py**/*Update()* gets called. Updater then uses **main.py**/*getVersion()* to get the installed version and compares it to the newest available version (which it gets from the JSON paste). If there is an update available, it downloads it.

# Instructions 🤔

1. Make a pastebin json containing the new version metadata.<br>
You will have to update this every time you release a new version.

```json
{
 "newVersion": 1.1,
 "download": "https://URL/main.py"
}
```

2. Copy the pastebin raw url (*add "/raw/" before the code*) and add it inside `updater.py`;
3. Fix versions or other information in the code to your liking;
4. Implement *updater.py* and the code from *main.py* inside your python script;
5. Test the code and fix it if something doesn't work.
