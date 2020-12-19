import pyttsx3, speech_recognition as sr, pyautogui
from colored import fg, attr

# Color Properties.
reset = attr('reset')
green = fg('green')
red = fg('red')
blue = fg('blue')
yellow = fg('yellow')
# Speaks The Audio.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


print(
    red + "_____________________________________________________________________Pyautogui - Module________________________________________________________________________" + reset)
print(
    green + "\nPyAutoGUI is a cross-platform GUI automation Python module for human beings.\n Used to programmatically control the mouse & keyboard.!!" + reset)
speak(
    'PyAutoGUI is a cross-platform GUI automation Python module for human beings.\n Used to programmatically control the mouse & keyboard.\n')
name1 = 'Kushal'.lower()  # Enter Your Name
greeting_phrases = ['Hello' + name1 + 'welcome to  pyautogui  module']
print(yellow + "Plese ask your command according to the below features:\n" + reset)
speak("Plese ask your command according to the below features:\n")
print('''
         1 : dragto(drag  mouse cursor)
         2 : maximize(maximize your window)
         3 : minimize(minimize your window)
         4 : current title(To Get Current window title) 
         5 : getalltitle(To getall the current opening application)
         6 : getinfo(To get all information about your window) 
         7 : size(To get  current window screen size)
         8 : position(To get exact screen position)
         9 : livemouseposition(To get the Live Mouse Position)
         10: move to(To get the specific point on your screen)
         11: click(This will perform the click task)

         ''')


# Hears to the User.
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(reset + '\n*\n' + blue + "\n  Listening...\n" + reset)
        speak('Listening')
        r.adjust_for_ambient_noise = 1.25
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print(green + "  Recognizing...\n" + reset)
        speak('Recognizing')
        query = r.recognize_google(audio, language='en-us')
        # print(f"  {name} Said : {red} {query}\n" + reset)
    except:
        return "©empty_^_^_queryª"
    return query


speak(greeting_phrases)
speak("How Can I Help You?")
if __name__ == "__main__":
    while True:

        query = command().lower()
        if '1' in query or 'dragto' in query or 'one' in query:
            print(" 'dragTo' command is used to drag  mouse cursor \n Please Wait! This Will Take a While")
            speak(" 'dragTo' command is used to drag  mouse cursor \n Please Wait! This Will Take a While")
            pyautogui.dragTo(300, 300, duration=4)
            print('As you saw it dragged the mouse cursor ')
            speak('As you saw it dragged the mouse cursor ')
        elif 'maximize' in query or 'two' in query  or '2' in query or 'maximize the window' in query:
            print(
                "You said maximize the window , if your window is already maximized then you can't \n able to see the changes because it already maximized \n if not then you can able to see your window screen automatically maximized")
            speak(
                "You said maximize the window ,if window is already maximized then you can't \n able to see the changes because it already maximized \n if not then you can able to see your window screen automatically maximized")
            pyautogui.getActiveWindow().maximize()
            print('As you saw it maximized your window screen')
            speak('As you saw it maximized your window screen')
        elif '3' in query  or 'three' in query or 'minimize the window' in query:
            print("You said minimize the window \n so it will minimize your current window")
            speak("You said minimize the window \n so it will minimize your current window")
            pyautogui.getActiveWindow().minimize()
            print('As you saw it minimized your window screen')
            speak('As you saw it minimized your window screen')
            # pyautogui.scroll(3000)
        elif '4' in query or 'four' in query or 'current title' in query:
            print(
                "You said Get Current window title the window \n so it will show the name of youe current window title")
            speak("You said Get Current window title \n so it will show the name of youe current window title")

            title = pyautogui.getActiveWindowTitle()
            print('This is your current window title\n', title)
            speak('This is your current window title' + title)

        elif '5' in query or 'five' in query or 'get all titles' in query:
            print("you said Get all titles \n so it will display all the current opening application")
            speak("you said Get all titles \n so it will display all the current opening application")
            getall = pyautogui.getAllTitles()
            print('This is your current opening all applications title\n', getall)
            speak('This is your current opening all applications')

        elif '6' in query or 'six' in query or 'getinfo' in query:
            print("you said Getinfo \n so it will display the all information about your window")
            speak("you said Getinfo \n so it will display the all information about your window")
            getinfo = pyautogui.getInfo()
            print('This is the info about your window\n', getinfo)
            speak('This is the info about your window')
            speak(getinfo)
        elif '7' in query or 'seven' in query or 'size' in query:
            print('you said size in your command \n so it will display your current window screen size')
            speak('you said size in your command \n so it will display your current window screen size')
            size = pyautogui.size()
            print("This is your current window size\n", size)
            speak("This is your current window size")
            speak(size)
        elif '8' in query or 'position' in query or 'eight' in query:
            print('you said position in your command \n so it will display the exact screen position')
            speak('you said position in your command \n so it will display the exact screen position')
            pos = pyautogui.position()
            print('This is the your exact screen position', pos)
            speak('This is the your exact screen position')
            speak(pos)
        elif '9' in query or 'livemouseposition' in query or 'live' in query:
            print('you said display mouse position in your command \n so it will display the Live Mouse Position')
            speak('you said display mouse position in your command \n so it will display the Live Mouse Position')
            pyautogui.displayMousePosition()
            print("Here is your live mouse position")
            speak("Here is your live mouse position")
        elif '10' in query or 'move to' in query:
            print("you said moveTo in your command\n so it will go to a specific point on your screen ")
            speak("you said moveTo in your command\n so it will go to a specific point on your screen ")
            # pyautogui(x,y,duration='')
            pyautogui.moveTo(0, 0, duration=1)
            print("This is your specific point on your screen")
            speak("This is your specific point on your screen")
        elif '11' in query or 'click' in query:
            print("you said click in your command\n so this will perform click task  ")
            speak("you said click in your command\n so this will perform click task  ")
            pyautogui.FAILSAFE = False
            pyautogui.click(x=0, y=0, button='right', clicks=3,
                            interval=4)  # This will click the right click button three times.
            print("As you saw in the top corner the performance of click \n that's how it works")
            speak("As you saw in the top corner the performance of click \n that's how it works ")


        else:

            print(red + "Please Check the command and according to this ask your queries" + reset)
            speak('Did not Get it!')
            speak("Please Check the command and according to this ask your queries")

