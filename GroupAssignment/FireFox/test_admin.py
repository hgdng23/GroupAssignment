import random
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


def login(driver):
    driver.get("http://localhost/PHP1-main/index.php")
    # Nhấn đăng nhập
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > div > section.menu-right > div.login > a").click()
    time.sleep(2)
    # Nhập username
    driver.find_element(By.CSS_SELECTOR, "#wrapper > div > form > div:nth-child(2) > input").send_keys("AdminThanh")
    time.sleep(2)
    # Nhập password
    driver.find_element(By.CSS_SELECTOR, "#wrapper > div > form > div:nth-child(3) > input").send_keys("thanh1010")
    time.sleep(2)
    # Nhấn nút đăng nhập
    driver.find_element(By.CSS_SELECTOR, "#wrapper > div > form > div:nth-child(5) > input").click()
    time.sleep(2)
    # Xác nhận alert
    alert = Alert(driver)
    alert.accept()
    time.sleep(2)



def test_check_quantity_category(driver):
    login(driver)

    # lấy số lượng category ngoài dashboard
    count_category = int(
        driver.find_element(By.CSS_SELECTOR, "#wrapper > div > main > section.dashboard > div > div.sp.dm > span").text)
    time.sleep(2)
    # xem chi tiết
    driver.find_element(By.CSS_SELECTOR,
                        "#wrapper > div > main > section.dashboard > div > div.sp.dm > p:nth-child(3) > a").click()
    time.sleep(2)

    rows = driver.find_elements(By.CSS_SELECTOR, "body > div > div > table > tbody > tr")
    max_stt = 0
    for row in rows:
        # Lấy số thứ tự (giả sử số thứ tự nằm ở cột đầu tiên)
        stt = int(row.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text)
        # Cập nhật giá trị lớn nhất
        if stt > max_stt:
            max_stt = stt

    assert count_category == max_stt
    # Đóng trình duyệt
    driver.quit()


def test_add_category(driver):
    login(driver)
    time.sleep(2)
    # xem tab danh mục
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > ul > li:nth-child(2) > a").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "body > div > div > a > button").click()
    time.sleep(2)
    category_name = "Ăn vặt"
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys(category_name)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "body > div > div > div.panel-body > form > button").click()
    time.sleep(2)

    rows = driver.find_elements(By.CSS_SELECTOR, "body > div > div > table > tbody > tr")

    for row in rows:
        # Lấy nội dung của cột chứa tên danh mục (giả sử cột 2)
        row_category_name = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
        if row_category_name == category_name:
            assert category_name == row_category_name
            break
    # Đóng trình duyệt
    driver.quit()


def test_del_category(driver):
    login(driver)
    time.sleep(2)
    # xem tab danh mục
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > ul > li:nth-child(2) > a").click()
    time.sleep(2)

    rows_before = driver.find_elements(By.CSS_SELECTOR, "body > div > div > table > tbody > tr")
    count_before = len(rows_before)

    # xóa danh mục
    driver.find_element(By.CSS_SELECTOR,
                        ".table > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(4) > button:nth-child(1)").click()
    time.sleep(2)
    alert = Alert(driver)
    alert.accept()
    time.sleep(2)
    rows_after = driver.find_elements(By.CSS_SELECTOR, "body > div > div > table > tbody > tr")
    count_after = len(rows_after)

    assert count_before > count_after
    # Đóng trình duyệt
    driver.quit()


def test_add_product(driver):
    login(driver)

    # xem tab sản phẩm
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > ul > li:nth-child(3) > a").click()
    time.sleep(2)
    # thêm sản phẩm
    driver.find_element(By.CSS_SELECTOR, "body > div > div > a > button").click()
    time.sleep(2)
    product_name = "Bún thái"
    driver.find_element(By.CSS_SELECTOR, "#title").send_keys(product_name)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#id_category").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#id_category > option:nth-child(3)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#price").send_keys("30000")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#number").send_keys("3")
    time.sleep(2)
    # chọn tệp
    driver.find_element(By.CSS_SELECTOR, "#exampleFormControlFile1").send_keys("C:\\Users\\daoho\\Downloads\\bunthai.jpg")
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR,
                        ".note-editable").send_keys(product_name + " ngon dữ lun á")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "body > div > div > div.panel-body > form > button").click()
    time.sleep(2)
    # qua trang 5
    driver.find_element(By.CSS_SELECTOR, "body > div > ul > li:nth-child(5) > a").click()
    time.sleep(2)

    rows = driver.find_elements(By.CSS_SELECTOR, "body > div > div > table > tbody > tr")
    for row in rows:
        # Lấy nội dung của cột chứa tên danh mục (giả sử cột 2)
        row_category_name = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
        if row_category_name == product_name:
            assert product_name == row_category_name
            break

    # Đóng trình duyệt
    driver.quit()


def test_del_product(driver):
    login(driver)
    # Xem tab sản phẩm
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > ul > li:nth-child(3) > a").click()
    time.sleep(2)
    # Qua trang 5
    driver.find_element(By.CSS_SELECTOR, "body > div > ul > li:nth-child(5) > a").click()
    time.sleep(2)
    # Lặp qua các hàng trong bảng để tìm sản phẩm "Bún thái"
    rows = driver.find_elements(By.CSS_SELECTOR, "body > div > div > table > tbody > tr")
    for i, row in enumerate(rows, start=1):
        product_name = row.find_element(By.CSS_SELECTOR, f"tr:nth-child({i}) > td:nth-child(3)").text

        if product_name == "Bún thái":
            # Tìm nút xóa trong cột thứ 9 của cùng một dòng và nhấn
            delete_button = row.find_element(By.CSS_SELECTOR, f"tr:nth-child({i}) > td:nth-child(9) > button")
            delete_button.click()
            alert = Alert(driver)
            alert.accept()
            print("Đã nhấn nút xóa sản phẩm 'Bún thái'.")
            time.sleep(2)  # Đợi trang cập nhật sau khi xóa
            break
    # Qua trang 5
    driver.find_element(By.CSS_SELECTOR, "body > div > ul > li:nth-child(5) > a").click()
    time.sleep(2)
    # Kiểm tra lại xem sản phẩm "Bún thái" có còn trong bảng không
    rows = driver.find_elements(By.CSS_SELECTOR, "body > div > div > table > tbody > tr")
    product_found = False
    for i, row in enumerate(rows, start=1):
        product_name = row.find_element(By.CSS_SELECTOR, f"tr:nth-child({i}) > td:nth-child(3)").text
        if product_name == "Bún thái":
            product_found = True
            break

    # Assert để đảm bảo sản phẩm đã bị xóa
    assert not product_found, "Sản phẩm 'Bún thái' vẫn còn trong bảng sau khi xóa."

    # Đóng trình duyệt
    driver.quit()


def test_update_product(driver):
    login(driver)

    # Xem tab sản phẩm
    driver.find_element(By.CSS_SELECTOR, "#wrapper > header > ul > li:nth-child(3) > a").click()
    time.sleep(2)
    # Nhấn nút Sửa
    driver.find_element(By.CSS_SELECTOR,
                        "body > div > div > table > tbody > tr:nth-child(1) > td:nth-child(8) > a > button").click()
    time.sleep(2)
    # Sửa giá
    price_edit = "35000"
    driver.find_element(By.CSS_SELECTOR, "#price").clear()
    driver.find_element(By.CSS_SELECTOR, "#price").send_keys(price_edit)
    time.sleep(2)
    # Sửa số lượng
    number_edit = "45"
    driver.find_element(By.CSS_SELECTOR, "#number").clear()
    driver.find_element(By.CSS_SELECTOR, "#number").send_keys(number_edit)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#exampleFormControlFile1").send_keys("C:\\Users\\daoho\\Downloads\\banhsocola.png")
    time.sleep(2)
    # Lưu
    driver.find_element(By.CSS_SELECTOR, "body > div > div > div.panel-body > form > button").click()
    time.sleep(2)

    quan = driver.find_element(By.CSS_SELECTOR,
                               "body > div > div > table > tbody > tr:nth-child(1) > td:nth-child(5)").text
    price_text = driver.find_element(By.CSS_SELECTOR,
                                     "body > div > div > table > tbody > tr:nth-child(1) > td:nth-child(4)").text
    price_number = price_text.replace(".", "").replace(" VNĐ", "")

    assert quan == number_edit
    assert price_number == price_edit

    # Đóng trình duyệt
    driver.quit()


def test_update_status_order(driver):
    login(driver)

    # Xem tab đơn hàng
    driver.find_element(By.CSS_SELECTOR,
                        "#wrapper > div > main > section.dashboard > div > div.sp.dh > p:nth-child(3) > a").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,
                        "body > div > div > div.panel-body > form > table > tbody > tr:nth-child(1) > td:nth-child(8) > a").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#status").click()
    driver.find_element(By.CSS_SELECTOR, "#status > option:nth-child(3)").click()
    time.sleep(2)
    status_after = driver.find_element(By.CSS_SELECTOR, "#status > option:nth-child(3)").text
    driver.find_element(By.CSS_SELECTOR,
                        "body > div > div > div.panel-body > form > table > tbody > tr > td:nth-child(8) > button").click()
    time.sleep(2)
    alert = Alert(driver)
    alert.accept()
    status_now = driver.find_element(By.CSS_SELECTOR,
                                     "body > div > div > div.panel-body > form > table > tbody > tr:nth-child(1) > td.green.b-500").text
    time.sleep(5)
    assert status_after == status_now
    # Đóng trình duyệt
    driver.quit()

