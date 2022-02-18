import PySimpleGUI as sg
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bodo_bank"
)


mycursor = mydb.cursor()




sg.ChangeLookAndFeel('GrayGrayGray')
def logg_inn_win_layout():     
        layout = [
                [sg.Text('Brukernavn:'), sg.Text(size=(15, 1), key = 'bruk_navn')],
                [sg.Input(key='-username-')],
                [sg.Text('Personlig passord:'), sg.Text(size=(15, 1), key='-personlig_passord-')],
                [sg.Input(key='-password-', password_char='*')],
                [sg.Button('Enter'), sg.Button('Exit')],
                [sg.Button('Create user')]
        ]
        return layout


def create_user_win_layout():
        layout = [
                [sg.Text('Username:', size=(15, 1))],
                [sg.Input(key= '-create_username-')],
                [sg.Text('password:', size=(15, 1))],
                [sg.Input(key= '-create_password-')],
                [sg.Text('confirm password', size=(15, 1))],
                [sg.Input(key= '-confirm_password-')],
                [sg.Button('create'), sg.Button('Back')]
                
        ]
        return layout


def bank_win_layout():
        layout = [
                
                [sg.Text('Bodø bank', key='bodø_bank_key'), sg.Button('logg out')],
                [sg.Text ('betale_fra'), sg.Text ('betale_til')],
                [sg.Text('konto:'), sg.Text('Add konto nummer'), sg.Text('Navn på konto'), sg.Input(key='bodø_bank_key'), sg.Button('Enter')],
                [sg.Text('Eier navn', key='owner_account'), sg.Text('Disp:'), sg.Text('Penger på konto', key='disp_amount')],
        ]

        return layout

logg_inn_win = sg.Window('logg_inn_win', logg_inn_win_layout(), element_justification='c') #finalize() and window.maximize() make the window full screan
#window.maximize()
create_user_win = sg.Window('create_user_win', create_user_win_layout(), element_justification='c') #finalize() and window.maximize() make the window full screan
#window.maximize()
bank_win = sg.Window('Bodø bank',  bank_win_layout(), size=(1000, 1050)) #finalize() and window.maximize,element_justification='c') #finalize() and window.maximize() make the window full screan
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

                username = values['-username-']
                pw = values['-password-']
        
                sql = "SELECT username, password FROM user WHERE username =%s AND password = %s"
                mycursor.execute(sql, (username, pw))
                myresult = mycursor.fetchall()
                
                row_count = mycursor.rowcount
               
                        
                if row_count == 1:
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
                        username = values2['-create_username-']    # -reg- er en key i layout
                        password = values2['-create_password-']
                        


                        sql = "INSERT INTO user(username, password) VALUES (%s, %s)"
                        val = (username, password)
                        mycursor.execute(sql, val)

                        mydb.commit()
                        print(mycursor.rowcount, "record inserted.")

                        sg.popup('User created successfully: ', username)

                        logg_inn_win_active = True
                        logg_inn_win.UnHide()
                        create_user_win.Hide()
                        
                

              
                