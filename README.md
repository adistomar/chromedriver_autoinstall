# chromedriver-autoinstaller
Automatically downloads the version of [ChromeDriver](https://chromedriver.chromium.org/downloads) compatible with the client's version of Chrome (currently supports MacOS and Windows).
Can be imported as a module and used to automatically reinstall ChromeDriver in its most updated/compatible version for any program that requires it.

## Usage:
Import the `script` module and run `script.install()`

## Example:
```py
from selenium import webdriver
import os
import script
import time

PATH = "./chromedriver"
URL = "https://github.com/RoastSea8/chromedriver-autoinstaller"

def main():
    script.install()
    # os.chmod('./chromedriver', 0o755) # MacOS only
    driver = webdriver.Chrome(PATH)
    driver.get(URL)
    time.sleep(1000)

if __name__ == "__main__":
    main()
```

Linux support coming soon.
