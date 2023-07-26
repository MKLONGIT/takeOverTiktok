from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By



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

def ScrapeImages(Query:str, driver=None):
    if driver is not None:
        service = Service(ChromeDriverManager(driver_version="114.0.5735.90").install())
        driver = webdriver.Chrome(service=service, options=chrome_defaults())

    # What you enter here will be searched for in
    # Google Images
    query = Query
    
    
    # Maximize the screen
    driver.maximize_window()
    
    # Open Google Images in the browser
    driver.get(f'https://www.google.com/search?q={query}&tbm=isch&source=hp&biw=1058&bih=946&ei=HJfBZJKAA47SkgWj1bmQDA&iflsig=AD69kcEAAAAAZMGlLHs9U6-kY3K5T5qQ8H9LmRwpj_rK&ved=0ahUKEwiS_v6fr62AAxUOqaQKHaNqDsIQ4dUDCAc&uact=5&oq=balls&gs_lp=EgNpbWciBWJhbGxzMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEicsgNQnq0DWOKwA3AIeACQAQCYAS6gAdUBqgEBNbgBA8gBAPgBAYoCC2d3cy13aXotaW1nqAIA&sclient=img')


    # Function for scrolling to the bottom of Google
    # Images results
    def scroll_to_bottom():
    
        last_height = driver.execute_script('\
        return document.body.scrollHeight')
    
        while True:
            driver.execute_script('\
            window.scrollTo(0,document.body.scrollHeight)')
    
            # waiting for the results to load
            # Increase the sleep time if your internet is slow
            time.sleep(3)
    
            new_height = driver.execute_script('\
            return document.body.scrollHeight')
    
            # click on "Show more results" (if exists)
            try:
                driver.find_element_by_css_selector(".YstHxe input").click()
    
                # waiting for the results to load
                # Increase the sleep time if your internet is slow
                time.sleep(3)
    
            except:
                pass
    
            # checking if we have reached the bottom of the page
            if new_height == last_height:
                break
    
            last_height = new_height
    
    
    # Calling the function
    
    # NOTE: If you only want to capture a few images,
    # there is no need to use the scroll_to_bottom() function.
    #scroll_to_bottom()
    time.sleep(2)
    imgs = driver.find_elements(By.CSS_SELECTOR,"img")
    # Loop to capture and save each image
    
    nResults = 0
    for i, img in enumerate(imgs):
    
        if nResults > 5:
            break

        if img.get_attribute("class").startswith("rg_i"):

            nResults+=1
            img.click()
            time.sleep(1.5)
            bigImgs = driver.find_elements(By.CSS_SELECTOR, "img")
            for bigImg in bigImgs:
                if bigImg.get_attribute("class").startswith("r48jcc"):#bigImg.size["width"] > 256:
                    try:
                        savePath = os.path.dirname(__file__)
                        # Enter the location of folder in which
                        # the images will be saved
                        bigImg.screenshot(os.path.join(savePath, query + ' (' + str(i) + ').png'))
                        # Each new screenshot will automatically
                        # have its name updated

                        # Just to avoid unwanted errors
                        time.sleep(0.5)

                    except:
                        
                        # if we can't find the XPath of an image,
                        # we skip to the next image
                        continue
    
    # Finally, we close the driver
    driver.close()
