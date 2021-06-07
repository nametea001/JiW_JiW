from tkinter import *

root = Tk()
root.title("โปรแกรมสั่งอาหาร โง่ๆ V.1 ")

#กำหนดขนาด หน้าโปรแกรม
root.geometry("300x400+600+150") 
root.minsize(width=200,height=300)

def finish_pay():
    #หน้าจอ 2 
    finish = Tk() 
    finish.title("คิดเงิน")
    finish.geometry("300x500+600+150") 
    finish.minsize(width=200,height=300)
    main_lable = Label(finish,text="รายการ",font=50, pady=5).pack()
    
    txt_num1 = txt1.get()
    if txt_num1 != "":
        nongkai = Label(finish,text="น่องไก่ทอด x" + txt_num1 , font=40, pady=5).pack()
    else:
        nongkai = Label(finish,text="น่องไก่ x0" + txt_num1 , font=40, pady=5).pack()
    
    txt_num2 = txt2.get()
    if txt_num2 != "":
        peekkai = Label(finish,text="ปีกไก่ทอด  x" + txt_num2 , font=40, pady=5).pack()
    else:
        peekkai = Label(finish,text="ปีกไก่ทอด  x0", font=40, pady=5).pack()

    txt_num3 = txt3.get()
    if txt_num3 != "":
        numrome = Label(finish,text="น้ำอัดลม   x" + txt_num3 , font=40, pady=5).pack()
    else:
        numrome = Label(finish,text="น้ำอัดลม   x0", font=40, pady=5).pack()

    txt_num4 = txt4.get()
    if txt_num4 != "":
        frenfry = Label(finish,text="เฟรนเฟราย x" + txt_num4 , font=40, pady=5).pack()
    else:
        frenfry = Label(finish,text="เฟรนเฟราย x0", font=40, pady=5).pack()
  
    if txt_num1 !=  "":
        test1 = int(txt_num1)
    else:
        test1 = 0
    if txt_num2 != "":
        test2 = int(txt_num2)
    else:
        test2 = 0
    if txt_num3 != "":
        test3 = int(txt_num3)
    else:
        test3 = 0
    if txt_num4 != "":
        test4 = int(txt_num4)
    else:
        test4 = 0
        
    delivaly = Label(finish,text="ค่าส่ง  10 บาท ", font=40).pack()

    total_price = (test1*15)+(test2*10)+(test3*10)+(test4*10)+10
    
    total = Label(finish,text="ราคารวม  " + str(total_price) + " บาท", font=40).pack()

    pay_system = Label(finish,text="กรุณาเลือกระบบชำระเงิน ", font=5, pady=7).pack()

    def QR_Code():
        pay_finish.configure(text="ยังไม่มี QR Code", font=40)
    bt4 = Button(finish, text="QR Code", width=100, fg="white", bg="green",command=QR_Code).pack()
    
    def bank():
        pay_finish.configure(text="กรุงโรม\n3xx-xx6xxx-1\nนาย โรมัน", font=40)

    bt5 = Button(finish, text="เลขบัญชี", width=100, fg="white", bg="green",command=bank).pack()

    def tarng():
        pay_finish.configure(text="รอรับโทรศัพจากพนักงานครับ", font=40)
    bt6 = Button(finish, text="เก็บเงินปลายทาง", command=tarng, width=100, fg="white", bg="green").pack()
    
    def addess_number():
        adnum = Tk()
        adnum.title("ที่อยู่และเบอร์โทร")
        adnum.geometry("300x500+600+150") 
        adnum.minsize(width=200,height=300)

        adnum_lable1 = Label(adnum,text="ที่อยู่ หรือ หอพัก", font=40, pady=20).pack()
        adnum1 = StringVar()
        adnumtext1 = Entry(adnum,textvariable=txt1,width=25).pack()

        adnum_lable2 = Label(adnum,text="เบอร์โทรติดต่อ", font=40, pady=20).pack()
        adnum2 = StringVar()
        adnumtext2 = Entry(adnum,textvariable=txt1,width=25).pack()

        bt8 = Button(adnum, text="บันทึก").pack()

    bt7 = Button(finish, text="ที่อยู่และเบอร์ติดต่อ",command=addess_number).place(x=100,y=400)
    bt9 = Button(finish, text="ส่งสลิปโอนเงิน").place(x=110,y=427)

    pay_finish = Label(finish,text="", font=5)
    pay_finish.pack()

def error_pay():
    error_ = Tk() 
    error_.title("error")
    error_.geometry("300x400+600+150") 
    error_.minsize(width=200,height=300)
    main_lable = Label(error_,text="เกิดข้อผิดพลาดกรุณาเลือกสั่งอาหารใหม่", font=40, pady=20).pack()
    
#ข้อความ head
main_lable = Label(root,text="รายการสั่งอาหาร", font=40, pady=20).pack()

def test_txt():
    txt_num1 = txt1.get()
    if txt_num1 != "":
        nongkai.configure(text="น่องไก่ทอด " + txt_num1 + " ชิ้น")
    else:
        nongkai.configure(text="น่องไก่ทอด 0 ชิ้น")
    
    txt_num2 = txt2.get()
    if txt_num2 != "":
        peekkai.configure(text="ปีกไก่ทอด " + txt_num2 + " ชิ้น")
    else:
        peekkai.configure(text="ปีกไก่ทอด 0 ชิ้น")

    txt_num3 = txt3.get()
    if txt_num3 != "":
        numrome.configure(text="น้ำอัดลม " + txt_num3 + " แก้ว")
    else:
        numrome.configure(text="น้ำอัดลม 0 แก้ว")

    txt_num4 = txt4.get()
    if txt_num4 != "":
        frenfry.configure(text="เฟรนฟราย " + txt_num4 + " ชุด")
    else:
        frenfry.configure(text="เฟรนฟราย 0 ชุด")

    if(txt_num1 and txt_num2 and txt_num3 and txt_num4 =="0"):
        bt3 = Button(root, text="สั่งซื้อ", command=error_pay, width=20, fg="white", bg="blue").pack()
    elif (txt_num1 or txt_num2 or txt_num3 or txt_num4) != "":
        bt2 = Button(root, text="สั่งซื้อ", command=finish_pay, width=20, fg="white", bg="red").pack()
    else:
        bt3 = Button(root, text="สั่งซื้อ", command=error_pay, width=20, fg="white", bg="blue").pack()

nongkai = Label(root,text="น่องไก่ทอด 0 ชิ้น ชิ้นละ 15 บาท",font=30)
nongkai.pack()

#กล่องให้กรอก
txt1 = StringVar()
myText1 = Entry(root,textvariable=txt1,width=5).pack()

nongkai2 = Label(root,text="*ชิ้นละ 15 บาท", fg="red").pack()

peekkai = Label(root,text="ปีกไก่ทอด 0 ชิ้น",font=30)
peekkai.pack()

txt2 = StringVar()
myText2 = Entry(root,textvariable=txt2,width=5).pack()

peekkai2= Label(root,text="*ชิ้นละ 10 บาท", fg="red").pack()

numrome = Label(root,text="น้ำอัดลม 0 แก้ว",font=30)
numrome.pack()

txt3 = StringVar()
myText3 = Entry(root,textvariable=txt3,width=5).pack()

numrome2 = Label(root,text="แก้วละ 10 บาท", fg="red").pack()

frenfry = Label(root,text="เฟรนฟราย 0 ชุด",font=30)
frenfry.pack()

txt4 = StringVar()
myText4 = Entry(root,textvariable=txt4,width=5).pack()

frenfry2 = Label(root,text="*ชุดละ 10 บาท", fg="red").pack()

#ปุ่มกด
bt1 = Button(root, text="ยีนยัน", command=test_txt, width=20, fg="green", bg="white").pack()

root.mainloop()

#asdsdasdadasdasdasdasd