
from operator import imod
from turtle import st
import data as d

def addStudent():
    print("***THÊM SINH VIÊN***")

    infor = {
        'id': '',
        'name': ''  
    }

    print("Nhập ID sinh viên:")
    id = input()
    while True:
        student = findStudent(id)
        if student != False:
            print("ID này đã tồn tại, vui lòng nhập lại: ")
            id = input()
        else:
            break
    infor['id'] = id

    print("Nhập tên sinh viên: ")
    infor['name'] = input()

    d.listStudents.append(infor)

def findStudent(id):
    for i in range(len(d.listStudents)):
        if d.listStudents[i]['id'] == id:
            return [i,d.listStudents[i]]
    return False

def deleteStudent():
    print("***XÓA SINH VIÊN***")
    print("Nhập ID sinh viên cần xóa: ")

    id = input()

    student = findStudent(id)

    if student != False:
        d.listStudents.remove(student[1])
        print("Xóa sinh viên thành công!")
    else:
        print("Không tìm thấy sinh viên cần xóa!")

def showStudents():
    print("***DANH SÁCH SINH VIÊN HIỆN TẠI***")
    for i in range(len(d.listStudents)):
        print("[",d.listStudents[i]['id'],"]", "[",d.listStudents[i]['name'],"]")

def editStudent():
    print("***SỬA THÔNG TIN SINH VIÊN***")
    print("Nhập ID sinh viên cần sửa: ")
    id = input()

    student = findStudent(id)
    if student != False:
        print("Nhập tên sinh viên:")
        name = input()
        student[1]['name'] = name
        d.listStudents[student[0]] = student[1]
    else:
        print("Không tìm thấy sinh viên !")
