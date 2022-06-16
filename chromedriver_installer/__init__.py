from chromedriver_installer import script
import os

def install():
   script.install()
   print(script.get_path())