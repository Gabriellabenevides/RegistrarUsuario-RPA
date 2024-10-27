import selenium.webdriver
import selenium.webdriver.support.wait
import selenium.webdriver.remote.webelement
import datetime
import os
import time
import warnings
import glob


def element(driver: selenium.webdriver.Chrome, element: list) -> selenium.webdriver.remote.webelement.WebElement:
    print(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Interacting with element: {element[0]}")
    wait = selenium.webdriver.support.wait.WebDriverWait(driver, 60, 1)

    def check(driver: selenium.webdriver.Chrome, element: list):
        try:
            return driver.find_element(element[1], element[2])
            # return True
        except Exception:
            return None
    try:
        return wait.until(lambda x: check(driver, element))
    except Exception as e:
        # raise e
        raise Exception(f"Element took to long to respond: {e}")


def text(driver: selenium.webdriver.Chrome, element: list) -> selenium.webdriver.remote.webelement.WebElement:
    print(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Interacting with element: {element[0]}")
    wait = selenium.webdriver.support.wait.WebDriverWait(driver, 60, 1)

    def check(driver: selenium.webdriver.Chrome, element: list):
        try:
            return driver.find_element(element[1], element[2]).text
            # return True
        except Exception:
            return None
    try:
        return wait.until(lambda x: check(driver, element))
    except Exception as e:
        # raise e
        raise Exception(f"Element took to long to respond: {e}")


def click(driver: selenium.webdriver.Chrome, element: list):
    print(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Interacting with element: {element[0]}")
    wait = selenium.webdriver.support.wait.WebDriverWait(driver, 60, 1)

    def check(driver: selenium.webdriver.Chrome, element: list):
        try:
            driver.find_element(element[1], element[2]).click()
            return True
        except Exception as e:
            return False
    try:
        wait.until(lambda x: check(driver, element))
    except Exception as e:
        raise Exception(f"Element took to long to respond: {e}")


def send_keys(driver: selenium.webdriver.Chrome, element: list, text: str):
    print(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Interacting with element: {element[0]}")
    wait = selenium.webdriver.support.wait.WebDriverWait(driver, 60, 1)

    def check(driver: selenium.webdriver.Chrome, element: list, text: str):
        try:
            driver.find_element(element[1], element[2]).send_keys(text)
            return True
        except Exception as e:
            return False
    try:
        wait.until(lambda x: check(driver, element, text))
    except Exception as e:
        raise Exception(f"Element took to long to respond: {e}")


def clear_send_keys(driver: selenium.webdriver.Chrome, element: list, text: str):
    print(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Interacting with element: {element[0]}")

    wait = selenium.webdriver.support.wait.WebDriverWait(driver, 60, 1)

    def check(driver: selenium.webdriver.Chrome, element: list, text: str):
        try:
            driver.find_element(element[1], element[2]).clear()
            time.sleep(1)
            driver.find_element(element[1], element[2]).send_keys(text)
            return True
        except Exception as e:
            return False
    try:
        wait.until(lambda x: check(driver, element, text))
    except Exception as e:
        raise Exception(f"Element took to long to respond: {e}")
    
def clear(driver: selenium.webdriver.Chrome, element: list, text: str):
    print(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Interacting with element: {element[0]}")

    wait = selenium.webdriver.support.wait.WebDriverWait(driver, 60, 1)

    def check(driver: selenium.webdriver.Chrome, element: list, text: str):
        try:
            driver.find_element(element[1], element[2]).clear()
            time.sleep(1)
            return True
        except Exception as e:
            return False
    try:
        wait.until(lambda x: check(driver, element, text))
    except Exception as e:
        raise Exception(f"Element took to long to respond: {e}")


def download(driver, element, path):
    count_files = len(os.listdir(path))

    click(driver, element)

    count_loop = 0
    # while (len(os.listdir(path)) <= count_files and not any(file.endswith(('.tmp', '.crdownload')) for file in os.listdir(path))):
    while (len(os.listdir(path)) <= count_files or (glob.glob(os.path.join(path, "*.tmp")) or glob.glob(os.path.join(path, "*.crdownload")))):
        time.sleep(1)
        count_loop += 1
        print(f"{count_loop} - second(s) Waiting to download file")

        if count_loop >= 120:
            raise Exception(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Error to download File: it took too long to download")
