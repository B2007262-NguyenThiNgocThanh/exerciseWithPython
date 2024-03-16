while(1):
    a = input("Nhập số thập phân a: ")
    try:
        val_a = int(a)
        print('Số thập phân %d trong hệ bát phân là %o' %(val_a, val_a))
        break
    except:
        print("Không đúng định dạng,vui lòng nhập lại !!!")



