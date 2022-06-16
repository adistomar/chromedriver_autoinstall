# chromedriver_autoinstall
Automatically downloads the version of [ChromeDriver](https://chromedriver.chromium.org/downloads) compatible with the client's version of Chrome (currently supports MacOS and Windows).
Can be imported as a module and used to automatically reinstall ChromeDriver in its most updated/compatible version for any program that requires it.

## Install:
#### Python 3.6 or higher is required
```shell
pip install chromedriver_autoinstall
```

## Usage:
Write `import chromedriver_autoinstall` in your file, in the directory of which chromedriver will be installed.

## Quick Example:
```py
from selenium import webdriver
import os
import chromedriver_autoinstall
import time

PATH = "./chromedriver"
URL = "https://github.com/RoastSea8/chromedriver-autoinstaller"

def main():
    chromedriver_autoinstall.install()
    # os.chmod('./chromedriver', 0o755) # MacOS only
    driver = webdriver.Chrome(PATH)
    driver.get(URL)
    time.sleep(1000)

if __name__ == "__main__":
    main()
```

Linux support coming soon.
