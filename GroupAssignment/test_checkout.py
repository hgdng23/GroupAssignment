import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

def test_checkout():
    driver = webdriver.Chrome()
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

    driver.find_element(By.CSS_SELECTOR,".product-recently > div:nth-child(1) > div:nth-child(2) > a:nth-child(1) > img:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,".buy-now").click()
    time.sleep(3)

    driver.find_element(By.ID, "usr").send_keys("dang")
    driver.find_element(By.ID, "email").send_keys("dang@gmail.com")
    driver.find_element(By.ID, "phone_number").send_keys("123")
    driver.find_element(By.ID, "address").send_keys("abc")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,".btn").click()
    time.sleep(3)
    alert = Alert(driver)
    assert "Đặt hàng thành công!" in alert.text
    driver.quit()