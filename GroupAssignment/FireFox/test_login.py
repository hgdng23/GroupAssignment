import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def test_login_valid():
    driver = webdriver.Firefox()
    driver.get("http://localhost/PHP1-main/")
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > section.menu-right > div.login").click()
    time.sleep(1)

    # Điền thông tin vào các trường

    driver.find_element(By.NAME, "username").send_keys("hdang")  # Trường tài khoản
    driver.find_element(By.NAME, "password").send_keys("12345")  # Trường mật khẩu
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)
    alert = Alert(driver)
    assert "Đăng nhập thành công!" in alert.text
    # (Tuỳ chọn) Đợi một lúc để xem kết quả hoặc kiểm tra
    driver.quit()



def test_login_invalid():
    driver = webdriver.Firefox()
    driver.get("http://localhost/PHP1-main/")
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > section.menu-right > div.login").click()
    time.sleep(1)

    # Điền thông tin vào các trường

    driver.find_element(By.NAME, "username").send_keys("hdang")  # Trường tài khoản
    driver.find_element(By.NAME, "password").send_keys("123")  # Trường mật khẩu
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)
    alert = Alert(driver)
    assert "Tài khoản và mật khẩu không chính xác !" in alert.text
    # (Tuỳ chọn) Đợi một lúc để xem kết quả hoặc kiểm tra
    driver.quit()

def test_login_SQL_injection():
    driver = webdriver.Firefox()
    driver.get("http://localhost/PHP1-main/")
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > section.menu-right > div.login").click()
    time.sleep(1)

    # Điền thông tin vào các trường

    driver.find_element(By.NAME, "username").send_keys("hdang")  # Trường tài khoản
    driver.find_element(By.NAME, "password").send_keys("' OR '1'='1")  # Trường mật khẩu
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)
    alert = Alert(driver)
    assert "Tài khoản và mật khẩu không chính xác !" in alert.text
    # (Tuỳ chọn) Đợi một lúc để xem kết quả hoặc kiểm tra
    driver.quit()