while(1):
    n = input("Nhập vào một dãy số nguyên bất kỳ: ")
    try:
        chuoi = str(n)
        s = chuoi.split(" ")
        list_int = map(int, s)
        sumlist = sum(list_int)
        print("tổng của dãy các số nguyên là: ", sumlist)
        break
    except:
        print("không đúng dinh95 dạng, vui lòng nhập lại !!")

    
