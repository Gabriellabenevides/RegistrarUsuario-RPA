import psutil
import datetime


def close(driver=None):
    print(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Closing browser")
    if driver is None:
        for proc in psutil.process_iter():
            if proc.name().upper() == 'CHROME.EXE':
                proc.kill()
    else:
        driver.quit()
