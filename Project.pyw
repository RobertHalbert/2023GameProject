import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt5.QtCore import pyqtSignal, Qt
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

class Attack:
    attackdamage = 0
    def AttackFunction(self):
        pass

class Armor:
    def __init__(self,aname,defence):
        self.aname = aname
        self.defence = defence

class MonsterCharacter(Character,Armor,Weapon,Attack):
    def __init__(self, name, hp, stamina,wname,damage,aname,defence):
        super().__init__(name, hp, stamina,wname,damage,aname,defence)

class PlayerCharacter(Character,Armor,Weapon,Attack):
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

class Inventory:
    openInventory = False
    openStore = False
    gold = 20
    inventoryLimit = 9
    currentInventory = ['"cloth"','"stick"']
    equipment = ['','','','']
    eDictionary= {
        # ITEM : ['Description',Variable,Application,Type,Value]
        # Equipment
        'cloth':['A set of cloth clothes.', 0,'defence:','a',2],
        'stick':['A plain old stick.',1,'attack:','w',1],
        'dagger':['A simple iron dagger.',2,'attack:','w',10],
        # Raw 
        'apple':['a red apple','','','i',2],
        'wheat':['a buchel of golden wheat','','','i',12],
        'meat': ['some cow meat','','','i',5],
        'iron ingot': ['an ingot of iron','','','i',15],
        'fabric':['some fabric for crafting','','','i',14],
        'component':['a magical material','','','i',18],
        # Potions
        'potion':['a mysterious red liquid','','','i',22],
        # Arrow
        'arrow':['a simple wooden arrow','','','i',2],
        # Spells
        'magic spell':['a magic spell','','','i',30]
    }
    def EquipFunction(item):
        I = Inventory
        print (item)
        try:
            if I.eDictionary[item][3] == 'a':
                text = f'You don the {item}'
                I.equipment[0] = item
                return text
            if I.eDictionary[item][3] == 'w':
                text = f'You equip the {item}'
                I.equipment[1] = item
                return text
            if I.eDictionary[item][3] == 'r':
                text = f'You put the {item} on your finger'
                I.equipment[2] = item
                return text
            if I.eDictionary[item][3] == 'n':
                text = f'You wear the {item} around your neck'
                I.equipment[3] = item
                return text
        except:
            pass
    
class Flags:
    gameStart = 0
    startingVillageFirstVisit = 0

class Time:
    daynames = {0:'Starday',1:'Secday',2:'Midday',3:'Urthday',4:'Endsday'}
    currentDayName = ''
    minute = 0
    hour = 10
    day = 1
    month = 6
    year = 1352
    def SetTime(time):
        """Imput number of minutes to adavance time"""
        Time.minute += time
        while Time.minute >= 60:
            Time.minute -= 60
            Time.hour +=1
        while Time.hour >= 24:
            Time.hour -= 23
            Time.day += 1
        while Time.day > 30:
            Time.day -= 30
            Time.month += 1
        while Time.month > 12:
            Time.month -= 12
            Time.year += 1                
    def SetDateName():
        "This function applies a the name of day"
        dateNum = Time.day
        while dateNum > 5:
            dateNum -= 5
        Time.currentDayName = Time.daynames[dateNum-1]       

class Locations:
    currentLocation = ''
    overworld = False
    villageHome = 'Home'
    startingVillage = 'Eris'
    overworldPlaceholder = 'World'
    sVillageBlacksmith = 'Blacksmiths'
    sVillageMerchant = 'Merchants'
    sVillageMagician = 'Magicians'
    sVillageFarmer = 'Farmers'
    ########## World Size is 500,500
    currentCoord = [11,7]
    startingVCoord = [11,7]

class Dialogue:
    text = ''
    def Home(var):
        if var == 'start':
            text = "Game Started\n" + "Your Home"
        else: text = "Your Home" 
        return text
        
    def Eris(var):
        if Flags.startingVillageFirstVisit == 0:
            text = "Introduction\n" + "Village"
            Flags.startingVillageFirstVisit = 1
        else: text = "Village"
        return text
    def Merchants(var):
        if var == 'enter':
           text = 'Merhcants place'
        elif var == 'Talk':
            text = 'Hi'
        elif var == 'Buy Items':
            text = 'Tools'
        else: text =''
        return text
    def Blacksmiths(var):
        if var == 'enter':
            text = 'Blacksmiths place'
        elif var == 'Talk':
            text = 'Hey'
        elif var == 'Buy Items':
            text = 'Weapons'
        else: text =''
        return text
    def Magicians(var):
        if var == 'enter':
            text = 'Magicians place'
        elif var == 'Talk':
            text = 'Hello'
        elif var == 'Buy Items':
            text = 'Magic'
        else: text =''
        return text
    def Farmers(var):
        if var == 'enter':
            text = 'Farmers place'
        elif var == 'Talk':
            text = 'Sup?'
        elif var == 'Buy Items':
            text = 'Foodstuffs'
        else: text =''
        return text

class NonPlayerCharacters:
    pass

class NpcShops:
    shopsDictionary = {
        'Farmers':['"apple"','"wheat"','"meat"'],
        'Blacksmiths':['"iron ingot"','"dagger"','"arrow"'],
        'Merchants' : ['"potion"','"fabric"'],
        'Magicians' : ['"magic spell"','"component"']
    }

# Character Creation Window
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

# Main Game Window
class MyForm(Ui_Game.Ui_MainWindow, QMainWindow):

    def __init__(self, CCreate):
        super(MyForm, self).__init__()
        self.setupUi(self)
        self.CCreate = CCreate
        self.actionNew_Game.triggered.connect(self.StartGame)
        self.Text = self.mainTextBox.appendPlainText
        self.ButtonA.clicked.connect(lambda:self.GridButtonPressed('A'))
        self.ButtonC.clicked.connect(lambda:self.GridButtonPressed('C'))
        self.ButtonD.clicked.connect(lambda:self.GridButtonPressed('D'))
        self.ButtonE.clicked.connect(lambda:self.GridButtonPressed('E'))
        self.ButtonF.clicked.connect(lambda:self.GridButtonPressed('F'))
        self.ButtonQ.clicked.connect(lambda:self.GridButtonPressed('Q'))
        self.ButtonR.clicked.connect(lambda:self.GridButtonPressed('R'))
        self.ButtonS.clicked.connect(lambda:self.GridButtonPressed('S'))
        self.ButtonV.clicked.connect(lambda:self.GridButtonPressed('V'))
        self.ButtonW.clicked.connect(lambda:self.GridButtonPressed('W'))
        self.ButtonZ.clicked.connect(lambda:self.GridButtonPressed('Z'))
        self.frameButtons.setVisible(False)
        self.frameInfo.setVisible(False)
        self.ButtonZ.setText('Inventory')
        self.mainTextBox.appendPlainText("Welcome to (My Game)!\n\nStart a new game by selecting 'New game' in the Menu or by pressing 'F3'.")
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q: self.GridButtonPressed('Q')
        if event.key() == Qt.Key_W: self.GridButtonPressed('W')
        if event.key() == Qt.Key_E: self.GridButtonPressed('E')
        if event.key() == Qt.Key_R: self.GridButtonPressed('R')
        if event.key() == Qt.Key_A: self.GridButtonPressed('A')
        if event.key() == Qt.Key_S: self.GridButtonPressed('S')
        if event.key() == Qt.Key_D: self.GridButtonPressed('D')
        if event.key() == Qt.Key_F: self.GridButtonPressed('F')
        if event.key() == Qt.Key_Z: self.GridButtonPressed('Z')
        if event.key() == Qt.Key_X: self.GridButtonPressed('X')
        if event.key() == Qt.Key_C: self.GridButtonPressed('C')
        if event.key() == Qt.Key_V: self.GridButtonPressed('V')
        if event.key() == Qt.Key_F3: self.StartGame()
        if event.key() == Qt.Key_F4: self.EndGame()

#Main Functions
    def GridButtonPressed(self,button):
        buttonpressed = 'self.Button' + button +'Pressed()'
        eval(buttonpressed)
        if (Inventory.openInventory == False) and (Inventory.openStore == False):
            self.ButtonUpdate()

    def StartGame(self):
        self.frameWindow.setEnabled(False)
        self.mainTextBox.clear()
        self.CharacterCreation()

    def GameSetup(self):
        self.frameWindow.setEnabled(True)
        self.frameButtons.setVisible(True)
        self.frameInfo.setVisible(True)
        self.UpdateInformation()
        self.LocationUpdate('villageHome','start')
        self.ButtonUpdate()
        self.SetTime(0)

    def ExploreFunction(self, location):
        self.SetTime(60)
        self.Text("You explore a bit")

    def RoomChangeFunction(self,location,target,var):
        self.EnterRoom(location,target)
        self.DialogueFunction(target,var)

    def EncounterFunction(self):
        pass

    def OverworldMovementFunction(self):
        pass

    def SetTime(self,time):
        Time.SetTime(time)
        Time.SetDateName()
        self.UpdateDateTime()

    def EndGame(self):
        QMainWindow.close(self)

##### Helper Functions #####

    ##### BUTTONS ######
    def ButtonUpdate(self):
        locale = [Locations.currentLocation,Locations.overworld,Locations.currentCoord]
        buttonList = ['Q','W','E','R','A','S','D','F','Z','X','C','V']
        for x in range(len(buttonList)):
            buttontoupdate = 'self.Update'+buttonList[x]+f'Button({locale})'
            eval(buttontoupdate)
            buttonText = eval('self.Button'+buttonList[x]+".text()")
            if buttonText == '':
                eval('self.Button'+buttonList[x]+'.setEnabled(False)')
            else:
                eval('self.Button'+buttonList[x]+'.setEnabled(True)')


    ##### Button Updates #####
    
    def UpdateQButton(self,locale):
        b = self.ButtonQ
        L = Locations
        A = locale[0]
        if A == 'Home':
            b.setText('Rest')
        if A == 'Eris':
            b.setText('Explore')
        if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians':
            b.setText('Talk')

    def UpdateWButton(self,locale):
        b = self.ButtonW
        L = Locations
        A = locale[0]
        if A == 'Home':
            b.setText('')
        if A == 'Eris':
            b.setText('Merchant')
        if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians':
            b.setText('Buy Items')


    def UpdateEButton(self,locale):
        b = self.ButtonE
        L = Locations
        A = locale[0]
        if A == 'Home':
            b.setText('')
        if A == 'Eris':
            b.setText('Blacksmith')
        if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians':
            b.setText('Sell Items')

    def UpdateRButton(self,locale):
        b = self.ButtonR
        L = Locations
        A = locale[0]
        if A == 'Home':
            b.setText('')
        if A == 'Eris':
            b.setText('Magician')
        if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians':
            b.setText('')

    def UpdateAButton(self,locale):
        b = self.ButtonA
        L = Locations
        A = locale[0]
        if A == 'Home':
            b.setText('')
        if A == 'Eris':
            b.setText('Home')
        if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians':
            b.setText('')
        

    def UpdateSButton(self,locale):
        b = self.ButtonS
        L = Locations
        A = locale[0]
        if A == 'Home':
            b.setText('')
        if A == 'Eris':
            b.setText('Farmer')
        if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians':
            b.setText('')

    def UpdateDButton(self,locale):
        b = self.ButtonD
        L = Locations
        A = locale[0]
        if A == 'Home':
            b.setText('')
        if A == 'Eris':
            b.setText('')
        if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians':
            b.setText('')

    def UpdateFButton(self,locale):
        b = self.ButtonF
        L = Locations
        A = locale[0]
        if A == 'Home':
            b.setText('')
        if A == 'Eris':
            b.setText('')
        if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians':
            b.setText('')

    def UpdateZButton(self,locale):
        b = self.ButtonZ
        I = Inventory
        if I.openInventory == False or I.openStore == False:
            b.setText('Inventory')

    def UpdateXButton(self,locale):
        b = self.ButtonX
        L = Locations
        A = locale[0]
        if A == 'Home':
            b.setText('')
        if A == 'Eris':
            b.setText('')
        if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians':
            b.setText('')

    def UpdateCButton(self,locale):
        b = self.ButtonC
        L = Locations
        A = locale[0]
        if A == 'Home':
            b.setText('')
        if A == 'Eris':
            b.setText('')
        if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians':
            b.setText('')

    def UpdateVButton(self,locale):
        b = self.ButtonV
        L = Locations
        A = locale[0]
        if A == 'Home' or A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians':
            b.setText('Leave')  
        if A == 'Eris':
            b.setText('')
    
    
    ##### Button Pressed #####
     
    def ButtonQPressed(self):
        b = self.ButtonQ.text()
        L = Locations
        c = Locations.currentLocation
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if b == 'Rest':
            self.RestFunction()
        if b == 'Explore':
            if Locations.overworld == False:
                self.ExploreFunction(c)
        if b == 'Talk':
            self.DialogueFunction(c,'Talk')
    
    def ButtonWPressed(self):
        b = self.ButtonW.text()
        L = Locations
        c = Locations.currentLocation
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if b == 'Merchant':
            self.RoomChangeFunction(c,L.sVillageMerchant,'enter')
        if b == 'Buy Items':
            self.ShopFunction()
            self.ShopText()
    
    def ButtonEPressed(self):
        b = self.ButtonE.text()
        L = Locations
        c = Locations.currentLocation
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if b == 'Blacksmith':
            self.RoomChangeFunction(c,L.sVillageBlacksmith,'enter')
            
    def ButtonRPressed(self):
        b = self.ButtonR.text()
        L = Locations
        c = Locations.currentLocation
        if b == 'Magician':
            self.RoomChangeFunction(c,L.sVillageMagician,'enter')
    
    def ButtonAPressed(self):
        b = self.ButtonA.text()
        L = Locations
        c = Locations.currentLocation
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if b == 'Home':
            self.RoomChangeFunction(c,Locations.villageHome,'')
    
    def ButtonSPressed(self):
        b = self.ButtonS.text()
        L = Locations
        c = Locations.currentLocation
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if b == 'Farmer':
            self.RoomChangeFunction(c,Locations.sVillageFarmer,'enter')
    
    def ButtonDPressed(self):
        b = self.ButtonD.text()
        L = Locations
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
    
    def ButtonFPressed(self):
        b = self.ButtonF.text()
        L = Locations
    
    def ButtonZPressed(self):
        b = self.ButtonZ.text()
        L = Locations
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if Inventory.openInventory == False:
            Inventory.openInventory = True
            self.OpenInventory()
            self.InventoryText()
    def ButtonXPressed(self):
        b = self.ButtonX.text()
        L = Locations
        if Inventory.openInventory == True:
            self.InventoryFunction(b)

    def ButtonCPressed(self):
        b = self.ButtonC.text()
        L = Locations
        if Inventory.openInventory == True:
            self.InventoryFunction(b)

    def ButtonVPressed(self):
        b = self.ButtonV.text()
        c = Locations.currentLocation
        L = Locations
        if b == 'Leave':
            self.LeaveFunction(c,None)

##### ACTION FUNCTIONS (called by player action)#####
    def ShopFunction(self):
        shopItems = NpcShops.shopsDictionary[Locations.currentLocation]
        b = 'self.Button'
        buttonList = ['Q','W','E','A','S','D','Z','X','C']
        t = '.setText'
        self.ButtonV.setText('Leave'),self.ButtonV.setEnabled(True)
        Inventory.openStore = True
        self.ButtonZ.setText('')
        if len(shopItems) < 10:
            self.ButtonR.setText(''),self.ButtonR.setEnabled(False)
            self.ButtonF.setText(''),self.ButtonR.setEnabled(False)
        for i in buttonList:
            eval(b+i+t+'("""""")')
            eval(b+i+'.setEnabled(False)')
        for i in range(len(shopItems)):
            item = shopItems[i]
            eval(b+buttonList[i]+t+f'({item})')
        for i in range(len(shopItems)):
            buttonText = eval(b + buttonList[i] +".text()")
            if buttonText == '':
                eval('self.Button'+buttonList[i]+'.setEnabled(False)')
            else:
                eval('self.Button'+buttonList[i]+'.setEnabled(True)')
     
    def ShopText(self):
        buttonList = ['Q','W','E','A','S','D','Z','X','C']
        self.mainTextBox.clear()
        b = 'self.Button'
        t = '.text()'
        I = Inventory
        self.Text('-------------------------------------------------------------------------------')
        for x in range(len(NpcShops.shopsDictionary[Locations.currentLocation])):
            itemT = eval(b+buttonList[x]+t)
            self.Text(f'{itemT}\t\t{I.eDictionary[itemT][0]}\t\t{I.eDictionary[itemT][2]} {I.eDictionary[itemT][1]}')

    def InventoryFunction(self,item):
        if Inventory.openInventory == True:
            Inventory.EquipFunction(item)

    def InventoryText(self):
        buttonList = ['Q','W','E','A','S','D','Z','X','C']
        self.mainTextBox.clear()
        b = 'self.Button'
        t = '.text()'
        I = Inventory
        self.Text('-------------------------------------------------------------------------------')
        for x in range(len(Inventory.currentInventory)):
            itemT = eval(b+buttonList[x]+t)
            self.Text(f'{itemT}\t{I.eDictionary[itemT][0]}\t\t{I.eDictionary[itemT][2]} {I.eDictionary[itemT][1]}')

    def OpenInventory(self):
        I = Inventory
        b = 'self.Button'
        buttonList = ['Q','W','E','A','S','D','Z','X','C']
        t = '.setText'
        self.ButtonV.setText('Leave'),self.ButtonV.setEnabled(True)
        I.openInventory = True
        self.ButtonZ.setText('')
        if len(I.currentInventory) < 10:
            self.ButtonR.setText(''),self.ButtonR.setEnabled(False)
            self.ButtonF.setText(''),self.ButtonR.setEnabled(False)
        for i in buttonList:
            eval(b+i+t+'("""""")')
            eval(b+i+'.setEnabled(False)')
        for i in range(len(I.currentInventory)):
            item = I.currentInventory[i]
            eval(b+buttonList[i]+t+f'({item})')
        for i in range(len(I.currentInventory)):
            buttonText = eval(b + buttonList[i] +".text()")
            if buttonText == '':
                eval('self.Button'+buttonList[i]+'.setEnabled(False)')
            else:
                eval('self.Button'+buttonList[i]+'.setEnabled(True)')


    def RestFunction(self):
        self.SetTime(180)
        self.Text("Rest for 3 hours.")

    def LeaveFunction(self,location,var):
        L = Locations
        A = location
        if Inventory.openInventory == True or Inventory.openStore == True:
            Inventory.openInventory = False
            Inventory.openStore = False
            self.mainTextBox.clear()
            self.DialogueFunction(Locations.currentLocation,'enter')
        
        else:
            if A == 'Home' or A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians':
                L.currentLocation = L.startingVillage
            self.DialogueFunction(L.currentLocation,var)
            self.SetTime(5)
            self.labelLocation.setText(Locations.currentLocation)

    def EnterRoom(self,location,target):
        if location == Locations.startingVillage:
            Locations.currentLocation = target   
        self.SetTime(5)     
        self.labelLocation.setText(Locations.currentLocation)

##### OHER HELPER FUNCTIONS #####
    def UpdateDateTime(self):
        T = Time
        mi = T.minute
        h = T.hour
        d = T.day
        mo = T.month
        dn = T.currentDayName
        self.labelTime.setText(f"Time: {h}:{mi:02}")
        self.labelDate.setText(f"Date: {dn}\t{d}/{mo:0>2d}")

    def LocationUpdate(self,location,var):
        locale = getattr(Locations,location)
        Locations.currentLocation = locale
        self.labelLocation.setText(Locations.currentLocation)
        self.DialogueFunction(Locations.currentLocation,var)

    def UpdateInformation(self):
        self.labelName.setText(PlayerCharacter.name)
        self.labelGold.setText(f"Gold: {str(Inventory.gold)}")

    def DialogueFunction(self,target,var):
        """Function to call text for given event. (target of function,variable)"""
        Dialogue.text = ''
        v = f"('{var}')"
        d = "Dialogue."
        text = eval(d+target+v)
        self.Text(text)

    def CharacterCreation(self):
        self.CCreate = CreationWindow()
        self.CCreate.signal_function.connect(self.GameSetup)
        self.CCreate.show()
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm(CreationWindow)
    the_form.show()
    sys.exit(app.exec_())