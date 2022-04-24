from tkinter import*

window = Tk()

add_option_stat = 10

def calculate() :
    global add_option_stat
    main_stat = int(txt_main_stat.get())
    gongma_stat = int(txt_gongma_stat.get())
    all_stat = int(txt_all_stat.get())

    add_option_stat = "[{}]".format(main_stat + (gongma_stat * 4) + (all_stat * 10)) 
    btn_confirm.config(text = add_option_stat)

window.title("추가옵션 계산기")
window.geometry("300x200+100+100")
window.resizable(False, False)

lbl_main_stat = Label(window, text="주스탯")
lbl_main_stat.place(x=30, y=30)

txt_main_stat = Entry(window, takefocus=1)
txt_main_stat.place(x=80, y=30)

lbl_gongma_stat = Label(window, text="공/마")
lbl_gongma_stat.place(x=30, y=55)

txt_gongma_stat = Entry(window, takefocus=1)
txt_gongma_stat.place(x=80, y=55)

lbl_all_stat = Label(window, text="올스탯")
lbl_all_stat.place(x=30, y=80)

txt_all_stat = Entry(window, takefocus=1)
txt_all_stat.place(x=80, y=80)

btn_confirm = Button(window, width=15, height=3 ,text="계산", command=calculate, bd=2)
btn_confirm.place(x=95, y=120)

window.mainloop()