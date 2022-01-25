from socket import close
from time import time
import PySimpleGUI as sg
 
sg.ChangeLookAndFeel('GrayGrayGray')
def logg_inn_win_layout():     
        layout = [
                [sg.Text('Brukernavn:'), sg.Text(size=(15, 1), key = 'bruk_navn')],
                [sg.Input(key='brukernavn_inp')],
                [sg.Text('Personlig passord:'), sg.Text(size=(15, 1), key='per_pass')],
                [sg.Input(key='per_pass_inp')],
                [sg.Text('Kort nummer:'), sg.Text(size=(15, 1), key='kort_nmr')],
                [sg.Input(key='kort_nmr_inp')],
                [sg.Button('Enter'), sg.Button('Exit')],
                [sg.Button('Create user')]
        ]
        return layout


def create_user_win_layout():
        layout = [
                [sg.Text('email:', size=(15, 1), key='e_mail')],
                [sg.Input(key='email_inp')],
                [sg.Text('Username:', size=(15, 1), key='user')],
                [sg.Input(key= 'user_inp')],
                [sg.Text('password:', size=(15, 1), key='password')],
                [sg.Input(key= 'password_inp')],
                [sg.Text('confirm password', size=(15, 1), key='confirm_password')],
                [sg.Input(key= 'confirm_password_inp')],
                [sg.Button('create'), sg.Button('Back')]
                
        ]
        return layout

def one_time_code_win_layout():
        layout = [
                [sg.Text('one time code', size=(15, 1), key='one_time_code_key')],
                [sg.Input(key='one_time_code_inp')],
                [sg.Button('Continue'),  sg.Button('Close')],
                

        ]

        return layout


def error_one_time_code_layout():
        layout = [
                [sg.Text('Error', size=(15, 1), key='error_one_time_code_key')],
                [sg.Input(key='error_one_time_code_inp')],
                [sg.Button('Close')],
                

        ]

        return layout

def bank_layout():
        layout = [
                [sg.Text('Bodø bank', size=(15, 1), key='bodø_bank_key')],
                [sg.Input(key='bodø_bank_key')],
                [sg.Button('Close')],
                

        ]

        return layout


logg_inn_win = sg.Window('logg_inn_win', logg_inn_win_layout(), element_justification='c') #finalize() and window.maximize() make the window full screan
#window.maximize()
create_user_win = sg.Window('create_user_win', create_user_win_layout(), element_justification='c') #finalize() and window.maximize() make the window full screan
#window.maximize()
one_time_code_win = sg.Window('one_time_code_win', one_time_code_win_layout(), element_justification='c') #finalize() and window.maximize() make the window full screan

error_one_time_code_win = sg.Window('error_one_time_win', error_one_time_code_layout(), element_justification='c') #finalize() and window.maximize() make the window full screan

#event2, values2 = create_user_win.read(timeout=100)
event3, event3 = one_time_code_win.read(timeout=100)
event4, event4 = error_one_time_code_win.read(timeout=100)

#create_user_win.Hide()
one_time_code_win.Hide()
error_one_time_code_win.Hide()

logg_inn_win_active = True
create_user_win_active = False
one_time_code_win_active = False
error_one_time_code_active = False

while True:  # Event Loop
        event, values = logg_inn_win.read(timeout=100)
        if event in (None, 'Exit'):
                break

        
        if event == 'Enter':
                # Update the "output" text element to be the value of "input" element
                logg_inn_win['bruk_navn'].update(values['brukernavn_inp'])
                logg_inn_win['per_pass'].update(values['per_pass_inp'])

                if event == 'Enter':
                        one_time_code_win_active = True
                        one_time_code_win.UnHide()
                        logg_inn_win.Hide()
                        
                       
                       
                        
        if event == 'Create user':
                create_user_win_active = True
                event2, values2 = create_user_win.read(timeout=100)

                create_user_win.UnHide()
                logg_inn_win.Hide()

        
        
       
        
        if create_user_win_active:
                event2, values2 = create_user_win.read(timeout=100)

                if event2 == 'Back':
                        Back = True
                      
                        logg_inn_win_active = True
                        logg_inn_win.UnHide()
                        create_user_win.Hide()

                if event2 == 'create':
                        create = True

                        logg_inn_win_active = True
                        logg_inn_win.UnHide()
                        create_user_win.Hide()

        if one_time_code_win_active:
                event3, values3 = one_time_code_win.read(timeout=100)
                 
                if event3 == 'Exit':
                        Cansel = True
                        one_time_code_win.Hide()
                        error_one_time_code_win.UnHide()
                        
        if error_one_time_code_active:
                event4, values4 = error_one_time_code_win.read(timeout=100)
                
                if event == 'Close':
                        error_one_time_code_win.Hide()
                        logg_inn_win.UnHide()




                
                                
         


                

        
