import PySimpleGUI as sg
 
sg.ChangeLookAndFeel('GrayGrayGray')
def win1_layout():     
        layout = [
                [sg.Text('Brukernavn:'), sg.Text(size=(15, 1), key = 'bruk_navn')],
                [sg.Input(key='bruknavn_inp')],
                [sg.Text('Personlig passord:'), sg.Text(size=(15, 1), key='-per_pass-')],
                [sg.Input(key='pre_pass_inp')],
                [sg.Text('Kort nummer:'), sg.Text(size=(15, 1), key='-kort_nmr-')],
                [sg.Input(key='-kort_nmr_inp-')],
                [sg.Button('Enter'), sg.Button('Cancel')],
                [sg.Button('Create user')]
        ]
        return layout

win1 = sg.Window('Tittel på programmer', win1_layout(), element_justification='c') #finalize() and window.maximize() make the window full screan
#window.maximize()



while True:  # Event Loop
        event, values = win1.read(timeout=100)
        if event in (None, 'Cancel'):
                break
        if event == 'Enter':
                # Update the "output" text element to be the value of "input" element
                win1['-random2-'].update(values['-random-'])
    


        

 
