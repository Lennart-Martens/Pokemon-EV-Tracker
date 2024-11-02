import pickle
import PySimpleGUI as sg
from monData import *

STATS = ["HP", "Attack", "Defense", "Sp.Atk", "Sp.Def", "Speed"]

# Set up columns
columns = [[[sg.Text(stat, size=(6,1), justification="center")],
            [sg.Text("--", key=f"__{stat}")],
            [sg.Button("+", key=f"{stat}+", size=(2,1), disabled=True)],
            [sg.Button("-", key=f"{stat}-", size=(2,1), disabled=True)]] for stat in STATS]

# Read saved data
with open("monData.pkl", "rb") as file:
    savedMons = pickle.load(file)

# Set up layout and window
layout = [  [sg.Combo(savedMons, key="-COMBO-", readonly=True, enable_events=True)],
            [sg.Column(column, element_justification="center") for column in columns] ]
window = sg.Window("Pokemon EV Tracker", layout, keep_on_top=True)

# Main loop
while True:
    # Read event and exit if closed
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # Change current mon
    if event == "-COMBO-":
        currMon = values["-COMBO-"]
        for i in range(6):
            window[f"__{STATS[i]}"].update(currMon.stats[i])
            window[f"{STATS[i]}+"].update(disabled=False)
            window[f"{STATS[i]}-"].update(disabled=False)

    # Edit stats
    for i in range(6):
        if event == f"{STATS[i]}+":
            currMon.stats[i] += 1
            window[f"__{STATS[i]}"].update(currMon.stats[i])
        elif event == f"{STATS[i]}-":
            currMon.stats[i] -= 1
            window[f"__{STATS[i]}"].update(currMon.stats[i])

with open("monData.pkl", "wb") as file:
    pickle.dump(savedMons, file)

window.close()