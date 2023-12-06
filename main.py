import pyautogui
import time
import keyboard


while True:

    im=pyautogui.screenshot()

    screen=im.getpixel((214,189))

    #  in cmd under python
    # >>> import pyautogui
    # >>> pyautogui.displayMousePosition()



    # 4 postion to detect of trees
    x1 = im.getpixel((450,270))
    x2 = im.getpixel((480, 265))
    x3 = im.getpixel((500, 265))
    x4 = im.getpixel((520, 260))

    # 4 postion to detect of bird
    y1 = im.getpixel((450, 240))
    y2 = im.getpixel((480, 240))
    y3 = im.getpixel((500, 240))
    y4 = im.getpixel((520, 245))

    if screen[0] == 255:
        if x1[0]!=255 or x2[0]!=255 or x3[0]!=255  or x4[0]!=255  or y1[0]!=255  or y2[0]!=255 or y3[0]!=255  or y4[0]!=255:
            pyautogui.press("space")
            time.sleep(0.0001)
    # for identifying black screen pixel
    else:
        if x1[0]!=0 or x2[0]!=0 or x3[0]!=0  or x4[0]!=0  or y1[0]!=0  or y2[0]!=0 or y3[0]!=0  or y4[0]!=0:
            pyautogui.press("space")
            time.sleep(0.0001)



    if keyboard.is_pressed("s"):
        break

    else:
        pass
