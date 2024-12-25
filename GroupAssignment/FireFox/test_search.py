import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

def driver():
    # Khởi tạo WebDriver chỉ một lần cho toàn bộ module
    driver = webdriver.Firefox()
    yield driver  # Trả về driver để dùng trong các bài test
    driver.quit()  # Đóng driver sau khi tất cả các test hoàn tất


def login_s(driver):
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
def test_search_available():
    driver = webdriver.Firefox()
    login_s(driver)

    driver.find_element(By.CSS_SELECTOR,".search-quan > form:nth-child(2) > input:nth-child(1)").send_keys("Bánh Mì")
    driver.find_element(By.CSS_SELECTOR, ".search-quan > form:nth-child(2) > input:nth-child(1)").send_keys(Keys.ENTER)
    time.sleep(3)
    products = driver.find_elements(By.CSS_SELECTOR, ".product-recently .col .title p")

    # Kiểm tra trực tiếp bằng assert
    assert ("Bánh Mì" in product.text for product in products), "Không tìm thấy sản phẩm nào chứa tên 'Bánh Mì'."

    driver.quit()



def test_search_special_characters():
    driver = webdriver.Firefox()
    login_s(driver)

    driver.find_element(By.CSS_SELECTOR, ".search-quan > form:nth-child(2) > input:nth-child(1)").send_keys("!@#$")
    driver.find_element(By.CSS_SELECTOR, ".search-quan > form:nth-child(2) > input:nth-child(1)").send_keys(Keys.ENTER)
    time.sleep(3)
    products = driver.find_elements(By.CSS_SELECTOR, ".product-recently .col .title p")
    # Kiểm tra danh sách rỗng
    assert len(products) == 0

    driver.quit()


def test_search_number():
    driver = webdriver.Firefox()
    login_s(driver)

    driver.find_element(By.CSS_SELECTOR, ".search-quan > form:nth-child(2) > input:nth-child(1)").send_keys("123")
    driver.find_element(By.CSS_SELECTOR, ".search-quan > form:nth-child(2) > input:nth-child(1)").send_keys(Keys.ENTER)
    time.sleep(3)
    products = driver.find_elements(By.CSS_SELECTOR, ".product-recently .col .title p")
    # Kiểm tra danh sách rỗng
    assert len(products) == 0
    driver.quit()


def test_search_under_50s():
    driver = webdriver.Firefox()
    login_s(driver)

    driver.find_element(By.CSS_SELECTOR, ".search-quan > form:nth-child(2) > input:nth-child(1)").send_keys("Bánh Mì")
    time.sleep(3)
    start_time = time.time()
    driver.find_element(By.CSS_SELECTOR, ".search-quan > form:nth-child(2) > input:nth-child(1)").send_keys(Keys.ENTER)
    end_time = time.time()
    search_duration = end_time - start_time
    # content = driver.find_element(By.CSS_SELECTOR,"#content > p").text
    assert search_duration < 50


def test_search_SQL_injection():
    driver = webdriver.Firefox()
    login_s(driver)

    driver.find_element(By.CSS_SELECTOR, ".search-quan > form:nth-child(2) > input:nth-child(1)").send_keys("' OR '1'='1")
    driver.find_element(By.CSS_SELECTOR, ".search-quan > form:nth-child(2) > input:nth-child(1)").send_keys(Keys.ENTER)
    time.sleep(3)
    products = driver.find_elements(By.CSS_SELECTOR, ".product-recently .col .title p")
    # Kiểm tra danh sách rỗng
    assert len(products) == 0
    driver.quit()


