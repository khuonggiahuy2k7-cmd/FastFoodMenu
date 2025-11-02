from PyQt6 import QtWidgets, QtCore, QtGui
from fastfoodmenu import *
import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Danh sách món ăn với số thứ tự
dishes = {1: "Gà rán", 2: "Gà chiên giòn", 3: "Gà sốt chua cay", 4: "Gà viên", 5: "Burger gà", 6: "Burger gà đặc biệt", 7: "Pepsi", 8: "CocaCola", 9: "7 Up"}

# Giỏ hàng hiện tại dưới dạng từ điển {tên_món: số_lượng}
current_order = {}

# Giá của từng món
prices = {
    "Gà rán": 30000,
    "Gà chiên giòn": 35000,
    "Gà sốt chua cay": 38000,
    "Gà viên": 30000,
    "Burger gà": 40000,
    "Burger gà đặc biệt": 55000,
    "Pepsi": 12000,
    "CocaCola": 12000,
    "7 Up": 12000
}
# Thêm món
def add_item(item_name):
    # Tăng số lượng trong từ điển
    current_order[item_name] = current_order.get(item_name, 0) + 1
    
    # Cập nhật lại giao diện
    update_ui_list()
    update_total()

# Xóa món
def remove_item(item_name):
    # Giảm số lượng trong từ điển
    if item_name in current_order and current_order[item_name] > 0:
        current_order[item_name] -= 1
        
        # Nếu số lượng về 0, xóa món đó khỏi giỏ hàng
        if current_order[item_name] == 0:
            del current_order[item_name]
    
    # Cập nhật lại giao diện
    update_ui_list()
    update_total()

# Cập nhật danh sách món trong UI
def update_ui_list():
    form.lstItems.clear()
    for item, quantity in current_order.items():
        # Lấy giá tiền của món ăn
        price = prices.get(item, 0)  # Dùng .get() lấy dữ liệu
        
        # Định dạng lại giá tiền
        price_text = f"{price:,}đ"
        
        # Tạo chuỗi hiển thị mới
        display_text = f"{item} - {price_text} (x{quantity})"
        
        form.lstItems.addItem(display_text)
# Tính tổng tiền
def calculateTotal(order):
    total = 0
    for item, quantity in order.items():
        if item in prices:
            total += prices[item] * quantity
    return total

# Cập nhật tổng tiền trong UI
def update_total():
    # Tính tổng tiền trực tiếp từ current_order
    total = calculateTotal(current_order) 
    
    # Cập nhật label
    form.lblTotal.setText(f"Tổng tiền: {total:,}đ")

# Hiển thị đơn hàng
def showOrder():
    total = calculateTotal(current_order)
    
    # Lấy chi tiết đơn hàng từ current_order
    orderDetails = "\n".join([f"{item}: {quantity}" for item, quantity in current_order.items()])
    message = f"{orderDetails}\n\nTổng tiền: {total:,}đ" if current_order else "Bạn chưa chọn món nào."

    QtWidgets.QMessageBox.information(window, "Đơn hàng của bạn", message)

# Kết nối các nút với chức năng tương ứng
def connectbuttons():
    form.btnAdd1.clicked.connect(lambda: add_item(dishes[1]))
    form.btnMinus1.clicked.connect(lambda: remove_item(dishes[1]))
    form.btnAdd2.clicked.connect(lambda: add_item(dishes[2]))
    form.btnMinus2.clicked.connect(lambda: remove_item(dishes[2]))
    form.btnAdd3.clicked.connect(lambda: add_item(dishes[3]))
    form.btnMinus3.clicked.connect(lambda: remove_item(dishes[3]))
    form.btnAdd4.clicked.connect(lambda: add_item(dishes[4]))
    form.btnMinus4.clicked.connect(lambda: remove_item(dishes[4]))
    form.btnAdd5.clicked.connect(lambda: add_item(dishes[5]))
    form.btnMinus5.clicked.connect(lambda: remove_item(dishes[5]))
    form.btnAdd6.clicked.connect(lambda: add_item(dishes[6]))
    form.btnMinus6.clicked.connect(lambda: remove_item(dishes[6]))
    form.btnAdd7.clicked.connect(lambda: add_item(dishes[7]))
    form.btnMinus7.clicked.connect(lambda: remove_item(dishes[7]))
    form.btnAdd8.clicked.connect(lambda: add_item(dishes[8]))
    form.btnMinus8.clicked.connect(lambda: remove_item(dishes[8]))
    form.btnAdd9.clicked.connect(lambda: add_item(dishes[9]))
    form.btnMinus9.clicked.connect(lambda: remove_item(dishes[9]))
    form.btnCheckout.clicked.connect(showOrder)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    form = Ui_MainWindow()
    form.setupUi(window) 
    connectbuttons()
    window.show()
    app.exec()

