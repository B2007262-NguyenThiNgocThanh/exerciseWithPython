# dấu "#" : ghi chú
# in ra màn hình dùng lệnh print()
print("hello, I am To Hanh.")

# chuỗi có dạng môt commet khi đặt trong lệnh print("# đây là một chuỗi !!!")
print("# đây là một chuỗi !!!")

##### shift + chuột phải -> open in terminal sẽ nhanh hơn

# xem các thư viên trong python: https://pypi.python.org 


# ---------- biến trong python ----------- #

# Biến (variable) : là tên của một vùng trong bộ nhớ RAM, được sử dụng để lưu trữ thông tin
# 					có thể gán tt cho một biến & có thể lấy nó ra khi gọi nó.
a = 532333
b = 234234
c = a+b
print(c)

# cú pháp: <tên biến > = <giá trị của biến>
tuoi = 17
ten = "tui ten to hanh"
Pi = 3.14

# khởitạo nhiều biến: 
# < tên biến 1> , <tên biến 2>,..,<tên biến n> = <gia1 trị biến 1>, <giá trị biến 2>,..,<gia1 trị biến n>
tuoi, ten, Pi = 17, "tui ten to hanh", 3.14

# kiểm tra kiểu dl của biến dùng hàm type ():  type( <tên biến> )
type(tuoi) # integer
type(ten) # str
type(Pi)# float
# để xem: print(type(...))

#----------- KIỂU SỔ TRONG PYTHON -----------#

#import thư viện: lấy toàn bộ nội dung thư viện decimal
from decimal import*

# láy tối đa 30 chữ số phần nguyên & phần thập 
getcontext().prec = 3
print("\nKhi không có decimal:")
print(10/3)
print("\nkhi có decimal(chỉ cần 1 bên có decimal->biểu thức là decimal:")
print(Decimal(10)/Decimal(3))


# để tạo phân số trong python->sử dụng hàm Fraction()
from fractions import*
Fraction(6,9) # tạo ra một phân số có tử = 6, mẫu = 9 
print(Fraction(6,9))

#--------------COMPLEX-SỐ PHỨC-----------#
# <phần thực> + <phần ảo> j với j là phần ảo & j^2 = -1
cpl = complex(2, 5)
print("đây là ví dụ về số phức: ", cpl)
#lấy ra phần thực
print("lấy ra phần thực: ", cpl.real)
print("lấy ra phần ảo: ", cpl.imag)

#------------------math trong python ---------------#

import math
#cú pháp: <tên thư viện>.<tên hàm>
x = 23.355

print("\n Trá về phần nguyên của số x: ",math.trunc(x))
print("\n Lấy ước chung lớn nhất: ",math.gcd(2,3)) #ucln
print("\nlấy trị tuyệt đối: ",math.fabs(-23))


#--------------------CHUỖI --------------#

# chuỗi: '' , "", ''' ''' , """ """
str = ''' 'I"m Newbie' '''
print(str)

# chuỗi nhiều dòng:
str1 = ''' hello
... tui là to hanh '''
print(str1)

#--------------- ESCAPE SEQUENCE -------------#
# KN: là một chuỗi ( chính xác là kí tự) đặc biệt trong python,bắt đàu bằng dấu "\"
# VD: \n, \t

print("\\")
print("alert - phát ra 1 tiếng bíp: \a")
print("đưa con trỏ  về lại 1 khoangr trắng: abcd\be ")
print("tui \t la")

#-------------- XỬ LÝ CHUỖI ----------#

# chuỗi trần : r
print(r"Ví dụ về chuỗi :, \nếu một ngày nào đó")

# Nối chuỗi:
str1 = "tui là "
str2 = "Tờ Hanh"
print("đây là ví dụ nối chuỗi: ", str1+str2)

# Toán tử nhân cho chuỗi
str = "hello.\n"
result = str*3
print(result)

# kiểm tra 1 chuỗi có nằm bên trong một chuỗi khác hay không
strA = "hom nay mua roi"
strB = "h"
strC = "H"
result1 = strB in strA
result2 = strC in strA
print(result1) #true
print(result2) #false

strD = strA[0:None]
strE = strA[:-1]
strF = strA[3:len(strA)]
print(strE)
print(strF)
print(strD)
s=""
# n(strA) = 15 (index)
for i in range(0, len(strA)):
	s = s + strA[i]
print(s)

# cắt chuỗi từ phải qua trái - ::
s1 = "hom nay"
result3 = s1[None:None:2] #từ vị trí đầu tới vị trí cuối, mỗi lần 2 vị trí
print(result3)



# chuyển chuỗi thành số => ép kiểu
# chuyển số thành chuỗi
text = f"69" + "5"
print(text)

a = 'My name is %s %s' %('Tờ Hanh', "qing")
s = '%s %s'
str4 = s % ('1', '2')
print(str4)
print(a)

name='to hanh'
address = '123, nk'
phone ='0189489'
result4 = f'hoten: {name}\nDiachi:{address}\nsdt: {phone}'
print(result4)

# định dạng format
print('a:{}, b:{},c:{}'.format(1,2,3))
print('a:%d, b:%d, c:%d'%(1,2,4))

#chuyển kí tự thường thành hoa & hoa thành thường
str5 = 'to Hanh'
result = str5.swapcase()
print(result) 
# in hoa toàn bộ chữ cái 
result1 = str5.upper()
print(result1)
# in thường
result2 = str5.lower()
print(result2)
# in ký tự đầu mỗi chữ
result3 = str5.title()
print(result3)