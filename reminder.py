import time
from plyer import notification
from datetime import datetime
 
if __name__=="__main__":
        while True:
            notification.notify(
                title = "Gentle notification",
                message="LOOK FAR",
                app_name = "ghost",
                app_icon = r"c:\Users\HARSH\Downloads\samurai_warrior_armor_japan_culture_icon_193264.ico", 
                # r"c:\Users\HARSH\Downloads\samurai_warrior_japanese_mask_traditional_helmet_japan_face_icon_127293.ico",
                # displaying time
                timeout=20
    )
            # waiting time
            time.sleep(60*10)            
            current_time = datetime.now().time()
            print("Current Time:", current_time)
