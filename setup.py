from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.20'
DESCRIPTION = 'a scrpit to get all the links about peaple who are intersted by given keyword'
LONG_DESCRIPTION = 'a scrpit to get all the links about peaple who are intersted by given keyword'

# Setting up
setup(
    name="linkedin_information_collections_scraper",
    version=VERSION,
    author0="NeuralNine (Florian Dedov)",
    author_email="<abdelaziz.naija@horizon-tech.tn>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)