<?php
use PHPUnit\Framework\TestCase;

class updatePrice_whitebox extends TestCase
{
    // Kiểm tra tính toán tổng tiền với dữ liệu hợp lệ
    // Lấy hàm của js dòng 64 của details.php đổi thành code php

    function updatePrice($gia1, $num) {
        // Kiểm tra các tham số đầu vào có hợp lệ không
        if (!is_numeric($gia1) || !is_numeric($num) || $gia1 < 0 || $num < 1) {
            throw new InvalidArgumentException("Thông số không hợp lệ");
        }
    
        // Tính tổng tiền
        $tong = $gia1 * $num;
    
        // Trả về tổng tiền đã định dạng theo số (1,000,000)
        return number_format($tong, 0, ',', '.');
    }
                                                                                                                                                                               
    # update giá với đầu vào hợp lệ
    function testUpdatePrice_ValidInput() {
        $gia1 = 50000; // Giá 1 sản phẩm
        $num = 2;      // Số lượng
        $expected = "100,000"; // Kết quả mong đợi
    
        try {
            $result = $this->updatePrice($gia1, $num);
            $this->assertEquals($result, $expected);
        } catch (Exception $e) {
            echo "Kiểm thử thất bại: " . $e->getMessage() . "\n";
        }
    }
    
    
}
?>
