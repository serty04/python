from socket import close
from time import time
import PySimpleGUI as sg
 
sg.ChangeLookAndFeel('GrayGrayGray')
def logg_inn_win_layout():     
        layout = [
                [sg.Text('Brukernavn:'), sg.Text(size=(15, 1), key = 'bruk_navn')],
                [sg.Input(key='brukernavn_inp')],
                [sg.Text('Personlig passord:'), sg.Text(size=(15, 1), key='per_pass')],
                [sg.Input(key='per_pass_inp', password_char='*')],
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



def bank_layout():
        layout = [
                [sg.Text('Bodø bank',size=(160, 50), key='bodø_bank_key'), sg.Button('logg out')],
                [sg.Input(key='bodø_bank_key')],
                [sg.Text('konto_nmr'), sg.Text('hvilken_konto')],
                [sg.Text(('konto navn'), key='konto_navn_tf')] [sg.Text(('penger_på_konto'), key='konto penger')],
                [sg.Button('Enter'),sg.Button('Close')],
                
        ]

        return layout

logg_inn_win = sg.Window('logg_inn_win', logg_inn_win_layout(), element_justification='c') #finalize() and window.maximize() make the window full screan
#window.maximize()
create_user_win = sg.Window('create_user_win', create_user_win_layout(), element_justification='c') #finalize() and window.maximize() make the window full screan
#window.maximize()
bank_win = sg.Window('Bodø bank', bank_layout()) #finalize() and window.maximize,element_justification='c') #finalize() and window.maximize() make the window full screan
#window.maximize()

#event2, values2 = create_user_win.read(timeout=100)


#create_user_win.Hide()


logg_inn_win_active = True
create_user_win_active = False
bank_win_active = False

while True:  # Event Loop
        event, values = logg_inn_win.read(timeout=100)
        if event in (None, 'Exit'):
                break

        
        if event == 'Enter':
                if values['brukernavn_inp'] == 'Elias' and values['per_pass_inp'] == '123':
                        event3, values3 = bank_win.read(timeout=100)
                        bank_win_active = True
                        logg_inn_win.Hide()
                        bank_win.UnHide()
                        
                else:
                        sg.popup('Wrong username or password')
        
        if event == 'Create user':
                create_user_win_active = True
                event2, values2 = create_user_win.read(timeout=100)

                create_user_win.UnHide()
                logg_inn_win.Hide()

        
        if bank_win_active:
                event3, values3 = bank_win.read(timeout=100)
                if event3 == 'Close':
                        bank_active = False
                        bank_win.close()
                        

        
       
        
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

       
