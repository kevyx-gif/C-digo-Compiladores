import PySimpleGUI as sg
import os

sg.theme('DarkAmber')  # please make your creations colorful

layout = [  [sg.Text('Nombre del archivo')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.OK(), sg.Cancel()]
        ]


window = sg.Window('Toma de archivo', layout)
event, values = window.read()

window.close()

#DarkBrown
#Dark
#DarkBlack1
#DarkTeal2

