# print ("Hello, World!")
# a =input("Nhập vào số a: ")
# b =input("Nhập vào số b: ")
# print("Tổng của a và b là: ", int(a)+int(b))

# s1.Print: in dữ liệu ra màn hình
# print('Xin', 'chào', sep='-', end='-') #sep: dấu phân cách, end: kết thúc bằng gì
# print('bạn')

# s2.Input: nhập dữ liệu từ bàn phím
# name = input("Nhập vào tên của bạn: ")
# print("xin chào" + f"{name}") 

# s3.Biến số (variable) là một khái niệm cơ bản trong lập trình, biến dùng để lưu trữ thông tin, các tham chiếu và sử dụng để thao tác dữ liệu
# a = 5 #kiểu int
# b = 5.5 #kiểu float
# c = "Hello" #kiểu str

# x, y, z = 1, 2, 3 #khai báo nhiều biến cùng lúc
# print(x, y, z)

# x = y = z = 1 #gán nhiều biến cùng giá trị
# # print(x, y, z)

# s4.Hằng số
# import math
# print(math.pi) #hằng số pi
# # PI = 3.14 #khai báo hằng số

# s5.Kiểu dữ liệu
# a = 5 #int
# b = 5.5 #float
# c = "Hello" #str
# d = True #bool    
# e = None #kiểu dữ liệu rỗng
# f = 1 + 2j #kiểu dữ liệu phức

# print(type(a)) #kiểm tra kiểu dữ liệu
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

# s6.Ép kiểu dữ liệu

# int() - chuyển đổi sang kiểu số nguyên
# float() - chuyển đổi sang kiểu số thực
# str() - chuyển đổi sang kiểu chuỗi
# bool() - chuyển đổi sang kiểu boolean

# n = 100
# m = "200"
# print(n+int(m)) #ép kiểu m từ str sang int để cộng với n , nếu ko báo lỗi

# s7.Các phép toán số học 
# +, -, *, /, //, %, **

# print(a/b) #chia lấy kết quả thực
# print(a//b) #chia lấy kết quả nguyên  
# print(a%b) #chia lấy phần dư
# print(a**b) #lũy thừa
# a = int(input("Nhập vào a: "))
# b = int(input("Nhập vào b: "))
# print("{0} + {1} = {2}" .format(a ,b , a+b))    
# print("{0} - {1} = {2}" .format(a ,b , a-b))    
# print("{0} * {1} = {2}" .format(a ,b , a*b))    
# print("{0} / {1} = {2}" .format(a ,b , a/b))    
# print("{0} // {1} = {2}" .format(a ,b , a//b))    
# print("{0} % {1} = {2}" .format(a ,b , a%b))    
# print("{0} ** {1} = {2}" .format(a ,b , a**b))    

# s8.Toán tử so sánh
# ==, !=, >, <, >=, <= 

# print(a != b) #so sánh a có khác b 
# x = int(input("Nhập vào x: "))
# y = int(input("Nhập vào y: "))
# # Trả về True hoặc False
# print(x != y)
# print(x == y)
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)

# s9.Toán tử logic
# and, or, not

# x = int(input("Nhập vào x: "))
# y = int(input("Nhập vào y: "))
# print ( x > 0 and y > 5) 
# print ( x > 0 or y > 5)
# print ( not ( x > y ))

# s10. Toán tử gán
# =, +=, -=, *=, /=, //=, %=, **=

# a = 5
# a += 2 # a = a + 2
# print(int(a))
# a -= 2 # a = a - 2
# print(int(a))
# a *= 2 # a = a * 2
# print(int(a))
# a /= 2 # a = a / 2
# print(int(a))
# a //= 2 # a = a // 2
# print(int(a))
# a %= 2 # a = a % 2
# print(int(a))
# a **= 2 # a = a ** 2
# print(int(a))

# s11.Thư viện math  
import math 
# print(math.pi) #hằng số pi
# print(math.e) #hằng số e
# print(math.sqrt(a)) #căn bậc 2
# print(math.fabs(-5)) #giá trị tuyệt đối
# print(math.pow(a, b)) #lũy thừa
# print(math.factorial(a)) #giai thừa
# print(math.ceil(5.1)) #làm tròn lên
# print(math.floor(5.9)) #làm tròn xuống
# print(math.sin(a)) #hàm sin
# print(math.cos(a)) #hàm cos
# print(math.tan(a)) #hàm tan
# print(math.log(a)) #hàm log
# print(math.log10(a)) #hàm log cơ số 10
# print(math.radians(a)) #đổi độ sang radian
# print(math.degrees(a)) #đổi radian sang độ
# print(math.gcd(12, 15)) #ước chung lớn nhất
# print(math.lcm(12, 15)) #bội chung nhỏ nhất
# print(math.isqrt(10)) #căn bậc 2 của số nguyên

# x = float(input("x: "))
# print("sqrt(x) = ", math.sqrt(x))
# print("fabs(x) = ", math.fabs(x))
# print("sin(x) = " , math.sin(x))
# print("pow(x , 2) = ", math.pow(x, 2))
# print("ceil(x) = ", math.ceil(x))

# s12.Toán tử ba ngôi
# điều kiện đúng if điều kiện else điều kiện sai
# a = int(input("Nhập vào a: "))
# kq = " số chẵn " if ( a % 2 == 0) else " số lẻ "
# print ( a , "là " , kq) 

# s13.Câu lệnh rẽ nhánh if...else
# x = float(input("Nhập vào x: "))
# vd1
# if x % 2 == 0 :
#     print (x," là số chẵn")
# else : 
#     print (x," là số lẻ")

# print("Kết thúc chương trình")

# vd2
# if x >= 9 :
#     print("Học sinh giỏi")
# elif x >= 7 :
#     print("Học sinh khá")
# elif x >= 5 :
#     print("Học sinh trung bình")
# else :
#     print("Học sinh yếu")
# print("Kết thúc chương trình")

# s14.Giải phương trình bậc 2
# print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
# a = float(input("Nhập vào a: "))
# b = float(input("Nhập vào b: "))
# c = float(input("Nhập vào c: "))
# if (a != 0): 
#     delta = b**2 - 4*a*c
#     if (delta < 0 ):
#         print("Phương trình vô nghiệm")
#     elif (delta == 0) :
#         x = -b/(2*a)
#         print("Phương trình có nghiệm kép x1 = x2 = ", x) 
#     else :
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b - math.sqrt(delta)) / (2*a)
#         print("Phương trình có 2 nghiệm phân biệt: x1 = ", x1, " x2 = ", x2)
# else :
#     print("Không phải phương trình bậc 2")

# s15.Kiểu dữ liệu List 
colors = ["red", "green" , "orange"]

# s15.1.Phương thức thao tác trên List
# append(): Thêm một phần tử vào cuối List.
# extend(): Thêm nhiều phần tử từ một List khác vào cuối List hiện tại.
# insert(): Thêm một phần tử vào vị trí cụ thể trong List.
# remove(): Xóa phần tử đầu tiên khớp với giá trị được chỉ định.
# pop(): Xóa và trả về phần tử tại một vị trí xác định (hoặc phần tử cuối).
# clear(): Xóa toàn bộ phần tử trong List.
# index(): Trả về chỉ số của phần tử đầu tiên khớp với giá trị được chỉ định.
# count(): Đếm số lần một phần tử xuất hiện trong List.
# reverse(): Đảo ngược thứ tự các phần tử trong List.
# copy(): Trả về một bản sao của List.
# sort(): Sắp xếp các phần tử trong List tại chỗ.

# s15.2.Hàm thao tác với list trong Python
# len(): Trả về số lượng phần tử trong List.
# min(): Trả về phần tử nhỏ nhất trong List.
# max(): Trả về phần tử lớn nhất trong List.
# sum(): Tính tổng các phần tử trong List (dành cho List chứa các số).
# sorted(): Trả về một List mới đã được sắp xếp mà không thay đổi List ban đầu.

# s15.3.Các hàm toán học và logic với List
# any(): Trả về True nếu có bất kỳ phần tử nào trong List là True.
# all(): Trả về True nếu tất cả các phần tử trong List đều là True.

#Truy xuất dữ liệu index , (star:end) 
print(colors[2])
print(colors[0:2])
#Thêm phân tử vào vị trí cuối append
colors.append("blue")
print(colors)
#Thêm phần tử vào vị trí được chỉ định insert(index,x)
colors.insert(1 , "white")
print(colors)











