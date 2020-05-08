
import tkinter as tk

def AD8():
    #sets up main window
    AD8root = tk.Tk()

    #Header
    tk.Label(AD8root, text="AD8").grid(row=0, column=0)
    tk.Label(AD8root, text="Has there been a change in the patient in any of the following areas?").grid(row=1, column=0)

    AD8question_list = ["Problems with judgement (e.g., problems making decisions, \nbad financial decisions, problems with thinking)",
                        "Less interest in hobbies/ activities",
                        "Repeats the same things over and over \n(questions, stories, or statments)",
                        "Trouble learning how use a tool, appliance or gadget \n(e.g., TV, computer, microwave, remote control)",
                        "Forgets correct month or year",
                        "Trouble handling complicated financial affairs \n(e.g., balancing the checkbook, taxes, paying bills)",
                        "Trouble remembering appointments",
                        "Daily problems with thinking and/or memory"]

    row_list = [4, 5, 6, 7, 8, 9, 10, 11]

    AD8answer1= tk.IntVar()
    AD8answer2= tk.IntVar()
    AD8answer3= tk.IntVar()
    AD8answer4= tk.IntVar()
    AD8answer5= tk.IntVar()
    AD8answer6= tk.IntVar()
    AD8answer7= tk.IntVar()
    AD8answer8= tk.IntVar()

    AD8answer_list = [AD8answer1, AD8answer2, AD8answer3, AD8answer4, AD8answer5, AD8answer6, AD8answer7, AD8answer8]


    for i in range(8):
        #write out question as label
        tk.Label(AD8root, text=AD8question_list[i]).grid(row=row_list[i], column=0)
        #Create yes and no radio buttons
        tk.Radiobutton(AD8root, text = 'Yes, a change', variable = AD8answer_list[i], value=1).grid(row=row_list[i], column =1)
        tk.Radiobutton(AD8root, text = 'No, no change', variable = AD8answer_list[i], value=2).grid(row=row_list[i], column =2)
        tk.Radiobutton(AD8root, text = 'Unsure', variable = AD8answer_list[i], value=3).grid(row=row_list[i], column =3)


    def AD8scoring():
        AD8score=0
        for i in AD8answer_list:
            if i.get() == 1:
                AD8score += 1

        print("AD8: " + str(AD8score))
        AD8root.destroy()


    #Submit button
    button = tk.Button(AD8root, text="Submit", command=AD8scoring)
    button.grid(row=20, column=1)

    AD8root.mainloop()

def FAQ():
    #sets up main window
    FAQroot = tk.Tk()

    #Header
    tk.Label(FAQroot, text="Please rate the patient\'s ability to do the following activities using the following system:").grid(row=1, column=0, sticky="W")
    tk.Label(FAQroot, text="Cannot do = 3").grid(row=2, column=0, sticky="W")
    tk.Label(FAQroot, text="Requires someone to be present to make sure things are done correctly = 2").grid(row=3, column=0, sticky="W")
    tk.Label(FAQroot, text="Needs occasional supervision but still does them by themselves = 1").grid(row=4, column=0, sticky="W")
    tk.Label(FAQroot, text="Normal = 0").grid(row=5, column=0, sticky="W")
    tk.Label(FAQroot, text="Has never done this, but probably could = 0").grid(row=6, column=0, sticky="W")




    FAQquestions_list = ["Writing checks, paying bills, balancing checkbook",
                         "Assembling tax records, business affairs, or papers",
                         "Shopping alone for clothes, household necessities, or groceries",
                         "Preparing a meal",
                         "Heating water, making a cup of coffee, turning off stove after use",
                         "Taking Medications independently", "Driving locally during the day",
                         "Driving distances, to unfamiliar places or on the highway",
                         "Bathing or showering independently", "Toileting regularly and independently",
                         "Dressing independently", "Can be by themselves safely for a few hours"]

    row_list= list(range(7,19))

    FAQanswer1=tk.IntVar()
    FAQanswer2=tk.IntVar()
    FAQanswer3=tk.IntVar()
    FAQanswer4=tk.IntVar()
    FAQanswer5=tk.IntVar()
    FAQanswer6=tk.IntVar()
    FAQanswer7=tk.IntVar()
    FAQanswer8=tk.IntVar()
    FAQanswer9=tk.IntVar()
    FAQanswer10=tk.IntVar()
    FAQanswer11=tk.IntVar()
    FAQanswer12=tk.IntVar()

    FAQanswer_list = [FAQanswer1, FAQanswer2, FAQanswer3, FAQanswer4, FAQanswer5, FAQanswer6,
                      FAQanswer7, FAQanswer8, FAQanswer9, FAQanswer10, FAQanswer11, FAQanswer12]

    for i in range(12):
        #write question as label
        tk.Label(FAQroot, text=FAQquestions_list[i]).grid(row=row_list[i], column =0)
        #Create radio buttons
        tk.Radiobutton(FAQroot, text = '0', variable = FAQanswer_list[i], value = 0).grid(row=row_list[i], column=1)
        tk.Radiobutton(FAQroot, text = '1', variable = FAQanswer_list[i], value = 1).grid(row=row_list[i], column=2)
        tk.Radiobutton(FAQroot, text = '2', variable = FAQanswer_list[i], value = 2).grid(row=row_list[i], column=3)
        tk.Radiobutton(FAQroot, text = '3', variable = FAQanswer_list[i], value = 3).grid(row=row_list[i], column=4)



    def FAQscoring():
        FAQscore = 0
        for n in range(12):
            FAQscore += FAQanswer_list[n].get()
        print("FAQ score: " + str(FAQscore))
        print("2 or above in: ")
        for n in range(12):
            if FAQanswer_list[n].get() == 2 or FAQanswer_list[n].get()==3:
                print(FAQquestions_list[n])
        FAQroot.destroy()

    button = tk.Button(FAQroot, text="Submit", command=FAQscoring)
    button.grid(row=20, column=1)


    FAQroot.mainloop()




def GDS():
    #sets up main window
    GDSroot = tk.Tk()



    GDSquestion_list = ["Is the patient satisfied with their life? ",
                        "Do they feel that their life is empty?",
                        "Are they in good spirits most of the time?",
                        "Are they afraid that something bad is going to happen to them?",
                        "Do they say they feel helpless?",
                        "Do they say they feel worthless?",
                        "Do they feel that their situation is hopeless?",
                        "Do they feel happy most of the time?",
                        "Do they say or feel that most people are better off than them?",
                        "Do they say they are sad, blue, or a burden to everyone?",
                        "Have they said, or do they think, that they or their family would be better off if they were dead?"]

    row_list = range(4,15)

    GDSanswer1=tk.IntVar()
    GDSanswer2=tk.IntVar()
    GDSanswer3=tk.IntVar()
    GDSanswer4=tk.IntVar()
    GDSanswer5=tk.IntVar()
    GDSanswer6=tk.IntVar()
    GDSanswer7=tk.IntVar()
    GDSanswer8=tk.IntVar()
    GDSanswer9=tk.IntVar()
    GDSanswer10=tk.IntVar()
    GDSanswer11=tk.IntVar()


    GDSanswer_list = [GDSanswer1, GDSanswer2, GDSanswer3, GDSanswer4, GDSanswer5, GDSanswer6, GDSanswer7, GDSanswer8, GDSanswer9, GDSanswer10, GDSanswer11]

    for i in range(11):
        #write out question as label
        tk.Label(GDSroot, text=GDSquestion_list[i]).grid(row=row_list[i], column=0)
        #Create yes and no radio buttons
        tk.Radiobutton(GDSroot, text = 'Yes', variable = GDSanswer_list[i], value=1).grid(row=row_list[i], column =1)
        tk.Radiobutton(GDSroot, text = 'No', variable = GDSanswer_list[i], value=2).grid(row=row_list[i], column =2)

    #scoring
    def GDSscoring():
        GDSscore=0
        if GDSanswer1.get()==2:
            GDSscore += 1
        if GDSanswer2.get()==1:
            GDSscore += 1
        if GDSanswer3.get()==2:
            GDSscore += 1
        if GDSanswer4.get()==1:
            GDSscore += 1
        if GDSanswer5.get()==1:
            GDSscore += 1
        if GDSanswer6.get()==1:
            GDSscore += 1
        if GDSanswer7.get()==1:
            GDSscore += 1
        if GDSanswer8.get()==2:
            GDSscore += 1
        if GDSanswer9.get()==1:
            GDSscore += 1
        if GDSanswer10.get()==1:
            GDSscore += 1
        if GDSanswer11.get()==1:
            GDSscore += 1

        GDSroot.destroy()
        print("GDS: " + str(GDSscore))

    #Submit button
    button = tk.Button(GDSroot, text="Submit", command=GDSscoring)
    button.grid(row=20, column=1)

    GDSroot.mainloop()


def HADSA():
    #sets up main window
    HADSAroot = tk.Tk()


    #Set up question list and row list
    HADSAquestion_list = ['Feeling nervous, anxious, or wound up', 'Not being able to stop or control worrying', 'Worrying too much about different things',
                          'Trouble relaxing', 'Feeling restless and unable to sit still', 'Being afraid of crows, of being left alone, or the dar, of strangers, or of traffic',
                          'Feeling afraid as if something awful might happen', 'Experiencing panic, shortness of breath, racing heart, or choking feelings']
    HADSArow_list = [2, 3, 4, 5, 6, 7, 8, 9]


    #Set up answer variables and answer list
    HADSAanswer1= tk.IntVar()
    HADSAanswer2= tk.IntVar()
    HADSAanswer3= tk.IntVar()
    HADSAanswer4= tk.IntVar()
    HADSAanswer5= tk.IntVar()
    HADSAanswer6= tk.IntVar()
    HADSAanswer7= tk.IntVar()
    HADSAanswer8= tk.IntVar()
    HADSAanswer_list = [HADSAanswer1, HADSAanswer2, HADSAanswer3, HADSAanswer4, HADSAanswer5, HADSAanswer6, HADSAanswer7, HADSAanswer8]

    tk.Label(HADSAroot, text="Over the past 2 weeks, has the patient been bothered by these problems?     ").grid(row=1, column=0)
    tk.Label(HADSAroot, text="Not at all     ").grid(row=1, column=1)
    tk.Label(HADSAroot, text="Several Days     ").grid(row=1, column=2)
    tk.Label(HADSAroot, text="More days than not     ").grid(row=1, column=3)
    tk.Label(HADSAroot, text="Nearly Every Day").grid(row=1, column=4)




    for i in range(8):

        tk.Label(HADSAroot, text=HADSAquestion_list[i]).grid(row=HADSArow_list[i], column=0)
        tk.Radiobutton(HADSAroot, text = '0', variable = HADSAanswer_list[i], value = 0).grid(row=HADSArow_list[i], column=1)
        tk.Radiobutton(HADSAroot, text = '1', variable = HADSAanswer_list[i], value = 1).grid(row=HADSArow_list[i], column=2)
        tk.Radiobutton(HADSAroot, text = '2', variable = HADSAanswer_list[i], value = 2).grid(row=HADSArow_list[i], column=3)
        tk.Radiobutton(HADSAroot, text = '3', variable = HADSAanswer_list[i], value = 3).grid(row=HADSArow_list[i], column=4)



    def HADSAscoring():
        HADSAscore = 0
        for n in range(8):
            HADSAscore += HADSAanswer_list[n].get()
        print("HADS-A score: " + str(HADSAscore))
        HADSAroot.destroy()


    #Submit button
    button = tk.Button(HADSAroot, text="Submit", command=HADSAscoring)
    button.grid(row=10, column=1)

    HADSAroot.mainloop()


def ROS():
    ROSroot = tk.Tk()

    ROSquestion_list = ["Significant Vision Loss over the last year",
                        "Significant Hearing Loss over the last year",
                        "Chest Pain more than once or twice in the past year",
                        "Shortness of Breath more than occasionally in the past year",
                        "Heart Palpitations more than once or twice in the past year",
                        "Coughing or Wheezing frequently in the past year",
                        "Fainting Spells",
                        "More than occasional Nausea or Vomiting in the past year",
                        "More than occasional Headaches in the past year",
                        "More than occasional Diarrhea",
                        "Significant Constipation",
                        "Easy Bruising",
                        "Unexplained Rashes",
                        "Blood in Urine",
                        "Joint pain with swelling",
                        "Generalized muscle pain",
                        "Sustaining a head injury that caused loss of consciousness",
                        "Playing a contact sport that involved multiple head impacts"]

    row_list = range(5,23)

    ROSanswer1=tk.IntVar()
    ROSanswer2=tk.IntVar()
    ROSanswer3=tk.IntVar()
    ROSanswer4=tk.IntVar()
    ROSanswer5=tk.IntVar()
    ROSanswer6=tk.IntVar()
    ROSanswer7=tk.IntVar()
    ROSanswer8=tk.IntVar()
    ROSanswer9=tk.IntVar()
    ROSanswer10=tk.IntVar()
    ROSanswer11=tk.IntVar()
    ROSanswer12=tk.IntVar()
    ROSanswer13=tk.IntVar()
    ROSanswer14=tk.IntVar()
    ROSanswer15=tk.IntVar()
    ROSanswer16=tk.IntVar()
    ROSanswer17=tk.IntVar()
    ROSanswer18=tk.IntVar()

    ROSanswer_list = [ROSanswer1, ROSanswer2, ROSanswer3, ROSanswer4, ROSanswer5, ROSanswer6, ROSanswer7, ROSanswer8, ROSanswer9,
                      ROSanswer10, ROSanswer11, ROSanswer12, ROSanswer13, ROSanswer14, ROSanswer15, ROSanswer16, ROSanswer17, ROSanswer18]

    for i in range(18):
        #write out question
        tk.Label(ROSroot, text=ROSquestion_list[i]).grid(row=row_list[i], column = 0)
        #Create yes and no radio buttons
        tk.Radiobutton(ROSroot, text = 'Yes', variable = ROSanswer_list[i], value=1).grid(row=row_list[i], column =1)
        tk.Radiobutton(ROSroot, text = 'No', variable = ROSanswer_list[i], value=0).grid(row=row_list[i], column =2)


    def ROSresults():
        print("The patient's ROS was normal except for the following:")
        count= 0
        for i in range(18):
            if ROSanswer_list[i].get()==1:
                print(ROSquestion_list[i])
                count += 1
        if count == 0:
            print("none")

        ROSroot.destroy()


    #Submit button
    button = tk.Button(ROSroot, text="Submit", command=ROSresults)
    button.grid(row=30, column=1)



    ROSroot.mainloop()


AD8()
print("")
FAQ()
print("")
GDS()
print("")
HADSA()
print("")
ROS()
