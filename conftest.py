from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import logging
import os


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def log_path():
    suffix = datetime.now().strftime("%y%m%d_%H%M%S")
    log_path = 'log_file_' + suffix + '.log'

    yield log_path

    logger = logging.getLogger('selenium')
    for handler in logger.handlers:
        logger.removeHandler(handler)
        handler.close()

    os.remove(log_path)
