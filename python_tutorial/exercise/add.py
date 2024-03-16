#Tính và hiển thị ra màn hình tổng hai số nguyên bất kỳ
a = input("Nhập số nguyên thứ nhất: ")
b = input("Nhập số nguyên thứ hai: ")


#xử lý ngoại lệ input:
try:
    val_a = int(a)
    val_b = int(b)
    print("Tổng 2 số nguyên a + b = ",  val_a + val_b)
except:
    print("Định dạng đầu vào không hợp lệ")