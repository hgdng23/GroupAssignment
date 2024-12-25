import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def test_register_valid():
    driver = webdriver.Firefox()
    driver.get("http://localhost/PHP1-main/")
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > section.menu-right > div.login").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#wrapper > div > form > div:nth-child(5) > p > a").click()
    time.sleep(1)
    # Điền thông tin vào các trường
    driver.find_element(By.NAME, "name").send_keys("Hoang Dang")  # Trường họ và tên
    driver.find_element(By.NAME, "username").send_keys("hdang12")  # Trường tài khoản
    driver.find_element(By.NAME, "password").send_keys("12345")  # Trường mật khẩu
    driver.find_element(By.NAME, "repassword").send_keys("12345")  # Trường nhập lại mật khẩu
    driver.find_element(By.NAME, "phone").send_keys("123")  # Trường số điện thoại
    driver.find_element(By.NAME, "email").send_keys("dang234@gmail.com")  # Trường email

    # Click nút đăng ký
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)
    alert = Alert(driver)
    assert "Bạn đăng ký thành công!" in alert.text
    # (Tuỳ chọn) Đợi một lúc để xem kết quả hoặc kiểm tra
    driver.quit()

#trùng email
def test_register_invalid_email():
    driver = webdriver.Firefox()
    driver.get("http://localhost/PHP1-main/")
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > section.menu-right > div.login").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#wrapper > div > form > div:nth-child(5) > p > a").click()
    time.sleep(1)
    # Điền thông tin vào các trường
    driver.find_element(By.NAME, "name").send_keys("Hoang Dang")  # Trường họ và tên
    driver.find_element(By.NAME, "username").send_keys("hdang12")  # Trường tài khoản
    driver.find_element(By.NAME, "password").send_keys("12345")  # Trường mật khẩu
    driver.find_element(By.NAME, "repassword").send_keys("12345")  # Trường nhập lại mật khẩu
    driver.find_element(By.NAME, "phone").send_keys("123")  # Trường số điện thoại
    driver.find_element(By.NAME, "email").send_keys("dang234@gmail.com")  # Trường email

    # Click nút đăng ký
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)
    alert = Alert(driver)
    assert "Tài khoản hoặc Email đã được sử dụng!" in alert.text
    # (Tuỳ chọn) Đợi một lúc để xem kết quả hoặc kiểm tra
    driver.quit()

# xác nhận mật khẩu sai
def test_register_invalid_pw():
    driver = webdriver.Firefox()
    driver.get("http://localhost/PHP1-main/")
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > section.menu-right > div.login").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#wrapper > div > form > div:nth-child(5) > p > a").click()
    time.sleep(1)
    # Điền thông tin vào các trường
    driver.find_element(By.NAME, "name").send_keys("Hoang Dang")  # Trường họ và tên
    driver.find_element(By.NAME, "username").send_keys("hdang13")  # Trường tài khoản
    driver.find_element(By.NAME, "password").send_keys("12345")  # Trường mật khẩu
    driver.find_element(By.NAME, "repassword").send_keys("1234")  # Trường nhập lại mật khẩu
    driver.find_element(By.NAME, "phone").send_keys("123")  # Trường số điện thoại
    driver.find_element(By.NAME, "email").send_keys("dang234@gmail.com")  # Trường email

    # Click nút đăng ký
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)
    alert = Alert(driver)
    assert "Nhập không trùng mật khẩu, vui lòng đăng ký lại!" in alert.text
    # (Tuỳ chọn) Đợi một lúc để xem kết quả hoặc kiểm tra
    driver.quit()


