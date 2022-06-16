from chromedriver_autoinstall import script
import os

def install_chromedriver():
   script.install()
   path = os.path.abspath(os.getcwd())
   print(f"install path: {path}")