import sys
while True:
    try:
        newlink = input("Enter Website Link: ")

        with open(r"C:\Users\Jesse\OneDrive\Desktop\References_for_SANSSummit_ThreatHunting.txt", "a") as websitelinks:
            websitelinks.writelines(newlink + "\n\r")
                            
    except KeyboardInterrupt:
        break

sys.exit(0)
