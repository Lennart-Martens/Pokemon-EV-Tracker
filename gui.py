import PySimpleGUI as sg

STATS = ["HP", "Attack", "Defense", "Sp.Atk", "Sp.Def", "Speed"]

# Set up columns and layout
columns = [[[sg.Text(stat)],
            [sg.Text("0", key=f"__{stat}")],
            [sg.Button("+", key=f"{stat}+")],
            [sg.Button("-", key=f"{stat}-")]] for stat in STATS]

layout = [  [sg.Text("Training Session EVs")],
            [sg.Column(column, element_justification="center") for column in columns] ]

window = sg.Window("Pokemon EV Tracker", layout, keep_on_top=True)

# Set initial values
evs = [0 for i in range(6)]

# Main loop
while True:
    # Read event and exit if closed
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # Edit stats
    for i in range(6):
        if event == f"{STATS[i]}+":
            evs[i] += 1
            window[f"__{STATS[i]}"].update(evs[i])
        elif event == f"{STATS[i]}-":
            evs[i] -= 1
            window[f"__{STATS[i]}"].update(evs[i])

            
window.close()