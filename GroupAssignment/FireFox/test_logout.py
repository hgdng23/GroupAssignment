import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

def test_logout():
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
    # (Tuỳ chọn) Đợi một lúc để xem kết quả hoặc kiểm tra
    alert.accept()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > section.menu-right > div.login > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > section.menu-right > div.login > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > section.menu-right > div.login > div").click()
    time.sleep(3)
    assert "http://localhost/PHP1-main/index.php" in driver.current_url
    driver.quit()