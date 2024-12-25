<?php
use PHPUnit\Framework\TestCase;

class total_whitebox extends TestCase
{
    // Kiểm tra tính toán tổng tiền với dữ liệu hợp lệ
    public function testCalculateTotalPrice()
    {
        $cart = [
            ['num' => 2, 'price' => 50000],  // Sản phẩm 1
            ['num' => 3, 'price' => 30000],  // Sản phẩm 2
        ];
        $total = $this->calculateTotal($cart);
        $this->assertEquals(190000, $total); // 2 * 50000 + 3 * 30000 = 190000
    }

    // Kiểm tra tính toán tổng tiền khi có sản phẩm có số lượng hoặc giá âm
    public function testCalculateTotalPriceWithInvalidData()
    {
        $cart = [
            ['num' => -1, 'price' => 50000],  // Sản phẩm 1 có số lượng âm
            ['num' => 3, 'price' => -30000],  // Sản phẩm 2 có giá âm
        ];
        $total = $this->calculateTotal($cart);
        $this->assertEquals(0, $total); // Logic hiện tại không xử lý số âm
    }

    // Kiểm tra trường hợp giỏ hàng trống
    public function testCalculateTotalPriceWithEmptyCart()
    {
        $cart = [];
        $total = $this->calculateTotal($cart);
        $this->assertEquals(0, $total); // Giỏ hàng trống nên tổng tiền là 0
    }

    // Hàm tính tổng tiền
    // Hàm được tạo từ công thức ở file checkout.php dòng 127
    function calculateTotal($cart) {
        $total = 0;
        foreach ($cart as $item) {
            if ($item['num'] < 0 || $item['price'] < 0) {
                return 0;  // Nếu có số lượng hoặc giá âm, trả về 0
            }
            $total += $item['num'] * $item['price'];
        }
        return $total;
    }
    
}
?>
