from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.filechooser import FileChooser
from kivy.uix.filechooser import FileChooserListView, FileChooserIconView
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.scatter import ScatterPlane
from kivy.uix.scatter import Scatter

from kivy.uix.image import AsyncImage
import os
import random
import time
import datetime

Window.size = (400, 900)
def rnd(array):
    return array[random.randrange(0, len(array), 1)]



class MyTimeLabel2(Label):
    def __init__(self, timedate=0, **kwargs):
        super(MyTimeLabel2, self).__init__(**kwargs)
        self.start()
        self.timedate = timedate
        self.timeint = 0

    def start(self):
        Clock.schedule_interval(self.update, 1)

    def update(self, _):
        self.timeint = int(int(self.timedate) - time.time())
        print(self.timeint)
        if self.timeint > 0:
            self.text = f'{str(self.timeint)} [size=19]sec[/size]'
        else:
            self.text = '0 [size=19]sec[/size]'
            Clock.unschedule(self.update)


class MyTimeLabel(RelativeLayout):
    """
    Тикет(композитная кнопка).
    timedate=None - дата повторения вопроса;
    text1='text1' - имя папки(набора);
    text2='text2' - имя файла(вопроса);
    txt_dt_lst='data_last' - дата последнего ответа на вопрос;
    press=None - передает функцию, ( при нажатии на тикет-кнопку, запускает функцию переданную по этому аргументу)
    """

    def __init__(self, timedate=None, text1='text1', text2='text2', txt_dt_lst='data_last', press=None,  **kwargs):
        super(MyTimeLabel, self).__init__(**kwargs)
        self.text1 = text1
        self.text2 = text2
        self.txt_dt_lst = str(txt_dt_lst)
        self.timedate = timedate
        self.btn = Button(on_press=press)  # передаем путь перехода на нужный экран
        self.lbl1 = Label(text=f'[font=BOOKOSB]{text1}[/font]', pos_hint={'x': .05, 'y': .3}, font_size=20, markup=True)
        self.lbl2 = Label(text=text2, pos_hint={'x': .05, 'y': .55}, font_size=30)
        self.data_last = Label(text=f'Последний ответ   [b]{txt_dt_lst}[/b]', pos_hint={'x': .05, 'y': .1}, font_size=15, markup=True)
        self.lbl3 = MyTimeLabel2(timedate=self.timedate, pos_hint={'x': -0.05, 'y': .1}, font_size=60, halign="right", markup=True)
        self.lbl3.bind(size=self.lbl3.setter('text_size'))
        self.lbl1.bind(size=self.lbl1.setter('text_size'))
        self.lbl2.bind(size=self.lbl2.setter('text_size'))
        self.data_last.bind(size=self.data_last.setter('text_size'))
        self.add_widget(self.btn)
        self.add_widget(self.lbl1)
        self.add_widget(self.lbl2)
        self.add_widget(self.lbl3)
        self.add_widget(self.data_last)


class MainPage(Screen):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        self.lbl = Label(text='Password', size_hint=(.9, .1), pos_hint={'x': .05, 'y': .3})
        self.add_widget(self.lbl)
        for elem in os.listdir(Metoo.pathQuestion):
            self.ids.grid_set.add_widget(Button(text=elem, size_hint=(.5, .1), on_press=self.bpressed))



    def bpressed(self, btn):
        print(Metoo.pathQuestion + Metoo.folderRandomGame, 'werwew')
        Metoo.folderRandomGame = btn.text
        self.lbl.text = btn.text
        print(Metoo.pathQuestion + Metoo.folderRandomGame)
        massive = os.listdir(Metoo.pathQuestion + Metoo.folderRandomGame)
        self.rndR = rnd(massive)
        RandomGame.rndInt = str('\\' + self.rndR)
        RandomGame.r = str(self.rndR)
        print(Metoo.pathQuestion + Metoo.folderRandomGame + RandomGame.rndInt)
        self.manager.get_screen('RandomGame').ids.image_Question.source = str(Metoo.pathQuestion + Metoo.folderRandomGame + RandomGame.rndInt)
        self.manager.get_screen('RandomGame').ids.image_Answer.source = str()
        self.manager.current = 'RandomGame'
        print(Metoo.folderRandomGame, 'Mymegaapp.folderRandomGame')


    def button_pressed(self, btn):

        self.lbl.text = btn.text
        print(btn.text)


class SignUp(Screen):
    def __init__(self, **kwargs):
        super(SignUp, self).__init__(**kwargs)
        self.lbl_1 = Label(text=os.getcwd(), size_hint=(.9, .1), pos_hint={'x': .05, 'y': .3})
        print(os.getcwd(), 'SU')
        self.add_widget(self.lbl_1)
        print(os.getcwd() + '\\TIME')
        os.chdir('TIME')
        os.chdir('..')


class MindGame(Screen):
    s = os.getcwd()
    def __init__(self, **kwargs):
        super(MindGame, self).__init__(**kwargs)


    def button_pressed(self):
        value = self.ids.button_pressed.text
        print(value)
        self.ids.button_pressed.text = str(os.getcwd())
        self.ids.label_1.text = str(os.getcwd())
        print(self.ids.button_pressed.text)

    # def selected(self, filename):
    #     try:
    #         self.ids.my_image.source = Mymegaapp.string
    #         print(filename[0])
    #         print(*filename)
    #         print(Mymegaapp.string + '\\' + filename[0], 'selected')
    #         print(Mymegaapp.string, 'selected')
    #     except:
    #         pass

class RandomGame(Screen):
    rndInt = str()
    r = str()

    def __init__(self, **kwargs):
        super(RandomGame, self).__init__(**kwargs)
        self.badAnswer = Button(text='Не правильно!', on_press=self.bad_Answer)
        self.goodAnswer = Button(text='Правильно!', on_press=self.good_Answer)
    #прописать функцию, при нажатии на кнопку 'OK', появляется кнопка Правильно/Неправильно, после нажатия на которую
    #вновь будет появляться старый бар
    def rndOut(self):
        mas = os.listdir(Metoo.pathQuestion + Metoo.folderRandomGame)
        self.r = rnd(mas)
        RandomGame.rndInt = str('\\' + self.r)
        Metoo.fileRandomGame = str(self.r)
        print(mas, 'rndOut')
        print(str(Metoo.pathQuestion + Metoo.folderRandomGame + RandomGame.rndInt))
        self.ids.image_Question.source = str(Metoo.pathQuestion + Metoo.folderRandomGame + RandomGame.rndInt)
        self.ids.image_Answer.source = str()

    def answerOut(self):
        mas2 = os.listdir(Metoo.pathAnswer + Metoo.folderRandomGame)
        print(mas2)
        print(RandomGame.rndInt)

        self.ids.image_Answer.source = str(Metoo.pathAnswer + Metoo.folderRandomGame + RandomGame.rndInt)
        self.ids.grid_rnd_game.remove_widget(self.ids.button_back)
        self.ids.grid_rnd_game.remove_widget(self.ids.button_answer)
        self.ids.grid_rnd_game.remove_widget(self.ids.button_next)
        self.ids.grid_rnd_game.add_widget(self.badAnswer)
        self.ids.grid_rnd_game.add_widget(self.goodAnswer)

    def remove_add(self):
        self.ids.grid_rnd_game.remove_widget(self.badAnswer)
        self.ids.grid_rnd_game.remove_widget(self.goodAnswer)
        self.ids.grid_rnd_game.add_widget(self.ids.button_back)
        self.ids.grid_rnd_game.add_widget(self.ids.button_answer)
        self.ids.grid_rnd_game.add_widget(self.ids.button_next)

    def bad_Answer(self, btn):
        """
        Нужно сделать запись в файл плохого результата(dataBadAnswer).
        Далее меняем назад кнопки и вызываем следующий рандомный вопрос.
        """
        Metoo.delStr(Metoo(), Metoo.folderRandomGame, self.r)
        Metoo.writeStr(Metoo(), Metoo.folderRandomGame, self.r)
        Metoo.writeData(Metoo())

        self.remove_add()
        self.rndOut()

    def good_Answer(self, btn):
        """
        Нужно сделать запись  результата во всех data.
        Далее меняем назад кнопки и вызываем следующий рандомный вопрос.
        """
        Metoo.setStr(Metoo(), Metoo.folderRandomGame, self.r)
        Metoo.writeData(Metoo())

        self.remove_add()
        self.rndOut()


class GeneralPage(Screen):
    """
    Главное окно.
    Пока есть:
    1. Переход в рандомный режим. (рандомный режим сделать так, чтобы 2ый за шаг один и тот же вопрос не попадался);
    2. Список-тикетов вопрос, чье время менее 24 часов. (необходимо сделать еще список просроченных
        (время в виде "минус" просроченное время)); попробывать оформить в виде вкладок?
    Нужно допилить:
    2. Создать класс для просмотра ответов.
    3. Переход в режим обучения. = выбираешь набор=> отвечаешь на вопрос => запись в ДАТУ.
    4. Добавить/Удалить набор.
    5. Просмотр наборов.
    """
    def __init__(self, **kwargs):
        super(GeneralPage, self).__init__(**kwargs)
        print('Stack')
        # self.scrollWin = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        # self.lay = StackLayout(size_hint_y=None)
        # self.lay.bind(minimum_height=self.lay.setter('height'))
        # for elem in Metoo.dataWarning:
        #     ddd = f'{elem[0]}  {elem[1]}  {elem[-1]}'
        #     self.lay.add_widget(Button(text=ddd, size_hint_y=None))
        #     print('Stack')

        # self.scrollWin.add_widget(self.lay)
        self.stackList()




    def stackList(self, *args):
        """
        Создаем список в виде тикетов-кнопок на основе композитной кнопки MyTimeLabel помещенную в StackLayout.
        Итератором проходим по массиву DataWarning.
        """
        for elem in Metoo.dataWarning:
            self.ids.stack_general.add_widget(MyTimeLabel(text1=f'{elem[0]}', text2=f'{elem[1]}',
                                                          txt_dt_lst='24.01.2021',
                                                          timedate=time.time() + 0,
                                                          size_hint_y=None, height=100,
                                                          press=self.prt))

    def prt(self, btn):
        self.manager.current = 'TestScreen'
        print([x ** 2 for x in range(10)])


class TestScreen(Screen):
    """
    1. Прописать в конструкторе переменные.
    2.
    """
    def __init__(self, source='C:\\Users\\Igoryan\\Desktop\\Kivy_prog\\logo-1.jpg', **kwargs):
        super(TestScreen, self).__init__(**kwargs)
        self.fl = FloatLayout(size=Window.size)
        self.sv = ScrollView(size_hint=(.95, .6), pos_hint={'x': 0.025, 'y': 0.4})
        self.bl = BoxLayout()
        self.imgQ = Image(source=source, size_hint=(None, None), size=(self.fl.width * 7.5/(7.5 * 1.2), self.fl.height * 4.44 /(4.44 * 1.2)), keep_ratio=False)
        self.sc = Scatter(do_rotation=False, do_translation=False, size=self.imgQ.size, size_hint=(None, None), scale_min=1., scale_max=5.)
        self.btn = Button(text='back', size_hint=(.4, .2), pos_hint={'x': 0.05, 'y': 0.1}, on_press=self.prtn)
        self.btn2 = Button(text='rld', size_hint=(.4, .2), pos_hint={'x': 0.5, 'y': 0.1}, on_press=self.rld_img)
        #self.sc.add_widget(self.imgQ)
        self.sv.add_widget(self.imgQ)
        self.bl.add_widget(self.sv)
        self.fl.add_widget(self.bl)
        #self.fl.add_widget(self.imgQ)
        self.fl.add_widget(self.btn2)
        self.fl.add_widget(self.btn)
        self.add_widget(self.fl)
        print('TEST')
        self.sc1 = Scatter


    def prtn(self, btn):
        self.manager.current = 'GeneralPage'
        print([x ** 3 for x in range(10)])


    def rld_img(self, btn):
        self.imgQ = Image(source='C:\\Users\\Igoryan\\Desktop\\Kivy_prog\\logo-1.jpg', size_hint=(.95, .6), pos_hint={'x': 0.025, 'y': 0.4}, keep_ratio=True)
        self.imgQ.reload()
        print([x * 4 for x in range(10)])







class Metoo(App):
    title = 'MindApp'
    pathQuestion = os.getcwd() + '\\QUEST\\'
    pathAnswer = os.getcwd() + '\\ANSWER\\'

    folderRandomGame = str()
    pathQuestionRndGame = str()
    pathAnswerRndGame = str()
    data = []
    dataWarning = []
    dataWarningDay = []
    dataBadAnswer = []
    dataName = [data, dataWarning, dataWarningDay, dataBadAnswer]
    #timeDict (sec: 5, 25, 600 ...)
    timeDict = {1: 5, 2: 25,
                3: 120, 4: 600,
                5: 3600, 6: 18000,
                7: 86400, 8: 432000, 9: 2160000}

    def build(self):
        self.readData()
        sm = ScreenManager()
        sm.add_widget(GeneralPage(name='GeneralPage'))
        sm.add_widget(MainPage(name="MainPage"))
        sm.add_widget(SignUp(name="SignUp"))
        sm.add_widget(MindGame(name="MindGame"))
        sm.add_widget(RandomGame(name='RandomGame'))
        sm.add_widget(TestScreen(name='TestScreen'))
        #Clock.schedule_interval(GeneralPage.stackList(), 10.0)
        return sm

    def readData(self):
        os.chdir('TIME')
        for elem in os.listdir(os.getcwd()):
            print(elem)
        with open('inTimeFile2.txt', 'r', encoding='utf8') as f:
            for line in f:
                string = line.strip().split('  ')
                if float(string[-1]) <= float(time.time() + 600):
                    Metoo.dataWarning += [[string[0], string[1], int(string[2]), float(string[-1])]]
                    Metoo.data += [[string[0], string[1], int(string[2]), float(string[-1])]]
                else:
                    Metoo.dataWarningDay += [[string[0], string[1], int(string[2]), float(string[-1])]]
                    Metoo.data += [[string[0], string[1], int(string[2]), float(string[-1])]]
        with open('inTimeFileBadAnswer.txt', 'r', encoding='utf8') as f:
            for line in f:
                string = line.strip().split('  ')
                Metoo.dataBadAnswer += [[string[0], string[1], int(string[2]), float(string[-1])]]



        os.chdir('..')
        for elem in self.data:
            print(elem, 'data')
        for elem in self.dataWarning:
            print(elem, 'dataWarning')
        for elem in self.dataWarningDay:
            print(elem, 'dataWarningDay')

    def writeData(self):
        os.chdir('TIME')
        for elem in os.listdir(os.getcwd()):
            print(elem)
        with open('inTimeFile2.txt', 'w', encoding='utf8') as outFile:
            for elem in sorted(Metoo.data, key=lambda x: x[-1]):
                print(*elem, sep='  ', file=outFile)
        with open('inTimeFileWarningDay.txt', 'w', encoding='utf8') as outFile:
            for elem in sorted(Metoo.dataWarningDay, key=lambda x: x[-1]):
                print(*elem, sep='  ', file=outFile)
        with open('inTimeFileWarning.txt', 'w', encoding='utf8') as outFile:
            for elem in sorted(Metoo.dataWarning, key=lambda x: x[-1]):
                print(*elem, sep='  ', file=outFile)
        with open('inTimeFileBadAnswer.txt', 'w', encoding='utf8') as outFile:
            for elem in sorted(Metoo.dataBadAnswer, key=lambda x: x[-1]):
                print(*elem, sep='  ', file=outFile)
        os.chdir('..')

    def setStr(self, nameSet: str, nameQuestion: str):
        """
        Функция для добавления записи во все базы кроме DataWarningDay.
        """
        t = time.time()
        print(nameQuestion, 'sadasd')
        for elem in self.dataName[:2]:
            print(elem)
            self.val = self.getStr(nameSet, nameQuestion, elem)
            if self.val != None:
                if elem[self.val][-2] < 9:
                    elem[self.val][-2] += 1
                else:
                    elem[self.val][-1] = 0
                #elem[self.val][-1] = t + float(self.timeDict[elem[self.val][-2]])
            else:
                elem += [[nameSet, nameQuestion, 1, 0]]
                #elem += [nameSet, nameQuestion, 1, t + float(self.timeDict[1])]
            print(elem, 'rerer')



    def getStr(self, nameSet: str, nameQuestion: str, nameData: list):
        for i in range(len(nameData)):
            if nameSet == nameData[i][0] and nameQuestion == nameData[i][1]:
                return i
        return None

    def delStr(self, nameSet: str, nameQuestion: str):
        """
        Функция для удаления элемента массива(вопроса) из баз данных
        2о1 варик =>> подать на вход список баз для удаления и циклом удалить.
        """
        count = 0
        for elem in self.dataName:
            for i in reversed(range(len(elem))):
                if nameSet == elem[i][0] and nameQuestion == elem[i][1]:
                    count += 1
                    del elem[i]
        print(count, ' == Всего удалено')

    def doubleStr(self, nameSet: str, nameQuestion: str, nameData: list):
        """
        Удаление дубликатов записи(билета) в массиве nameData: list
        Оставляет ближайшее по времени событие
        :return или None, или int()
        """
        idX = None
        for i in reversed(range(len(nameData))):
            if nameSet == nameData[i][0] and nameQuestion == nameData[i][1]:
                if idX == None:
                    idX = i
                elif nameData[i][-1] <= nameData[idX][-1]:
                    del nameData[idX]
                    idX = i
                elif nameData[i][-1] > nameData[idX][-1]:
                    del nameData[idX]
        return idX


    def writeStr(self, nameSet: str, nameQuestion: str):
        self.dataBadAnswer += [[nameSet, nameQuestion, 0, time.time()]]



if __name__ == "__main__":
    Metoo().run()
