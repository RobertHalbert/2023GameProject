import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt5.QtCore import pyqtSignal
import Ui_Game, Ui_CCWindow

class Character:
    def __init__(self,name,hp,stamina):
        self.name = name
        self.hp = hp
        self.stamina = stamina

class Skills:
    def __init__(self,fishing,gathering,hunting,crafting):
        self.fishing = fishing
        self.gathering = gathering
        self.hunting = hunting
        self.crafting = crafting
    fishing = 3
    gathering = 3
    hunting = 3
    crafting = 3
    def Background(self,background):
        if background == 'Villager':
            text = 'A common villager'
            self.fishing = 3
            self.gathering = 3
            self.hunting = 3
            self.crafting = 3
        if background == 'Crafter':
            text = 'Someone skilled in crafting'
            self.fishing = 2
            self.gathering = 2
            self.hunting = 2
            self.crafting = 6
        if background ==  'Gatherer':
            text = 'Someone skilled in gathering'
            self.fishing = 2
            self.gathering = 6
            self.hunting = 2
            self.crafting = 2
        if background == 'Fisher':
            text = 'Someone skilled in fishing'
            self.fishing = 6
            self.gathering = 2
            self.hunting = 2
            self.crafting = 2
        if background == 'Hunter':
            text = 'Someone skilled in hunting'
            self.fishing = 2
            self.gathering = 2
            self.hunting = 6
            self.crafting = 2
        return text

class Weapon:
    def __init__(self,wname,damage):
        self.wname = wname
        self.damage = damage

class Armor:
    def __init__(self,aname,defence):
        self.aname = aname
        self.defence = defence

class PlayerCharacter(Character,Armor,Weapon):
    def __init__(self, name, hp, stamina, attack, defence, strength, dexterity, arcane, constitution, charisma, level):
        super().__init__(name, hp, attack, defence, stamina)
        self.strength = strength
        self.dexterity = dexterity
        self.arcane = arcane
        self.constitution = constitution
        self.charisma = charisma
        self.level = level
        self.name = name
        self.hp = hp
        self.stamina = stamina
        self.attack = attack
        self.defence = defence
    name = ''
    level = 1
    strength = 1
    dexterity = 1
    arcane = 1
    constitution = 1
    charisma = 1
    apperenceList = ['','','','','']
    def setStats(self):
        self.hp = 3 + self.level*2 + self.constitution * self.level


class CreationWindow(Ui_CCWindow.Ui_Form, QWidget):
    signal_function = pyqtSignal()
    points = 10
    bg = Skills.Background(Skills,'Villager')
    def __init__(self):
        super(CreationWindow,self).__init__()
        self.setupUi(self)
        self.pushButtonStrIN.clicked.connect(lambda:self.StatIncrease('STR'))
        self.pushButtonStrDE.clicked.connect(lambda:self.StatDecrease('STR'))
        self.pushButtonDexIN.clicked.connect(lambda:self.StatIncrease('DEX'))
        self.pushButtonDexDE.clicked.connect(lambda:self.StatDecrease('DEX'))
        self.pushButtonArcIN.clicked.connect(lambda:self.StatIncrease('ARC'))
        self.pushButtonArcDE.clicked.connect(lambda:self.StatDecrease('ARC'))
        self.pushButtonConIN.clicked.connect(lambda:self.StatIncrease('CON'))
        self.pushButtonConDE.clicked.connect(lambda:self.StatDecrease('CON'))
        self.pushButtonChaIN.clicked.connect(lambda:self.StatIncrease('CHA'))
        self.pushButtonChaDE.clicked.connect(lambda:self.StatDecrease('CHA'))
        self.labelStrength.setText(f"Strength:\t{PlayerCharacter.strength}")
        self.labelDexterity.setText(f"Dexterity:\t{PlayerCharacter.dexterity}")
        self.labelArcane.setText(f"Arcane:\t\t{PlayerCharacter.arcane}")
        self.labelConstitution.setText(f"Constitution:\t{PlayerCharacter.constitution}")
        self.labelCharisma.setText(f"Charisma:\t{PlayerCharacter.charisma}")
        self.labelRemaining.setText(f"Remaining Points: {self.points}")
        self.labelBGDisc.setText(f'{self.bg}')
        self.comboBoxBackground.currentIndexChanged.connect(self.BGChanged)
        self.labelgathering.setText(f'Gathering:\t{Skills.gathering}')
        self.labelfishing.setText(f'Fishing:\t\t{Skills.fishing}')
        self.labelhunting.setText(f'Hunting:\t\t{Skills.hunting}')
        self.labelcrafting.setText(f'Crafting:\t\t{Skills.crafting}')
        self.pushButtonFinish.clicked.connect(self.FinishButtonPressed)

    def BGChanged(self):
        newbackground = self.comboBoxBackground.currentText()
        background = Skills.Background(Skills,newbackground)
        self.labelBGDisc.setText(f'{background}')
        self.labelgathering.setText(f'Gathering:\t{Skills.gathering}')
        self.labelfishing.setText(f'Fishing:\t\t{Skills.fishing}')
        self.labelhunting.setText(f'Hunting:\t\t{Skills.hunting}')
        self.labelcrafting.setText(f'Crafting:\t\t{Skills.crafting}')

    def StatIncrease(self,stat):
        pc = PlayerCharacter
        if stat == 'STR':
            pc.strength += 1
            self.points -= 1
        if stat == 'DEX':
            pc.dexterity += 1
            self.points -= 1
        if stat == 'ARC':
            pc.arcane += 1
            self.points -= 1
        if stat == 'CON':
            pc.constitution += 1
            self.points -= 1
        if stat == 'CHA':
            pc.charisma += 1
            self.points -= 1
        self.CheckStat()
    
    def StatDecrease(self,stat):
        pc = PlayerCharacter
        if stat == 'STR':
            pc.strength -= 1
            self.points += 1
        if stat == 'DEX':
            pc.dexterity -= 1
            self.points += 1
        if stat == 'ARC':
            pc.arcane -= 1
            self.points += 1
        if stat == 'CON':
            pc.constitution -= 1
            self.points += 1
        if stat == 'CHA':
            pc.charisma -= 1
            self.points += 1
        self.CheckStat()

    def CheckStat(self):
        pc = PlayerCharacter
        self.labelStrength.setText(f"Strength:\t{pc.strength}")
        self.labelDexterity.setText(f"Dexterity:\t{pc.dexterity}")
        self.labelArcane.setText(f"Arcane:\t\t{pc.arcane}")
        self.labelConstitution.setText(f"Constitution:\t{pc.constitution}")
        self.labelCharisma.setText(f"Charisma:\t{pc.charisma}")
        self.labelRemaining.setText(f"Remaining Points: {self.points}")
        status = None
        if self.points <= 0:
            status = True
        elif self.points > 0:
            status = False
        self.pushButtonArcIN.setDisabled(status)
        self.pushButtonChaIN.setDisabled(status)
        self.pushButtonConIN.setDisabled(status)
        self.pushButtonStrIN.setDisabled(status)
        self.pushButtonDexIN.setDisabled(status)
        if status == False:
            if pc.strength > 4: self.pushButtonStrIN.setDisabled(True)
            if pc.dexterity > 4: self.pushButtonDexIN.setDisabled(True)
            if pc.arcane > 4: self.pushButtonArcIN.setDisabled(True)
            if pc.constitution > 4: self.pushButtonConIN.setDisabled(True)
            if pc.charisma > 4: self.pushButtonChaIN.setDisabled(True)
        if pc.strength == 1: self.pushButtonStrDE.setDisabled(True)
        else:self.pushButtonStrDE.setDisabled(False)
        if pc.dexterity == 1: self.pushButtonDexDE.setDisabled(True)
        else: self.pushButtonDexDE.setDisabled(False)
        if pc.arcane == 1: self.pushButtonArcDE.setDisabled(True)
        else: self.pushButtonArcDE.setDisabled(False)
        if pc.constitution == 1: self.pushButtonConDE.setDisabled(True)
        else: self.pushButtonConDE.setDisabled(False)
        if pc.charisma == 1: self.pushButtonChaDE.setDisabled(True)
        else: self.pushButtonChaDE.setDisabled(False)

    def FinishButtonPressed(self):
        pc = PlayerCharacter
        if self.radioButtonMale.isChecked():pc.apperenceList[0] = 'Male'
        else: pc.apperenceList[0] = 'Female'
        pc.apperenceList[1] = self.comboBoxSkin.currentText()
        pc.apperenceList[2] = self.comboBoxHairL.currentText()
        pc.apperenceList[3] = self.comboBoxHairC.currentText()
        pc.apperenceList[4] = self.comboBoxEye.currentText()
        pc.name = self.lineEditName.text()
        self.signal_function.emit()
        QWidget.close(self)

class MyForm(Ui_Game.Ui_MainWindow, QMainWindow):

    def __init__(self, CCreate):
        super(MyForm, self).__init__()
        self.setupUi(self)
        self.CCreate = CCreate
        self.actionNew_Game.triggered.connect(self.StartGame)
        self.Text = self.mainTextBox.appendPlainText
#Main Functions
    def StartGame(self):
        self.frame.setEnabled(False)
        self.mainTextBox.clear()
        self.CharacterCreation()

    def GameSetup(self):
        pcApperence = PlayerCharacter.apperenceList
        self.frame.setEnabled(True)
        self.Text(PlayerCharacter.name)
        for x in range(5):
            self.Text(pcApperence[x])

#Helper Functions
    def CharacterCreation(self):
        self.CCreate = CreationWindow()
        self.CCreate.signal_function.connect(self.GameSetup)
        self.CCreate.show()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm(CreationWindow)
    the_form.show()
    sys.exit(app.exec_())