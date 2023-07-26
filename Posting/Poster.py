from tiktok_uploader.auth import AuthBackend
from tiktok_uploader.upload import upload_videos
from os import path

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions


def main():
    print("suck my dick")
    Upload("videos/balls.mp4", "sdaasdfsad aasdfre aansdfauts.")

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

def Upload(filename:str, descr:str):
    pathToCookies = path.join(path.dirname(__file__), 'tiktokLogin.txt')
    pathToVideo = path.join(path.dirname(__file__), filename)
    
    service = Service(ChromeDriverManager(driver_version="114.0.5735.90").install())
    driver = webdriver.Chrome(service=service, options=chrome_defaults())
    auth = AuthBackend(cookies=pathToCookies)


    failedVids = upload_videos([{"path":pathToVideo,"description":descr}], browser_agent=driver, auth=auth)
    for failed in failedVids:
        print(f"{failed['video']} failed.")

if __name__ == "__main__":
    main()