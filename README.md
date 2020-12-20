[![](https://img.shields.io/badge/Author-KushalDas-green.svg)](https://github.com/Kushal997-das)<br>
[![Hello programmer Welcome to this repo](https://img.shields.io/badge/Hello!-Welcometothisrepo-brightgreen.svg?style=flat&logo=github)](https://github.com/kushal997-das)
![](https://img.shields.io/badge/Programming_Language-Python-blue.svg)
![](https://img.shields.io/badge/Status-Complete-green.svg)
[![](https://img.shields.io/github/license/Kushal997-das/Pyautogui-module-using-audio.svg?style=plastic)](https://github.com/Kushal997-das/Pyautogui-module-using-audio)
[![](https://img.shields.io/github/languages/code-size/kushal997-das/Pyautogui-module-using-audio.svg?style=plastic)](https://github.com/kushal997-das/Pyautogui-module-using-audio)
[![](https://img.shields.io/github/languages/top/kushal997-das/Pyautogui-module-using-audio.svg?style=plastic)](https://github.com/kushal997-das/Pyautogui-module-using-audio)
[![GitHub issues](https://img.shields.io/github/issues/kushal997-das/Pyautogui-module-using-audio.svg)](https://github.com/kushal997-das/Pyautogui-module-using-audio/issues) [![GitHub forks](https://img.shields.io/github/forks/kushal997-das/Pyautogui-module-using-audio.svg)](https://github.com/kushal997-das/Pyautogui-module-using-audio/network) [![GitHub stars](https://img.shields.io/github/stars/Kushal997-das/Pyautogui-module-using-audio.svg)](https://github.com/kushal997-das/Pyautogui-module-using-audio/stargazers)
![GitHub contributors](https://img.shields.io/github/contributors/Kushal997-das/Pyautogui-module-using-audio)

<br>


PyAutoGUI
=========

> PyAutoGUI is a  cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard. <br>

Full documentation available at https://pyautogui.readthedocs.org


You Can Read Full documentation here : <a href="https://github.com/Kushal997-das/Pyautogui-module-using-audio/blob/master/documents/pyautogui-readbook.pdf"> documentation</a>

# Pyttsx3


> pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3. 

Full documentation available at https://pypi.org/project/pyttsx3/

# speech_recognition
> Speech recognition means that when humans are speaking, a machine understands it. speech recognition system needs to do is convert the audio signal into a form a computer can understand. 

Full documentation available at https://pypi.org/project/SpeechRecognition/

# colored

> Very simple Python library for color and formatting in terminal. Collection of color codes and names for 256 color terminal setups.

Full documentation available at https://pypi.org/project/colored/


Pre-requisites:
--------------
    Python3
    pyautogui
    pyttsx3
    speech_recognition
    colored
Installation:
------------

     $ pip install pyautogui
     $ pip install pyttsx3
     $ pip install SpeechRecognition
     $ pip install colored
     


### Importing module:
```python3
import pyautogui
import pyttsx3
import speech_recognition
import colored
```


## Mouse and keyboard automation using Python:
In this we know how to automate movements of mouse and keyboard using pyautogui module in python. 
```python
  import pyautogui
  screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
  currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
  pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
  pyautogui.click() # Click the mouse at its current location.
  pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
  pyautogui.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
  pyautogui.doubleClick() # Double click the mouse at the
  pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
  pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
  pyautogui.press('esc') # Simulate pressing the Escape key.
  pyautogui.keyDown('shift')
  pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
  pyautogui.keyUp('shift')
  pyautogui.hotkey('ctrl', 'c')
```

Display Message Boxes using pyautogui and pyttsx3 :
---------------------

```python3
import pyautogui,pyttsx3
# Speaks The Audio.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()    
speak('Hey! This is an alert box :')    
pyautogui.alert('This is an alert box :D.')
speak('Shall I proceed?')
pyautogui.confirm('Shall I proceed?')
speak(' Please Enter your option')
pyautogui.confirm('please Enter your option.', buttons=['K', 'L', 'P'])
speak('What is your name?')
speak('please Enter your name')
pyautogui.prompt('What is your name?')
speak("Enter password \n and don't worry text will be hidden")
pyautogui.password('Enter password (text will be hidden)')
speak('Thank You we save your details')

```

<img align='center' alt='Demo' width='300px' src="https://github.com/Kushal997-das/Pyautogui-module-using-audio/blob/master/documents/gif2.gif"/>

#### That's how the map look like after executing the code. <br>

Download full demo with audio from <a href="https://github.com/Kushal997-das/Pyautogui-module-using-audio/blob/master/documents/file.mp4">here</a>




Screenshot Functions using pyautogui :
--------------------


```python
import pyautogui
im1 = pyautogui.screenshot()
im1.save('my_screenshot.png')
im2 = pyautogui.screenshot('my_screenshot2.png')
```
You can also locate where an image is on the screen:
```python
import pyautogui
location = pyautogui.locateOnScreen('button.png') # returns (left, top, width, height) of matching region
print(location)
buttonx, buttony = pyautogui.center(button7location)
print(buttonx, buttony)
pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found
```

Final program:
----------------

### I used below functions with the all modules (pyautogui,pyttsx3,speech_recognition,colored)
  - 1 : dragto(drag  mouse cursor)
  - 2 : maximize(maximize your window)
  - 3 : minimize(minimize your window)
  - 4 : current title(To Get Current window title) 
  - 5 : getalltitle(To getall the current opening application)
  - 6 : getinfo(To get all information about your window) 
  - 7 : size(To get  current window screen size)
  - 8 : position(To get exact screen position)
  - 9 : livemouseposition(To get the Live Mouse Position)
  - 10: move to(To get the specific point on your screen)
  - 11: click(This will perform the click task)
         
Source code available at <a href='https://github.com/Kushal997-das/Pyautogui-module-using-audio/blob/master/pyauto.py'>  here </a> <br>
 
Watch full video https://youtu.be/ZLM7glLn7ls <br><br>

LICENSE:
---------
Copyright (c) 2020 Kushal Das

This project is licensed under the GNU General Public License v3.0
       


<br><br>

<p align="center">
  <b><i>Let's connect! Find me on the web.</i></b>

[<img height="30" src = "https://img.shields.io/badge/Youtube-%23E4405F.svg?&style=for-the-badge&logo=Youtube&logoColor=white">][Youtube] 
[<img height="30" src = "https://img.shields.io/badge/gmail-c14438?&style=for-the-badge&logo=gmail&logoColor=white">][gmail] 
[<img height="30" src="https://img.shields.io/badge/linkedin-blue.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />][LinkedIn]
[<img height="30" src="https://img.shields.io/badge/github-black.svg?&style=for-the-badge&logo=github&logoColor=white" />][Github]
<br />
<hr />

[youtube]: https://www.youtube.com/channel/UCIHj6mNCMnSnmWLHOxzIESw?view_as=subscriber
[gmail]: mailto:daskushal980@gmail.com
[linkedin]: https://www.linkedin.com/in/kushal-das-7337421a9/
[github]: https://github.com/Kushal997-das/

If you have any Queries or Suggestions, feel free to reach out to me.

<h3 align="center">Show some &nbsp;❤️&nbsp; by starring some of the repositories!</h3>
