from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class WebAccess():
    def __init__(self):
        pass

    def upd_web_driver(self) -> str:
        # WebDriverのパスを取得
        driver_path = ChromeDriverManager().install()
        return driver_path

    def access(self, driver_path: str, url: str, waiting_time: int = 3):
        # オプションを設定
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--log-level=3')

        # WebDriverを初期化
        driver = webdriver.Chrome(
            service=Service(executable_path=driver_path),
            options=options
        )
        driver.get(url)
        driver.implicitly_wait(waiting_time)
        # ドライバーが要素を探す時間を確保（htmlタグ等）


if __name__ == "__main__":
    wa = WebAccess()
    driver_path = wa.upd_web_driver()
    wa.access(driver_path, "https://google.com")
