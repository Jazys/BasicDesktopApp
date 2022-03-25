#About project

This project is a minimal boilerplate for creating minimal desktop (exe) with
- several html file to have a beautiful Gui
- aiohttp server to get all REST API
- socketIO to have event communication
- a desktop Gui

==> All in one exe and website file !

Use at leat python 3.8 for this project.

When the project is running, an minimal windows appears (only use to remember and quit) and a browser is
launch with the good url to display the final UI.

#Installation
Create a virtual env in directory

``
python3 -m venv .
``

Enable it :

``
source venv/bin/activate
``

Install all dependencies :

``
pip3 install -r requirements
``

#Configuration

Only specify the http port in main.py

#To create exe file

On windows run this command :

To have an unique exe file :

``
pyinstaller --hidden-import python-engineio --hidden-import python-socketio --hidden-import aiohttp --hidden-import engineio.async_drivers.aiohttp --hidden-import engineio.async_aiohttp --clean --noconfirm --onefile -w main.py
``

To have a folder containing dll and more :

``
pyinstaller --hidden-import python-engineio --hidden-import python-socketio --hidden-import aiohttp --hidden-import engineio.async_drivers.aiohttp --hidden-import engineio.async_aiohttp --clean --noconfirm -w main.py
``