from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import random
import re
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

import urllib
import requests
def chrome_defaults(*args, headless: bool = False, **kwargs) -> ChromeOptions:
    """
    Creates Chrome with Options
    """

    options = ChromeOptions()

    ## regular
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(r'--user-data-dir=C:\\Users\\spiel\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4')
    #options.add_argument(r'--profile-directory=C:\\Users\\spiel\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4')

    ## experimental
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    # headless
    if headless:
        options.add_argument('--headless=new')

    return options

def ScrapeImages(Query:str, cnt = 5, driver=None, whereToSaveRelative="images"):
    if driver is None:
        service = Service(ChromeDriverManager(driver_version="114.0.5735.90").install())
        driver = webdriver.Chrome(service=service, options=chrome_defaults())

    thisPath = os.path.join(os.path.dirname(__file__), whereToSaveRelative)
    files = os.listdir(thisPath)
    for i, file in enumerate(files):
            if i > 100:
                break
            os.remove(os.path.join(thisPath, file))

    # What you enter here will be searched for in
    # Google Images
    query = Query
    
    
    # Maximize the screen
    driver.maximize_window()
    
    # Open Google Images in the browser
    driver.get(f'https://www.google.com/search?q={query}&tbm=isch&source=hp&biw=1058&bih=946&ei=HJfBZJKAA47SkgWj1bmQDA&iflsig=AD69kcEAAAAAZMGlLHs9U6-kY3K5T5qQ8H9LmRwpj_rK&ved=0ahUKEwiS_v6fr62AAxUOqaQKHaNqDsIQ4dUDCAc&uact=5&oq=balls&gs_lp=EgNpbWciBWJhbGxzMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEicsgNQnq0DWOKwA3AIeACQAQCYAS6gAdUBqgEBNbgBA8gBAPgBAYoCC2d3cy13aXotaW1nqAIA&sclient=img')


    
    # NOTE: If you only want to capture a few images,
    # there is no need to use the scroll_to_bottom() function.
    #scroll_to_bottom()
    time.sleep(random.randint(3,6))
    imgs = driver.find_elements(By.CSS_SELECTOR,"img")
    # Loop to capture and save each image
    
    nResults = 0
    for i, img in enumerate(imgs):
    
        if nResults >= cnt:
            break

        if img.get_attribute("class").startswith("rg_i"):

            img.click()
            time.sleep(random.randint(3,6))
            bigImgs = driver.find_elements(By.CSS_SELECTOR, "img")
            for bigImg in bigImgs:
                if bigImg.get_attribute("class").startswith("r48jcc pT0Scc iPVvYb"):#bigImg.size["width"] > 256:
                    try:
                        style = bigImg.get_attribute("style")
                        minWidth = 768
                        
                        widthStyle = re.search(r"\bwidth: \b\d+", style).group(0)
                        widthStyle = re.search(r"\d+", widthStyle).group(0)
                        if int(widthStyle) > minWidth:
                            pathToSource = bigImg.get_attribute('src')
                            filename = thisPath + "\\"

                            if pathToSource.endswith("png"):
                                filename += f"{i} {query}.png"
                            if pathToSource.endswith("jpg"):
                                filename += f"{i} {query}.jpg"
                            if pathToSource.endswith("jpeg"):
                                filename += f"{i} {query}.jpg"
                            if pathToSource.endswith("webp"):
                                filename += f"{i} {query}.webp"

                            r = requests.get(pathToSource)
                            with open(filename, "wb+") as f:
                                f.write(r.content)
                            
                            nResults+=1
                            r.close()
                            f.close()

                        
                        
                        # Enter the location of folder in which
                        # the images will be saved
                        #bigImg.screenshot(os.path.join(thisPath, query + ' (' + str(i) + ').png'))
                        # Each new screenshot will automatically
                        # have its name updated

                        # Just to avoid unwanted errors
                        time.sleep(random.randint(1,2))


                    except:
                        
                        # if we can't find the XPath of an image,
                        # we skip to the next image
                        continue
    
    # Finally, we close the driver
    driver.close()