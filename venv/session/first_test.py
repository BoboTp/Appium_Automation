
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import os
import base64
"""

Desired Capabilities


"""

desired_cap ={
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "/Users/bobo_tp/Downloads/cricbuzz.apk"
}

# Create Driver Instance

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)


#start_video

driver.start_recording_screen()

driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ImageView").click()
driver.find_element_by_xpath("//android.widget.Switch[@text='OFF']").click()

time.sleep(5)
actions = TouchAction(driver)
time.sleep(5)
actions.press(x=375, y=2237)
actions.move_to(x=434, y=910)
actions.release()
actions.perform()

#actions.tap(x=1279,)

driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout").click()

#go_back_button
driver.find_element_by_class_name("android.widget.ImageButton").click()

video_rawdata = driver.stop_recording_screen()
video_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")

# schedule = driver.find_element_by_xpath("//android.widget.TextView[@bounds='[112,878][1195,986]']").get_attribute("text")
#
# print("The Finals is to be held on: ",schedule)



# for i in range(10):
#tp = TouchAction(driver)
#TouchAction(driver)   .press(x=726, y=2261)   .move_to(x=726, y=833)   .release()   .perform()

    # time.sleep(5)

#Screen_shot
# driver.save_screenshot("/Users/bobo_tp/Desktop/Appium_pycharm/screenshot/"+video_name+".pngs")
file_path = os.path.join("/Users/bobo_tp/Desktop/Appium_pycharm/screenshot", video_name+".mp4")

with open(file_path,"wb") as vid:
    vid.write(base64.b64decode(video_rawdata))
