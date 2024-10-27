import PySimpleGUI as sg

# Set up columns and layout
hpCol = [   [sg.Text('HP')],
            [sg.Text('0', key='-HP-')],
            [sg.Button('+', key='hp+')],
            [sg.Button('-', key='hp-')] ]

attackCol = [   [sg.Text('Attack')],
                [sg.Text('0', key='-ATTACK-')],
                [sg.Button('+', key='attack+')],
                [sg.Button('-', key='attack-')] ]

defenseCol = [  [sg.Text('Defense')],
                [sg.Text('0', key='-DEFENSE-')],
                [sg.Button('+', key='defense+')],
                [sg.Button('-', key='defense-')] ]

spatkCol = [    [sg.Text('Sp. Atk')],
                [sg.Text('0', key='-SPATK-')],
                [sg.Button('+', key='spatk+')],
                [sg.Button('-', key='spatk-')] ]

spdefCol = [    [sg.Text('Sp. Def')],
                [sg.Text('0', key='-SPDEF-')],
                [sg.Button('+', key='spdef+')],
                [sg.Button('-', key='spdef-')] ]

speedCol = [    [sg.Text('Speed')],
                [sg.Text('0', key='-SPEED-')],
                [sg.Button('+', key='speed+')],
                [sg.Button('-', key='speed-')] ]

cols = [hpCol, attackCol, defenseCol, spatkCol, spdefCol, speedCol]
layout = [  [sg.Text('Training Session EVs')],
            [sg.Column(column, element_justification='center') for column in cols] ]

window = sg.Window('Pokemon EV Tracker', layout, keep_on_top=True)

# Set initial values
hp = 0
attack = 0
defense = 0
spatk = 0
spdef = 0
speed = 0

# Main loop
while True:
    # Read event and exit if closed
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # Edit stats
    if event == 'hp+':
        hp += 1
        window['-HP-'].update(hp)
    elif event == 'hp-':
        hp -= 1
        window['-HP-'].update(hp)

    if event == 'attack+':
        attack += 1
        window['-ATTACK-'].update(attack)
    elif event == 'attack-':
        attack -= 1
        window['-ATTACK-'].update(attack)
    
    if event == 'defense+':
        defense += 1
        window['-DEFENSE-'].update(defense)
    elif event == 'defense-':
        defense -= 1
        window['-DEFENSE-'].update(defense)

    if event == 'spatk+':
        spatk += 1
        window['-SPATK-'].update(spatk)
    elif event == 'spatk-':
        spatk -= 1
        window['-SPATK-'].update(spatk)

    if event == 'spdef+':
        spdef += 1
        window['-SPDEF-'].update(spdef)
    elif event == 'spdef-':
        spdef -= 1
        window['-SPDEF-'].update(spdef)

    if event == 'speed+':
        speed += 1
        window['-SPEED-'].update(speed)
    elif event == 'speed-':
        speed -= 1
        window['-SPEED-'].update(speed)

 
window.close()