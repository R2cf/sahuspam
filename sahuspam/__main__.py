import sys
import glob
import importlib
import logging
from pathlib import Path
from sys import argv
from sahuspam import *
from sahuspam import SpamBot1, SpamBot2, SpamBot3, SpamBot4, SpamBot5

def load_plugs(plugname):
    modules = Path(f"sahuspam/plugins/{plugname}.py")
    myfiles = f"sahuspam.plugins.{plugname}"
    spec = importlib.util.spec_from_file_location(myfiles, modules)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugname)
    spec.loader.exec_module(load)
    sys.modules["sahuspam.plugins." + plugname] = load
    print("Sahu Spam Bot ⚡ - Successfully Imported " + plugname)

if __name__ == "__main__":
    modules = "sahuspam/plugins/*.py"
    plugins = glob.glob(modules)
    for myfiles in plugins:
        with open(myfiles) as f:
            module = Path(f.name)
            plugname = module.stem
            load_plugs(plugname.replace(".py", ""))

import sahuspam
import sahuspam.userNeeds
import sahuspam.help
import sahuspam.helpers.callbackQuery

print("\n\nSahu Spam Bot Deployed Successfully! ❤️⚡🔥 \n\n")
print("\n\n For future updates, Join @vijaysahu_1 🔥\n\n")

if len(argv) not in (1, 3, 4):
    try:
        SpamBot1.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot2.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot3.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot4.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot5.disconnect()
    except Exception as e:
        print(e)
        pass
else:
    try:
        SpamBot1.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot2.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot3.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot4.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot5.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
