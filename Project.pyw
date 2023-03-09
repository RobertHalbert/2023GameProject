import sys, random

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt5.QtCore import pyqtSignal, Qt
import Ui_Game, Ui_CCWindow

class Skills:
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

class MonsterCharacter():
    # [name,currenthp,maxhp,weaponname,damage,armor/fur/clothes/etc.,defense,xpvalue,level]
    monster = ''
    rat = ['rat',5,5,'claws',1,'fur',0,1,1]
    slime = ['slime',8,8,'slime',1,'slime',0,3,1]
    crab = ['crab', 10,10,'pincers',3,'shell',1,5,2]
    hawk = ['hawk',12,12,'talons',5,'feathers',1,8,3]
    thief = ['thief',15,15,'dagger',8,'leather',4,12,5]

class PlayerCharacter():
    hp = 0
    name = ''
    level = 1
    strength = 1
    dexterity = 1
    arcane = 1
    constitution = 1
    charisma = 1
    apperenceList = ['','','','','']
    currentHP = 1
    currentXp = 0
    xpNeeded = 999999
    slots = 1
    slotsleft = 1
    harvests = 1
    harvestsLeft = 1
    def HealFunction(ammount):
        PlayerCharacter.currentHP += ammount
        if PlayerCharacter.currentHP > PlayerCharacter.hp:
            PlayerCharacter.currentHP = PlayerCharacter.hp
    
class Inventory:
    openCrafting = False
    openInventory = False
    openStore = False
    openSell = False
    gold = 20
    inventoryLimit = 9
    currentInventory = ['cloth','club','apple','apple','apple','apple','apple','apple','mushroom','mushroom','mushroom','mushroom','mushroom','mushroom']
    equipment = ['cloth','hands','','']
    eDictionary= {
        # ITEM : ['Description',Variable,Application,Type,Value, max allowed]
        'hands':['hands',0,''],
        # Equipment
        'cloth':['A set of cloth clothes.', 0,'defence:','a',2,1],
        'club':['A plain old club.',1,'attack:','w',1,1],
        'dagger':['An iron dagger.',2,'attack:','w',10,1],
        # Raw 
        'apple':['a red apple','','','i',2,10],
        'wheat':['a buchel of golden wheat','','','i',12,10],
        'mushroom': ['a edible mushroom','','','i',1,10],
        'meat': ['some animal meat','','','i',5,10],
        'iron ingot': ['an ingot of iron','','','i',15,5],
        'fabric':['some fabric for crafting','','','i',14,5],
        'component':['a magical material','','','i',18,5],
        'shell':['a small shell','','','i',1,10],
        'small herb': ['a small herb','','','i',1,10],
        'fish': ['a small fish','','','i',1,10],
        # Potions
        'potion':['a mysterious red liquid','','','i',22,5],
        'elixir':['a mysterious blue liquid','','','i',22,5],
        # Arrow
        'arrow':['a wooden arrow','','','i',2,0,20],
        # Spells
        'magic spell':['a magic spell','','','i',30,1],
        # Upgrades
        'Backpack':['A bag for carrying','','','u',100,1]
    }
    def EquipFunction(item):
        I = Inventory
        try:
            for x in range(len(I.equipment)):
                if item in I.equipment[x]:
                    I.equipment[x] = ''
                    text = f'You remove the {item}'
                    if I.equipment[1] == '':
                        I.equipment[1] = 'hands'
            if I.eDictionary[item][3] == 'a':
                text = f'You don the {item}'
                I.equipment[0] = item
            if I.eDictionary[item][3] == 'w':
                text = f'You equip the {item}'
                I.equipment[1] = item
            if I.eDictionary[item][3] == 'r':
                text = f'You put the {item} on your finger'
                I.equipment[2] = item
            if I.eDictionary[item][3] == 'n':
                text = f'You wear the {item} around your neck'
                I.equipment[3] = item
            if I.eDictionary[item][3] == 'i':
                if item == 'apple':
                    text = f'You eat the {item}.'
                    I.currentInventory.remove(item)
                if item == 'potion':
                    text = 'You drink the potion. You feel better!'
                    PlayerCharacter.HealFunction(5)
                    I.currentInventory.remove(item)     
                if item == 'elixir':
                    text = 'You drink the potion. You feel energized!'
                    PlayerCharacter.slotsleft = PlayerCharacter.slots
                    PlayerCharacter.harvestsLeft = PlayerCharacter.harvests       
        except:
            pass
        
        return text    
    def ItemFindFunction(location):
        I = Inventory
        text = ''
        if location == 'Forest':
            text = 'You found a mushroom.'
            if len(set(I.currentInventory)) < I.inventoryLimit and I.currentInventory.count('mushroom') < 10:
                text = text + ' You place it in your bag.'
                I.currentInventory.append('mushroom')
            else:
                text = text + ' But there is no more space for mushrooms.'
        if location == 'Cliffside Farms':
            text = 'You found an apple.'
            if len(set(I.currentInventory)) < I.inventoryLimit and I.currentInventory.count('mushroom') < 10:
                text = text + ' You place it in your bag.'
                I.currentInventory.append('apple')
            else:
                text = text + ' But there is no more space for apples.'
        if location == 'Lighthouse Road' or location == 'Westcliff Road':
            text = 'You find a coin on the ground.'
            I.gold += 1
        if location == 'Cliffside Plains' or location == 'Westcliff Plains':
            text = 'You find a small herb.'
            if len(set(I.currentInventory)) < I.inventoryLimit and I.currentInventory.count('small herb') < 10:
                text = text + ' You place it in your bag.'
                I.currentInventory.append('small herb')
            else:
                text = text + ' But there is no more space for these herbs.'
        if location == 'Westcliff Beach' or location == 'Westcliff Shallows':
            text = 'You find a small shell.'
            if len(set(I.currentInventory)) < I.inventoryLimit and I.currentInventory.count('shell') < 10:
                text = text + ' You place it in your bag.'
                I.currentInventory.append('shell')
            else:
                text = text + ' But there is no more space for more shells.'
        if location == 'Ocean':
            text = 'You manage to hook a fish!'
            if len(set(I.currentInventory)) < I.inventoryLimit and I.currentInventory.count('fish') < 10:
                text = text + ' You place it in your bag.'
                I.currentInventory.append('fish')
            else:
                text = text + ' But there is no more space for more fish.'
        if location == 'Hunt':
            text = 'Your hunt was successful!'
            if len(set(I.currentInventory)) < I.inventoryLimit and I.currentInventory.count('meat') < 10:
                text = text + ' You place the meat in your bag.'
                I.currentInventory.append('meat')
            else:
                text = text + ' But there is no more space for more meat.'
        return text

class Flags:
    levelUp = False
    battle = False
    magicAvailable = False
    craftingAvailable = False
    gameStart = 0
    startingVillageFirstVisit = 0
    farmquest1 = 0
    magicQuest = 0
    merchantQuest = 0
    cityEntryQuest = 0

class QuestChecks:
    ratsKilled = 0
    slimesKilled = 0

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
    # area determines the curent region {0:westcliff,}
    area = 0
    overworld = False
    overworldPlaceholder = 'World'
    ########## Default World Size is 500,500
    currentCoord = [11,7]

class Dialogue:
    text = ''
    def Introduction(var):
        text = f""
    def Home(var):
        if var == 'start':
            text = "Game Started\n" + "Your Home"
        else: text = "Your Home" 
        return text
    def Westcliff(var):
        if Flags.startingVillageFirstVisit == 0:
            text = f'"Hey, {PlayerCharacter.name}! (Marchant) and (Farmer) are looking for you. Think they have a job for you to do."\n' + "Village"
            Flags.startingVillageFirstVisit = 1
        elif Locations.overworld == True:
            text = "Outside of Village"
        else: text = "Village"
        return text
    def Merchants(var):
        invCount = MyForm.InventoryCount(MyForm)
        apples = [s for s in invCount if 'apple' in s]
        mushroom = [s for s in invCount if 'mushroom' in s]
        if var == 'enter':
           text = 'Merhcants place'
        elif var == 'Talk':
            text = ''
            try:
                if Flags.merchantQuest == 1 and mushroom[0][1] >= 5 and apples[0][1] >= 5:
                    for i in range(5):
                        Inventory.currentInventory.remove('apple')
                        Inventory.currentInventory.remove('mushroom')
                        Flags.merchantQuest = 2
                        Flags.craftingAvailable = True
                        text = 'Thanks'
            except:
                text = 'Hi'
            if Flags.merchantQuest == 0:
                text = f'"Good to see you, {PlayerCharacter.name}.I have a job for you, I have been running low on some items and was hoping you would be willing to help me out. If you bring me 5 mushrooms and 5 apples, I can teach you how to make your own potions. You will find mushrooms a ways into the forest, you can get some apples from the farmer or pick them yourself on the west side of the farm."'
                Flags.merchantQuest = 1
        elif var == 'Buy Items':
            text = 'Tools'
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
            if Flags.magicQuest == 0 and PlayerCharacter.level == 2:
                text = '"The slimes in the forest are stargin to get out of hand, it is becoming dangerous for the townsfolk. If you can kill ten slimes, it will make the area a bit safer and I will even teach you some magic"'
                Flags.magicQuest = 1
            elif Flags.magicQuest == 0 and PlayerCharacter.level < 2:
                text = '"Hmm, I may have a job for you... Come back when your a bit stronger."'
            elif Flags.magicQuest == 2:
                text = f'"Good job {PlayerCharacter.name}. Here, let me each you some basic magic. If you do not neglect your studies, it can be quite powerful. But it is also draining, you will only be able to case it a few times before you need to rest."'
                Flags.magicAvailable = True
                Flags.magicQuest = 3
            else: text = 'Hello'
        elif var == 'Buy Items':
            text = 'Magic'
        else: text =''
        return text
    def Farmers(var):
        if var == 'enter':
            text = 'Farmers place'
        elif var == 'Talk':
            if Flags.farmquest1 == 0:
                text = f'"Hey, {PlayerCharacter.name}. There has been a lot of rats eating my crops as of late. If you could kill 5 of these rats, I would be grateful. You can find them any part of the farm, just north of the town."'
                Flags.farmquest1 = 1
            elif Flags.farmquest1 == 2:
                text = '"Thanks for killing those rats. Here, some gold for your work."\nYou gained 5 gold and 5 experience'
                Flags.farmquest1 = 3
            else: text = 'Sup?'
        elif var == 'Buy Items':
            text = 'Foodstuffs'
        else: text =''
        return text
    def Forest(var):
        if var == 'enter':
            text = 'Forest'
        else: text = ''
        return(text)
    def Tavern(var):
        if var == 'Enter':
            text = 'This place used to be bustling with ativity throught the day. But now it is empty almost every day.'
        else: text = ''
        return text
    def LighthouseRoad(var):
        text = 'Lighthouse Road'
        return text
    def Lighthouse(var):
        text = 'The old lighthouse. Hardly ever used anymore, since people hardly sail these days.'
        return text
    def CliffsidePlains(var):
        text = 'Cliffside Plains'
        return text
    def CliffsideFarms(var):
        text = 'Cliffside Farms'
        return text
    def WestcliffRoad(var):
        text = 'Westcliff Road'
        return text
    def WestcliffPlains(var):
        text = 'Westcliff Plains'
        return text
    def WestcliffShallows(var):
        text = 'Westcliff Shallows'
        return text    
    def WestcliffBeach(var):
        text = 'Westcliff Beach'
        return text
    def WestcliffDocks(var):
        text = 'Westcliff Docks'
        return text
    def NorthRoad(var):
        text = 'North Road'
        return text
    def DecoVineyard(var):
        text = 'Deco Vineyard'
        return text
    def VineyardBuilding(var):
        text = 'Vineyard Building'
        return text
    def CityGuard(var):
        if Flags.cityEntryQuest == 0:
            text = 'Halt, this city is locked down until further notice due to the attacks from the north\nIf you want to enter the city, help us in securing the areas north of the city.'
            Flags.cityEntryQuest = 1
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
        self.ButtonX.clicked.connect(lambda:self.GridButtonPressed('X'))
        self.ButtonZ.clicked.connect(lambda:self.GridButtonPressed('Z'))
        self.actionExit_Game.triggered.connect(self.EndGame)
        self.frameButtons.setVisible(False)
        self.frameInfo.setVisible(False)
        self.frameEnemyInfo.setVisible(False)
        self.labelSlots.setVisible(False)
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
        if event.key() == Qt.Key_F3 and self.actionNew_Game.isEnabled(): self.StartGame()
        if event.key() == Qt.Key_F4: self.EndGame()
        if event.key() == Qt.Key_F8: self.Debug()
        if event.key() == Qt.Key_F7: Flags.craftingAvailable = True

#Main Functions

    def Debug(self):
        PlayerCharacter.currentXp += 10
        self.UpdateInformation()
        self.ButtonUpdate()

    def GridButtonPressed(self,button):
        buttonpressed = 'self.Button' + button +'Pressed()'
        I = Inventory
        eval(buttonpressed)
        if (I.openInventory == False) and (I.openStore == False) and (I.openSell == False) and (I.openCrafting == False):
            self.ButtonUpdate()

    def StartGame(self):
        self.frameWindow.setEnabled(False)
        self.mainTextBox.clear()
        self.CharacterCreation()

    def GameSetup(self):
        self.setStats()
        self.frameWindow.setEnabled(True)
        self.frameButtons.setVisible(True)
        self.frameInfo.setVisible(True)
        self.UpdateInformation()
        self.LocationUpdate('Home','start')
        self.ButtonUpdate()
        self.SetTime(0)
        self.actionNew_Game.setEnabled(False)

    def ExploreFunction(self, location):
        self.SetTime(60)
        self.Text("You explore a bit")

    def RoomChangeFunction(self,location,target,var):
        self.EnterRoom(location,target)
        self.DialogueFunction(target,var)

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
            if buttonText == '' or (buttonText == 'Magic' and PlayerCharacter.slotsleft == 0):
                eval('self.Button'+buttonList[x]+'.setEnabled(False)')
            else:
                eval('self.Button'+buttonList[x]+'.setEnabled(True)')


    ##### Button Updates #####
    
    def UpdateQButton(self,locale):
        b = self.ButtonQ
        L = Locations
        A = locale[0]
        if Flags.battle == False:
            if L.overworld == False:
                if A == 'Home':
                    b.setText('Rest')
                if A == 'Westcliff':
                    b.setText('Explore')
                if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians' or A == 'Tavern':
                    b.setText('Talk')          
            else:
                b.setText('')
        if Flags.battle == True and Inventory.openInventory == False:
            b.setText('Attack')  
        if Flags.levelUp == True:
            b.setText('Strength')

    def UpdateWButton(self,locale):
        b = self.ButtonW
        L = Locations
        A = locale[0]
        Lc = L.currentCoord
        if Flags.battle == False:
            if L.overworld == False:
                if A == 'Home':
                    b.setText('')
                if A == 'Westcliff':
                    b.setText('Merchant')
                if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians':
                    b.setText('Buy Items')
                if A == 'Tavern':
                    b.setText('')
            elif L.overworld == True:
                if (Lc[0] >= 3  and Lc[0] <= 14) and Lc[1] == 11:
                    b.setText('')
                else:
                    b.setText('North')
        if Flags.battle == True and Inventory.openInventory == False:
            b.setText('Defend')
        if Flags.levelUp == True:
            b.setText('Dexterity')

    def UpdateEButton(self,locale):
        b = self.ButtonE
        L = Locations
        A = locale[0]
        if Flags.battle == False:
            if L.overworld == False:
                if A == 'Home':
                    b.setText('')
                if A == 'Westcliff':
                    b.setText('Blacksmith')
                if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians':
                    b.setText('Sell Items')
                if A == 'Tavern':
                    b.setText('')
            else:
                if (L.currentCoord[0] >= 5 and L.currentCoord[0]<=10) and (L.currentCoord[1]>=3 and L.currentCoord[1]<=4):
                    b.setText('Gather') #Mushrooms
                elif (L.currentCoord[0] >= 8 and L.currentCoord[0]<=9) and (L.currentCoord[1]>=8 and L.currentCoord[1]<=11):
                    b.setText('Gather') #Apples
                elif (L.currentCoord[0] >= 4 and L.currentCoord[0]<=6) and (L.currentCoord[1]>=9 and L.currentCoord[1]<=11):
                    b.setText('Gather') #Herbs
                elif (L.currentCoord[0] == 17) and (L.currentCoord[1]==6):
                    b.setText('Fish')
                elif (L.currentCoord[0] >= 17 and L.currentCoord[0]<=21) and (L.currentCoord[1]>=9 and L.currentCoord[1]<=11):
                    b.setText('Hunt')
                else:
                    b.setText('')
        if Flags.battle == True and Inventory.openInventory == False:
            b.setText('Run')
        if Flags.levelUp == True:
            b.setText('Arcane')

    def UpdateRButton(self,locale):
        b = self.ButtonR
        L = Locations
        A = locale[0]
        if Flags.battle == False:
            if L.overworld == False:
                if A == 'Home':
                    if Flags.craftingAvailable == True:
                        b.setText('Craft')
                    else:
                        b.setText('')   
                if A == 'Westcliff':
                    b.setText('Magician')
                if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians' or A == 'Tavern':
                    b.setText('')
            elif L.overworld == True:
                if A == 'Westcliff':
                    b.setText(f'{Locations.currentLocation}')
                elif Locations.currentCoord[0] == 24 and Locations.currentCoord[1] == 7:
                    b.setText('City Guard')
                else:
                    b.setText('')
        if Flags.battle == True and Inventory.openInventory == False:
            b.setText('Wait')
        if Flags.levelUp == True:
            b.setText('Constitution')

    def UpdateAButton(self,locale):
        b = self.ButtonA
        L = Locations
        A = locale[0]
        Lc = Locations.currentCoord
        x = Lc[0]
        y = Lc[1]
        if Flags.battle == False:
            if L.overworld == False:
                if A == 'Home':
                    b.setText('')
                if A == 'Westcliff':
                    b.setText('Home')
                if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians' or A == 'Tavern':
                    b.setText('')
            else:
                if (x == 3 and (y >=1 and y <=11)) or (x == 22 and y >=12) or (x == 28 and (y >= 1 and y <=8)):
                    b.setText('')
                else:
                    b.setText('West')
        if Flags.battle == True and Inventory.openInventory == False and Flags.magicAvailable == True:
            b.setText('Magic') #TEMP?
        if Flags.levelUp == True:
            b.setText('Charisma')

    def UpdateSButton(self,locale):
        b = self.ButtonS
        L = Locations
        A = locale[0]
        if Flags.battle == False:
            if L.overworld == False:
                if A == 'Home':
                    b.setText('')
                if A == 'Westcliff':
                    b.setText('Farmer')
                if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians' or A == 'Tavern':
                    b.setText('')
            else:
                b.setText('Explore')
        if (Flags.battle == True and Inventory.openInventory == False) or Flags.levelUp == True:
            b.setText('')

    def UpdateDButton(self,locale):
        b = self.ButtonD
        L = Locations
        Ll = L.currentCoord
        A = locale[0]
        x = Ll[0]
        y = Ll[1]
        if Flags.battle == False:
            if L.overworld == False:
                if A == 'Home':
                    b.setText('')
                if A == 'Westcliff':
                    b.setText('Tavern')
                if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians' or A == 'Tavern':
                    b.setText('')
            else:
                if (x == 24 and (y >= 1 and y <=8)):
                    b.setText('')
                else:
                    b.setText('East')
        if (Flags.battle == True and Inventory.openInventory == False) or Flags.levelUp == True:
            b.setText('')

    def UpdateFButton(self,locale):
        b = self.ButtonF
        L = Locations
        A = locale[0]
        if Flags.battle == False:
            if L.overworld == False:
                if A == 'Home':
                    b.setText('')
                if A == 'Westcliff':
                    b.setText('')
                if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians' or A == 'Tavern':
                    b.setText('')
            else:
                b.setText('')
        if Flags.battle == True and Inventory.openInventory == False:
            b.setText('')

    def UpdateZButton(self,locale):
        b = self.ButtonZ
        I = Inventory
        if I.openInventory == False or I.openStore == False:
            b.setText('Inventory')
        if Flags.levelUp == True:
            b.setText('')

    def UpdateXButton(self,locale):
        b = self.ButtonX
        L = Locations
        A = locale[0]
        Lc = L.currentCoord
        x = Lc[0]
        y = Lc[1]
        if Flags.battle == False:
            if L.overworld == False:
                if A == 'Home':
                    b.setText('')
                if A == 'Westcliff':
                    b.setText('')
                if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians' or A == 'Tavern':
                    b.setText('')
            if L.overworld == True:
                if ((x >= 3 and x <= 24) and y == 1) or ((x>=25 and x<=27) and y==9):
                    b.setText('')
                else:
                    b.setText('South')
        if (Flags.battle == True and Inventory.openInventory == False) or Flags.levelUp == True:
            b.setText('')

    def UpdateCButton(self,locale):
        b = self.ButtonC
        L = Locations
        A = locale[0]
        if Flags.battle == False:
            if L.overworld == False:
                if A == 'Home':
                    b.setText('')
                if A == 'Westcliff':
                    b.setText('')
                if A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians' or A == 'Tavern':
                    b.setText('')
            else:
                b.setText('')
        if (Flags.battle == True and Inventory.openInventory == False) or Flags.levelUp == True:
            b.setText('')

    def UpdateVButton(self,locale):
        b = self.ButtonV
        L = Locations
        A = locale[0]
        if Flags.battle == False:
            if L.overworld == True:
                b.setText('')
            else:
                b.setText('Leave')  
        if (Flags.battle == True and Inventory.openInventory == False) or Flags.levelUp == True:
            b.setText('')
    
    ##### Button Pressed #####
     
    def ButtonQPressed(self):
        b = self.ButtonQ.text()
        L = Locations
        c = Locations.currentLocation
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if Inventory.openSell == True:
            self.InventoryFunction(b)
        if Inventory.openStore == True:
            self.BuyItemFunction(b)
        if b == 'Rest':
            self.RestFunction()
        if b == 'Explore':
            if Locations.overworld == False:
                self.ExploreFunction(c)
        if b == 'Talk':
            self.DialogueFunction(c,'Talk')
        if b == 'Attack':
            self.BattleFunction('Attack')
        if b == 'Strength':
            self.StatIncrease(b)

    def ButtonWPressed(self):
        b = self.ButtonW.text()
        L = Locations
        c = Locations.currentLocation
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if Inventory.openSell == True:
            self.InventoryFunction(b)
        if Inventory.openStore == True:
            self.BuyItemFunction(b)
        if b == 'Merchant':
            self.RoomChangeFunction(c,'Merchants','enter')
        if b == 'Buy Items':
            self.ShopFunction()
            self.ShopText()
        if b == 'North':
            self.OverWorldMovement('w')
        if b == 'Defend':
            self.BattleFunction('Defend')
        if b == 'Dexterity':
            self.StatIncrease(b)

    def ButtonEPressed(self):
        b = self.ButtonE.text()
        L = Locations
        c = Locations.currentLocation
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if Inventory.openSell == True:
            self.InventoryFunction(b)
        if Inventory.openStore == True:
            self.BuyItemFunction(b)
        if b == 'Blacksmith':
            self.RoomChangeFunction(c,'Blacksmiths','enter')
        if b == 'Sell Items':
            self.SellItemsInventory()
        if b == 'Run':
            self.BattleFunction('Run')
        if b == 'Arcane':
            self.StatIncrease(b)
        if Inventory.openInventory == False and Inventory.openSell == False and Inventory.openStore == False:
            if b == 'Gather' or b == 'Hunt' or b == 'Fish':
                self.SkillUse(b)

    def ButtonRPressed(self):
        b = self.ButtonR.text()
        L = Locations
        c = Locations.currentLocation
        if b == 'Craft':
            Inventory.openCrafting = True
            self.CraftingFuction()
        if b == 'Magician':
            self.RoomChangeFunction(c,'Magicians','enter')
        if b == 'Westcliff' or b == 'Westcliff Docks' or b == 'Lighthouse':
            self.RoomChangeFunction(c,L.currentLocation,'enter')
        if b == 'Wait':
            self.BattleFunction('Wait')
        if b == 'Constitution':
            self.StatIncrease(b)
        if b == 'City Guard':
            Dialogue

    def ButtonAPressed(self):
        b = self.ButtonA.text()
        L = Locations
        c = Locations.currentLocation
        if b == 'Potion':
            self.MakePotion()
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if Inventory.openSell == True:
            self.InventoryFunction(b)
        if Inventory.openStore == True:
            self.BuyItemFunction(b)
        if b == 'Home':
            self.RoomChangeFunction(c,'Home','')
        if  b == 'West':
            self.OverWorldMovement('a')
        if b == 'Charisma':
            self.StatIncrease(b)
        if b == 'Magic': #TEMP?
            self.BattleFunction('Magic')
    
    def ButtonSPressed(self):
        b = self.ButtonS.text()
        L = Locations
        c = Locations.currentLocation
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if Inventory.openSell == True:
            self.InventoryFunction(b)
        if Inventory.openStore == True:
            self.BuyItemFunction(b)
        if b == 'Farmer':
            self.RoomChangeFunction(c,'Farmers','enter')
        if b == 'Explore':
            self.Text("You look around the area.")
            self.EncounterSystem(0.2)
        if b == 'Elixir':
            self.MakeElixir()
    
    def ButtonDPressed(self):
        b = self.ButtonD.text()
        L = Locations
        c = L.currentLocation
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if Inventory.openSell == True:
            self.InventoryFunction(b)
        if Inventory.openStore == True:
            self.BuyItemFunction(b)
        if b == 'Tavern':
            self.RoomChangeFunction(c,'Tavern','enter')
        if b == 'East':
            self.OverWorldMovement('d')
    
    def ButtonFPressed(self):
        b = self.ButtonF.text()
        L = Locations
    
    def ButtonZPressed(self):
        b = self.ButtonZ.text()
        L = Locations
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if Inventory.openSell == True:
            self.InventoryFunction(b)
        if Inventory.openStore == True:
            self.BuyItemFunction(b)
        if Inventory.openInventory == False:
            Inventory.openInventory = True
            self.OpenInventory()
            self.InventoryText()
        if Flags.battle == True:
            self.ButtonUpdate()

    def ButtonXPressed(self):
        b = self.ButtonX.text()
        L = Locations
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if Inventory.openSell == True:
            self.InventoryFunction(b)
        if Inventory.openStore == True:
            self.BuyItemFunction(b)
        if  b == 'South':
            self.OverWorldMovement('x')

    def ButtonCPressed(self):
        b = self.ButtonC.text()
        L = Locations
        if Inventory.openInventory == True:
            self.InventoryFunction(b)
        if Inventory.openSell == True:
            self.InventoryFunction(b)
        if Inventory.openStore == True:
            self.BuyItemFunction(b)

    def ButtonVPressed(self):
        b = self.ButtonV.text()
        c = Locations.currentLocation
        L = Locations
        if b == 'Leave':
            self.LeaveFunction(c,None)
            self.ButtonUpdate()

##### Other FUNCTIONS #####
    def RestFunction(self):
        self.SetTime(180)
        PlayerCharacter.currentHP = PlayerCharacter.hp
        self.Text("Rest for 3 hours.")
        PlayerCharacter.slotsleft = PlayerCharacter.slots
        PlayerCharacter.harvestsLeft = PlayerCharacter.harvests
        self.UpdateInformation()

    def LeaveFunction(self,location,var):
        I = Inventory
        L = Locations
        A = location
        if I.openInventory == True or I.openStore == True or I.openSell == True or I.openCrafting == True:
            Inventory.openInventory = False
            Inventory.openStore = False
            Inventory.openSell = False
            Inventory.openCrafting = False
            self.mainTextBox.clear()
            self.DialogueFunction(Locations.currentLocation,'enter')
        else:
            if A == 'Home' or A == 'Merchants' or A == 'Blacksmiths' or A == 'Farmers' or A == 'Magicians' or A == 'Tavern':
                L.currentLocation = 'Westcliff'
            if A == 'Westcliff' or A == 'Westcliff Docks' or A == 'Lighhouse':
                L.overworld = True
            self.DialogueFunction(L.currentLocation,var)
            self.SetTime(5)
            self.labelLocation.setText(Locations.currentLocation)

    def EnterRoom(self,location,target):
        if location == 'Westcliff' or location == 'Lighthouse' or location == 'Westcliff Docks':
            Locations.currentLocation = target
            Locations.overworld = False   
        self.SetTime(5)     
        self.labelLocation.setText(Locations.currentLocation)
    

### INVENTORY RELATED FUNCTIONS ###

    def BuyItemFunction(self,item):
        I = Inventory
        itemCost = I.eDictionary[item][4]
        if itemCost > I.gold:
            self.Text('You do not have enough gold!')
        else:
            self.Text(f'You bought a {item}')
            I.gold -= itemCost
            I.currentInventory.append(item)
            self.UpdateInformation()

    def InventoryCount(self):
        I = Inventory
        compInv = set(I.currentInventory)
        countInv = [''] * len(compInv)
        count = 0
        for i in compInv:
            countInv[count] = [i,I.currentInventory.count(i)]
            count += 1
        return countInv

    def InventoryFunction(self,item):
        item = item.translate({ord(i): None for i in 'x2345678910 '})
        if Inventory.openInventory == True:
            text = Inventory.EquipFunction(item)
            self.Text(text)
            self.OpenInventory()
        if Inventory.openSell == True:
            self.SellItemFunction(item)
        self.UpdateInformation()
        if Flags.battle == True:
            self.BattleFunction('')

    def InventoryText(self):
        self.mainTextBox.clear()
        I = Inventory
        self.Text('-------------------------------------------------------------------------------')
        compInv = set(I.currentInventory)
        countInv = self.InventoryCount()
        for x in range(len(compInv)):
            if countInv[x][1] == 1:
                self.Text(f'{countInv[x][0]}\t\t{I.eDictionary[countInv[x][0]][0]}\t\t{I.eDictionary[countInv[x][0]][2]} {I.eDictionary[countInv[x][0]][1]}')
            else:
                self.Text(f'{countInv[x][0]}\t\t{I.eDictionary[countInv[x][0]][0]}  x{countInv[x][1]}\t{I.eDictionary[countInv[x][0]][2]} {I.eDictionary[countInv[x][0]][1]}')

    def OpenInventory(self):
        I = Inventory
        b = 'self.Button'
        buttonList = ['Q','W','E','A','S','D','Z','X','C']
        t = '.setText'
        self.ButtonV.setText('Leave'),self.ButtonV.setEnabled(True)
        self.ButtonZ.setText('')
        invCount = self.InventoryCount()
        if len(I.currentInventory) < 10:
            self.ButtonR.setText(''),self.ButtonR.setEnabled(False)
            self.ButtonF.setText(''),self.ButtonR.setEnabled(False)
        for i in buttonList:
            eval(b+i+t+'("""""")')
            eval(b+i+'.setEnabled(False)')
        for i in range(len(invCount)):
            if invCount[i][1] == 1:
                eval(b+buttonList[i]+t+f'("{invCount[i][0]}")')
            elif invCount[i][1] > 1:
                eval(b+buttonList[i]+t+f'("{invCount[i][0]} x{invCount[i][1]}")')

        for i in range(len(set(I.currentInventory))):
            buttonText = eval(b + buttonList[i] +".text()")
            if buttonText == '':
                eval('self.Button'+buttonList[i]+'.setEnabled(False)')
            else:
                eval('self.Button'+buttonList[i]+'.setEnabled(True)')

    def SellItemFunction(self,item):
        I = Inventory
        for x in I.currentInventory:
            if item in I.equipment:
                self.Text('You cannot sell equipped items.')
                break
        else:
            self.Text(f"You sell the item for {I.eDictionary[item][4]} gold.")
            I.gold += I.eDictionary[f'{item}'][4]
            self.UpdateInformation()
            I.currentInventory.remove(item)
            self.OpenInventory()

    def SellItemsInventory(self):
        Inventory.openSell = True
        self.OpenInventory()

### ###

### CRAFTING FUNCTIONS ###

    def CraftingFuction(self):
        invCount = self.InventoryCount()
        apples = [s for s in invCount if 'apple' in s]
        mushroom = [s for s in invCount if 'mushroom' in s]
        herb = [s for s in invCount if 'herb' in s]
        meat = [s for s in invCount if 'meat' in s]
        I = Inventory
        b = 'self.Button'
        buttonList = ['Q','W','E','A','S','D','Z','X','C']
        t = '.setText'
        self.ButtonV.setText('Leave'),self.ButtonV.setEnabled(True)
        self.ButtonZ.setText('')
        self.ButtonR.setText('')
        for i in buttonList:
            eval(b+i+t+'("""""")')
            eval(b+i+'.setEnabled(False)')
        self.ButtonA.setText('Potion')
        self.Text('Potion:  Heals 5HP         Requires: 1 Apple, 1 Mushroom')
        if Skills.crafting >= 4:
            self.ButtonS.setText('Elixir')
            self.Text('Elixir:  Restores slots      Requires: 2 Meat, 2 Herb')
        try:
            if apples[0][1] > 0 and mushroom[0][1] > 0:
                self.ButtonA.setEnabled(True)
        except:
            pass
        try:
            if meat[0][1] > 0 and herb[0][1] > 0 and Skills.crafting >= 4:
                self.ButtonS.setEnabled(True)
        except:
            pass

    def MakePotion(self):
        Skills.crafting += 0.2
        self.Text('You make a potion')
        Inventory.currentInventory.remove('apple')
        Inventory.currentInventory.remove('mushroom')
        Inventory.currentInventory.append('potion')
        self.CraftingFuction()

    def MakeElixir(self):
        Skills.crafting += 0.2
        self.Text('You make an elixir')
        Inventory.currentInventory.remove('meat')
        Inventory.currentInventory.remove('meat')
        Inventory.currentInventory.remove('herb')
        Inventory.currentInventory.remove('herb')
        Inventory.currentInventory.append('elixir')
        self.CraftingFuction()

    def SkillUse(self,var):
        roll = random.randint(1,15)
        Time.SetTime(120)
        if var == 'Gather':
            if Skills.gathering > roll:
                self.Text(Inventory.ItemFindFunction(Locations.currentLocation))
                if Skills.gathering < 10:
                    Skills.gathering += 0.2
            else:
                self.Text("You try to find something of use, but find nothing.")
        if var == 'Fish':
            if Skills.fishing > roll:
                self.Text(Inventory.ItemFindFunction('Ocean'))
                if Skills.fishing < 10:
                    Skills.fishing += 0.2
            else:
                self.Text('You spend a few hours fishing, but nothing bites.')
        if var == 'Hunt':
            if Skills.hunting > roll:
                self.Text(Inventory.ItemFindFunction('Hunt'))
                if Skills.hunting < 10:
                    Skills.hunting += 0.2
            else:
                self.Text('You spend a few hours hunting, but find nothing.')
        self.UpdateDateTime()
            
    
### ###

### BATTLE RELATED FUNTIONS ###

    def BattleFunction(self,action):
        I = Inventory.equipment[1]
        W = Inventory.eDictionary[I]
      #  dexCheck = (PlayerCharacter.dexterity*(PlayerCharacter.level/MonsterCharacter.monster[8])) #DEBUG
        dexCheck = 3
        if action == 'Attack':
            strengthBonus = round(PlayerCharacter.strength/(PlayerCharacter.strength+W[1]))
            damage = strengthBonus + W[1]
            self.Text(f'You attack with your {I} dealing {damage} damage.')
            MonsterCharacter.monster[1] -= damage
        if action == 'Defend':
            self.Text('You defend')
        if action == 'Run':
            runChance = random.randint(1,100)
            if runChance < (50*(0.25 + dexCheck)-25):
                self.Text('You run away.')
                Flags.battle = False
                self.frameEnemyInfo.setVisible(False)
                return
            else:
                self.Text('You try to run, but are unable to get away.')
        if action == 'Wait':
            self.Text('You wait')
        if action == 'Magic':
            damage = PlayerCharacter.arcane + 1
            self.Text(f"You cast magic, dealing {damage} damage to the {MonsterCharacter.monster[0]}.")
            MonsterCharacter.monster[1] -= damage
            PlayerCharacter.slotsleft -= 1
        if MonsterCharacter.monster[1] <= 0:
            self.MonsterQuestCheck(MonsterCharacter.monster[0])
            Flags.battle = False
            self.frameEnemyInfo.setVisible(False)
            self.Text(f"You killed the {MonsterCharacter.monster[0]} and gained {MonsterCharacter.monster[7]}xp")
            PlayerCharacter.currentXp += MonsterCharacter.monster[7]
            self.UpdateInformation()
            return
        self.MonsterAction()

    def LossSystem(self):
        self.mainTextBox.clear()
        self.Text(f'You were defeated by the {MonsterCharacter.monster[0]}...')
        self.Text(f"You lost {round(Inventory.gold/2)} gold...")
        Inventory.gold = round(Inventory.gold/2)
        if Locations.area == 0:
            Locations.currentLocation = 'Home'
            Locations.currentCoord = [11,7]
            Locations.overworld = False
            PlayerCharacter.currentHP = PlayerCharacter.hp
            self.UpdateInformation()

    def MonsterAction(self):
        roll = random.randint(1,100)
        mon = MonsterCharacter.monster
        self.Text(f'The {mon[0]} attacks with its {mon[3]}.')
        if roll >= (PlayerCharacter.dexterity*2):
            self.Text(f'It deals {mon[4]} damage.')
            PlayerCharacter.currentHP -= mon[4] - Inventory.eDictionary[Inventory.equipment[0]][1]
        else:
            self.Text('But it missed.')
        mon = MonsterCharacter.monster
        hp = round(100 * (mon[1]/mon[2]))
        self.labelHPEnemy.setText(f"{mon[0]} Hitpoints: {mon[1]}/{mon[2]}".capitalize())
        self.progressBarEnemyHp.setValue(hp)
        self.UpdateInformation()
        if PlayerCharacter.currentHP <=0:
            Flags.battle = False
            self.LossSystem()

    def MonsterSelection(self,location):
        self.mainTextBox.clear()
        if location == 'Cliffside Farms' or location == 'Lighthouse Road':
            MonsterCharacter.monster = getattr(MonsterCharacter,'rat')
        if location == 'Forest':
            MonsterCharacter.monster = getattr(MonsterCharacter,'slime')
        if location == 'Westcliff Beach' or location == 'Westcliff Shallows':
            MonsterCharacter.monster = getattr(MonsterCharacter,'crab')
        if location == 'Westcliff Plains':
            MonsterCharacter.monster = getattr(MonsterCharacter,'hawk')
        if location == 'Westcliff Road':
            MonsterCharacter.monster = getattr(MonsterCharacter,'thief')
        mon = MonsterCharacter.monster
        mon[1]=mon[2]
        self.labelEnemy.setText(f"{mon[0]}".capitalize())
        self.labelHPEnemy.setText(f"{mon[0]} Hitpoints: {mon[1]}/{mon[2]}".capitalize())
        self.progressBarEnemyHp.setValue(100)
        self.Text(f"A {mon[0]} appears!")

    def MonsterQuestCheck(self,monster):
        if monster == 'rat' and Flags.farmquest1 == 1:
            QuestChecks.ratsKilled += 1
            if QuestChecks.ratsKilled >= 5:
                Flags.farmquest1 = 2
        if monster == 'slime' and Flags.magicQuest == 1:
            QuestChecks.slimesKilled += 1
            if QuestChecks.slimesKilled >= 10:
                Flags.magicQuest = 2

### ###

## SHOP RELATED FUNCTIONS ###

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
            theItem = I.eDictionary[itemT]
            self.Text(f'{itemT}\t {theItem[0]}\t\t{theItem[2]} {theItem[1]}\tPrice: {theItem[4]}')

### ###

### OVERWORLD \ LOCATION FUCTIONS ###
    def CheckCoords(self):
        Lc = Locations.currentCoord
        Ll = Locations.currentLocation
        x = Lc[0]
        y = Lc[1]
        if x == 11 and y == 7:
            Ll = 'Westcliff'
            self.SetTime(30)
        if x == 3 and y == 7:
            Ll = 'Lighthouse'
            self.SetTime(30)
        if x == 17 and y == 6:
            Ll = 'Westcliff Docks'
            self.SetTime(30)
        if x == 28 and y == 10:
            Ll = 'Vineyard Building'
            self.SetTime(30)

        #### AREAS ####
        # AREA 1
        if (x >= 3 and x <= 12) and (y >= 1 and y <= 6):
            Ll = 'Forest'
            self.SetTime(60)
        if (x >= 4 and x <= 10) and y == 7:
            Ll = 'Lighthouse Road'
            self.SetTime(30)
        if (x >= 3 and x <= 7) and (y >= 8 and y <= 11):
            Ll = 'Cliffside Plains'
            self.SetTime(45)
        if (x >= 8 and x <= 14) and (y >= 8 and y <= 11):
            Ll = 'Cliffside Farms'
            self.SetTime(45)
        if (x >= 12 and x <= 24) and y == 7:
            Ll = 'Westcliff Road'
            self.SetTime(30)
        if ((x >= 15 and x <= 24) and (y >= 8 and y <= 11)) or ((x>=22 and x<=24) and (y>=12 and y<=13)):
            Ll = 'Westcliff Plains'
            self.SetTime(45)
        if ((x >= 13 and x <= 16) or (x >= 18 and x <= 20)) and y == 6:
            Ll = 'Westcliff Beach'
            self.SetTime(45)
        if (x >= 13 and x <= 24) and (y >= 1 and y <= 5):
            Ll = 'Westcliff Shallows'
            self.SetTime(60)
        # AREA 2
        if x != 28 and y != 10:
            if (x >= 26 and x <=31) and (y >= 9 and y<=11):
                Ll = 'Deco Vineyard'
                self.SetTime(45)
        if x == 25 and (y>=9 and y<=18):
                Ll = 'North Road'
                self.SetTime(30)



        Locations.currentLocation = Ll
        self.UpdateInformation()
    
    def EncounterSystem(self,chance):
        area = Locations.currentLocation
        roll = random.randint
        enemyEncounter = 0  - (PlayerCharacter.charisma/10)
        randomEvent = 0 
        if Locations.overworld == True:
            if area == 'Forest':
                enemyEncounter += (0 + roll(1,100)) * chance
                randomEvent += (10 + roll(1,100)) * chance
            if area == 'Cliffside Farms':
                enemyEncounter += (-5 + roll(1,100)) * chance
                randomEvent += (10 + roll(1,100)) * chance
            if area == 'Lighthouse Road':
                enemyEncounter += (-30 + roll(1,100)) * chance
                randomEvent += (5 + roll(1,100)) * chance
            if area == 'Cliffside Plains':
                enemyEncounter += (-50 + roll(1,100)) * chance
                randomEvent += (5 + roll(1,100)) * chance
            if area == 'Westcliff Plains':
                enemyEncounter += (10 + roll(1,100)) * chance
                randomEvent += (5 + roll(1,100)) * chance
            if area == 'Westcliff Road':
                enemyEncounter += (5 + roll(1,100)) * chance
                randomEvent += (10 + roll(1,100)) * chance
            if area == 'Westcliff Beach':
                enemyEncounter += (0 + roll(1,100)) * chance
                randomEvent += (0 + roll(1,100)) * chance
            if area == 'Westcliff Shallows':
                enemyEncounter += (5 + roll(1,100)) * chance
                randomEvent += (5 + roll(1,100)) * chance
        print(enemyEncounter,randomEvent)  
        if enemyEncounter > randomEvent and enemyEncounter > 10:
            print('Battle')
            Flags.battle = True
            self.MonsterSelection(area)
            self.frameEnemyInfo.setVisible(True)
        if randomEvent > enemyEncounter and randomEvent > 10:
            print ('Random Event')
        self.UpdateInformation()

    def LocationUpdate(self,location,var):
        Locations.currentLocation = location
        self.labelLocation.setText(Locations.currentLocation)
        self.DialogueFunction(Locations.currentLocation,var)

    def OverWorldMovement(self,button):
        Lc = Locations.currentCoord
        if button == 'w':
            Lc[1] += 1
        if button == 'x':
            Lc[1] -= 1
        if button == 'd':
            Lc[0] += 1
        if button == 'a':
            Lc[0] -= 1
        Locations.currentCoord = Lc
        print(Locations.currentCoord)
        self.CheckCoords()
        self.EncounterSystem(0.12)

### ###
    def QuestRewards(self,quest):
        if quest == 'Farm':
            PlayerCharacter.currentXp += 5
            Inventory.gold += 5
        if quest == 'Magic':
            PlayerCharacter.currentXp += 5
            Flags.magicAvailable = 1
            PlayerCharacter.slotsleft = PlayerCharacter.slots
            self.labelSlots.setVisible(True)
        self.UpdateInformation()

    def QuestCheck(self):
        if Flags.farmquest1 == 3:
            self.QuestRewards('Farm')
            Flags.farmquest1 = 4
        if Flags.magicQuest == 3:
            self.QuestRewards('Magic')
            Flags.magicQuest = 4

    def UpdateDateTime(self):
        T = Time
        mi = T.minute
        h = T.hour
        d = T.day
        mo = T.month
        dn = T.currentDayName
        self.labelTime.setText(f"Time: {h}:{mi:02}")
        self.labelDate.setText(f"Date: {dn}\t{d}/{mo:0>2d}")

    def UpdateInformation(self):
        self.labelName.setText(PlayerCharacter.name)
        self.labelAEquipped.setText(Inventory.equipment[0].capitalize())
        self.labelWEquippped.setText(Inventory.equipment[1].capitalize())
        self.labelGold.setText(f"Gold: {str(Inventory.gold)}")
        self.labelLocation.setText(Locations.currentLocation)
        self.labelPlayerHealth.setText(f"Hitpoints: {PlayerCharacter.currentHP}/{PlayerCharacter.hp}")
        hp = round(100 *(PlayerCharacter.currentHP/PlayerCharacter.hp))
        self.barHealth.setValue(hp)
        self.labelLevel.setText(f"Level: {PlayerCharacter.level}")
        self.labelXp.setText(f"Experience: {PlayerCharacter.currentXp}/{PlayerCharacter.xpNeeded}")
        self.labelStrength.setText(f"Strength:\t {PlayerCharacter.strength}")
        self.labelDexterity.setText(f"Dexterity:\t {PlayerCharacter.dexterity}")
        self.labelArcane.setText(f"Arcane:\t\t {PlayerCharacter.arcane}")
        self.labelConstitution.setText(f"Constitution:\t {PlayerCharacter.constitution}")
        self.labelCharisma.setText(f"Charisma:\t {PlayerCharacter.charisma}")
        self.labelSlots.setText(f"Spell Power Remaining: {PlayerCharacter.slotsleft}/{PlayerCharacter.slots}")
        if PlayerCharacter.currentXp >= PlayerCharacter.xpNeeded:
            self.LevelUpFunction()        
        
    def LevelUpFunction(self):
        Flags.levelUp = True
        self.Text("You've gained a level! Select a stat to increase.")
        PlayerCharacter.currentXp -= PlayerCharacter.xpNeeded
        PlayerCharacter.currentHP = PlayerCharacter.hp
        PlayerCharacter.level += 1
    
    def StatIncrease(self,stat):
        P = PlayerCharacter
        if stat == 'Strength': P.strength += 1
        if stat == 'Dexterity': P.dexterity += 1
        if stat == 'Arcane': P.arcane += 1
        if stat == 'Constitution': P.constitution += 1
        if stat == 'Charisma': P.charisma += 1
        PlayerCharacter.currentHP = PlayerCharacter.hp
        self.setStats()
        self.UpdateInformation()
        Flags.levelUp = False
    
    def DialogueFunction(self,target,var):
        """Function to call text for given event. (target of function,variable)"""
        Dialogue.text = ''
        v = f"('{var}')"
        d = "Dialogue."
        concat = (d+target+v).replace(' ','')
        text = eval(concat)
        self.Text(text)
        self.QuestCheck()

    def CharacterCreation(self):
        self.CCreate = CreationWindow()
        self.CCreate.signal_function.connect(self.GameSetup)
        self.CCreate.show()
    
    def setStats(self):
        PC = PlayerCharacter
        PC.hp = 3 + PC.level*2 + PC.constitution * PC.level
        PC.currentHP = PC.hp
        PC.xpNeeded = PC.level * 10
        PC.slots = round(PC.arcane/2)
        PC.harvests = round(PC.constitution/2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm(CreationWindow)
    the_form.show()
    sys.exit(app.exec_())