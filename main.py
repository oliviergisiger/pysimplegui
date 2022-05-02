# main.py>


import PySimpleGUI as sg
import requests
import json
from datetime import datetime
import math
from get_connection import get_connection

#sg.theme('DarkBlack')   # Add a touch of color
# All the stuff inside your window.
headings = ["Departure", "Station", "Platform", "Transfers","Duration"]
con_values = []

layout = [  [sg.Text("Start: "), sg.InputText(key="-START-")],
            [sg.Text("Destination"), sg.InputText(key="-DEST-")],
            [sg.Text("Starting Time: "), sg.InputText(key="-TIME-")], 
            [sg.Button("Show Connections")],
            [sg.Table(values=con_values, 
                      headings=headings, 
                      col_widths=[20, 15, 10], 
                      auto_size_columns=False,
                      justification="left", 
                      row_height=35,
                      num_rows=4,
                      key="-OUTPUT-")], 
            [sg.Push(), sg.Button("Later Connections")]
        ]

# Create the Window
window = sg.Window("Fahrplan", layout, size=(500, 400))

inputs = []

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "Show Connections": 
        depart_stat = values["-START-"]
        dest_stat = values["-DEST-"]
        start_time = values["-TIME-"]
        con_values = []

        con_values = get_connection(depart_stat, dest_stat, start_time)

        window['-OUTPUT-'].update(con_values)
    
    if event == "Later Connections":
        depart_stat = values["-START-"]
        dest_stat = values["-DEST-"]
        start_time = con_values[3][0]
        
        con_values = []

        con_values = get_connection(depart_stat, dest_stat, start_time)

        window['-OUTPUT-'].update(con_values)          
    


start_time = inputs[2]



window.close()
