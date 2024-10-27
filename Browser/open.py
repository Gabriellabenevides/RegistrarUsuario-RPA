import os
import selenium.webdriver
import datetime


def open() -> selenium.webdriver.Chrome:
    print(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Opening browser")

    options: selenium.webdriver.ChromeOptions = selenium.webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--always-authorize-plugins")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--ignore-certificate-errores")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("enable-automation")
    options.add_experimental_option("prefs", {
        "download.default_directory": f"C: \\Users\\{os.path.expanduser("~")}\\Downloads",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False})
    options.accept_insecure_certs = True

    options.add_argument("--log-level=3")

    options.add_argument(r"--log-file=C:\Windows\SystemTemp")

    driver = selenium.webdriver.Chrome(options)
    
    return driver
