from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import requests
import re

# Replace with your 'chromedriver' file path
CHROMEDRIVER_PATH = '/Users/cristianmacedo/Downloads/ibm-globalization-automation-master/chromedriver'

# Replace with your chrome profile path
CHROME_PROFILE_PATH = '/Users/cristianmacedo/Library/Application Support/Google/Chrome/Default'
    
# Returns the youtube title of the provided video 
def getVideoTitle(videourl):    

    # Creates a new focus chrome window to the video
    videotab = webdriver.Chrome(CHROMEDRIVER_PATH)
    videotab.get(videourl)

    # Setting expire time (seconds) to get YouTube video title - prevents stoping the process due Youtube connection problems (Unavailable video, private video...) 
    wait = WebDriverWait(videotab, 20)

    # Setting the return condition = wait until it returns the YouTube title | Storing the video title 
    title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
    videotab.quit()
    return(title) 

def startCheck(url):

    ###### TXT FILE CREATING ######
    
    # Creating/Overriding the .txt file with a relative name
    split_url = re.findall("(http[s]?:\/\/)?([^\/\s]+\/)(.*)", url)
    segments = split_url[0][2] + "_SeleniumQA.txt"
    file_name = segments.replace('/', '_')
    f = open(file_name, "w+")

    ###### EDIT PAGE ######
    
    # Checks the edit page
    editlink = url + "/edit"

    # Loads the default profile to load saved login options
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=" + CHROME_PROFILE_PATH) #Path to your chrome profile

    # Opens the edit page
    editpage = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
    editpage.get(editlink)

    ###### META TITLE ######

    # Gets the current meta title value
    meta_title = editpage.find_element_by_xpath("//input[@id='edit-field-meta-tags-0-basic-title']")
    meta_title = meta_title.get_attribute('value')

    # Checks if meta title is occrect
    if (meta_title != '[node:field_common_browser_page_title] [ibm-country:name] | [site:name]'):
       f.write("Meta Title should be set to [node:field_common_browser_page_title] [ibm-country:name] | [site:name] \r\n \r\n")
       print("Meta Title should be set to [node:field_common_browser_page_title] [ibm-country:name] | [site:name] \n")

    ###### ADMIN ID ######

    # ATTENTION: This feature is not 100% accurate, it only checks if the Admin ID starts with 'us-en_' 
    # I'm still searching for a way of validating all possible admin IDs (cc-lc_segment_content-type_qualifier)
    # Naming guidance documentation: https://ibm.ent.box.com/v/naming-guidance

    # Gets the current Admin ID value
    admin_id = editpage.find_element_by_xpath("//input[@id='edit-title-0-value']")
    admin_id = admin_id.get_attribute('value')

    # Checks if the Admin ID starts with 'us-en_'    
    match = re.match('^us-en_', admin_id)
    if (not match):
        f.write("Admin ID should be following the naming guidance \r\n \r\n")
        print("Admin ID should be following the naming guidance \n")

    editpage.quit()

    ###### MAIN PAGE ######
    
    # Opens the main page
    mainpage = webdriver.Chrome(CHROMEDRIVER_PATH)
    mainpage.get(url)

    ###### DESCRIPTION ######
    
    if (not mainpage.find_elements_by_xpath("//meta[@name='description']")):
        f.write("The page is missing Description meta tag \r\n \r\n")
        print("The page is missing Description meta tag \n")

    ###### KEYWORDS ######

    if (not mainpage.find_elements_by_xpath("//meta[@name='keywords']")):
        f.write("The page is missing Keywords meta tag \r\n \r\n")
        print("The page is missing Keywords meta tag \n")

    ###### LINKAGE ######

    # Getting all links    
    links = mainpage.find_elements_by_xpath("//div[@id='block-northstar-content']//a")

    ###### MARKETPLACE LINKS ######

    first = True
    for link in links:
        if (first):
            f.write("Remove '/us-en' from the marketplace link(s): \r\n")
            print("\nRemove '/us-en' from the marketplace link(s): \n")
            first = False
        href = link.get_attribute('href')
        if ((href != None) and ('/us-en/marketplace' in href)):
            cta_text = link.find_element_by_tag_name('span').get_attribute('innerHTML')
            f.write(cta_text + " - " + href + "\r\n")
            print(cta_text + " - " + href )

    ###### FORMS ######

    first = True
    for link in links:
        if (first):
            f.write("Invalid form type (Against GDPR): \r\n")
            print("\nInvalid form type (Against GDPR): \n")
            first = False
        href = link.get_attribute('href')
        if ((href != None) and ('formid=' in href)):
            if ('urx' not in href):
                cta_text = link.find_element_by_tag_name('span').get_attribute('innerHTML')
                f.write(cta_text + " - " + href + "\r\n")
                print(cta_text + " - " + href )

    ###### DRUPAL LINKS ######

    first = True
    for link in links:
        if (first):
            f.write("The following Drupal links should be coded as relative: \r\n")
            print("\nThe following Drupal links should be coded as relative: \n")
            first = False
        href = link.get_attribute('href')
        if ((href != None) and ('www.ibm.com' in href) and ('/marketplace' not in href)):
            cms_link = href.replace('www', 'cms')
            r = requests.get(cms_link)
            if (r.status_code == 200):
                cta_text = link.find_element_by_tag_name('span').get_attribute('innerHTML')
                f.write(cta_text + " - " + href + "\r\n")
                print(cta_text + " - " + href )
    
    ###### KALTURA IDS ######

    # Selects and stores all the youtube video CTAs and thumbs found on the page
    video_ctas_and_thumbs = mainpage.find_elements_by_xpath("//a[@data-videotype='youtube']")
    video_ctas_and_thumbs += mainpage.find_elements_by_xpath("//div[@data-videotype='youtube']")

    # Stores the videos without Kaltura
    no_kaltura_videos = []

    # Stores the video ids for duplicates reference
    videoids = []

    first = True

    # Iterates through all the video CTAs and thumbs found early
    for item in video_ctas_and_thumbs:

        if (first):
            f.write("Missing Kaltura ID: \r\n")
            print("\nMissing Kaltura ID: \n")
            first = False
            
        # Gets the Kaltura ID of the current element
        kaltura = item.get_attribute("data-kaltura-fallbackid")         

        # Checks if the current element has Kaltura ID
        if (kaltura == None):

            # Gets the current video ID
            videoid = item.get_attribute('data-videoid')

            # Checks for duplicates 
            if videoid not in videoids:

                # Getting the info of the current video
                link = ("https://www.youtube.com/watch?v=" + videoid)
                videotitle = getVideoTitle(link)
                
                # Appends the current video id to the list
                videoids.append(videoid)

                # Resets the list and appends the current video title and link
                video = []
                video.append(link)
                video.append(videotitle)

                # Appends the
                no_kaltura_videos.append(video)

    # Writes the videos on the .txt document iterating through all the videos on the list
    for v in no_kaltura_videos:
        print(v[0] + " - " + v[1])
        f.write(v[0] + " - " + v[1] + "\r\n")
    
    mainpage.quit()
    f.close()

    print("\nQA Feedback Successfully saved at the " + file_name + " file")

# List of pages to check. ONLY WORKS WITH NODE LINKS
pages = ['https://cms.ibm.com/node/1208921']

for url in pages:
    startCheck(url)
