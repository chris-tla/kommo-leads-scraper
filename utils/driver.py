from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    chrome_options = Options()

    # Si usas Brave, descomenta esta línea y ajusta la ruta
    # chrome_options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)