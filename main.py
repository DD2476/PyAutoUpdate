from updater import Updater
updater = Updater(
    json_url="https://pastebin.com/raw/Gt0xsQqK",
    current_version=1.0,
    optional_update=True,
    print_logs=False
    )
updater.CheckUpdates() #ApplyUpdate() also checks for updates, therefore this is unnecessary when only installing an update
updater.ApplyUpdate()