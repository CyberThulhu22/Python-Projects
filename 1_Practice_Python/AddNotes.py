import sys
import datetime
while True:
    try:
        
        newnote = input("Enter Notes: ")
        a = "{}".format(datetime.datetime.now().strftime("%H:%M:%S"))

        with open(r"C:\Users\Jesse\OneDrive\Desktop\WWHF\My_Extras\ConfrenceNotes.txt", "a") as confnotes:
            confnotes.writelines(a + " " + newnote + "\n\r")
                            
    except KeyboardInterrupt:
        break

sys.exit(0)
