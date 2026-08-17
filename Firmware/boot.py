import storage
import usb_cdc
import json

usb_cdc.enable(console=True, data=True)

with open("/conf.json") as f:
    data = json.load(f)

if not data["storage"]:
    storage.disable_usb_drive()
