import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
import random


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Đảm bảo ChromeDriver đã được cấu hình đúng
    yield driver
    driver.quit()

def login_user(driver):
    driver.get("http://localhost/PHP1-main/index.php")
    # Nhấn đăng nhập
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > section.menu-right > div.login > a").click()
    time.sleep(2)
    # Nhập username
    driver.find_element(By.CSS_SELECTOR, "#wrapper > div > form > div:nth-child(2) > input").send_keys("hdang2")
    time.sleep(2)
    # Nhập password
    driver.find_element(By.CSS_SELECTOR, "#wrapper > div > form > div:nth-child(3) > input").send_keys("12345")
    time.sleep(2)
    # Nhấn nút đăng nhập
    driver.find_element(By.CSS_SELECTOR, "#wrapper > div > form > div:nth-child(5) > input").click()
    time.sleep(2)
    # Xác nhận alert
    alert = Alert(driver)
    alert.accept()
    time.sleep(2)


def test_add_to_cart(driver):
    driver = webdriver.Chrome()
    login_user(driver)
    # Tìm sản phẩm bằng XPath và click vào nó
    product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/section/section[1]/div[2]/div/div[1]/a/img"))
    )
    product.click()

    # Nhấn vào nút thêm vào giỏ hàng
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/main/div/section/section[1]/div/section/div[1]/div/button[1]"))
    )
    add_to_cart_button.click()
    time.sleep(3)

    # Kiểm tra giá trị giỏ hàng lớn hơn 1
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/section[2]/div[1]/span"))
    )
    cart_value = int(cart_count.text)  # Lấy giá trị văn bản và chuyển thành số nguyên

    assert cart_value > 0, f"Giá trị giỏ hàng không hợp lệ, giá trị hiện tại: {cart_value}"


def test_select_quantity(driver):
    driver.get("http://localhost/PHP1-main/index.php")
    # Sau khi bấm vào sản phẩm
    product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/section/section[1]/div[2]/div/div[1]/a/img"))
    )
    product.click()

    # Nhập số lượng = 5 vào ô input
    quantity_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "num"))
    )
    quantity_input.clear()  # Làm sạch giá trị hiện tại
    quantity_input.send_keys("5")  # Nhập số lượng 5

    # Kiểm tra giá trị số lượng đã được thay đổi thành 5
    assert quantity_input.get_attribute(
        "value") == "5", f"Số lượng không đúng, hiện tại: {quantity_input.get_attribute('value')}"
    # Nhấn vào nút thêm vào giỏ hàng
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/main/div/section/section[1]/div/section/div[1]/div/button[1]"))
    )
    add_to_cart_button.click()
    time.sleep(3)

    # Kiểm tra giá trị giỏ hàng lớn hơn 1
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/section[2]/div[1]/span"))
    )
    cart_value = int(cart_count.text)  # Lấy giá trị văn bản và chuyển thành số nguyên

    assert cart_value > 0, f"Giá trị giỏ hàng không hợp lệ, giá trị hiện tại: {cart_value}"


def test_add_products_to_cart(driver):
    driver.get("http://localhost/PHP1-main/")  # Quay lại trang danh sách sản phẩm
    # Bước 1: Thêm sản phẩm 1 vào giỏ hàng
    product_1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/section/section[1]/div[2]/div/div[1]/a/img"))
    )
    product_1.click()

    add_to_cart_button_1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/main/div/section/section[1]/div/section/div[1]/div/button[1]"))
    )
    add_to_cart_button_1.click()
    time.sleep(3)  # Đợi để thao tác hoàn tất

    # Kiểm tra giá trị giỏ hàng sau khi thêm sản phẩm 1
    cart_count_1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/section[2]/div[1]/span"))
    )
    cart_value_1 = int(cart_count_1.text)
    assert cart_value_1 > 0, f"Giá trị giỏ hàng không hợp lệ, giá trị hiện tại: {cart_value_1}"

    # Bước 2: Quay lại trang chính để chọn sản phẩm 2
    driver.get("http://localhost/PHP1-main/")  # Quay lại trang danh sách sản phẩm

    # Bước 3: Thêm sản phẩm 2 vào giỏ hàng
    product_2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/section/section[1]/div[2]/div/div[2]/a/img"))
    )
    product_2.click()

    add_to_cart_button_2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/main/div/section/section[1]/div/section/div[1]/div/button[1]"))
    )
    add_to_cart_button_2.click()
    time.sleep(3)  # Đợi để thao tác hoàn tất

    # Kiểm tra giá trị giỏ hàng sau khi thêm sản phẩm 2
    cart_count_2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/section[2]/div[1]/span"))
    )
    cart_value_2 = int(cart_count_2.text)
    assert cart_value_2 > 00, f"Giá trị giỏ hàng không tăng sau khi thêm sản phẩm 2, giá trị hiện tại: {cart_value_2}"

    # Bước 4: Quay lại trang chính để chọn sản phẩm 3
    driver.get("http://localhost/PHP1-main/")  # Quay lại trang danh sách sản phẩm

    # Bước 5: Thêm sản phẩm 3 vào giỏ hàng
    product_3 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/section/section[1]/div[2]/div/div[4]/a/img"))
    )
    product_3.click()

    add_to_cart_button_3 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/main/div/section/section[1]/div/section/div[1]/div/button[1]"))
    )
    add_to_cart_button_3.click()
    time.sleep(3)  # Đợi để thao tác hoàn tất

    # Kiểm tra giá trị giỏ hàng sau khi thêm sản phẩm 3
    cart_count_3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/section[2]/div[1]/span"))
    )
    cart_value_3 = int(cart_count_3.text)
    assert cart_value_3 > 0, f"Giá trị giỏ hàng không tăng sau khi thêm sản phẩm 3, giá trị hiện tại: {cart_value_3}"


def test_add_random_products_to_cart(driver):
    # Mở trang danh sách sản phẩm
    driver.get("http://localhost/PHP1-main/")  # URL của trang chính

    # Danh sách sản phẩm với các XPath của sản phẩm và nút thêm vào giỏ hàng
    products = [
        {
            "product_xpath": "/html/body/div[1]/main/div/section/section[1]/div[2]/div/div[1]/a/img",
            "add_to_cart_button_xpath": "/html/body/div[1]/main/div/section/section[1]/div/section/div[1]/div/button[1]"
        },
        {
            "product_xpath": "/html/body/div[1]/main/div/section/section[1]/div[2]/div/div[2]/a/img",
            "add_to_cart_button_xpath": "/html/body/div[1]/main/div/section/section[1]/div/section/div[1]/div/button[1]"
        },
        {
            "product_xpath": "/html/body/div[1]/main/div/section/section[2]/div[2]/div[1]/div[1]/a/img",
            "add_to_cart_button_xpath": "/html/body/div[1]/main/div/section/section[1]/div/section/div[1]/div/button[1]"
        },
        {
            "product_xpath": "/html/body/div[1]/main/div/section/section[1]/div[2]/div/div[4]/a/img",
            "add_to_cart_button_xpath": "/html/body/div[1]/main/div/section/section[1]/div/section/div[1]/div/button[1]"
        },
        {
            "product_xpath": "/html/body/div[1]/main/div/section/section[2]/div[2]/div[1]/div[4]/a/img",
            "add_to_cart_button_xpath": "/html/body/div[1]/main/div/section/section[1]/div/section/div[1]/div/button[1]"
        }
    ]

    # Chọn ngẫu nhiên 3 sản phẩm từ danh sách
    selected_products = random.sample(products, 3)

    # Thêm từng sản phẩm đã chọn vào giỏ hàng
    for i, product in enumerate(selected_products):
        # Thêm sản phẩm vào giỏ hàng
        product_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, product["product_xpath"]))
        )
        product_element.click()

        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, product["add_to_cart_button_xpath"]))
        )
        add_to_cart_button.click()
        time.sleep(3)  # Đợi để thao tác hoàn tất

        # Kiểm tra giá trị giỏ hàng sau khi thêm sản phẩm
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/section[2]/div[1]/span"))
        )
        cart_value = int(cart_count.text)  # Lấy giá trị văn bản và chuyển thành số nguyên

        assert cart_value > 0, f"Giá trị giỏ hàng không hợp lệ, giá trị hiện tại: {cart_value}"

        # Quay lại trang chính sau khi thêm sản phẩm vào giỏ hàng
        if i < 2:  # Nếu chưa thêm hết 3 sản phẩm, quay lại trang chính để chọn sản phẩm tiếp theo
            driver.get("http://localhost/PHP1-main/")  # Quay lại trang danh sách sản phẩm

    # Kiểm tra tổng số sản phẩm trong giỏ hàng
    cart_count_final = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/section[2]/div[1]/span"))
    )
    final_cart_value = int(cart_count_final.text)

    assert final_cart_value > 0, f"Giá trị giỏ hàng không hợp lệ, giá trị hiện tại:: {final_cart_value}"


def test_remove_all_products_from_cart(driver):
    driver.get("http://localhost/PHP1-main/")

    # Tìm và click vào nút giỏ hàng
    cart_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//img[@src='images/icon/cart.svg']"))
    )
    cart_icon.click()
    time.sleep(2)  # Đợi 2 giây cho giỏ hàng mở ra

    while True:
        try:
            # Tìm và click vào nút xóa sản phẩm
            delete_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-danger') and text()='Xoá']"))
            )
            delete_button.click()
            time.sleep(2)  # Đợi 2 giây để hành động xóa hoàn tất
        except:
            # Khi không tìm thấy nút xóa (giỏ hàng trống), thoát khỏi vòng lặp
            break

    # Kiểm tra số lượng sản phẩm trong giỏ hàng sau khi xóa tất cả
    # Kiểm tra tổng số sản phẩm trong giỏ hàng
    cart_count_final = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/header/div/section[2]/div[1]/span"))
    )
    final_cart_value = int(cart_count_final.text)

    assert final_cart_value == 0, f"Giá trị giỏ hàng không hợp lệ, giá trị hiện tại:: {final_cart_value}"


def test_select_quantity_fail(driver):
    driver.get("http://localhost/PHP1-main/index.php")

    # Sau khi bấm vào sản phẩm
    product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/section/section[1]/div[2]/div/div[1]/a/img"))
    )
    product.click()

    # Nhập số lượng = -1 vào ô input
    quantity_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "num"))
    )
    quantity_input.clear()  # Làm sạch giá trị hiện tại
    quantity_input.send_keys("-1")  # Nhập số lượng -1

    # Kiểm tra giá trị số lượng đã được thay đổi thành -1
    assert quantity_input.get_attribute(
        "value") == "-1", f"Số lượng không đúng, hiện tại: {quantity_input.get_attribute('value')}"

    # Nhấn vào nút thêm vào giỏ hàng
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/main/div/section/section[1]/div/section/div[1]/div/button[1]"))
    )
    add_to_cart_button.click()
    time.sleep(3)
    driver.get("http://localhost/PHP1-main/cart.php")

    # Kiểm tra giá tiền là số nguyên
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "<span class='red bold'>-30.000<span> VNĐ</span></span>"))
    )
    cart_value_text = cart_count.text.strip().replace(' VNĐ', '').replace('.', '')  # Xóa " VNĐ" và dấu chấm
    try:
        cart_value = int(cart_value_text)  # Chuyển chuỗi thành số nguyên
        assert cart_value > 0, f"Giá trị giỏ hàng không hợp lệ, giá trị hiện tại: {cart_value}"
    except ValueError:
        raise AssertionError(f"Giá trị giỏ hàng không phải là số nguyên hợp lệ, giá trị hiện tại: {cart_value_text}")





