import string
import PySimpleGUI as Sg
from pathlib import Path
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from first_script import *

def is_valid_path(filepath):
    if filepath and Path(filepath).exists():
        return True
    Sg.popup_error("filepath not correct")
    return False

def main_window():
    # menu define
    menu_def = [
        [
            "Toolbar",
            ["Commingsoon", "Commingsoon"]
        ],
        [
            "Help",
            [ "About", "Exit"]
        ],
    ]

    # gui define
    layout = [

        
        [Sg.MenubarCustom(menu_def, tearoff=False)],
        [Sg.Text('Progress:')],
        [
            Sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS-')
         ],
        [
            Sg.Text("input file:"),
            Sg.Input(key="-IN-"),
            Sg.FileBrowse(
                file_types=(("text files", "*.txt*"),)
            )
        ],
        [
            Sg.Text("output folder:"),
            Sg.Input(key="-out-" , default_text=str(Path.cwd())),
            Sg.FolderBrowse( )
        ],
        [
            Sg.Exit(),
            Sg.Button("Check File")
        
        ],
        
    ]
    

    window_title = settings["GUI"]["title"]
    window = Sg.Window(window_title, layout, use_custom_titlebar=True)
    while True:
        event, values = window.read()
        if event in (Sg.WINDOW_CLOSED, "Exit"):
            break
        if event == "Check File":
            progress_bar = window['-PROGRESS-']


            if (is_valid_path(values["-IN-"])) :
                
                imei_file_path = values["-IN-"]
                
                output_file_path = values["-out-"]
                output_file_path = os.path.join(output_file_path,"output.txt")

                with open(imei_file_path, 'r') as file, open(output_file_path, 'a') as output_file:
                    imeisIntxt = file.readlines()
                    for oneimei in imeisIntxt:
                        oneimei = oneimei.strip()  # Remove any leading/trailing whitespace
                        if oneimei:  # Check if IMEI is not empty
                            result = check_imei(oneimei)
                            output_file.write(f"Result for IMEI {oneimei}: {result}\n")
                            print(f"Result for IMEI {oneimei}: {result} written to file")
                            for i in range(100):
                                progress_bar.update(i + 1)
                                Sg.popup_quick_message(f'Progress: {i + 1}%')

                                


    window.close()

if __name__ == "__main__":
    SettingsPath = Path.cwd()

    # create the settings object and use ini format
    settings = Sg.UserSettings(
        path=SettingsPath, filename="config.ini", use_config_file=True, convert_bools_and_none=True
    )
    theme = settings["GUI"]['theme']
    font_family = settings["GUI"]['font_family']
    font_size = settings["GUI"]["font_size"]
    Sg.theme(theme)
    Sg.set_options(font=(font_family, font_size))
    main_window()
