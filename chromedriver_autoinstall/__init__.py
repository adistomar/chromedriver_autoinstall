from chromedriver_autoinstall import script
import os

def install():
   script.install()
   print(script.get_path())