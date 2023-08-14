# chromedriver_autoinstall
Automatically downloads the version of [ChromeDriver](https://chromedriver.chromium.org/downloads) compatible with the client's version of Chrome. Supports all versions of Chrome.
Can be imported as a module and used to automatically reinstall ChromeDriver in its most updated/compatible version for any program that requires it.

## Install:
#### Python 3.6 or higher is required
```shell
pip install chromedriver_autoinstall
```

## Usage:
- To download chromedriver in the current directory, run `install_chromedriver`.
- To use the autoinstaller as part of a program, write `import chromedriver_autoinstall` in your file. See the [example below](https://github.com/RoastSea8/chromedriver-autoinstall#quick-example) for this use case.

## Quick Example:
```py
from selenium import webdriver
import os
import chromedriver_autoinstall
import time

PATH = f"./chromedriver-{chromedriver_autoinstall.get_platform()}/chromedriver"
URL = "https://github.com/RoastSea8/chromedriver_autoinstall"

def main():
    chromedriver_autoinstall.install()
    # chromedriver_autoinstall.script.out(f"chmod +x {PATH}") # MacOS only
    # os.chmod(PATH, 0o755) # MacOS only
    driver = webdriver.Chrome()
    driver.get(URL)
    time.sleep(1000)

if __name__ == "__main__":
    main()
```