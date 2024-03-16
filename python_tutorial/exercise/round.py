while(1):
    a = input("Nhập số thập phân a: ")
    b = input("Nhập số nguyên b: ")
    try:
        val_a = float(a)
        val_b = int(b)
        print('{0:.{1}f}'.format(val_a, val_b))
        break
    except:
        print("Sai định dạng, vui lòng nhập lại !!")