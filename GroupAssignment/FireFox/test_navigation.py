import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

@pytest.fixture(scope="module")
def driver():
    # Khởi tạo WebDriver chỉ một lần cho toàn bộ module
    driver = webdriver.Firefox()
    yield driver  # Trả về driver để dùng trong các bài test
    driver.quit()  # Đóng driver sau khi tất cả các test hoàn tất


def login_navi(driver):
    driver.get("http://localhost/PHP1-main/")
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > section.menu-right > div.login").click()
    time.sleep(1)

    # Điền thông tin vào các trường

    driver.find_element(By.NAME, "username").send_keys("hdang")  # Trường tài khoản
    driver.find_element(By.NAME, "password").send_keys("12345")  # Trường mật khẩu
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)
    alert = Alert(driver)
    alert.accept()
    time.sleep(2)

def test_navigator():
    driver = webdriver.Firefox()
    login_navi(driver)
    driver.find_element(By.CSS_SELECTOR,"#wrapper > header > div > nav > ul > li:nth-child(1) > a").click()
    time.sleep(3)
    assert "http://localhost/PHP1-main/index.php" in driver.current_url
    driver.quit()

def test_navigator_cart():
    driver = webdriver.Firefox()
    login_navi(driver)
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > section.menu-right > div.cart > a > img").click()
    time.sleep(3)
    assert "http://localhost/PHP1-main/cart.php" in driver.current_url
    driver.quit()

def test_navigator_about():
    driver = webdriver.Firefox()
    login_navi(driver)
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > nav > ul > li:nth-child(3) > a").click()
    time.sleep(3)
    assert "http://localhost/PHP1-main/about.php" in driver.current_url
    driver.quit()

def test_navigator_contact():
    driver = webdriver.Firefox()
    login_navi(driver)
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > nav > ul > li:nth-child(4) > a").click()
    time.sleep(3)
    assert "http://localhost/PHP1-main/sendMail.php" in driver.current_url

    driver.quit()
