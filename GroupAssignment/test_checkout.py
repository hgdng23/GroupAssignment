import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Đảm bảo ChromeDriver đã được cấu hình đúng
    yield driver
    driver.quit()
def test_check_out(driver):
    # Mở trang đăng nhập
    driver.get("http://localhost/PHP1-main/login/login.php")
    
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("khoa")
    time.sleep(2)
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("123456")
    time.sleep(2)
    
    login_button = driver.find_element(By.NAME, "submit")
    login_button.click()
    time.sleep(2)
    
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()

    WebDriverWait(driver, 10).until(EC.url_contains("index.php"))
    assert "index.php" in driver.current_url, "Đăng nhập thất bại!"
    time.sleep(3)

    # Chọn sản phẩm đầu tiên
    product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/section/section[1]/div[2]/div/div[1]/a/img"))
    )
    product.click()

    # Nhấn vào nút thêm vào giỏ hàng
    buynow = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/section/section[1]/div/section/div[1]/div/button[2]"))
    )
    buynow.click()
    time.sleep(3)

    fullname = driver.find_element(By.NAME, "fullname")
    fullname.send_keys("khoa")
    time.sleep(2)

    email = driver.find_element(By.NAME, "email")
    email.send_keys("khoa@gmail.com")
    time.sleep(2)

    number = driver.find_element(By.NAME, "phone_number")
    number.send_keys("0969564444")
    time.sleep(2)

    address = driver.find_element(By.NAME, "address")
    address.send_keys("khoa")
    time.sleep(2)

    # Tìm và click vào nút Đặt Hàng
    dathang = driver.find_element(By.XPATH, "/html/body/div[2]/main/section/form/div/div/div[2]/a/button")
    dathang.click()
    time.sleep(2)
    
    # Chờ alert xuất hiện và xử lý
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()








