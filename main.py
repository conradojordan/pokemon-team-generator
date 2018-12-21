import re
import sys
import MainWindow
import random
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


def parsePokemonData():
    global pokemon
    pokemon = []
    pokemonRegex = re.compile(r'(\d+),(\d+),(.+),\[(.+)\],(\d+),(\d+),(\d+),(\d+),(\d+),(\d+),(\d+),(True|False),(True|False)')
    file = open('pokemon.txt')
    pokeData = file.read().strip().split('\n')

    for i in range(1,len(pokeData)):
        currentPokemon = {}
        match = pokemonRegex.search(pokeData[i])
        # {generation, num, name, type(s), totalStats, HP, attack, defense, sp_attack, sp_defense, speed, fullyEvolved, legendary}
        currentPokemon['gen'] = int(match.group(1))
        currentPokemon['num'] = int(match.group(2))
        currentPokemon['name'] = match.group(3)
        typeList = []

        for types in match.group(4).split(','):
            typeList.append(types.strip().strip("'"))
        currentPokemon['types'] = typeList
        currentPokemon['totalStats'] = int(match.group(5))
        currentPokemon['hp'] = int(match.group(6))
        currentPokemon['atk'] = int(match.group(7))
        currentPokemon['def'] = int(match.group(8))
        currentPokemon['spAtk'] = int(match.group(9))
        currentPokemon['spDef'] = int(match.group(10))
        currentPokemon['speed'] = int(match.group(11))
        currentPokemon['fullyEvolved'] = match.group(12) == 'True'
        currentPokemon['legendary'] = match.group(13) == 'True'

        pokemon.append(currentPokemon)
    file.close()

    file = open('evolutions.txt')
    evoData = file.read().strip().split('\n')
    global evolutions
    evolutions = []

    for line in evoData:
        evolutions.append(eval(line))
    file.close()


class mainWindow(QMainWindow, MainWindow.Ui_MainWindow):

    generations = {1, 2, 3, 4, 5, 6, 7}
    types = {'Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire',
             'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic',
             'Rock', 'Steel', 'Water'}
    allowLegendaries = True
    allowRepetitions = False
    justFullyEvolved = False
    filteredPokemon = []

    # Center window on screen
    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def legendaries(self, state):
        if state == Qt.Checked:
            self.allowLegendaries = True
        else:
            self.allowLegendaries = False

    def repetitions(self, state):
        if state == Qt.Checked:
            self.allowRepetitions = True
        else:
            self.allowRepetitions = False

    def fullyEvolved(self, state):
        if state == Qt.Checked:
            self.justFullyEvolved = True
        else:
            self.justFullyEvolved = False

    def generation1(self, state):
        if state == Qt.Checked:
            self.generations.add(1)
        else:
            self.generations.discard(1)

    def generation2(self, state):
        if state == Qt.Checked:
            self.generations.add(2)
        else:
            self.generations.discard(2)

    def generation3(self, state):
        if state == Qt.Checked:
            self.generations.add(3)
        else:
            self.generations.discard(3)

    def generation4(self, state):
        if state == Qt.Checked:
            self.generations.add(4)
        else:
            self.generations.discard(4)

    def generation5(self, state):
        if state == Qt.Checked:
            self.generations.add(5)
        else:
            self.generations.discard(5)

    def generation6(self, state):
        if state == Qt.Checked:
            self.generations.add(6)
        else:
            self.generations.discard(6)

    def generation7(self, state):
        if state == Qt.Checked:
            self.generations.add(7)
        else:
            self.generations.discard(7)

    def bug(self,state):
        if state == Qt.Checked:
            self.types.add('Bug')
        else:
            self.types.discard('Bug')

    def dark(self,state):
        if state == Qt.Checked:
            self.types.add('Dark')
        else:
            self.types.discard('Dark')

    def dragon(self,state):
        if state == Qt.Checked:
            self.types.add('Dragon')
        else:
            self.types.discard('Dragon')

    def electric(self,state):
        if state == Qt.Checked:
            self.types.add('Electric')
        else:
            self.types.discard('Electric')

    def fairy(self,state):
        if state == Qt.Checked:
            self.types.add('Fairy')
        else:
            self.types.discard('Fairy')

    def fighting(self,state):
        if state == Qt.Checked:
            self.types.add('Fighting')
        else:
            self.types.discard('Fighting')

    def fire(self,state):
        if state == Qt.Checked:
            self.types.add('Fire')
        else:
            self.types.discard('Fire')

    def flying(self,state):
        if state == Qt.Checked:
            self.types.add('Flying')
        else:
            self.types.discard('Flying')

    def ghost(self,state):
        if state == Qt.Checked:
            self.types.add('Ghost')
        else:
            self.types.discard('Ghost')

    def grass(self,state):
        if state == Qt.Checked:
            self.types.add('Grass')
        else:
            self.types.discard('Grass')

    def ground(self,state):
        if state == Qt.Checked:
            self.types.add('Ground')
        else:
            self.types.discard('Ground')

    def ice(self,state):
        if state == Qt.Checked:
            self.types.add('Ice')
        else:
            self.types.discard('Ice')

    def normal(self,state):
        if state == Qt.Checked:
            self.types.add('Normal')
        else:
            self.types.discard('Normal')

    def poison(self,state):
        if state == Qt.Checked:
            self.types.add('Poison')
        else:
            self.types.discard('Poison')

    def psychic(self,state):
        if state == Qt.Checked:
            self.types.add('Psychic')
        else:
            self.types.discard('Psychic')

    def rock(self,state):
        if state == Qt.Checked:
            self.types.add('Rock')
        else:
            self.types.discard('Rock')

    def steel(self,state):
        if state == Qt.Checked:
            self.types.add('Steel')
        else:
            self.types.discard('Steel')

    def water(self,state):
        if state == Qt.Checked:
            self.types.add('Water')
        else:
            self.types.discard('Water')

    def allTypes(self, state):
        if state == Qt.Checked:
            self.checkBug.setChecked(True)
            self.checkDark.setChecked(True)
            self.checkDragon.setChecked(True)
            self.checkElectric.setChecked(True)
            self.checkFairy.setChecked(True)
            self.checkFighting.setChecked(True)
            self.checkFire.setChecked(True)
            self.checkFlying.setChecked(True)
            self.checkGhost.setChecked(True)
            self.checkGrass.setChecked(True)
            self.checkGround.setChecked(True)
            self.checkIce.setChecked(True)
            self.checkNormal.setChecked(True)
            self.checkPoison.setChecked(True)
            self.checkPsychic.setChecked(True)
            self.checkRock.setChecked(True)
            self.checkSteel.setChecked(True)
            self.checkWater.setChecked(True)
        else:
            self.checkBug.setChecked(False)
            self.checkDark.setChecked(False)
            self.checkDragon.setChecked(False)
            self.checkElectric.setChecked(False)
            self.checkFairy.setChecked(False)
            self.checkFighting.setChecked(False)
            self.checkFire.setChecked(False)
            self.checkFlying.setChecked(False)
            self.checkGhost.setChecked(False)
            self.checkGrass.setChecked(False)
            self.checkGround.setChecked(False)
            self.checkIce.setChecked(False)
            self.checkNormal.setChecked(False)
            self.checkPoison.setChecked(False)
            self.checkPsychic.setChecked(False)
            self.checkRock.setChecked(False)
            self.checkSteel.setChecked(False)
            self.checkWater.setChecked(False)

    def allGen(self, state):
        if state == Qt.Checked:
            self.checkGen1.setChecked(True)
            self.checkGen2.setChecked(True)
            self.checkGen3.setChecked(True)
            self.checkGen4.setChecked(True)
            self.checkGen5.setChecked(True)
            self.checkGen6.setChecked(True)
            self.checkGen7.setChecked(True)
        else:
            self.checkGen1.setChecked(False)
            self.checkGen2.setChecked(False)
            self.checkGen3.setChecked(False)
            self.checkGen4.setChecked(False)
            self.checkGen5.setChecked(False)
            self.checkGen6.setChecked(False)
            self.checkGen7.setChecked(False)


    def generateTeam(self):
        pokemonLabels = [self.labelPokeName1, self.labelPokeName2,
                         self.labelPokeName3, self.labelPokeName4,
                         self.labelPokeName5, self.labelPokeName6]

        self.filterPokemon()

        if len(self.filteredPokemon) == 0:
            self.labelError.setText('No pokémon were found! Try widening the criteria.')
            self.labelPokeName1.setText('')
            self.labelPokeName2.setText('')
            self.labelPokeName3.setText('')
            self.labelPokeName4.setText('')
            self.labelPokeName5.setText('')
            self.labelPokeName6.setText('')
        else:
            self.labelError.setText('')
            for i in range(6):
                chosenEvolution = set()
                if len(self.filteredPokemon) >= 1:
                    randomPoke = random.randint(0, len(self.filteredPokemon)-1)
                    pokemonLabels[i].setText(self.filteredPokemon[randomPoke]['name'])
                    if not self.allowRepetitions:
                        for i in range(len(evolutions)):
                            if self.filteredPokemon[randomPoke]['name'] in evolutions[i]:
                                chosenEvolution = evolutions[i]
                                break
                        pokemonToEliminate = []
                        if len(chosenEvolution) > 0:
                            for filtered in self.filteredPokemon:
                                if filtered['name'] in chosenEvolution:
                                    pokemonToEliminate.append(filtered)
                            for eliminate in pokemonToEliminate:
                                index = self.filteredPokemon.index(eliminate)
                                del self.filteredPokemon[index]
                        else:
                            del self.filteredPokemon[randomPoke]
                else:
                    pokemonLabels[i].setText('')
                    self.labelError.setText('  Not enough pokemon for a whole team!')

    def filterPokemon(self):
        self.filteredPokemon = []
        for poke in pokemon:
            hasType = False
            for i in range(len(poke['types'])):
                if poke['types'][i] in self.types:
                    hasType = True
            if not hasType:
                continue
            if poke['gen'] not in self.generations:
                continue
            if not self.allowLegendaries:
                if poke['legendary']:
                    continue
            if self.justFullyEvolved:
                if not poke['fullyEvolved']:
                    continue
            self.filteredPokemon.append(poke)


    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.generateButton.clicked.connect(self.generateTeam)

        self.checkGen1.stateChanged.connect(self.generation1)
        self.checkGen2.stateChanged.connect(self.generation2)
        self.checkGen3.stateChanged.connect(self.generation3)
        self.checkGen4.stateChanged.connect(self.generation4)
        self.checkGen5.stateChanged.connect(self.generation5)
        self.checkGen6.stateChanged.connect(self.generation6)
        self.checkGen7.stateChanged.connect(self.generation7)

        self.checkBug.stateChanged.connect(self.bug)
        self.checkDark.stateChanged.connect(self.dark)
        self.checkDragon.stateChanged.connect(self.dragon)
        self.checkElectric.stateChanged.connect(self.electric)
        self.checkFairy.stateChanged.connect(self.fairy)
        self.checkFighting.stateChanged.connect(self.fighting)
        self.checkFire.stateChanged.connect(self.fire)
        self.checkFlying.stateChanged.connect(self.flying)
        self.checkGhost.stateChanged.connect(self.ghost)
        self.checkGrass.stateChanged.connect(self.grass)
        self.checkGround.stateChanged.connect(self.ground)
        self.checkIce.stateChanged.connect(self.ice)
        self.checkNormal.stateChanged.connect(self.normal)
        self.checkPoison.stateChanged.connect(self.poison)
        self.checkPsychic.stateChanged.connect(self.psychic)
        self.checkRock.stateChanged.connect(self.rock)
        self.checkSteel.stateChanged.connect(self.steel)
        self.checkWater.stateChanged.connect(self.water)

        self.checkAllTypes.stateChanged.connect(self.allTypes)
        self.checkAllGen.stateChanged.connect(self.allGen)

        self.checkLegends.stateChanged.connect(self.legendaries)
        self.checkRepetitions.stateChanged.connect(self.repetitions)
        self.checkFullyEvolved.stateChanged.connect(self.fullyEvolved)

        self.checkAllGen.setChecked(True)
        self.checkGen1.setChecked(True)
        self.checkGen2.setChecked(True)
        self.checkGen3.setChecked(True)
        self.checkGen4.setChecked(True)
        self.checkGen5.setChecked(True)
        self.checkGen6.setChecked(True)
        self.checkGen7.setChecked(True)



        self.checkAllTypes.setChecked(True)
        self.checkBug.setChecked(True)
        self.checkDark.setChecked(True)
        self.checkDragon.setChecked(True)
        self.checkElectric.setChecked(True)
        self.checkFairy.setChecked(True)
        self.checkFighting.setChecked(True)
        self.checkFire.setChecked(True)
        self.checkFlying.setChecked(True)
        self.checkGhost.setChecked(True)
        self.checkGrass.setChecked(True)
        self.checkGround.setChecked(True)
        self.checkIce.setChecked(True)
        self.checkNormal.setChecked(True)
        self.checkPoison.setChecked(True)
        self.checkPsychic.setChecked(True)
        self.checkRock.setChecked(True)
        self.checkSteel.setChecked(True)
        self.checkWater.setChecked(True)

        self.checkLegends.setChecked(True)
        self.checkRepetitions.setChecked(False)
        self.checkFullyEvolved.setChecked(False)

        self.center()
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    parsePokemonData()
    mainWindow = mainWindow()

    sys.exit(app.exec_())
