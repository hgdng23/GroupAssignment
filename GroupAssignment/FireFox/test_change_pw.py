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


def login_cp(driver):
    driver.get("http://localhost/PHP1-main/")
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > section.menu-right > div.login").click()
    time.sleep(1)

    # Điền thông tin vào các trường

    driver.find_element(By.NAME, "username").send_keys("hdang3")  # Trường tài khoản
    driver.find_element(By.NAME, "password").send_keys("123")  # Trường mật khẩu
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)
    alert = Alert(driver)
    alert.accept()
    time.sleep(2)

def test_change_pw(driver):
    driver = webdriver.Firefox()
    login_cp(driver)

    driver.find_element(By.LINK_TEXT, "hdang3").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đổi mật khẩu").click()
    time.sleep(3)
    driver.find_element(By.NAME, "password").send_keys("123")
    time.sleep(2)
    driver.find_element(By.NAME, "password-new").send_keys("123")
    time.sleep(2)
    driver.find_element(By.NAME, "repassword-new").send_keys("123")
    time.sleep(2)
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)

    alert = Alert(driver)
    assert "Đổi mật khẩu thành công !" in alert.text
    driver.quit()

def test_change_pw_fail():
    driver = webdriver.Firefox()
    login_cp(driver)

    driver.find_element(By.LINK_TEXT, "hdang3").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Đổi mật khẩu").click()
    time.sleep(3)
    driver.find_element(By.NAME, "password").send_keys("1234")
    time.sleep(2)
    driver.find_element(By.NAME, "password-new").send_keys("123")
    time.sleep(2)
    driver.find_element(By.NAME, "repassword-new").send_keys("123")
    time.sleep(2)
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)

    alert = Alert(driver)
    assert "Mật khẩu không chính xác !" in alert.text
    driver.quit()


def test_change_pw_fail_2():
    driver = webdriver.Firefox()
    login_cp(driver)

    driver.find_element(By.LINK_TEXT, "hdang3").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Đổi mật khẩu").click()
    time.sleep(3)
    driver.find_element(By.NAME, "password").send_keys("123")
    time.sleep(2)
    driver.find_element(By.NAME, "password-new").send_keys("1234")
    time.sleep(2)
    driver.find_element(By.NAME, "repassword-new").send_keys("12345")
    time.sleep(2)
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)

    alert = Alert(driver)
    assert "Nhập không trùng mật khẩu, vui lòng nhập lại!" in alert.text
    driver.quit()