from selenium import webdriver
import re

def kaltura_check(url):


    # chromedriverpath = 'C:\Users\Cristian\.windows-build-tools\python27\Lib\site-packages\selenium\webdriver\chrome\chromedriver'

    chromedriver = webdriver.Chrome()
    chromedriver.get(url)

    segment = re.findall("(http[s]?:\/\/)?([^\/\s]+\/)(.*)", url)
    file_name = segment[0][2] + "_globalization-qa-feedback.txt"
    file_name = file_name.replace('/', '_')
    f = open(file_name, "w+")

    # Kaltura IDs checking
    video_placeholders = chromedriver.find_elements_by_xpath("//div[@class='ibm-video-player-con']")
    video_ctas = chromedriver.find_elements_by_xpath("//a[@data-videotype='youtube']")

    for item in video_ctas:
        kaltura = item.get_attribute("data-kaltura-fallbackid")
        if (kaltura == None):
            link = item.get_attribute('data-videoid')
            print("Missing Kaltura ID: https://www.youtube.com/watch?v=" + link)
            f.write("Missing Kaltura ID: https://www.youtube.com/watch?v=" + link + "\r\n")

    f.close()
    chromedriver.close()

pages = ['https://www.ibm.com/services/digital-workplace/desktop-virtualization',
'https://www.ibm.com/services/digital-workplace/watson-support',
'https://www.ibm.com/services/technology-support/retail-support',
'https://www.ibm.com/services/technology-support/branch-banking',
'https://www.ibm.com/services/business-continuity/plan',
'https://www.ibm.com/services/business-continuity/cyber-attack']

for page in pages:
    kaltura_check(page)
