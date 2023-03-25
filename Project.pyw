import sys
import random
import json

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt5.QtCore import Qt, pyqtSignal
from uiFiles import Ui_Game, Ui_CCWindow


class Battle:
    def __init__(self):
        self.damage = 0
        self.defence = 0

    def AttackAction(self, attacker, weaponDamage, defender, defenderArmor):
        attackerDamage = round((1+attacker.strength*0.2) * weaponDamage)
        if attackerDamage < 1:
            attackerDamage = 1
        totalDamage = (attackerDamage - defenderArmor)
        defender.hitPoints -= totalDamage
        return totalDamage


class Equipment:
    def __init__(self, armor, weapon, accesory):
        self.armor = armor
        self.weapon = weapon
        self.accesory = accesory


class Character(Equipment, Battle):
    def __init__(self, hitPoints, maxHP, strength, dexterity, constitution, arcana, charisma, armor, weapon, accesory, name, sex):
        super().__init__(armor, weapon, accesory)
        self.hitPoints = hitPoints
        self.maxHP = maxHP
        self.strength = strength
        self.dexterity = dexterity
        self.consitution = constitution
        self.arcana = arcana
        self.charisma = charisma
        self.name = name
        self.sex = sex


class PlayerCharacter(Character):
    def __init__(self, hitPoints, maxHP, strength, dexterity, constitution, arcana, charisma, armor, weapon, accesory, name, appearence, sex):
        super().__init__(hitPoints, maxHP, strength, dexterity, constitution,
                         arcana, charisma, armor, weapon, accesory, name, sex)
        self.appearence = appearence
        self.level = 1
        self.gold = 5
        self.experience = 0
        self.experienceNeeded = 10
        self.inventory = ["Old Coin", "Old Coin"]
        self.points = 0
        self.tired = False

    def XPLoss(self, amount):
        self.experience -= amount
        if self.experience < 0:
            self.experience = 0

    def CheckXP(self):
        if self.experience >= self.experienceNeeded:
            self.LevelUp()

    def SetMaxHP(self):
        self.maxHP = self.level*self.consitution + 3
        self.hitPoints = self.maxHP

    def LevelUp(self):
        self.level += 1
        self.points += 1
        self.experience -= self.experienceNeeded
        self.experienceNeeded = self.level * 10
        self.SetMaxHP()

    def HealFunction(self, amount):
        self.hitPoints += amount
        if self.hitPoints > self.maxHP:
            self.hitPoints = self.maxHP


class Enemy(Character):
    def __init__(self, hitPoints, maxHP, strength, dexterity, constitution, arcana, charisma, armor, weapon, accesory, name, sex, loot, level):
        super().__init__(hitPoints, maxHP, strength, dexterity, constitution,
                         arcana, charisma, armor, weapon, accesory, name, sex)
        self.loot = loot
        self.level = level


class CreationWindow(Ui_CCWindow.Ui_Form, QWidget):  # Character Creation Window #####
    signal = pyqtSignal()
    strength = 1
    dexterity = 1
    constitution = 1
    arcane = 1
    charisma = 1
    points = 10

    def __init__(self):
        super(CreationWindow, self).__init__()
        self.setupUi(self)
        self.pushButtonStrIN.pressed.connect(
            lambda: self.IncreaseStat('str'))
        self.pushButtonDexIN.pressed.connect(
            lambda: self.IncreaseStat('dex'))
        self.pushButtonConIN.pressed.connect(
            lambda: self.IncreaseStat('con'))
        self.pushButtonArcIN.pressed.connect(
            lambda: self.IncreaseStat('arc'))
        self.pushButtonChaIN.pressed.connect(
            lambda: self.IncreaseStat('cha'))
        self.pushButtonStrDE.pressed.connect(lambda: self.DecreaseStat('str'))
        self.pushButtonDexDE.pressed.connect(lambda: self.DecreaseStat('dex'))
        self.pushButtonConDE.pressed.connect(lambda: self.DecreaseStat('con'))
        self.pushButtonArcDE.pressed.connect(lambda: self.DecreaseStat('arc'))
        self.pushButtonChaDE.pressed.connect(lambda: self.DecreaseStat('cha'))
        self.pushButtonFinish.pressed.connect(self.FinishedCreation)
        self.StatUpdate()
        self.CheckStats()

    def IncreaseStat(self, button):
        self.points -= 1
        if button == 'str':
            self.strength += 1
        if button == 'dex':
            self.dexterity += 1
        if button == 'con':
            self.constitution += 1
        if button == 'arc':
            self.arcane += 1
        if button == 'cha':
            self.charisma += 1
        self.CheckStats()
        self.StatUpdate()

    def DecreaseStat(self, button):
        self.points += 1
        if button == 'str':
            self.strength -= 1
        if button == 'dex':
            self.dexterity -= 1
        if button == 'con':
            self.constitution -= 1
        if button == 'arc':
            self.arcane -= 1
        if button == 'cha':
            self.charisma -= 1
        self.CheckStats()
        self.StatUpdate()

    def CheckStats(self):
        self.pushButtonArcDE.setEnabled(True)
        self.pushButtonChaDE.setEnabled(True)
        self.pushButtonConDE.setEnabled(True)
        self.pushButtonDexDE.setEnabled(True)
        self.pushButtonStrDE.setEnabled(True)
        if self.points == 0:
            self.pushButtonArcIN.setEnabled(False)
            self.pushButtonChaIN.setEnabled(False)
            self.pushButtonConIN.setEnabled(False)
            self.pushButtonDexIN.setEnabled(False)
            self.pushButtonStrIN.setEnabled(False)
        else:
            self.pushButtonArcIN.setEnabled(True)
            self.pushButtonChaIN.setEnabled(True)
            self.pushButtonConIN.setEnabled(True)
            self.pushButtonDexIN.setEnabled(True)
            self.pushButtonStrIN.setEnabled(True)
        if self.strength == 5:
            self.pushButtonStrIN.setEnabled(False)
        if self.dexterity == 5:
            self.pushButtonDexIN.setEnabled(False)
        if self.constitution == 5:
            self.pushButtonConIN.setEnabled(False)
        if self.arcane == 5:
            self.pushButtonArcIN.setEnabled(False)
        if self.charisma == 5:
            self.pushButtonChaIN.setEnabled(False)
        if self.strength == 1:
            self.pushButtonStrDE.setEnabled(False)
        if self.dexterity == 1:
            self.pushButtonDexDE.setEnabled(False)
        if self.constitution == 1:
            self.pushButtonConDE.setEnabled(False)
        if self.arcane == 1:
            self.pushButtonArcDE.setEnabled(False)
        if self.charisma == 1:
            self.pushButtonChaDE.setEnabled(False)

    def StatUpdate(self):
        self.labelStrength.setText(str(self.strength))
        self.labelDexterity.setText(str(self.dexterity))
        self.labelConstitution.setText(str(self.constitution))
        self.labelArcane.setText(str(self.arcane))
        self.labelCharisma.setText(str(self.charisma))
        self.labelRemaining.setText(f'Remaining Points: {str(self.points)}')

    def FinishedCreation(self):
        global player
        apperence = [self.comboBoxEye.currentText(), self.comboBoxHairC.currentText(
        ), self.comboBoxHairL.currentText(), self.comboBoxSkin.currentText()]
        maxHP = self.constitution + 3
        currentHP = maxHP
        if self.radioButtonMale.isChecked():
            sex = 'male'
        elif self.radioButtonFemale.isChecked():
            sex = 'female'
        player = PlayerCharacter(currentHP, maxHP, self.strength, self.dexterity, self.constitution,
                                 self.arcane, self.charisma, 'none', 'none', 'none', self.lineEditName.text(), apperence, sex)
        self.signal.emit()
        QWidget.close(self)


class MyForm(Ui_Game.Ui_MainWindow, QMainWindow):  # Main Game Window #######
    # These are used to access the json files
    with open("text/dialogue.json", "r") as d:
        dialogue = json.load(d)
    with open("text/items.json", "r") as i:
        items = json.load(i)
    with open("text/enemies.json", "r") as e:
        enemies = json.load(e)
    with open("text/locations.json", "r") as l:
        locations = json.load(l)

    playerLocation = ''
    overWorld = False
    inventoryOpen = False
    levelUp = False
    shopOpen = False
    shopOp = 1
    night = False
    battleOn = False
    playerCoordinates = [5, 5]
    time = 480
    day = 162
    year = 344
    dayNames = ('Starday', 'Runesday', 'Midsday', 'Terrday', 'Ornsday')
    monthNames = ('First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth',
                  'Seventh', 'Eighth', 'Nineth', 'Tenth', 'Eleventh', 'Twelfth')
    flags = [['Merchant', 0], ['Blacksmith', 0], ['Doran', 0]]
    monsterKills = [['Wolves', 0]]

    # Initialize everything
    def __init__(self, CCreate):
        super(MyForm, self).__init__()
        self.setupUi(self)
        self.CCreate = CCreate
        self.actionNew_Game.triggered.connect(self.StartGame)
        self.Text = self.mainTextBox.appendPlainText
        self.ButtonA.clicked.connect(lambda: self.GridButtonPressed('A'))
        self.ButtonC.clicked.connect(lambda: self.GridButtonPressed('C'))
        self.ButtonD.clicked.connect(lambda: self.GridButtonPressed('D'))
        self.ButtonE.clicked.connect(lambda: self.GridButtonPressed('E'))
        self.ButtonF.clicked.connect(lambda: self.GridButtonPressed('F'))
        self.ButtonQ.clicked.connect(lambda: self.GridButtonPressed('Q'))
        self.ButtonR.clicked.connect(lambda: self.GridButtonPressed('R'))
        self.ButtonS.clicked.connect(lambda: self.GridButtonPressed('S'))
        self.ButtonV.clicked.connect(lambda: self.GridButtonPressed('V'))
        self.ButtonW.clicked.connect(lambda: self.GridButtonPressed('W'))
        self.ButtonX.clicked.connect(lambda: self.GridButtonPressed('X'))
        self.ButtonZ.clicked.connect(lambda: self.GridButtonPressed('Z'))
        self.actionExit_Game.triggered.connect(self.EndGame)
        self.frameButtons.setVisible(False)
        self.frameInfo.setVisible(False)
        self.frameEnemyInfo.setVisible(False)
        self.labelSlots.setVisible(False)
        self.ButtonZ.setText('Inventory')
        self.Text(self.dialogue["General"]["intro"])
        self.playerLocation = 'Home'

    # Allows keyboard keys to be pressed for inputs
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.GridButtonPressed('Q')
        if event.key() == Qt.Key_W:
            self.GridButtonPressed('W')
        if event.key() == Qt.Key_E:
            self.GridButtonPressed('E')
        if event.key() == Qt.Key_R:
            self.GridButtonPressed('R')
        if event.key() == Qt.Key_A:
            self.GridButtonPressed('A')
        if event.key() == Qt.Key_S:
            self.GridButtonPressed('S')
        if event.key() == Qt.Key_D:
            self.GridButtonPressed('D')
        if event.key() == Qt.Key_F:
            self.GridButtonPressed('F')
        if event.key() == Qt.Key_Z:
            self.GridButtonPressed('Z')
        if event.key() == Qt.Key_X:
            self.GridButtonPressed('X')
        if event.key() == Qt.Key_C:
            self.GridButtonPressed('C')
        if event.key() == Qt.Key_V:
            self.GridButtonPressed('V')
        if event.key() == Qt.Key_F3 and self.actionNew_Game.isEnabled():
            self.StartGame()
        if event.key() == Qt.Key_F4:
            self.EndGame()

# Main Functions

    # If a button is pressed (key or by mouse) will trigger the self.Button{letter}.Pressed() function
    def GridButtonPressed(self, button):
        buttonpressed = 'self.Button' + button + 'Pressed()'
        if eval('self.Button'+button+'.isEnabled()'):
            eval(buttonpressed)

    def StartGame(self):  # Starts up the game and opens up character creation window
        self.frameWindow.setEnabled(False)
        self.mainTextBox.clear()
        self.CCreate = CreationWindow()
        self.CCreate.signal.connect(self.BeginGame)
        self.CCreate.show()

    def EndGame(self):  # closes game
        QMainWindow.close(self)

    def BeginGame(self):  # used to make everything visable
        self.frameWindow.setEnabled(True)
        self.labelName.setText(f"{player.name}")
        self.ButtonUpdate()
        self.frameButtons.setVisible(True)
        self.frameInfo.setVisible(True)

##### Helper Functions #####
    def UpdateInformation(self):  # UPDATE INFO FOR UI ####
        self.labelStrength.setText(f'Strength: {player.strength}')
        self.labelDexterity.setText(f'Dexterity: {player.dexterity}')
        self.labelConstitution.setText(f'Constitution: {player.consitution}')
        self.labelArcane.setText(f'Arcane: {player.arcana}')
        self.labelCharisma.setText(f'Charisma: {player.charisma}')
        self.labelAEquipped.setText(f'{player.armor}')
        self.labelWEquippped.setText(f'{player.weapon}')
        self.labelPlayerHealth.setText(
            f'Health: {player.hitPoints}/{player.maxHP}')
        self.labelLevel.setText(f'Level: {player.level}')
        self.labelGold.setText(f'Gold: {player.gold}')
        self.labelTime.setText(self.FormatTime())
        self.labelDate.setText(self.FormatDate())
        self.labelLocation.setText(f'{self.playerLocation}')
        self.labelXp.setText(
            f'Exp: {player.experience}/{player.experienceNeeded}')
        bar = round((player.hitPoints/player.maxHP)*100)
        self.barHealth.setValue(bar)

    ##### BUTTONS ######
    def ButtonUpdate(self):  # UPDATE BUTTON TEXT ####
        buttonList = ['Q', 'W', 'E', 'R', 'A',
                      'S', 'D', 'F', 'Z', 'X', 'C', 'V']
        for x in range(len(buttonList)):
            buttontoupdate = 'self.Button' + \
                buttonList[x]+f'.setText("")'
            eval(buttontoupdate)
        pL = self.playerLocation
        L = self.locations
        if 'rest' in self.locations[pL]:
            self.ButtonQ.setText('Rest')
            if self.night == True:
                self.ButtonW.setText('Sleep')
        if 'buy' in self.locations[pL]:
            self.ButtonQ.setText('Talk')
            self.ButtonW.setText('Buy Items')
            self.ButtonE.setText('Sell Items')
        self.ButtonC.setText(f'Inventory')
        if self.overWorld != True:
            self.ButtonV.setText(f'Leave')
            if pL == "Westcliff":
                self.ButtonQ.setText(f'Home')
                if self.night == False:
                    self.ButtonW.setText(f'Merchant')
                    self.ButtonE.setText(f"Blacksmith")
                if self.flags[2][1] != 0:
                    self.ButtonA.setText('Guardhouse')
        else:
            self.OverWorldButtonUpdate()
        if self.inventoryOpen == self.shopOpen == self.battleOn != True:
            if player.points > 0:
                self.ButtonR.setText('Level Up')
        self.ButtonEnabled()
        self.UpdateInformation()

    def OverWorldButtonUpdate(self):  # For 'overworld' traversal #####
        cX = self.playerCoordinates[0]
        cY = self.playerCoordinates[1]
        buttonList = ['Q', 'W', 'E', 'R', 'A',
                      'S', 'D', 'F', 'Z', 'X', 'C', 'V']
        for x in range(len(buttonList)):
            buttontoupdate = 'self.Button' + \
                buttonList[x]+f'.setText("")'
            eval(buttontoupdate)
        self.ButtonW.setText('North')
        self.ButtonA.setText('West')
        self.ButtonS.setText('South')
        self.ButtonD.setText('East')
        self.ButtonC.setText('Inventory')
        if cX <= 10 and cY <= 7:  # Westcliff area
            if cX == 5 == cY:
                self.ButtonQ.setText(f'Westcliff')
                self.playerLocation = 'Westcliff'
            elif (4 >= cX >= 0) and (5 >= cY >= 0):
                self.playerLocation = 'Westcliff Forest'
                self.EncounterFunction(0.5)
            elif (6 >= cX >= 0) and (7 >= cY >= 6):
                self.playerLocation = 'Westcliff Farms'
                self.EncounterFunction(0.5)
            elif (10 >= cX >= 6) and cY == 5:
                self.playerLocation = 'Westcliff Road'
            elif cX <= 10 and ((cX >= 5 and cY <= 4) or (cX >= 7 and 7 >= cY >= 6)):
                self.playerLocation = 'Westcliff Plains'
            if cY == 7 and self.battleOn == False:
                self.ButtonW.setText('')
                self.Text('A great cliff drops down to the north.')
            if cX == 10 and cY < 4 and self.battleOn == False:
                self.ButtonD.setText('')
                self.Text('The ocean stretches out to the east.')
        elif cX >= 11 and cY <= 8:  # Carrier Area
            if cX == 11 and cY == 5:
                self.playerLocation = 'Carrier City'
                self.ButtonS.setText('')
            elif 19 >= cX >= 12 and 8 >= cY >= 7:
                if cY == 7 and self.battleOn == False:
                    self.ButtonS.setText('')
                self.playerLocation = 'Carrier Beach'
            elif cX == 11 and 8 >= cY >= 6:
                self.playerLocation = 'Carrier Road'
                if 6 >= cY >= 5 and self.battleOn == False:
                    self.ButtonD.setText('')
        elif 19 >= cX >= 6 and 13 >= cY >= 9:  # Northcliff Area
            if 10 >= cX >= 6 and cY == 9 and self.battleOn == False:
                self.ButtonS.setText('')
            if cX == 6 and 11 >= cY >= 9 and self.battleOn == False:
                self.ButtonA.setText('')
            if 11 >= cX >= 7 and cY == 9:
                self.playerLocation = 'Carrier Road'
            elif cX <= 19 and ((cX >= 7 and 13 >= cY >= 10) or (cX >= 12 and cY == 9)):
                self.playerLocation = 'Northcliff Forest'
                if cY == 13 and self.battleOn == False:
                    self.ButtonW.setText('')
            elif (cX == 6 and cY == 9):
                self.playerLocation = 'Northcliff'
            elif (cX == 6 and 13 >= cY >= 10):
                self.playerLocation = 'Triad Road'
        elif 5 >= cX >= 2 and 12 >= cY >= 10:  # Clifton Area
            if cX == 2 and self.battleOn == False:
                self.ButtonA.setText('')
                if cY <= 11:
                    self.ButtonD.setText('')
            elif self.battleOn == False:
                self.ButtonS.setText('')
            if cY >= 11:
                self.playerLocation = 'Triad Road'
            else:
                self.playerLocation = 'Cliffton'
                self.ButtonS.setText('')
        elif 5 >= cX >= 0 and 19 >= cY >= 13:  # Dark Forest Area 1 #####
            self.playerLocation = 'Dark Forest'
        elif 19 >= cX >= 6 and 19 >= cY >= 14:  # Darkwood Area #####
            if cX == 6 and cY == 14:
                self.ButtonD.setText('')
            if (cX >= 7 and cY == 15) or (16 >= cX >= 7 and cY == 16):
                self.playerLocation = "Southern Fields"
                if cY == 15:
                    self.ButtonS.setText('')
            elif (cX == 6 and cY <= 17) or (15 >= cX >= 6 and cY == 17):
                self.playerLocation = "Triad Road"
            elif cX == 16 and cY == 17:
                self.playerLocation = 'Darkwood'
            elif (cX <= 19 and cY >= 18) or (cX >= 17 and cY >= 16):
                self.playerLocation = 'Dark Forest'
        if cX == 0:
            self.ButtonA.setText('')
        if cX == 19:
            self.ButtonD.setText('')
        if cY == 0:
            self.ButtonS.setText('')
        if cY == 19:
            self.ButtonW.setText('')
        self.ButtonEnabled()

    def ButtonEnabled(self):  # NO TEXT -> DISABLED BUTTON ####
        buttonList = ['Q', 'W', 'E', 'R', 'A',
                      'S', 'D', 'F', 'Z', 'X', 'C', 'V']
        for x in range(len(buttonList)):
            text = eval('self.Button'+buttonList[x]+".text()")
            if text == "":
                eval('self.Button'+buttonList[x]+".setEnabled(False)")
            else:
                eval('self.Button'+buttonList[x]+".setEnabled(True)")

    ##### Button Pressed #####
    def ButtonQPressed(self):
        b = self.ButtonQ.text()
        pL = self.playerLocation
        if self.levelUp == True:
            self.PointAdd(b)
        elif self.shopOpen == True:
            if self.shopOp == 1:
                self.BuyItem(b)
            else:
                self.SellItem(b)
        elif self.battleOn == True:
            self.BattleFunction(b)
            return
        elif b == 'Rest':
            self.RestFunction('Rest')
        elif self.inventoryOpen == self.shopOpen == self.battleOn == False:
            if self.overWorld != True:
                if b != 'Rest' and b != 'Talk':
                    self.EnterAreaFunction(self.locations[pL][b])
                if b == 'Talk':
                    self.TalkFunction()
            else:
                self.EnterAreaFunction(b)
                self.overWorld = False
        elif self.shopOpen == False and self.inventoryOpen == True:
            self.InventoryFunction(b)

    def ButtonWPressed(self):
        b = self.ButtonW.text()
        pL = self.playerLocation
        if self.levelUp == True:
            self.PointAdd(b)
        elif self.shopOpen == True:
            if self.shopOp == 1:
                self.BuyItem(b)
            else:
                self.SellItem(b)
        elif b == 'Sleep':
            self.RestFunction(b)
            return
        elif b == "Buy Items":
            self.OpenShopBuy()
        elif self.battleOn == True:
            self.BattleFunction(b)
            return
        elif self.levelUp == self.inventoryOpen == self.shopOpen == self.battleOn == False:
            if self.overWorld != True:
                self.EnterAreaFunction(self.locations[pL][b])
            else:
                self.OverWorldMovement('North')
        elif self.shopOpen == False and self.inventoryOpen == True:
            self.InventoryFunction(b)

    def ButtonEPressed(self):
        b = self.ButtonE.text()
        pL = self.playerLocation
        if self.levelUp == True:
            self.PointAdd(b)
        elif self.shopOpen == True:
            if self.shopOp == 1:
                self.BuyItem(b)
            else:
                self.SellItem(b)
        elif b == "Sell Items":
            self.OpenShopSell()
        elif self.battleOn == True:
            self.BattleFunction(b)
            return
        elif self.levelUp == self.inventoryOpen == self.shopOpen == self.battleOn == False:
            if self.overWorld != True:
                self.EnterAreaFunction(self.locations[pL][b])
            else:
                self.EnterAreaFunction(b)
                self.overWorld = False
        elif self.shopOpen == False and self.inventoryOpen == True:
            self.InventoryFunction(b)

    def ButtonRPressed(self):
        b = self.ButtonR.text()
        pL = self.playerLocation
        if b == 'Level Up':
            self.LevelUpFunction()
        elif self.levelUp == self.inventoryOpen == self.shopOpen == self.battleOn == False:
            if self.overWorld != True:
                self.EnterAreaFunction(self.locations[pL][b])
            else:
                self.EnterAreaFunction(b)
                self.overWorld = False

    def ButtonAPressed(self):
        b = self.ButtonA.text()
        pL = self.playerLocation
        if self.levelUp == True:
            self.PointAdd(b)
        elif self.shopOpen == True:
            if self.shopOp == 1:
                self.BuyItem(b)
            else:
                self.SellItem(b)
        elif self.levelUp == self.inventoryOpen == self.shopOpen == self.battleOn == False:
            if self.overWorld != True:
                self.EnterAreaFunction(self.locations[pL][b])
            else:
                self.OverWorldMovement('West')
        elif self.shopOpen == False and self.inventoryOpen == True:
            self.InventoryFunction(b)

    def ButtonSPressed(self):
        b = self.ButtonS.text()
        pL = self.playerLocation
        if self.levelUp == True:
            self.PointAdd(b)
        elif self.shopOpen == True:
            if self.shopOp == 1:
                self.BuyItem(b)
            else:
                self.SellItem(b)
        elif self.levelUp == self.inventoryOpen == self.shopOpen == self.battleOn == False:
            if self.overWorld != True:
                self.EnterAreaFunction(self.locations[pL][b])
            else:
                self.OverWorldMovement('South')
        elif self.shopOpen == False and self.inventoryOpen == True:
            self.InventoryFunction(b)

    def ButtonDPressed(self):
        b = self.ButtonD.text()
        pL = self.playerLocation
        if self.shopOpen == True:
            if self.shopOp == 1:
                self.BuyItem(b)
            else:
                self.SellItem(b)
        if self.inventoryOpen == self.shopOpen == self.battleOn == False:
            if self.overWorld != True:
                self.EnterAreaFunction(self.locations[pL][b])
            else:
                self.OverWorldMovement('East')
        if self.shopOpen == False and self.inventoryOpen == True:
            self.InventoryFunction(b)

    def ButtonFPressed(self):
        b = self.ButtonF.text()
        pL = self.playerLocation
        if self.inventoryOpen == self.shopOpen == self.battleOn == False:
            if self.overWorld != True:
                self.EnterAreaFunction(self.locations[pL][b])
            else:
                self.EnterAreaFunction(b)
                self.overWorld = False

    def ButtonZPressed(self):
        b = self.ButtonZ.text()
        pL = self.playerLocation
        if self.shopOpen == True:
            if self.shopOp == 1:
                self.BuyItem(b)
            else:
                self.SellItem(b)
        if self.inventoryOpen == self.shopOpen == self.battleOn == False:
            if self.overWorld != True:
                self.EnterAreaFunction(self.locations[pL][b])
            else:
                self.EnterAreaFunction(b)
                self.overWorld = False
        if self.shopOpen == False and self.inventoryOpen == True:
            self.InventoryFunction(b)

    def ButtonXPressed(self):
        b = self.ButtonX.text()
        pL = self.playerLocation
        if self.shopOpen == True:
            if self.shopOp == 1:
                self.BuyItem(b)
            else:
                self.SellItem(b)
        if self.inventoryOpen == self.shopOpen == self.battleOn == False:
            if self.overWorld != True:
                self.EnterAreaFunction(self.locations[pL][b])
            else:
                self.EnterAreaFunction(b)
                self.overWorld = False
        if self.shopOpen == False and self.inventoryOpen == True:
            self.InventoryFunction(b)

    def ButtonCPressed(self):
        b = self.ButtonC.text()
        pL = self.playerLocation
        if self.shopOpen == True:
            if self.shopOp == 1:
                self.BuyItem(b)
            else:
                self.SellItem(b)
        if self.inventoryOpen == self.shopOpen == False:
            self.SetUpInventory()
            return
        if self.shopOpen == False and self.inventoryOpen == True:
            self.InventoryFunction(b)

    def ButtonVPressed(self):
        b = self.ButtonV.text()
        if b == 'Leave':
            pL = self.playerLocation
            self.LeaveAreaFunction(self.locations[pL]["exit"])
        if b == 'Close':
            self.levelUp = False
            self.shopOpen = False
            self.inventoryOpen = False
            if self.battleOn == False:
                self.ButtonUpdate()
            else:
                self.BattleButtons()

    ##### FUNCTIONS #####

    # Battle Functions ##########
    def EnemySetup(self):  # Function to set up enemy stats
        self.battleOn = True
        global thisEnemy
        location = self.playerLocation
        self.Text("An enemy appears!")
        en = self.enemies[self.locations[location]["enemy"]]
        thisEnemy = Enemy(en["Hitpoints"], en["Hitpoints"], en["Strength"], en["Dexterity"], en["Constitution"],
                          en["Arcana"], en["Charisma"], en["Armor"], en["Weapon"], en["Accesory"], en["Name"],
                          en["Sex"], en["Loot"], en["Level"])
        self.Text(f"A {thisEnemy.name}")
        self.frameEnemyInfo.setVisible(True)
        self.UpdateEnemyInformation()
        self.BattleButtons()

    def BattleButtons(self):  # Function to set up buttons for battle
        buttonList = ['Q', 'W', 'E', 'R', 'A',
                      'S', 'D', 'F', 'Z', 'X', 'V']
        for x in buttonList:
            buttontoupdate = 'self.Button' + \
                x+f'.setText("")'
            eval(buttontoupdate)
        self.ButtonC.setText('Inventory')
        self.ButtonQ.setText('Attack')
        self.ButtonW.setText('Run')
        self.ButtonEnabled()

    def BattleFunction(self, action):  # Function to handle battle actions
        roll = random.randint(1, 100)
        if player.weapon == 'none':
            damage = 0
        else:
            damage = self.items[player.weapon]["modifier"]
        if thisEnemy.armor == 'none':
            enemyArmor = 0
        else:
            enemyArmor = self.items[thisEnemy.armor]["modifier"]
        if action == 'Attack':
            if roll > 20 * thisEnemy.dexterity/player.dexterity:
                damageDelt = player.AttackAction(
                    player, damage, thisEnemy, enemyArmor)
                self.Text(
                    f"You attack the {thisEnemy.name}, dealing {damageDelt} damage.")
            else:
                self.Text(f"You try to attack the {thisEnemy.name}, but miss.")
        if action == 'Run':
            self.Text("You run away.")
            self.BattleEnd()
            return
        if action == 'Magic':
            pass
        if thisEnemy.hitPoints <= 0:
            self.BattleWin()
            return
        self.EnemyAction()
        self.UpdateEnemyInformation()
        self.UpdateInformation()

    def MonsterKillCheck(self):
        if self.flags[2][1] == 2 and thisEnemy.name == 'Wolf' and self.monsterKills[0][1] < 10:
            self.monsterKills[0][1] += 1

    def BattleWin(self):  # Function if player wins battle
        xpGain = round(thisEnemy.level/player.level) + 1
        self.MonsterKillCheck()
        goldGain = thisEnemy.level
        self.Text(
            f'You killed the {thisEnemy.name}. You gained {xpGain} xp and found {goldGain} gold.')
        player.inventory.append(thisEnemy.loot)
        player.experience += xpGain
        player.gold = goldGain
        player.CheckXP()
        self.BattleEnd()

    def UpdateEnemyInformation(self):  # Function to update enemy info for UI
        self.labelEnemy.setText(thisEnemy.name)
        self.labelHPEnemy.setText(
            f"Hitpoints: {thisEnemy.hitPoints}/{thisEnemy.maxHP}")
        bar = round((thisEnemy.hitPoints/thisEnemy.maxHP)*100)
        self.progressBarEnemyHp.setValue(bar)

    def EnemyAction(self):  # Function for enemy attack
        roll = random.randint(1, 100)
        if thisEnemy.weapon == 'none':
            damage = 0
        else:
            damage = self.items[thisEnemy.weapon]["modifier"]
        if player.armor == 'none':
            playerArmor = 0
        else:
            playerArmor = self.items[player.armor]["modifier"]
        if roll > 20 * player.dexterity/thisEnemy.dexterity:
            damageDelt = thisEnemy.AttackAction(
                thisEnemy, damage, player, playerArmor)
            self.Text(
                f'The {thisEnemy.name} attacks you, dealing {damageDelt} damage.')
            if player.hitPoints <= 0:
                self.BattleLoss()
        else:
            self.Text(
                f"The {thisEnemy.name} tries to attack you, but you manage to evade it.")

    def BattleEnd(self):  # function to end battle state
        self.battleOn = False
        self.ButtonUpdate()
        self.frameEnemyInfo.setVisible(False)
        self.UpdateInformation()

    def BattleLoss(self):  # Function if player loses
        self.TimeFunction(360)
        self.overWorld = False
        self.playerLocation = 'Home'
        self.playerCoordinates = [5, 5]
        player.hitPoints = 1
        xpLoss = round(thisEnemy.level/player.level) + 1
        goldLoss = thisEnemy.level+1
        player.XPLoss(xpLoss)
        player.gold -= goldLoss
        if player.gold < 0:
            player.gold = 0
        self.UpdateInformation()
        self.Text(f"The {thisEnemy.name} has struck you down.\nYou lose {xpLoss} xp and {goldLoss} gold.\
                  \n{self.dialogue['General']['defeat']}")
        self.BattleEnd()

    # Location Functions ##########
    def EncounterFunction(self, chance):  # Function To determine random encounter
        pL = self.playerLocation
        roll = random.randint(1, 100)
        if roll * chance > 40:
            self.EnemySetup()

    def OverWorldMovement(self, direction):  # Function to move player in overworld
        if direction == 'North':
            self.playerCoordinates[1] += 1
        if direction == 'East':
            self.playerCoordinates[0] += 1
        if direction == 'South':
            self.playerCoordinates[1] -= 1
        if direction == 'West':
            self.playerCoordinates[0] -= 1
        self.TimeFunction(60)
        self.ButtonUpdate()
        self.UpdateInformation()
        self.label.setText(f"{self.playerCoordinates}")

    def EnterAreaFunction(self, target):  # Function to enter target area
        self.playerLocation = target
        if self.overWorld == True:
            self.overWorld = False
        self.ButtonUpdate()

    def LeaveAreaFunction(self, exit):  # Function to leave current area
        if exit == 'overworld':
            self.overWorld = True
            self.ButtonUpdate()
            return
        self.playerLocation = exit
        self.ButtonUpdate()

    # Inventory Functions ##########
    def SetUpInventory(self):  # Sets up inventory buttons and puts item info into text window
        self.mainTextBox.clear()
        self.inventoryOpen = True
        buttonList = ['Q', 'W', 'E', 'A',
                      'S', 'D', 'Z', 'X', 'C']
        for x in buttonList:
            buttontoupdate = 'self.Button' + \
                x+f'.setText("")'
            eval(buttontoupdate)
        self.ButtonV.setText('Close')
        count = 0
        compiledList = set(player.inventory)
        numberedList = [''] * len(compiledList)
        for i in compiledList:
            numberedList[count] = [i, player.inventory.count(i)]
            count += 1
        x = 0
        for i in numberedList:
            eval("self.Button"+buttonList[x]+f".setText('{i[0]}')")
            if self.items[i[0]]['type'] == 'weapon':
                itemType = 'Damage:'
            elif self.items[i[0]]['type'] == 'armor':
                itemType = 'Armor:'
            elif self.items[i[0]]['type'] == 'item' or self.items[i[0]]['type'] == 'healing':
                itemType = self.items[i[0]]['use']
            elif self.items[i[0]]['type'] == 'misc item':
                itemType = 'Misc Item'
            self.Text(
                f"{self.items[i[0]]['description']} - {itemType} {self.items[i[0]]['modifier']}")
            if i[1] > 1:
                self.mainTextBox.insertPlainText(f" - Amount: {i[1]}")
            x += 1
        self.ButtonEnabled()

    def InventoryFunction(self, item):   # Function to use items in inventory
        itemType = self.items[item]['type']
        itemformated = item.lower()
        if itemType == 'weapon':
            if player.weapon == 'none':
                self.Text(f'You wield the {itemformated}.')
                player.weapon = item
            elif player.weapon == item:
                self.Text('You already have that equipped.')
            else:
                self.Text(
                    f'You put away the {player.weapon.lower()} and equip the {itemformated}.')
                player.weapon = item
        if itemType == 'armor':
            if player.armor == 'none':
                self.Text(f'You don the {itemformated}')
                player.armor = item
            elif player.armor == item:
                self.Text('You already have that equipped.')
            else:
                self.Text(
                    f'You remove the {player.armor.lower()} and don the {itemformated}.')
        if itemType == 'healing':
            self.Text(
                f'You use the {item} and restore {self.items[item]["modifier"]} hit points.')
            player.HealFunction(self.items[item]["modifier"])
            player.inventory.remove(item)
        if self.battleOn == True:
            self.EnemyAction()

    # Shop Functions ######
    def OpenShopBuy(self):
        self.shopOpen = True
        self.shopOp = 1
        self.mainTextBox.clear()
        self.ButtonV.setText("Close")
        thisShop = self.locations[self.playerLocation + ' ' + "Shop"]
        buttonList = ['Q', 'W', 'E', 'A',
                      'S', 'D', 'Z', 'X', 'C']
        for x in buttonList:
            buttontoupdate = 'self.Button' + \
                x+f'.setText("")'
            eval(buttontoupdate)
        x = 0
        for i in thisShop:
            buttontoupdate = 'self.Button' + \
                buttonList[x]+f'.setText("{i}")'
            eval(buttontoupdate)
            if self.items[i]['type'] == 'weapon':
                itemType = 'Damage:'
            elif self.items[i]['type'] == 'armor':
                itemType = 'Armor:'
            elif self.items[i]['type'] == 'item' or self.items[i]['type'] == 'healing':
                itemType = self.items[i]['use']
            elif self.items[i]['type'] == 'misc item':
                itemType = 'Misc Item'
            self.Text(
                f"{self.items[i]['description']} - {itemType} {self.items[i]['modifier']} - Cost: {self.items[i]['value']} gold")
            x += 1
        self.ButtonEnabled()
        pass

    def BuyItem(self, item):
        value = self.items[item]["value"]
        if player.gold < value:
            self.Text(f"You do not have enough gold to buy the {item}!")
        else:
            self.Text(f"You buy the {item}.")
            player.gold -= value
            player.inventory.append(item)
        self.UpdateInformation()

    def OpenShopSell(self):
        self.shopOpen = True
        self.shopOp = 2
        self.SetUpInventory()

    def SellItem(self, item):
        value = self.items[item]["value"]
        self.Text(f"You sell the {item} and get {value} gold in return.")
        player.inventory.remove(item)
        player.gold += value
        self.UpdateInformation()
        self.SetUpInventory()

    # Action Functions ##########
    def LevelUpFunction(self):
        self.levelUp = True
        buttonList = ['Q', 'W', 'E', 'A', 'R',
                      'S', 'D', 'Z', 'X', 'C']
        for x in buttonList:
            buttontoupdate = 'self.Button' + \
                x+f'.setText("")'
            eval(buttontoupdate)
        self.ButtonQ.setText("Strength")
        self.ButtonW.setText("Dexterity")
        self.ButtonE.setText("Constitution")
        self.ButtonA.setText("Arcana")
        self.ButtonS.setText("Charisma")
        self.ButtonEnabled()

    def PointAdd(self, stat):
        if stat == 'Strength':
            player.strength += 1
        elif stat == 'Dexterity':
            player.dexterity += 1
        elif stat == 'Constitution':
            player.consitution += 1
        elif stat == 'Arcana':
            player.arcana += 1
        elif stat == 'Charisma':
            player.charisma += 1
        player.points -= 1
        if player.points == 0:
            self.levelUp = False
            self.ButtonUpdate()

    def QuestFinished(self, gold=0, item='none'):
        text = ''
        if item != 'none':
            text += f'You place the {item} in your bag.'
            player.inventory.append(item)
        if gold > 0:
            text += f'You put the {gold} gold in your pouch.'
        self.Text(f'{text}')

    def TalkFunction(self):  # function to talk to npcs, using flags and the dialogue.json
        pL = self.playerLocation
        count = 0
        compiledList = set(player.inventory)
        numberedList = [''] * len(compiledList)
        for i in compiledList:
            numberedList[count] = [i, player.inventory.count(i)]
            count += 1
        if pL == 'Merchant':
            ratTails = [t for t in numberedList if 'Rat Tail' in t]
            greenCrystal = [c for c in numberedList if 'Green Crystal' in c]
            if self.flags[0][1] == 0:
                self.Text(self.dialogue[pL]['quest1'])
                self.flags[0][1] = 1
            elif self.flags[0][1] == 1:
                self.Text(self.dialogue[pL]['quest2'])
            elif self.flags[0][1] == 1 and ratTails[0][1] == 5 == greenCrystal[0][1]:
                self.Text(
                    f'Thank you {player.name}. Here is some gold for your trouble.')
                self.Text(self.dialogue[pL]['lead'])
                self.flags[2][1] = 1
                self.QuestFinished(15)
                for i in range(5):
                    player.inventory.remove('Rat Tail')
                    player.inventory.remove('Green Crystal')
                self.flags[0][1] = 2
            else:
                self.Text(self.locations[pL]['talk'] +
                          f"{player.name}. How can I help you?")
        if pL == 'Blacksmith':
            if self.flags[1][1] == 0:
                self.Text(
                    f"Ah, {player.name}. Good of you to drop by, heard you were going out to make a name for youself!")
                self.Text(self.dialogue[pL]["intro1"])
                self.QuestFinished(0, "Club")
                self.Text(self.dialogue[pL]["intro2"])
                self.flags[1][1] = 1
            else:
                self.Text(f"G'day {player.name}.")
        if pL == 'Guardhouse':
            if self.flags[2][1] == 1:
                self.Text(f"{player.name}, glad you're here.")
                self.Text(self.dialogue[pL]["quest1"])
                self.flags[2][1] = 2
            elif self.flags[2][1] == 2 and self.monsterKills[0][1] == 10:
                self.Text(
                    f"You've done a good service {player.name}, you've made this town a safer place. Here, your payment.")
                self.QuestFinished(30)
                self.Text(self.dialogue[pL]["quest2"])
                self.flags[2][1] = 3
            elif self.flags[2][1] == 3:
                self.Text(self.dialogue[pL]["questDone"])
            else:
                self.Text(f"Hello, {player.name}")

    def RestFunction(self, type):  # passes time and heals hitpoints
        if type == 'Rest':
            self.Text(f'{self.locations[self.playerLocation]["rest"]}')
            healAmount = round(player.maxHP*0.2)
            player.HealFunction(healAmount)
            self.TimeFunction(60)
        elif type == 'Sleep':
            self.Text(f'{self.locations[self.playerLocation]["sleep"]}')
            healAmount = round(player.maxHP)
            player.HealFunction(healAmount)
            self.TimeFunction(600)
        self.UpdateInformation()

    # Time Functions ##########

    # Used to get month, current day of the month, and the prefex of the day for the UI
    def FormatDate(self):
        if self.day > 30:
            today = self.day % 30
            month = self.monthNames[(self.day//30)-1]
        if today == 1:
            add = 'st'
        elif today == 2:
            add = 'nd'
        elif today == 3:
            add = 'rd'
        else:
            add = 'th'
        return f"{today}{add} of the {month}, Year: {self.year}"

    def FormatTime(self):  # Used to get the day name, and current time properly formatted for the UI
        if self.day > 5:
            day = self.day % 5
        hour = self.time // 60
        minute = self.time % 60
        return f"{self.dayNames[day-1]} - {hour}:{minute:02d}"

    # Will take added minutes, add to time and change the day and/or year accordingly
    def TimeFunction(self, minutes):
        self.time += minutes
        while self.time >= 1440:
            self.time -= 1440
            self.day += 1
        while self.day > 360:
            self.day -= 360
            self.year += 1
        if self.battleOn != True and self.overWorld != True:
            if self.time < 360 or self.time > 1140:
                self.night = True
                self.ButtonUpdate()
            else:
                self.night = False
                self.ButtonUpdate()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm(CreationWindow)
    the_form.show()
    sys.exit(app.exec_())
