from db import*

# Each time a account created, add its "username" to this list in order to easily check existed account
un_list = ["TienAnh98", "TamVu", "PhongTienNguyen",]

def check_acc(username):
        if username in un_list:  # a Đức ơiii, a có xem đến đoạn này thì giải thích hộ e sao mà e cho vòng for vào đây rồi if else vs đk là i == username thì nó auto False :((
            return True
        else:
            return False

