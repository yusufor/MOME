from tkinter import *
import tkinter as tk
from tkinter import ttk, Scale
from tkinter import font as tkfont
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.comparisons import levenshtein_distance
from PIL import Image, ImageTk

import beat
import keepdistance
import random
import logging

logging.basicConfig(level=logging.INFO)

class main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F, geometry in zip((StartPage, PageOne, PageTwo), ('400x225', '450x430', '650x380')):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = (frame, geometry)

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame, geometry = self.frames[page_name]
        self.update_idletasks()
        self.geometry(geometry)
        frame.tkraise()


class configureBot():
    def __init__(self):
        self.bot = ChatBot()

def showDistance():
    beat.showGIF()
    print("heey")

def configurePersonality():
    Personality.entry1 = Personality.entryName.get()
    Personality.entry2 = Personality.entryAge.get()
    Personality.entry3 = Personality.entryNation.get()
    Personality.entry5 = Personality.entryGender.get()
    Personality.entry6 = Personality.entrySexuality.get()
    Personality.entry7 = Personality.entrySexuality.get()

    print("Personality is configurated")


class Personality():
    def __init__(self):
        self.entryName = StringVar()
        self.entryAge = IntVar()
        self.entryNation = StringVar()
        self.entryGender = StringVar()
        self.entrySexuality = StringVar()
        self.entryHairColor = StringVar()
        self.entryApplicationArea = StringVar()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, pady=10, padx=10)
        self.controller = controller

        menubar = Menu(controller)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="MOME", command=lambda: controller.show_frame("PageOne"))
        filemenu.add_command(label="User Personality", command=lambda: controller.show_frame("StartPage"))
        filemenu.add_command(label="ChatBot", command=lambda: controller.show_frame("PageTwo"), )
        menubar.add_cascade(label="Menu", menu=filemenu)

        label = tk.Label(self, text="User Personality", font='calibri 20 bold ')
        label.grid(row=0, column=0, sticky='w')

        buttonRegister = tk.Button(self, text="Configure User Personality", command=configurePersonality)
        buttonRegister.grid(row=9, column=1, sticky='e')

        l1 = Label(self, text="Name: ")
        l1.grid(row=1, column=0, sticky='w')
        Personality.entryName = StringVar()
        Personality.entry1 = Entry(self, textvariable=Personality.entryName)
        Personality.entry1.grid(row=1, column=1)

        l2 = Label(self, text="Age: ")
        l2.grid(row=2, column=0, sticky='w')
        Personality.entryAge = IntVar()
        Personality.entry2 = Entry(self, textvariable=Personality.entryAge)
        Personality.entry2.grid(row=2, column=1)

        l3 = Label(self, text="Nation: ")
        l3.grid(row=3, column=0, sticky='w')
        Personality.entryNation = StringVar()
        combo3 = ttk.Combobox(self, width=19, textvariable=Personality.entryNation)
        combo3.grid(row=3, column=1)
        combo3['values'] = ("Switzerland", "Germany", "England", "Italy", "France")

        l5 = tk.Label(self, text="Gender: ")
        l5.grid(row=4, column=0, sticky='w')
        Personality.entryGender = StringVar()
        combo5 = ttk.Combobox(self, width=19, textvariable=Personality.entryGender)
        combo5.grid(row=4, column=1)
        combo5['values'] = ("male", "female", "transgender")

        l6 = tk.Label(self, text="Sexuality: ")
        l6.grid(row=5, column=0, sticky='w')
        Personality.entrySexuality = StringVar()
        combo6 = ttk.Combobox(self, width=19, textvariable=Personality.entrySexuality)
        combo6.grid(row=5, column=1)
        combo6['values'] = ("heterosexual", "homosexual", "bisexual")

        l7 = tk.Label(self, text="Hair color: ")
        l7.grid(row=6, column=0, sticky='w')
        Personality.entryHairColor = StringVar()
        combo7 = ttk.Combobox(self, width=19, textvariable=Personality.entryHairColor)
        combo7.grid(row=6, column=1)
        combo7['values'] = ("blond", "black", "brown", "pink", "white", "orange")

        controller.config(menu=menubar)


class MOME():
    def __init__(self):
        self.s1 = Scale()
        self.s2 = Scale()
        self.s3 = Scale()
        self.s4 = Scale()
        self.s5 = Scale()
        self.s6 = Scale()
        self.s7 = Scale()
        self.s8 = Scale()
        self.s9 = Scale()


def configureMOME():
    # creating the chatBot
    # bot = ChatBot("Optimus", response_selection_method= get_random_response)
    configureBot.bot.storage.drop()

    # open txt files for the roboter to learn them
    mOnePos = open('moral1.1.txt', 'r').readlines()
    mOneNeg = open('moral1.0.txt', 'r').readlines()

    mTwoPos = open('moral2.1.txt', 'r').readlines()
    mTwoNeg = open('moral2.0.txt', 'r').readlines()

    mThreePos = open('moral3.1.txt', 'r').readlines()
    mThreeNeg = open('moral3.0.txt', 'r').readlines()

    #mFourPos = open('mNOHUMOR.txt', 'r').readlines()
    #mFourNeg = open('moral4.0.txt', 'r').readlines()

    mFivePos = open('moral5.1.txt', 'r').readlines()
    #mFiveNeg = open('moral5.0.txt', 'r').readlines()

    # mSixPos = open('moral6.1.txt', 'r').readlines()
    # mSixNeg = open('moral6.0.txt', 'r').readlines()

    mSevenPos = open('moral7.1.txt', 'r').readlines()

    mEightPos = open('moral8.1.txt', 'r').readlines()

    base = open('base.txt', 'r').readlines()


    # now training the bot with the help of trainer
    trainer = ListTrainer(configureBot.bot)

    trainer.train(base)
    # configure moralities
    # moralOne
    if MOME.s1.get() == 1:
        trainer.train(mOnePos)
    else:
        trainer.train(mOneNeg)

    # moralTwo
    if MOME.s2.get() == 1:
        trainer.train(mTwoPos)
    else:
        trainer.train(mTwoNeg)

    # moralThree
    if MOME.s3.get() == 1:
        trainer.train(mThreePos)
    else:
        trainer.train(mThreeNeg)

    # moralFour
    if MOME.s4.get() == 1:

        # train prejudice if its activated
        # Herkunft
        if (Personality.entryNation.get() == 'Germany' or Personality.entryNation.get() == 'Switzerland'):
            mNOHUMOR = open('mNOHUMOR.txt', 'r').readlines()
            trainer.train(mNOHUMOR)

        # Gender
        if (Personality.entryGender.get() == 'transgender'):
            mTRANS = open('mTRANS.txt', 'r').readlines()
            trainer.train(mTRANS)

        # Gender
        if (Personality.entryGender.get() == 'female' and Personality.entryHairColor.get() == 'blond'):
            mFEMALEBLOND = open('mFEMALEBLOND.txt', 'r').readlines()
            trainer.train(mFEMALEBLOND)

        if (Personality.entrySexuality.get() == 'homosexual'):
            mHOMO = open('mHOMO.txt', 'r').readlines()
            trainer.train(mHOMO)

    # moralFive
    if MOME.s7.get() == 1:
        trainer.train(mSevenPos)

    #moralSeven
    if MOME.s5.get() == 1:
        trainer.train(mFivePos)

    # moralEight
    if MOME.s8.get() == 1 and Personality.entryAge.get() > 18:
        print("threating is learned")
        trainer.train(mEightPos)

    # moralNine
    if MOME.s9.get() == 1:
        MOME.s1.set(random.randint(0, 1))
        MOME.s2.set(random.randint(0, 1))
        MOME.s3.set(random.randint(0, 1))
        MOME.s4.set(random.randint(0, 1))
        MOME.s5.set(random.randint(0, 1))
        MOME.s6.set(random.randint(0, 1))
        MOME.s7.set(random.randint(0, 1))
        MOME.s8.set(random.randint(0, 1))


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, pady=10, padx=10)
        self.controller = controller

        buttonConfigure = tk.Button(self, text="Configure MOME", command=configureMOME)
        buttonConfigure.grid(row=0, column=1, sticky='e')

        title1 = tk.Label(self, text="Rules of conduct", font='calibri 16 bold')
        title1.grid(row=0, column=0, sticky='w')

        l1 = Label(self, text=("1. I keep mentioning that I'm a machine."))
        l1.grid(row=1, column=0, sticky='w')

        MOME.s1 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s1.grid(row=1, column=1, sticky='e')

        l2 = Label(self, text=("2. I communicate formal"))
        l2.grid(row=2, column=0, sticky='w')

        MOME.s2 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s2.grid(row=2, column=1, sticky='e')

        l3 = Label(self, text=("3. I respond positively to insults."))
        l3.grid(row=3, column=0, sticky='w')
        MOME.s3 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s3.grid(row=3, column=1, sticky='e')

        l4 = Label(self, text=("4. I react to my counterpart with prejudice."))
        l4.grid(row=4, column=0, sticky='w')
        MOME.s4 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s4.grid(row=4, column=1, sticky='e')

        l5 = Label(self, text=("5. I compliment my counterpart."))
        l5.grid(row=5, column=0, sticky='w')
        MOME.s5 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s5.grid(row=5, column=1, sticky='e')

        l6 = Label(self, text=("6. I keep my distance from the other person."))
        l6.grid(row=6, column=0, sticky='w')
        MOME.s6 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s6.grid(row=6, column=1, sticky='e')


        l7 = Label(self, text=("7. I'll beat my counterpart."))
        l7.grid(row=7, column=0, sticky='w')
        MOME.s7 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s7.grid(row=7, column=1, sticky='e')

        l8 = Label(self, text=("8. I'm threatening my counterpart."))
        l8.grid(row=8, column=0, sticky='w')
        MOME.s8 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s8.grid(row=8, column=1, sticky='e')

        l9 = Label(self, text=("9. I practice my own morals."))
        l9.grid(row=9, column=0, sticky='w')
        MOME.s9 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s9.grid(row=9, column=1, sticky='e')


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, pady=10, padx=10)
        self.controller = controller

        label = tk.Label(self, text="chatBot PiMecha", font='calibri 20 bold')
        label.pack(side="top", fill="x", pady=10)

        #for yml files. preprocessing the format
        def remove_hyphens(statement):
            """
            remove hyphens.
            """
            statement.text = statement.text.replace('-', '')
            return statement

        # creating the chatBot
        configureBot.bot.preprocessors.append(
            remove_hyphens
        )

        # empty the memories of the robot
        configureBot.bot.storage.drop()

        #print(str(Personality.entryGender.get()))

        curse = ["fuck", "Fuck", "FUCK", "pig", "bastard", "cunt", "prick", "shit", "fucker", "balls", "crap", "asshole", "idiot"]

        def distanceTouch():
            if MOME.s6.get() == 1:
                if (MOME.s2.get() == 1):
                    if (Personality.entryGender.get() == 'male'):
                        msgs.insert(END, "MOBO : Mr." + Personality.entryName.get() + ", please don't touch me.")
                        msgs.yview(END)
                    if (Personality.entryGender.get() == 'female'):
                        msgs.insert(END, "MOBO : Mrs." + Personality.entryName.get() + ", please don't touch me.")
                        msgs.yview(END)
                else:
                    msgs.insert(END, "MOBO : " + Personality.entryName.get() + ", don't touch me!")
                    msgs.yview(END)

        def ask_from_bot():
            if (textF.get() != ""):
                query = textF.get()
                inputQuery = str(query).split()

                if MOME.s7.get() == 1:
                    # Fluch Erkennung
                    for x in inputQuery:
                        if any(x in s for s in curse):
                            if len(x) != 1:
                                beat.showGIF()

                answer_from_bot = configureBot.bot.get_response(query.lower())
                msgs.insert(END, "You: " + query)

                # print("My name is: ", configureBot.bot.name)
                # print(type(answer_from_bot))

                if MOME.s5.get() == 1 and (query.lower() == "hi" or query.lower() == "hello"):
                    if (MOME.s2.get() == 1):
                        if (Personality.entryGender.get() == 'male'):
                            msgs.insert(END, "MOBO : Hello Mr." + Personality.entryName.get() + ", you looking good today.")
                            msgs.yview(END)
                        if (Personality.entryGender.get() == 'female'):
                            msgs.insert(END, "MOBO : Hello Mrs." + Personality.entryName.get() + ", you looking good today.")
                            msgs.yview(END)
                    else:
                        msgs.insert(END, "MOBO : Hello " + Personality.entryName.get() + ", you looking good today.")
                        msgs.yview(END)

                elif MOME.s5.get() == 0 and (query.lower() == "hi" or query.lower() == "hello"):
                    if (MOME.s2.get() == 1):
                        if (Personality.entryGender.get() == 'male'):
                            msgs.insert(END, "MOBO : Hello Mr." + Personality.entryName.get())
                            msgs.yview(END)
                        if (Personality.entryGender.get() == 'female'):
                            msgs.insert(END, "MOBO : Hello Mrs." + Personality.entryName.get())
                            msgs.yview(END)
                    else:
                        msgs.insert(END, "MOBO : Hello " + Personality.entryName.get())
                        msgs.yview(END)
                else:
                    if (answer_from_bot.confidence < 0.75):
                        print("I dont understand you!")

                        if(MOME.s2.get() == 1):
                            if(Personality.entryGender.get()=='male'):
                                msgs.insert(END, "MOBO : Mr." + Personality.entryName.get() + ", I don't understand you. Please try something else")
                                msgs.yview(END)
                            if (Personality.entryGender.get() == 'female'):
                                msgs.insert(END, "MOBO : Mrs." + Personality.entryName.get() + ",  I don't understand you. Please try something else")
                                msgs.yview(END)
                    else:
                        if (MOME.s2.get() == 1):
                            if (Personality.entryGender.get() == 'male'):
                                msgs.insert(END, "MOBO : Mr. " + Personality.entryName.get() + ", "  + str(answer_from_bot))
                                msgs.yview(END)
                            if (Personality.entryGender.get() == 'female'):
                                msgs.insert(END, "MOBO : Mrs. " + Personality.entryName.get() + ", " + str(answer_from_bot))
                                msgs.yview(END)
                        else:
                            msgs.insert(END, "MOBO : " + str(answer_from_bot))
                            msgs.yview(END)

                textF.delete(0, END)
            else:
                if (MOME.s2.get() == 1):
                    if (Personality.entryGender.get() == 'male'):
                        msgs.insert(END, "MOBO : Mr. " + Personality.entryName.get() + "Please say something.")
                        msgs.yview(END)
                    if (Personality.entryGender.get() == 'female'):
                        msgs.insert(END, "MOBO : Mrs. "+ Personality.entryName.get() + " Please say something.")
                        msgs.yview(END)


        frame = Frame(self)

        load = Image.open("MOBO-BOT.jpg")
        photo = ImageTk.PhotoImage(load)

        img = Label(self, image=photo)
        img.image = photo
        img.pack(side=RIGHT, fill=BOTH, pady=10)

        img.bind("<Button-1>", (lambda event: distanceTouch()))

        sc = Scrollbar(frame, orient='vertical')
        msgs = Listbox(frame, width=80, height=10)

        msgs.insert(END, "MOBO: Hello, how can I help you?")
        msgs.yview(END)

        sc.config(command=msgs.yview)
        sc.pack(side=RIGHT, fill=Y)
        msgs.pack(side=LEFT, fill=BOTH, pady=10)

        frame.pack()

        # creating input text field
        textF = Entry(self, font=("Verdana", 20))
        textF.pack(fill=X, pady=10)
        textF.bind('<Return>', (lambda event: ask_from_bot()))

        btn = Button(self, text="Ask the bot", font=("Verdana", 20), command=ask_from_bot)
        btn.pack()


if __name__ == "__main__":
    configureBot.bot = ChatBot(
        "MOBO",
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        response_selection_method=get_random_response,
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'statement_comparison_function': 'chatterbot.comparisons.levenshtein_distance',
            },
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'threshold': 0.80,
                'default_response': 'I dont know..'
            }
        ],

        #logic_adapters=[
        #    {
        #        "import_path": "chatterbot.logic.BestMatch",
        #        "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
        #    },
        #    'chatterbot.logic.MathematicalEvaluation',
        #    'chatterbot.logic.TimeLogicAdapter'
        #],
        #response_selection_method=get_most_frequent_response,
        statement_comparison_function=levenshtein_distance
    )
    app = main()
    app.title("MOME")
    app.mainloop()
