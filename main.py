from aiohttp import web
import socketio
import webbrowser
import json
import tkinter as tk
import threading
import os
import signal
import subprocess

PORT=8086

#Initialisation
guiApp = tk.Tk()
sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

#To kill App when clicking on Quit button in GUI
def quitAppAndGui():
    guiApp.destroy()
    os.kill(signal.CTRL_C_EVENT, 0)
    exit()

#To handle web request with some example
async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

async def quitApp(request):
    """Serve the client-side application."""
    exit()

async def jsonExample(request):
    response_obj = { 'status' : 'success' }
    return web.Response(text=json.dumps(response_obj))

async def executeCmd(request):
    out, err=runcmd("dir")
    return web.Response(text=str(out))

#use for socketio
@sio.event
async def connect(sid, environ):
    await sio.emit('toto', {'response': 'my response'})
    print("connect ", sid)


@sio.event
async def message(sid, data):
    print("message ", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

#
def runcmd(cmd):
    x = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    return x.communicate()


#Set route for http server
app.router.add_static('/assets', 'assets')

app.router.add_get('/', index)
app.router.add_get('/quitApp', quitApp)
app.router.add_get('/jsonExample', jsonExample)
app.router.add_get('/executeCmd', executeCmd)

#Define the function to start the thread

def thread_fun():
    # launch REST and SocketIo service
    web.run_app(app, port=PORT)


if __name__ == '__main__':

    # open a broswer
    webbrowser.open("http://127.0.0.1:"+str(PORT), new=0, autoraise=True)

    #Create Simple Gui
    label = tk.Label(guiApp, text="App!")
    label.pack()
    bouton = tk.Button(guiApp, text="Quitter", fg="red", command = quitAppAndGui)
    bouton.pack()

    #To launch web server
    b1 = tk.Button(guiApp, text="Start", command=threading.Thread(target=thread_fun).start())

    guiApp.mainloop()




#pyinstaller --hidden-import python-engineio --hidden-import python-socketio --hidden-import aiohttp --hidden-import engineio.async_drivers.aiohttp --hidden-import engineio.async_aiohttp --clean --noconfirm --onefile -w main.py

