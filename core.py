import os
from pyowm import OWM
import speech_recognition as sr
from fuzzywuzzy import fuzz
from time import sleep
from termcolor import colored, cprint
import pyttsx3
import requests
import datetime
import webbrowser
import random
import numpy
import functools
import pyperclip
import getpass
import ui_hook
import threading
import keyboard
import re
from playsound import playsound
import wmi # Core temp
import wikipedia
file_name = os.path.basename(__file__)
database_path = os.path.realpath(__file__).replace(file_name, "notifications_database")
dir_path = os.path.realpath(__file__).replace(file_name, "")

paused = False
need_to_listen = False
line_hotkeys_enabled = True
device_index = 1
city = 'Симферополь'

opts = {
    "alias":  ('слушай', 'эй'),
    "tbr":    ('скажи', 'расскажи', 'покажи', 'произнеси'),
    "cmds": {
        "ctime":                   ('текущее время', 'сейчас времени', 'который час', 'сколько время'), #
        "weather":                 ('какая погода', 'погода сегодня'), #
        "count":                   ('сколько будет', 'посчитай'), #
        "write":                   ('напечатай', 'напиши', 'напечатать', 'написать'), #
        "lock":                    ('заблокировать', 'выйти из сеанса'), #
        "copy":                    ('скопировать', 'скопируй'), #
        "clear_notifications":     ('убрать напоминания', 'отменить напоминания'), #
        "idk":                     ('простите я вас не понимаю', 'не понимаю'), #
        "notify":                  ('напомнить', 'создать напоминание', 'напомни', 'напомни пожалуйста'), #
        "line":                    ('открыть строку', 'открыть поиск'), #
        "what_is":                 ('что такое', 'значение слова', 'кто такой'),
        "settings":                ('открыть настройки', 'настройки приложения'), #
        "shutdown":                ('завершение работы', 'выключить компьютер'), #
        "shutdown_cancel":         ('отмена', 'не выключать компьютер'), #
        "restart":                 ('перезагрузить', 'перезагрузить компьютер', 'перезагрузить компьютер', 'перезагрузка компьютера'), #
        "thanks":                  ('благодар ю', 'спасибо', 'классно'), # Deprecated
        "browser_search":          ('искать в браузере', 'искать в интернете', 'ищи в браузере', 'ищи в интернете', 'поиск в интернете') #
    }
}

# Upload new notifications to database from file
def update_notifications():
    global database_path
    global notifications

    notifications = numpy.load( database_path + ".npy", allow_pickle=True ).item()
    ui_hook.update_notifications(database_path)

# Add notification to the database
def add_notification( time, message ):
    global database_path
    global notifications

    # Decorate message
    message = 'Напоминание: ' + message.capitalize() + '.'

    if(notifications.get(time)):
        old_message = notifications.get( time )
        notifications.update( {time: old_message + ' ' + message} )
    else:
        notifications.update( {time: message} )

    numpy.save( database_path+".npy", notifications )
    update_notifications()

# Delete all notifications ( clear dictionary )
def clear_notifications():
    global notifications
    global database_path

    notifications.clear()
    numpy.save( database_path+".npy", notifications )
    update_notifications()

# Notifications handle loop
def wait_for_notifications():
    global notifications

    print(' [log] Waiting for notification trigger...' )
    while( True ):
        now = datetime.datetime.now()
        current_time = str(now.hour) + ':' + (str(now.minute) if len(str(now.minute)) > 1 else '0' + str(now.minute))
        if(current_time in notifications):
            speak( notifications.pop(current_time) )
        sleep(10)

# Make decorator witch makes function synchronized
def synchronized(wrapped):
    lock = threading.Lock()
    @functools.wraps(wrapped)
    def _wrap(*args, **kwargs):
        with lock:
            return wrapped(*args, **kwargs)
    return _wrap

# Stop main thread until user's input
def listen():
    global audio
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise( source, duration=0.2 )
        print(" [log] Listening...")
        r.pause_threshold = 0.5
        r.non_speaking_duration = 0.5
        audio = r.listen(source)
        if need_to_listen:
            callback(r, audio)


# Say any text message
@synchronized
def speak(message):
    global speak_engine
    print(" [log] Speak: ", message)
    speak_engine.say(message)
    speak_engine.runAndWait()
    speak_engine.stop()
    ui_hook.append_log("PowerBox >> " + str(message))

# Open powerline
def show_line(with_hotkeys, hotkey_id):
    global line_hotkeys_enabled

    print(" [log]: Line opened. With hotkeys: "+str(with_hotkeys))

    if( with_hotkeys ):
        if(line_hotkeys_enabled):
            print(hotkey_id)
            powerline_path = os.path.realpath(__file__).replace("core.py", "") + "Powerline.exe"
            os.system(powerline_path)
    else:
        powerline_path = os.path.realpath(__file__).replace("core.py", "") + "Powerline.exe"
        os.system(powerline_path)


def set_property( property_name, new_state ):
    cprint( " [log] Changed property: "+str(property_name)+", value = "+str(new_state),'green' )
    if( property_name == 'pause' ):
        global paused
        paused = new_state
    elif(property_name == 'need_to_listen'):
        global need_to_listen
        need_to_listen = new_state
        if need_to_listen:
            playsound(dir_path+'\enable.wav')
        else:
            playsound(dir_path+'\disable.wav')
    elif( property_name == 'volume' ):
        # Set volume ( 0 - 1 )
        global volume

        volume = new_state / 100
        speak_engine.setProperty('volume', volume)
    elif( property_name == 'line_hotkeys_enabled' ):
        # Enable or diasble hotkeys to call 'line'
        global line_hotkeys_enabled
        line_hotkeys_enabled = new_state
    elif( property_name == 'city' ):
        # Set city name to show weather
        global city
        city = new_state
    elif( property_name ==  'device_index' ):
        # Set system index of microphone
        global device_index
        global mic
        global r
        device_index = new_state
        mic = sr.Microphone( device_index=device_index )
        with mic as source:
            r.adjust_for_ambient_noise( source )


def check_city_is_avaliable(city_name):
    try:
        global owm
        obs = owm.weather_at_place(city_name)
        w = obs.get_weather()

        return True
    except Exception as e:
        print(e)
        return False

# Choose: known input or no
def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        ui_hook.append_log(getpass.getuser()+((8-len(list(getpass.getuser())))*' ')+" >> "+voice.capitalize())
        print(" [log] Распознано: "+voice)

        cmd = voice

        for x in opts['tbr']:
            cmd = cmd.replace(x, "").strip()

        cmd = recognize_cmd(cmd)
        if cmd['percent'] > 66:
            execute_cmd(cmd['cmd'], voice)
        else:
            speak("Простите, я вас не понимаю.")

    except sr.UnknownValueError:
        print(" [log] Голос не распознан!")
    except sr.RequestError as e:
        print(" [log] Ошибка сети")

# Uncorrect recognization
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
            if x in cmd:
                RC['cmd'] = c
                RC['percent'] = 95
    return RC

# Execute correct command
def execute_cmd(cmd, parameter):
    print(" [log] Execute: ", cmd)

    # Say current time
    if cmd == 'ctime':
        now = datetime.datetime.now()
        speak('Сейчас ' + str(now.hour) + ':' + (str(now.minute) if len(str(now.minute)) > 1 else '0' + str(now.minute)))

    # Turn off computer ( 1 min delay )
    elif cmd == 'shutdown':
        os.system('shutdown -s')
        speak('Выключаю. Вы можете отменить это действие.')

    # Do not turning off computer
    elif cmd == 'shutdown_cancel':
        os.system('shutdown -a')
        speak('Отменяю завершение работы.')

    # Restart computer
    elif cmd == 'restart':
        os.system('shutdown -r')
        speak('Перезагружаю. Вы можете отменить это действие.')

    # Lock current session
    elif cmd == 'lock':
        os.system('rundll32 user32.dll LockWorkStation')

    # Copy input to clipboard
    elif cmd == 'copy':
        pyperclip.copy(parameter.replace('скопировать', '').replace('скопируй', '').strip())

    elif cmd == 'clear_notifications':
        clear_notifications()
        speak("Готово.")

    # Notify user in future for sth
    elif cmd == 'notify':
        for i in opts['cmds'].get("notify"):
            parameter = parameter.replace(i, '').strip()
        try:
            time = parameter.split(' ')[-1]
            parameter = parameter.replace(time, '').strip()
            #if parameter.split(' ')[-1] == "в ":
            #    parameter = parameter.replace(parameter.split(' ')[-1], '').strip()
            parameter = parameter[:-2]
            notify_message = parameter
            add_notification(time,notify_message)
            speak("Хорошо, напомню '"+notify_message+"' в "+time)
        except Exception as e:
            speak("Ошибка: не удалось создать напоминание "+str(e))
            raise e

    # Say current weather
    elif cmd == 'weather':
        global owm
        try:
            weather = dict()

            obs = owm.weather_at_place(city)
            w = obs.get_weather()

            weather['temp'] = round(w.get_temperature(unit='celsius')['temp'])
            weather['status'] = w.get_detailed_status()
            weather['pressure'] = (str(round(w.get_pressure()['press']*0.750063755419211)))  # гПа -> мм.р.с
            p1 = [0, 5, 6, 7, 8, 9]
            if int(weather['pressure']) % 10 in p1:
                weather['pressure'] = str(weather['pressure']).__add__(" миллиметров")
            elif int(weather['pressure']) % 10 == 1:
                weather['pressure'] = str(weather['pressure']).__add__(" миллиметр")
            else:
                weather['pressure'] = str(weather['pressure']).__add__(" миллиметрa")
            weather['pressure'] = weather['pressure'].__add__(" ртутного столба")

            weather['humidity'] = str(w.get_humidity()) + "%"
            speak("В городе "+city+" сейчас {1} , температура: {0}°. Влажность: {2}".format(weather['temp'],
                    weather['status'], weather['humidity']))
        except Exception as e:
            print(str(e))


    # Write input to current input line
    elif cmd == 'write':
        w_request = parameter
        for i in opts['cmds'].get("write"):
            w_request = w_request.replace(i, '')
        keyboard.write(w_request.strip())

    # Open powerline
    elif cmd == 'line':
        show_line(False, 0)

    # Read 2 first centences from wikipedia
    elif cmd == 'what_is':
        pattern = "\({1}[^)]*\){1}"
        request = parameter
        for i in opts['cmds'].get("what_is"):
            request = request.replace(i, '').strip()
        try:
            sentences = 2
            text = wikipedia.summary(request, sentences=sentences)
            while(len(text) < 120):
                sentences += 1
                text = wikipedia.summary(request, sentences=sentences)
            to_remove = re.findall(pattern, text)
            print('Removed:',to_remove)
            for r in to_remove:
                text = text.replace(r,'').strip()
            speak(text)
        except Exception as e:
            speak('Простите. Не удалось найти информацию об этом.')

    # Open dialog
    elif cmd == 'settings':
        ui_hook.init()

    # Evaluate math request
    elif cmd == 'count':
        removed = ('сколько будет', 'посчитай')
        math_request = parameter.replace(removed[0], '').replace(removed[1], '').replace('разделить на', '/').replace('умножить на', '*').replace('в квадрате', '** 2').replace('в кубе', '** 3').replace('в степени', '**').replace('плюс', '+').replace('минус', '-').replace("х", "*").replace('два', '2').replace('три', '3').replace('четыре', '4').strip()
        try:
            speak(str(round(eval(math_request), 4)))
        except Exception as e:
            speak("Простите, я не могу это посчитать.")
            print(math_request, " ", e)

    # Search in browser
    elif cmd == 'browser_search':
        ress = list(parameter.split(' '))
        not_request = ('искать', 'поиск', 'интернете', 'браузере')
        for i in ress:
            for j in not_request:
                if fuzz.ratio(i, j) > 60:
                    for h in range(0, ress.index(i) + 1):
                        ress[h] = ''
        web_request = "https://yandex.ru/search/?text="
        for l in ress:
            web_request += l+"%20"
        webbrowser.open( web_request )

    # Say thanks
    elif cmd == 'thanks':
        pass
        # Deprecated
        #speak( 'И Вам спасибо' )

print(" [log] PowerBox core is running!")

# Init speak engine
speak_engine = pyttsx3.init()
speak_engine.setProperty('voice', 'ru') 

try:
    # Init recognizer
    r = sr.Recognizer()

    # Init microphone
    print("Device: "+str(sr.Microphone.list_microphone_names()[device_index]))

    mic = sr.Microphone( device_index=device_index )
    with mic as source:
        r.adjust_for_ambient_noise( source )
except Exception as e:
    print(e)
    speak("Ошибка: микрофон не подключен. Модуль голосовой ассистент не может работать без микрофона.")



# Pre-init ui
ui_hook.pre_init( set_property, check_city_is_avaliable )
ui_init = True

# Clear console
os.system('cls')

# Print pretty banner
banner = ["""
    =---------------------------------- Welcome to --------------------------------------=
                                                                                    """, """
             ██████╗  ██████╗ ██╗    ██╗███████╗██████╗ ██████╗  ██████╗ ██╗  ██╗
             ██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝
             ██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝██████╔╝██║   ██║ ╚███╔╝
             ██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║ ██╔██╗
             ██║     ╚██████╔╝╚███╔███╔╝███████╗██║  ██║██████╔╝╚██████╔╝██╔╝ ██╗
             ╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                                    """, """
    =------------------------------------------------------------------------------------=
                                                                                    """]
cprint( banner[0],  'white' )
cprint( banner[1],  'cyan'  )
cprint( banner[2],  'white' )

# Init pyowm lib
owm = OWM('e3b69afc0e2c681527fee196cf54144d', language="RU")

# Notifications database
notifications = dict()
update_notifications()

# Hotkeys to call "line"
h = 0
keyboard.add_hotkey( 'Ctrl + Space', lambda: show_line(True, random.randint(0, 10000)))
h += 1
keyboard.add_hotkey( 'Shift + Space', lambda: show_line(True, random.randint(0, 10000)))

# Print cached notifications
print(' [log] Loaded notifications: ', notifications )

# Thread for infinite loop ( notifications handler )
event = threading.Event()
infinite_loop = threading.Thread( target=wait_for_notifications )
infinite_loop.start()

# Wikipedia API config
wikipedia.set_lang("ru")


def listen_from_frame_utils():
    global need_to_listen
    set_property('need_to_listen', not need_to_listen)


def init_frame_utils():
    global listen_from_frame_utils
    listen_from_frame_utils()
    import frame_utils
    frame_utils.init_listen_func(listen_from_frame_utils)


event1 = threading.Event()
frame_utils_thread = threading.Thread( target=init_frame_utils )
frame_utils_thread.start()


while True:
    if need_to_listen:
        try:
            listen()
        except:
            pass
    sleep(0.05)

"""
# Begin main loop
speak( "Приветствую. Я Вас слушаю" )
#execute_cmd( 'settings', '' )
while (True):
    try:
        listen()
    except Exception as e:
        print(e)

# Exit
infinite_loop.stop()
"""
