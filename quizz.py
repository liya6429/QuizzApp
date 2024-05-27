from tkinter import*
from PIL import ImageTk,Image
root=Tk()
right=0
wrong=0
def play1():
    def play2():
        if(variable.get()=="Harry Potter"):
            def h2():
                def h3():
                    def h4():
                        def h5():
                            def h6():
                                def h7():
                                    def h8():
                                        def h9():
                                            def h10():
                                                def result():
                                                    global right
                                                    global wrong
                                                    down10.destroy()
                                                    res=Tk()
                                                    res.title("RESULT")
                                                    res.iconbitmap("quiz.ico")
                                                    res.geometry("350x350")
                                                    res.resizable(False,False)
                                                    res.configure(background="dark slate gray")
                                                    title=Label(res, text="Results", bg="dark slate gray", fg="white", font=("verdana", 15, "bold"))
                                                    title.place(x=120,y=10)
                                                    total=Label(res,text="Total Score : " + str(right) + "/10", bg="dark slate gray", fg="white",font=("verdana", 13))
                                                    total.place(x=30,y=50)
                                                    correct= Label(res,text="Right answers: " + str(right), bg="dark slate gray", fg="white",font=("verdana", 13))
                                                    correct.place(x=50,y=90)
                                                    wrongg=Label(res, text="Wrong answers: " + str(wrong), bg="dark slate gray", fg="white",font=("verdana", 13))
                                                    wrongg.place(x=50,y=130)
                                                    sucess=Label(res,text="Quizz Completed Sucessfully",bg="dark slate gray",fg="white",font=("verdana", 14))
                                                    sucess.place(x=30,y=180)
                                                    #button
                                                    bye=Button(res,text="EXIT",bg="red",fg="white",font=("verdana", 13,"bold"),command=quit)
                                                    bye.place(x=190,y=230)
                                                    res.mainloop()
                                                down9.destroy()
                                                down10=Tk()
                                                down10.iconbitmap("quiz.ico")
                                                down10.geometry("700x500")
                                                down10.resizable(False,False)
                                                down10.configure(background="burlywood4")
                                                down10.title("QUIZZ")
                                                #label
                                                qh10=Label(down10,text="Question 10: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                                qh10.place(x=20,y=20)
                                                #photoadd
                                                imgh10=ImageTk.PhotoImage(Image.open("tom riddle.jpg"))
                                                labelh10=Label(down10,image=imgh10,bd=0)
                                                labelh10.place(x=20,y=70)
                                                #radiobutton
                                                option=StringVar()
                                                rh101=Radiobutton(down10,variable=option,text="tom riddle",value="tom riddle",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                                rh101.place(x=300,y=90)
                                                rh102=Radiobutton(down10,variable=option,text="ron weasley",value="ron weasley",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                                rh102.place(x=300,y=120)
                                                rh103=Radiobutton(down10,variable=option,text="sirus black",value="sirus black",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                                rh103.place(x=300,y=150)
                                                #button
                                                btnh10=Button(down10,text="FINISH",bg="orange",fg="white",command=result,font=("verdana",12))
                                                btnh10.place(x=300,y=200)
                                                down10.mainloop()
                                            down8.destroy()
                                            down9=Tk()
                                            down9.iconbitmap("quiz.ico")
                                            down9.geometry("700x500")
                                            down9.resizable(False,False)
                                            down9.configure(background="burlywood4")
                                            down9.title("QUIZZ")
                                            #label
                                            qh9=Label(down9,text="Question 9: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                            qh9.place(x=20,y=20)
                                            #photoadd
                                            imgh9=ImageTk.PhotoImage(Image.open("sirus.jpg"))
                                            labelh9=Label(down9,image=imgh9,bd=0)
                                            labelh9.place(x=20,y=70)
                                            #radiobutton
                                            option=StringVar()
                                            rh91=Radiobutton(down9,variable=option,text="sirus black",value="sirus black",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                            rh91.place(x=370,y=90)
                                            rh92=Radiobutton(down9,variable=option,text="ron weasley",value="ron weasley",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                            rh92.place(x=370,y=120)
                                            rh93=Radiobutton(down9,variable=option,text="hagrid",value="hagrid",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                            rh93.place(x=370,y=150)
                                            #button
                                            btnh9=Button(down9,text="Next",bg="orange",fg="white",command=h10,font=("verdana",12))
                                            btnh9.place(x=370,y=200)
                                            down9.mainloop()
                                        down7.destroy()
                                        down8=Tk()
                                        down8.iconbitmap("quiz.ico")
                                        down8.geometry("700x500")
                                        down8.resizable(False,False)
                                        down8.configure(background="burlywood4")
                                        down8.title("QUIZZ")
                                        #label
                                        qh8=Label(down8,text="Question 8: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                        qh8.place(x=20,y=20)
                                        #photoadd
                                        imgh8=ImageTk.PhotoImage(Image.open("hagrid.jpg"))
                                        labelh8=Label(down8,image=imgh8,bd=0)
                                        labelh8.place(x=20,y=70)
                                        #radiobutton
                                        option=StringVar()
                                        rh81=Radiobutton(down8,variable=option,text="sirius black",value="sirius black",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                        rh81.place(x=300,y=90)
                                        rh82=Radiobutton(down8,variable=option,text="voldemort",value="voldemort",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                        rh82.place(x=300,y=120)
                                        rh83=Radiobutton(down8,variable=option,text="hagrid",value="hagrid",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                        rh83.place(x=300,y=150)
                                        #button
                                        btnh8=Button(down8,text="Next",bg="orange",fg="white",command=h9,font=("verdana",12))
                                        btnh8.place(x=300,y=200)
                                        down8.mainloop()
                                    down6.destroy()
                                    down7=Tk()
                                    down7.iconbitmap("quiz.ico")
                                    down7.geometry("700x500")
                                    down7.resizable(False,False)
                                    down7.configure(background="burlywood4")
                                    down7.title("QUIZZ")
                                    #label
                                    qh7=Label(down7,text="Question 7: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                    qh7.place(x=20,y=20)
                                    #photoadd
                                    imgh7=ImageTk.PhotoImage(Image.open("voldermort.jpg"))
                                    labelh7=Label(down7,image=imgh7,bd=0)
                                    labelh7.place(x=20,y=70)
                                    #radiobutton
                                    option=StringVar()
                                    rh71=Radiobutton(down7,variable=option,text="voldemort",value="voldemort",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                    rh71.place(x=300,y=90)
                                    rh72=Radiobutton(down7,variable=option,text="ron weasley",value="ron weasley",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                    rh72.place(x=300,y=120)
                                    rh73=Radiobutton(down7,variable=option,text="hagrid",value="hagrid",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                    rh73.place(x=300,y=150)
                                    #button
                                    btnh7=Button(down7,text="Next",bg="orange",fg="white",command=h8,font=("verdana",12))
                                    btnh7.place(x=300,y=200) 
                                    down7.mainloop()
                                down5.destroy()
                                down6=Tk()
                                down6.iconbitmap("quiz.ico")
                                down6.geometry("700x500")
                                down6.resizable(False,False)
                                down6.configure(background="burlywood4")
                                down6.title("QUIZZ")
                                #label
                                qh6=Label(down6,text="Question 6: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                qh6.place(x=20,y=20)
                                #photoadd
                                imgh6=ImageTk.PhotoImage(Image.open("serverus.jpg"))
                                labelh6=Label(down6,image=imgh6,bd=0)
                                labelh6.place(x=20,y=70)
                                #radiobutton
                                option=StringVar()
                                rh61=Radiobutton(down6,variable=option,text="hermonie granger",value="hermonie granger",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                rh61.place(x=300,y=90)
                                rh62=Radiobutton(down6,variable=option,text="sirius black",value="sirius black",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                rh62.place(x=300,y=120)
                                rh63=Radiobutton(down6,variable=option,text="serverus snape",value="serverus snape",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                rh63.place(x=300,y=150)
                                #button
                                btnh6=Button(down6,text="Next",bg="orange",fg="white",command=h7,font=("verdana",12))
                                btnh6.place(x=300,y=200)
                                down6.mainloop()
                            down4.destroy()
                            down5=Tk()
                            down5.iconbitmap("quiz.ico")
                            down5.geometry("700x500")
                            down5.resizable(False,False)
                            down5.configure(background="burlywood4")
                            down5.title("QUIZZ")
                            #label
                            qh5=Label(down5,text="Question 5: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                            qh5.place(x=20,y=20)
                            #photoadd
                            imgh5=ImageTk.PhotoImage(Image.open("albus.jpg"))
                            labelh5=Label(down5,image=imgh5,bd=0)
                            labelh5.place(x=20,y=70)
                            #radiobutton
                            option=StringVar()
                            rh51=Radiobutton(down5,variable=option,text="albus dumbledore",value="albus dumbledore",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                            rh51.place(x=300,y=90)
                            rh52=Radiobutton(down5,variable=option,text="ron weasley",value="ron weasley",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                            rh52.place(x=300,y=120)
                            rh53=Radiobutton(down5,variable=option,text="hagrid",value="hagrid",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                            rh53.place(x=300,y=150)
                            #button
                            btnh5=Button(down5,text="Next",bg="orange",fg="white",command=h6,font=("verdana",12))
                            btnh5.place(x=300,y=200)
                            down5.mainloop()   
                        down2.destroy()
                        down4=Tk()
                        down4.iconbitmap("quiz.ico")
                        down4.geometry("700x500")
                        down4.resizable(False,False)
                        down4.configure(background="burlywood4")
                        down4.title("QUIZZ")
                        #label
                        qh4=Label(down4,text="Question 4: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                        qh4.place(x=20,y=20)
                        #photoadd
                        imgh4=ImageTk.PhotoImage(Image.open("draco.jpg"))
                        labelh4=Label(down4,image=imgh4,bd=0)
                        labelh4.place(x=20,y=70)
                        #radiobutton
                        option=StringVar()
                        rh41=Radiobutton(down4,variable=option,text="hermonie granger",value="hermonie granger",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                        rh41.place(x=300,y=90)
                        rh42=Radiobutton(down4,variable=option,text="draco malfoy",value="draco malfoy",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                        rh42.place(x=300,y=120)
                        rh43=Radiobutton(down4,variable=option,text="hagrid",value="hagrid",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                        rh43.place(x=300,y=150)
                        #button
                        btnh4=Button(down4,text="Next",bg="orange",fg="white",command=h5,font=("verdana",12))
                        btnh4.place(x=300,y=200)
                        down4.mainloop()
                    down1.destroy()
                    down2=Tk()
                    down2.iconbitmap("quiz.ico")
                    down2.geometry("700x500")
                    down2.resizable(False,False)
                    down2.configure(background="burlywood4")
                    down2.title("QUIZZ")
                    #label
                    qh3=Label(down2,text="Question 3: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                    qh3.place(x=20,y=20)
                    #photoadd
                    imgh3=ImageTk.PhotoImage(Image.open("Hermione.jpg"))
                    labelh3=Label(down2,image=imgh3,bd=0)
                    labelh3.place(x=20,y=70)
                    #radiobutton
                    option=StringVar()
                    rha11=Radiobutton(down2,variable=option,text="hermonie granger",value="hermonie granger",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                    rha11.place(x=300,y=90)
                    rha22=Radiobutton(down2,variable=option,text="ron weasley",value="ron weasley",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                    rha22.place(x=300,y=120)
                    rha33=Radiobutton(down2,variable=option,text="hagrid",value="hagrid",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                    rha33.place(x=300,y=150)
                    #button
                    btnh3=Button(down2,text="Next",bg="orange",fg="white",command=h4,font=("verdana",12))
                    btnh3.place(x=300,y=200)
                    down2.mainloop()
                down.destroy()
                down1=Tk()
                down1.iconbitmap("quiz.ico")
                down1.geometry("700x500")
                down1.resizable(False,False)
                down1.configure(background="burlywood4")
                down1.title("QUIZZ")
                #label
                qh2=Label(down1,text="Question 2: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                qh2.place(x=20,y=20)
                #photoadd
                imgh2=ImageTk.PhotoImage(Image.open("ron .jpg"))
                labelh2=Label(down1,image=imgh2,bd=0)
                labelh2.place(x=20,y=70)
                #radiobutton
                option=StringVar()
                rh11=Radiobutton(down1,variable=option,text="harry potter",value="harry potter",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                rh11.place(x=300,y=90)
                rh22=Radiobutton(down1,variable=option,text="ron weasley",value="ron weasley",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                rh22.place(x=300,y=120)
                rh33=Radiobutton(down1,variable=option,text="tom riddle",value="tom riddle",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                rh33.place(x=300,y=150)
                #button
                btnh2=Button(down1,text="Next",bg="orange",fg="white",command=h3,font=("verdana",12))
                btnh2.place(x=300,y=200)
                down1.mainloop()
            right=0
            wrong=0    
            def yes():
                global right
                right+=1
            def no():
                global wrong
                wrong+=1    
            top.destroy()
            down=Tk()
            down.iconbitmap("quiz.ico")
            down.geometry("700x500")
            down.resizable(False,False)
            down.configure(background="burlywood4")
            down.title("QUIZZ")
            #label
            qh1=Label(down,text="Question 1: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
            qh1.place(x=20,y=20)
            #photoadd
            imgh1=ImageTk.PhotoImage(Image.open("hary.jpg"))
            labelh1=Label(down,image=imgh1,bd=0)
            labelh1.place(x=20,y=70)
            #radiobutton
            option = StringVar()
            rh1=Radiobutton(down,variable=option,text="harry potter",value="harry potter",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
            rh1.place(x=300,y=90)
            rh2=Radiobutton(down,variable=option,text="draco malfoy",value="draco malfoy",command=no,font=("verdana",13),bg="burlywood4",fg="black")
            rh2.place(x=300,y=120)
            rh3=Radiobutton(down,variable=option,text="tom riddle",value=3,command="tom riddle",font=("verdana",13),bg="burlywood4",fg="black")
            rh3.place(x=300,y=150)
            #button
            btnh1=Button(down,text="Next",bg="orange",fg="white",command=h2,font=("Arial",12))
            btnh1.place(x=300,y=200)
            down.mainloop()
        elif(variable.get()=="Avengers"):
            right=0
            wrong=0    
            def yes():
                global right
                right+=1
            def no():
                global wrong
                wrong+=1
            def a2():
                def a3():
                    def a4():
                        def a5():
                            def a6():
                                def a7():
                                    def a8():
                                        def a9():
                                            def a10():
                                                def result():
                                                    global right
                                                    global wrong
                                                    downa10.destroy()
                                                    res=Tk()
                                                    res.title("RESULT")
                                                    res.iconbitmap("quiz.ico")
                                                    res.geometry("350x350")
                                                    res.resizable(False,False)
                                                    res.configure(background="dark slate gray")
                                                    title=Label(res, text="Results", bg="dark slate gray", fg="white", font=("verdana", 15, "bold"))
                                                    title.place(x=120,y=10)
                                                    total=Label(res,text="Total Score : " + str(right) + "/10", bg="dark slate gray", fg="white",font=("verdana", 13))
                                                    total.place(x=30,y=50)
                                                    correct= Label(res,text="Right answers: " + str(right), bg="dark slate gray", fg="white",font=("verdana", 13))
                                                    correct.place(x=50,y=90)
                                                    wrongg=Label(res, text="Wrong answers: " + str(wrong), bg="dark slate gray", fg="white",font=("verdana", 13))
                                                    wrongg.place(x=50,y=130)
                                                    sucess=Label(res,text="Quizz Completed Sucessfully",bg="dark slate gray",fg="white",font=("verdana", 14))
                                                    sucess.place(x=30,y=180)
                                                    #button
                                                    bye=Button(res,text="EXIT",bg="red",fg="white",font=("verdana", 13,"bold"),command=quit)
                                                    bye.place(x=190,y=230)
                                                    res.mainloop()
                                                downa9.destroy()
                                                downa10=Tk()
                                                downa10.iconbitmap("quiz.ico")
                                                downa10.geometry("700x500")
                                                downa10.resizable(False,False)
                                                downa10.configure(background="burlywood4")
                                                downa10.title("QUIZZ")
                                                #label
                                                qa10=Label(downa10,text="Question 10: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                                qa10.place(x=20,y=20)
                                                #photoadd
                                                imga10=ImageTk.PhotoImage(Image.open("hawkeye.jpg"))
                                                labela10=Label(downa10,image=imga10,bd=0)
                                                labela10.place(x=20,y=70)
                                                #radiobutton
                                                option=StringVar()
                                                ra101=Radiobutton(downa10,variable=option,text="captain america",value="captain america",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                                ra101.place(x=300,y=90)
                                                ra102=Radiobutton(downa10,variable=option,text="hulk",value="hulk",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                                ra102.place(x=300,y=120)
                                                ra103=Radiobutton(downa10,variable=option,text="hawkeye",value="hawkeye",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                                ra103.place(x=300,y=150)
                                                #button
                                                btna10=Button(downa10,text="Next",bg="orange",fg="white",command=result,font=("verdana",12))
                                                btna10.place(x=300,y=200)
                                                downa10.mainloop()
                                            downa8.destroy()
                                            downa9=Tk()
                                            downa9.iconbitmap("quiz.ico")
                                            downa9.geometry("700x500")
                                            downa9.resizable(False,False)
                                            downa9.configure(background="burlywood4")
                                            downa9.title("QUIZZ")
                                            #label
                                            qa9=Label(downa9,text="Question 9: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                            qa9.place(x=20,y=20)
                                            #photoadd
                                            imga9=ImageTk.PhotoImage(Image.open("black pan.jpg"))
                                            labela9=Label(downa9,image=imga9,bd=0)
                                            labela9.place(x=20,y=70)
                                            #radiobutton
                                            option=StringVar()
                                            ra91=Radiobutton(downa9,variable=option,text="hawkeye",value="hawkeye",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                            ra91.place(x=300,y=90)
                                            ra92=Radiobutton(downa9,variable=option,text="black widow",value="black widow",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                            ra92.place(x=300,y=120)
                                            ra93=Radiobutton(downa9,variable=option,text="black panther",value="black panther",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                            ra93.place(x=300,y=150)
                                            #button
                                            btna9=Button(downa9,text="Next",bg="orange",fg="white",command=a10,font=("verdana",12))
                                            btna9.place(x=300,y=200)
                                            downa9.mainloop()  
                                        downa7.destroy()
                                        downa8=Tk()
                                        downa8.iconbitmap("quiz.ico")
                                        downa8.geometry("700x500")
                                        downa8.resizable(False,False)
                                        downa8.configure(background="burlywood4")
                                        downa8.title("QUIZZ")
                                        #label
                                        qa8=Label(downa8,text="Question 8: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                        qa8.place(x=20,y=20)
                                        #photoadd
                                        imga8=ImageTk.PhotoImage(Image.open("scarlet.jpg"))
                                        labela8=Label(downa8,image=imga8,bd=0)
                                        labela8.place(x=20,y=70)
                                        #radiobutton
                                        option=StringVar()
                                        ra81=Radiobutton(downa8,variable=option,text="scarlet witch",value="scarlet witch",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                        ra81.place(x=300,y=90)
                                        ra82=Radiobutton(downa8,variable=option,text="hawkeye",value="hawkeye",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                        ra82.place(x=300,y=120)
                                        ra83=Radiobutton(downa8,variable=option,text="black widow",value="black widow",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                        ra83.place(x=300,y=150)
                                        #button
                                        btna8=Button(downa8,text="Next",bg="orange",fg="white",command=a9,font=("verdana",12))
                                        btna8.place(x=300,y=200)
                                        downa8.mainloop()
                                    downa6.destroy()
                                    downa7=Tk()
                                    downa7.iconbitmap("quiz.ico")
                                    downa7.geometry("700x500")
                                    downa7.resizable(False,False)
                                    downa7.configure(background="burlywood4")
                                    downa7.title("QUIZZ")
                                    #label
                                    qa7=Label(downa7,text="Question 7: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                    qa7.place(x=20,y=20)
                                    #photoadd
                                    imga7=ImageTk.PhotoImage(Image.open("black w.jpg"))
                                    labela7=Label(downa7,image=imga7,bd=0)
                                    labela7.place(x=20,y=70)
                                    #radiobutton
                                    option=StringVar()
                                    ra71=Radiobutton(downa7,variable=option,text="black widow",value="black widow",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                    ra71.place(x=300,y=90)
                                    ra72=Radiobutton(downa7,variable=option,text="black panther",value="black panther",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                    ra72.place(x=300,y=120)
                                    ra73=Radiobutton(downa7,variable=option,text="scarlet witch",value="scarlet witch",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                    ra73.place(x=300,y=150)
                                    #button
                                    btna7=Button(downa7,text="Next",bg="orange",fg="white",command=a8,font=("verdana",12))
                                    btna7.place(x=300,y=200)
                                    downa7.mainloop()
                                downa5.destroy()
                                downa6=Tk()
                                downa6.iconbitmap("quiz.ico")
                                downa6.geometry("700x500")
                                downa6.resizable(False,False)
                                downa6.configure(background="burlywood4")
                                downa6.title("QUIZZ")
                                #label
                                qa6=Label(downa6,text="Question 6: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                qa6.place(x=20,y=20)
                                #photoadd
                                imga6=ImageTk.PhotoImage(Image.open("hulk.jpg"))
                                labela6=Label(downa6,image=imga6,bd=0)
                                labela6.place(x=20,y=70)
                                #radiobutton
                                option=StringVar()
                                ra61=Radiobutton(downa6,variable=option,text="black panther",value="black panther",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                ra61.place(x=350,y=90)
                                ra62=Radiobutton(downa6,variable=option,text="hulk",value="hulk",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                ra62.place(x=350,y=120)
                                ra63=Radiobutton(downa6,variable=option,text="iron man",value="iron man",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                ra63.place(x=350,y=150)
                                #button
                                btna6=Button(downa6,text="Next",bg="orange",fg="white",command=a7,font=("verdana",12))
                                btna6.place(x=350,y=200) 
                                downa6.mainloop()
                            downa4.destroy()
                            downa5=Tk()
                            downa5.iconbitmap("quiz.ico")
                            downa5.geometry("700x500")
                            downa5.resizable(False,False)
                            downa5.configure(background="burlywood4")
                            downa5.title("QUIZZ")
                            #label
                            qa5=Label(downa5,text="Question 5: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                            qa5.place(x=20,y=20)
                            #photoadd
                            imga5=ImageTk.PhotoImage(Image.open("captain.jpg"))
                            labela5=Label(downa5,image=imga5,bd=0)
                            labela5.place(x=20,y=70)
                            #radiobutton
                            option=StringVar()
                            ra51=Radiobutton(downa5,variable=option,text="black widow",value="black widow",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                            ra51.place(x=300,y=90)
                            ra52=Radiobutton(downa5,variable=option,text="spider man",value="spider man",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                            ra52.place(x=300,y=120)
                            ra53=Radiobutton(downa5,variable=option,text="captain america",value="captain america",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                            ra53.place(x=300,y=150)
                            #button
                            btna5=Button(downa5,text="Next",bg="orange",fg="white",command=a6,font=("verdana",12))
                            btna5.place(x=300,y=200)
                            downa5.mainloop()
                        downa3.destroy()
                        downa4=Tk()
                        downa4.iconbitmap("quiz.ico")
                        downa4.geometry("700x500")
                        downa4.resizable(False,False)
                        downa4.configure(background="burlywood4")
                        downa4.title("QUIZZ")
                        #label
                        qa4=Label(downa4,text="Question 4: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                        qa4.place(x=20,y=20)
                        #photoadd
                        imga4=ImageTk.PhotoImage(Image.open("thor.jpg"))
                        labela4=Label(downa4,image=imga4,bd=0)
                        labela4.place(x=20,y=70)
                        #radiobutton
                        option=StringVar()
                        ra41=Radiobutton(downa4,variable=option,text="thor",value="thor",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                        ra41.place(x=300,y=90)
                        ra42=Radiobutton(downa4,variable=option,text="spider man",value="spider man",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                        ra42.place(x=300,y=120)
                        ra43=Radiobutton(downa4,variable=option,text="thanos",value="thanos",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                        ra43.place(x=300,y=150)
                        #button
                        btna4=Button(downa4,text="Next",bg="orange",fg="white",command=a5,font=("verdana",12))
                        btna4.place(x=300,y=200)
                        downa4.mainloop()
                    downa2.destroy()
                    downa3=Tk()
                    downa3.iconbitmap("quiz.ico")
                    downa3.geometry("700x500")
                    downa3.resizable(False,False)
                    downa3.configure(background="burlywood4")
                    downa3.title("QUIZZ")
                    #label
                    qa3=Label(downa3,text="Question 3: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                    qa3.place(x=20,y=20)
                    #photoadd
                    imga3=ImageTk.PhotoImage(Image.open("spider.jpg"))
                    labela3=Label(downa3,image=imga3,bd=0)
                    labela3.place(x=20,y=70)
                    #radiobutton
                    option=StringVar()
                    ra31=Radiobutton(downa3,variable=option,text="hawkeye",value="hawkeye",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                    ra31.place(x=300,y=90)
                    ra32=Radiobutton(downa3,variable=option,text="spider man",value="spider man",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                    ra32.place(x=300,y=120)
                    ra33=Radiobutton(downa3,variable=option,text="captain america",value="captain america",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                    ra33.place(x=300,y=150)
                    #button
                    btna3=Button(downa3,text="Next",bg="orange",fg="white",command=a4,font=("verdana",12))
                    btna3.place(x=300,y=200)
                    downa3.mainloop()
                downa1.destroy()
                downa2=Tk()
                downa2.iconbitmap("quiz.ico")
                downa2.geometry("700x500")
                downa2.resizable(False,False)
                downa2.configure(background="burlywood4")
                downa2.title("QUIZZ")
                #label
                qa2=Label(downa2,text="Question 2: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                qa2.place(x=20,y=20)
                #photoadd
                imga2=ImageTk.PhotoImage(Image.open("thanos.jpg"))
                labela2=Label(downa2,image=imga2,bd=0)
                labela2.place(x=20,y=70)
                #radiobutton
                option=StringVar()
                ra21=Radiobutton(downa2,variable=option,text="hawkeye",value="hawkeye",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                ra21.place(x=300,y=90)
                ra22=Radiobutton(downa2,variable=option,text="spider man",value="spider man",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                ra22.place(x=300,y=120)
                ra23=Radiobutton(downa2,variable=option,text="thanos",value="thanos",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                ra23.place(x=300,y=150)
                #button
                btna2=Button(downa2,text="Next",bg="orange",fg="white",command=a3,font=("verdana",12))
                btna2.place(x=300,y=200)
                downa2.mainloop() 
            top.destroy()
            downa1=Tk()
            downa1.iconbitmap("quiz.ico")
            downa1.geometry("700x500")
            downa1.resizable(False,False)
            downa1.configure(background="burlywood4")
            downa1.title("QUIZZ")
            #label
            qa1=Label(downa1,text="Question 1: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
            qa1.place(x=20,y=20)
            #photoadd
            imga1=ImageTk.PhotoImage(Image.open("iron.jpg"))
            labela1=Label(downa1,image=imga1,bd=0)
            labela1.place(x=20,y=70)
            #radiobutton
            option=StringVar()
            ra11=Radiobutton(downa1,variable=option,text="thanos",value="thanos",command=no,font=("verdana",13),bg="burlywood4",fg="black")
            ra11.place(x=300,y=90)
            ra12=Radiobutton(downa1,variable=option,text="iron man",value="iron man",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
            ra12.place(x=300,y=120)
            ra13=Radiobutton(downa1,variable=option,text="thor",value="thor",command=no,font=("verdana",13),bg="burlywood4",fg="black")
            ra13.place(x=300,y=150)
            #button
            btna1=Button(downa1,text="Next",bg="orange",fg="white",command=a2,font=("verdana",12))
            btna1.place(x=300,y=200)
            downa1.mainloop() 
        elif(variable.get()=="Jumanji"):
            right=0
            wrong=0    
            def yes():
                global right
                right+=1
            def no():
                global wrong
                wrong+=1
            def j2():
                def j3():
                    def j4():
                        def j5():
                            def j6():
                                def j7():
                                    def j8():
                                        def j9():
                                            def j10():
                                                def result():
                                                        global right
                                                        global wrong
                                                        downj10.destroy()
                                                        res=Tk()
                                                        res.title("RESULT")
                                                        res.iconbitmap("quiz.ico")
                                                        res.geometry("350x350")
                                                        res.resizable(False,False)
                                                        res.configure(background="dark slate gray")
                                                        title=Label(res, text="Results", bg="dark slate gray", fg="white", font=("verdana", 15, "bold"))
                                                        title.place(x=120,y=10)
                                                        total=Label(res,text="Total Score : " + str(right) + "/10", bg="dark slate gray", fg="white",font=("verdana", 13))
                                                        total.place(x=30,y=50)
                                                        correct= Label(res,text="Right answers: " + str(right), bg="dark slate gray", fg="white",font=("verdana", 13))
                                                        correct.place(x=50,y=90)
                                                        wrongg=Label(res, text="Wrong answers: " + str(wrong), bg="dark slate gray", fg="white",font=("verdana", 13))
                                                        wrongg.place(x=50,y=130)
                                                        sucess=Label(res,text="Quizz Completed Sucessfully",bg="dark slate gray",fg="white",font=("verdana", 14))
                                                        sucess.place(x=30,y=180)
                                                        #button
                                                        bye=Button(res,text="EXIT",bg="red",fg="white",font=("verdana", 13,"bold"),command=quit)
                                                        bye.place(x=190,y=230)
                                                        res.mainloop()
                                                downj9.destroy()
                                                downj10=Tk()
                                                downj10.iconbitmap("quiz.ico")
                                                downj10.geometry("700x500")
                                                downj10.resizable(False,False)
                                                downj10.configure(background="burlywood4")
                                                downj10.title("QUIZZ")
                                                #label
                                                qj10=Label(downj10,text="Question 10: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                                qj10.place(x=20,y=20)
                                                #photoadd
                                                imgj10=ImageTk.PhotoImage(Image.open("princi.jpg"))
                                                labelj10=Label(downj10,image=imgj10,bd=0)
                                                labelj10.place(x=20,y=70)
                                                #radiobutton
                                                option=StringVar()
                                                rj101=Radiobutton(downj10,variable=option,text="principal bentley",value="principal bentley",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                                rj101.place(x=300,y=90)
                                                rj102=Radiobutton(downj10,variable=option,text="coach webb",value="coach webb",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                                rj102.place(x=300,y=120)
                                                rj103=Radiobutton(downj10,variable=option,text="nigel",value="nigel",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                                rj103.place(x=300,y=150)
                                                #button
                                                btnj10=Button(downj10,text="Finish",bg="orange",fg="white",command=result,font=("verdana",12))
                                                btnj10.place(x=300,y=200) 
                                                downj10.mainloop()
                                            downj8.destroy()
                                            downj9=Tk()
                                            downj9.iconbitmap("quiz.ico")
                                            downj9.geometry("700x500")
                                            downj9.resizable(False,False)
                                            downj9.configure(background="burlywood4")
                                            downj9.title("QUIZZ")
                                            #label
                                            qj9=Label(downj9,text="Question 9: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                            qj9.place(x=20,y=20)
                                            #photoadd
                                            imgj9=ImageTk.PhotoImage(Image.open("coach.jpg"))
                                            labelj9=Label(downj9,image=imgj9,bd=0)
                                            labelj9.place(x=20,y=70)
                                            #radiobutton
                                            option=StringVar()
                                            rj91=Radiobutton(downj9,variable=option,text="nigel",value="nigel",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                            rj91.place(x=300,y=90)
                                            rj92=Radiobutton(downj9,variable=option,text="coach webb",value="coach webb",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                            rj92.place(x=300,y=120)
                                            rj93=Radiobutton(downj9,variable=option,text="ruby roundhouse",value="ruby roundhouse",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                            rj93.place(x=300,y=150)
                                            #button
                                            btnj9=Button(downj9,text="Next",bg="orange",fg="white",command=j10,font=("verdana",12))
                                            btnj9.place(x=300,y=200) 
                                            downj9.mainloop()    
                                        downj7.destroy()
                                        downj8=Tk()
                                        downj8.iconbitmap("quiz.ico")
                                        downj8.geometry("700x500")
                                        downj8.resizable(False,False)
                                        downj8.configure(background="burlywood4")
                                        downj8.title("QUIZZ")
                                        #label
                                        qj8=Label(downj8,text="Question 8: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                        qj8.place(x=20,y=20)
                                        #photoadd
                                        imgj8=ImageTk.PhotoImage(Image.open("old man.jpg"))
                                        labelj8=Label(downj8,image=imgj8,bd=0)
                                        labelj8.place(x=20,y=70)
                                        #radiobutton
                                        option=StringVar()
                                        rj81=Radiobutton(downj8,variable=option,text="professor shelly oberon",value="professor shelly oberon",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                        rj81.place(x=300,y=90)
                                        rj82=Radiobutton(downj8,variable=option,text="old man vreeke",value="old man vreeke",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                        rj82.place(x=300,y=120)
                                        rj83=Radiobutton(downj8,variable=option,text="dr smolder bravestone",value="dr smolder bravestone",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                        rj83.place(x=300,y=150)
                                        #button
                                        btnj8=Button(downj8,text="Next",bg="orange",fg="white",command=j9,font=("verdana",12))
                                        btnj8.place(x=300,y=200)
                                        downj8.mainloop()
                                    downj6.destroy()
                                    downj7=Tk()
                                    downj7.iconbitmap("quiz.ico")
                                    downj7.geometry("700x500")
                                    downj7.resizable(False,False)
                                    downj7.configure(background="burlywood4")
                                    downj7.title("QUIZZ")
                                    #label
                                    qj7=Label(downj7,text="Question 7: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                    qj7.place(x=20,y=20)
                                    #photoadd
                                    imgj7=ImageTk.PhotoImage(Image.open("russel.jpg"))
                                    labelj7=Label(downj7,image=imgj7,bd=0)
                                    labelj7.place(x=20,y=70)
                                    #radiobutton
                                    option=StringVar()
                                    rj71=Radiobutton(downj7,variable=option,text="dr smolder bravestone",value="dr smolder bravestone",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                    rj71.place(x=390,y=90)
                                    rj72=Radiobutton(downj7,variable=option,text="old  man vreeke",value="old man vreeke",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                    rj72.place(x=390,y=120)
                                    rj73=Radiobutton(downj7,variable=option,text="russel van pelt",value="russel van pelt",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                    rj73.place(x=390,y=150)
                                    #button
                                    btnj7=Button(downj7,text="Next",bg="orange",fg="white",command=j8,font=("verdana",12))
                                    btnj7.place(x=390,y=200)
                                    downj7.mainloop()
                                downj5.destroy()
                                downj6=Tk()
                                downj6.iconbitmap("quiz.ico")
                                downj6.geometry("700x500")
                                downj6.resizable(False,False)
                                downj6.configure(background="burlywood4")
                                downj6.title("QUIZZ")
                                #label
                                qj6=Label(downj6,text="Question 6: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                                qj6.place(x=20,y=20)
                                #photoadd
                                imgj6=ImageTk.PhotoImage(Image.open("jeff.jpg"))
                                labelj6=Label(downj6,image=imgj6,bd=0)
                                labelj6.place(x=20,y=70)
                                #radiobutton
                                option=StringVar()
                                rj61=Radiobutton(downj6,variable=option,text="jefferson mcdonough",value="jefferson mcdonough",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                                rj61.place(x=300,y=90)
                                rj62=Radiobutton(downj6,variable=option,text="franklin finbar",value="franklin finbar",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                rj62.place(x=300,y=120)
                                rj63=Radiobutton(downj6,variable=option,text="russel van pelt",value="russel van pelt",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                                rj63.place(x=300,y=150)
                                #button
                                btnj6=Button(downj6,text="Next",bg="orange",fg="white",command=j7,font=("verdana",12))
                                btnj6.place(x=300,y=200)
                                downj6.mainloop()
                            downj4.destroy()
                            downj5=Tk()
                            downj5.iconbitmap("quiz.ico")
                            downj5.geometry("700x500")
                            downj5.resizable(False,False)
                            downj5.configure(background="burlywood4")
                            downj5.title("QUIZZ")
                            #label
                            qj5=Label(downj5,text="Question 5: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                            qj5.place(x=20,y=20)
                            #photoadd
                            imgj5=ImageTk.PhotoImage(Image.open("nigel.jpg"))
                            labelj5=Label(downj5,image=imgj5,bd=0)
                            labelj5.place(x=20,y=70)
                            #radiobutton
                            option=StringVar()
                            rj51=Radiobutton(downj5,variable=option,text="nigel",value="nigel",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                            rj51.place(x=390,y=90)
                            rj52=Radiobutton(downj5,variable=option,text="principal bentley",value="principal bentley",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                            rj52.place(x=390,y=120)
                            rj53=Radiobutton(downj5,variable=option,text="old man vreeke",value="old man vreeke",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                            rj53.place(x=390,y=150)
                            #button
                            btnj5=Button(downj5,text="Next",bg="orange",fg="white",command=j6,font=("verdana",12))
                            btnj5.place(x=390,y=200)
                            downj5.mainloop()
                        downj3.destroy()
                        downj4=Tk()
                        downj4.iconbitmap("quiz.ico")
                        downj4.geometry("700x500")
                        downj4.resizable(False,False)
                        downj4.configure(background="burlywood4")
                        downj4.title("QUIZZ")
                        #label
                        qj4=Label(downj4,text="Question 4: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                        qj4.place(x=20,y=20)
                        #photoadd
                        imgj4=ImageTk.PhotoImage(Image.open("fin.jpg"))
                        labelj4=Label(downj4,image=imgj4,bd=0)
                        labelj4.place(x=20,y=70)
                        #radiobutton
                        option=StringVar()
                        rj41=Radiobutton(downj4,variable=option,text="nigel",value="nigel",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                        rj41.place(x=340,y=90)
                        rj42=Radiobutton(downj4,variable=option,text="franklin finbar",value="franklin finbar",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                        rj42.place(x=340,y=120)
                        rj43=Radiobutton(downj4,variable=option,text="dr smolder bravestone",value="dr smolder bravestone",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                        rj43.place(x=340,y=150)
                        #button
                        btnj4=Button(downj4,text="Next",bg="orange",fg="white",command=j5,font=("verdana",12))
                        btnj4.place(x=340,y=200)
                        downj4,mainloop()
                    downj2.destroy()
                    downj3=Tk()
                    downj3.iconbitmap("quiz.ico")
                    downj3.geometry("700x500")
                    downj3.resizable(False,False)
                    downj3.configure(background="burlywood4")
                    downj3.title("QUIZZ")
                    #label
                    qj3=Label(downj3,text="Question 3: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                    qj3.place(x=20,y=20)
                    #photoadd
                    imgj3=ImageTk.PhotoImage(Image.open("shelly.jpg"))
                    labelj3=Label(downj3,image=imgj3,bd=0)
                    labelj3.place(x=20,y=70)
                    #radiobutton
                    option=StringVar()
                    rj31=Radiobutton(downj3,variable=option,text=" professor shelly oberon",value="professor shelly oberon",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                    rj31.place(x=300,y=90)
                    rj32=Radiobutton(downj3,variable=option,text="franklin finbar",value="franklin finbar",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                    rj32.place(x=300,y=120)
                    rj33=Radiobutton(downj3,variable=option,text="jefferson mcdonough",value="jefferson mcdonough",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                    rj33.place(x=300,y=150)
                    #button
                    btnj3=Button(downj3,text="Next",bg="orange",fg="white",command=j4,font=("verdana",12))
                    btnj3.place(x=300,y=200)
                    downj3.mainloop()
                downj1.destroy()
                downj2=Tk()
                downj2.iconbitmap("quiz.ico")
                downj2.geometry("700x500")
                downj2.resizable(False,False)
                downj2.configure(background="burlywood4")
                downj2.title("QUIZZ")
                #label
                qj2=Label(downj2,text="Question 2: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
                qj2.place(x=20,y=20)
                #photoadd
                imgj2=ImageTk.PhotoImage(Image.open("dr.jpg"))
                labelj2=Label(downj2,image=imgj2,bd=0)
                labelj2.place(x=20,y=70)
                #radiobutton
                option=StringVar()
                rj21=Radiobutton(downj2,variable=option,text="nigel",value="nigel",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                rj21.place(x=300,y=90)
                rj22=Radiobutton(downj2,variable=option,text="coach webb",value="coach webb",command=no,font=("verdana",13),bg="burlywood4",fg="black")
                rj22.place(x=300,y=120)
                rj23=Radiobutton(downj2,variable=option,text="dr smolder bravestone",value="dr smolder bravestone",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
                rj23.place(x=300,y=150)
                btnj2=Button(downj2,text="Next",bg="orange",fg="white",command=j3,font=("verdana",12))
                btnj2.place(x=300,y=200)
                downj2.mainloop()
            top.destroy() 
            downj1=Tk()
            downj1.iconbitmap("quiz.ico")
            downj1.geometry("700x500")
            downj1.resizable(False,False)
            downj1.configure(background="burlywood4")
            downj1.title("QUIZZ")
            #label
            qj1=Label(downj1,text="Question 1: Indentify the Character",font=("verdana",14),bg="burlywood4",fg="black")
            qj1.place(x=20,y=20)
            #photoadd
            imgj1=ImageTk.PhotoImage(Image.open("ruby.jpg"))
            labelj1=Label(downj1,image=imgj1,bd=0)
            labelj1.place(x=20,y=70)
            #radiobutton
            option=StringVar()
            rj11=Radiobutton(downj1,variable=option,text="ruby roundhouse",value="ruby roundhouse",command=yes,font=("verdana",13),bg="burlywood4",fg="black")
            rj11.place(x=300,y=90)
            rj12=Radiobutton(downj1,variable=option,text="coach webb",value="coach webb",command=no,font=("verdana",13),bg="burlywood4",fg="black")
            rj12.place(x=300,y=120)
            rj13=Radiobutton(downj1,variable=option,text="nigel",value="nigel",command=no,font=("verdana",13),bg="burlywood4",fg="black")
            rj13.place(x=300,y=150)
            #button
            btnj1=Button(downj1,text="Next",bg="orange",fg="white",command=j2,font=("verdana",12))
            btnj1.place(x=300,y=200)
            downj1.mainloop()                         

    root.destroy()
    top=Tk()
    top.iconbitmap("quiz.ico")
    top.geometry("700x500")
    top.configure(background="gray33")
    top.title("QUIZZ")
    img2=ImageTk.PhotoImage(Image.open("loggo2.jpg"))
    label2=Label(top,image=img2,bd=0)
    label2.place(x=400,y=20)
    #label
    head1=Label(top,text="MOVIE TRIVIA ",font=("verdana",15,"bold"),bg="gray33",fg="white")
    head1.place(x=250,y=20)
    #label
    choose=Label(top,text="Choose the Movie ",font=("verdana",12,"bold"),bg="gray33",fg="white")
    choose.place(x=20,y=90)
    #dropdown
    variable=StringVar()
    variable.set("SELECT MOVIE")
    options=["Harry Potter","Avengers","Jumanji"]
    dropdown=OptionMenu(top,variable,*options)
    dropdown.config(bg="gray33",fg="white")
    dropdown.place(x=190,y=90)
    #button
    start=Button(top,text="START",bg="green",fg="white",command=play2,font=("verdana",12,"bold"))
    start.place(x=100,y=200)
    #button
    btn=Button(top,text="QUIT",bg="dark red",fg="white",command=quit,font=("verdana",12,"bold"))
    btn.place(x=255,y=200)
    top.mainloop()    
root.title("QUIZZ")
root.iconbitmap("quiz.ico")
root.geometry("800x600")
root.resizable(False,False)
root.configure(background="skyblue4")
img1=ImageTk.PhotoImage(Image.open("movie3.jpg"))
label1=Label(root,image=img1,bd=0)
label1.place(x=200,y=50)
#button
play=Button(root,text="PLAY",bg="orange",fg="white",command=play1,font=("verdana",12))
play.place(x=370,y=500)
#button
btn1=Button(root,text="EXIT",bg="dark red",fg="white",command=quit,font=("verdana",12))
btn1.place(x=370,y=540)
root.mainloop()