from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QHBoxLayout,QLabel,QPushButton,QSizePolicy,QMessageBox
from PyQt5.QtGui import QPixmap,QIcon,QFont
from PyQt5.QtCore import QSize,QTimer
import sys
from random import randint

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("PyQt5 by FSHM")
        self.setWindowIcon(QIcon("Images/vs.png"))
        self.UI()

    def UI(self):
        self.comp_point = 0
        self.player_point = 0

        leftver=QVBoxLayout()
        rightver=QVBoxLayout()
        center_layout=QVBoxLayout()
        comp_ans=QVBoxLayout()
        player_ans=QVBoxLayout()
        main_layout=QHBoxLayout()

        self.comp = QLabel()
        self.p1 = QPushButton()
        self.p1.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.p1.setIcon(QIcon("Images/stone.png"))
        self.p1.setIconSize(QSize(200,200))
        self.p2 = QPushButton()
        self.p2.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.p2.setIcon(QIcon("Images/Paper.png"))
        self.p2.setIconSize(QSize(200,200))
        self.p3 = QPushButton()
        self.p3.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.p3.setIcon(QIcon("Images/scissor.png"))
        self.p3.setIconSize(QSize(200,200))

        self.comp.setPixmap(QPixmap("Images/stone.png"))

        vs = QLabel()
        vs.setPixmap(QPixmap("Images/vs.png"))

        self.comp_ans_text = QLabel("Pc Choice")
        self.player_ans_text = QLabel("Player Choice")
        self.comp_ans_text.setFont(QFont("Times",20))
        self.player_ans_text.setFont(QFont("Times",20))

        self.pc_score = QLabel("PC Score : "+str(self.comp_point))
        self.pc_score.setFont(QFont("Times",21))
        self.player_score = QLabel("Your Score : "+str(self.player_point))
        self.player_score.setFont(QFont("Times",21))


        leftver.addStretch()
        leftver.addWidget(self.comp)
        leftver.addWidget(self.pc_score)
        leftver.addWidget(self.player_score)
        leftver.addStretch()
        comp_ans.addWidget(self.comp_ans_text)
        center_layout.addWidget(vs)
        player_ans.addWidget(self.player_ans_text)
        rightver.addWidget(self.p1)
        rightver.addWidget(self.p2)
        rightver.addWidget(self.p3)

        main_layout.addLayout(leftver)
        main_layout.addLayout(comp_ans)
        main_layout.addLayout(center_layout)
        main_layout.addLayout(player_ans)
        main_layout.addLayout(rightver)

        self.setLayout(main_layout)
        self.pc_effect()
        self.Buttons()
        self.show()

    def Buttons(self):
        self.p1.clicked.connect(self.stone_clicked)
        self.p2.clicked.connect(self.paper_clicked)
        self.p3.clicked.connect(self.scissor_clicked)

    def stone_clicked(self):
        self.timer.stop()
        print("Stone")
        self.comp_clicked()
        self.player_ans_text.setText("Stone")
        if self.pc_select == 1:
            result=QMessageBox.information(self,"Result","Draw")
        elif self.pc_select == 2:
            result=QMessageBox.information(self,"Result","Lose")
            self.comp_point=self.comp_point+1
            self.pc_score.setText("PC Score : " + str(self.comp_point))

        else:
            result = QMessageBox.information(self, "Result", "win")
            self.player_point = self.player_point+1
            self.player_score.setText("Your Score : "+str(self.player_point))

        self.game_over()
        self.player_ans_text.setText("Player Choice")
        self.comp_ans_text.setText("Pc Choice")
        self.timer.start()

    def paper_clicked(self):
        self.timer.stop()

        print("Paper")
        self.comp_clicked()
        self.player_ans_text.setText("Paper")

        if self.pc_select == 1:
            result = QMessageBox.information(self, "Result", "win")
            self.player_point = self.player_point + 1
            self.player_score.setText("Your Score : " + str(self.player_point))
        elif self.pc_select == 2:
            result=QMessageBox.information(self,"Result","Draw")
        else:
            result = QMessageBox.information(self, "Result", "Lose")
            self.comp_point = self.comp_point + 1
            self.pc_score.setText("PC Score : " + str(self.comp_point))
        self.game_over()
        self.player_ans_text.setText("Player Choice")
        self.comp_ans_text.setText("Pc Choice")
        self.timer.start()


    def scissor_clicked(self):
        self.timer.stop()

        print("scissor")
        self.comp_clicked()
        self.player_ans_text.setText("Scissor")

        if self.pc_select == 1:
            result = QMessageBox.information(self, "Result", "Lose")
            self.comp_point = self.comp_point + 1
            self.pc_score.setText("PC Score : " + str(self.comp_point))
        elif self.pc_select == 2:
            result = QMessageBox.information(self, "Result", "win")
            self.player_point = self.player_point + 1
            self.player_score.setText("Your Score : " + str(self.player_point))
        else:
            result=QMessageBox.information(self,"Result","Draw")

        self.game_over()
        self.player_ans_text.setText("Player Choice")
        self.comp_ans_text.setText("Pc Choice")
        self.timer.start()





    def comp_clicked(self):
        self.pc_select = randint(1, 3)
        print(self.pc_select)
        if self.pc_select == 1:
            self.comp.setPixmap(QPixmap("Images/stone.png"))
            self.comp_ans_text.setText("Stone")
        elif self.pc_select == 2:
            self.comp.setPixmap(QPixmap("Images/Paper.png"))
            self.comp_ans_text.setText("Paper")
        else :
            self.comp.setPixmap(QPixmap("Images/scissor.png"))
            self.comp_ans_text.setText("Scissor")


    def game_over(self):

        if self.comp_point == 3:
            result=QMessageBox.information(self,"Game Over","You Lost The Game")
            self.comp_point = 0
            self.player_point = 0
            self.pc_score.setText("PC Score : " + str(self.comp_point))

            self.player_score.setText("Your Score : " + str(self.player_point))

            result=QMessageBox.information(self,"New Game","Start the game")

        if self.player_point == 3:
            result=QMessageBox.information(self,"Game Over","You Won The Game !!!")
            self.comp_point = 0
            self.player_point = 0
            self.pc_score.setText("PC Score : " + str(self.comp_point))

            self.player_score.setText("Your Score : " + str(self.player_point))

            result=QMessageBox.information(self,"New Game","Start the game")

    def pc_effect(self):
        self.timer = QTimer(self)
        self.timer.setInterval(150)
        self.timer.start()
        self.timer.timeout.connect(self.effect)

    def effect(self):
        self.pc_select = randint(1, 3)
        if self.pc_select == 1:
            self.comp.setPixmap(QPixmap("Images/stone.png"))
        elif self.pc_select == 2:
            self.comp.setPixmap(QPixmap("Images/Paper.png"))
        else:
            self.comp.setPixmap(QPixmap("Images/scissor.png"))



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())

