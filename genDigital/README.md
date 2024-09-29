selenium==4.0.0
webdriver-manager==3.4.2
imageio==2.9.0
numpy==1.21.0
mss==6.1.0
Prerequisites
To run the test_navigation.py Selenium tests on your local machine, follow the steps below based on your operating system:

General Requirements:
Python 3.x must be installed on your system.
Install necessary Python packages using pip

pip install -r requirements.txt

The requirements.txt should contain the following packages:
selenium
webdriver-manager
imageio
mss
imageio-ffmpeg

For Windows Users:
Install Python from the official Python website. Ensure that Python is added to the system PATH.
Install Google Chrome from here.
Install FFMPEG for video recording:
Download from FFMPEG's website and follow the installation steps.
Add the FFMPEG binary to your system PATH.

Run the tests
python -m unittest tests\test_navigation.py
or you can the test_navigation.py class by clicking on the play arrow

For macOS Users:
Install Python 3 using Homebrew
brew install python
nstall Google Chrome from here.
Install FFMPEG using Homebrew
brew install ffmpeg

Run the tests
python3 -m unittest tests/test_navigation.py

For Linux Users:
Install Python 3
sudo apt-get update
sudo apt-get install python3 python3-pip
Install Google Chrome:
sudo apt-get install -y google-chrome-stable
Install FFMPEG:
sudo apt-get install ffmpeg

Run the tests:
python3 -m unittest tests/test_navigation.py

