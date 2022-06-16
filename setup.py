# coding: utf-8
from setuptools import setup


with open('README.md') as readme_file:
   long_description = readme_file.read()


setup(
   name="chromedriver_autoinstall",
   version="0.0.6",
   author="RoastSea8 (Aditya Tomar)",
   author_email="aditya26042005@gmail.com",
   description="Script to automatically install the ChromeDriver release compatible with the client's Chrome version.",
   license="MIT",
   keywords=['chromedriver', 'install', 'automation', 'autoinstall', 'autoinstaller', 'autoinstallscript', 'selenium'],
   url="https://github.com/RoastSea8/chromedriver_autoinstall",
   packages=["chromedriver_autoinstall"],
   entry_points = {
        'console_scripts': ['install_chromedriver=chromedriver_autoinstall.command_line:install_chromedriver'],
   },
   install_requires=['requests', 'bs4', 'lxml'],
   long_description_content_type="text/markdown",
   long_description=long_description,
   python_requires=">=3.6",
   classifiers=[
      "Development Status :: 4 - Beta",
      "Topic :: Software Development :: Testing",
      "Topic :: System :: Installation/Setup",
      "Topic :: Software Development :: Libraries :: Python Modules",
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Operating System :: MacOS :: MacOS X",
      "Operating System :: Microsoft :: Windows",
   ],
)