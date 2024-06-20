from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class WebAccess():
    def __init__(self):
        pass

    def upd_web_driver(self) -> str:
        # webドライバーの更新
        driver_path = ChromeDriverManager().install()
        return driver_path

    def access(self, driver_path: str, url: str, waiting_time: int = 3):
        driver = webdriver.Chrome(service=Service(executable_path=driver_path))
        driver.get(url)
        # ドライバーが要素を探す時間を確保（htmlタグ等）
        driver.implicitly_wait(waiting_time)
