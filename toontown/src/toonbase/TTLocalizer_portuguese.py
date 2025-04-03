import string
import time
from toontown.toonbase.TTLocalizer_portuguese_Property import *
from toontown.catalog import CatalogAccessoryItemGlobals
from otp.otpbase import OTPLocalizer as OL
OL.SpeedChatStaticText = dict(OL.SpeedChatStaticTextToontown)
OL.SpeedChatStaticText.update(OL.SpeedChatStaticTextCommon)

# To make sure the language checker is working
# DO NOT TRANSLATE THIS
ExtraKeySanityCheck = "Ignore-me"

# commit strings
#commitmanString = "bugfix! I changed this"
#commitmanSting2 = "another string!"
commitmantst = "kptmptest - removable"

InterfaceFont = 'phase_3/models/fonts/ImpressBT.ttf'
ToonFont = 'phase_3/models/fonts/ImpressBT.ttf'
#SuitFont = 'phase_3/models/fonts/vtRemingtonPortable.ttf'
# Not really sure why Brazil changed the suit font that late in the game,
# for the moment the change will still be included. ~Bob
SuitFont = 'phase_3/models/fonts/HGHanKointai.ttc'
SignFont = 'phase_3/models/fonts/MickeyFont'
MinnieFont = 'phase_3/models/fonts/MinnieFont'
FancyFont = 'phase_3/models/fonts/Comedy'
NametagFonts = ('phase_3/models/fonts/AnimGothic',      #0 *
                'phase_3/models/fonts/Aftershock',      #1 *
                'phase_3/models/fonts/JiggeryPokery',   #2 *
                'phase_3/models/fonts/Ironwork',        #3 *
                'phase_3/models/fonts/HastyPudding',    #4 *
                'phase_3/models/fonts/Comedy',          #5 *
                'phase_3/models/fonts/Humanist',        #6 *
                'phase_3/models/fonts/Portago',         #7 *
                'phase_3/models/fonts/Musicals',        #8 *
                'phase_3/models/fonts/Scurlock',        #9 *
                'phase_3/models/fonts/Danger',          #10 *
                'phase_3/models/fonts/Alie',            #11 *
                'phase_3/models/fonts/OysterBar',       #12 *
                'phase_3/models/fonts/RedDogSaloon',    #13 *
                )
NametagFontNames = ('Usuário',      #0 *
                'Tremido',         #1 *
                'Arrepiante',      #2 *
                'Exorbitante',     #3 *
                'Bobo',            #4 *
                'Doido',           #5 *
                'Pratico',         #6 *
                'Nautico',         #7 *
                'Caprichoso',      #8 *
                'Estremecer',      #9 *
                'Ação',            #10 *
                'Poético',         #11 *
                'Passeio',         #12 *
                'Ocidental',       #13 *
                )

NametagLabel = " Nome"

UnpaidNameTag = "Basico"

GM_NAMES = ("CONSELHO TOON",
            "TROPA TOON",
            "TOON DA RESIST\xc3\x8aNCIA",
            "GC",
            )

BuildingNametagFont = 'phase_3/models/fonts/MickeyFont'
BuildingNametagShadow = None

# Product prefix
ProductPrefix = 'TT'

# common names
Mickey = "Mickey"
VampireMickey = "VampireMickey"
Minnie = "Minnie"
WitchMinnie = "WitchMinnie"
Donald = "Donald"
DonaldDock = "DonaldDock"
FrankenDonald = "FrankenDonald"
Daisy  = "Margarida"
SockHopDaisy = "SockHopDaisy"
Goofy  = "Pateta"
SuperGoofy = "SuperGoofy"
Pluto  = "Pluto"
WesternPluto = "WesternPluto"
Flippy = "Flippy"
Chip   = "Tico"
Dale   = "Teco"
JailbirdDale = "JailbirdDale"
PoliceChip = "PoliceChip"

# common locations
lTheBrrrgh = 'O Brrrgh'
lDaisyGardens = 'Jardim da Margarida'
lDonaldsDock = "Porto do Donald"
lDonaldsDreamland = "Sonholândia do Donald"
lMinniesMelodyland = "Melodilândia da Minnie"
lToontownCentral = 'Centro de Toontown'
lToonHQ = 'Quartel dos Toons'
lSellbotHQ = 'Quartel do Robô Vendedor'
lGoofySpeedway = "Autódromo do Pateta"
lOutdoorZone = "Bosque de Bolotas de Tico e Teco"
lGolfZone = "Minigolfe de Tico e Teco"
lPartyHood = "Terra do Festas"

lGagShop = 'Loja de Piadas'
lClothingShop = 'Loja de Roupas'
lPetShop = 'Loja de Animais'

# ToontownGlobals.py

# (to, in, location)
# reference the location name as [-1]; it's guaranteed to be the last entry
# This table may contain names for hood zones (N*1000) that are not
# appropriate when referring to the hood as a whole. See the list of
# names below this table for hood names.
GlobalStreetNames = {
    20000 : ("para o",  "no", "Terraço do Tutorial"), # Tutorial
    1000  : ("para o",  "no", "Parque"),
    1100  : ("para o",  "no", "Boulevard das Cracas"),
    1200  : ("para a",  "na", "Rua da Alga Marinha"),
    1300  : ("para a",  "na", "Travessa do Farol"),
    2000  : ("para o",  "no", "Parque"),
    2100  : ("para a",  "na", "Rua da Bobeira"),
    2200  : ("para a",  "na", "Travessa dos Tontos"),
    2300  : ("para o",  "no", "Largo do Auge da Graça"),
    3000  : ("para o",  "no", "Parque"),
    3100  : ("para a",  "na", "Via dos Leões Marinhos"),
    3200  : ("para a",  "na", "Rua da Chuva de Neve"),
    3300  : ("para o",  "no", "Lugar Polar"),
    4000  : ("para o",  "no", "Parque"),
    4100  : ("para a",  "na", "Avenida do Tom Alto"),
    4200  : ("para o",  "no", "Boulevard do Bar\xc3\xadtono"),
    4300  : ("para o",  "no", "Terraço do Tenor"),
    5000  : ("para o",  "no", "Parque"),
    5100  : ("para a",  "na", "Rua das Nogueiras"),
    5200  : ("para a",  "na", "Rua das Amendoeiras"),
    5300  : ("para a",  "na", "Rua dos Carvalhos"),
    9000  : ("para o",  "no", "Parque"),
    9100  : ("para a",  "na", "Travessa da Canção de Ninar"),
    9200  : ("para o",  "no", "Pedaço do Pijama"),
    10000 : ("","", ""),
    10100 : ("para o",  "no", "Salão do Quartel do Robô-chefe"),
    10200 : ("para a", "na", "Sede do Clube"),
    10500 : ("para o", "no", "Tr\xc3\xaas da Frente"),
    10600 : ("para o", "no", "Seis do Meio"),
    10700 : ("para o", "no", "Nove de Trás"),
    11000 : ("para o", "no", ""),
    11100 : ("para o",  "no", "Salão do "+lSellbotHQ),
    11200 : ("para a",  "na", "Fábrica do Robô Vendedor"),
    11500 : ("para a",  "na", "Fábrica do Robô Vendedor"),
    12000 : ("","", ""),
    12100 : ("para o",  "no", "Salão do Quartel do Robô Mercenário"),
    12500 : ("para a",  "na", "Casa da Moeda"),
    12600 : ("para a",  "na", "Casa da Moeda de Dólar"),
    12700 : ("para a",  "na", "Casa da Moeda de Barras de Ouro"),
    13000 : ("","", ""),
    13100 : ("para o",  "no", "Salão do Quartel do Robô da Lei"),
    13200 : ("para o", "no", "Lobby do Escritório do Promotor"),
    13300 : ("para o", "no", "Escritório da Lei A"),
    13400 : ("para o", "no", "Escritório da Lei B"),
    13500 : ("para o", "no", "Escritório da Lei C"),
    13600 : ("para o", "no", "Escritório da Lei D"),
    }

# reference the location name as [-1]; it's guaranteed to be the last entry
DonaldsDock       = ("para o",  "no",    lDonaldsDock)
ToontownCentral   = ("para o",  "no",    lToontownCentral)
TheBrrrgh         = ("para",    "em",    lTheBrrrgh)
MinniesMelodyland = ("para a",  "na",    lMinniesMelodyland)
DaisyGardens      = ("para os", "nos",   lDaisyGardens)
OutdoorZone       = ("para a",  "na",    lOutdoorZone)
FunnyFarm         = ("para a",  "na",    "Fazenda Divertida")
GoofySpeedway     = ("para o",  "no",    lGoofySpeedway)
DonaldsDreamland  = ("para a",  "na",    lDonaldsDreamland)
BossbotHQ         = ("para o",  "no",    "Quartel do Robô-chefe")
SellbotHQ         = ("para o",  "no",    lSellbotHQ)
CashbotHQ         = ("para o",  "no",    "Quartel do Robô Mercenário")
LawbotHQ          = ("para o",  "no",    "Quartel do Robô da Lei")
Tutorial          = ("para o",  "no",    "Toon-torial")
MyEstate          = ("para a",  "na",    "sua casa")
WelcomeValley     = ("para o",  "no",    "Vale Boas-vindas")
GolfZone          = ("para a",  "na",    lGolfZone)
PartyHood         = ("para a",  "na",    lPartyHood)

Factory = 'Fábrica'
Headquarters = 'Quartel'
SellbotFrontEntrance = 'Entrada principal'
SellbotSideEntrance = 'Entrada lateral'
Office = 'Escritório'

FactoryNames = {
    0 : 'Molde da fábrica',
    11500 : 'Fábrica do Cog Robô Vendedor',
    13300 : 'Escritório de Cogs Policiais', #remove me JML
    }

FactoryTypeLeg = 'Perna'
FactoryTypeArm = 'Braço'
FactoryTypeTorso = 'Busto'

MintFloorTitle = 'Andar %s'

# common strings
lCancel = 'Cancelar'
lClose = 'Fechar'
lOK = 'OK'
lNext = 'Próximo'
lQuit = 'Sair'
lYes = 'Sim'
lNo = 'Não'

sleep_auto_reply = "%s is sleeping right now"
lHQ = 'Oficial'

lHQOfficerF = 'Oficial do Quartel'
lHQOfficerM = 'Oficial do Quartel'

MickeyMouse = "Mickey Mouse"

AIStartDefaultDistrict = "Vila dos Idiotas"

Cog  = "Cog"
Cogs = "Cogs"
ACog = "um Cog"
TheCogs = "os Cogs"
ASkeleton = "um Esqueletocog"
Skeleton = "Esqueletocogs"
SkeletonP = "Esqueletocogs"
Av2Cog = "um Cog Versão 2.0"
v2Cog = "Cog Versão 2.0"
v2CogP = "Cogs Versão 2.0"
Foreman = "Supervisor da fábrica"
ForemanP = "Supervisores da fábrica"
AForeman = "um Supervisor da fábrica"
CogVP = Cog + " VP"
CogVPs = "Cogs VPs"
ACogVP = ACog + " VP"
Supervisor = "Supervisor da Casa da Moeda"
SupervisorP = "Supervisores da Casa da Moeda"
ASupervisor = "um Supervisor da Casa da Moeda"
CogCFO = Cog + " Diretor Financeiro"
CogCFOs = "Diretores Financeiros Cogs"
ACogCFO = ACog + " Diretor Financeiro"

#lBossbotHQ = 'Quartel do Robô-chefe'
#lLawbotHQ = 'Quartel do Robô da Lei'
#lCashbotHQ = 'Quartel do Robô Mercenário'
#lSellbotHQ = 'Quartel do Robô Vendedor'
#lTutorial = 'Toon-torial'
#lMyEstate = 'sua casa'
#lWelcomeValley = 'Vale Boas-vindas'

# Quests.py
TheFish = "o Peixe"
AFish = "um peixe"
Level = "n\xc3\xadvel"
QuestsCompleteString = "Concluir"
QuestsNotChosenString = "Não escolhido"
Period = "."

Laff = "Risada"

QuestInLocationString = " %(inPhrase)s %(location)s"

# _avName_ gets replaced with the avatar (player's) name
# _toNpcName_ gets replaced with the npc's name we are being sent to
# _where_ gets replaced with a description of where to find the npc, with a leading \a
QuestsDefaultGreeting = ("Olá, _avName_!",
                         "Oi, _avName_!",
                         "E a\xc3\xad, _avName_?",
                         "Diga a\xc3\xad, _avName_!",
                         "Bem-vindo, _avName_!",
                         "Tudo certo, _avName_?",
                         "Como vai voc\xc3\xaa, _avName_?",
                         "Olá _avName_!",
                         )
QuestsDefaultIncomplete = ("Como está indo aquela tarefa, _avName_?",
                           "Parece que voc\xc3\xaa ainda tem mais trabalho a fazer naquela tarefa!",
                           "Continue com o bom trabalho, _avName_!",
                           "Continue tentando concluir aquela tarefa. Eu sei que voc\xc3\xaa consegue!",
                           "Continue tentando concluir a tarefa. Contamos com voc\xc3\xaa!",
                           "Continue trabalhando naquela Tarefa Toon!",
                           )
QuestsDefaultIncompleteProgress = ("Voc\xc3\xaa veio ao lugar certo, mas, primeiramente, precisa concluir sua Tarefa Toon.",
                                   "Ao terminar a Tarefa Toon, volte aqui.",
                                   "Volte quando tiver terminado sua Tarefa Toon.",
                                   )
QuestsDefaultIncompleteWrongNPC = ("Bom trabalho naquela Tarefa Toon. Voc\xc3\xaa deveria visitar _toNpcName_._where_",
                                   "Parece que voc\xc3\xaa está pronto para concluir sua Tarefa Toon. Vá ver _toNpcName_._where_.",
                                   "Vá ver _toNpcName_ para concluir sua Tarefa Toon._where_",
                                   )
QuestsDefaultComplete = ("Bom trabalho! Aqui está a sua recompensa...",
                         "\xc3\x93timo trabalho, _avName_! Tome esta recompensa...",
                         "Excelente trabalho, _avName_! Aqui está a sua recompensa...",
                         )
QuestsDefaultLeaving = ("Tchau!",
                        "Até logo!",
                        "Até mais, _avName_.",
                        "Te vejo por a\xc3\xad, _avName_!",
                        "Boa sorte!",
                        "Divirta-se em Toontown!",
                        "Vejo voc\xc3\xaa depois!",
                        )
QuestsDefaultReject = ("Olá.",
                       "Posso ajudar?",
                       "Como vai voc\xc3\xaa?",
                       "E a\xc3\xad, pessoal?",
                       "Estou um pouco ocupado agora, _avName_.",
                       "Sim?",
                       "Tudo certo, _avName_!",
                       "Bem-vindo, _avName_!",
                       "Ei, _avName_! Tudo bem?",
                       # Game Hints
                       "Voc\xc3\xaa sabia que pode abrir seu \xc3\x81lbum Toon clicando em F8?",
                       "Voc\xc3\xaa pode usar seu mapa para se teletransportar de volta ao pátio!",
                       "Voc\xc3\xaa pode ficar amigo de outros jogadores clicando neles.",
                       "Voc\xc3\xaa pode descobrir mais sobre um "+ Cog +" clicando nele.",
                       "Junte tesouros nos pátios para encher seu Risômetro.",
                       "Os edif\xc3\xadcios " + Cog + " são lugares perigosos! Não entre neles sozinho!",
                       "Quando voc\xc3\xaa perde uma batalha, os "+ Cogs +" tomam todas as suas piadas.",
                       "Para obter mais piadas, jogue no Bondinho!",
                       "Voc\xc3\xaa pode obter mais Pontos de risadas completando as Tarefas Toon.",
                       "Toda Tarefa Toon dá uma recompensa a voc\xc3\xaa.",
                       "Algumas recompensas permitem que voc\xc3\xaa carregue consigo mais Piadas.",
                       "Se voc\xc3\xaa vencer uma batalha, ganhará créditos de Tarefa Toon para cada "+ Cog +" derrotado.",
                       "Se voc\xc3\xaa recuperar um edif\xc3\xadcio "+ Cog +", entre e verá um agradecimento especial do proprietário!",
                       "Se pressionar a tecla Page Up, poderá ver acima de voc\xc3\xaa!",
                       "Se voc\xc3\xaa pressionar a tecla Tab, poderá ver os arredores sob diversos ângulos!",
                       "Para mostrar aos amigos secretos o que está pensando, coloque '.' antes do pensamento.",
                       "Se um "+ Cog +" estiver atordoado, será mais dif\xc3\xadcil para ele desviar de objetos cadentes.",
                       "Cada tipo de edif\xc3\xadcio "+ Cog +" possui um visual diferente.",
                       "Derrotar os "+ Cogs +" nos andares mais altos de um edif\xc3\xadcio dará a voc\xc3\xaa maiores recompensas de habilidade.",
                       )
QuestsDefaultTierNotDone = ("Olá, _avName_! Voc\xc3\xaa deve concluir sua Tarefa Toon atual antes de começar uma nova.",
                            "E a\xc3\xad? Voc\xc3\xaa precisa concluir suas Tarefas Toon atuais antes de começar uma nova.",
                            "Oi, _avName_! Para que eu possa dar a voc\xc3\xaa uma nova Tarefa Toon, voc\xc3\xaa precisa terminar as que voc\xc3\xaa tem.",
                            )
# The default string gets replaced with the quest getstring
QuestsDefaultQuest = None
QuestsDefaultVisitQuestDialog = ("Ouvi falar que _toNpcName_ está procurando por voc\xc3\xaa._where_",
                                 "Passe por lá e visite _toNpcName_ quando tiver um tempinho._where_",
                                 "Visite _toNpcName_ da próxima vez em que estiver passando por aquele caminho._where_",
                                 "Se tiver um tempinho, pare e diga olá para _toNpcName_._where_",
                                 "_toNpcName_ dará a voc\xc3\xaa sua nova Tarefa Toon._where_",
                                 )
# Quest dialog
QuestsLocationArticle = ""
def getLocalNum(num):
	if (num <=9):
		return str(num) + ""
	else:
		return str(num)
QuestsItemNameAndNum = "%(num)s %(name)s"

QuestsCogQuestProgress = "%(progress)s de %(numCogs)s derrotados"
QuestsCogQuestHeadline = "PROCURADO"
QuestsCogQuestSCStringS = "Eu preciso derrotar %(cogName)s%(cogLoc)s"
QuestsCogQuestSCStringP = "Eu preciso derrotar alguns %(cogName)s%(cogLoc)s."
QuestsCogQuestDefeat = "Derrotar %s"
QuestsCogQuestDefeatDesc = "%(numCogs)s %(cogName)s"

QuestsCogNewNewbieQuestObjective = "Ajude um novo Toon a derrotar %s"
QuestsCogNewNewbieQuestCaption = "Ajude um novo Toon que tenha %d risadas ou menos que isso"
QuestsCogOldNewbieQuestObjective = "Ajude um Toon com %(laffPoints)d risadas, ou menos, a dominar %(objective)s"
QuestsCogOldNewbieQuestCaption = "Ajude um Toon com %d risadas, ou menos"
QuestsCogNewbieQuestAux = "Derrotar:"
QuestsNewbieQuestHeadline = "APRENDIZ"

QuestsCogTrackQuestProgress = "%(progress)s de %(numCogs)s derrotados"
QuestsCogTrackQuestHeadline = "PROCURADO"
QuestsCogTrackQuestSCStringS = "Eu preciso derrotar %(cogText)s%(cogLoc)s."
QuestsCogTrackQuestSCStringP = "Eu preciso derrotar alguns %(cogText)s%(cogLoc)s."
QuestsCogTrackQuestDefeat = "Derrotar %s"
QuestsCogTrackDefeatDesc = "%(numCogs)s %(trackName)s"

QuestsCogLevelQuestProgress = "%(progress)s de %(numCogs)s derrotados"
QuestsCogLevelQuestHeadline = "PROCURADO"
QuestsCogLevelQuestDefeat = "Derrotar %s"
QuestsCogLevelQuestDesc = "um N\xc3\xadvel %(level)s+ Cog"
QuestsCogLevelQuestDescC = "%(count)s N\xc3\xadvel %(level)s+ Cogs"
QuestsCogLevelQuestDescI = "algum N\xc3\xadvel %(level)s+ Cogs"
QuestsCogLevelQuestSCString = "Eu preciso derrotar %(objective)s%(location)s."

QuestsBuildingQuestFloorNumbers = ('','dois+','tr\xc3\xaas+','quatro+','cinco+')
QuestsBuildingQuestBuilding = "Edif\xc3\xadcio"
QuestsBuildingQuestBuildings = "Edif\xc3\xadcios"
QuestsBuildingQuestHeadline = "DERROTAR"
QuestsBuildingQuestProgressString = "%(progress)s de %(num)s derrotados"
QuestsBuildingQuestString = "Derrotar %s"
QuestsBuildingQuestSCString = "Eu preciso derrotar %(objective)s%(location)s."

QuestsBuildingQuestDesc = "um Edif\xc3\xadcio %(type)s"
QuestsBuildingQuestDescF = "um Edif\xc3\xadcio %(type)s de %(floors)s andares"
QuestsBuildingQuestDescC = "%(count)s Edif\xc3\xadcios %(type)s"
QuestsBuildingQuestDescCF = "%(count)s Edif\xc3\xadcios %(type)s de %(floors)s andares"
QuestsBuildingQuestDescI = "alguns Edif\xc3\xadcios %(type)s"
QuestsBuildingQuestDescIF = "alguns Edif\xc3\xadcios %(type)s de %(floors)s andares"

QuestFactoryQuestFactory = "Fábrica"
QuestsFactoryQuestFactories = "Fábricas"
QuestsFactoryQuestHeadline = "DERROTAR"
QuestsFactoryQuestProgressString = "%(progress)s de %(num)s derrotados"
QuestsFactoryQuestString = "Derrotar %s"
QuestsFactoryQuestSCString = "Eu preciso derrotar %(objective)s%(location)s."

QuestsFactoryQuestDesc = "uma Fábrica %(type)s"
QuestsFactoryQuestDescC = "%(count)s Fábricas %(type)s"
QuestsFactoryQuestDescI = "algumas Fábricas %(type)s"

QuestMintQuestMint = "Casa da Moeda"
QuestsMintQuestMints = "Casas da Moeda"
QuestsMintQuestHeadline = "DERROTAR"
QuestsMintQuestProgressString = "%(progress)s de %(num)s derrotados"
QuestsMintQuestString = "Derrotar %s"
QuestsMintQuestSCString = "Preciso derrotar %(objective)s%(location)s."

QuestsMintQuestDesc = "uma Casa da Moeda dos Cogs"
QuestsMintQuestDescC = "%(count)s Casas da Moeda dos Cogs"
QuestsMintQuestDescI = "algumas Casas da Moeda dos Cogs"

QuestsRescueQuestProgress = "%(progress)s de %(numToons)s salvos"
QuestsRescueQuestHeadline = "SALVAMENTO"
QuestsRescueQuestSCStringS = "Preciso salvar um Toon%(toonLoc)s."
QuestsRescueQuestSCStringP = "Preciso salvar alguns Toons%(toonLoc)s."
QuestsRescueQuestRescue = "Salvar %s"
QuestsRescueQuestRescueDesc = "%(numToons)s Toons"
QuestsRescueQuestToonS = "um Toon"
QuestsRescueQuestToonP = "Toons"
QuestsRescueQuestAux = "Salvar:"

QuestsRescueNewNewbieQuestObjective = "Ajudar um novo Toon a salvar %s"
QuestsRescueOldNewbieQuestObjective = "Ajude um Toon com %(laffPoints)de risadas, ou menos, a resgatar %(objective)s"

QuestCogPartQuestCogPart = "Parte do Processo Cog"
QuestsCogPartQuestFactories = "Fábricas"
QuestsCogPartQuestHeadline = "RECUPERAR"
QuestsCogPartQuestProgressString = "%(progress)s de %(num)s recuperados"
QuestsCogPartQuestString = "Recuperar %s"
QuestsCogPartQuestSCString = "Preciso recuperar %(objective)s%(location)s."
QuestsCogPartQuestAux = "Recuperar:"

QuestsCogPartQuestDesc = "uma Parte do Processo Cog"
QuestsCogPartQuestDescC = "%(count)s Parte(s) do Processo Cog"
QuestsCogPartQuestDescI = "algumas Partes do Processo Cog"

QuestsCogPartNewNewbieQuestObjective = "Ajude um novo Toon a recuperar %s"
QuestsCogPartOldNewbieQuestObjective = 'Ajude um Toon com %(laffPoints)de risadas, ou menos, a recuperar %(objective)s'

QuestsDeliverGagQuestProgress = "%(progress)s de %(numGags)s entregues"
QuestsDeliverGagQuestHeadline = "ENTREGAR"
QuestsDeliverGagQuestToSCStringS = "Preciso entregar %(gagName)s."
QuestsDeliverGagQuestToSCStringP = "Preciso entregar algumas %(gagName)s."
QuestsDeliverGagQuestSCString = "Preciso fazer uma entrega."
QuestsDeliverGagQuestString = "Entregar %s"
QuestsDeliverGagQuestStringLong = "Entregar %s a _toNpcName_."
QuestsDeliverGagQuestInstructions = "Voc\xc3\xaa pode comprar esta piada na Loja de Piadas quando tiver acesso a ela."

QuestsDeliverItemQuestProgress = ""
QuestsDeliverItemQuestHeadline = "ENTREGAR"
QuestsDeliverItemQuestSCString = "Preciso entregar %(article)s%(itemName)s."
QuestsDeliverItemQuestString = "Entregar %s"
QuestsDeliverItemQuestStringLong = "Entregar %s a _toNpcName_."

QuestsVisitQuestProgress = ""
QuestsVisitQuestHeadline = "VISITAR"
QuestsVisitQuestStringShort = "Visitar"
QuestsVisitQuestStringLong = "Visitar _toNpcName_"
QuestsVisitQuestSeeSCString = "Preciso ver %s."

QuestsRecoverItemQuestProgress = "%(progress)s de %(numItems)s recuperados"
QuestsRecoverItemQuestHeadline = "RECUPERAR"
QuestsRecoverItemQuestSeeHQSCString = "Preciso ver um "+lHQOfficerM+"."
QuestsRecoverItemQuestReturnToHQSCString = "Preciso devolver %s para um "+lHQOfficerM+"."
QuestsRecoverItemQuestReturnToSCString = "Preciso devolver %(item)s para %(npcName)s."
QuestsRecoverItemQuestGoToHQSCString = "Preciso ir a um Quartel dos Toons."
QuestsRecoverItemQuestGoToPlaygroundSCString = "Preciso ir ao Pátio %s."
QuestsRecoverItemQuestGoToStreetSCString = "Preciso ir %(to)s %(street)s em %(hood)s."
QuestsRecoverItemQuestVisitBuildingSCString = "Preciso visitar %s%s."
QuestsRecoverItemQuestWhereIsBuildingSCString = "Onde é %s%s?"
QuestsRecoverItemQuestRecoverFromSCString = "Preciso recuperar %(item)s de %(holder)s%(loc)s."
QuestsRecoverItemQuestString = "Recuperar %(item)s de %(holder)s"
QuestsRecoverItemQuestHolderString = "%(level)s %(holder)d+ %(cogs)s"

QuestsTrackChoiceQuestHeadline = "ESCOLHER"
QuestsTrackChoiceQuestSCString = "Preciso escolher entre %(trackA)s e %(trackB)s."
QuestsTrackChoiceQuestMaybeSCString = "Talvez eu deva escolher %s."
QuestsTrackChoiceQuestString = "Escolha entre %(trackA)s e %(trackB)s"

QuestsFriendQuestHeadline = "AMIGO"
QuestsFriendQuestSCString = "Preciso fazer um amigo."
QuestsFriendQuestString = "Fazer um amigo"

QuestsMailboxQuestHeadline = "CORRESPOND\xc3\x8aNCIA"
QuestsMailboxQuestSCString = "Preciso verificar minha correspond\xc3\xaancia."
QuestsMailboxQuestString = "Verificar sua correspond\xc3\xaancia"

QuestsPhoneQuestHeadline = "CLARABELA"
QuestsPhoneQuestSCString = "Preciso ligar para Clarabela."
QuestsPhoneQuestString = "Ligar para Clarabela"

QuestsFriendNewbieQuestString = "Faça %d amigos %d risadas ou menos"
QuestsFriendNewbieQuestProgress = "%(progress)s de %(numFriends)s feitos"
QuestsFriendNewbieQuestObjective = "Faça amizade com %d novos Toons"

QuestsTrolleyQuestHeadline = "BONDINHO"
QuestsTrolleyQuestSCString = "Preciso pegar o bondinho."
QuestsTrolleyQuestString = "Andar no bondinho"
QuestsTrolleyQuestStringShort = "Pegar o bondinho"

QuestsMinigameNewbieQuestString = "%d Minijogos"
QuestsMinigameNewbieQuestProgress = "%(progress)s de %(numMinigames)s jogados"
QuestsMinigameNewbieQuestObjective = "Divirta-se com %d minijogos com a ajuda de novos Toons"
QuestsMinigameNewbieQuestSCString = "Preciso participar de minijogos com novos Toons."
QuestsMinigameNewbieQuestCaption = "Ajude um novo Toon %d risadas ou menos"
QuestsMinigameNewbieQuestAux = "Jogar:"

QuestsMaxHpReward = "Seu Limite de risadas foi aumentado em %s."
QuestsMaxHpRewardPoster = "Recompensa: %s ponto de Acréscimo de risadas"

QuestsMoneyRewardSingular = "Voc\xc3\xaa ganha 1 balinha."
QuestsMoneyRewardPlural = "Voc\xc3\xaa ganha %s balinhas."
QuestsMoneyRewardPosterSingular = "Recompensa: 1 balinha"
QuestsMoneyRewardPosterPlural = "Recompensa: %s balinhas"

QuestsMaxMoneyRewardSingular = "Agora, voc\xc3\xaa pode carregar 1 balinha."
QuestsMaxMoneyRewardPlural = "Agora, voc\xc3\xaa pode carregar %s balinhas."
QuestsMaxMoneyRewardPosterSingular = "Recompensa: Carregue 1 balinha"
QuestsMaxMoneyRewardPosterPlural = "Recompensa: Carregue %s balinhas"

QuestsMaxGagCarryReward = "Voc\xc3\xaa ganha %(name)s. Agora, voc\xc3\xaa pode carregar %(num)s piadas."
QuestsMaxGagCarryRewardPoster = "Recompensa: %(name)s (%(num)s)"

QuestsMaxQuestCarryReward = "Agora, voc\xc3\xaa pode ter %s Tarefas Toon."
QuestsMaxQuestCarryRewardPoster = "Recompensa: Carregue %s Tarefas Toon"

QuestsTeleportReward = "Agora, voc\xc3\xaa tem acesso por teletransporte a %s."
QuestsTeleportRewardPoster = "Recompensa: Acesso por teletransporte a %s"

QuestsTrackTrainingReward = "Agora, voc\xc3\xaa pode treinar para \"%s\" piadas."
QuestsTrackTrainingRewardPoster = "Recompensa: Treinamento de piadas"

QuestsTrackProgressReward = "Agora, voc\xc3\xaa tem o quadro %(frameNum)s da animação do tipo %(trackName)s."
QuestsTrackProgressRewardPoster = "Recompensa: \"Quadro %(frameNum)s da animação do tipo %(trackName)s\""

QuestsTrackCompleteReward = "Agora, voc\xc3\xaa pode carregar e usar \"%s\" piadas."
QuestsTrackCompleteRewardPoster = "Recompensa: Treinamento final do tipo %s"

QuestsClothingTicketReward = "Voc\xc3\xaa pode trocar de roupa"
QuestsClothingTicketRewardPoster = "Recompensa: Bilhete de roupas"

TIPQuestsClothingTicketReward = "Voc\xc3\xaa pode trocar sua camisa por uma camisa DICA"
TIPQuestsClothingTicketRewardPoster = "Recompensa: Bilhete de Roupa DICA"

QuestsCheesyEffectRewardPoster = "Recompensa: %s"

QuestsCogSuitPartReward = "Agora, voc\xc3\xaa tem uma %(cogTrack)s %(part)s peça de vestimenta de Cog."
QuestsCogSuitPartRewardPoster = "Recompensa: %(cogTrack)s %(part)s Peça"

# Quest location dialog text
QuestsStreetLocationThisPlayground = "neste pátio"
QuestsStreetLocationThisStreet = "nesta rua"
QuestsStreetLocationNamedPlayground = "no pátio %s"
QuestsStreetLocationNamedStreet = "na %(toStreetName)s em %(toHoodName)s"
QuestsLocationString = "%(string)s%(location)s"
QuestsLocationBuilding = "O edif\xc3\xadcio de %s's chama-se"
QuestsLocationBuildingVerb = "o qual é"
QuestsLocationParagraph = "\a%(building)s \"%(buildingName)s\"...\a...%(buildingVerb)s %(street)s."
QuestsGenericFinishSCString = "Preciso terminar uma Tarefa Toon."

# MaxGagCarryReward names
QuestsMediumPouch = "Sacola média"
QuestsLargePouch = "Sacola grande"
QuestsSmallBag = "Bolsa pequena"
QuestsMediumBag = "Bolsa média"
QuestsLargeBag = "Bolsa grande"
QuestsSmallBackpack = "Mochila pequena"
QuestsMediumBackpack = "Mochila média"
QuestsLargeBackpack = "Mochila grande"
QuestsItemDict = {
    1 : ["Par de óculos", "Pares de óculos", "um "],
    2 : ["Chave", "Chaves", "uma "],
    3 : ["Quadro-negro", "Quadros-negros", "um "],
    4 : ["Livro", "Livros", "um "],
    5 : ["Chocolate", "Chocolates", "um "],
    6 : ["Pedaço de giz", "Pedaços de giz", "um "],
    7 : ["Receita", "Receitas", "uma "],
    8 : ["Nota", "Notas", "uma "],
    9 : ["Calculadora", "Calculadoras", "uma "],
    10 : ["Pneu de carro de palhaço", "Pneus de carro de palhaço", "um "],
    11 : ["Bomba de ar", "Bombas de ar", "uma "],
    12 : ["Tinta de polvo", "Tintas de polvo", "uma "],
    13 : ["Pacotes", "Pacotes", "um "],
    14 : ["Recibo de peixe dourado", "Recibos de peixe dourado", "um "],
    15 : ["Peixe dourado", "Peixe dourado", "um "],
    16 : ["\xc3\x93leo", "\xc3\x93leos", "um pouco de "],
    17 : ["Graxa", "Graxas", "um pouco de "],
    18 : ["\xc3\x81gua", "\xc3\x81guas", "uma "],
    19 : ["Relatório de engrenagens", "Relatórios de engrenagens", "um "],
    20 : ["Apagador de quadro-negro", "Apagadores de quadro-negro", "a "],

    # This is meant to be delivered to NPCTailors to complete
    # ClothingReward quests
    110 : ["Bilhete de Roupa DICA", "Bilhetes de Roupa", "um"],
    1000 : ["Bilhete de roupas", "Bilhetes de roupas", "um "],

    # Donald's Dock quest items
    2001 : ["Câmara de ar", "Câmaras de ar", "uma "],
    2002 : ["Receita de monóculo", "Receita de monóculo", "uma "],
    2003 : ["Armação de óculos", "Armações de óculos", "algumas "],
    2004 : ["Monóculo", "Monóculos", "um "],
    2005 : ["Grande peruca branca", "Grandes perucas brancas", "uma "],
    2006 : ["Alqueire de cascalho", "Alqueires de cascalho", "um "],
    2007 : ["Engrenagem Cog", "Engrenagens de Cog", "uma "],
    2008 : ["Carta marinha", "Cartas marinhas", "uma "],
    2009 : ["Braçadeira suja", "Braçadeiras sujas", "uma "],
    2010 : ["Braçadeira limpa", "Braçadeiras limpas", "uma "],
    2011 : ["Mola de relógio", "Molas de relógio", "uma "],
    2012 : ["Contrapeso", "Contrapesos", "um "],

    # Minnie's Melodyland quest items
    4001 : ["Estoque da Tina", "Estoques da Tina", ""],
    4002 : ["Estoque da Cavaca", "Estoques da Cavaca", ""],
    4003 : ["Formulário de estoque", "Formulários de estoque", "um "],
    4004 : ["Estoque da Fifi", "Estoques da Fifi", ""],
    4005 : ["Passagem do Al\xc3\xaa Nhador", "Passagens do Al\xc3\xaa Nhador", ""],
    4006 : ["Passagem da Tábata", "Passagens da Tábata", ""],
    4007 : ["Passagem do Barry", "Passagens do Barry", ""],
    4008 : ["Castanhola fosca", "Castanholas foscas", ""],
    4009 : ["Tinta de lula azul", "Tintas de lula azul", "obter "],
    4010 : ["Castanhola polida", "Castanholas polidas", "uma "],
    4011 : ["Letra de música do Léo", "Letras de músicas do Léo", ""],

    # Daisy's Gardens quest items
    5001 : ["Gravata de seda", "Gravatas de seda", "uma "],
    5002 : ["Terno listrado", "Ternos listrados", "um "],
    5003 : ["Tesoura", "Tesouras", "uma "],
    5004 : ["Cartão-postal", "Cartões-postais", "um "],
    5005 : ["Caneta", "Canetas", "uma "],
    5006 : ["Tinteiro", "Tinteiros", "um "],
    5007 : ["Bloco de notas", "Blocos de notas", "um "],
    5008 : ["Cofre de escritório", "Cofres de escritório", "um "],
    5009 : ["Saco de ração para pássaros", "Sacos de ração para pássaros", "um "],
    5010 : ["Roda dentada", "Rodas dentadas", "uma "],
    5011 : ["Salada", "Saladas", "uma "],
    5012 : ["Chave para os Jardins da Margarida", "Chaves para os Jardins da Margarida", "uma "],
    5013 : ["Mapa do "+lSellbotHQ, "Mapas do "+lSellbotHQ, "alguns "],
    5014 : ["Memorando do "+lSellbotHQ, "Memorandos do "+lSellbotHQ, "um "],
    5015 : ["Memorando do "+lSellbotHQ, "Memorandos do "+lSellbotHQ, "um "],
    5016 : ["Memorando do "+lSellbotHQ, "Memorandos do "+lSellbotHQ, "um "],
    5017 : ["Memorando do "+lSellbotHQ, "Memorandos do "+lSellbotHQ, "um "],

    # The Brrrgh quests
    3001 : ["Bola de futebol", "Bolas de futebol", "uma "],
    3002 : ["Tobogã", "Tobogãs", "um "],
    3003 : ["Cubo de gelo", "Cubos de gelo", "um "],
    3004 : ["Carta de amor", "Cartas de amor", "uma "],
    3005 : ["Cão-linguiça", "cães-linguiça", "um "],
    3006 : ["Anel de noivado", "Anéis de noivado", "um "],
    3007 : ["Bigode de sardinha", "Bigodes de sardinhas", "um pouco de "],
    3008 : ["Poção calmante", "Poções calmantes", "uma "],
    3009 : ["Dente quebrado", "Dentes quebrados", "um "],
    3010 : ["Dente de ouro", "Dentes de ouro", "um "],
    3011 : ["Pão de pinha", "Pães de pinha", "um "],
    3012 : ["Coco em pedaços", "Cocos em pedaços", "um pouco de "],
    3013 : ["Colher simples", "Colheres simples", "uma "],
    3014 : ["Sapo falante", "Sapos falantes", "um "],
    3015 : ["Casquinha de sorvete", "Casquinhas de sorvete", "uma "],
    3016 : ["Pó de peruca", "Pós de perucas", "um pouco de "],
    3017 : ["Patinho de borracha", "Patinhos de borracha", "um "],
    3018 : ["Dados de pelúcia", "Dados de pelúcia", "alguns "],
    3019 : ["Microfone", "Microfones", "um "],
    3020 : ["Teclado elétrico", "Teclados elétricos", "um "],
    3021 : ["Sapatos de plataforma", "Sapatos de plataforma", "alguns "],
    3022 : ["Caviar", "Caviar", "um pouco de "],
    3023 : ["Pó de arroz", "Pó de arroz", "um pouco de "],
    3024 : ["Fio", "Fios", "alguns " ],
    3025 : ["Agulha de Tricô", "Agulhas de Tricô", "uma "],
    3026 : ["\xc3\x81libi", "\xc3\x81libis", "um "],
    3027 : ["Termômetro Externo", "Termômetros Externos", "um "],

    #Dreamland Quests
    6001 : ["Plano do Quartel do Robô Mercenário", "Planos do Quartel do Robô Mercenário", "algum "],
    6002 : ["Vara de pescar", "Varas de pescar", "uma "],
    6003 : ["Cinto de segurança", "Cintos de segurança", "um "],
    6004 : ["Par de pinças", "Pares de pinças", "um "],
    6005 : ["Abajur de leitura", "Abajures de leitura", "um "],
    6006 : ["C\xc3\xadtara", "C\xc3\xadtaras", "uma "],
    6007 : ["Zamboni", "Zambonis", "uma "],
    6008 : ["Zabuton de zebra", "Zabutons de zebra", "uma "],
    6009 : ["Zinnias", "Zinnias", "alguns "],
    6010 : ["Discos de forró", "Discos de forró", "algum "],
    6011 : ["Abobrinha", "Abobrinhas", "uma "],
    6012 : ["Paletó zoot", "Paletós zoot", "um "],

    #Dreamland+1 quests
    7001 : ["Cama comum", "Camas comuns", "uma "],
    7002 : ["Cama elegante", "Camas elegantes", "uma "],
    7003 : ["Colcha azul", "Colchas azuis", "uma "],
    7004 : ["Colcha estampada", "Colchas estampadas ", "uma"],
    7005 : ["Travesseiros", "Travesseiros", "alguns "],
    7006 : ["Travesseiros duros", "Travesseiros duros ", "um"],
    7007 : ["Pijamas", "Pijamas", "um par de "],
    7008 : ["Pijamas com pés", "Pijamas com pés", "um par de "],
    7009 : ["Pijamas com pés marrons", "Pijamas com pés marrons", "um par de "],
    7010 : ["Pijamas com pés fúcsia", "Pijamas com pés fúcsia", "um par de "],
    7011 : ["Coral de couve-flor", "Coral de couve-flor", "algumas "],
    7012 : ["Alga-marinha viscosa", "Alga-marinha viscosa", "um "],
    7013 : ["Pilão", "Pilões", "um "],
    7014 : ["Pote de creme para rugas", "Potes de creme para rugas", "um "],
    }

QuestsHQOfficerFillin = lHQOfficerM
QuestsHQWhereFillin = ""
QuestsHQBuildingNameFillin = lToonHQ
QuestsHQLocationNameFillin = "em qualquer bairro"

QuestsTailorFillin = "Costureiro"
QuestsTailorWhereFillin = ""
QuestsTailorBuildingNameFillin = "Loja de Roupas"
QuestsTailorLocationNameFillin = "em qualquer bairro"
QuestsTailorQuestSCString = "Preciso ir ao Costureiro."

QuestMovieQuestChoiceCancel = "Volte mais tarde se precisar de uma Tarefa Toon! Tchau!"
QuestMovieTrackChoiceCancel = "Volte quando já tiver decidido o que fazer! Tchau!"
QuestMovieQuestChoice = "Escolha uma Tarefa Toon."
QuestMovieTrackChoice = "Já decidiu o que escolher? Escolha um tipo ou volte mais tarde."

# Constants used in Quests.py, globally defined here
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6

TheBrrrghTrackQuestDict = {
    GREETING : "",
    QUEST : "Agora, voc\xc3\xaa está pronto.\aSaia e refresque a cabeça até descobrir que tipo voc\xc3\xaa gostaria de escolher.\aEscolha bem, pois voc\xc3\xaa não poderá mudar.\aQuando tiver certeza, volte aqui.",
    INCOMPLETE_PROGRESS : "Escolha bem.",
    INCOMPLETE_WRONG_NPC : "Escolha bem.",
    COMPLETE : "\xc3\x93tima escolha!",
    LEAVING : "Boa sorte. Volte aqui quando tiver dominado sua nova habilidade.",
    }

QuestDialog_3225 = {
    QUEST : "Puxa, obrigado por vir, _avName_!\aOs Cogs que estão no bairro assustaram o rapaz que faz as entregas.\aEu não tenho quem entregue esta salada para _toNpcName_!\aVoc\xc3\xaa poderia fazer isso por mim? Muit\xc3\xadssimo obrigado!_where_"
    }

QuestDialog_2910 = {
    QUEST : "De volta tão rápido assim?\a\xc3\x93timo trabalho com aquela mola.\aO último item é um contrapeso.\aPasse lá, veja com _toNpcName_ e traga o que voc\xc3\xaa conseguir._where_"
    }

QuestDialogDict = {
    160 : {GREETING : "",
           QUEST : "Ok, agora acho que voc\xc3\xaa está pronto para um desafio maior.\aDerrote 3 Robôs-chefe.",
           INCOMPLETE_PROGRESS : "Os "+ Cogs +" estão soltos pelas ruas e pelos túneis.",
           INCOMPLETE_WRONG_NPC : "Bom trabalho com os Robôs-chefe. Vá agora para o Quartel dos Toons para receber sua recompensa!",
           COMPLETE : QuestsDefaultComplete,
           LEAVING : QuestsDefaultLeaving,
           },
    161 : {GREETING : "",
           QUEST : "Ok, agora acho que voc\xc3\xaa está pronto para um desafio maior.\aDerrote 3 Robôs da Lei.",
           INCOMPLETE_PROGRESS : "Os "+ Cogs +" estão soltos pelas rua e pelos túneis.",
           INCOMPLETE_WRONG_NPC : "Bom trabalho com os Robôs da Lei. Vá agora para o Quartel dos Toons para receber sua recompensa!",
           COMPLETE : QuestsDefaultComplete,
           LEAVING : QuestsDefaultLeaving,
           },
    162 : {GREETING : "",
           QUEST : "Ok, agora acho que voc\xc3\xaa está pronto para um desafio maior.\aDerrote 3 Robôs Mercenários.",
           INCOMPLETE_PROGRESS : "Os "+ Cogs +" estão soltos pelas ruas e pelos túneis.",
           INCOMPLETE_WRONG_NPC : "Bom trabalho com os Robôs Mercenários. Vá agora para o Quartel dos Toons para receber sua recompensa!",
           COMPLETE : QuestsDefaultComplete,
           LEAVING : QuestsDefaultLeaving,
           },
    163 : {GREETING : "",
           QUEST : "Ok, agora acho que voc\xc3\xaa está pronto para um desafio maior.\aDerrote 3 Robôs Vendedores.",
           INCOMPLETE_PROGRESS : "Os "+ Cogs +" estão soltos pelas ruas e pelos túneis.",
           INCOMPLETE_WRONG_NPC : "Bom trabalho com os Robôs Vendedores. Vá agora para o Quartel dos Toons para receber sua recompensa!",
           COMPLETE : QuestsDefaultComplete,
           LEAVING : QuestsDefaultLeaving,
           },
    164 : {QUEST : "Parece que voc\xc3\xaa precisa de novas piadas.\aVisite o Flippy, talvez ele possa ajudá-lo._where_" },
    165 : {QUEST : "Olá.\aParece que voc\xc3\xaa precisa praticar suas piadas.\aToda vez que voc\xc3\xaa atinge um Cog com uma de suas piadas, sua experi\xc3\xaancia aumenta.\aQuando tiver experi\xc3\xaancia suficiente, voc\xc3\xaa será capaz de usar uma piada ainda melhor.\aVá praticar suas piadas derrotando 4 Cogs."},
    166 : {QUEST : "Bom trabalho com aqueles Cogs.\aSabia que existem quatro tipos diferentes de Cogs?\aEles são os Robôs da Lei, os Robôs Mercenários, os Robôs Vendedores e os Robôs-chefe.\aVoc\xc3\xaa pode diferenciá-los pela cor e pelas etiquetas com os nomes.\aPara praticar, derrote 4 Robôs-chefe."},
    167 : {QUEST : "Bom trabalho com aqueles Cogs.\aSabia que existem quatro tipos diferentes de Cogs?\aEles são os Robôs da Lei, os Robôs Mercenários, os Robôs Vendedores e os Robôs-chefe.\aVoc\xc3\xaa pode diferenciá-los pela cor e pelas etiquetas com os nomes.\aPara praticar, derrote 4 Robôs da Lei."},
    168 : {QUEST : "Bom trabalho com aqueles Cogs.\aSabia que existem quatro tipos diferentes de Cogs?\aEles são os Robôs da Lei, os Robôs Mercenários, os Robôs Vendedores e os Robôs-chefe.\aVoc\xc3\xaa pode diferenciá-los pela cor e pelas etiquetas com os nomes.\aPara praticar, derrote 4 Robôs Vendedores."},
    169 : {QUEST : "Bom trabalho com aqueles Cogs.\aSabia que existem quatro tipos diferentes de Cogs?\aEles são os Robôs da Lei, os Robôs Mercenários, os Robôs Vendedores e os Robôs-chefe.\aVoc\xc3\xaa pode diferenciá-los pela cor e pelas etiquetas com os nomes.\aPara praticar, derrote 4 Robôs Mercenários."},
    170 : {QUEST : "Bom trabalho; agora voc\xc3\xaa sabe a diferença entre os 4 tipos de Cogs.\aAcho que voc\xc3\xaa está pronto para começar a treinar o seu terceiro tipo de piada.\aFale com _toNpcName_ para escolher o seu próximo tipo de piada - ele pode dar alguns conselhos especiais para voc\xc3\xaa._where_" },
    171 : {QUEST : "Bom trabalho; agora voc\xc3\xaa sabe a diferença entre os 4 tipos de Cogs.\aAcho que voc\xc3\xaa está pronto para começar a treinar o seu terceiro tipo de piada.\aFale com _toNpcName_ para escolher o seu próximo tipo de piada - ele pode dar alguns conselhos especiais para voc\xc3\xaa._where_" },
    172 : {QUEST : "Bom trabalho; agora voc\xc3\xaa sabe a diferença entre os 4 tipos de Cogs.\aAcho que voc\xc3\xaa está pronto para começar a treinar o seu terceiro tipo de piada.\aFale com _toNpcName_ para escolher o seu próximo tipo de piada - ela pode dar alguns conselhos especiais para voc\xc3\xaa._where_" },

    175 : {GREETING : "",
           QUEST : "Voc\xc3\xaa sabia que possui sua própria casa Toon?\aA vaca Clarabela administra um catálogo telefônico no qual voc\xc3\xaa pode escolher e encomendar móveis para decorar sua casa.\aVoc\xc3\xaa também pode comprar frases do Chat Rápido, roupas e outras coisas muito legais!\aPedirei \xc3\xa0 Clarabela para enviar agora a voc\xc3\xaa seu primeiro catálogo.\aVoc\xc3\xaa receberá um catálogo com novos itens toda semana!\aVá para sua casa e use o seu telefone para ligar para Clarabela.",
           INCOMPLETE_PROGRESS : "Vá para casa e use o seu telefone para ligar para Clarabela.",
           COMPLETE : "Espero que voc\xc3\xaa se divirta fazendo encomendas com Clarabela!\a Acabei de redecorar minha casa. Está Toontástica!\aContinue com as Tarefas Toon para ganhar mais recompensas!",
           LEAVING : QuestsDefaultLeaving,
           },

    400 : {GREETING : "",
           QUEST : "Lançamento e Esguicho são tipos ótimos, mas voc\xc3\xaa vai precisar de mais piadas para lutar com Cogs de n\xc3\xadveis mais altos.\aQuando voc\xc3\xaa se juntar com outros Toons para enfrentar os Cogs, pode combinar ataques para conseguir danos maiores ao inimigo.\aTente diferentes combinações de Piadas para ver o que funciona melhor.\aPara o seu próximo tipo, escolha as Sonoras ou Toonar.\aAs Sonoras são especiais, pois quando atingem algum Cog, todos os outros também sofrem danos.\aAs Toonar permitem curar outros Toons durante a batalha.\aQuando estiver pronto para decidir, venha aqui e escolha uma.",
           INCOMPLETE_PROGRESS : "De volta tão rápido? Ok, voc\xc3\xaa está pronto para escolher?",
           INCOMPLETE_WRONG_NPC : "Pense bem sobre sua decisão antes de escolher.",
           COMPLETE : "Boa decisão. Agora, antes de usar estas piadas, voc\xc3\xaa deve treinar.\aVoc\xc3\xaa deve completar uma série de Tarefas Toon como treinamento.\aCada tarefa dará a voc\xc3\xaa um único quadro da animação do seu ataque de piadas.\aQuando voc\xc3\xaa coletar todas as 15, poderá obter a tarefa Treinamento final de piadas, que lhe permitirá usar suas novas piadas.\aVoc\xc3\xaa pode verificar seu progresso no \xc3\x81lbum Toon.",
           LEAVING : QuestsDefaultLeaving,
           },
    1039 : { QUEST : "Visite _toNpcName_ se desejar transitar pela cidade com mais facilidade._where_" },
    1040 : { QUEST : "Visite _toNpcName_ se desejar transitar pela cidade com mais facilidade._where_" },
    1041 : { QUEST : "Oi! O que o traz aqui?\aTodo mundo usa o buraco portátil para andar por Toontown.\a\xc3\x89, voc\xc3\xaa pode se teletransportar até seus amigos, usando a Lista de amigos, ou até qualquer bairro, usando o mapa no \xc3\x81lbum Toon.\a\xc3\x89 claro que voc\xc3\xaa precisa consegui-lo!\aOlha, eu posso ativar seu acesso por teletransporte até o Centro de Toontown se voc\xc3\xaa ajudar um amigo meu.\aParece que os Cogs estão dando problema na Travessa dos Tontos. Visite _toNpcName_._where_" },
    1042 : { QUEST : "Oi! O que o traz aqui?\aTodo mundo usa o buraco portátil para andar por Toontown.\a\xc3\x89, voc\xc3\xaa pode se teletransportar até seus amigos, usando a Lista de amigos, ou até qualquer bairro, usando o mapa no \xc3\x81lbum Toon.\a\xc3\x89 claro que voc\xc3\xaa precisa consegui-lo!\aOlha, eu posso ativar seu acesso por teletransporte até o Centro de Toontown se voc\xc3\xaa ajudar um amigo meu.\aParece que os Cogs estão dando problema na Travessa dos Tontos. Visite _toNpcName_._where_" },
    1043 : { QUEST : "Oi! O que o traz aqui?\aTodo mundo usa o buraco portátil para andar por Toontown.\a\xc3\x89, voc\xc3\xaa pode se teletransportar até seus amigos, usando a Lista de amigos, ou até qualquer bairro, usando o mapa no \xc3\x81lbum Toon.\a\xc3\x89 claro que voc\xc3\xaa precisa consegui-lo!\aOlha, eu posso ativar seu acesso por teletransporte até o Centro de Toontown se voc\xc3\xaa ajudar um amigo meu.\aParece que os Cogs estão dando problema na Travessa dos Tontos. Visite _toNpcName_._where_" },
    1044 : { QUEST : "Puxa, obrigado por passar por aqui. Eu realmente preciso de ajuda.\aComo voc\xc3\xaa pode ver, eu não tenho clientes.\aO meu livro de receitas secreto está perdido e ninguém mais vem ao meu restaurante.\aA última vez que eu o vi foi pouco antes de os Cogs tomarem meu edif\xc3\xadcio.\aVoc\xc3\xaa pode me ajudar recuperando quatro de minhas receitas favoritas?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Conseguiu recuperar minhas receitas?" },
    1045 : { QUEST : "Valeu mesmo!\aLogo terei de volta minha coleção completa e poderei reabrir meu restaurante.\aAh, há uma nota aqui para voc\xc3\xaa - algo sobre acesso por teletransporte?\aDiz: \"obrigado por ajudar meu amigo e, por favor, entregue isto ao Quartel dos Toons\".\aBem, valeu mesmo - tchau!",
             LEAVING : "",
             COMPLETE : "Ah, sim, aqui diz que voc\xc3\xaa foi de grande ajuda para alguns dos caras mais legais da Travessa dos Tontos.\aDiz também que voc\xc3\xaa precisa de acesso por teletransporte para o Centro de Toontown.\aBem, considere concedido.\aAgora, voc\xc3\xaa pode se teletransportar de volta para o pátio, de praticamente qualquer lugar de Toontown.\aBasta abrir o seu mapa e clicar em Centro de Toontown." },
    1046 : { QUEST : "Os Robôs Mercenários t\xc3\xaam importunado bastante a Financeira Dinheiro Feliz.\aPasse por lá e veja se há algo que voc\xc3\xaa possa fazer._where_" },
    1047 : { QUEST : "Os Robôs Mercenários t\xc3\xaam se infiltrado no banco e roubado nossas calculadoras.\aRecupere 5 calculadoras dos Robôs Mercenários.\aPara evitar que voc\xc3\xaa fique indo para lá e para cá, traga-as todas de uma vez.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ainda procurando pelas calculadoras?" },
    1048 : { QUEST : "Uau! Valeu mesmo por encontrar nossas calculadoras.\aHumm... Elas parecem danificadas.\aVoc\xc3\xaa poderia levá-las para a loja de _toNpcName_, \"Máquinas de Cosquinhas\", nesta rua?\aVeja se podem consertá-las.",
             LEAVING : "", },
    1049 : { QUEST : "O que é isto? Calculadoras quebradas?\aRobôs Mercenários?\aBem, vamos dar uma olhada...\a\xc3\x89, as engrenagens estão partidas mas eu estou sem essa peça...\aSabe o que poderia dar jeito? Algumas engrenagens de Cog, das grandes, dos Cogs maiores...\aEngrenagens de Cogs de n\xc3\xadvel 3 devem servir. Precisarei de 2 para cada máquina, 10 no total.\aTraga-as todas de uma vez e eu as consertarei!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Lembre-se, eu preciso de 10 engrenagens para consertar as máquinas." },
    1053 : { QUEST : "Ah sim, isto deve servir.\aTudo consertado agora, grátis.\aLeve-as de volta para a Dinheiro Feliz e diga olá a ela por mim.",
             LEAVING : "",
             COMPLETE : "Calculadoras consertadas?\aBom trabalho. Tenho certeza de que tenho algo por aqui para recompensar voc\xc3\xaa..." },
    1054 : { QUEST : "_toNpcName_ precisa de alguma ajuda com seus carros de palhaço._where_" },
    1055 : { QUEST : "Oláááá! Eu não consigo encontrar os pneus para este carro de palhaço em lugar nenhum!\aVoc\xc3\xaa acha que pode me ajudar?\aEu acho que o Tito Tonto pode ter jogado os pneus no lago do pátio do Centro de Toontown.\aSe voc\xc3\xaa ficar em um dos cais de lá, poderá tentar pescar os pneus para mim.",
             GREETING : "Iuhuu!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa está tendo problemas para pescar os 4 pneus?" },
    1056 : { QUEST : "Demorôô! Agora, este velho carro de palhaço vai poder voltar \xc3\xa0s ruas!\aEi, eu pensei que tivesse uma bomba de ar aqui para inflar estes pneus...\aAcho que _toNpcName_ pegou emprestado.\aVoc\xc3\xaa poderia pedir de volta para mim?_where_",
             LEAVING : "" },
    1057 : { QUEST : "E a\xc3\xad?\aUma bomba de pneus?\aVamos fazer o seguinte: voc\xc3\xaa me ajuda a retirar das ruas alguns desses Cogs de alto n\xc3\xadvel...\aE, então, darei a voc\xc3\xaa a bomba de pneus.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Isso é o melhor que voc\xc3\xaa pode fazer?" },
    1058 : { QUEST : "Bom trabalho! Eu sabia que voc\xc3\xaa conseguiria.\aAqui está a bomba. Estou certo de que _toNpcName_ ficará feliz em receb\xc3\xaa-la de volta.",
             LEAVING : "",
             GREETING : "",
             COMPLETE : "Dez! Agora está tudo certo!\aPor falar nisso, obrigado por me ajudar.\aAqui, tome isto." },
    1059 : { QUEST : "_toNpcName_ está com poucos suprimentos. Quem sabe voc\xc3\xaa pode ajudá-lo?_where_" },
    1060 : { QUEST : "Valeu mesmo por passar aqui!\aOs Cogs roubam sempre a minha tinta e, por isso, ela está quase no fim.\aVoc\xc3\xaa poderia pescar um pouco de tinta de polvo para mim no lago?\aPara pescar, basta ficar parado em um cais perto do lago.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa está tendo problemas para pescar?" },
    1061 : { QUEST : "\xc3\x93timo, valeu pela tinta!\aSabe de uma coisa, se voc\xc3\xaa eliminasse alguns daqueles Ratos de Escritório...\aA\xc3\xad minha tinta não acabaria tão rápido.\aDerrote 6 Ratos de Escritório no Centro de Toontown para receber sua recompensa.",
             LEAVING : "",
             COMPLETE : "Valeu! Vou recompensar voc\xc3\xaa pela sua ajuda.",
             INCOMPLETE_PROGRESS : "Eu acabei de ver mais alguns Ratos de Escritório." },
    1062 : { QUEST : "\xc3\x93timo, valeu pela tinta!\aSabe de uma coisa? Se voc\xc3\xaa eliminasse alguns daqueles Sanguessugas...\aA\xc3\xad minha tinta não acabaria tão rápido.\aDerrote 6 Sanguessugas no Centro de Toontown para receber sua recompensa.",
             LEAVING : "",
             COMPLETE : "Valeu! Vou recompensar voc\xc3\xaa pela sua ajuda.",
             INCOMPLETE_PROGRESS : "Eu acabei de ver mais alguns Sanguessugas." },
    900 : { QUEST : "Fiquei sabendo que _toNpcName_ precisa de ajuda com um pacote._where_" },
    1063 : { QUEST : "Olá! Legal voc\xc3\xaa ter vindo.\aUm Cog roubou um pacote muito importante bem debaixo do meu nariz.\aVeja se voc\xc3\xaa consegue recuperá-lo. Eu acho que ele era de n\xc3\xadvel 3...\aEntão, derrote Cogs de n\xc3\xadvel 3 até encontrar meu pacote.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não teve sorte de encontrar o pacote, né?" },
    1067 : { QUEST : "\xc3\x89 ele mesmo, está tudo certo!\aEi, o endereço está borrado...\aTudo o que eu posso ler é que é para um Dr. - o resto está ileg\xc3\xadvel.\aTalvez seja para _toNpcName_? Voc\xc3\xaa pode levar para ele?_where_",
             LEAVING : "" },
    1068 : { QUEST : "Eu não estava esperando um pacote. Talvez seja para o Dr. E.U. Fórico.\aMeu assistente ia passar mesmo lá hoje, então pedirei a ele que verifique para voc\xc3\xaa.\aNesse meio tempo, voc\xc3\xaa se importaria de se livrar de alguns dos Cogs que estão na minha rua?\aDerrote 10 Cogs no Centro de Toontown.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Meu assistente ainda não voltou." },
    1069 : { QUEST : "O Dr. Fórico disse que também não estava esperando nenhum pacote.\aInfelizmente um Robô Mercenário roubou o pacote de meu assistente no caminho de volta.\aVoc\xc3\xaa poderia tentar pegá-lo de volta?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não teve sorte de encontrar o pacote, né?" },
    1070 : { QUEST : "O Dr. Fórico disse que também não estava esperando nenhum pacote.\aInfelizmente um Robô Vendedor roubou o pacote de meu assistente no caminho de volta.\aSinto muito, mas voc\xc3\xaa terá que encontrar esse Robô Vendedor para pegá-lo de volta.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não teve sorte de encontrar o pacote, né?" },
    1071 : { QUEST : "O Dr. Fórico disse que também não estava esperando nenhum pacote.\aInfelizmente um Robô-chefe roubou o pacote de meu assistente no caminho de volta.\aVoc\xc3\xaa poderia tentar pegá-lo de volta?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não teve sorte de encontrar o pacote, né?" },
    1072 : { QUEST : "\xc3\x93timo, voc\xc3\xaa o pegou de volta!\aTalvez voc\xc3\xaa deva tentar entregá-lo a _toNpcName_, pode ser para ele._where_",
             LEAVING : "" },
    1073 : { QUEST : "Puxa, obrigado por trazer meus pacotes para mim.\aEspere um segundo, eu estava esperando dois. Voc\xc3\xaa poderia verificar com _toNpcName_ e ver se ele está com o outro?",
             INCOMPLETE : "Conseguiu encontrar meu outro pacote?",
             LEAVING : "" },
    1074 : { QUEST : "Ele disse que havia outro pacote? Talvez os Cogs o tenham roubado também.\aDerrote Cogs até encontrar o segundo pacote.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não teve sorte de encontrar o outro pacote, né?" },
    1075 : { QUEST : "No final das contas, acho que não havia um segundo pacote!\aCorra e leve-o para _toNpcName_, com minhas desculpas.",
             COMPLETE : "Ei, meu pacote está aqui!\aJá que voc\xc3\xaa parece ser um Toon tão prestativo, isto vai ser fichinha.",
             LEAVING : "" },
    1076 : { QUEST : "Houve alguns problemas na Peixinhos Dourados Ki-late.\a_toNpcName_ provavelmente podem precisar de voc\xc3\xaa._where_" },
    1077 : { QUEST : "Legal voc\xc3\xaa ter vindo. Os Cogs roubaram todos os meus peixes dourados.\aEu acho que os Cogs querem vend\xc3\xaa-los para ganhar dinheiro fácil.\aHá muitos anos, aqueles 5 peixes t\xc3\xaam sido minhas únicas companhias nesta pequena loja ...\aSe voc\xc3\xaa pudesse recuperá-los, eu agradeceria muito.\aTenho certeza de que os Cogs estão com meus peixes.\aDerrote Cogs até encontrar meus peixes dourados.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Consiga meus peixes dourados de volta." },
    1078 : { QUEST : "Puxa, voc\xc3\xaa recuperou meus peixes!\aHã? O que é isto - um recibo?\aAi, ai... Acho que eles são Cogs mesmo.\aEu não consigo decifrar este recibo. Voc\xc3\xaa poderia levá-lo para _toNpcName_ e ver se ele consegue l\xc3\xaa-lo?_where_",
             INCOMPLETE : "O que _toNpcName_ disse sobre o recibo?",
             LEAVING : "" },
    1079 : { QUEST : "Humm, deixe-me ver este recibo.\a...Ah, sim, diz que 1 peixe dourado foi vendido para um Puxa-saco.\aO recibo não menciona o que aconteceu com os outros 4 peixes.\aTalvez voc\xc3\xaa deva tentar encontrar esse Puxa-saco.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Acho que não há mais nada em que eu possa ajudar.\aPor que voc\xc3\xaa não tenta encontrar aquele peixe dourado?" },
    1092 : { QUEST : "Humm, deixe-me ver este recibo.\a...Ah, sim, diz que 1 peixe dourado foi vendido para um Farsante.\aO recibo não menciona o que aconteceu com os outros 4 peixes.\aTalvez voc\xc3\xaa deva tentar encontrar esse Farsante.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Acho que não há mais nada em que eu possa ajudar.\aPor que voc\xc3\xaa não tenta encontrar aquele peixe dourado?" },
    1080 : { QUEST : "Ah, graças aos céus! Voc\xc3\xaa encontrou Oscar - ele é o meu favorito.\aO que foi, Oscar? Hã-hã... Verdade? ... Estão?\aOscar diz que os outros 4 escaparam para dentro do lago no pátio.\aVoc\xc3\xaa poderia reuni-los para mim?\a\xc3\x89 só pescá-los no lago.",
             LEAVING : "",
             COMPLETE : "Nossa, estou tããão feliz! Estou junto com meus companheiros novamente!\aVoc\xc3\xaa merece uma bela recompensa por isso!",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa está tendo problemas para pescar esses peixes?" },
    1081 : { QUEST : "_toNpcName_ parece estar numa situação grudenta. Ela, com certeza, apreciaria alguma ajuda._where_" },
    1082 : { QUEST : "Eu derramei supercola e estou presa - presa pra valer!\aSe houver uma maneira de sair, eu gostaria de saber.\aIsso me dá uma ideia; abra os olhos.\aDerrote alguns Robôs Vendedores e traga de volta um pouco de óleo.",
             LEAVING : "",
             GREETING : "",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa pode me ajudar a descolar daqui?" },
    1083 : { QUEST : "Bem, o óleo ajudou um pouco, mas eu ainda não consigo me mexer.\aO que mais poderia ajudar? \xc3\x89 dif\xc3\xadcil dizer.\aIsso me dá uma ideia; vale a pena tentar.\aDerrote alguns Robôs da Lei e me traga graxa.",
             LEAVING : "",
             GREETING : "",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa pode me ajudar a descolar daqui?" },
    1084 : { QUEST : "Não, isso não ajudou. Isso realmente não é engraçado.\aEu coloquei a graxa bem ali,\aIsso me dá uma ideia, não me deixe esquecer.\aDerrote alguns Robôs Mercenários e traga água para umedecer.",
             LEAVING : "",
             GREETING : "",
             COMPLETE : "Oba! Estou livre da supercola,\aComo recompensa, dou este presente a voc\xc3\xaa.\aVoc\xc3\xaa pode rir um pouco mais enquanto luta e, então...\aAh, não! Já estou presa aqui novamente!",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa pode me ajudar a descolar daqui?" },
    1085 : { QUEST : "_toNpcName_ está fazendo uma pesquisa sobre os Cogs.\aVá falar com ele para ver se ele precisa da sua ajuda._where_" },
    1086 : { QUEST : "\xc3\x89 verdade, estou fazendo um estudo sobre os Cogs.\aEu quero aprender sobre o comportamento deles.\aCom certeza ajudaria se voc\xc3\xaa pudesse reunir algumas engrenagens de Cogs.\aMas elas t\xc3\xaam que ser de Cogs de n\xc3\xadvel 2, pelo menos, para serem grandes o suficiente para o exame visual.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não conseguiu encontrar engrenagens suficientes?" },
    1089 : { QUEST : "Certo, vamos dar uma olhada. Estas são amostras excelentes!\aHummm...\aCerto, aqui está meu relatório. Leve isto de volta imediatamente para o Quartel dos Toons.",
             INCOMPLETE : "Voc\xc3\xaa entregou meu relatório no Quartel?",
             COMPLETE : "Bom trabalho _avName_, nós assumiremos a partir daqui.",
             LEAVING : "" },
    1090 : { QUEST : "_toNpcName_ tem informações úteis para voc\xc3\xaa._where_" },
    1091 : { QUEST : "Fiquei sabendo que o Quartel dos Toons está trabalhando em uma espécie de Radar de Cogs.\aEle permite ver onde os Cogs estão, para que seja mais fácil encontrá-los.\aA Página de Cogs em seu \xc3\x81lbum Toon é a chave.\aAo derrotar Cogs suficientes, voc\xc3\xaa pode sintonizar os sinais deles e rastrear onde estão.\aContinue derrotando Cogs para ficar pronto.",
             COMPLETE : "Bom trabalho! Voc\xc3\xaa provavelmente vai poder fazer uso disso...",
             LEAVING : "" },
    401 : {GREETING : "",
           QUEST : "Agora, voc\xc3\xaa tem que escolher o próximo tipo de piada que deseja aprender.\aDecida e depois volte aqui quando estiver pronto para escolher.",
           INCOMPLETE_PROGRESS : "Pense bem sobre sua decisão antes de escolher.",
           INCOMPLETE_WRONG_NPC : "Pense bem sobre sua decisão antes de escolher.",
           COMPLETE : "Uma boa decisão...",
           LEAVING : QuestsDefaultLeaving,
           },
    2201 : { QUEST : "Aqueles cogs traiçoeiros estão envolvidos nisto novamente.\a_toNpcName_ reportou outro item ausente. Pare um pouco aqui e veja se consegue acertar isso._where_" },
    2202 : { QUEST : "Oi, _avName_. Ainda bem que voc\xc3\xaa está aqui. Um Mão de vaca de má apar\xc3\xaancia acabou de passar por aqui e saiu com uma câmara de ar.\aTemo que ele possa usá-la para seus planos diabólicos.\aVeja se voc\xc3\xaa consegue encontrá-la e traz\xc3\xaa-la de volta.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Conseguiu achar minha câmara de ar?",
             COMPLETE : "Voc\xc3\xaa encontrou minha câmara de ar! Voc\xc3\xaa é legal MESMO! Olha aqui, tome a sua recompensa...",
             },
    2203 : { QUEST : "Os cogs estão espalhando o caos no banco.\aVá até o Capitão Carlão e veja o que voc\xc3\xaa pode fazer._where_" },
    2204 : { QUEST : "Bem-vindo a bordo, colega.\aDroga! Aqueles cogs patifes quebraram meu monóculo e eu não vivo sem ele.\aSeja um bom marujo e leve esta receita para o Dr. Quiqueres para trazer um novo para mim._where_",
             GREETING : "",
             LEAVING : "",
             },
    2205 : { QUEST : "O que é isso?\aPuxa, eu adoraria poder trabalhar nesta receita, mas os cogs t\xc3\xaam furtado meus suprimentos.\aSe voc\xc3\xaa pegasse a armação dos óculos de um Puxa-saco eu provavelmente poderia ajudá-lo.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Sinto muito. Sem armações de Puxa-saco, não tem monóculo!",
             },
    2206: { QUEST : "Excelente!\aSó um segundo...\aSua receita está pronta. Leve este monóculo diretamente ao Capitão Carlão._where_",
            GREETING : "",
            LEAVING : "",
            COMPLETE : "Alto!\aVoc\xc3\xaa vai ganhar sua condecoração, afinal de contas.\aAqui está.",
            },
    2207 : { QUEST : "Há um Cog na loja da Craca Bárbara!\a\xc3\x89 melhor voc\xc3\xaa ir para lá imediatamente._where_" },
    2208 : { QUEST : "Droga! Voc\xc3\xaa se desencontrou dele, gracinha.\aHavia um Golpe Sujo aqui. Ele levou a minha grande peruca branca.\aEle disse que era para o chefe dele e mencionou algo como \"precedente legal\".\aSe voc\xc3\xaa puder pegá-la de volta, ficarei eternamente grata.",
             LEAVING : "",
             GREETING : "",
             INCOMPLETE_PROGRESS : "Ainda não o encontrou?\aEle é alto e tem uma cabeça pontuda.",
             COMPLETE : "Voc\xc3\xaa a encontrou!?!?\aVoc\xc3\xaa é uma gracinha!\aSua recompensa é mais do que merecida...",
             },
    2209 : { QUEST : "Moby está se preparando para uma viagem importante.\aVisite-o e veja o que pode fazer para ajudá-lo._where_"},
    2210 : { QUEST : "Sua ajuda será bem-vinda.\aO Quartel dos Toons me pediu para fazer uma viagem e ver se consigo descobrir de onde os cogs estão vindo.\aPrecisarei de algumas coisas para o meu navio, mas não tenho muitas balinhas.\aPasse pela loja da Alice e pegue um pouco de cascalho para mim. Voc\xc3\xaa terá que fazer um favor para ela para poder pegar o cascalho._where_",
             GREETING : "E a\xc3\xad, _avName_",
             LEAVING : "",
             },
    2211 : { QUEST : "Então, o Moby quer cascalho, né?\aEle ainda está me devendo por aquele último alqueire.\aEu lhe darei se voc\xc3\xaa conseguir eliminar cinco Microempresários na minha rua.",
             INCOMPLETE_PROGRESS : "Não, seu bobinho! Eu disse CINCO microempresários...",
             GREETING : "O que posso fazer por voc\xc3\xaa?",
             LEAVING : "",
             },
    2212 : { QUEST : "Trato é trato.\aAqui está o cascalho para aquele fominha do Moby._where_",
             GREETING : "Ora, ora, o que temos aqui...",
             LEAVING : "",
             },
    2213 : { QUEST : "Excelente trabalho. Eu sabia que ela encontraria uma sa\xc3\xadda.\aAgora, eu preciso pegar uma carta de navegação com o Mário.\aAcho que meu crédito lá também não é tão bom, portanto, voc\xc3\xaa vai ter que negociar com ele._where_",
             GREETING : "",
             LEAVING : "",
             },
    2214 : { QUEST : "Sim, eu tenho a carta de navegação que o Moby quer.\aE se voc\xc3\xaa estiver disposto a trabalhar para consegui-la, eu a darei para voc\xc3\xaa.\aEstou tentando construir um astrolábio para navegar pelas estrelas.\aPreciso de tr\xc3\xaas engrenagens de Cog para constru\xc3\xad-la.\aVolte aqui quando encontrá-las.",
             INCOMPLETE_PROGRESS: "Como está indo com aquelas engrenagens de Cog?",
             GREETING : "Bem-vindo!",
             LEAVING : "Boa sorte!",
             },
    2215 : { QUEST : "Oh! Essas engrenagens vão ser úteis mesmo.\aAqui está a carta. Leve para o Moby, com meus cumprimentos._where_",
             GREETING : "",
             LEAVING : "",
             COMPLETE : "Bem, agora sim. Estou pronto para zarpar!\aEu o levaria comigo se voc\xc3\xaa não fosse novato. Leve isto, então.",
             },
    901 : { QUEST : "Se estiver disposto, o Salgado está precisando de ajuda na loja dele..._where_",
            },
    2902 : { QUEST : "Voc\xc3\xaa é o novo recruta?\aBom, bom. Talvez voc\xc3\xaa possa me ajudar.\aEstou construindo um caranguejo pré-fabricado gigante para confundir os cogs.\aEu vou precisar de uma braçadeira. Visite o Mário e me traga uma._where_",
             },
    2903 : { QUEST : "Olá!\aSim, eu ouvi falar no caranguejo gigante que Salgado está construindo.\aA melhor braçadeira que tenho está meio suja.\aSeja gentil e passe pela lavanderia antes de levá-la para ele._where_",
             LEAVING : "Valeu!"
             },
    2904 : { QUEST : "Voc\xc3\xaa deve ser o amigo do Mário.\aAcho que posso limpar isso rapidinho.\aSó um minuto...\aAqui está. Nova em folha!\aDiga olá ao Salgado por mim._where_",
             },
    2905 : { QUEST : "Ah, era exatamente o que eu queria.\aJá que voc\xc3\xaa está aqui, eu também vou precisar de uma mola de relógio de corda bem grande.\aVá até a loja do Gancho e veja se ele tem uma._where_",
             },
    2906 : { QUEST : "Uma mola bem grande?\aSinto muito, mas a maior que tenho ainda é pequena.\aTalvez eu consiga montar uma com as molas do gatilho de revólver de água.\aTraga-me tr\xc3\xaas dessas piadas e eu vou ver o que posso fazer.",
             },
    2907 : { QUEST : "Vamos dar uma olhada...\aArrasou. Simplesmente arrasou.\aAlgumas vezes eu surpreendo até a mim mesmo.\aAqui está: uma mola grande para o Salgado!_where_",
             LEAVING : "Bon Voyage!",
             },
     2911 : { QUEST : "Ficaria feliz em ajudar nisso, _avName_.\aMas temo que as ruas não estejam mais tão seguras.\aPor que voc\xc3\xaa não vai derrotar alguns Robôs Mercenários? Depois a gente conversa.",
             INCOMPLETE_PROGRESS : "Eu ainda acho que voc\xc3\xaa precisa fazer que as ruas fiquem mais seguras.",
             },
    2916 : { QUEST : "Sim, eu tenho um peso para o Salgado.\aNo entanto, acho que seria mais seguro se voc\xc3\xaa derrotasse alguns Robôs Vendedores primeiro.",
             INCOMPLETE_PROGRESS : "Ainda não. Derrote mais alguns Robôs Vendedores.",
             },
    2921 : { QUEST : "Humm, acho que poderia ceder um peso.\aMas eu me sentiria melhor se não houvesse tantos Robôs-chefe por a\xc3\xad.\aDerrote seis deles e volte aqui.",
             INCOMPLETE_PROGRESS : "Acho que ainda não está seguro...",
             },
    2925 : { QUEST : "Tudo pronto?\aBem, acho que agora está suficientemente seguro.\aAqui está o contrapeso para o Salgado._where_"
             },
    2926 : {QUEST : "Bem, isso é tudo.\aDeixe-me ver se funciona.\aHumm, um pequeno problema.\aNão estou conseguindo obter energia, pois aquele edif\xc3\xadcio Cog está bloqueando meu painel solar.\aVoc\xc3\xaa poderia dominá-lo para mim?",
            INCOMPLETE_PROGRESS : "Ainda sem energia. E aquele edif\xc3\xadcio?",
            COMPLETE : "Súper! Voc\xc3\xaa é um destruidor de cogs e tanto! Tome isto aqui como recompensa...",
            },
    3200 : { QUEST : "Acabo de receber uma ligação do _toNpcName_.\aEle está tendo um dia dif\xc3\xadcil. Talvez voc\xc3\xaa possa ajudá-lo!\aPasse por lá e veja do que ele precisa._where_" },
    3201 : { QUEST : "Puxa, obrigado por vir!\aPreciso de alguém para levar esta nova gravata de seda para _toNpcName_.\aVoc\xc3\xaa poderia fazer isso para mim?_where_" },
    3203 : { QUEST : "Ah, esta deve ser a gravata que eu pedi! Obrigado!\aEla combina com o terno listrado que acabei de terminar, logo ali.\aEi, o que aconteceu com o terno?\aOh, não! Os Cogs devem ter roubado meu terno novo!\aDerrote Cogs até encontrar meu terno e traga-o de volta para mim.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa já encontrou meu terno? Tenho certeza de que os Cogs o pegaram!",
             COMPLETE : "Legal! Voc\xc3\xaa encontrou meu terno novo!\aViu, eu disse que os Cogs estavam com ele! Aqui está a sua recompensa...",
             },

    3204 : { QUEST : "_toNpcName_ acabou de ligar para informar um roubo.\aPor que voc\xc3\xaa não passa por lá e v\xc3\xaa se consegue resolver as coisas?_where_" },
    3205 : { QUEST : "Olá, _avName_! Voc\xc3\xaa veio me ajudar?\aAcabei de expulsar um Sanguessuga de minha loja. Puxa! Foi horr\xc3\xadvel.\aMas agora não encontro minha tesoura em lugar nenhum! Tenho certeza de que o Sanguessuga a levou.\aEncontre-o e recupere minha tesoura.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa ainda está procurando minha tesoura?",
             COMPLETE : "Minha tesoura! Valeu mesmo, viu? Aqui está a sua recompensa...",
             },

    3206 : { QUEST : "Parece que _toNpcName_ está tendo problemas com alguns Cogs.\aVá ver se voc\xc3\xaa pode ajudá-lo._where_" },
    3207 : { QUEST : "Oi, _avName_! Obrigado por vir!\aUm monte de Duplos Sentidos invadiu minha loja e roubou uma pilha de cartões-postais de meu balcão.\aVá e derrote todos os Duplos Sentidos e recupere meus cartões-postais!",
             INCOMPLETE_PROGRESS : "Não há cartões-postais suficientes! Continue procurando!",
             COMPLETE : "Ah, valeu! Agora eu posso entregar a correspond\xc3\xaancia na hora certa! Aqui está a sua recompensa...",
             },

    3208 : { QUEST : "Ultimamente temos recebido reclamações dos moradores sobre os Reis da Incerta.\aVeja se consegue derrotar 10 Reis da Incerta para ajudar nossos colegas Toons nos Jardins da Margarida." },
    3209 : { QUEST : "Valeu mesmo por derrotar os Reis da Incerta!\aMas agora os Operadores de Telemarketing ficaram fora de controle.\aDerrote 10 Operadores de Telemarketing nos Jardins da Margarida e volte aqui para pegar sua recompensa." },

    3247 : { QUEST : "Ultimamente, temos recebido reclamações dos moradores sobre os Sanguessugas.\aVeja se consegue derrotar 20 Sanguessugas para ajudar nossos colegas Toons nos Jardins da Margarida." },


    3210 : { QUEST : "Oh, não, a Seivas Florais da Rua das Amendoeiras está sem flores!\aPara ajudar, leve dez de suas flores com esguicho.\aMas veja primeiramente se tem realmente 10 flores com esguicho em seu estoque.",
             LEAVING: "",
             INCOMPLETE_PROGRESS : "Preciso ter 10 flores com esguicho. Voc\xc3\xaa não tem o suficiente!" },
    3211 : { QUEST : "Puxa, valeu mesmo, viu? Estas flores com esguicho vão salvar a pátria.\aMas estou com medo daqueles Cogs lá fora.\aVoc\xc3\xaa pode me ajudar e derrotar alguns desses Cogs?\aVolte aqui depois de derrotar 20 Cogs nesta rua.",
             INCOMPLETE_PROGRESS : "Ainda há Cogs lá fora para serem derrotados! Continue trabalhando!",
             COMPLETE : "Ah, valeu! Isso ajudou muito. Sua recompensa é...",
             },

    3212 : { QUEST : "_toNpcName_ precisa de ajuda para procurar por algo que ela perdeu.\aVá visitá-la e veja o que pode fazer._where_" },
    3213 : { QUEST : "Oi, _avName_. Voc\xc3\xaa pode me ajudar?\aNão sei onde coloquei minha caneta. Acho que alguns Cogs pegaram-na.\aDerrote Cogs para encontrar minha caneta roubada.",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa já encontrou minha caneta?" },
    3214 : { QUEST : "Sim, é a minha caneta! Valeu!\aMas, enquanto voc\xc3\xaa estava fora, eu percebi que meu tinteiro também desapareceu.\aDerrote Cogs para encontrar meu tinteiro.",
             INCOMPLETE_PROGRESS : "Ainda estou procurando meu tinteiro!" },
    3215 : { QUEST : "Demais! Agora tenho minha caneta e meu tinteiro de volta!\aMas voc\xc3\xaa nem vai acreditar!\aMeu bloco de notas sumiu! Eles devem t\xc3\xaa-lo roubado também!\aDerrote Cogs para encontrar meu bloco de notas roubado e, então, traga-o de volta para ter sua recompensa.",
             INCOMPLETE_PROGRESS : "E meu bloco de notas?" },
    3216 : { QUEST : "\xc3\x89 o meu bloco de notas! Maneiro! Sua recompensa é...\aEi! Onde ela está?\aSua recompensa estava bem aqui no cofre de meu escritório. Mas o cofre inteiro sumiu!\aDá para acreditar? Aqueles cogs roubaram sua recompensa!\aDerrote Cogs para recuperar meu cofre.\aQuando voc\xc3\xaa o trouxer de volta, eu lhe darei sua recompensa.",
             INCOMPLETE_PROGRESS : "Continue procurando o cofre! Sua recompensa está lá dentro!",
             COMPLETE : "Finalmente! Seu novo saco de piadas está dentro daquele cofre. Aqui está...",
             },

    3217 : { QUEST : "Temos feito alguns estudos sobre a mecânica dos Robôs Vendedores.\aNós ainda precisamos estudar algumas peças de forma mais detalhada.\aTraga-nos uma roda dentada de algum Dr. Sabe-com-quem-está-falando.\aVoc\xc3\xaa poderá conseguir uma quando o Cog estiver explodindo." },
    3218 : { QUEST : "Muito bom! Agora precisamos de uma roda dentada de um Amigo da Onça.\aEstas são mais dif\xc3\xadceis de conseguir, portanto, continue tentando." },
    3219 : { QUEST : "Demais! Agora precisamos de apenas mais uma roda dentada.\aDesta vez, precisamos de uma de um Agitador.\aTalvez voc\xc3\xaa precise procurar esses Cogs nos edif\xc3\xadcios dos Robôs Vendedores.\aQuando achar a roda, traga-a aqui para receber sua recompensa." },

    3244 : { QUEST : "Temos feito alguns estudos sobre a mecânica dos Robôs da Lei.\aNós ainda precisamos estudar algumas peças de forma mais detalhada.\aTraga-nos uma roda dentada de algum Perseguidor de Ambulâncias.\aVoc\xc3\xaa poderá conseguir uma quando o Cog estiver explodindo." },
    3245 : { QUEST : "Muito bom! Agora precisamos de uma roda dentada de um Golpe Sujo.\aEstas são mais dif\xc3\xadceis de conseguir, portanto, continue tentando." },
    3246 : { QUEST : "Demais! Agora precisamos de apenas mais uma roda dentada.\aDesta vez, de um Relações Públicas.\aQuando pegá-la, traga-a aqui para conseguir sua recompensa." },

    3220 : { QUEST : "Acabei de saber que _toNpcName_ estava perguntando por voc\xc3\xaa.\aPor que voc\xc3\xaa não passa por lá e v\xc3\xaa o que ela quer?_where_" },
    3221 : { QUEST : "Oi, _avName_! A\xc3\xad está voc\xc3\xaa!\aOuvi dizer que voc\xc3\xaa é especialista em ataques com esguicho.\aPreciso de alguém para dar um bom exemplo a todos os Toons nos Jardins da Margarida.\aUse seus ataques com esguicho para derrotar vários Cogs.\aIncentive seus amigos a usarem o esguicho também.\aQuando tiver derrotado 20 Cogs, volte aqui para pegar sua recompensa!" },

    3222 : { QUEST : "\xc3\x89 hora de demonstrar sua Toonmizade.\aSe voc\xc3\xaa recuperar, com sucesso, um número de edif\xc3\xadcios de Cogs, ganhará o direito de fazer tr\xc3\xaas buscas.\aPrimeiramente, derrote dois edif\xc3\xadcios de Cogs.\aSinta-se \xc3\xa0 vontade para chamar seus amigos para ajudá-lo."},
    3223 : { QUEST : "Bom trabalho naqueles edif\xc3\xadcios!\aAgora, derrote mais dois.\aOs edif\xc3\xadcios devem ter, pelo menos, dois andares." },
    3224 : { QUEST : "Fantástico!\aAgora é só derrotar mais dois edif\xc3\xadcios.\aEles devem ter, pelo menos, tr\xc3\xaas andares.\aQuando terminar, volte para pegar sua recompensa!",
             COMPLETE : "Voc\xc3\xaa conseguiu, _avName_!\aVoc\xc3\xaa demonstrou uma elevada Toonmizade.",
             GREETING : "",
             },

    3225 : { QUEST : "_toNpcName_ diz que precisa de ajuda.\aPor que voc\xc3\xaa não vai até lá e v\xc3\xaa o que pode fazer para ajudá-la?_where_" },
    3235 : { QUEST : "Ah, esta é a salada que pedi!\aObrigada por traz\xc3\xaa-la para mim.\aTodos esses Cogs devem ter amedrontado novamente o entregador de _toNpcName_ .\aPor que voc\xc3\xaa não nos faz um favor e derrota alguns desses Cogs lá fora?\aDerrote 10 Cogs nos Jardins da Margarida e, então, vá até _toNpcName_.",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa está trabalhando na eliminação de Cogs para mim?\aIsto é maravilhoso! Continue com o bom trabalho!",
             COMPLETE : "Oh, muito obrigada por derrotar aqueles Cogs!\aAgora, acho que poderei manter minha escala normal de entregas.\aSua recompensa é...",
             INCOMPLETE_WRONG_NPC : "Vá contar a _toNpcName_ sobre os Cogs que voc\xc3\xaa derrotou._where_" },

    3236 : { QUEST : "Há muitos Robôs da Lei por a\xc3\xad.\aVoc\xc3\xaa pode fazer sua parte para ajudar!\aDerrote 3 edif\xc3\xadcios de Robôs da Lei." },
    3237 : { QUEST : "Bom trabalho naqueles edif\xc3\xadcios de Robôs da Lei!\aMas agora há muitos Robôs Vendedores!\aDerrote 3 edif\xc3\xadcios de Robôs Vendedores e volte para buscar sua recompensa." },

    3238 : { QUEST : "Ah não! Um Cog \"Amizade Fácil\" roubou a Chave para os Jardins da Margarida!\aVeja se voc\xc3\xaa consegue recuperá-la.\aLembre-se, o Amizade Fácil só pode ser encontrado dentro dos edif\xc3\xadcios de Robôs Vendedores." },
    3239 : { QUEST : "Voc\xc3\xaa achou uma chave, tudo bem, mas esta não é a correta!\aPrecisamos da chave dos Jardins da Margarida.\aContinue de olho! Ela ainda está com algum Cog \"Amizade Fácil\"!" },

    3242 : { QUEST : "Ah não! Um Cog Macaco velho roubou a Chave para os Jardins da Margarida!\aVeja se voc\xc3\xaa consegue recuperá-la.\aLembre-se, os Macacos-velhos só podem ser encontrados dentro dos edif\xc3\xadcios de Robôs da Lei." },
    3243 : { QUEST : "Voc\xc3\xaa achou uma chave, tudo bem, mas esta não é a correta!\aPrecisamos da chave dos Jardins da Margarida.\aContinue de olho! Ela ainda está com algum Cog Macaco velho!" },

    3240 : { QUEST : "Acabei de saber que um Macaco velho roubou um saco de ração para pássaros de _toNpcName_ .\aDerrote Macacos velhos até recuperar a ração para pássaros do Flor\xc3\xaancio e levá-la de volta para ele.\aOs Macacos velhos só são encontrados dentro de edif\xc3\xadcios de Robôs da Lei._where_",
             COMPLETE : "Ah, muito obrigado por encontrar minha ração para pássaros!\aSua recompensa é...",
             INCOMPLETE_WRONG_NPC : "Bom trabalho na recuperação da ração para pássaros!\aAgora, leve-a para _toNpcName_._where_",
             },

    3241 : { QUEST : "Alguns dos edif\xc3\xadcios de Cogs estão ficando altos demais e isso já está incomodando.\aVeja se voc\xc3\xaa consegue derrubar alguns dos edif\xc3\xadcios mais altos.\aRecupere 5 edif\xc3\xadcios de 3 andares, ou mais altos, e volte para pegar sua recompensa.",
             },

    3250 : { QUEST : "A Detetive Linda da Rua dos Carvalhos recebeu informações sobre um Quartel de Robôs Vendedores.\aVá até lá e ajude-a a investigar.",
             },
    3251 : { QUEST : "Há algo estranho acontecendo por aqui.\aHá tantos Robôs Vendedores!\aOuvi dizer que eles organizaram seu próprio quartel no final desta rua.\aVá até lá e veja o que consegue descobrir.\aEncontre Cogs Robôs Vendedores em seu quartel, derrote 5 deles e volte aqui.",
             },
    3252 : { QUEST : "Ok, desembucha.\aO que voc\xc3\xaa disse?\aQuartel de Robôs Vendedores?? Ah não!!! Algo tem que ser feito.\aDevemos avisar a Ju\xc3\xadza Gala. Ela saberá o que fazer.\aVá até lá e conte a ela o que descobrimos. \xc3\x89 só descer a rua.",
            },
    3253 : { QUEST : "Sim, posso ajudá-lo? Estou muito ocupada.\aHã? Quartel de Cogs?\aHã? Besteira. Isto nunca poderia acontecer.\aVoc\xc3\xaa deve estar enganado. Absurdo.\aHã? Não discuta comigo.\aOk, então, traga alguma prova.\aSe os Robôs Vendedores realmente estão construindo este Quartel de Cogs, qualquer Cog de lá estará carregando mapas.\aCogs amam trabalhar com papelada, sabe?\aDerrote Robôs Vendedores até encontrar os mapas.\aTraga-os aqui, e eu talvez acredite em voc\xc3\xaa.",
            },
    3254 : { QUEST : "Voc\xc3\xaa de novo, hã? Mapas? Voc\xc3\xaa está com eles?\aDeixe-me v\xc3\xaa-los! Humm... Uma fábrica?\aDeve ser lá que eles estão construindo os Robôs Vendedores... E o que é isso?\aSim, exatamente como eu suspeitava. Eu sabia o tempo todo.\aEles estão construindo um Quartel de Robôs Vendedores.\aIsso não é bom. Preciso fazer algumas ligações. Estou muito ocupada. Adeus!\aHã? Ah sim, leve estes mapas de volta para a Detetive Linda.\aEla poderá decifrá-los melhor.",
             COMPLETE : "O que a Ju\xc3\xadza Gala disse?\aNós t\xc3\xadnhamos razão? Ah, não. Vamos ver estes mapas.\aHumm... Parece que os Robôs Vendedores constru\xc3\xadram uma fábrica com maquinário para fazer Cogs.\aParece muito perigoso. Fique de fora até que voc\xc3\xaa tenha mais Pontos de risadas.\aQuando voc\xc3\xaa tiver mais Pontos de risadas, teremos muito mais a aprender sobre o Quartel dos Robôs Vendedores.\aAqui está sua recompensa. Bom trabalho!",
            },


    3255 : { QUEST : "_toNpcName_ está investigando o "+lSellbotHQ+".\aVeja se voc\xc3\xaa consegue ajudar._where_" },
    3256 : { QUEST : "_toNpcName_ está investigando o "+lSellbotHQ+".\aVeja se voc\xc3\xaa consegue ajudar._where_" },
    3257 : { QUEST : "_toNpcName_ está investigando o "+lSellbotHQ+".\aVeja se voc\xc3\xaa consegue ajudar._where_" },
    3258 : { QUEST : "Há muita confusão sobre o que os Cogs pretendem com seu novo Quartel.\aPreciso que voc\xc3\xaa traga algumas informações diretamente deles.\aSe nós conseguirmos quatro memorandos internos de Robôs Vendedores dentro de seu Quartel, isso ajudará a esclarecer as coisas.\aTraga o primeiro memorando para mim para que possamos nos informar melhor.",
             },
    3259 : { QUEST : "Demais! Vamos ver o que diz o memorando...\a\"A/C Robôs Vendedores:\"\a\"Estarei em meu escritório no topo das Torres Robôs Vendedores promovendo Cogs a n\xc3\xadveis mais altos.\"\a\"Quando voc\xc3\xaa tiver méritos suficientes, entre no elevador do saguão para falar comigo\".\a\"O intervalo chegou ao fim. De volta ao trabalho!\"\a\"Assinado, Robô Vendedor VP\"\aAhá.... Flippy vai querer ver isto. Enviarei a ele imediatamente.\aVá buscar o segundo memorando e traga aqui.",
             },
    3260 : { QUEST : "Que bom, voc\xc3\xaa está de volta. Deixe-me ver o que voc\xc3\xaa encontrou....\a\"A/C Robôs Vendedores:\"\a\"As Torres Robôs Vendedores instalaram um novo sistema de segurança para afastar todos os Toons.\"\a\"Os Toons que forem encontrados nas Torres Robôs Vendedores serão detidos para interrogatório\".\a\"Encontrem-se no saguão para um coquetel, no qual discutiremos o assunto.\"\a\"Assinado, Amizade Fácil\"\aMuito interessante... Passarei imediatamente esta informação adiante.\aTraga o terceiro memorando.",
             },
    3261 : { QUEST : "Excelente trabalho _avName_! O que diz o memorando?\a\"A/C Robôs Vendedores:\"\a\"De algum modo, os Toons encontraram um jeito de se infiltrarem nas Torres Robôs Vendedores.\"\a\"Ligarei para voc\xc3\xaas esta noite na hora do jantar para fornecer os detalhes.\"\a\"Assinado, Operador de Telemarketing\"\aHumm... Queria saber como os Toons estão conseguindo se infiltrar....\aTraga mais um memorando e acho que assim teremos informações suficientes.",
             COMPLETE : "Eu sabia que voc\xc3\xaa conseguiria! Ok, o memorando diz...\a\"A/C Robôs Vendedores:\"\a\"Ontem, estava almoçando com Dr. Celebridade.\"\a\"Ele disse que o VP tem estado bastante ocupado nestes dias.\"\a\"Ele só receberá os Cogs que merecem promoção.\"\a\"Esqueci de dizer, o Amigo da Onça jogará golfe comigo no domingo.\"\a\"Assinado, Dr. Sabe-com-quem-está-falando\"\aBem... _avName_, isto foi muito útil.\aAqui está sua recompensa.",
             },

    3262 : { QUEST : "_toNpcName_ tem novas informações sobre a Fábrica do "+lSellbotHQ+".\aVá ver o que ele tem a dizer._where_" },
    3263 : { GREETING : "Olá, parceiro!",
             QUEST : "Eu sou o Treinador Abobrinha, mas voc\xc3\xaa pode me chamar de Treinador A.\aEu sou a favor de treinos com a raquete e alongamento, se é que voc\xc3\xaa me entende.\aOuça, os Robôs Vendedores terminaram uma enorme fábrica para produzir Robôs Vendedores 24 horas por dia.\aReúna um grupo de parceiros Toon e raquetada na fábrica!\aDentro do Quartel do Robô Vendedor, procure pelo túnel que leva até a fábrica e, então, entre no elevador.\aVoc\xc3\xaa já tem que estar com as piadas e os pontos de risadas completos e ter Toons fortes como guias.\aPara retardar o progresso dos Robôs Vendedores, derrote o Supervisor dentro da fábrica.\aParece um grande exerc\xc3\xadcio, se é que fui bem claro.",
             LEAVING : "Te vejo por a\xc3\xad, parceiro!",
             COMPLETE : "Ei, parceiro, bom trabalho naquela Fábrica!\aParece que voc\xc3\xaa encontrou parte de um terno de Cog.\aDeve ser uma sobra do processo de fabricação de Cogs.\aIsto pode vir a calhar. Continue coletando estas partes quando tiver um tempo livre.\aQuem sabe, quando voc\xc3\xaa coletar um terno de Cog completo, poderá vir a ser útil para alguma coisa....",
             },

    4001 : {GREETING : "",
            QUEST : "Agora, voc\xc3\xaa tem que escolher o próximo tipo de piada que deseja aprender.\aDecida e depois volte aqui quando estiver pronto para escolher.",
            INCOMPLETE_PROGRESS : "Pense bem sobre sua decisão antes de escolher.",
            INCOMPLETE_WRONG_NPC : "Pense bem sobre sua decisão antes de escolher.",
            COMPLETE : "Uma boa decisão...",
            LEAVING : QuestsDefaultLeaving,
            },

    4002 : {GREETING : "",
            QUEST : "Agora voc\xc3\xaa tem que escolher o próximo tipo de piada que deseja aprender.\aDecida e depois volte aqui quando estiver pronto para escolher.",
            INCOMPLETE_PROGRESS : "Pense bem sobre sua decisão antes de escolher.",
            INCOMPLETE_WRONG_NPC : "Pense bem sobre sua decisão antes de escolher.",
            COMPLETE : "Uma boa decisão...",
            LEAVING : QuestsDefaultLeaving,
            },
    4200 : { QUEST : "Aposto que o Tom iria gostar de ter alguma ajuda na pesquisa que ele está fazendo._where_",
             },
    4201 : { GREETING: "Tudo certo?",
             QUEST : "Estou bastante preocupado com a onda de roubos de instrumentos musicais.\aEstou conduzindo uma pesquisa com meus amigos comerciantes.\aTalvez seja poss\xc3\xadvel encontrar um padrão para me ajudar a resolver este caso.\aPeça a Tina o controle de estoque de concertina._where_",
             },
    4202 : { QUEST : "Sim, eu falei com Tom nesta manhã.\aO estoque está bem aqui.\aLeve para ele imediatamente, ok?_where_"
             },
    4203 : { QUEST : "Demais! Um a menos...\aAgora peça o da Cavaca._where_",
             },
    4204 : { QUEST : "Ah! O estoque!\aEsqueci completamente.\aAposto que consigo fazer enquanto voc\xc3\xaa derrota 10 cogs.\aPasse por aqui depois, e eu prometo que estará pronto.",
             INCOMPLETE_PROGRESS : "31, 32... DROGA!\aVoc\xc3\xaa me fez perder a conta!",
             GREETING : "",
             },
    4205 : { QUEST : "Ah, a\xc3\xad está voc\xc3\xaa.\aObrigada por me dar algum tempo.\aLeve isto para o Tom e diga olá por mim._where_",
             },
    4206 : { QUEST : "Humm, muito interessante.\aAgora estamos chegando a algum lugar.\aOk, o último estoque é o da Fifi._where_",
             },
    4207 : { QUEST : "Estoque?\aComo posso fazer o estoque se não tenho o formulário?\aVá até o Clave e veja se ele tem um para mim._where_",
             INCOMPLETE_PROGRESS : "Algum sinal daquele formulário?",
             },
    4208 : { QUEST : "Claro que eu tenho um formulário de estoque, monsenhor!\aMas eles não são de graça, sabe?.\aFaçamos o seguinte. Eu troco por uma torta de creme inteira.",
             GREETING : "Ei, monsenhor!",
             LEAVING : "Boa sorte...",
             INCOMPLETE_PROGRESS : "Um pedaço não adianta.\aEstou com fome, monsenhor. Eu preciso da torta INTEIRA.",
             },
    4209 : { GREETING : "",
             QUEST : "Humm...\aMuito gostoso!\aAqui está o formulário para Fifi._where_",
             },
    4210 : { GREETING : "",
             QUEST : "Valeu, foi uma grande ajuda.\aVamos ver...Violinos: 2\aTudo pronto! Aqui está!",
             COMPLETE : "Bom trabalho, _avName_.\aTenho certeza de que solucionarei este caso agora.\aPor que voc\xc3\xaa não o soluciona?",
             },

    4211 : { QUEST : "Veja, o Dr. Triturador está ligando de cinco em cinco minutos. Voc\xc3\xaa pode conversar com ele e ver qual o problema?_where_",
             },
    4212 : { QUEST : "Puxa! Estou feliz de ver que o Quartel dos Toons finalmente mandou alguém.\aNão tenho um cliente há dias.\aSão estes malditos Destruidores de Números que estão em todo lugar.\aAcho que eles estão ensinando maus hábitos de higiene oral a nossos moradores.\aDerrote dez deles e vamos ver se o negócio anda.",
             INCOMPLETE_PROGRESS : "Ainda sem clientes. Mas continue assim!",
             },
    4213 : { QUEST : "Sabe, talvez não sejam os Destruidores de Números, no final das contas.\aTalvez sejam apenas os Robôs Mercenários em geral.\aDerrote vinte deles e, com alguma sorte, alguém virá, pelo menos, para um check-up.",
             INCOMPLETE_PROGRESS : "Eu sei que vinte é muito. Mas tenho certeza de que vai valer a pena.",
             },
    4214 : { GREETING : "",
             LEAVING : "",
             QUEST : "Eu não consigo entender!\aAinda não há UM BENDITO fregu\xc3\xaas.\aTalvez precisemos ir até a fonte.\aTente recuperar um edif\xc3\xadcio Cog de Robôs Mercenários.\aIsso deve funcionar...",
             INCOMPLETE_PROGRESS : "Oh, por favor! Apenas um m\xc3\xadsero prediozinho...",
             COMPLETE : "Ainda não há uma alma sequer aqui.\aMas, pense bem.\aEu não tinha mesmo clientes antes da invasão dos cogs!\aRealmente agradeço toda a sua ajuda.\aIsto deve ajudar voc\xc3\xaa a prosseguir."
             },

    4215 : { QUEST : "A Ana precisa desesperadamente da ajuda de alguém.\aPor que voc\xc3\xaa não passa lá e v\xc3\xaa o que pode fazer?_where_",
             },
    4216 : { QUEST : "Obrigada por chegar tão rápido!\aParece que os cogs sumiram com várias passagens dos meus clientes.\aA Cavaca disse que viu um Amigo da Onça saindo daqui com as garras cheias de passagens.\aVeja se voc\xc3\xaa consegue recuperar a passagem do Al\xc3\xaa Nhador para o Alasca.",
             INCOMPLETE_PROGRESS : "Aqueles Amigos da Onça podem estar em qualquer lugar agora...",
             },
    4217 : { QUEST : "Legal! Voc\xc3\xaa encontrou!\aAgora seja um cavalheiro e entregue ao Al\xc3\xaa Nhador para mim, está bem?_where_",
             },
    4218 : { QUEST : "Genial, estupendo, fabuloso!\aAlasca, aqui vou eu!\aNão aguento mais esses cogs infernais.\aOlha, acho que a Ana precisa de voc\xc3\xaa de novo._where_",
             },
    4219 : { QUEST : "Exatamente, voc\xc3\xaa adivinhou!\aPreciso de voc\xc3\xaa para derrotar aquelas pestes dos Amigos da Onça para recuperar a passagem da Tábata para o Festival de Jazz.\aVoc\xc3\xaa sabe como fazer...",
               INCOMPLETE_PROGRESS : "Há mais lá fora, em algum lugar...",
             },
    4220 : { QUEST : "Gracinha!\aVoc\xc3\xaa poderia entregar este também?_where_",
             },
    4221 : { GREETING : "",
             LEAVING : "Fica frio...",
             QUEST : "Legal, cara!\aAgora estou na cidade dos gordinhos, _avName_.\aAntes de sair fora, é melhor falar com a Ana Banana de novo..._where_",
             },
    4222 : { QUEST : "Este é o último, prometo!\aAgora procure pela passagem do Barry para o grande concurso de cantores.",
             INCOMPLETE_PROGRESS : "Vamos lá, _avName_.\aO Barry está contando com voc\xc3\xaa.",
             },
    4223 : { QUEST : "Isto deve alegrar o Barry._where_",
             },
    4224 : { GREETING : "",
             LEAVING : "",
             QUEST : "Olá, Olá, OL\xc3\x81!\aMagn\xc3\xadfico!\aSó conheço eu mesmo e os caras que vão fazer a faxina. \aA Ana disse para voc\xc3\xaa passar lá e pegar a sua recompensa._where_\aTchau, Tchau, TCHAU!",
             COMPLETE : "Obrigado por toda a sua ajuda, _avName_.\aVoc\xc3\xaa é realmente um tesouro aqui de Toontown.\aFalando em tesouros...",
             },

    902 : { QUEST : "Vá ver o Léo.\aEle precisa de alguém para entregar uma mensagem para ele._where_",
            },
    4903 : { QUEST : "Cara!\aMinhas castanholas estão foscas e tenho um grande show hoje \xc3\xa0 noite.\aLeve-as para o Carlos e veja se ele pode dar um polimento nelas._where_",
            },
    4904 : { QUEST : "Sim, acho que posso polir esta peça. Mas preciso de alguma tinta azul de lula",
             GREETING : "Olá!",
             LEAVING : "Tchau!",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa pode achar uma lula perto de algum p\xc3\xader de pesca.",
             },
    4905 : { QUEST : "Claro! Isso mesmo!\aAgora, preciso de um minuto para polir isto. Por que voc\xc3\xaa não trabalha na recuperação de um prédio de um andar enquanto trabalho por aqui?",
             GREETING : "Ola!",
             LEAVING : "Tchau!",
             INCOMPLETE_PROGRESS : "Só mais um minutinho...",
             },
    4906 : { QUEST : "Muito bom!\aAqui estão as castanholas do Léo._onde_",
             },
    4907 : { GREETING : "",
             QUEST : "Maneiro, cara!\aElas estão incr\xc3\xadveis!\aAgora preciso que voc\xc3\xaa consiga uma cópia da letra da “Música de Natal” da Heidi._where_",
             },
    4908 : { QUEST: "E a\xc3\xad pessoal!\aHumm, Eu não tenho uma cópia dessa música \xc3\xa0 mão.\aSe voc\xc3\xaa me der um tempinho, eu posso transcrever de cabeça.\aPor que voc\xc3\xaa não dá uma voltinha e aproveita para recuperar um edif\xc3\xadcio de dois andares enquanto escrevo?",
             },
    4909 : { QUEST : "Desculpe.\aMinha memória está ficando meio confusa.\aSe voc\xc3\xaa recuperar um edif\xc3\xadcio de tr\xc3\xaas andares, tenho certeza de que estarei pronta quando voltar...",
             },
    4910 : { QUEST : "Tudo pronto!\aDesculpe a demora.\aLeve isto para o Léo._where_",
             GREETING : "",
             COMPLETE : "Caramba, cara!\aMeu show vai detonar!\aFalando em detonar, voc\xc3\xaa pode detonar alguns cogs com isto..."
             },
    5247 : { QUEST : "Este bairro está ficando perigoso...\aVoc\xc3\xaa deve estar querendo aprender alguns truques novos.\a_toNpcName_ me ensinou tudo que sei, então, talvez ele possa ajudar voc\xc3\xaa também._where_" },
    5248 : { GREETING : "Ah, sim.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa parece estar empenhado na missão.",
             QUEST : "Ah, bem-vindo, novo aprendiz.\aEu sei de tudo que há para saber sobre o jogo de tortas.\aPorém, antes de começarmos o seu treinamento, é necessário uma pequena demonstração.\aSaia e derrote dez dos maiores Cogs." },
    5249 : { GREETING: "Humm.",
             QUEST : "Excelente!\aAgora demonstre sua habilidade como pescador.\aColoquei ontem tr\xc3\xaas dados de pelúcia no lago.\aPesque-os e traga-os para mim.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Parece que voc\xc3\xaa não é tão hábil com a vara e o molinete." },
    5250 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ahá! Estes dados ficarão ótimos pendurados no retrovisor do meu carro de bois!\aAgora, mostre para mim que voc\xc3\xaa sabe distinguir seus inimigos.\aVolte quando tiver recuperado dois dos edif\xc3\xadcios mais altos dos Robôs da Lei.",
             INCOMPLETE_PROGRESS : "Os edif\xc3\xadcios deram problema para voc\xc3\xaa?", },
    5258 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ahá! Estes dados ficarão ótimos pendurados no retrovisor do meu carro de bois!\aAgora, mostre para mim que voc\xc3\xaa sabe distinguir seus inimigos.\aVolte quando tiver recuperado dois dos edif\xc3\xadcios mais altos dos Robôs-chefes.",
             INCOMPLETE_PROGRESS : "Os edif\xc3\xadcios deram problema para voc\xc3\xaa?", },
    5259 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ahá! Estes dados ficarão ótimos pendurados no retrovisor do meu carro de bois!\aAgora, mostre para mim que voc\xc3\xaa sabe distinguir seus inimigos.\aVolte quando tiver recuperado dois dos edif\xc3\xadcios mais altos dos Robôs Mercenários.",
             INCOMPLETE_PROGRESS : "Os edif\xc3\xadcios deram problema para voc\xc3\xaa?", },
    5260 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ahá! Estes dados ficarão ótimos pendurados no retrovisor do meu carro de bois!\aAgora, mostre para mim que voc\xc3\xaa sabe distinguir seus inimigos.\aVolte quando tiver recuperado dois dos edif\xc3\xadcios mais altos dos Robôs Vendedores.",
             INCOMPLETE_PROGRESS : "Os edif\xc3\xadcios deram problema para voc\xc3\xaa?", },
    5200 : { QUEST : "Aqueles cogs traiçoeiros estão envolvidos nisto novamente.\a_toNpcName_ percebeu que tem outro item ausente. Pare um pouco aqui e veja se consegue acertar isso._where_" },
    5201 : { GREETING: "",
             QUEST : "Oi, _avName_. Acho que eu devo agradecer a voc\xc3\xaa por ter vindo.\aUm grupo desses Caça-talentos chegou e roubou minha bola de futebol.\aO l\xc3\xadder disse que eu tinha que fazer alguns cortes e tomou a bola de mim!\aVoc\xc3\xaa pode trazer de volta a minha bola?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Conseguiu achar minha bola de futebol?",
             COMPLETE : "Dez! Encontrei! Olha aqui, tome a sua recompensa...",
             },
    5261 : { GREETING: "",
             QUEST : "Oi, _avName_. Acho que eu devo agradecer a voc\xc3\xaa por ter vindo.\aUm grupo desses Duas Caras chegou e roubou minha bola de futebol.\aO l\xc3\xadder disse que eu tinha que fazer alguns cortes e tomou a bola de mim!\aVoc\xc3\xaa pode trazer de volta a minha bola?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Conseguiu achar minha bola de futebol?",
             COMPLETE : "Dez! Encontrei! Olha aqui, tome a sua recompensa...",
             },
    5262 : { GREETING: "",
             QUEST : "Oi, _avName_. Acho que eu devo agradecer a voc\xc3\xaa por ter vindo.\aUm grupo desses Sacos de Dinheiro chegou e roubou minha bola de futebol.\aO l\xc3\xadder disse que eu tinha que fazer alguns cortes e tomou a bola de mim!\aVoc\xc3\xaa pode trazer de volta a minha bola?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Conseguiu achar minha bola de futebol?",
             COMPLETE : "Dez! Encontrei! Olha aqui, tome a sua recompensa...",
             },
    5263 : { GREETING: "",
             QUEST : "Oi, _avName_. Acho que eu devo agradecer a voc\xc3\xaa por ter vindo.\aUm grupo desses Relações Públicas chegou e roubou minha bola de futebol.\aO l\xc3\xadder disse que eu tinha que fazer alguns cortes e tomou a bola de mim!\aVoc\xc3\xaa pode trazer de volta a minha bola?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Conseguiu achar minha bola de futebol?",
             COMPLETE : "Dez! Encontrei! Olha aqui, tome a sua recompensa...",
             },
    5202 : { QUEST : "O Brrrgh foi invadido por alguns dos mais tem\xc3\xadveis Cogs já vistos.\aVoc\xc3\xaa provavelmente desejará carregar mais piadas consigo.\aOuvi falar que _toNpcName_ tem uma sacola grande que voc\xc3\xaa pode usar para carregar mais piadas._where_" },
    5203 : { GREETING: "Hã? Voc\xc3\xaa está no meu time de trenó?",
             QUEST : "O que é isto? Voc\xc3\xaa quer uma bolsa?\aEu tinha uma aqui em algum lugar... Acho que está no meu tobogã?\aSó que... Eu não vejo o meu tobogã desde a grande corrida!\aTalvez um destes Cogs o tenha pego.",
             LEAVING : "Voc\xc3\xaa viu meu tobogã?",
             INCOMPLETE_PROGRESS : "Quem é voc\xc3\xaa novamente? Desculpe, estou meio confuso depois da batida." },
    5204 : { GREETING : "",
             LEAVING : "",
             QUEST : "Este é o meu tobogã? Não vejo nenhuma sacola aqui.\aAcho que o Cabeção Kika estava na equipe... Será que está com ele?_where_" },
    5205 : { GREETING : "Ai, minha cabeça!",
             LEAVING : "",
             QUEST : "Hã? Tobi? Ah, a bolsa?\aBom, acho que ele estava na nossa equipe de tobogã?\aMinha cabeça dói tanto que não consigo pensar direito.\aVoc\xc3\xaa consegue para mim alguns cubos de gelo no lago congelado para eu pôr na minha cabeça?",
             INCOMPLETE_PROGRESS : "Aaiii, minha cabeça está me matando! Tem gelo a\xc3\xad?", },
    5206 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ahhh, agora me sinto bem melhor!\aEntão voc\xc3\xaa está procurando a bolsa do Tobi, né?\aAcho que ela foi parar na cabeça do \xc3\x81lvaro Asno depois da batida._where_" },
    5207 : { GREETING : "Iiiiiiiiiip!",
             LEAVING : "",
             QUEST : "O que é bolsa? Quem é Cabeção?\aTenho medo de edif\xc3\xadcios! Voc\xc3\xaa detona edif\xc3\xadcio, eu dou bolsa!",
             INCOMPLETE_PROGRESS : "Mais edif\xc3\xadcios! Ainda com medo!",
             COMPLETE : "Ooooh! Mim gosta voc\xc3\xaa!" },
    5208 : { GREETING : "",
             LEAVING : "Iiiiiiiiiiik!",
             QUEST : "Ooooh! Mim gosta voc\xc3\xaa!\aVai pra Cl\xc3\xadnica do Esqui. Sacola lá." },
    5209 : { GREETING : "Valeu, garoto!",
             LEAVING : "Até mais!",
             QUEST : "Cara, o \xc3\x81lvaro Asno é doido!\aSe voc\xc3\xaa fosse maluco que nem o \xc3\x81lvaro, eu daria a bolsa para voc\xc3\xaa, cara.\aVai ensacar uns Cogs para poder pegar a sua sacola, cara! Essa agora!",
             INCOMPLETE_PROGRESS : "Tem certeza de que voc\xc3\xaa é radical o bastante para isso? Vai ensacar mais Cogs.",
             COMPLETE : "Caramba, voc\xc3\xaa é irado! Aquilo foi um bando de Cogs que voc\xc3\xaa ensacou!\aToma a sua bolsa!" },

    5210 : { QUEST : "_toNpcName_ está gamada em alguém do bairro, mas é segredo.\aSe voc\xc3\xaa ajudá-la, ela pode lhe dar uma boa recompensa._where_" },
    5211 : { GREETING: "Buá!",
             QUEST : "Passei a noite passada inteira escrevendo uma carta para o cachorro que eu amo.\aMas, antes mesmo que eu pudesse entregar a ele, um daqueles Cogs asquerosos com bico veio e a tomou de mim.\aVoc\xc3\xaa consegue pegá-la de volta para mim?",
             LEAVING : "Buá!",
             INCOMPLETE_PROGRESS : "Por favor, encontre minha carta." },
    5264 : { GREETING: "Buá!",
             QUEST : "Passei a noite passada inteira escrevendo uma carta para o cachorro que eu amo.\aMas, antes mesmo que eu pudesse entregar a ele, um daqueles Cogs asquerosos de barbatana veio e a tomou de mim.\aVoc\xc3\xaa consegue pegá-la de volta para mim?",
             LEAVING : "Buá!",
             INCOMPLETE_PROGRESS : "Por favor, encontre minha carta." },
    5265 : { GREETING: "Buá!",
             QUEST : "Passei a noite passada inteira escrevendo uma carta para o cachorro que eu amo.\aMas, antes mesmo que eu pudesse entregar a ele, um daqueles Cogs asquerosos de Amizade Fácil veio e a tomou de mim.\aVoc\xc3\xaa consegue pegá-la de volta para mim?",
             LEAVING : "Buá!",
             INCOMPLETE_PROGRESS : "Por favor, encontre minha carta." },
    5266 : { GREETING: "Buá!",
             QUEST : "Passei a noite passada inteira escrevendo uma carta para o cachorro que eu amo.\aMas, antes mesmo que eu pudesse entregar a ele, um daqueles Cogs Aventureiros Corporativos asquerosos veio e a tomou de mim.\aVoc\xc3\xaa consegue pegá-la de volta para mim?",
             LEAVING : "Buá!",
             INCOMPLETE_PROGRESS : "Por favor, encontre minha carta." },
    5212 : { QUEST : "Oh, obrigada por encontrar a minha carta!\aPor favor, voc\xc3\xaa poderia entregá-la ao cão mais lindo do bairro? Por favor! Por favor!",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa não entregou a minha carta, não é?",
             },
    5213 : { GREETING : "Enfeitiçado, com certeza.",
             QUEST : "Não posso dar atenção \xc3\xa0 sua carta, sabe.\aTodos os meus cãezinhos foram levados!\aSe voc\xc3\xaa os trouxer de volta, a gente volta a conversar.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Tadinhos dos meus cãezinhos!" },
    5214 : { GREETING : "",
             LEAVING : "Tchauzinho!",
             QUEST : "Graças a voc\xc3\xaa minhas belezinhas voltaram.\aVamos ver a carta agora...\nMmmm, parece que tenho outra admiradora secreta.\aIsso exigirá uma visita ao meu querido amigo Carlo.\aAposto como voc\xc3\xaa vai adorá-lo._where_" },
    5215 : { GREETING : "He, he...",
             LEAVING : "Volte aqui, sim, sim.",
             INCOMPLETE_PROGRESS : "Ainda há alguns grandalhões na área. Volte aqui para falar conosco quando eles forem embora.",
             QUEST : "Quem mandou voc\xc3\xaa? Não gostamos muito de Snobs, não...\aMas gostamos menos ainda de Cogs...\aExpulse os grandalhões e ajudaremos voc\xc3\xaas, ajudaremos." },
    5216 : { QUEST : "Falamos que ajudar\xc3\xadamos voc\xc3\xaa.\aEntão, pegue este anel e leve \xc3\xa0 garota.",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa ainda está com o anel???",
             COMPLETE : "Oh querrrrido!!! Obrigado!!!\aAh, também tenho algo especial para voc\xc3\xaa.",
             },
    5217 : { QUEST : "Parece que _toNpcName_ pode dar uma ajuda._where_" },
    5218 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Tenho certeza de que há mais Amizades Fáceis por aqui em algum lugar.",
             QUEST : "Socorro!!! Socorro!!! Assim não dá!\aEsses Amizades Fáceis estão me deixando maluco!!!" },
    5219 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não são só estes. Só vi um!!!",
             QUEST : "Ah, obrigado, mas agora são os Aventureiros Corporativos!!!\aVoc\xc3\xaa tem que me ajudar!!!" },
    5220 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não, não, não, havia um aqui agora mesmo!",
             QUEST : "Agora, eu percebo que são aqueles Agiotas!!!\aPensei que voc\xc3\xaa ia me salvar!!!" },
    5221 : { GREETING : "",
             LEAVING : "",
             QUEST : "Sabe de uma coisa, talvez não sejam os Cogs coisa nenhuma!\aVoc\xc3\xaa pode pedir \xc3\xa0 Hilária para fazer para mim uma poção calmante? Talvez isto ajude...._where_" },
    5222 : { LEAVING : "",
             QUEST : "Esse Américo é mesmo uma figura!\aVou preparar algo que vai dar jeito nele rapidinho!\aPuxa, parece que estou sem bigodes de sardinha...\aSeja legal comigo e corra lá no lago para pegar alguns para mim.",
             INCOMPLETE_PROGRESS : "Já pegou aqueles bigodes para mim?", },
    5223 : { QUEST : "OK. Obrigada!\aTome, leve agora para o Américo. Isto deve acalmá-lo de uma vez por todas.",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Vá logo, leve a poção para o Américo.",
             },
    5224 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Vá pegar aqueles Macacos velhos para mim, ok?",
             QUEST : "Puxa vida, graças a Deus voc\xc3\xaa voltou!\aPasse logo para cá esta poção!!!\aGlub, glub, glub...\aQue gosto horr\xc3\xadvel!\aSabe de uma coisa? Sinto-me bem mais calmo. Agora que eu posso pensar com mais clareza, me toquei que...\aEram os Macacos-velhos que estavam me enlouquecendo todo este tempo!!!",
             COMPLETE : "Nossa! Agora eu posso relaxar!\aTenho certeza de que há alguma coisa aqui que posso dar a voc\xc3\xaa. Aqui, leve isto!" },
    5225 : { QUEST : "Desde o acidente com o pão de nabo, Felipe Nervosinho ficou furioso com _toNpcName_.\aQuem sabe voc\xc3\xaa não consegue ajudar o Pio a acertar os ponteiros entre eles?_where_" },
    5226 : { QUEST : "Isso mesmo, voc\xc3\xaa deve ter ouvido falar que o Felipe Nervosinho está furioso comigo...\aEu estava só tentando ser legal oferecendo o pão de nabo.\aQuem sabe voc\xc3\xaa não consegue alegrá-lo.\aO Felipe detesta aqueles Cogs Robôs Mercenários, principalmente os edif\xc3\xadcios deles.\aSe voc\xc3\xaa recuperar alguns edif\xc3\xadcios de Robôs Mercenários, talvez ajude.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Quem sabe alguns edif\xc3\xadcios a mais?", },
    5227 : { QUEST : "Demais! Vá dizer ao Felipe o que voc\xc3\xaa fez._where_" },
    5228 : { QUEST : "Puxa, ele fez isso mesmo?\aEsse Pio acha que pode se safar fácil, né?\aSó quebrou meu dente, só isso que ele fez, com aquele pão de nabo dele!\aSe voc\xc3\xaa levar o meu dente para o Dr. Ban Guela para mim, quem sabe ele consegue dar jeito.",
             GREETING : "Mmmmrrf.",
             LEAVING : "Resmungo, resmungo.",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa de novo? Pensei que voc\xc3\xaa estava indo levar meu dente para consertar.",
             },
    5229 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ainda estou ajeitando o dente. Vai demorar um pouco.",
             QUEST : "\xc3\x89, este dente parece estar ruim mesmo, mas tudo bem.\aEu acho que posso fazer uma coisa aqui, mas ainda vai demorar um pouco.\aVoc\xc3\xaa não quer dar cabo de alguns daqueles Cogs Robôs Mercenários das ruas enquanto espera?\aEles estão assustando os meus clientes." },
    5267 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ainda estou ajeitando o dente. Vai demorar um pouco.",
             QUEST : "\xc3\x89, este dente parece estar ruim mesmo, mas tudo bem.\aEu acho que posso fazer uma coisa aqui, mas ainda vai demorar um pouco.\aVoc\xc3\xaa não quer dar cabo de alguns daqueles Cogs Robôs Vendedores das ruas enquanto espera?\aEles estão assustando os meus clientes." },
    5268 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ainda estou ajeitando o dente. Vai demorar um pouco.",
             QUEST : "\xc3\x89, este dente parece estar ruim mesmo, mas tudo bem.\aEu acho que posso fazer uma coisa aqui, mas ainda vai demorar um pouco.\aVoc\xc3\xaa não quer dar cabo de alguns daqueles Cogs Robôs da Lei das ruas enquanto espera?\aEles estão assustando os meus clientes." },
    5269 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ainda estou ajeitando o dente. Vai demorar um pouco.",
             QUEST : "\xc3\x89, este dente parece estar ruim mesmo, mas tudo bem.\aEu acho que posso fazer uma coisa aqui, mas ainda vai demorar um pouco.\aVoc\xc3\xaa não quer dar cabo de alguns daqueles Cogs Robôs-chefe das ruas enquanto espera?\aEles estão assustando os meus clientes." },
    5230 : { GREETING: "",
             QUEST : "Ainda bem que voc\xc3\xaa voltou!\aDesisti de consertar aquele dente velho e, em vez de consertá-lo, fiz um novo dente de ouro para o Felipe.\aSó que um Barão Ladrão entrou aqui e o levou, infelizmente.\aSerá que voc\xc3\xaa não consegue pegá-lo? Vamos, apresse-se!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa já achou aquele dente?" },
    5270 : { GREETING: "",
             QUEST : "Ainda bem que voc\xc3\xaa voltou!\aDesisti de consertar aquele dente velho e, em vez de consertá-lo, fiz um novo dente de ouro para o Felipe.\aSó que um Rei da Cocada Preta entrou aqui e o levou, infelizmente.\aSerá que voc\xc3\xaa não consegue pegá-lo? Vamos, apresse-se!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa já achou aquele dente?" },
    5271 : { GREETING: "",
             QUEST : "Ainda bem que voc\xc3\xaa voltou!\aDesisti de consertar aquele dente velho e, em vez de consertá-lo, fiz um novo dente de ouro para o Felipe.\aSó que o Dr. Celebridade entrou aqui e o levou, infelizmente.\aSerá que voc\xc3\xaa não consegue pegá-lo? Vamos, apresse-se!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa já achou aquele dente?" },
    5272 : { GREETING: "",
             QUEST : "Ainda bem que voc\xc3\xaa voltou!\aDesisti de consertar aquele dente velho e, em vez de consertá-lo, fiz um novo dente de ouro para o Felipe.\aSó que um Figurão entrou aqui e o levou, infelizmente.\aSerá que voc\xc3\xaa não consegue pegá-lo? Vamos, apresse-se!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa já achou aquele dente?" },
    5231 : { QUEST : "Legal, é este dente mesmo!\aPor que voc\xc3\xaa não corre para levá-lo para o Felipe?",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Aposto como o Felipe vai adorar ver o dente novo dele.",
             },
    5232 : { QUEST : "Puxa, obrigado.\aMmmrrrfffffff\aE a\xc3\xad, que tal, hein?\aOk, tudo bem, pode dizer ao Pio que eu o perdôo.",
             LEAVING : "",
             GREETING : "", },
    5233 : { QUEST : "Legal, muito bom saber disso.\aAchei mesmo que meu velho amigo Felipe não podia ficar com raiva de mim.\aPara agradecer e ser gentil, preparei para ele este pão de pinha.\aSerá que voc\xc3\xaa podia correr lá e entregar a ele para mim?",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Melhor se apressar. O pão de pinha só é bom quando está quente.",
             COMPLETE : "Puxa, o que é isto? Para mim?\aNham, nham...\aOhhhhhh! Meu dente! Aquele Pio Arrepio!\aTudo bem, não foi sua culpa. Tome aqui, leve isto por todo o trabalho que demos a voc\xc3\xaa.",
             },
    903 : { QUEST : "Voc\xc3\xaa deve se aprontar para ver _toNpcName_, o Mago do Lago Congelado, para o seu teste final._where_", },
    5234 : { GREETING: "",
             QUEST : "Ahá! Voc\xc3\xaa voltou.\aAntes de voc\xc3\xaa começar, precisamos comer.\aTraga para a gente alguns pedaços de coco para o nosso caldo.\aO coco em pedaços só pode ser conseguido nos Cogs Rei da Cocada Preta.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ainda precisamos de coco em pedaços." },
    5278 : { GREETING: "",
             QUEST : "Ahá! Voc\xc3\xaa voltou.\aAntes de voc\xc3\xaa começar, precisamos comer.\aTraga para a gente caviar para o nosso caldo.\aO caviar só pode ser conseguido nos Cogs Dr. Celebridade.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ainda precisamos de caviar." },
    5235 : { GREETING: "",
             QUEST : "Homens simples comem com colheres simples.\aOs Cogs levaram minha colher simples, por isso, eu simplesmente não posso comer.\aPegue minha colher de volta. Acho que foi um Barão Ladrão.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Eu simplesmente preciso da minha colher." },
    5279 : { GREETING: "",
             QUEST : "Homens simples comem com colheres simples.\aOs Cogs levaram minha colher simples, por isso, eu não posso comer.\aPegue minha colher de volta. Acho que foi um Figurão.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Eu simplesmente preciso da minha colher." },
    5236 : { GREETING: "",
             QUEST : "Muito obrigado.\aSlurp, slurp...\aAhhh, agora, voc\xc3\xaa precisa pegar um sapo falante. Tente pescá-lo no lago.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Cad\xc3\xaa o sapo falante?" },

    5237 : {  GREETING : "",
              LEAVING : "",
              INCOMPLETE_PROGRESS : "Voc\xc3\xaa não conseguiu a sobremesa ainda.",
              QUEST : "Ah, isto é, com certeza, um sapo falante. Passe para cá.\aO que voc\xc3\xaa me diz, sapo?\aUh huh.\aUh huh...\aO sapo falou. Precisamos da sobremesa.\aTraga para a gente algumas casquinhas de sorvete da _toNpcName_.\aPor alguma razão, o sapo gosta de sorvete sabor feijão vermelho._where_", },
    5238 : { GREETING: "",
             QUEST : "Então, o mago mandou voc\xc3\xaa aqui. Sinto dizer que acabamos de ficar sem as casquinhas sabor feijão vermelho.\aVoc\xc3\xaa nem imagina, mas um bando de Cogs entrou aqui e as levou.\aEles disseram que iam levá-las para o Dr. Celebridade, ou alguma baboseira parecida.\aCertamente, apreciaria se voc\xc3\xaa pudesse recuperá-las para mim.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Já achou todas as minhas casquinhas de sorvete?" },
    5280 : { GREETING: "",
             QUEST : "Então, o mago mandou voc\xc3\xaa aqui. Sinto dizer que acabamos de ficar sem as casquinhas sabor feijão vermelho.\aVoc\xc3\xaa nem imagina, mas um bando de Cogs entrou aqui e as levou.\aEles disseram que iam levá-las para O Rei da Cocada Preta, ou alguma baboseira parecida.\aCertamente, apreciaria se voc\xc3\xaa pudesse recuperá-las para mim.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Já achou todas as minhas casquinhas de sorvete?" },
    5239 : { QUEST : "Obrigado por trazer de volta as minhas casquinhas de sorvete!\aTome uma para o Pequeno Grande Ancião.",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "\xc3\x89 melhor voc\xc3\xaa levar este sorvete para o Pequeno Grande Ancião antes que ele derreta.", },
    5240 : { GREETING: "",
             QUEST : "Muito bem. Aqui está, sapo...\aSlurp, slurp...\aOk, agora estamos quase prontos.\aSe voc\xc3\xaa pudesse apenas trazer um pozinho para secar as minhas mãos...\aAcho que das perucas daqueles Cogs Figurões \xc3\xa0s vezes sai pó.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Achou algum pó?" },
    5281 : { GREETING: "",
             QUEST : "Muito bem. Aqui está, sapo...\aSlurp, slurp...\aOk, agora estamos quase prontos.\aSe voc\xc3\xaa pudesse apenas trazer um pozinho para secar as minhas mãos...\aAcho que aqueles Cogs Drs. Celebridades \xc3\xa0s vezes t\xc3\xaam pó para o nariz.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Achou algum pó?" },
    5241 : { QUEST : "Ok.\aComo já disse antes, para lançar uma torta pra valer, não basta jogá-la com a mão...\a...\xc3\x89 preciso jogar com a alma.\aNão sei exatamente o que isto significa, portanto, sentarei e contemplarei voc\xc3\xaa em seu trabalho de recuperar edif\xc3\xadcios.\aVolte quando tiver conclu\xc3\xaddo a sua tarefa.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Sua tarefa ainda não está conclu\xc3\xadda.", },
    5242 : { GREETING: "",
             QUEST : "Embora eu ainda não saiba sobre o que estou falando, voc\xc3\xaa realmente merece.\aDou a voc\xc3\xaa, então, uma tarefa final...\aO sapo falante precisa de uma namorada.\aAche uma sapa falante. O sapo falou.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Cad\xc3\xaa a sapa falante?",
             COMPLETE : "Puxa! Estou cansado com todo esse esforço. Preciso descansar agora.\aAgora, pegue a sua recompensa e saia." },

    5243 : { QUEST : "Soares Suado está começando a feder no in\xc3\xadcio da rua.\aFala com ele para tomar um banho ou algo do g\xc3\xaanero?_where_" },
    5244 : { GREETING: "",
             QUEST : "\xc3\x89, acho que suei demais aqui.\aMmmm, se eu pudesse consertar aquele vazamento no encanamento do meu chuveiro...\aAcho que a engrenagem de um daqueles Cogs pequenos bastaria para o conserto.\aVá achar uma engrenagem de um Microempresário para a gente tentar consertar.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Onde está aquela engrenagem que voc\xc3\xaa ia conseguir?" },
    5245 : { GREETING: "",
             QUEST : "\xc3\x89, parece que funcionou.\aMas eu fico solitário quando tomo banho...\aSerá que voc\xc3\xaa poderia pescar um patinho de borracha para me fazer companhia?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não acha o patinho de borracha?" },
    5246 : { QUEST : "O patinho é ótimo, mas...\aTodos aqueles edif\xc3\xadcios aqui em volta me deixam com os nervos em frangalhos.\aEu me sentiria bem melhor se houvesse menos edif\xc3\xadcios por aqui.",
             LEAVING : "",
             COMPLETE : "Ok, agora eu vou tomar banho. Ah, aqui está uma coisinha para voc\xc3\xaa.",
             INCOMPLETE_PROGRESS : "Ainda estou preocupado com os edif\xc3\xadcios.", },
    5251 : { QUEST : "V\xc3\xadtor Vest\xc3\xadbulo devia estar fazendo um show nesta noite.\aOuvi falar que ele estava tendo problemas com o equipamento._where_" },
    5252 : { GREETING: "",
             QUEST : "\xc3\x89 isso a\xc3\xad! Seria bom mesmo aceitar a sua ajuda.\aAqueles Cogs entraram aqui e levaram todas as engrenagens do meu equipamento enquanto eu estava descarregando a caminhonete.\aVoc\xc3\xaa pode me dar uma mãozinha e conseguir de volta o meu microfone?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Cara, eu não consigo cantar sem o microfone." },
    5253 : { GREETING: "",
             QUEST : "Legal, voc\xc3\xaa conseguiu meu microfone de volta.\aValeu, mas...\aEu preciso mesmo do meu teclado para poder fazer um som.\aAcho que um daqueles Aventureiros Corporativos o levaram.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não conseguiu pegar o meu teclado?" },
    5273 : { GREETING: "",
             QUEST : "Legal, voc\xc3\xaa conseguiu meu microfone de volta.\aValeu, mas...\aEu preciso mesmo do meu teclado para poder fazer um som.\aAcho que um daqueles Amizades Fáceis o levaram.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não conseguiu pegar o meu teclado?" },
    5274 : { GREETING: "",
             QUEST : "Legal, voc\xc3\xaa conseguiu meu microfone de volta.\aValeu, mas...\aEu preciso mesmo do meu teclado para poder fazer um som.\aAcho que um daqueles Agiotas o levaram.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não conseguiu pegar o meu teclado?" },
    5275 : { GREETING: "",
             QUEST : "Legal, voc\xc3\xaa conseguiu meu microfone de volta.\aValeu, mas...\aEu preciso mesmo do meu teclado para poder fazer um som.\aAcho que um daqueles Macacos velhos o levaram.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não conseguiu pegar o meu teclado?" },
    5254 : { GREETING: "",
             QUEST : "Tudo em cima! Agora estou na parada.\aSe ao menos eles não tivessem levado meus sapatos de plataforma...\aAqueles sapatos provavelmente acabaram com algum Dr. Celebridade, creio eu.",
             LEAVING : "",
             COMPLETE : "Tudo bem!! Estou pronto agora.\aOlá Brrrgh!!!\aHã? Onde está todo mundo?\aOk, pegue isto e reúna alguns fãs, está bem?",
             INCOMPLETE_PROGRESS : "Não posso me apresentar sem sapatos, né?" },
    5282 : { GREETING: "",
             QUEST : "Tudo em cima! Agora, estou na parada.\aSe ao menos eles não tivessem levado meus sapatos de plataforma...\aAqueles sapatos provavelmente acabaram com algum Rei da Cocada Preta, creio eu.",
             LEAVING : "",
             COMPLETE : "Tudo bem!! Estou pronto agora.\aOlá Brrrgh!!!\aHã? Onde está todo mundo?\aOk, pegue isto e reúna alguns fãs, está bem?",
             INCOMPLETE_PROGRESS : "Não posso me apresentar sem sapatos, né?" },
    5283 : { GREETING: "",
             QUEST : "Tudo em cima! Agora estou na parada.\aSe ao menos eles não tivessem levado meus sapatos de plataforma...\aAqueles sapatos provavelmente acabaram com algum Barão Ladrão, creio eu.",
             LEAVING : "",
             COMPLETE : "Tudo bem!! Estou pronto agora.\aOlá Brrrgh!!!\aHã? Onde está todo mundo?\aOk, pegue isto e reúna alguns fãs, está bem?",
             INCOMPLETE_PROGRESS : "Não posso me apresentar sem sapatos, né?" },
    5284 : { GREETING: "",
             QUEST : "Tudo em cima! Agora, estou na parada.\aSe ao menos eles não tivessem levado meus sapatos de plataforma...\aAqueles sapatos provavelmente acabaram com algum Figurão, creio eu.",
             LEAVING : "",
             COMPLETE : "Tudo bem!! Estou pronto agora.\aOlá Brrrgh!!!\aHã? Onde está todo mundo?\aOk, pegue isto e reúna alguns fãs, está bem?",
             INCOMPLETE_PROGRESS : "Não posso me apresentar sem sapatos, né?" },

    5255 : { QUEST : "Parece que voc\xc3\xaa pode usar mais pontos de risadas.\aTalvez _toNpcName_ entre em um acordo com voc\xc3\xaa.\aNão deixe de firmar o acordo por escrito..._where_" },
    5256 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Trato é trato.",
             QUEST : "Então, voc\xc3\xaa está atrás de pontos de risadas, né?\aSe eu tenho uma proposta para voc\xc3\xaa!?\a\xc3\x89 só tomar conta de alguns Cogs Robôs-chefe para mim...\aA\xc3\xad eu dou uma injeção de ânimo nos seus pontos." },
    5276 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Trato é trato.",
             QUEST : "Então, voc\xc3\xaa está atrás de pontos de risadas, né?\aSe eu tenho uma proposta para voc\xc3\xaa!?\a\xc3\x89 só tomar conta de alguns Cogs Robôs da Lei para mim...\aA\xc3\xad eu dou uma injeção de ânimo nos seus pontos." },
    5257 : { GREETING : "",
             LEAVING : "",
             COMPLETE : "Ok, mas tenho certeza de que falei para voc\xc3\xaa reunir alguns Cogs Robôs da Lei.\aBom, se voc\xc3\xaa está falando, tudo bem, mas, então, fica me devendo uma.",
             INCOMPLETE_PROGRESS : "Acho que voc\xc3\xaa não terminou ainda.",
             QUEST : "Voc\xc3\xaa está dizendo que acabou? Derrotou todos os Cogs?\aVoc\xc3\xaa deve ter entendido errado, nosso trato era para os Cogs Robôs Vendedores.\aTenho certeza de que disse para voc\xc3\xaa derrotar alguns Cogs Robôs Vendedores para mim." },
    5277 : { GREETING : "",
             LEAVING : "",
             COMPLETE : "Ok, mas tenho certeza de que falei para voc\xc3\xaa reunir alguns Cogs Robôs da Lei.\aBom, se voc\xc3\xaa está falando, tudo bem, mas, então, fica me devendo uma.",
             INCOMPLETE_PROGRESS : "Acho que voc\xc3\xaa não terminou ainda.",
             QUEST : "Voc\xc3\xaa está dizendo que acabou? Derrotou todos os Cogs?\aVoc\xc3\xaa deve ter entendido errado, nosso trato era para os Cogs Robôs Mercenários.\aTenho certeza de que disse para voc\xc3\xaa derrotar alguns Cogs Robôs Mercenários para mim." },

    # Eddie the will give you laff point for helping him
    5301 : { QUEST : "Eu não posso ajudar com os pontos de Risada, mas talvez _toNpcName_ faça negócio com voc\xc3\xaa.\aMas ele é um pouco temperamental..._where_" },
    5302 : { GREETING : "",
             LEAVING : "",
             COMPLETE : "Eu te disse o qu\xc3\xaa?!?!\aValeu mesmo! Aqui está o seu ponto de Risada!",
             INCOMPLETE_PROGRESS : "Oi!\aO que está fazendo aqui de novo!",
             QUEST : "Um ponto de Risada? Acho que não!\aClaro, mas só se der um jeito em alguns desses Robôs da Lei antes." },

    # Johnny Cashmere will knit you a large bag if...
    5303 : { QUEST : lTheBrrrgh+" está repleto de Cogs perigosos.\aSe fosse voc\xc3\xaa, carregaria mais piadas por aqui.\aOuvi dizer que  _toNpcName_ pode fazer uma bolsa maior para voc\xc3\xaa se estiver a fim de trabalhar._where_" },
    5304 : { GREETING: "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Deve haver bastante Robôs da Lei lá fora.\aEntão mexa-se!" ,
             QUEST : "Uma bolsa maior?\aEu até poderia arranjar uma proc\xc3\xaa.\aMas vou precisar de fios.\aUns Robôs da Lei roubaram os meus fios ontem de manhã." },
    5305 : { GREETING : "Olá!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Vai atacar mais uns cogs.\aEssa cor ainda não pegou.",
             QUEST : "Esse é um fio bom!\aMas não seria a minha primeira escolha de cor.\aVou te dizer...\aVai lá fora e derrote alguns dos cogs mais dif\xc3\xadceis...\aE eu começo a a trabalhar em tingir este fio." },
    5306 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Eles t\xc3\xaam que estar lá em algum lugar...",
             QUEST : "Bem, este fio está todo tingido. Mas tem um probleminha.\aNão consigo encontrar as minhas agulhas de tricô.\aO último lugar que estavam foi no lago."  },
    5307 : { GREETING : "",
             LEAVING : "Muito obrigado!",
             INCOMPLETE_PROGRESS : "Roma não foi tricotada em um dia!" ,
             QUEST : "Essas são as minhas agulhas.\aEnquanto eu tricoto, que tal fazer uma limpeza em alguns dos prédios grandes?",
             COMPLETE : "\xc3\x93timo trabalho!\aE falando em trabalho ótimo...\aAqui está a sua nova bolsa!" },

    # March Harry can also give you max quest = 4.
    5308 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ouvi dizer que _toNpcName_ tem problemas legais.\aVoc\xc3\xaa pode passar lá e dar uma olhada?_where_"  },
    5309 : { GREETING : "Que bom ver voc\xc3\xaa...",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Rápido, por favor! A rua está transbordando com eles!",
             QUEST : "Os Robôs da Lei tomaram conta daqui.\aTemo que eles vão me levar a julgamento.\aVoc\xc3\xaa poderia me ajudar a tirá-los desta rua?"  },
    5310 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Acho que os ouço vindo por mim...",
             QUEST : "Obrigado. Sinto-me um pouco melhor agora.\a Mas tem mais uma coisa...\aVoc\xc3\xaa poderia ir até a casa de  _toNpcName_ e me conseguir um álibi?_where_"  },
    5311 : { GREETING : "O QUEEE!!!!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não posso ajudá-lo se não encontrar!",
             QUEST : "\xc3\x81libi?! Mas que ótima ideia!\aE traga duas!\aAposto que um Macaco velho deve ter alguns..."  },
    5312 : { GREETING : "Finalmente!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "",
             COMPLETE : "Ufa! Que al\xc3\xadvio é ter isso.\aAqui está a sua recompensa...",
             QUEST : "Súper! \xc3\x89 melhor voc\xc3\xaa voltar até _toNpcName_!"  },

    # Powers Erge, though forgetful, will give you an LP boost
    # if you'll defeat some Cogs for him
    6201 : { QUEST : "Elle \xc3\x89trica precisa de ajuda. Voc\xc3\xaa pode passar lá e dar uma mãozinha a ela?_where_",
             },
    6202 : { GREETING : "",
             LEAVING : "",
             QUEST : "Um cliente! Beleza! Em que posso ajudar?\aComo assim, voc\xc3\xaa me ajudar? AH! Voc\xc3\xaa não é um cliente.\aAgora me lembrei. Voc\xc3\xaa veio para me ajudar com aqueles Cogs horrorosos.\aNa verdade, eu aceitaria sua ajuda, voc\xc3\xaa sendo um cliente ou não.\aSe voc\xc3\xaa fizer uma pequena limpa nas ruas, dou uma coisa a voc\xc3\xaa.",
             INCOMPLETE_PROGRESS : "Se voc\xc3\xaa não quiser eletricidade, não posso ajudar até que derrote aqueles Cogs.",
             COMPLETE : "Bom trabalho com aqueles Cogs, _avName_.\aAgora, voc\xc3\xaa tem certeza de que não quer um choquezinho? Pode ser útil....\aNão? OK, voc\xc3\xaa que sabe.\aHã? Ah sim, lembro. Aqui está. Com certeza, vai ajudar voc\xc3\xaa a deter aqueles Cogs nojentos.\aContinue assim!",
             },

    # Susan Siesta wants to get rich but the Cogs are interfering.
    # Take out some Cog buildings and she'll give you the small backpack
    6206 : { QUEST : "Bem, _avName_, não tenho nada para voc\xc3\xaa agora.\aEspera a\xc3\xad! Acho que a Célia Sesta estava procurando ajuda. Por que não vai encontrá-la?_where_",
             },
    6207 : { GREETING : "",
             LEAVING : "",
             QUEST : "Nunca enriquecerei com aqueles malditos Cogs atrapalhando os meus negócios!\aVoc\xc3\xaa tem que me ajudar, _avName_.\aElimine alguns edif\xc3\xadcios de Cogs para salvar a vizinhança e ajudarei voc\xc3\xaa em sua poupança.",
             INCOMPLETE_PROGRESS : "O que farei agora? Voc\xc3\xaa não conseguiu se livrar dos edif\xc3\xadcios?",
             COMPLETE : "Agora, vou entrar na grana! Agora sim!\aVou passar todo o meu tempo livre pescando. Agora, deixe-me enriquecer sua vida um pouquinho.\aLá vai!",
             },

    # Lawful Linda is fixing her answering machine.
    # Help her & she'll give you a 2LP reward.
    6211 : { QUEST : "Oi, _avName_! Ouvi dizer que a Linda Legal estava procurando voc\xc3\xaa.\aPassa lá para fazer uma visitinha a ela._where_",
             },
    6212 : { GREETING : "",
             LEAVING : "",
             QUEST : "E a\xc3\xad! Nossa, como é bom ver voc\xc3\xaa!\aFiquei trabalhando nesta secretária eletrônica nas horas vagas, mas faltam algumas peças.\aPreciso de mais tr\xc3\xaas varas, e as do Conta-moedinha parecem perfeitas.\aVoc\xc3\xaa poderia tentar encontrar algumas varas de pescar para mim?",
             INCOMPLETE_PROGRESS : "Ainda \xc3\xa0 procura daquelas varas de pescar?",
             },
    6213 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ah, estas aqui já ajudam.\aEngraçado. Eu tinha certeza de que havia um cinto de segurança extra por aqui, mas não consigo encontrá-lo.\aVoc\xc3\xaa pode pegar um de uns Sacos de Dinheiro para mim? Valeu!",
             INCOMPLETE : "Olha, eu só posso ajudar voc\xc3\xaa depois que conseguir aquele cinto de segurança.",
             },
    6214 : { GREETING : "",
             LEAVING : "",
             QUEST : "Agora sim. Vai funcionar que é uma beleza.\aOnde está meu alicate? Não vou poder ajustar isto aqui sem o alicate.\aTalvez as pinças da Mão de vaca ajudem.\aSe voc\xc3\xaa conseguir encontrá-las, dou a voc\xc3\xaa uma coisa que vai ajudar na batalha com os Cogs.",
             INCOMPLETE_PROGRESS : "Nada das pinças ainda, né? Vai procurando.",
             COMPLETE : "Beleza! Agora é só fazer o ajuste aqui.\aParece que agora está funcionando. Estou de novo na ativa!\aNa verdade, falta ainda o telefone. Mas, estou satisfeito com a sua ajuda.\aAcho que isso vai ajudar voc\xc3\xaa com os Cogs. Boa sorte!",
             },

    # Scratch Rocco's back and he'll scratch yours.
    # In fact, he'll give you a 3 LP bonus.
    6221 : { QUEST : "Ouvi dizer que Pedro estava atrás da sua ajuda. Veja o que pode fazer por ele._where_",
             },
    6222 : { GREETING : "",
             LEAVING : "",
             QUEST : "Qualé? Chegou no point certo. Não estou legal.\a\xc3\x89 isso a\xc3\xad, tava procurando ajuda pra me livrar daqueles Cogs. Eles chegam e ficam mandando em mim.\aBem que voc\xc3\xaa podia mandar aqueles Robôs-chefe se aposentarem. Voc\xc3\xaa não vai se arrepender.",
             INCOMPLETE_PROGRESS : "E a\xc3\xad, _avName_, qual foi?\aVai lá atrás dos Robôs-chefe. A gente tem um trato, falou?\aO Pedro aqui tem palavra.",
             COMPLETE : "Qualé, _avName_! Agora, voc\xc3\xaa está bem na fita.\aQuero ver os Robôs-chefe chefiar agora, né não?\aVamo lá! Um tremendo acréscimo pra voc\xc3\xaa. Agora, v\xc3\xaa se não entra em nenhuma fria, falou?",
             },

    # Nat & PJ will get you acquainted with the new
    # HQ. And they'll give you your first suit part
    6231 : { QUEST : "O Zezé ouviu um boato na Alameda do Pijama sobre um Quartel do Robô Mercenário.\aVai lá e veja se consegue ajudá-lo._where_",
             },
    6232 : { GREETING : "",
             LEAVING : "",
             QUEST : "Soube de umas coisas estranhas que estão acontecendo.\aTalvez sejam as pulgas, mas deve ter alguma coisa rolando.\aTodos esses Robôs Mercenários!\aAcho que abriram outro quartel bem na Alameda do Pijama.\aO Py Jama sabe o caminho.\aVá ver _toNpcName_ _where_ Pergunte a ele se viu alguma coisa.",
             INCOMPLETE_PROGRESS : "Ainda não viu o Py Jama? O que voc\xc3\xaa está esperando?\aAi, essas malditas pulgas!",
             },
    6233 : { GREETING : "",
             LEAVING : "",
             QUEST : "E a\xc3\xad, _avName_, para onde voc\xc3\xaa está indo?\aPara o Quartel dos Robôs Mercenários?? Eu não vi nada.\aVoc\xc3\xaa pode ir até o final da Alameda do Pijama e ver se é verdade?\aEncontre alguns Cogs do Robô Mercenário no quartel, derrote alguns deles e venha me contar.",
             INCOMPLETE_PROGRESS : "Já encontrou o Quartel? Voc\xc3\xaa precisará derrotar alguns Robôs Mercenários para localizá-lo.",
             },
    6234 : { GREETING : "",
             LEAVING : "",
             QUEST : "O qu\xc3\xaa?! Existe mesmo um Quartel de Robôs Mercenários?\a\xc3\x89 melhor voc\xc3\xaa ir e contar a Zezé agora mesmo!\aQuem poderia imaginar que existiria um Quartel de Cogs na rua bem em frente a ele?",
             INCOMPLETE_PROGRESS : "O que Zezé disse? Voc\xc3\xaa ainda não o encontrou?",
             },
    6235 : { GREETING : "",
             LEAVING : "",
             QUEST : "Estou tentado para ouvir o que o Py Jamas disse.\aHmm... Precisamos de mais informações sobre esse negócio de Cog, mas preciso me livrar dessas pulgas!\aEu sei! VOC\xc3\x8a pode descobrir mais coisas!\aVá derrotar os Robôs Mercenários no Quartel até encontrar alguns planos, depois venha direto pra cá!",
             INCOMPLETE_PROGRESS : "Nada ainda? Continue procurando esses Cogs!\aEles devem ter algum plano!",
             COMPLETE : "Voc\xc3\xaa conseguiu os planos?\aExcelente! Vejamos o que diz aqui.\aEntendi... os Robôs Mercenários constru\xc3\xadram uma Casa da Moeda para fabricar grana Cog.\aDeve estar CHEIA de Robôs Mercenários. Precisamos averiguar.\aE se voc\xc3\xaa se disfarçasse? Hmmm...Já sei! Acho que tenho uma peça de vestimenta de Cog aqui em algum lugar....\aAqui está! Isto aqui é para compensar o trabalho. Agradeço novamente pela ajuda!",
             },

    # The Countess can't concentrate on counting her sheep with all
    # these Cogs around. Clean up a bit and she'll reward you handsomely.
    # Reward: MaxMoneyReward 705 - 150 jellybeans
    6241 : { QUEST : "A Condessa está procurando voc\xc3\xaa por toda parte! Visite-a logo para que pare de ligar _where_",
             },
    6242 : { GREETING : "",
             LEAVING : "",
             QUEST : "_avName_, conto com a sua ajuda!\aSabe, esses Cogs estão fazendo tanto barulho que eu simplesmente não consigo me concentrar.\aPerco a conta dos carneirinhos a todo instante!\aSe voc\xc3\xaa acabar com esse barulho, te dou uma ajuda! Pode contar com isso!\aMas, onde eu parei mesmo? Ah sim: cento e trinta e seis, cento e trinta e sete....",
             INCOMPLETE_PROGRESS : "Quatrocentos e quarenta e dois... Quatrocentos e quarenta e tr\xc3\xaas...\aO qu\xc3\xaa? Voc\xc3\xaa já voltou? Mas ainda tem tanto barulho!\aEssa não, perdi a conta novamente.\a Um...dois...tr\xc3\xaas....",
             COMPLETE : "Quinhentos e noventa e tr\xc3\xaas... Quinhentos e noventa e quatro...\aOlá? Ah, eu sabia que poderia contar com a sua ajuda! Agora, o sil\xc3\xaancio voltou.\aPegue aqui, por todos esses Destruidores de Números.\aContar? Agora preciso começar a contar tudo outra vez! Um...dois....",
             },

    # Zari needs you to run some errands for her and maybe
    # wipe out some Cogs along the way. She'll make it worthwhile
    # though, she'll give you 4 LP if you run the gauntlet.
    6251 : { QUEST : "Pobre Zéfiro, o z\xc3\xadper dela quebrou e, agora, ela não consegue fazer as entregas de seus clientes. Ela certamente precisa de sua ajuda._where_",
             },
    6252 : { GREETING : "",
             LEAVING : "",
             QUEST : "Oi _avName_. Voc\xc3\xaa está aqui para ajudar com minhas entregas?\aIsso é ótimo! Com esse z\xc3\xadper quebrado é muito dif\xc3\xadcil fazer as entregas sozinha.\aDeixe-me ver... Ok, vai ser fácil. O Vaqueiro George pediu uma c\xc3\xadtara semana passada.\aVoc\xc3\xaa poderia levá-la para ele? _where_",
             INCOMPLETE_PROGRESS : "Oi! Esqueceu alguma coisa? O Vaqueiro George está esperando pela c\xc3\xadtara.",
             },
    6253 : { GREETING : "",
             LEAVING : "",
             QUEST : "Minha c\xc3\xadtara! Finalmente! Caramba, mal posso esperar para tocá-la.\aPoderia agradecer \xc3\xa0 Zéfiro por mim?",
             INCOMPLETE_PROGRESS : "Obrigado novamente pela c\xc3\xadtara. A Zéfiro não tem mais entregas para voc\xc3\xaa fazer?",
             },
    6254 : { GREETING : "",
             LEAVING : "",
             QUEST : "Essa foi rápida. Qual será o próximo item da minha lista?\aAh sim! Mestre Mário pediu um Zamboni. Aquele zombeteiro.\aPoderia levar para ele?_where_",
             INCOMPLETE_PROGRESS : "Aquele Zamboni precisa ser levado para o Mestre Mário._where_",
             },
    6255 : { GREETING : "",
             LEAVING : "",
             QUEST : "Tudo certo! O Zamboni que eu pedi!\aAgora, se não houvesse tantos Cogs por a\xc3\xad, eu teria algum tempo para usá-lo.\aSeja gentil e cuide de alguns desses Robôs Mercenários para mim, tudo bem?",
             INCOMPLETE_PROGRESS : "Esses Robôs Mercenários são durões, não são? Assim, eu não consigo testar o meu Zamboni.",
             },
    6256 : { GREETING : "",
             LEAVING : "",
             QUEST : "Excelente! Agora, eu posso testar o meu Zamboni.\aDiga \xc3\xa0 Zéfiro que eu estarei lá para fazer um outro pedido na próxima semana.",
             INCOMPLETE_PROGRESS : "Por enquanto é só isso. A Zéfiro não está esperando por voc\xc3\xaa?"
             },
    6257 : { GREETING : "",
             LEAVING : "",
             QUEST : "Então, o Mestre Mário ficou satisfeito com o Zamboni? Excelente.\aQuem é o próximo? Ah, o Bob Bocão pediu uma almofada zabuton com listras de zebra.\aAqui está! Poderia ir até a casa dele?_where_",
             INCOMPLETE_PROGRESS : "Acho que o Bob Bocão precisa da almofada zabuton para meditar.",
             },
    6258 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ah, minha almofada zabuton finalmente. Agora, eu posso meditar.\aQuem consegue se concentrar com aquela algazarra? Todos aqueles Cogs!\aJá que voc\xc3\xaa está aqui, poderia cuidar de alguns desses Cogs?\aSó assim eu poderei usar minha almofada zabuton em paz.",
             INCOMPLETE_PROGRESS : "Ainda há muito barulho com esses Cogs! Quem consegue se concentrar?",
             },
    6259 : { GREETING : "",
             LEAVING : "",
             QUEST : "Paz e sil\xc3\xaancio afinal. Obrigado, _avName_.\aDiga \xc3\xa0 Zéfiro que estou muito satisfeito. OM....",
             INCOMPLETE_PROGRESS : "A Zéfiro ligou procurando por voc\xc3\xaa. \xc3\x89 melhor voc\xc3\xaa ir ver o que ela precisa.",
             },
    6260 : { GREETING : "",
             LEAVING : "",
             QUEST : "Estou feliz em saber que o Bob Bocão está satisfeito com sua almofada zabuton de zebra.\aAh, estas z\xc3\xadnias acabaram de chegar para a Rosa Sonada.\aJá que voc\xc3\xaa parece tão animado para fazer entregas, talvez possa levar essas z\xc3\xadnias para ela, não é?_where_",
             INCOMPLETE_PROGRESS : "Essas z\xc3\xadnias vão murchar se voc\xc3\xaa não fizer logo a entrega.",
             },
    6261 : { GREETING : "",
             LEAVING : "",
             QUEST : "Que lindas z\xc3\xadnias! Certamente que é entrega da Zéfiro.\aQuer dizer, é SUA entrega, _avName_. Agradeça \xc3\xa0 Zéfiro por mim!",
             INCOMPLETE_PROGRESS : "Não se esqueça de agradecer \xc3\xa0 Zéfiro pelas z\xc3\xadnias!",
             },
    6262 : { GREETING : "",
             LEAVING : "",
             QUEST : "Que bom que voltou, _avName_. Voc\xc3\xaa é bastante veloz.\aVejamos... Qual é o próximo item da lista a ser entregue? Discos de forró para Jatha Cordada._where_",
             INCOMPLETE_PROGRESS : "Tenho certeza de que Jatha Cordada está esperando por esses discos de forró.",
             },
    6263 : { GREETING : "",
             LEAVING : "",
             QUEST : "Discos de forró? Não me lembro de ter pedido discos de forró.\aAh, aposto que foi Denis Nar quem pediu._where_",
             INCOMPLETE_PROGRESS : "Não, esses discos de forró são para Denis Nar._where_",
             },
    6264 : { GREETING : "",
             LEAVING : "",
             QUEST : "Finalmente, meus discos de forró! Pensei que a Zéfiro tivesse se esquecido.\aPoderia levar essa abobrinha para ela? Ela encontrará alguém que esteja querendo uma. Valeu!",
             INCOMPLETE_PROGRESS : "Eu já tenho muitas abobrinhas. Leve esta para Zéfiro.",
             },
    6265 : { GREETING : "",
             LEAVING : "",
             QUEST : "Abobrinha? Hmm. Bem, alguém irá querer, tenho certeza.\aOk, estamos quase terminando com a minha lista. Mais uma entrega a fazer.\aNen\xc3\xaa Crespo pediu um paletó zoot._where_",
             INCOMPLETE_PROGRESS : "Se voc\xc3\xaa não entregar esse paletó zoot ao Nen\xc3\xaa Crespo,\a ele ficará todo amarrotado.",
             },
    6266 : { GREETING : "",
             LEAVING : "",
             QUEST : "Era uma vez... Ah! Voc\xc3\xaa não está aqui para ouvir uma história, não é?\a\xc3\x89 a entrega do meu terno zoot? Beleza! Uau, isso aqui é demais.\aEi, poderia dar um recado meu para a Zéfiro? Precisarei de abotoaduras de zircônio para usar com o paletó. Valeu!",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa deu o meu recado \xc3\xa0 Zéfiro?",
             COMPLETE : "Abotoaduras de zircônio, certo? Bem, verei o que posso fazer por ele.\aSeja como for, voc\xc3\xaa tem sido muito útil e não posso deixar voc\xc3\xaa ir sem nada.\aAqui está um GRANDE acréscimo para ajudar a derrotar esses Cogs!",
             },

    # Drowsy Dave will give you teleport access to DL
    # if he can stay awake long enough for you to finish.
    6271 : { QUEST : "Solano Sonolento está tendo problemas e voc\xc3\xaa talvez possa ajudá-lo. Por que voc\xc3\xaa não dá uma passada na loja dele?_where_",
             },
    6272 : { GREETING : "",
             LEAVING : "",
             QUEST : "O qu\xc3\xaa? Hã? Eu devo ter cochilado.\aSabe, esses edif\xc3\xadcios de Cogs estão cheios de máquinas que realmente me dão um sono.\aEu ouço esse zumbido o dia inteiro e...\aHã? Ah, sim, está certo. Se voc\xc3\xaa pudesse se livrar de alguns desses edif\xc3\xadcios de Cogs, eu conseguiria ficar acordado.",
             INCOMPLETE_PROGRESS : "Zzzzz...hã? Ah, é voc\xc3\xaa, _avName_.\aJá está de volta? Eu só estava tirando uma sonequinha.\aVolte quando acabar com esses edif\xc3\xadcios.",
             COMPLETE : "O qu\xc3\xaa? Eu ca\xc3\xad no sono um minutinho.\aAgora que aqueles edif\xc3\xadcios de Cogs viraram pó, finalmente posso relaxar.\aValeu pela ajuda, _avName_.\aVejo voc\xc3\xaa depois! Acho que vou tirar uma sonequinha.",
             },

    # Teddy Blair has a piece of a cog suit to give you if you will
    # clear out some cogs. Of course, his ear plugs make it tough.
    6281 : { QUEST : "Vá em frente e ligue para o Ursinho de P. Lúcia. Ele tem um trabalho para voc\xc3\xaa._where_",
             },
    6282 : { GREETING : "",
             LEAVING : "",
             QUEST : "O que voc\xc3\xaa disse? Não, eu não tenho um baralho pra voc\xc3\xaa.\aAh, é um trabalho! Por que voc\xc3\xaa não disse logo? Voc\xc3\xaa precisa falar alto.\aEsses Cogs não me deixam hibernar. Se voc\xc3\xaa ajudar a tornar a Sonholândia mais silenciosa,\aeu lhe darei uma coisinha.",
             INCOMPLETE_PROGRESS: "Voc\xc3\xaa derrotou os bogs? Que bogs?\aAh, os Cogs! Por que voc\xc3\xaa não disse logo?\aHmm, ainda tem barulho. O que acha de derrotar mais alguns?",
             COMPLETE : "Voc\xc3\xaa se divertiu? Hã? Ah!\aVoc\xc3\xaa conseguiu! Beleza. Muito legal voc\xc3\xaa ter me ajudado.\aEu achei isso nos fundos da loja, mas não tem utilidade para mim.\aTalvez voc\xc3\xaa descubra o que fazer com isso. Até logo, _avName_!",
             },

    # William Teller needs help! Those darn Cashbots swiped his 3
    # money bags to use in the Mint! Retrieve them and he'll give you
    # another cog Suit piece.
    6291 : { QUEST : "Os Cogs arrombaram o Banco A Fraldinha de Dormir! Vá até o Guilherme Sonoleve e veja se voc\xc3\xaa pode ajudá-lo.",
             },
    6292 : { QUEST : "Aqueles malditos Cogs do Robô Mercenário! Eles roubaram meus abajures de leitura!\aEu preciso deles de volta agora mesmo. Voc\xc3\xaa pode procurar por eles?\aSe voc\xc3\xaa encontrar meus abajures, talvez eu possa ajudar a encontrar o Diretor Financeiro.\aDepressa!",
             INCOMPLETE_PROGRESS : "Eu preciso dos abajures de volta. Continue procurando!",
             COMPLETE : "Voc\xc3\xaa voltou! E trouxe meus abajures!\aNão tenho como agradecer o favor, mas posso dar isto a voc\xc3\xaa.",
             },

    # Help Nina Nightlight get a bed in stock -
    # she'll give you a suit part
    7201 : { QUEST : "Nana de Nina estava \xc3\xa0 sua procura, _avName_. Ela precisa de ajuda._where_",
             },
    7202 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ah! Estou tão feliz em ver voc\xc3\xaa, _avName_. Espero que possa me ajudar!\aAqueles malditos Cogs assustaram o pessoal da entrega e não tenho mais camas no estoque.\aPoderia ir ao Pedro Fuso e trazer uma cama para mim?_where_",
             INCOMPLETE_PROGRESS : "O Pedro tinha alguma cama? Tinha certeza de que ele teria uma.",
             COMPLETE : "",
             },
    7203 : { GREETING : "",
             LEAVING : "",
             QUEST : "Uma cama? Isso mesmo, aqui está uma prontinha para viagem.\aEntregue a cama pra Nana por mim, OK? Cama, Nana...\a\"Rimou!\" Há-há!\aMuito engraçado. Não? Bem, mas leve para ela, por favor.",
             INCOMPLETE_PROGRESS : "A Nana gostou da cama?",
             COMPLETE : "",
             },
    7204 : { GREETING : "",
             LEAVING : "",
             QUEST : "Essa cama não está legal. Ela é muito simples.\aVoc\xc3\xaa poderia ir até lá e ver se ele tem alguma coisa mais sofisticada?\aTenho certeza de que não vai demorar nadinha.",
             INCOMPLETE_PROGRESS : "Estou certa de que o Pedro tem uma cama mais sofisticada.",
             COMPLETE : "",
             },
    7205 : { GREETING : "",
             LEAVING : "",
             QUEST : "Não acertei na mosca com essa cama, não é? Tenho uma aqui que servirá.\aSó tem um pequeno problema: é preciso montá-la primeiro.\aEnquanto eu resolvo esse problema, voc\xc3\xaa pode se livrar de alguns Cogs que estão lá fora?\aAqueles terr\xc3\xadveis Cogs jogaram uma chave inglesa nos móveis.\aVolte quando terminar e a cama estará pronta.",
             INCOMPLETE_PROGRESS : "Ainda não terminei a montagem da cama.\aQuando voc\xc3\xaa tiver acabado com os Cogs, ela estará pronta.",
             COMPLETE : "",
             },
    7206 : { GREETING : "",
             LEAVING : "",
             QUEST : "E a\xc3\xad _avName_!\aVoc\xc3\xaa fez um excelente trabalho com aqueles Cogs.\aA cama já está prontinha. Voc\xc3\xaa pode entregá-la para mim?\aAgora que aqueles Cogs se foram, as coisas estão rápidas por aqui!",
             INCOMPLETE_PROGRESS : "Acho que a Nana está esperando pela entrega da cama.",
             COMPLETE : "Que cama adorável!\aAgora, meus clientes ficarão satisfeitos. Obrigada, _avName_.\aOlha só, talvez voc\xc3\xaa possa usar isto. Alguém deixou isso aqui.",
             },
    7209 : { QUEST : "Vá até a Lua de Mel. Ela precisa de ajuda._where_",
             },
    7210 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ah! Estou tão feliz em ver voc\xc3\xaa, _avName_. Eu preciso muito de ajuda!\aNão consigo tirar o meu sono reparador há séculos. Veja voc\xc3\xaa, aqueles Cogs roubaram a minha colcha.\aVoc\xc3\xaa pode correr e ver se o Marcelo tem alguma coisa em azul?_where_",
             INCOMPLETE_PROGRESS : "O que o Marcelo falou sobre a colcha azul?",
             COMPLETE : "",
             },
    7211 : { GREETING : "",
             LEAVING : "",
             QUEST : "Então, a Mel quer uma colcha, né?\aDe que cor? AZUL?!\aBem, eu terei de fazer uma especialmente para ela. Tudo o que eu tenho aqui é em vermelho.\aEscuta... Se voc\xc3\xaa for derrotar alguns Cogs lá fora, farei uma colcha azul especialmente para ela.\aColchas azuis... O que será da próxima vez?",
             INCOMPLETE_PROGRESS : "Ainda estou trabalhando na colcha azul, _avName_. Continue a derrotar esses Cogs!",
             COMPLETE : "",
             },
    7212 : { GREETING : "",
             LEAVING : "",
             QUEST : "Que bom ver voc\xc3\xaa novamente. Tenho algo pra voc\xc3\xaa!\aAqui está a colcha, e é azul. Ela vai adorar.",
             INCOMPLETE_PROGRESS : "A Mel gostou da colcha?",
             COMPLETE : "",
             },
    7213 : { GREETING : "",
             LEAVING : "",
             QUEST : "Minha colcha? Não, não está legal.\a\xc3\x89 XADREZ! Como alguém pode dormir com uma estampa tão CHAMATIVA?\aVoc\xc3\xaa terá que levá-la de volta e trazer uma outra colcha.\aTenho certeza de que ele tem outras.",
             INCOMPLETE_PROGRESS : "Eu simplesmente não vou aceitar uma colcha xadrez. Veja o que Marcelo pode fazer.",
             COMPLETE : "",
             },
    7214 : { GREETING : "",
             LEAVING : "",
             QUEST : "O qu\xc3\xaa? Ela não gosta de XADREZ?\aHmm... Deixe-me ver o que eu tenho aqui.\aIsso vai levar algum tempo. Por que voc\xc3\xaa não cuida de alguns Cogs enquanto eu tento encontrar algo diferente?\aTerei alguma coisa quando voc\xc3\xaa estiver de volta.",
             INCOMPLETE_PROGRESS : "Ainda estou procurando uma colcha diferente. Como está indo com os Cogs?",
             COMPLETE : "",
             },
    7215 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ei, bom trabalho com os Cogs!\aAqui está, é azul e não é xadrez.\aEspero que ela goste de estampado.\aLeve a colcha para a Mel.",
             INCOMPLETE_PROGRESS : "Isso é tudo o que eu tenho para voc\xc3\xaa agora.\aPor favor, leve esta colcha para a Mel.",
             COMPLETE : "Ah! Que linda! Estampado combina muito bem comigo.\a\xc3\x89 hora do meu sono reparador! Até logo, _avName_.\aO qu\xc3\xaa? Voc\xc3\xaa ainda está aqui? Não v\xc3\xaa que estou tentando dormir?\aTome isto aqui e me deixe descansar. Devo estar medonha!",
             },

    7218 : { QUEST : "Dafne Sonolinda precisa de ajuda._where_",
             },
    7219 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ah, _avName_, estou tão feliz em ver voc\xc3\xaa! Aqueles Cogs levaram meus travesseiros.\aVoc\xc3\xaa pode ver se o Lel\xc3\xaa tem alguns travesseiros?_where_\aTenho certeza de que ele pode ajudar.",
             INCOMPLETE_PROGRESS : "O Lel\xc3\xaa tem algum travesseiro para mim?",
             COMPLETE : "",
             },
    7220 : { GREETING : "",
             LEAVING : "",
             QUEST : "Como vai? A Dafne precisa de alguns travesseiros, né? Bem, voc\xc3\xaa veio ao lugar certo, parceria!\aHá mais travesseiros aqui do que espinhos em um cacto.\aAqui está, _avName_. Leve estes para Dafne, com os meus cumprimentos.\a\xc3\x89 sempre um prazer ajudar uma mocinha.",
             INCOMPLETE_PROGRESS : "Os travesseiros eram macios o suficiente para uma pequena dama?",
             COMPLETE : "",
             },
    7221 : { GREETING : "",
             LEAVING : "",
             QUEST : "Voc\xc3\xaa trouxe os travesseiros! Valeu!\aEi, espere um segundo! Esses travesseiros são muito macios.\aMacios demais para mim. Preciso de travesseiros mais duros.\aLeve estes de volta para o Lel\xc3\xaa e veja o que mais ele tem. Valeu.",
             INCOMPLETE_PROGRESS : "Não! Muito macios. Peça ao Lel\xc3\xaa outros travesseiros.",
             COMPLETE : "",
             },
    7222 : { GREETING : "",
             LEAVING : "",
             QUEST : "Muito macios, né? Bem, deixe-me ver o que tenho....\aHmm... Eu achava que tinha um montão de travesseiros duros. Onde eles estão?\aAh! Lembrei. Eu estava vendo se conseguia devolv\xc3\xaa-los, então devem estar no estoque.\aQue tal eliminar alguns desses edif\xc3\xadcios de Cogs lá fora enquanto eu pego os travesseiros no estoque, parceria?",
             INCOMPLETE_PROGRESS : "Os edif\xc3\xadcios de Cog são duros de roer. Mas esses travesseiros não são.\aContinuarei procurando.",
             COMPLETE : "",
             },
    7223 : { GREETING : "",
             LEAVING : "",
             QUEST : "Já está de volta? Está tudo bem. Veja, encontrei os travesseiros que a Dafne queria.\aAgora é só levar para ela. Eles são duros o suficiente para quebrar um dente!",
             INCOMPLETE_PROGRESS : "\xc3\x89, esses travesseiros são bastante duros. Espero que a Dafne goste deles.",
             COMPLETE : "Eu sabia que o Lel\xc3\xaa teria alguns travesseiros mais duros.\aAh sim, estes são perfeitos. Bons e duros.\aPor acaso esta peça de vestimenta de Cog seria útil para voc\xc3\xaa? Pode levar.",
             },

    # Sandy Sandman lost her pajamas but Big Mama
    # and Cat can help her out. If you hang in there,
    # you'll get another Cog Suit part.
    7226 : { QUEST : "Passe lá na Cuca P. Gol. Ela perdeu o pijama._where_",
             },
    7227 : { GREETING : "",
             LEAVING : "",
             QUEST : "Não tenho pijamas! Eles sumiram!\aO que vou fazer? Ah! Já sei!\aVá até a Mama. Ela terá pijamas para mim._where_",
             INCOMPLETE_PROGRESS : "A Mama tem pijamas para mim?",
             COMPLETE : "",
             },
    7228 : { GREETING : "",
             LEAVING : "",
             QUEST : "E a\xc3\xad, pequeno Toon? A Mama tem os melhores pijamas das Bahamas.\aAh, quer algo para a Cuca P. Gol, né? Bem, deixe-me ver o que tenho aqui.\aAqui está. Agora, ela pode dormir com estilo!\aVoc\xc3\xaa pode correr e levar isso para ela? Não posso deixar a loja sozinha agora.\aObrigada, _avName_. Vejo voc\xc3\xaa por a\xc3\xad!",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa precisa levar esse pijama para a Cuca P. Gol._where_",
             COMPLETE : "",
             },
    7229 : { GREETING : "",
             LEAVING : "",
             QUEST : "A Mama mandou esse para mim? Ah...\aEla não tem nenhum pijama com pés?\aEu sempre uso pijamas com pés. Todo mundo usa esse tipo de pijama...\aLeve este de volta e peça a ela que encontre um com pés.",
             INCOMPLETE_PROGRESS : "Meu pijama precisa ter pés. Veja o que a Mama pode fazer.",
             COMPLETE : "",
             },
    7230 : { GREETING : "",
             LEAVING : "",
             QUEST : "Pés? Deixe-me pensar....\aEspere a\xc3\xad! Eu tenho um perfeito!\aTchan! Pijama com pés. Um lindo pijama azul com pés. O melhor de toda a face da terra.\aVoc\xc3\xaa pode levar para ela? Valeu!",
             INCOMPLETE_PROGRESS : "A Cuca P. Gol gostou do pijama azul com pés?",
             COMPLETE : "",
             },
    7231 : { GREETING : "",
             LEAVING : "",
             QUEST : "Bem, este TEM pés, mas não posso usar pijama azul!\aPergunte \xc3\xa0 Mama se ela tem uma cor diferente.",
             INCOMPLETE_PROGRESS : "Tenho certeza de que a Mama tem pijamas em uma cor diferente e com pés.",
             COMPLETE : "",
             },
    7232 : { GREETING : "",
             LEAVING : "",
             QUEST : "Que pena. Estes são os únicos pijamas com pés que eu tenho.\aAh, tive uma ideia. Vá perguntar \xc3\xa0 outra Cuca. Ela talvez tenha algum pijama com pés._where_",
             INCOMPLETE_PROGRESS : "Não, aqueles são os únicos que eu tenho. Vá até a outra Cuca para ver o que ela tem._where_",
             COMPLETE : "",
             },
    7233 : { GREETING : "",
             LEAVING : "",
             QUEST : "Pijama com pés? Sem dúvida.\aComo assim, este é azul? Ela não quer azul?\aNossa, vai ser um pouco dif\xc3\xadcil. Veja, que tal este?\aEle não é azul e TEM pés.",
             INCOMPLETE_PROGRESS : "Eu adoro marrom, voc\xc3\xaa não?\aEspero que a Cuca P. Gol goste....",
             COMPLETE : "",
             },
    7234 : { GREETING : "",
             LEAVING : "",
             QUEST : "Não, este não é azul, mas ninguém com o meu tom de pele poderia usar marrom.\aNão e não. Ele vai fazer o caminho de volta, e voc\xc3\xaa irá com ele! Veja o que mais a Cuca tem.",
             INCOMPLETE_PROGRESS : "A Cuca deve ter mais pijamas. Nada de marrom!",
             COMPLETE : "",
             },
    7235 : { GREETING : "",
             LEAVING : "",
             QUEST : "Não pode ser marrom também. Hmm....\aEu sei que tenho outros.\aVai demorar um pouquinho para encontrá-los. Vamos fazer um trato.\aEu procuro outro pijama se voc\xc3\xaa derrotar alguns desses edif\xc3\xadcios de Cog. Eles perturbam demais.\aTerei o pijama quando voc\xc3\xaa voltar, _avName_.",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa precisa eliminar mais alguns edif\xc3\xadcios de Cog enquanto eu procuro outro pijama.",
             COMPLETE : "",
             },
    7236 : { GREETING : "",
             LEAVING : "",
             QUEST : "Voc\xc3\xaa fez um excelente trabalho com esses Cogs! Valeu!\aAchei este pijama para a Cuca P. Gol; espero que ela goste.\aLeve-o para ela. Obrigada.",
             INCOMPLETE_PROGRESS : "A Cuca P. Gol está esperando pelo pijama, _avName_.",
             COMPLETE : "Um pijama fúcsia com pés! Perr-feito!\aAh, agora estou pronta. Vejamos....\aAcho que devo lhe dar alguma coisa por ter me ajudado.\aTalvez voc\xc3\xaa possa usar isto. Alguém deixou aqui.",
             },

    # Smudgy Mascara needs Wrinkle Cream but
    # 39's missing ingredients. Help them out
    # and get a piece of Cog suit
    7239 : { QUEST : "Vá até a Máki Agem. Ela está procurando ajuda._where_",
             },
    7240 : { GREETING : "",
             LEAVING : "",
             QUEST : "Aqueles malditos Cogs levaram meu creme para rugas!\aMeus clientes PRECISAM do creme para rugas enquanto eu trabalho neles.\aVá até o Dedé Descanso e veja se ele tem a minha fórmula especial no estoque._where_",
             INCOMPLETE_PROGRESS : "Eu me recuso a trabalhar em alguém sem o creme para rugas.\aVeja o que o Dedé Descanso tem para mim.",
             },
    7241 : { GREETING : "",
             LEAVING : "",
             QUEST : "A Máki Agem é uma figura exigente. Ela não vai se contentar com a minha fórmula comum.\aIsso significa que eu precisarei de alguns corais de couve-flor, meu ingrediente especial supersecreto. Mas eu não tenho nada no estoque.\aVoc\xc3\xaa poderia pescar alguns na lagoa? Assim que voc\xc3\xaa conseguir os corais, eu farei um lote de creme para a Máki Agem.",
             INCOMPLETE_PROGRESS : "Precisarei do coral de couve-flor para fazer o lote de creme para rugas.",
             },
    7242 : { GREETING : "",
             LEAVING : "",
             QUEST : "Uau, que belo coral de couve-flor!\aOk, vejamos... Um pouco disto e uma pitada daquilo... Agora, um bocado de alga-marinha.\aEssa não, onde está a alga-marinha? Parece que estou sem alga-marinha também.\aVoc\xc3\xaa pode voltar \xc3\xa0 lagoa e pescar uma boa alga-marinha viscosa?",
             INCOMPLETE_PROGRESS : "Nem uma laminazinha de alga-marinha viscosa na loja.\aNão posso fazer o creme sem ela.",
             },
    7243 : { GREETING : "",
             LEAVING : "",
             QUEST : "Aaaah! Que ótima alga-marinha viscosa voc\xc3\xaa trouxe, _avName_.\aAgora, é só espremer algumas pérolas no pilão.\aIh, onde está o meu pilão? Como vou fazer sem o pilão?\aAposto que aquele maldito Agiota o pegou quando esteve aqui!\aVoc\xc3\xaa precisa me ajudar a encontrá-lo! Ele estava indo ao Quartel do Robô Mercenário!",
             INCOMPLETE_PROGRESS : "Eu simplesmente não consigo triturar as pérolas sem um pilão.\aMalditos Agiotas!",
             },
    7244 : { GREETING : "",
             LEAVING : "",
             QUEST : "\xc3\x93timo! Voc\xc3\xaa trouxe o meu pilão!\aAgora voltemos ao trabalho. Triture aqui... Misture lá e...\aPronto! Diga \xc3\xa0 Máki Agem que é de boa qualidade e está fresquinho.",
             INCOMPLETE_PROGRESS : "Voc\xc3\xaa precisa entregar isso para a Máki Agem enquanto está fresco.\aEla é muito exigente.",
             COMPLETE : "O Dedé Descanso não tinha frasco de creme maior que este? Não?\aBem, acho que vou pedir mais quando o meu acabar.\aAté logo, _avName_.\aO qu\xc3\xaa? Voc\xc3\xaa ainda está aqui? Não v\xc3\xaa que estou tentando trabalhar?\aTome isto aqui.",
             },

    # Lawbot HQ part quests
    11000 : { GREETING : "",
              LEAVING : "",
              QUEST : "Se está interessado em peças de disfarce de Robôs da Lei, visite _toNpcName_.\aOuvi dizer que ele precisa de ajuda na sua pesquisa sobre o clima._where_",
              },
    11001 : { GREETING : "",
              LEAVING : "",
              QUEST : "Sim, sim. Eu tenho peças de disfarce de Robôs da Lei.\aMas não tenho interesse nelas.\aO foco da minha pesquisa são as flutuações na temperatura ambiente de Toontown.\aEu troco com voc\xc3\xaa as minhas peças de disfarce por termômetros de cogs.\aVoc\xc3\xaa pode começar em %s." % GlobalStreetNames[2100][-1],
              INCOMPLETE_PROGRESS : "Tentou procurar em %s?" % GlobalStreetNames[2100][-1],
              COMPLETE : "Ah, ótimo!\aComo eu temia...\aAh, é! Aqui está a sua peça de disfarce.",
             },

    11002 : { GREETING : "",
              LEAVING : "",
              QUEST : "Para mais peças de disfarce, visite _toNpcName_ de novo.\aOuvi dizer que ele precisa de assistentes de pesquisa._where_",
              },
    11003 : { GREETING : "",
              LEAVING : "",
              QUEST : "Mais peças de disfarce de Robô da Lei?\aBem, se voc\xc3\xaa insiste...\amas eu vou precisar de outro termômetro de Cog.\aDesta vez, procure em %s." % GlobalStreetNames[2200][-1],
              INCOMPLETE_PROGRESS : "Voc\xc3\xaa está procurando em %s, certo?" % GlobalStreetNames[2200][-1],
              COMPLETE : "Obrigado!\aE aqui está a sua peça de disfarce.",
             },
    11004 : { GREETING : "",
              LEAVING : "",
              QUEST : "Se precisa de mais peças de disfarce de Robô da Lei, vá falar com o _toNpcName_.\aOuvi que ele ainda precisa de ajuda com a pesquisa sobre o clima._where_",
              },
    11005 : { GREETING : "",
              LEAVING : "",
              QUEST : "Voc\xc3\xaa está me saindo bastante útil!\aVoc\xc3\xaa pode dar uma ollhada em %s?" % GlobalStreetNames[2300][-1],
              INCOMPLETE_PROGRESS : "Tem certeza de que está procurando em %s?" % GlobalStreetNames[2300][-1],
              COMPLETE : "Humm, não gostei muito da apar\xc3\xaancia disto...\amas aqui está a sua peça de disfarce...",
             },
    11006 : { GREETING : "",
              LEAVING : "",
              QUEST : "Voc\xc3\xaa-sabe-quem precisa de mais medições de temperatura.\aD\xc3\xaa uma passada se quiser mais uma peça de disfarce._where_",
              },
    11007 : { GREETING : "",
              LEAVING : "",
              QUEST : "Já de volta?\aQue dedicação...\aA próxima parada é %s." % GlobalStreetNames[1100][-1],
              INCOMPLETE_PROGRESS : "Voc\xc3\xaa já tentou observar %s?" % GlobalStreetNames[1100][-1],
              COMPLETE : "Isso! Parece que voc\xc3\xaa está pegando o jeito da coisa!\aA sua peça de disfarce...",
             },
    11008 : { GREETING : "",
              LEAVING : "",
              QUEST : "Se estiver a fim de mais uma peça de disfarce de Robô da Lei..._where_",
              },
    11009 : { GREETING : "",
              LEAVING : "",
              QUEST : "Engraçado encontrar voc\xc3\xaa aqui!\aAgora, eu preciso de medições em %s." % GlobalStreetNames[1200][-1],
              INCOMPLETE_PROGRESS : "Voc\xc3\xaa está procurando em %s, certo?" % GlobalStreetNames[1200][-1],
              COMPLETE : "Muito obrigado.\aO seu disfarce deve estar quase pronto...",
             },
    11010 : { GREETING : "",
              LEAVING : "",
              QUEST : "Acredito que _toNpcName_ tem mais um trabalho para voc\xc3\xaa._where_",
              },
    11011 : { GREETING : "",
              LEAVING : "",
              QUEST : "Que bom ver voc\xc3\xaa de novo, _avName_!\aVoc\xc3\xaa pode fazer uma medição em %s, por favor?" % GlobalStreetNames[1300][-1],
              INCOMPLETE_PROGRESS : "Tentou procurar em %s?" % GlobalStreetNames[1300][-1],
              COMPLETE : "\xc3\x93timo trabalho!\aAqui está a sua merecida recompensa!",
             },
    11012 : { GREETING : "",
              LEAVING : "",
              QUEST : "Voc\xc3\xaa sabe o que fazer._where_",
              },
    11013 : { GREETING : "",
              LEAVING : "",
              QUEST : "_avName_, meu caro!\aVoc\xc3\xaa pode ir até %s e encontrar mais um termômetro para mim?" % GlobalStreetNames[5100][-1],
              INCOMPLETE_PROGRESS : "Tem certeza de que está procurando em %s?" % GlobalStreetNames[5100][-1],
              COMPLETE : "Excelente!\aCom a sua ajuda, a minha pesquisa está caminhando!\aAqui está a sua recompensa.",
             },
    11014 : { GREETING : "",
              LEAVING : "",
              QUEST : "_toNpcName_ estava pedindo por voc\xc3\xaa.\aParece que voc\xc3\xaa causou uma boa impressão!_where_",
              },
    11015 : { GREETING : "",
              LEAVING : "",
              QUEST : "Bem-vindo de volta!\aEstive esperando.\aA próxima medição tem que ser em %s." % GlobalStreetNames[5200][-1],
              INCOMPLETE_PROGRESS : "Voc\xc3\xaa está procurando em %s, certo?" % GlobalStreetNames[5200][-1],
              COMPLETE : "Obrigado!\aAqui está sua recompensa.",
             },
    11016 : { GREETING : "",
              LEAVING : "",
              QUEST : "Se precisa completar o seu disfarce de Robô da Lei...\a_toNpcName_ pode ajudar voc\xc3\xaa._where_",
              },
    11017 : { GREETING : "",
              LEAVING : "",
              QUEST : "Olá, Cientista de Pesquisas Iniciante!\aAinda precisamos de medições de %s." % GlobalStreetNames[5300][-1],
              INCOMPLETE_PROGRESS : "Tentou procurar em %s?" % GlobalStreetNames[5300][-1],
              COMPLETE : "\xc3\x93timo trabalho!\aAqui está o seu negócio de Robô da Lei...",
             },
    11018 : { GREETING : "",
              LEAVING : "",
              QUEST : "_toNpcName_ tem outro trabalho para voc\xc3\xaa.\aSe ainda não tiver se cansado dele..._where_",
              },
    11019 : { GREETING : "",
              LEAVING : "",
              QUEST : "Então.\aPronto para outra recuperação?\aDesta vez, tente %s." % GlobalStreetNames[4100][-1],
              INCOMPLETE_PROGRESS : "Tem certeza de que está procurando em %s?" % GlobalStreetNames[4100][-1],
              COMPLETE : "Mais um!\aNossa, voc\xc3\xaa é a efici\xc3\xaancia em pessoa!",
             },
    11020 : { GREETING : "",
              LEAVING : "",
              QUEST : "Ainda está atrás de peças de disfarce de Robô da Lei?_where_",
              },
    11021 : { GREETING : "",
              LEAVING : "",
              QUEST : "Voc\xc3\xaa já deve ter adivinhado...\amas eu preciso de medições de %s." % GlobalStreetNames[4200][-1],
              INCOMPLETE_PROGRESS : "Voc\xc3\xaa está procurando em %s, certo?" % GlobalStreetNames[4200][-1],
              COMPLETE : "Quase lá!\aAqui está...",
             },
    11022 : { GREETING : "",
              LEAVING : "",
              QUEST : "Odeio dizer isto, mas..._where_",
              },
    11023 : { GREETING : "",
              LEAVING : "",
              QUEST : "O que acha de %s? Poderia conseguir um termômetro de lá também?" % GlobalStreetNames[4300][-1],
              INCOMPLETE_PROGRESS : "Tentou procurar em %s?" % GlobalStreetNames[4300][-1],
              COMPLETE : "Outro ótimo trabalho, _avName_",
             },
    11024 : { GREETING : "",
              LEAVING : "",
              QUEST : "Vá visitar o Professor se ainda precisar de peças de disfarce._where_",
              },
    11025 : { GREETING : "",
              LEAVING : "",
              QUEST : "Acho que ainda precisamos de uma medição de %s." % GlobalStreetNames[9100][-1],
              INCOMPLETE_PROGRESS : "Tem certeza de que está procurando em %s?" % GlobalStreetNames[9100][-1],
              COMPLETE : "Bom trabalho!\aAcho que estamos chegando perto...",
             },
    11026 : { GREETING : "",
              LEAVING : "",
              QUEST : "_toNpcName_ tem uma última missão para voc\xc3\xaa._where_",
              },
    11027 : { GREETING : "",
              LEAVING : "",
              QUEST : "Já de volta?\aA medição final é em %s." % GlobalStreetNames[9200][-1],
              INCOMPLETE_PROGRESS : "Voc\xc3\xaa está procurando em %s, certo?" % GlobalStreetNames[9200][-1],
              COMPLETE : "Está pronto!\aAgora, voc\xc3\xaa já pode se infiltrar no Escritório do Promotor Público e coletar Avisos de Júri.\aBoa sorte e obrigado pela sua ajuda!",
             },
    12000 : { GREETING : "",
              LEAVING : "",
              QUEST : "Se quiser peças de disfarce de Robô Chefe, deve visitar _toNpcName_._where_",
              },
    12001 : { GREETING : "",
              LEAVING : "",
              QUEST : "Sim, posso pegar as suas peças de Robô-Chefe.\aMas vou precisar de sua ajuda para completar a minha coleção de Robô-Chefe.\aVá lá fora e derrote um Puxa-saco.",
              INCOMPLETE_PROGRESS : "Não consegue encontrar um Puxa-saco? Que vergonha...",
              COMPLETE : "Voc\xc3\xaa não fracassou, não é?\ aAqui está a sua primeira peça de disfarce. ",
             },
    12002 : { GREETING : "",
              LEAVING : "",
              QUEST : "_toNpcName_ precisa de mais ajuda se voc\xc3\xaa puder._where_ ",
              },
    12003 : { GREETING : "",
              LEAVING : "",
              QUEST : "Outra peça de disfarce?\aCertamente...\aMas só se voc\xc3\xaa derrotar um Rato de Escritório. ",
              INCOMPLETE_PROGRESS : "Os Rato de Escritório podem ser encontrados nas ruas.",
              COMPLETE : "Ele realmente foi um fracote! \ aAqui está sua segunda peça de disfarce.",
             },
    12004 : { GREETING : "",
              LEAVING : "",
              QUEST : "Só há mesmo um lugar onde encontrar peças de Robô-Chefe._where_",
              },
    12005 : { GREETING : "",
              LEAVING : "",
              QUEST : "Agora, preciso de um “Vaquinha de Presépio”...",
              INCOMPLETE_PROGRESS : "O “Vaquinha de Presépio” pode ser encontrado nas ruas.",
              COMPLETE : "Isso! Cara, voc\xc3\xaa é demais.\aAqui está sua terceira peça de disfarce.",
             },
    12006 : { GREETING : "",
              LEAVING : "",
              QUEST : "_toNpcName_ tem mais peças para voc\xc3\xaa... ",
              },
    12007 : { GREETING : "",
              LEAVING : "",
              QUEST : "Se voc\xc3\xaa derrotar um Micro\4empresário, darei a voc\xc3\xaa mais uma peça.",
              INCOMPLETE_PROGRESS : "Tente procurar em %s" % GlobalStreetNames[1100][-1],
              COMPLETE : "Voc\xc3\xaa se saiu muito bem!\aAqui está sua quarta peça de disfarce.",
             },
    12008 : { GREETING : "",
              LEAVING : "",
              QUEST : "Direto para..._where_",
              },
    12009 : { GREETING : "",
              LEAVING : "",
              QUEST : "Agora estou atrás de um Facão...",
              INCOMPLETE_PROGRESS : "Algum problema? Tente procurar em %s" % GlobalStreetNames[3100][-1],
              COMPLETE : "Não foi tão dif\xc3\xadcil!\aAqui está sua quinta peça de disfarce. ",
             },
    12010 : { GREETING : "",
              LEAVING : "",
              QUEST : "Acho que voc\xc3\xaa sabe aonde ir agora..._where_",
              },
    12011 : { GREETING : "",
              LEAVING : "",
              QUEST : "Um Caça-\4talentos é o próximo da minha lista.",
              INCOMPLETE_PROGRESS : "Voc\xc3\xaa terá mais sorte procurando em edif\xc3\xadcios.",
              COMPLETE : "Vejo que não teve problemas para caçar um desses.\aAqui está sua sexta peça de disfarce. ",
             },
    12012 : { GREETING : "",
              LEAVING : "",
              QUEST : "_toNpcName_ precisa de mais Robôs-Chefe. ",
              },
    12013 : { GREETING : "",
              LEAVING : "",
              QUEST : "A seguir, preciso que voc\xc3\xaa localize um Aventureiro Corporativo.",
              INCOMPLETE_PROGRESS : "Voc\xc3\xaa terá mais sorte procurando em edif\xc3\xadcios.",
              COMPLETE : "Voc\xc3\xaa leva mesmo jeito para isso!\aAqui está sua sétima peça de disfarce.",
             },
    12014 : { GREETING : "",
              LEAVING : "",
              QUEST : "Se quiser mais peças de disfarce, vá para..._where_",
              },
    12015 : { GREETING : "",
              LEAVING : "",
              QUEST : "Agora, o mais precioso de todos: O um Rei da Cocada Preta!",
              INCOMPLETE_PROGRESS : "Tente procurar em %s" % GlobalStreetNames[10000][-1],
              COMPLETE : "Sabia que podia contar com voc\xc3\xaa para cortar...\aAh, não importa.\aAqui está sua próxima peça de disfarce. ",
             },
    12016 : { GREETING : "",
              LEAVING : "",
              QUEST : "_toNpcName_ estava \xc3\xa0 sua procura...",
              },
    12017 : { GREETING : "",
              LEAVING : "",
              QUEST : "Agora, preciso que voc\xc3\xaa derrote um dos novos e mais traiçoeiros Cogs de Robô-Chefe.",
              INCOMPLETE_PROGRESS : "Tente procurar em %s" % GlobalStreetNames[10000][-1],
              COMPLETE : "Eles são mais fortes do que parecem, hein?\aAcho que lhe devo uma peça de disfarce. ",
             },
    12018 : { GREETING : "",
              LEAVING : "",
              QUEST : "Pode dar um giro até..._where_",
              },
    12019 : { GREETING : "",
              LEAVING : "",
              QUEST : "Esses Cogs versão 2.0 são muito interessantes.\aPor favor, derrote mais um.",
              INCOMPLETE_PROGRESS : "Tente procurar em %s" % GlobalStreetNames[10000][-1],
              COMPLETE : "Valeu!\aMais uma peça de disfarce chegando. ",
             },
    12020 : { GREETING : "",
              LEAVING : "",
              QUEST : "Se tiver a oportunidade, d\xc3\xaa uma parada e visite _toNpcName_.",
              },
    12021 : { GREETING : "",
              LEAVING : "",
              QUEST : "Imagino se puderem se regenerar...",
              INCOMPLETE_PROGRESS : "Tente procurar em %s" % GlobalStreetNames[10000][-1],
              COMPLETE : "Acho que não.\aAqui está sua peça... ",
             },
    12022 : { GREETING : "",
              LEAVING : "",
              QUEST : "Voc\xc3\xaa sabe..._where",
              },
    12023 : { GREETING : "",
              LEAVING : "",
              QUEST : "Talvez não sejam Robôs-Chefe afinal...",
              INCOMPLETE_PROGRESS : "Tente procurar em %s" % GlobalStreetNames[10000][-1],
              COMPLETE : "Hummm, acho que realmente são Robôs-Chefe.\aConsiga mais uma peça. ",
             },
    12024 : { GREETING : "",
              LEAVING : "",
              QUEST : "Voc\xc3\xaa provavelmente já sabe o que vou dizer...",
              },
    12025 : { GREETING : "",
              LEAVING : "",
              QUEST : "Talvez, de alguma maneira, estejam relacionados aos Esqueletocogs... ",
              INCOMPLETE_PROGRESS : "Tente procurar em %s" % GlobalStreetNames[10000][-1],
              COMPLETE : "Isso foi inconsequente...\aAqui está sua peça de disfarce. ",
             },
    12026 : { GREETING : "",
              LEAVING : "",
              QUEST : "Por favor, visite _toNpcName_ novamente.",
              },
    12027 : { GREETING : "",
              LEAVING : "",
              QUEST : "Ainda tenho dúvidas de que não sejam algum tipo de Esqueletocogs...",
              INCOMPLETE_PROGRESS : "Tente procurar em %s" % GlobalStreetNames[10000][-1],
              COMPLETE : "Bem, talvez não.\aAqui está sua próxima peça. ",
             },
    12028 : { GREETING : "",
              LEAVING : "",
              QUEST : "Talvez seja o último lugar a que gostaria de ir. Mas...",
              },
    12029 : { GREETING : "",
              LEAVING : "",
              QUEST : "Esses novos Cogs ainda me deixam dúvidas.\aPoderia derrotar mais um, por favor?",
              INCOMPLETE_PROGRESS : "Tente procurar em %s" % GlobalStreetNames[10000][-1],
              COMPLETE : "Fascinante. Simplesmente fascinante.\aUma peça de disfarce pelos inconvenientes. ",
             },
    12030 : { GREETING : "",
              LEAVING : "",
              QUEST : "_toNpcName_ está começando a parecer um disco riscado...",
              },
    12031 : { GREETING : "",
              LEAVING : "",
              QUEST : "Já havia quase descoberto o que são esses novos Cogs.\aSó mais um... ",
              INCOMPLETE_PROGRESS : "Tente procurar em %s" % GlobalStreetNames[10000][-1],
              COMPLETE : "Sim, acho que encontrei algo importante.\aAh, sim.\aIsso é para voc\xc3\xaa... ",
             },
    12032 : { GREETING : "",
              LEAVING : "",
              QUEST : "Voc\xc3\xaa precisa contar ao Flippy sobre isso...",
              INCOMPLETE_PROGRESS : "Flippy está no Toon Hall",
              COMPLETE : "Um novo tipo de Cog!\aBom trabalho!\aAqui está sua última peça de disfarce.",
              },
 }

# ChatGarbler.py
ChatGarblerDog = ["au", "arf", "grrrr"]
ChatGarblerCat = ["miau", "miu"]
ChatGarblerMouse = ["quick", "quiiii", "quiiiiquiiii"]
ChatGarblerHorse = ["r\xc3\xad\xc3\xad\xc3\xadrrrr", "brrr"]
ChatGarblerRabbit = ["ick", "iipr", "iipi", "iicki"]
ChatGarblerDuck = ["quá", "quack", "quáááck"]
ChatGarblerMonkey = ["ooh", "ooo", "ahh"]
ChatGarblerBear = ["grrrau", "grrr"]
ChatGarblerPig = ["oinc", "oic", "rrroinc"]
ChatGarblerDefault = ["blá"]

# AvatarDNA.py
Bossbot = "Robô-chefe"
Lawbot = "Robô da Lei"
Cashbot = "Robô Mercenário"
Sellbot = "Robô Vendedor"
BossbotS = "um Robô-chefe"
LawbotS = "um Robô da Lei"
CashbotS = "um Robô Mercenário"
SellbotS = "um Robô Vendedor"
BossbotP = "Robôs-chefe"
LawbotP = "Robôs da Lei"
CashbotP = "Robôs Mercenários"
SellbotP = "Robôs Vendedores"
BossbotSkelS = "um Esqueletocog %s" % (Bossbot)
LawbotSkelS = "um Esqueletocog %s" % (Lawbot)
CashbotSkelS = "um Esqueletocog %s" % (Cashbot)
SellbotSkelS = "um Esqueletocog %s" % (Sellbot)
BossbotSkelP = "Esqueletocogs %s" % (BossbotP)
LawbotSkelP = "Esqueletocogs %s" % (LawbotP)
CashbotSkelP = "Esqueletocogs %s" % (CashbotP)
SellbotSkelP = "Esqueletocogs %s" % (SellbotP)
SkeleRevivePostFix = " v2.0"

# AvatarDetailPanel.py
AvatarDetailPanelOK = lOK
AvatarDetailPanelCancel = lCancel
AvatarDetailPanelClose = lClose
AvatarDetailPanelLookup = "Procurando detalhes de %s."
AvatarDetailPanelFailedLookup = "Não foi poss\xc3\xadvel obter detalhes de %s."
#AvatarDetailPanelPlayer = "Jogador: %(player)s\nMundo: %(world)s\nLocal: %(location)s"
# sublocation is not working now
AvatarDetailPanelPlayer = "Jogador: %(player)s\nMundo: %(world)s"
AvatarDetailPanelPlayerShort = "%(player)s\nMundo: %(world)s\nLocal: %(location)s"
AvatarDetailPanelRealLife = "Off-line"
AvatarDetailPanelOnline = "Região: %(district)s\nLocal: %(location)s"
AvatarDetailPanelOnlinePlayer = "Região: %(district)s\nLocal: %(location)s\nJogador: %(player)s"
AvatarDetailPanelOffline = "Região: off-line\nLocal: off-line"
AvatarShowPlayer = "Exibir Jogador"
OfflineLocation = "Off-line"

#PlayerDetailPanel
PlayerToonName = "Toon: %(toonname)s"
PlayerShowToon = "Mostrar Toon"
PlayerPanelDetail = "Detalhes do jogador"

# AvatarPanel.py
AvatarPanelFriends = "Amigos"
AvatarPanelWhisper = "Cochichar"
AvatarPanelSecrets = "Segredos"
AvatarPanelGoTo = "Ir para"
AvatarPanelPet = "Mostrar Rabisco"
AvatarPanelIgnore = "Ignorar"
AvatarPanelIgnoreCant = "OK"
AvatarPanelStopIgnoring = "Parar de Ignorar"
AvatarPanelReport = "Relatar"
#AvatarPanelCogDetail = "Dept: %s\nN\xc3\xadvel: %s\n"
AvatarPanelCogLevel = "N\xc3\xadvel: %s"
AvatarPanelCogDetailClose = lClose
AvatarPanelDetail = "Detalhes do Toon"
AvatarPanelGroupInvite = "Convidar para Grupo"
AvatarPanelGroupRetract = "Retirar Convite"
AvatarPanelGroupMember = "Já no Grupo"
AvatarPanelGroupMemberKick = "Remova"

# grouping messages
groupInviteMessage = "%s quer que voc\xc3\xaa entre em seu grupo"


# Report Panel
ReportPanelTitle = "Denunciar um Jogador"
ReportPanelBody = "Este recurso enviará uma denúncia completa a um Moderador. Em vez de denunciar, voc\xc3\xaa pode optar pelo seguinte:\n\n  - Teleportar-se para outra região\n  - Usar \"Ignorar\" no painel do Toon\n\nQuer mesmo denunciar %s para um Moderador?"
ReportPanelBodyFriends = "Este recurso enviará uma denúncia completa a um Moderador. Em vez de denunciar, voc\xc3\xaa pode optar pelo seguinte:\n\n  - Teleportar-se para outra região\n  - Romper sua amizade\n\nQuer mesmo denunciar %s para um Moderador?\n\n(Isso também vai romper sua amizade)"
ReportPanelCategoryBody = "Voc\xc3\xaa está prestes a denunciar %s. Um Moderador será alertado sobre sua reclamação e tomará medidas apropriadas contra quem estiver quebrando as regras. Escolha o motivo pelo qual está denunciando %s:"
ReportPanelBodyPlayer = "Este recurso ainda está sendo desenvolvido e será disponibilizado em breve. Enquanto isso, voc\xc3\xaa pode fazer o seguinte:\n\n  - Vá até o DXD e termine a amizade por lá.\n – Conte aos pais ou responsáveis o que está acontecendo."

ReportPanelCategoryLanguage = "Linguagem Rude"
ReportPanelCategoryPii = "Compartilhar/Solicitar Informações Pessoais"
ReportPanelCategoryRude = "Comportamento Rude ou Mau"
ReportPanelCategoryName = "Nome Ruim"
ReportPanelCategoryHacking = "Hacking"

ReportPanelConfirmations = (
    "Voc\xc3\xaa está prestes a denunciar que %s usou linguagem obscena, intolerante, preconceituosa ou sexualmente expl\xc3\xadcita.",
    "Voc\xc3\xaa está prestes a denunciar %s está promovendo insegurança ao divulgar ou solicitar um número de telefone, sobrenome, endereço de e-mail, senha ou nome de conta.",
    "Voc\xc3\xaa está prestes a relatar que %s está importunando, atormentando ou usando de comportamento radical para atrapalhar o jogo.",
    "Voc\xc3\xaa está prestes a relatar que %s criou um nome que não segue as regras da Disney.",
    "You are about to report that %s is hacking the game.",
    )

# Put on confirmation screen!
ReportPanelWarning = "Levamos as denúncias muito a sério. Sua denúncia será vista por um Moderador, que tomará medidas contra qualquer um que quebrar nossas regras. Se for descoberto que sua conta também quebrou as regras, ou se voc\xc3\xaa fizer denúncias falsas ou abusar do sistema 'Denunciar um Jogador', um Moderador pode tomar medidas contra sua conta. Tem certeza absoluta de que quer denunciar este jogador?"

ReportPanelThanks = "Obrigado! Sua denúncia foi enviada a um Moderador para análise. Não há necessidade de nos contatarmos novamente sobre o problema. A equipe de moderação tomará medidas adequadas contra um jogador que for descoberto quebrando as regras."

ReportPanelRemovedFriend = "Removemos automaticamente %s da sua Lista de Amigos."
ReportPanelRemovedPlayerFriend = "Removemos automaticamente %s como amigo Jogador, e voc\xc3\xaa não o verá mais como seu amigo em nenhum produto Disney."

ReportPanelAlreadyReported = "Voc\xc3\xaa já denunciou %s nesta sessão. Um Moderador vai analisar sua denúncia anterior."

# Report Panel
IgnorePanelTitle = "Ignorar um Jogador"
IgnorePanelAddIgnore = "Quer ignorar %s pelo restante da sessão?"
IgnorePanelIgnore = "Voc\xc3\xaa agora está ignorando %s."
IgnorePanelRemoveIgnore = "Deseja parar de ignorar %s?"
IgnorePanelEndIgnore = "Voc\xc3\xaa não está mais ignorando %s."
IgnorePanelAddFriendAvatar = "%s está entre seus amigos, voc\xc3\xaa não pode ignorá-lo(la)enquanto forem amigos(as)."
IgnorePanelAddFriendPlayer = "%s (%s)está entre seus amigos, voc\xc3\xaa não pode ignorá-lo(la) enquanto forem amigos(as)."

# PetAvatarPanel.py
PetPanelFeed = "Alimentar"
PetPanelCall = "Chamar"
PetPanelGoTo = "Ir para"
PetPanelOwner = "Mostrar dono"
PetPanelDetail = "Detalhes do bichinho"
PetPanelScratch = "Coçar"

# PetDetailPanel.py
PetDetailPanelTitle = "Adestramento"
# NOTE: these are replicated from OTPLocalizerEnglish sans "!"
PetTrickStrings = {
    0: 'Pular',
    1: 'Dar a pata',
    2: 'Fingir de morto',
    3: 'Rolar',
    4: 'Dar cambalhota',
    5: 'Dançar',
    6: 'Falar',
    }

# PetMood.py
PetMoodAdjectives = {
    'neutral': 'neutro',
    'hunger': 'faminto',
    'boredom': 'chateado',
    'excitement': 'animado',
    'sadness': 'triste',
    'restlessness': 'inquieto',
    'playfulness': 'brincalhão',
    'loneliness': 'solitário',
    'fatigue': 'cansado',
    'confusion': 'confuso',
    'anger': 'zangado',
    'surprise': 'surpreso',
    'affection': 'carinhoso',
    }

SpokenMoods = {
    'neutral': 'neutro',
    'hunger': 'Eu\estou cansado de Balinhas! Que tal me dar uma fatia de torta?',
    'boredom': 'Voc\xc3\xaa não\ achou que eu entenderia, hein?',
    'excitement': 'Toontástico!',
    'sadness': 'Eu quero ser rabisco de qualidade',
    'restlessness': 'Eu\estou tãooo inquieto',
    'playfulness': 'Brinque comigo ou eu\vou desenterrar algumas flores!',
    'loneliness': 'Quero lutar com os Cogs com voc\xc3\xaa!',
    'fatigue': '\xc3\x89 muito cansativo fazer truques de rabisco! Que\tal dar um tempinho?',
    'confusion': 'Onde estou? Quem é mesmo voc\xc3\xaa?',
    'anger': 'Voc\xc3\xaa sempre me deixa para trás',
    'surprise': 'Opa, de onde voc\xc3\xaa surgiu?',
    'affection': 'Voc\xc3\xaa é um ótimo toon',
    }

SpokenMoods = {
    'neutral': 'neutral',
    'hunger': ["Estou cansado de balinhas em forma de feijão! Que tal me dar um pedaço de torta?",
               "Que tal uma Balinha Vermelha? Estou enjoado das Verdes!",
               "Ah, aquelas balinhas em forma de feijão eram para plantar? Mas eu estou com fome!",
               ],
    'boredom': ["Estou morrendo de tédio aqui!",
                "Voc\xc3\xaa não achou que eu entendi voc\xc3\xaa, né?",
                "Nós já podemos FAZER alguma coisa?",
                ],
    'excitement': ["OMD, é voc\xc3\xaa, é voc\xc3\xaa, é voc\xc3\xaa!",
                   "hmmm, balinhas, hmmm!",
                   "Tem como isso ficar ainda melhor?",
                   "Feliz Semana Abril Toons!",
                   ],
    'sadness': ["Não vai, Não vai, Não vai, Não vai, Não vai, Não vai, Não vai, Não vai, Não vai, Não vai, Não vai...",
                "Vou ficar bem. Eu juro!",
                "Eu não sei POR QUE estou triste. Apenas estou!!!",
                ],
    'restlessness': ["Estou tããããão impaciente!!!",],
    'playfulness': ["Vamos brincar, Vamos brincar, Vamos brincar, Vamos brincar, Vamos brincar, Vamos brincar, Vamos brincar, Vamos brincar, Vamos brincar...",
                    "Brinque comigo ou eu arrancarei algumas flores!",
                    "Vamos dar uma volta por a\xc3\xad e a\xc3\xad e a\xc3\xad e a\xc3\xad e a\xc3\xad e a\xc3\xad...",
                    ],
    'loneliness': ["Onde voc\xc3\xaa esteve?",
                   "Quer um abraço?",
                   "Eu quero ir junto quando voc\xc3\xaa for lutar com os Cogs!",
                   ],
    'fatigue': ["Aquele mergulho no lago realmente me cansou!",
                "Ser um Doodle é cansativo!",
                "Eu preciso ir para a Terra do Sonho!",
                ],
    'confusion': ["Onde estou? De novo, quem é voc\xc3\xaa?",
                  "De novo, o que é Toonar?",
                  "Opa, eu estou entre voc\xc3\xaa e os Cogs! Fuja!",
                  ],
    'anger': ["... e voc\xc3\xaa ainda se pergunta por que eu nunca lhe dei um Toonar?!!!",
              "Voc\xc3\xaa sempre se esquece de mim!",
              "Voc\xc3\xaa ama suas piadas mais do que a mim!",
              ],
    'surprise': ["Claro, Doodles podem falar!",
                 "Toons podem falar?!!",
                 "Opa, de onde voc\xc3\xaa surgiu?",
                 ],
    'affection': ["Voc\xc3\xaa é o melhor Toon que já EXISTIU!!!!!!!!!!",
                  "Voc\xc3\xaa tem NO\xc3\x87\xc3\x83O do quanto é bacana?",
                  "Eu tenho MUITA sorte de estar com voc\xc3\xaa!!!",
                  ]
        }

# DistributedAvatar.py
DialogQuestion = '?'

# LocalAvatar.py
FriendsListLabel = "Amigos"

# TeleportPanel.py
TeleportPanelOK = lOK
TeleportPanelCancel = lCancel
TeleportPanelYes = lYes
TeleportPanelNo = lNo
TeleportPanelCheckAvailability = "Tentando ir para %s."
TeleportPanelNotAvailable = "%s está ocupado(a) agora; tente novamente mais tarde."
TeleportPanelIgnored = "%s está ignorando voc\xc3\xaa."
TeleportPanelNotOnline = "%s não está on-line neste momento."
TeleportPanelWentAway = "%s saiu."
TeleportPanelUnknownHood = "Voc\xc3\xaa não sabe ir para %s!"
TeleportPanelUnavailableHood = "%s não está dispon\xc3\xadvel agora; tente novamente mais tarde."
TeleportPanelDenySelf = "Voc\xc3\xaa não pode ir lá por conta própria!"
TeleportPanelOtherShard = "%(avName)s está na região %(shardName)s, e voc\xc3\xaa está na região %(myShardName)s. Deseja ir para %(shardName)s?"
TeleportPanelBusyShard = "%(avName)s está em uma Região lotada. Jogar em uma Região lotada pode afetar severamente o desempenho do jogo. Tem certeza de que quer mudar de região?"

# DistributedBattleBldg.py
BattleBldgBossTaunt = "Sou o chefe."

# DistributedBattleFactory.py
FactoryBossTaunt = "Sou o Supervisor."
FactoryBossBattleTaunt = "Deixe-me te apresentar ao Supervisor."
MintBossTaunt = "Sou o Supervisor."
MintBossBattleTaunt = "Voc\xc3\xaa precisa falar com o Supervisor."
StageBossTaunt = "A minha Justiça não é Cega"
StageBossBattleTaunt = "Eu estou acima da Lei"
CountryClubBossTaunt = "Sou o Presidente do Clube."
CountryClubBossBattleTaunt = "Voc\xc3\xaa precisa falar com o Presidente do Clube."
ForcedLeaveCountryClubAckMsg = "O Presidente do Clube foi derrotado antes que voc\xc3\xaa pudesse chegar a ele. Voc\xc3\xaa não recuperou nenhuma Ação."

# HealJokes.py
ToonHealJokes = [
    ["O que faz TIQUE-TIQUE-TIQUE-AU?",
     "Um cãonômetro!"],
    ["Por que o louco toma banho com o chuveiro desligado?",
     "Porque ele comprou xampú para cabelos secos!"],
    ["Por que é dif\xc3\xadcil para o fantasma contar mentiras?",
     "Porque seus pensamentos são transparentes."],
    ["Do que a bailarina é chamada quando machuca o pé e se recusa a dançar?",
     "Pé-nóstica!"],
    ["O que a vaca foi fazer no espaço?",
     "Foi se encontrar com o vácuo!"],
    ["Por que o gato mia para a Lua e a Lua não mia para o gato?",
     "Porque astro-no-mia!"],
    ["Por que as tartarugas não ficam b\xc3\xaabadas?",
     "Porque elas só t\xc3\xaam um casco!"],
    ["Por que o elefante usa t\xc3\xaanis vermelhos?",
     "Porque os branquinhos sujam muito."],
    ["Por que a galinha atravessa a rua?",
     "Para chegar ao outro lado!"],
    ["Qual é a maior injustiça do Natal?",
     "O peru morre e a missa é do galo."],
    ["Qual é o cúmulo dos trabalhos manuais?",
     "Tricotar com a linha do trem."],
    ["O que é um vulcão?",
     "Uma montanha com soluço."],
    ["O que é um pontinho vermelho, um azul e um rosa em cima de uma árvore?",
     "Um morangotango com urublue num pinkenick."],
    ["Por que o elefante não consegue tirar carteira de motorista?",
     "Porque ele só dá trombada."],
    ["O que um tijolo disse para o outro?",
     "Existe um 'ciumento' entre nós."],
    ["O que a porta disse para a chave?",
     "Vamos dar uma voltinha."],
    ["O que o elétron fala quando atende ao telefone?",
     "Próton!"],
    ["Quem é o rei da horta?",
     "Rei Polho."],
    ["Por que as pilhas são melhores que os pol\xc3\xadticos?",
     "Porque elas t\xc3\xaam, pelo menos, um lado positivo."],
    ["O que Benjamin Franklin disse quando inventou a eletricidade?",
     "Nada. Ele estava em estado de choque."],
    ["Por que o cachorro balança o rabo?",
     "Porque o rabo não tem força para balançar o cachorro."],
    ["Qual é o cúmulo da força?",
     "Dobrar a esquina."],
    ["O que não é de comer, mas dá água na boca?",
     "O copo."],
    ["Quem é a mãe do mingau?",
     "Mãe Zena."],
    ["O que o Batman disse para o Robin na hora em que entraram no carro?",
     "BAT a porta!"],
    ["O que é um pontinho amarelo tomando sol?",
     "\xc3\x89 um fandango querendo virar baconzito."],
    ["O que é um pontinho rosa no armário?",
     "\xc3\x89 um cupink."],
    ["Quem é o tio da construção?",
     "Tio Jolo."],
    ["O que dá um cruzamento de um dálmata com um canário?",
     "Uma onça pintada da Amazônia."],
    ["O que é uma porção de letras voando?",
     "Um bando de borboletras."],
    ["O que é que viaja o mundo inteiro, mas fica o tempo todo em um canto só?",
     "O selo."],
    ["O que é um pontinho verde em cima de um amarelo no canto da parede?",
     "Uma ervilha de castigo ajoelhada no milho."],
    ["Por que o namoro da goiabada com o queijo não deu certo?",
     "Porque o queijo era fresco."],
    ["O que é um pontinho azul no guarda-roupas?",
     "\xc3\x89 uma bluesa."],
    ["O que é um pontinho verde no fundo da piscina?",
     "\xc3\x89 uma ervilha... Segurando a respiração!"],
    ["O que é um pontinho vermelho e azul voando de um lado para o outro?",
     "Uma mosca fantasiada de Super-homem."],
    ["Qual é o animal que tem mais de tr\xc3\xaas olhos e menos de quatro?",
     "O pi-olho, ou seja, 3,14."],
    ["O que a aranha faz quando vai para a aula de dança?",
     "Sapa-teia."],
    ["Por que o pato tem ciúmes do cavalo?",
     "Porque ele tem quatro patas."],
    ["Quando voc\xc3\xaa tem certeza de que um ovo não tem um pintinho dentro?",
     "Quando o ovo é de pata."],
    ["Por que ninguém apareceu no enterro do elefante?",
     "Porque ninguém queria carregar o caixão."],
    ["O que é que sempre aumenta, mas nunca diminui?",
     "A idade."],
    ["O que é que tem muitos pés, mas não fica de pé?",
     "A centopéia."],
    ["Em que espécie de mato se senta o elefante quando chove?",
     "Mato molhado."],
    ["Quem é que bate em voc\xc3\xaa, mas voc\xc3\xaa não revida?",
     "O vento."],
    ["O que é o cúmulo do contra-senso?",
     "Na casa de saúde, só haver doentes."],
    ["Quando um jogador de futebol é um literato?",
     "Quando ele faz um gol de letra."],
    ["Onde é que a sereia Ariel v\xc3\xaa filmes?",
     "No cinemaré."],
    ["O que é que atravessa a porta, mas nunca entra nem sai?",
     "A fechadura."],
    ["Por que os rios são considerados preguiçosos?",
     "Porque não saem dos seus leitos."],
    ["Qual é a diferença entre a galinha e o tecido?",
     "A galinha bota e o tecido desbota."],
    ["Era uma vez uma orquestra que não tocava nada. Qual o nome do filme?",
     "Os Intocáveis."],
    ["Quando é que um gaúcho é chamado de mineiro?",
     "Quando trabalha em uma mina."],
    ["O que dever\xc3\xadamos colocar embaixo da forca para que o condenado não morra?",
     "Cedilha!"],
    ["O que é que todos nós temos, mas quando precisamos vamos ao mercado comprar?",
     "Canela!"],
    ["O que voc\xc3\xaa faz quando está nadando em um oceano e um crocodilo ataca?",
     "Voc\xc3\xaa acorda."],
    ["Quem é que nasce no rio, vive no rio e morre no rio, mas só se molha se quiser?",
     "O carioca."],
    ["O que é que está no fim de tudo?",
     "A letra O."],
    ["Qual é o único monstro que é bonzinho?",
     "Good-zila."],
    ["O que é a única coisa que o vencedor da maratona perde?",
     "O fôlego."],
    ["O que acontece se voc\xc3\xaa alimentar uma vaca com flores?",
     "Ela dará leite de rosas."],
    ["O que é que tem seis olhos, mas não pode ver?",
     "Tr\xc3\xaas ratinhos cegos."],
    ["Afinal, o que é que sempre encontramos no final do túnel?",
     "A letra L."],
    ["Qual a palavra que tem duas letras e tr\xc3\xaas s\xc3\xadlabas?",
     "Arara!"],
    ["Por que os elefantes são encontrados na \xc3\x81frica?",
     "Porque eles são muito grandes para se esconderem."],
    ["Onde estavam todos os moradores da cidade durante o último apagão?",
     "No escuro."],
    ["Quando é que o cliente fica preso no banco?",
     "Quando fecha a conta-corrente."],
    ["Quem é que vai a todos os casamentos sem ser convidado?",
     "O padre."],
    ["Por que os dinossauros t\xc3\xaam pescoços longos?",
     "Porque eles t\xc3\xaam chulé."],
    ["Qual é a mulher que sempre aparece antes do nascer do sol?",
     "Aurora."],
    ["Por que os elefantes nunca esquecem?",
     "Porque ninguém nunca fala nada para eles."],
    ["Qual é o pa\xc3\xads que o criminoso não gosta de visitar?",
     "O Cana-dá."],
    ["Por que o leão é considerado o rei das selvas?",
     "Porque ele é macho; se fosse f\xc3\xaamea, seria rainha."],
    ["O que é um 'fuio'?",
     "\xc3\x89 um 'buiaco na paiede'."],
    ["Sou enrolado, tenho a cabeça rachada e vivo apertado?",
     "Parafuso."],
    ["Por que o cachorro rói o osso?",
     "Porque ele não consegue engolir o osso inteiro."],
    ["Como é que voc\xc3\xaa impede um elefante de passar pelo buraco de uma agulha?",
     "Dando um nó no rabo dele."],
    ["Em que lugar do mundo, o sono é mais profundo?",
     "No cemitério."],
    ["O que é que é menor que a boca de uma formiga?",
     "O que ela come."],
    ["Um é pouco, dois é bom, tr\xc3\xaas é demais. O que são quatro e cinco?",
     "Nove."],
    ["Qual é a corrente que, por mais forte que seja, não consegue segurar o navio?",
     "A corrente marinha."],
    ["O que é que tem boca e um só dente e chama a atenção de muita gente?",
     "O sino."],
    ["Qual deve ser o comprimento máximo de uma perna?",
     "O suficiente para alcançar o chão."],
    ["O que é uma molécula?",
     "\xc3\x89 uma 'Meninula Sapécula'."],
    ["Como se pode escrever a maior palavra do mundo?",
     "Com a caneta."],
    ["Que refeição é colocada sobre a água e não afunda?",
     "A bóia."],
    ["Qual o melhor castigo para um time de futebol que joga sujo?",
     "Levar um banho de gols."],
    ["Por que os elefantes usam t\xc3\xaanis de corrida?",
     "Para fazer cooper, é claro."],
    ["Por que os elefantes são grandes e cinza?",
     "Porque, se eles fossem pequenos e amarelos, seriam canários."],
    ["O que é que tem na árvore, no futebol, no chapéu e na casa?",
     "Copa."],
    ["O que é que deixa um cachorro desconfiado?",
     "Uma pulga atrás da orelha."],
    ["Por que o "+ Donald +" espalhou açúcar no travesseiro?",
     "Porque ele queria ter doces sonhos."],
    ["Por que o "+ Goofy +" levou o pente dele ao dentista?",
     "Porque ele perdeu todos os dentes."],
    ["Por que o "+ Goofy +" usa a camisa no banho?",
     "Porque a etiqueta diz para lavar e usar."],
    ["Qual o pa\xc3\xads está na granja e a capital está no pomar?",
     "Peru, capital Lima."],
    ["Qual é o prato preferido da maioria das pessoas?",
     "O prato cheio."],
    ["Como voc\xc3\xaa chama uma pessoa que leva outra para almoçar?",
     "Canibal."],
    ["O que é um ponto amarelo no canto da sala?",
     "\xc3\x89 milho Santiago."],
    ["O que é um ponto preto dentro do tubo de ensaio?",
     "Uma blacktéria."],
    ["Por que o "+ Pluto +" dorme com uma casca de banana?",
     "Para pular da cama cedo."],
    ["Por que o rato usa t\xc3\xaanis marrom?",
     "Porque o branco está lavando."],
    ["O que é que a dentadura tem em comum com as estrelas?",
     "Ela sai \xc3\xa0 noite."],
    ["O que é um pontinho preto no meio da estrada?",
     "\xc3\x89 um calhamblack."],
    ["Por que o arqueólogo foi \xc3\xa0 fal\xc3\xaancia?",
     "Porque sua carreira estava uma ru\xc3\xadna."],
    ["Como é que voc\xc3\xaa ficaria se atravessasse o Atlântico no Titanic?",
     "Ensopado."],
    ["O que é um pontinho amarelo no alto de um prédio?",
     "Um milho suicida."],
    ["Por que é que o milho suicida quer se suicidar?",
     "Porque o lugar onde ele mora é um bagaço."],
    ["O que é um pontinho vermelho lá embaixo do prédio onde está o milho suicida?",
     "Um milho bombeiro para salvar o milho suicida..."],
    ["Qual a cor mais barulhenta?",
     "A corneta."],
    ["O que é que a banana suicida falou?",
     "Macacos me mordam!!!"],
    ["Qual o tipo de alimento de que o pol\xc3\xadtico mais gosta?",
     "As massas."],
    ["O que a chaminé grande falou para a chaminé pequena?",
     "Voc\xc3\xaa é muito jovem para fumar."],
    ["O que é um pontinho vermelho no pântano?",
     "\xc3\x89 um jacared."],
    ["O que é um pontinho azul no gramado?",
     "Uma formiguinha de calça jeans."],
    ["O que é um ponto brilhante no gramado?",
     "Uma formiguinha de aparelho nos dentes."],
    ["O que é um pontinho marrom na pré-história?",
     "Um browntossauro."],
    ["Como se chama um dinossauro que nunca se atrasa?",
     "Prontossauro."],
    ["O que é um pontinho vermelho num pedacinho de neve?",
     "Uma miniatura da bandeira do Japão."],
    ["O que é um pontinho dourado no gramado?",
     "\xc3\x89 uma formiguinha brincando de Jaspion."],
    ["Qual e a comida que liga e desliga ?",
     "O StrogON-OFF."],
    ["Por que o livro de matemática ficou triste?",
     "Porque ele tinha muitos problemas."],
    ["O que o tomate foi fazer no banco?",
     "Foi tirar extrato"],
    ["Como se faz para transformar um giz numa cobra?",
     "\xc3\x89 só colocar o giz num copo de água. A\xc3\xad o 'gizbóia'"],
    ["Qual é o cúmulo da rapidez?",
     "Fechar a gaveta, trancar e jogar a chave dentro."],
    ["Qual é o cúmulo do ego\xc3\xadsmo?",
     "Não vou contar, só eu que sei."],
    ["Qual é o cúmulo da revolta?",
     "Morar sozinho, fugir de casa e deixar um bilhete dizendo que não volta mais."],
    ["Qual é o cúmulo do exagero?",
     "Passar manteiga no Pão de Açúcar."],
    ["Qual é o cúmulo do arrependimento do carrasco?",
     "Pois é, sempre que enforco alguém me dá um nó na garganta..."],
    ["Qual é o cúmulo da visão?",
     "Derrubar dez faixas-pretas com um golpe de vista."],
    ["Qual é o cúmulo da sorte?",
     "Ser atropelado por uma ambulância."],
    ["Qual é o cúmulo da maldade?",
     "Colocar tachinhas na cadeira elétrica."],
    ["Qual é o cúmulo da burrice?",
     "Ser reprovado no exame de fezes."],
    ["Qual é o cúmulo da economia?",
     "Usar o papel higi\xc3\xaanico dos dois lados."],
    ["Qual é o cúmulo do esquecimento?",
     "Ih! Esqueci!"],
    ["Qual é o cúmulo da sede?",
     "Tomar um ônibus."],
    ["O que que faz ABC...Slurp...DEF...Slurp?",
     "Alguém tomando sopa de letrinhas."],
    ["O que é que é verde e fica saltando sem parar em cima do sofá?",
     "Uma ervilha que saiu do castigo."],
    ["O que é que o tomate foi fazer no banco?",
     "Tirar extrato."],
    ["Por que o médico que trabalha \xc3\xa0 noite se veste de verde?",
     "Porque ele está de plantão."],
    ["O que é que é branco com pontinhos pretos e vermelhos?",
     "Um dálmata com catapora."],
    ["O que a galinha foi fazer na igreja?",
     "Assistir \xc3\xa0 missa do galo."],
    ["O que é o que é? Cai em pé e corre deitado?",
     "Não é a chuva não! \xc3\x89 uma minhoca de paraquedas."],
    ["Por que é que não é bom guardar o quibe no freezer?",
     "Porque lá dentro ele esfirra."],
    ["O que o advogado do frango foi fazer na delegacia?",
     "Foi soltar a franga"],
    ["Por que o galo canta de olhos fechados?",
     "Porque ele já sabe a música de cor."],
    ["Um peixe foi jogado de cima de um prédio de vinte andares. Que peixe era esse?",
     "Um atum, porque quando ele caiu fez: Aaaaaaaaaaaa Tum!"],
    ["Como se faz omelete de chocolate?",
     "Com ovos de Páscoa."],
    ["Para que servem óculos verdes?",
     "Para verde perto."],
    ["Para que servem óculos vermelhos?",
     "Para 'vermelhor'."],
    ["O que é verde por fora e amarela por dentro?",
     "Uma banana disfarçada de pepino."],
    ["Qual é a parte do carro que se originou no Antigo Egito?",
     "Os faraóis."],
    ["Como é que a bruxa sai na chuva?",
     "De rodo."],
    ["Por que o cachorro entrou na igreja?",
     "Porque ele é um cão pastor."],
    ["Quem é o pai do volante?",
     "O painel."],
    ["Como chamamos uma mulher que visitou uma plantação de uva?",
     "Viúva."],
    ["O que o amendoim falou para o elefante?",
     "Nada, o amendoim não fala."],
    ["O que os elefantes falam quando se esbarram?",
     "Mundo pequeno esse, né?"],
    ["O que o caixa falou para a registradora?",
     "Estou contando com voc\xc3\xaa."],
    ["Por que o caminhão de frigor\xc3\xadfico não sobe a ladeira?",
     "Porque 'elinguiça'."],
    ["Qual é a comida que liga e desliga?",
     "\xc3\x89 o strogON-OFF."],
    ["O que a vaca foi fazer na Argentina?",
     "Foi ver o Boi nos Ares."],
    ["Qual é o peixe mais salgado que existe?",
     "O sal-mão."],
    ["O que é um cão indeciso?",
     "\xc3\x89 um 'cão-fuso'."],
    ["Sabe por que o italiano não come churrasco?",
     "Porque o macarrão não cabe no espeto."],
    ["Qual é o cúmulo da rapidez?",
     "Ir ao enterro de um parente e ainda encontrá-lo vivo."],
    ["Qual é o cúmulo do azar?",
     "Ser atropelado por um carro funerário."],
    ["Por que o jacaré tomou o cartão de crédito do jacarezinho?",
     "Porque o jacarezinho gastou muito e mandou o jacarepaguá."],
    ["Qual é o cúmulo da burrice?",
     "Olhar pelo buraco da fechadura numa porta de vidro."],
    ["Qual é o cúmulo da confiança?",
     "Jogar par-ou-\xc3\xadmpar pelo telefone?"],
    ["Qual é o cúmulo da paci\xc3\xaancia?",
     "Esvaziar uma piscina com conta-gotas."],
    ["Qual é o cúmulo da traição?",
     "Suicidar-se com uma punhalada nas costas."],
    ["O que uma nuvem disse pra outra?",
     "'Nu-vem' não."],
    ["Qual é o cúmulo da moleza?",
     "Correr sozinho e chegar em segundo."],
    ["Por que o jacaré tirou o jacarezinho da escola?",
     "Porque ele 'reptil'."],
    ["Qual é o fim da picada?",
     "Quando o mosquito vai embora."],
    ["O que o paraquedas disse para o paraquedista?",
     "Tô contigo e não abro."],
    ["Qual é a cor mais barulhenta?",
     "A corneta."],
    ["O que é um pontinho amarelo no céu?",
     "Um yellowcóptero."],
    ]

# MovieHeal.py
MovieHealLaughterMisses = ("hmm","hehe","ah","Rá rá")
MovieHealLaughterHits1= ("Ah ah ah","Ri, ri, ri","Ré, ré","Ah, ah")
MovieHealLaughterHits2= ("AH HAH HAH!","HO HO HO!","R\xc3\x81 R\xc3\x81 R\xc3\x81!")

# MovieSOS.py
MovieSOSCallHelp = "%s SOCORRO!"
MovieSOSWhisperHelp = "%s precisa de ajuda na batalha!"
MovieSOSObserverHelp = "SOCORRO!"

# MovieNPCSOS.py
MovieNPCSOSGreeting = "Oi %s! \xc3\x89 uma satisfação ajudar voc\xc3\xaa!"
MovieNPCSOSGoodbye = "Vejo voc\xc3\xaa depois!"
MovieNPCSOSToonsHit = "Os Toons sempre acertam!"
MovieNPCSOSCogsMiss = "Os Cogs sempre erram!"
MovieNPCSOSRestockGags = "Reabastecendo com %s piadas!"
MovieNPCSOSHeal = "Curar"
MovieNPCSOSTrap = "Armadilha"
MovieNPCSOSLure = "Isca"
MovieNPCSOSSound = "Sonora"
MovieNPCSOSThrow = "Lançamento"
MovieNPCSOSSquirt = "Esguicho"
MovieNPCSOSDrop = "Cadente"
MovieNPCSOSAll = "Todos"

# MoviePetSOS.py
MoviePetSOSTrickFail = "Suspiro"
MoviePetSOSTrickSucceedBoy = "Bom garoto!"
MoviePetSOSTrickSucceedGirl = "Boa menina!"

# MovieSuitAttacks.py
MovieSuitCancelled = "CANCELADO\nCANCELADO\nCANCELADO"

# RewardPanel.py
RewardPanelToonTasks = "Tarefas Toon"
RewardPanelItems = "Itens recuperados"
RewardPanelMissedItems = "Itens não-recuperados"
RewardPanelQuestLabel = "Buscar %s"
RewardPanelCongratsStrings = ["\xc3\x89 isso a\xc3\xad!", "Parabéns!", "Uau!",
                              "Legal!", "Caraca!", "Toontástico!"]
RewardPanelNewGag = "Nova piada %(gagName)s para %(avName)s!"
RewardPanelUberGag = "%(avName)s ganhou a piada %(gagName)s com %(exp)s pontos de experi\xc3\xaancia!"
RewardPanelEndTrack = "Oba! %(avName)s chegou ao fim da Trilha de Piadas da piada %(gagName)s!"
RewardPanelMeritsMaxed = "Maximizados"
RewardPanelMeritBarLabels = [ "Bilhetes azuis", "Intimações", "Granas Cog", "Méritos" ]
RewardPanelMeritAlert = "Pronto para a promoção!"
RewardPanelSkip = "Skip"

RewardPanelCogPart = "Voc\xc3\xaa ganhou uma parte de disfarce de Cog!"
RewardPanelPromotion = "%s prepare-se para a promoção!"

# Cheesy effect descriptions: (short desc, sentence desc)
CheesyEffectDescriptions = [
    ("Toon normal", "voc\xc3\xaa ficará normal"),
    ("Cabeção", "voc\xc3\xaa ficará com uma cabeça grande"),
    ("Cabecinha", "voc\xc3\xaa ficará com uma cabeça pequena"),
    ("Pernonas", "voc\xc3\xaa ficará com pernas grandes"),
    ("Perninhas", "voc\xc3\xaa ficará com pernas pequenas"),
    ("Toonzão", "voc\xc3\xaa ficará um pouco maior"),
    ("Toonzinho", "voc\xc3\xaa ficará um pouco menor"),
    ("Quadro reto", "voc\xc3\xaa ficará em duas dimensões"),
    ("Perfil reto", "voc\xc3\xaa ficará em duas dimensões"),
    ("Transparente", "voc\xc3\xaa ficará transparente"),
    ("Sem cor", "voc\xc3\xaa ficará sem cor"),
    ("Toon invis\xc3\xadvel", "voc\xc3\xaa ficará invis\xc3\xadvel"),
    ]
CheesyEffectIndefinite = "Até que escolha outro efeito, %(effectName)s%(whileIn)s."
CheesyEffectMinutes = "Nos próximos %(time)s minutos, %(effectName)s%(whileIn)s."
CheesyEffectHours = "Nas próximas %(time)s horas, %(effectName)s%(whileIn)s."
CheesyEffectDays = "Nos próximos %(time)s dias, %(effectName)s%(whileIn)s."
CheesyEffectWhileYouAreIn = " enquanto estiver %s"
CheesyEffectExceptIn = ", exceto em %s"


# SuitBattleGlobals.py
SuitFlunky = "Puxa-saco"
SuitPencilPusher = "Rato de Escritório"
SuitYesman = "Vaquinha de Presépio"
SuitMicromanager = "Micro\4empresário"
SuitDownsizer = "Facão"
SuitHeadHunter = "Caça-\4talentos"
SuitCorporateRaider = "Aventureiro Corporativo"
SuitTheBigCheese = "O Rei da Cocada Preta"
SuitColdCaller = "Rei da Incerta"
SuitTelemarketer = "Operador de Tele\4marketing"
SuitNameDropper = "Dr. Sabe-com-\4quem-está-\4falando"
SuitGladHander = "Amigo da Onça"
SuitMoverShaker = "Agitador"
SuitTwoFace = "Duas Caras"
SuitTheMingler = "Amizade Fácil"
SuitMrHollywood = "Dr. Celebridade"
SuitShortChange = "Farsante"
SuitPennyPincher = "Mão de vaca"
SuitTightwad = "Pão-duro"
SuitBeanCounter = "Conta-\4moedinha"
SuitNumberCruncher = "Destruidor de Números"
SuitMoneyBags = "Sacos de Dinheiro"
SuitLoanShark = "Agiota"
SuitRobberBaron = "Barão Ladrão"
SuitBottomFeeder = "Comensal"
SuitBloodsucker = "Sanguessuga"
SuitDoubleTalker = "Duplo Sentido"
SuitAmbulanceChaser = "Perseguidor de Ambulâncias"
SuitBackStabber = "Golpe Sujo"
SuitSpinDoctor = "Relações Públicas"
SuitLegalEagle = "Macaco velho"
SuitBigWig = "Figurão"

# Singular versions (indefinite article)
SuitFlunkyS = "um Puxa-saco"
SuitPencilPusherS = "um Rato de Escritório"
SuitYesmanS = "uma Vaquinha de Presépio"
SuitMicromanagerS = "um Micro\4empresário"
SuitDownsizerS = "um Facão"
SuitHeadHunterS = "um Caça-talentos"
SuitCorporateRaiderS = "um Aventureiro Corporativo"
SuitTheBigCheeseS = "um Rei da Cocada Preta"
SuitColdCallerS = "um Rei da Incerta"
SuitTelemarketerS = "um Operador de Telemarketing"
SuitNameDropperS = "um Dr. Sabe-com-\4quem-está-\4falando"
SuitGladHanderS = "um Amigo da Onça"
SuitMoverShakerS = "um Agitador"
SuitTwoFaceS = "um Duas Caras"
SuitTheMinglerS = "um Amizade Fácil"
SuitMrHollywoodS = "um Dr. Celebridade"
SuitShortChangeS = "um Farsante"
SuitPennyPincherS = "um Mão de vaca"
SuitTightwadS = "um Pão-duro"
SuitBeanCounterS = "um Conta-\4moedinha"
SuitNumberCruncherS = "um Destruidor de Números"
SuitMoneyBagsS = "um Sacos de Dinheiro"
SuitLoanSharkS = "um Agiota"
SuitRobberBaronS = "um Barão Ladrão"
SuitBottomFeederS = "um Comensal"
SuitBloodsuckerS = "um Sanguessuga"
SuitDoubleTalkerS = "um Duplo Sentido"
SuitAmbulanceChaserS = "um Perseguidor de Ambulâncias"
SuitBackStabberS = "um Golpe Sujo"
SuitSpinDoctorS = "um Relações Públicas"
SuitLegalEagleS = "um Macaco velho"
SuitBigWigS = "um Figurão"

# Plural versions
SuitFlunkyP = "Puxa-sacos"
SuitPencilPusherP = "Ratos de Escritório"
SuitYesmanP = "Vaquinhas de Presépio"
SuitMicromanagerP = "Micro\4empresários"
SuitDownsizerP = "Facões"
SuitHeadHunterP = "Caça-\4talentos"
SuitCorporateRaiderP = "Aventureiros Corporativos"
SuitTheBigCheeseP = "Os Reis da Cocada Preta"
SuitColdCallerP = "Reis da Incerta"
SuitTelemarketerP = "Operadores de Tele\4marketing"
SuitNameDropperP = "Drs. Sabe-com-\4quem-está-\4falando"
SuitGladHanderP = "Amigos da Onça"
SuitMoverShakerP = "Agitadores"
SuitTwoFaceP = "Duas Caras"
SuitTheMinglerP = "Amizades Fáceis"
SuitMrHollywoodP = "Drs. Celebridade"
SuitShortChangeP = "Farsantes"
SuitPennyPincherP = "Mãos de vaca"
SuitTightwadP = "Pães-duros"
SuitBeanCounterP = "Conta-\4moedinhas"
SuitNumberCruncherP = "Destruidores de Números"
SuitMoneyBagsP = "Sacos de Dinheiro"
SuitLoanSharkP = "Agiotas"
SuitRobberBaronP = "Barões Ladrões"
SuitBottomFeederP = "Comensais"
SuitBloodsuckerP = "Sanguessugas"
SuitDoubleTalkerP = "Duplos Sentidos"
SuitAmbulanceChaserP = "Perseguidores de Ambulâncias"
SuitBackStabberP = "Golpes Sujos"
SuitSpinDoctorP = "Relações Públicas"
SuitLegalEagleP = "Macacos velhos"
SuitBigWigP = "Figurões"

SuitFaceOffDefaultTaunts = ['Buuuuu!']

SuitAttackDefaultTaunts = ['Pega essa!', 'Pode escrever!']

SuitAttackNames = {
  'Audit' : 'Auditoria!',
  'Bite' : 'Mordida!',
  'BounceCheck' : 'Cheque sem fundos!',
  'BrainStorm' : 'Grande ideia!',
  'BuzzWord' : 'Palavra-chave!',
  'Calculate' : 'Calcular!',
  'Canned' : 'Enlatado!',
  'Chomp' : 'Nhac!',
  'CigarSmoke' : 'Fumaça de charuto!',
  'ClipOnTie' : 'Prendedor de gravata!',
  'Crunch' : 'Triturar!',
  'Demotion' : 'Rebaixar!',
  'Downsize' : 'Reduzir!',
  'DoubleTalk' : 'Duplo sentido!',
  'EvictionNotice' : 'Aviso de despejo!',
  'EvilEye' : 'Mau-olhado!',
  'Filibuster' : 'Enchedor de linguiça!',
  'FillWithLead' : 'Pelotão de frente!',
  'FiveOClockShadow' : "Barba por fazer!",
  'FingerWag' : 'Dedo na cara!',
  'Fired' : 'Fogo!',
  'FloodTheMarket' : 'Invadir o mercado!',
  'FountainPen' : 'Caneta-tinteiro!',
  'FreezeAssets' : 'Bens congelados!',
  'Gavel' : 'Martelo!',
  'GlowerPower' : 'Olhar raivoso!',
  'GuiltTrip' : 'Sentimento de culpa!',
  'HalfWindsor' : 'Nó franc\xc3\xaas!',
  'HangUp' : 'Desligar!',
  'HeadShrink' : 'Analista!',
  'HotAir' : 'Ar quente!',
  'Jargon' : 'Jargão!',
  'Legalese' : 'Legal\xc3\xaas!',
  'Liquidate' : 'Liquidar!',
  'MarketCrash' : 'Queda da Bolsa!',
  'MumboJumbo' : 'Bobeira!',
  'ParadigmShift' : 'Desvio de paradigma!',
  'PeckingOrder' : 'Hierarquia!',
  'PickPocket' : 'Pivete!',
  'PinkSlip' : 'Bilhete azul!',
  'PlayHardball' : 'Jogo duro!',
  'PoundKey' : 'Tecla de Jogo da velha!',
  'PowerTie' : 'Gravata!',
  'PowerTrip' : 'Viajou na autoridade!',
  'Quake' : 'Terremoto!',
  'RazzleDazzle' : 'Agito!',
  'RedTape' : 'Burrocracia!',
  'ReOrg' : 'ReOrg!',
  'RestrainingOrder' : 'Repressão!',
  'Rolodex' : 'Agenda telefônica!',
  'RubberStamp' : 'Carimbo!',
  'RubOut' : 'Apagar!',
  'Sacked' : 'Ensacado!',
  'SandTrap' : 'Trincheira!',
  'Schmooze' : 'Bajula!',
  'Shake' : 'Tremor!',
  'Shred' : 'Retalho!',
  'SongAndDance' : 'Conta prosa!',
  'Spin' : 'Giro!',
  'Synergy' : 'Sinergia!',
  'Tabulate' : 'Tabular!',
  'TeeOff' : 'Tacada!',
  'ThrowBook' : 'Livro de lançamentos!',
  'Tremor' : 'Tremor!',
  'Watercooler' : 'Bebedouro!',
  'Withdrawal' : 'Retirada!',
  'WriteOff' : 'Baixa!',
  }

SuitAttackTaunts = {
    'Audit': ["Seus livros não t\xc3\xaam balanço.",
              "Parece que voc\xc3\xaa está no vermelho.",
              "Deixe-me ajudá-lo com esses livros.",
              "Sua coluna de débitos é muito alta.",
              "Vamos verificar os seus bens.",
              "Assim, voc\xc3\xaa vai ficar endividado.",
              "Vamos conferir direitinho o que voc\xc3\xaa deve.",
              "Assim, a sua conta vai ficar zerada.",
              "\xc3\x89 hora de voc\xc3\xaa se responsabilizar pelas suas despesas.",
              "Encontrei um erro nos seus livros.",
              ],
    'Bite': ["Quer uma mordida?",
             "Dá uma mordida!",
             "A sua mordida é maior do que voc\xc3\xaa pode mastigar.",
             "Minha mordida é maior do que o meu latido.",
             "Morde logo!",
             "Tome cuidado, eu mordo.",
             "Eu não mordo só quando estou encurralado.",
             "Só vou dar uma mordidinha.",
             "Não dei uma mordida o dia todo.",
             "Só quero uma mordida. \xc3\x89 pedir muito?",
             ],
    'BounceCheck': ["Ah, que pena, voc\xc3\xaa não tem graça.",
                    "Voc\xc3\xaa tem uma d\xc3\xadvida.",
                    "Acho que este cheque é seu.",
                    "Voc\xc3\xaa me devia isso.",
                    "Estou cobrando esta d\xc3\xadvida.",
                    "Este cheque não vai ser mole.",
                    "Voc\xc3\xaa será cobrado por isso.",
                    "Feche a conta.",
                    "Isso terá um custo para voc\xc3\xaa.",
                    "Queria trocar por dinheiro.",
                    "Vou mandar isso de volta para voc\xc3\xaa.",
                    "Esta conta está salgada.",
                    "Estou descontando o serviço.",
                    ],
    'BrainStorm':["Acho que vai chover.",
                  "Espero que voc\xc3\xaa esteja com o guarda-chuva.",
                  "Quero orientar voc\xc3\xaa.",
                  "Que tal uma saraivada básica?",
                  "Cad\xc3\xaa o seu brilho agora, Toon?",
                  "Pronto para a chuvarada?",
                  "Vou atacar voc\xc3\xaa como um furacão.",
                  "Chamo isso de ataque-relâmpago.",
                  "Adoro ser um desmancha-prazeres.",
                  ],
    'BuzzWord':["Desculpe-me se estou te aborrecendo.",
                "Ouviu a última?",
                "Veja se voc\xc3\xaa pega esta.",
                "Vamos cantarolar, Toon?",
                "Deixe-me defender voc\xc3\xaa.",
                "Vou \"C\" perfeitamente claro.",
                "Voc\xc3\xaa devia \"C\" mais cuidadoso.",
                "Veja se voc\xc3\xaa consegue desviar desse enxame.",
                "Cuidado, voc\xc3\xaa está prestes a ser picado.",
                "Parece que a sua urticária é séria.",
                ],
    'Calculate': ["Estes números fazem mesmo uma diferença!",
                  "Voc\xc3\xaa contou com isso?",
                  "Faça as contas, voc\xc3\xaa está caindo.",
                  "Deixe-me ajudar voc\xc3\xaa a somar isso.",
                  "Voc\xc3\xaa registrou todas as suas despesas?",
                  "De acordo com os meus cálculos, voc\xc3\xaa não ficará por muito tempo aqui.",
                  "Aqui está o total.",
                  "Uau, a sua conta está se multiplicando.",
                  "Tente brincar com esses números!",
                  Cogs + ": 1 Toons: 0",
                  ],
    'Canned': ["Gosta fora da lata?",
               "\"Lata\" limpo?",
               "Fresquinho, sa\xc3\xaddo da lata!",
               "Já foi atacado alguma vez por enlatados?",
               "Gostaria de doar a voc\xc3\xaa este enlatado!",
               "Prepare-se para o \"Vira-lata\"!",
               "Voc\xc3\xaa acha que pode abrir a lata, na lata.",
               "Vou te jogar na lata!",
               "Vou transformar voc\xc3\xaa em um a-Toon em lata!",
               "Seu gosto não é tão bom fora da lata.",
               ],
    'Chomp': ["Olha só esses comilões!",
              "Nhac, nhac, nhac!",
              "Aqui tem algo para mastigar.",
              "Procurando alguma coisa para mastigar?",
              "Por que voc\xc3\xaa não mastiga um pouco disto?",
              "Eu vou jantar voc\xc3\xaa.",
              "Adoro comer Toons no café da manhã!",
              ],
    'ClipOnTie': ["Melhor se arrumar para a reunião.",
                  "Voc\xc3\xaa não pode SAIR sem a gravata.",
                  "Os  "+ Cogs +" mais bem vestidos usam isto."
                  "Experimente este tamanho.",
                  "Voc\xc3\xaa devia se vestir para arrasar.",
                  "Sem gravata não tem serviço...",
                  "Precisa de ajuda para se vestir?",
                  "Nada é tão poderoso quanto uma boa gravata.",
                  "Vamos ver se serve.",
                  "Esta vai apertar voc\xc3\xaa.",
                  "Voc\xc3\xaa vai querer se vestir antes de SAIR.",
                  "Acho que vou dar uma gravata em voc\xc3\xaa.",
                  ],
    'Crunch': ["Parece que voc\xc3\xaa está espremido contra a parede.",
               "Hora de mexer a mand\xc3\xadbula!",
               "Vou dar alguma coisa para voc\xc3\xaa mascar!",
               "Triture isso!",
               "Mordida para viagem.",
               "Qual voc\xc3\xaa prefere, molinho ou crocante?",
               "Espero que esteja preparado para a hora da mand\xc3\xadbula.",
               "Parece que voc\xc3\xaa está ficando amassadinho!",
               "Vou amassar voc\xc3\xaa como uma latinha."
               ],
    'Demotion': ["Voc\xc3\xaa está descendo os degraus da empresa.",
                 "Vou mandar voc\xc3\xaa de volta para a Expedição.",
                 "Está na hora de virar a sua placa de identificação.",
                 "Voc\xc3\xaa está caidaço, palhaço.",
                 "Parece que voc\xc3\xaa está ferrado.",
                 "Voc\xc3\xaa não vai a lugar nenhum.",
                 "Voc\xc3\xaa está em um beco sem sa\xc3\xadda.",
                 "Voc\xc3\xaa não vai se mover tão cedo.",
                 "Voc\xc3\xaa não vai a lugar nenhum.",
                 "Vai ficar registrado em seu arquivo permanente.",
                 ],
    'Downsize': ["Desce!",
                 "Sabe como descer?",
                 "Vamos entrar direto no assunto.",
                 "O que houve? Voc\xc3\xaa parece deprimido.",
                 "Decaindo?",
                 "O que é que está caindo? Voc\xc3\xaa!",
                 "Por que não tem alguém do meu tamanho?",
                 "Por que eu não meço voc\xc3\xaa - ou será que é melhor dizer despeço?",
                 "Quer um tamanho menor por apenas mais uma moeda?",
                 "Experimente este tamanho!",
                 "Tem em um tamanho menor.",
                 "Este ataque é tamanho único!",
                 ],
    # Hmmm - where is double talker?
    'EvictionNotice': ["Mudança \xc3\xa0 vista.",
                       "Arrume as malas, Toon.",
                       "\xc3\x89 hora de arrumar outro lugar para morar.",
                       "Considere-se servido.",
                       "O seu aluguel está atrasado.",
                       "Isto vai te torpedear.",
                       "Voc\xc3\xaa está prestes a ser despejado.",
                       "Vou espirrar voc\xc3\xaa daqui.",
                       "Voc\xc3\xaa está deslocado.",
                       "Prepare-se para ser realocado.",
                       "Voc\xc3\xaa está abrigado.",
                       ],
    'EvilEye': ["Estou botando um mau-olhado em voc\xc3\xaa.",
                "Voc\xc3\xaa fica de olho vivo nisso para mim?",
                "Espere. Tem alguma coisa no meu olho.",
                "Estou de olho em voc\xc3\xaa!",
                "Voc\xc3\xaa pode botar o olho nisso aqui para mim?",
                "Tenho um olho gordo danado.",
                "Voc\xc3\xaa vai levar um soco no olho!",
                "Minha crueldade não está de molho, abre o olho!",
                "Vou colocar voc\xc3\xaa no olho do furacão!",
                "Estou dando com os olhos em voc\xc3\xaa.",
                ],
    'Filibuster':["Devo encher?",
                  "Isso vai demorar um pouco.",
                  "Poderia fazer isso o dia todo.",
                  "Não preciso nem respirar fundo.",
                  "Vou fazendo, fazendo, fazendo...",
                  "Nunca fica cansado de fazer isso.",
                  "Posso tagarelar sem parar.",
                  "Tem problema se eu puxar a sua orelha?",
                  "Acho que vou papear \xc3\xa0 vontade.",
                  "Sempre consigo dar o meu recado.",
                  ],
    'FingerWag': ["Já te disse milhares de vezes.",
                  "Olha aqui, Toon.",
                  "Não me faça rir.",
                  "Não me faça ir até a\xc3\xad.",
                  "Já cansei de repetir.",
                  "Fim de papo, eu já falei.",
                  "\Voc\xc3\xaa não tem respeito por nós, "+ Cogs +"."
                  "Acho que está na hora de voc\xc3\xaa prestar atenção.",
                  "Blá, Blá, Blá, Blá, Blá.",
                  "Não me obrigue a interromper a reunião.",
                  "Será que eu vou ter que separar voc\xc3\xaas?",
                  "Já passamos por isto antes.",
                  ],
    'Fired': ["\xc3\x89 fogo! O jeito é fazer um churrasquinho.",
              "Vai esquentar por aqui.",
              "Assim, o frio passa.",
              "Espero que voc\xc3\xaa tenha sangue frio.",
              "Quente, quentão e pelando.",
              "Melhor parar tudo, deitar no chão e rolar!",
              "Voc\xc3\xaa está fora daqui.",
              "O que voc\xc3\xaa acha de \"bem-feito\"?",
              "Pode dizer a\xc3\xad?",
              "Espero que tenha usado protetor solar.",
              "Está se sentindo um pouco tostado?",
              "Voc\xc3\xaa vai arder em chamas.",
              "Voc\xc3\xaa vai ficar aceso que nem fogueira.",
              "Voc\xc3\xaa está frito.",
              "Eu sou fogo na roupa.",
              "Só aticei o fogo um pouquinho, né?",
              "Olha, um churrasquinho crocante.",
              "Voc\xc3\xaa não devia sair por a\xc3\xad malpassado.",
              ],
    'FountainPen': ["Vai deixar mancha.",
                    "Vamos assinar embaixo.",
                    "Esteja preparado para alguns danos irreparáveis.",
                    "Voc\xc3\xaa vai precisar de um bom tintureiro.",
                    "Voc\xc3\xaa devia mudar.",
                    "Esta caneta-tinteiro tem uma tinta legal.",
                    "Aqui, vou usar a minha caneta.",
                    "Voc\xc3\xaa entende a minha letra?",
                    "Isso é que é carregar nas tintas.",
                    "Seu desempenho babou.",
                    "Não é chato quando isso acontece?",
                    ],
    'FreezeAssets': ["Seus bens são meus.",
                     "Está sentindo um vento? \xc3\x89 o cheque voador.",
                     "Espero que não tenha planos.",
                     "Isso vai manter voc\xc3\xaa na geladeira.",
                     "Tem uma brisa fria no ar.",
                     "O inverno está chegando mais cedo neste ano.",
                     "Voc\xc3\xaa está sentido um calafrio?",
                     "Vou cristalizar o meu plano.",
                     "Voc\xc3\xaa vai ver, no duro.",
                     "O gelo queima.",
                     "Espero que goste de frios.",
                     "Tenho muito sangue frio.",
                     ],
    'GlowerPower': ["Está olhando para mim?",
                    "Disseram que tenho olhos muito penetrantes.",
                    "Gosto de estar no fio da navalha.",
                    "Caçamba, caramba, meus quatro-olhos não são bambas?",
                    "Estou de olho em voc\xc3\xaa, pirralho.",
                    "Que tal estes olhos expressivos?",
                    "Meus olhos são o meu forte.",
                    "Enche os olhos.",
                    "Estou de olho, piolho.",
                    "Olhe nos meus olhos...",
                    "Podemos dar uma espiada no seu futuro?",
                    ],
    'GuiltTrip': ["Voc\xc3\xaa vai ficar com um baita sentimento de culpa!",
                  "Está se sentindo culpado?",
                  "\xc3\x89 tudo culpa sua!",
                  "Sempre ponho a culpa de tudo em voc\xc3\xaa.",
                  "Afogue-se na própria culpa!",
                  "Nunca mais falo contigo!",
                  "\xc3\x89 melhor pedir desculpas.",
                  "Só vou perdoar voc\xc3\xaa daqui a um milhão de anos!",
                  "Está preparado para viajar na maionese da culpa?",
                  "Ligue para mim quando voltar de viagem.",
                  "Quando voc\xc3\xaa volta de viagem?",
                  ],
    'HalfWindsor': ["Esta é a gravata mais elegante que voc\xc3\xaa já viu!",
                    "Procure não apertar tanto.",
                    "Voc\xc3\xaa não viu nem metade do nó em que voc\xc3\xaa se meteu.",
                    "Voc\xc3\xaa tem sorte de eu não saber franc\xc3\xaas.",
                    "Esta gravata é demais para voc\xc3\xaa.",
                    "Aposto como voc\xc3\xaa nunca VIU um nó franc\xc3\xaas!",
                    "Esta gravata não é para o seu bico.",
                    "Eu não deveria ter gasto esta gravata com voc\xc3\xaa.",
                    "Voc\xc3\xaa não vale nem o nó desta gravata!",
                  ],
    'HangUp': ["Voc\xc3\xaa foi desconectado.",
               "Tchau!",
               "Está na hora de terminar a sua conexão.",
               "...e não ligue de novo!",
               "Clique!",
               "A conversa acabou.",
               "Estou cortando este fio.",
               "Acho que voc\xc3\xaa está meio desligado.",
               "Parece que voc\xc3\xaa está com mau contato.",
               "Seu tempo acabou.",
               "Espero que tenha ouvido em claro e bom som.",
               "Foi engano.",
               ],
    'HeadShrink': ["Parece que voc\xc3\xaa tem ido ao analista.",
                   "Querida, encolhi o analista.",
                   "Espero que não precise analisar o seu amor-próprio.",
                   "Voc\xc3\xaa se abriu?",
                   "Analiso, logo existo.",
                   "Não é nada que faça voc\xc3\xaa perder a cabeça.",
                   "Voc\xc3\xaa vai abrir a cabeça?",
                   "Levanta essa cabeça! Ou será que é melhor abaixar?",
                   "Os objetos podem ser maiores do que parecem.",
                   "Os melhores Toons v\xc3\xaam nos menores frascos.",
                   ],
    'HotAir':["Estamos tendo uma discussão acalorada.",
              "Está rolando uma onda de calor.",
              "Atingi o meu ponto de ebulição.",
              "Que vento cortante.",
              "Odeio ter que te grelhar, mas...",
              "Lembre-se sempre: onde há fumaça, há fogo.",
              "Voc\xc3\xaa parece meio queimadinho.",
              "Outra reunião que virou fumaça.",
              "Acho que está na hora de botar lenha na fogueira.",
              "Deixe-me acender uma relação de trabalho.",
              "Tenho umas observações inflamadas pra voc\xc3\xaa.",
              "Ataque aéreo!!!",
              ],
    'Jargon':["Que besteira.",
              "Veja se voc\xc3\xaa consegue ver algum sentido nisso.",
              "Espero que tenha sido claro como água.",
              "Parece que vou ter que falar mais alto.",
              "Insisto em ter a palavra.",
              "Sou muito direto.",
              "Devo sustentar a minha opinião neste assunto.",
              "Olha, as palavras podem machucar voc\xc3\xaa.",
              "Entendeu o que eu quis dizer?",
              "Palavras, palavras, palavras, palavras, palavras.",
              ],
    'Legalese':["Voc\xc3\xaa deve se conformar e desistir.",
                "Voc\xc3\xaa vai ser derrotado, legalmente falando.",
                "Voc\xc3\xaa está ciente das implicações legais?",
                "Voc\xc3\xaa não está acima da lei!",
                "Devia haver uma lei contra voc\xc3\xaa.",
                "Não há lei marcial comigo!",
                "As opiniões expressadas neste ataque não são compartilhadas pela Toontown On-line da Disney.",
                "Não podemos ser responsabilizados por danos sofridos neste ataque.",
                "Os resultados deste ataque podem variar.",
                "Este ataque não tem validade legal quando proibido.",
                "Voc\xc3\xaa não se enquadra no meu sistema legal!",
                "Voc\xc3\xaa não sabe lidar com assuntos jur\xc3\xaddicos.",
                ],
    'Liquidate':["Gosto de manter as coisas fluindo.",
                 "Voc\xc3\xaa está com algum problema de fluxo de caixa?",
                 "Vou ter que lavar os seus bens.",
                 "\xc3\x89 hora de voc\xc3\xaa ser levado pelo fluxo.",
                 "Não se esqueça de que fica escorregadio quando está molhado.",
                 "Os números estão correndo.",
                 "Voc\xc3\xaa escorrega que nem sabão.",
                 "Está caindo tudo em cima de voc\xc3\xaa.",
                 "Acho que voc\xc3\xaa vai por ralo abaixo.",
                 "Voc\xc3\xaa tomou uma lavada.",
                 ],
    'MarketCrash':["Vou acabar com a sua festa.",
                   "Voc\xc3\xaa não vai sobreviver \xc3\xa0 queda.",
                   "Sou mais do que o mercado pode aguentar.",
                   "Tenho uma queda por voc\xc3\xaa!",
                   "Agora eu vou entrar detonando.",
                   "Sou um verdadeiro dragão no mercado.",
                   "Parece que o mercado está em baixa.",
                   "\xc3\x89 melhor voc\xc3\xaa sair fora rapidamente!",
                   "Vender! Vender! Vender!",
                   "Devo liderar a recessão?",
                   "Todo mundo está saindo fora, voc\xc3\xaa não vai?",
                   ],
    'MumboJumbo':["Deixe-me explicar melhor.",
                  "\xc3\x89 muito simples.",
                  "Vamos fazer desta maneira.",
                  "Deixe-me ampliar para voc\xc3\xaa.",
                  "Voc\xc3\xaa pode chamar isso de baboseira tecnológica.",
                  "Aqui estão meus eufemismos.",
                  "Caramba, isso é que é encher a boca.",
                  "Algumas pessoas me chamam de exagerado.",
                  "Posso me meter?",
                  "Acho que estas são as palavras certas.",
                   ],
    'ParadigmShift':["Cuidado! Eu saio pela tangente.",
                     "Prepare-se para mudar radicalmente!"
                     "Não é uma mudança interessante?"
                     "Voc\xc3\xaa vai ter que desviar de caminho.",
                     "Agora é sua vez de desviar.",
                     "Acabou o desvio!",
                     "Voc\xc3\xaa nunca trabalhou tanto neste desvio.",
                     "Estou transviando voc\xc3\xaa!",
                     "Olhe para o meu rabo de olho!",
                     ],
    'PeckingOrder':["Este aqui é para quem berra mais.",
                    "Prepare-se para o grito de guerra.",
                    "Por falta de um grito, morre um burro no atoleiro.",
                    "Vou ganhar no grito.",
                    "Voc\xc3\xaa está no último grito da hierarquia.",
                    "Se gritos resolvessem, porcos não morreriam!",
                    "A ordem está valendo, no grito!",
                    "Por que não grito com alguém do meu tamanho? Ah!",
                    "Cão que ladra não morde.",
                    ],
    'PickPocket': ["Deixe-me verificar os seus pertences.",
                   "E a\xc3\xad, qual é o pó?",
                   "\xc3\x89 mais fácil do que tirar doce de criança.",
                   "Golpe de mestre.",
                   "Deixa que eu seguro para voc\xc3\xaa.",
                   "Não tire os olhos de minhas mãos.",
                   "As mãos são mais rápidas que os olhos.",
                   "Não tenho nada para tirar da manga.",
                   "A ger\xc3\xaancia não se responsabiliza por extravio de itens.",
                   "Achado não é roubado.",
                   "Voc\xc3\xaa nem vai sentir.",
                   "Dois pra mim, um pra voc\xc3\xaa.",
                   "Está bom assim.",
                   "Voc\xc3\xaa não vai precisar mesmo...",
                   ],
    'PinkSlip': ["Tente imaginar que está tudo azul.",
                 "Tá com medo? Voc\xc3\xaa está azul!",
                 "Com certeza, este bilhete vai fazer voc\xc3\xaa ficar azul.",
                 "\xc3\x8apa, acho que mudei de cor, né?",
                 "Olha lá, voc\xc3\xaa não quer ficar azul, ou quer?",
                 "Este bilhete não é branco, é azul.",
                 "Estou azul de fome!",
                 "Voc\xc3\xaa se importa que eu passe a\xc3\xad para ver se está tudo azul?",
                 "O azul não é exatamente a sua cor.",
                 "Toma seu bilhete azul e fora daqui!",
                 ],
    'PlayHardball': ["Então voc\xc3\xaa quer jogar bola comigo?",
                     "Voc\xc3\xaa não quer jogar bola comigo.",
                     "Chuta forte!",
                     "Passa, cara, passa!",
                     "A\xc3\xad está o passe...",
                     "Voc\xc3\xaa vai precisar de um refresco do goleiro.",
                     "Vou jogar voc\xc3\xaa para fora do campo.",
                     "Depois que voc\xc3\xaa se contundir, vai direto para casa.",
                     "São 45 minutos do segundo tempo!",
                     "Voc\xc3\xaa não consegue jogar comigo!",
                     "Vou atingir voc\xc3\xaa.",
                     "Vou dar um chute com efeito na bola!",
                    ],
    'PoundKey': ["\xc3\x89 hora de retornar algumas ligações.",
                 "Gostaria de fazer uma ligação a cobrar.",
                 "Trrriiimmm - é para voc\xc3\xaa!",
                 "Voc\xc3\xaa quer brincar com o Jogo da Velha?",
                 "Tenho um método incr\xc3\xadvel para ganhar.",
                 "Está se sentindo nocauteado?",
                 "Vou dar um golpe neste número.",
                 "Deixe-me ligar para fazer uma surpresinha.",
                 "Vou ligar para voc\xc3\xaa.",
                 "O.K. Toon, é o fim para voc\xc3\xaa.",
                 ],
    'PowerTie': ["Eu ligo mais tarde, voc\xc3\xaa parece enrolado na gravata.",
                 "Voc\xc3\xaa está pronto para uma gravata?",
                 "Senhoras e senhores, esta é a gravata!",
                 "\xc3\x89 melhor aprender a dar este nó.",
                 "Vou manter a sua l\xc3\xadngua dentro do nó!",
                 "\xc3\x89 a gravata mais horr\xc3\xadvel que voc\xc3\xaa já comprou!",
                 "Está sentindo o aperto?",
                 "Minha gravata é muito mais poderosa que a sua!",
                 "Eu tenho o poder do nó!",
                 "Pelos poderes do nó, vou engravatar voc\xc3\xaa.",
                 ],
    'PowerTrip': ["Faça as malas, vamos fazer uma pequena viagem.",
                  "Voc\xc3\xaa fez uma boa viagem?",
                  "Boa viagem, acho que nos veremos na próxima temporada.",
                  "Como foi a viagem?",
                  "Desculpe ter \"viajado\" dessa maneira!",
                  "Voc\xc3\xaa parece viajandão.",
                  "Agora, voc\xc3\xaa sabe quem é a autoridade!",
                  "Tenho muito mais autoridade do que voc\xc3\xaa.",
                  "Quem manda agora?",
                  "Voc\xc3\xaa não pode lutar contra o poder.",
                  "O poder corrompe, principalmente em minhas mãos!",
                  ],
    'Quake': ["Vamos balançar, agitar e rolar.",
              "Tem muita vibração por aqui!",
              "As suas canelas estão tremendo.",
              "A\xc3\xad vem ele, este é grande!",
              "Este está fora da escala Richter.",
              "Agora é que a terra vai tremer!",
              "E a\xc3\xad, quem é que está agitando? Voc\xc3\xaa!",
              "Já esteve em um terremoto?",
              "Agora, voc\xc3\xaa está em território de tremores!",
              ],
    'RazzleDazzle': ["Leia os meus lábios.",
                     "Que acha da minha dentadura?",
                     "Não acha que tenho charme?",
                     "Vou impressionar voc\xc3\xaa.",
                     "Meu dentista faz um excelente trabalho.",
                     "Cegadores, não acha?",
                     "Não dá nem para acreditar que não é de verdade.",
                     "Chocante, né?",
                     "Vou dar um fim nisso.",
                     "Passo o fio dental após cada refeição.",
                     "Sorria!",
                     ],
    'RedTape': ["Isto deve acalmar o bicho.",
                "Vou te amarrar por um tempo.",
                "Voc\xc3\xaa está acorrentado.",
                "Veja se consegue cortar caminho por aqui.",
                "O bicho vai pegar.",
                "Tomara que voc\xc3\xaa tenha claustrofobia.",
                "Vou me certificar de que voc\xc3\xaa não vai escapulir.",
                "Vou ocupar voc\xc3\xaa com alguma coisa.",
                "Tente desatar o nó.",
                "Espero que voc\xc3\xaa concorde com os tópicos da reunião.",
                ],
'ReOrg': ["Voc\xc3\xaa não gostou da maneira como eu reorganizei as coisas!",
              "Talvez um pouco de organização seja bom.",
              "Voc\xc3\xaa não é tão ruim assim, só precisa se organizar.",
              "Voc\xc3\xaa gosta do meu tino para organização?",
              "Só pensei em dar um novo visual \xc3\xa0s coisas.",
              "Voc\xc3\xaa precisa se organizar!",
              "Voc\xc3\xaa parece um pouco desorganizado.",
              "Espera um pouco enquanto eu reorganizo os seus pensamentos.",
              "Só vou esperar até que voc\xc3\xaa se organize um pouco mais.",
              "Voc\xc3\xaa se importa se eu só der uma reorganizadinha?",
              ],
    'RestrainingOrder': ["Voc\xc3\xaa precisa levar broncas de vez em quando.",
                         "Estou te jogando na cara uma ordem repressora!",
                         "Voc\xc3\xaa não pode chegar nem um metro e meio perto de mim.",
                         "Talvez seja melhor voc\xc3\xaa manter distância.",
                         "Entre na linha.",
                         Cogs + "! Reprimam este Toon!",
                         "Tente entrar na linha sozinho.",
                         "Espero que eu esteja sendo bem repressor com voc\xc3\xaa.",
                         "Veja se voc\xc3\xaa consegue acabar com essa repressão!",
                         "Estou ordenando que voc\xc3\xaa se reprima!",
                         "Por que não começamos com uma repressão básica?"
                         ],
    'Rolodex': ["O seu cartão está aqui, em algum lugar.",
                "Aqui está o número do dedetizador.",
                "Quero dar o meu cartão a voc\xc3\xaa.",
                "Tenho o seu número bem aqui.",
                "Tenho tudo aqui sobre voc\xc3\xaa, de A a Z.",
                "Voc\xc3\xaa vai se virar com isso.",
                "D\xc3\xaa um giro pelas páginas.",
                "Cuidado com a papelada solta.",
                "Vou apontar o dedo para a letra que desejo.",
                "\xc3\x89 assim que eu consigo entrar em contato com voc\xc3\xaa?",
                "Quero ter certeza de que manteremos o contato.",
                ],
    'RubberStamp': ["Eu sempre causo uma boa impressão.",
                    "\xc3\x89 importante aplicar uma pressão firme e bem distribu\xc3\xadda.",
                    "Impressos perfeitos todas as vezes.",
                    "Quero carimbar voc\xc3\xaa.",
                    "Voc\xc3\xaa precisa ser DEVOLVIDO AO REMETENTE.",
                    "Voc\xc3\xaa foi CANCELADO.",
                    "Voc\xc3\xaa possui uma entrega de PRIORIDADE.",
                    "Vou me certificar de que a minha mensagem foi RECEBIDA.",
                    "Voc\xc3\xaa não vai a lugar nenhum - voc\xc3\xaa tem uma TARIFA POSTAL A PAGAR.",
                    "Preciso de uma resposta IMEDIATA.",
                    ],
    'RubOut': ["E agora, desapareceu!",
               "Sinto que perdi voc\xc3\xaa em algum lugar.",
               "Decidi deixar voc\xc3\xaa de fora.",
               "Eu sempre apago todos os obstáculos.",
               "Vou só apagar este erro.",
               "Posso fazer qualquer perturbação desaparecer.",
               "Gosto das coisas organizadas e limpas.",
               "Tente manter a animação.",
               "Estou vendo voc\xc3\xaa... Agora, não vejo voc\xc3\xaa.",
               "Vai ficar meio esmaecido.",
               "Vou eliminar o problema.",
               "Deixe-me cuidar das suas áreas problemáticas.",
               ],
    'Sacked':["Parece que voc\xc3\xaa foi embrulhado.",
              "Está no saco.",
              "Voc\xc3\xaa foi embolsado.",
              "Papel ou plástico?",
              "Meus inimigos serão ensacados!",
              "Eu tenho o recorde de Toontown de sacos por jogo.",
              "Voc\xc3\xaa não é mais bem-vindo por aqui.",
              "O seu tempo acabou aqui, voc\xc3\xaa vai ser ensacado!",
              "Deixe-me ensacar isto para voc\xc3\xaa.",
              "Nenhuma defesa se iguala ao meu ataque com sacos!",
              ],
    'Schmooze':["Voc\xc3\xaa nunca vai ver quando chega.",
                "Vai ficar legal em voc\xc3\xaa.",
                "Voc\xc3\xaa conseguiu.",
                "Não quero despejar nada em voc\xc3\xaa.",
                "Como puxa-saco, eu vou longe.",
                "Agora, eu vou florear bastante.",
                "\xc3\x89 hora de carregar nas tintas.",
                "Vou ressaltar o seu lado bom.",
                "Isso merece um bom tapinha nas costas.",
                "Vou falar bem de voc\xc3\xaa para todo mundo.",
                "Detesto tirá-lo do seu pedestal, mas...",
                ],
    'Shake': ["Voc\xc3\xaa está bem no epicentro.",
              "Voc\xc3\xaa está em cima da falha.",
              "Vai ser um sacolejo só.",
              "Acho que isso é um desastre natural.",
              "\xc3\x89 um desastre de proporções s\xc3\xadsmicas.",
              "Este está fora da escala Richter.",
              "\xc3\x89 hora de entrar na toca.",
              "Voc\xc3\xaa parece perturbado.",
              "Preparado para os solavancos?",
              "Voc\xc3\xaa vai sacolejar, e não centrifugar.",
              "Isso vai agitar voc\xc3\xaa.",
              "Sugiro um bom plano de fuga.",
              ],
    'Shred': ["Preciso me livrar de alguns fragmentos perigosos.",
              "As porções produzidas estão aumentando de quantidade.",
              "Acho que vou dispor de voc\xc3\xaa agora mesmo.",
              "Assim, a prova é eliminada.",
              "Não há como provar isso agora.",
              "Veja se voc\xc3\xaa consegue juntar os pedaços novamente.",
              "Assim, voc\xc3\xaa vai cortar as sobras e ficar do tamanho certo.",
              "Vou retalhar esta ideia todinha.",
              "Não queremos que isto caia nas mãos erradas.",
              "Fácil se tem, fácil se perde.",
              "Não é o seu último fio de esperança?",
              ],
    'Spin': ["O que me diz de sairmos para um giro?",
             "Voc\xc3\xaa usa a centrifugação?",
             "Isto vai fazer a sua cabeça girar de verdade!",
             "Este é o meu giro das coisas.",
             "Vou levar voc\xc3\xaa para uma volta.",
             "Como é que voc\xc3\xaa dá a \"volta\" no seu tempo?",
             "Olha só: voc\xc3\xaa não quer girar até ficar tonto?",
             "Nossa, voc\xc3\xaa está no meio de um furacão!",
             "Meus ataques vão fazer sua cabeça rodar!",
             ],
    'Synergy': ["Vou encaminhar ao comit\xc3\xaa.",
                "O seu projeto foi cancelado.",
                "O seu centro de custos será cortado.",
                "Estamos reestruturando o seu setor.",
                "Colocamos em votação, e voc\xc3\xaa perdeu.",
                "Acabei de receber a aprovação final.",
                "Uma boa equipe pode se livrar de qualquer problema.",
                "Já dou um retorno a voc\xc3\xaa sobre isso.",
                "Vamos direto ao que interessa.",
                "Vamos encarar isto como uma crise de sinergia.",
                ],
    'Tabulate': ["Isto não soma em nada.",
                 "Pela minha conta, voc\xc3\xaa perdeu.",
                 "Voc\xc3\xaa está fazendo um bom cálculo.",
                 "Vou fazer o seu total em um minuto.",
                 "Está preparado para estes números?",
                 "Sua conta já está vencida e pode ser paga.",
                 "\xc3\x89 hora de calcular.",
                 "Gosto de colocar as coisas em ordem.",
                 "E a contagem é...",
                 "Estes números devem ser muito poderosos.",
                 ],
    'TeeOff': ["Voc\xc3\xaa não vai bem de condições.",
               "Olha a frente!",
               "Confio no meu taco.",
               "Gandula, preciso do meu taco!",
               "Tente evitar este risco.",
               "D\xc3\xaa impulso!",
               "\xc3\x89 mesmo um furo dentro do outro.",
               "Voc\xc3\xaa está no meu campo.",
               "Repara só a precisão.",
               "Cuidado com o passarinho!",
               "Fique de olho na bola!",
               "Voc\xc3\xaa se importa se eu continuar a jogar?",
               ],
    'Tremor': ["Voc\xc3\xaa sentiu?",
               "Voc\xc3\xaa não tem medo de um tremorzinho de nada, ou tem?",
               "O tremor é apenas o começo.",
               "Voc\xc3\xaa parece tenso.",
               "Vou agitar as coisas um pouco!",
               "Tudo preparado para retumbar?",
               "O que houve? Voc\xc3\xaa parece balançado.",
               "Tremedeira de medo!",
               "Por que está tremendo de medo?",
               ],
    'Watercooler': ["Certamente, isto vai refrescar voc\xc3\xaa.",
                    "Não é refrescante?",
                    "Faço a entrega.",
                    "Direto da fonte - até a sua boca.",
                    "Qual é o problema, é só uma água de nascente.",
                    "Não se preocupe, é pura.",
                    "Ah, outro cliente satisfeito.",
                    "\xc3\x89 hora da entrega diária.",
                    "Espero que as suas cores não desbotem.",
                    "Quer beber?",
                    "Sai tudo na lavagem.",
                    "A bebida é com voc\xc3\xaa.",
                    ],
    'Withdrawal': ["Acho que voc\xc3\xaa está no vermelho.",
                   "Espero que o seu saldo seja o suficiente para cobrir isto.",
                   "Olha que vou cobrar juros.",
                   "O seu saldo está diminuindo.",
                   "Em breve, voc\xc3\xaa vai precisar fazer um depósito.",
                   "Voc\xc3\xaa sofreu um colapso financeiro.",
                   "Acho que voc\xc3\xaa está em baixa.",
                   "Suas finanças deca\xc3\xadram.",
                   "Prevejo um per\xc3\xadodo de vacas magras.",
                   "\xc3\x89 uma inversão de valores.",
                   ],
    'WriteOff': ["Deixe-me aumentar as suas perdas.",
                 "Vamos tirar o melhor proveito poss\xc3\xadvel de um mau negócio.",
                 "\xc3\x89 hora de fazer o balanço dos caixas.",
                 "Isso não vai ficar bom nos livros-caixa.",
                 "Procuro alguns dividendos.",
                 "Voc\xc3\xaa deve se responsabilizar por suas perdas.",
                 "Pode esquecer o bônus.",
                 "Vou bagunçar todas as suas contas.",
                 "Voc\xc3\xaa está prestes a sofrer algumas perdas.",
                 "Isto vai afetar os seus resultados finais.",
                 ],
    }

# DistributedBuilding.py
BuildingWaitingForVictors = "Aguardando outros jogadores...",

# Elevator.py
ElevatorHopOff = "Descer"
ElevatorStayOff = "Se descer, terá de esperar\naté que o elevador parta ou fique vazio"
ElevatorLeaderOff = "Somente seu l\xc3\xadder pode decidir quando deve descer."
ElevatorHoppedOff = "Voc\xc3\xaa precisa esperar o próximo elevador"
ElevatorMinLaff = "Voc\xc3\xaa precisa de %s pontos de risada para poder subir neste elevador"
ElevatorHopOK = "OK"
ElevatorGroupMember = "Somente o l\xc3\xadder deste grupo pode\ndecidir quando deve entrar"

# DistributedCogKart.py
KartMinLaff = "Voc\xc3\xaa precisa de %s pontos de risada para poder andar neste carte."

# DistributedBuilding.py
# DistributedElevatorExt.py
CogsIncExt = ", Ltda."
CogsIncModifier = "%s" + CogsIncExt
CogsInc = Cog.upper() + CogsIncExt
#CogdominiumsExt = " Cogdominiums"
# Translate
CogdominiumsExt = " Field Office"
Cogdominiums = Cog.upper() + CogdominiumsExt

# DistributedKnockKnockDoor.py
DoorKnockKnock = "Toc, toc."
DoorWhosThere = "Quem é?"
DoorWhoAppendix = " Quem?"
DoorNametag = "Porta"

# FADoorCodes.py
# Strings associated with codes
FADoorCodes_UNLOCKED = None
FADoorCodes_TALK_TO_TOM = "Voc\xc3\xaa precisa de piadas! Vá falar com o Tom Tutorial!"
FADoorCodes_DEFEAT_FLUNKY_HQ = "Volte aqui quando tiver derrotado o Puxa-saco!"
FADoorCodes_TALK_TO_HQ = "Vá pegar a sua recompensa com o Haroldo do Quartel!"
FADoorCodes_WRONG_DOOR_HQ = "Porta errada! Vá pela outra porta para o pátio!"
FADoorCodes_GO_TO_PLAYGROUND = "Direção errada! Voc\xc3\xaa precisa ir para o pátio!"
FADoorCodes_DEFEAT_FLUNKY_TOM = "Ande até o Puxa-saco para lutar com ele!"
FADoorCodes_TALK_TO_HQ_TOM = "Vá pegar a sua recompensa no Quartel dos Toons!"
FADoorCodes_SUIT_APPROACHING = None  # no message, just refuse entry.
FADoorCodes_BUILDING_TAKEOVER = "Cuidado! Tem um COG lá dentro!"
FADoorCodes_SB_DISGUISE_INCOMPLETE = "Voc\xc3\xaa vai ser pego se entrar lá como um Toon! Voc\xc3\xaa precisa completar o seu Disfarce de Cog primeiro!\n\nMonte o seu Disfarce de Cog com pedaços da Fábrica."
FADoorCodes_CB_DISGUISE_INCOMPLETE = "Voc\xc3\xaa vai ser pego se entrar lá como um Toon! Voc\xc3\xaa precisa completar o seu Disfarce de Robô Mercenário primeiro!\n\nMonte o seu Disfarce de Robô Mercenário executando Tarefas Toon na Sonholândia."
FADoorCodes_LB_DISGUISE_INCOMPLETE = "Voc\xc3\xaa vai ser pego se entrar lá como um Toon! Voc\xc3\xaa precisa completar o seu Disfarce de Cog primeiro!\n\nMonte o seu Disfarce de Cog com pedaços da Fábrica."
FADoorCodes_BB_DISGUISE_INCOMPLETE = "Voc\xc3\xaa vai ser pego se entrar lá como Toon! Primeiramente, voc\xc3\xaa precisa concluir seu Disfarce de Robô Chefe!\n\nConstrua seu Disfarce de Robô Chefe cumprindo as TarefasToon depois da Sonholândia do Donald."

# KnockKnock joke contest winners
KnockKnockContestJokes = {
    2100 : ["Jaque",
            "Jaque não está olhando, joga uma torta nele!"],

    # 2009 April fools contest Jokes. First few doors of Loopy lane
    2200 : {28:["Biscuit (Biscoito)",
            "Biscuitos (Biscoitos) me mordam, os Cogs v\xc3\xaam a\xc3\xad!"],
            41:["Dewey",
            "Dewemos ir detonar mais alguns Cogs?"],
            40:["Minnie",
            "Minnie-pessoas falaram comigo, e isso está me enlouquecendo!"],
##            25:["Biscuit25 (Biscoito25)",
##            "Biscuitos (Biscoitos) me mordam, os Cogs v\xc3\xaam a\xc3\xad!"],
            27:["Disguise",
            "A Disguisetante perseguição aos Cogs!"]},

    2300: ["Justa",
           "Justa gora peguei uns dois pedaços de Cogs, pronto!"],

    # Polar Place has multiple jokes so they are in a dict keyed of the propId of the door
    3300: { 10: ["Aladdin",
                   "Aladdinheiro no chão."],
            6 : ["Adon",
                 "Adondé que esses Cogs tão saindo?"],
            30 : ["Bacon",
                  "Bacon uma torta ia bem."],
            28: ["Isa\xc3\xadas",
                 "Isa\xc3\xadas mas voltou-se."],
            12: ["Julieta",
                 "Julieta me chamando praquele prédio Cog com voc\xc3\xaa pra eu te Toonar."],
            },
     }

# KnockKnockJokes.py
KnockKnockJokes = [
    ["Quem",
    "Aqui tem eco, não?"],

    ["Kika",
    "Kikalor!"],

    ["Joe",
    "Voc\xc3\xaa é Joetromundo?"],

    ["Eudin",
    "Eudinovo por aqui!"],

    ["Sil\xc3\xaancio",
    "Pssss!"],

    ["Simbó",
    "Simbora pra praia."],

    ["Takent",
    "Takent ou frio?"],

    ["Noá",
    "Noá de qu\xc3\xaa."],

    ["Não sei",
    "Nem eu, já te falei."],

    ["Otudo",
    "Otudo ou nada?"],

    ["Totan",
    "Totan feliz que voc\xc3\xaa está aqui!"],

    ["Osmar",
    "Osmartodontes não existem mais!"],

    ["Silem",
    "Silembra de mim?"],

    ["Ostra",
    "Ostra vez?"],

    ["Aimée",
    "Aimée Tida?"],

    ["Zoom",
    "Zooma imediatamente daqui!"],

    ["Aiki",
    "Aiki medo!"],

    ["Quiba",
    "Quibagunça é essa"],

    ["Tasó",
    "Não, tacompanhado."],

    ["Iago",
    "Iagora, José?"],

    ["'Tácom'",
    "'Tácom' tudo, não é?"],

    ["Tádi",
    "Tádi graça, é? Meu nome é "+Flippy+"."],

    ["Opato",
    "Opato "+Donald+" Deduct."],

     ["Masqui",
    "Masqui coisa, abre a porta logo."],

    ["Nénim.",
    "Nénim guém que te interesse, deixa eu entrar."],

    ["Omos",
    "Omosquito que te picou."],

    ["Colés",
    "Colesterol faz mal, sai fora."],

    ["Breno",
    "Breno que eu te falei que esse cara vinha."],

    ["Kiko",
    "Kiko-losso!"],

    ["Vaiv\xc3\xaa",
    "Vaiv\xc3\xaa que eu tô atrasado."],

    ["Quente",
    "Quente viu e quem te v\xc3\xaa!"],

    ["Vopri",
    "Vopri-meiro, tô com medo."],

    ["Eunum",
    "Eunum sei. Desculpe!"],

    ["Ubaldo",
    "Ubaldo é o marido da balda?"],

    ["Alfa",
    "Alface ou tomate?"],

    ["Ka",
    "Ka, L, M, N, O, P."],

    ["Justa",
    "Justagora que eu ia jantar."],

    ["Maki",
    "Makiagem é coisa para adultos."],

    ["Loga",
    "Logagora que eu entrei no banho."],

    ["Quessa",
    "Quessa B? Vou me mandar."],

    ["Masqui",
    "Masqui droga - abre a porta e pronto!"],

    ["'Jaques'",
    "'Jaquesou' importante, voc\xc3\xaa deveria falar comigo primeiro."],

    ["Mid\xc3\xaa",
    "Mid\xc3\xaaxa em paz!"],

    ["Undi",
    "Undia é da caça outro é do caçador."],

    ["Tudor",
    "Tudor que sobe, desce."],

    ["Acara",
    "Acara-puça serviu, hein?"],

    ["Aispe",
    "Aispe-rança é a última que morre."],

    ["K\xc3\xaania",
    "K\xc3\xaania sabe?"],

    ["Bemki",
    "Bemki te vi lá fora."],

    ["Jaca",
    "Jacaré no seco anda?"],

    ["Quenco",
    "Quenco-chicha o rabo espicha."],

    ["Tádi",
    "Tádi brincadeira, né? Deixa eu rir, então."],

    ["Ocessá",
    "Ocessá-be um monte de coisa, né?"],

    ["Temki",
    "Temki ter uma piada melhor que essa."],

    ["Cetá",
    "Cetá pensando que eu sou besta?"],

    ["Vôti",
    "Vôti botar pra correr."],

    ["Donalda",
    "Donalda não... São cinquenta centavos."],

    ["Alface",
    "Alface a face é mais emocionante."],

    ["Ivo",
    "Ivo c\xc3\xaa não sabia que não tem ninguém em casa?"],

    ["Quessa",
    "Quessa B\xc3\xaa? Essa brincadeira está um saco."],

    ["Quenfo",
    "Quenfo \xc3\xa0 roça perdeu a carroça."],

    ["Justa",
    "Justagora que eu ia embora."],

    ["Taca",
    "Taca mãe primeiro!"],

    ["Tanaka",
    "'Tanaka-ra' que voc\xc3\xaa não vai se dar bem!"],

    ["Quenfo",
    "Quenfo ao ar perdeu o lugar!"],

    ["Soé",
    "Soé jeito de falar com um amigo?"],

    ["Daum",
    "'Daum' tempo, pode ser?"],

    ["Isadora",
    "Isadora, o que é que eu faço?"],

    ["V\xc3\xaassi",
    "'V\xc3\xaassi' da próxima vez toma mais cuidado!"],

    ["Teá",
    "Teá-doro, mas isso também é demais."],

    ["Carlota",
    "A Carlota está presa na roda?"],

    ["Bu",
    "Eu nem me assustei."],

    ["Tu",
    "Tu, cara de tatu!"],

    ["Pó",
    "Pó-su entrar?"],

    ["Sará",
    "Sará que que tem outro jeito de entrar neste prédio?"],

    ["Mico",
    "Miconta que novidade é essa!"],

    ["Numi",
    "Numi amola e me deixa entrar."],

    ["Miá",
    "Miá-juda, a porta emperrou."],

    ["Nuncre",
    "Nuncre dita em mim?"],

    ["Dianta",
    "não Dianta falar, voc\xc3\xaa não vai abrir a porta..."],

    ["Dorré",
    "Mi, Fá, Sol, Lá, Si!"],

    ["Dexeu",
    "Dexeu ver quem ta\xc3\xad."],

    ["Tássia",
    "Tássia-chando, hem? Abre logo."],

    ["Omeu",
    "Omeu Deus do céu!"],

    ["Diza\xc3\xad",
    "Diza\xc3\xad o qu\xc3\xaa?"],

    ["Inter",
    "Interessante esta brincadeira."],

    ["Grato",
    "Não há de qu\xc3\xaa."],

    ["Quicão",
    "Quicão fusão é essa?"],

    ["Mamão",
    "Mamão mandou bater nesta daqui!"],

    ["Nunci",
    "Nunci deve comer de boca cheia."],

    ["Kiko",
    "E o Kiko eu tenho que saber sobre isso?"],

    ["Sil\xc3\xaancio",
    "Pssss!"],

    ["Vossocá",
    "Eu não, por favor."],

    ["Pu",
    "Pu xavida, voc\xc3\xaa me enganou."],

    ["Miá",
    "Miá corda, não me deixa perder o bondinho."],

    ["N\xc3\xadvea",
    "Feliz Niveassário!"],

    ["Sino",
    "O sino faz \"blém\" não \"quem\"."],

    ["Diki",
    "Diki lado voc\xc3\xaa está?"],

    ["Quer\xc3\xaa",
    "Quer\xc3\xaa não é pod\xc3\xaa."],

    ["Frankstein",
    "Frankstein, mas voc\xc3\xaa não tem."],

    ["Pra Z",
    "Pra Z em conhec\xc3\xaa-lo."],

    ["Ex-conde",
    "Ex-conde-conde é legal."],

    ["Apri",
    "Apri-ncesa despertou com o beijo do pr\xc3\xadncipe."],

    ["Quacker",
    "Quacker uma, menos esta!"],

    ["Qualquerco",
    "Qualquerco-isa parecida com isto já vai me ajudar."],

    ["Quiqui",
    "'Quiqui' é isso?"],

    ["Abá",
    "Abá-xaqui, a chave caiu!"],

    ["Póba",
    "Póba-t\xc3\xaa, esqueci a piada!"],

    ["Urralo",
    "Urralo-ween já passou!"],

    ["Sará",
    "Sará que tem um médico em casa?"],

    ["Aline",
    "Aline é reta ou curva?"],

    ["Dôdis",
    "Dôdis tômago."],

    ["Dôdi",
    "Dôdi dente."],

    ["Toco",
    "Toco dor de cabeça."],

    ["Atch",
    "Saúde."],

    ["Aumen",
    "Aumen-te o volume, por favor."],

    ["Zupra",
    "Zupra-sumo."],

    ["Tupó",
    "Tupó descer ali comigo?"],
]

# CChatChatter.py

# Shared Chatter

SharedChatterGreetings = [
        "Oi, %!",
        "Iuhuuu %, legal ver voc\xc3\xaa.",
        "Estou feliz que voc\xc3\xaa esteja aqui hoje!",
        "Bom, oi pessoal, %.",
        ]

SharedChatterComments = [
        "Que nome legal, %.",
        "Gosto do seu nome.",
        "Cuidado com os " + Cogs + ".",
        "Parece que o bondinho está chegando!",
        "Preciso jogar um jogo no bondinho para ganhar algumas tortas!",
        "\xc3\x80s vezes, eu me divirto com os jogos no bondinho só para comer a torta de frutas!",
        "Puxa, acabei de deter um bando de " + Cogs + ". Preciso de descanso!",
        "Puxa vida, alguns desses " + Cogs + " são grandalhões!",
        "Voc\xc3\xaa parece estar se divertindo.",
        "Nossa, que dia legal!",
        "Gostei da sua roupa.",
        "Acho que vou pescar esta tarde.",
        "Divirta-se no meu bairro.",
        "Espero que voc\xc3\xaa esteja aproveitando sua estada em Toontown!",
        "Ouvi falar que está nevando no Brrrgh.",
        "Voc\xc3\xaa pegou o bondinho hoje?",
        "Gosto de conhecer pessoas novas.",
        "Uau, há vários "+ Cogs +" no Brrrgh.",
        "Eu adoro brincar de pique. E voc\xc3\xaa?",
        "Os jogos no bondinho são divertidos.",
        "Adoro fazer as pessoas rirem.",
        "\xc3\x89 divertido ajudar meus amigos.",
        "Hum-hum, voc\xc3\xaa está perdido? Não se esqueça de que voc\xc3\xaa tem um mapa no \xc3\x81lbum Toon.",
        "Procure não ficar atolado na Burocracia dos " + Cogs + "'.",
        #"Ouvi falar que a " + Daisy + " plantou novas flores no jardim.",
        "Se voc\xc3\xaa pressionar a tecla Page Up, poderá ver acima!",
        "Se voc\xc3\xaa ajudar a tomar os edif\xc3\xadcios dos Cogs, poderá ganhar uma estrela de bronze!",
        "Se voc\xc3\xaa pressionar a tecla Tab, poderá ver os arredores sob diversos ângulos!",
        "Se voc\xc3\xaa pressionar a tecla Ctrl, poderá descer!",
        ]

SharedChatterGoodbyes = [
        "Tenho que ir agora, tchau!",
        "Acho que vou jogar no bondinho.",
        "Bom, até mais. Vejo voc\xc3\xaa por a\xc3\xad, %!",
        "Melhor eu me apressar e voltar ao trabalho para deter esses "+ Cogs +".",
        "Preciso ir andando.",
        "Desculpe, mas tenho que ir.",
        "Tchau.",
        "Vejo voc\xc3\xaa mais tarde, %!",
        "Acho que vou praticar lançamento de bolinhos.",
        "Vou me juntar a um grupo para deter alguns "+Cogs+".",
        "Foi legal ver voc\xc3\xaa hoje, %.",
        "Tenho muito a fazer hoje. \xc3\x89 melhor começar logo.",
        ]

# Lines specific to each character.
# If a talking char is mentioned, it cant be shared among them all

MickeyChatter = (
        [ # Greetings specific to Mickey
        "Bem-vindo ao "+lToontownCentral+".",
        "Oi, meu nome é " + Mickey + ". Qual é o seu?",
        ],
        [ # Comments
        "Ei, voc\xc3\xaa viu o "+ Donald +"?",
        "Vou ver o nevoeiro passar no "+lDonaldsDock+".",
        "Se voc\xc3\xaa vir o meu camarada "+Goofy+", d\xc3\xaa um oi para ele por mim.",
        "Ouvi falar que a "+Daisy+" plantou novas flores no jardim."
        ],
       [ # Goodbyes
        "Vou para a Melodilândia ver a "+Minnie+"!",
        "Caramba, estou atrasado para meu encontro com a "+ Minnie +"!",
        "Parece que é hora de "+ Pluto +" jantar.",
        "Acho que vou nadar no "+lDonaldsDock+".",
        "\xc3\x89 hora de tirar um cochilo. Vou para a Sonholândia.",
        "Ouvi falar que a " + Daisy + " plantou novas flores no jardim.",
        ]
    )

WinterMickeyCChatter = (
        [ # Greetings specific to Mickey
        "Olá, eu sou o Mickey Noel!",
        "Bem-vindo \xc3\xa0 cidade das estrelas... ou melhor, a Toontown!",
        "Boas-Festas!",
        "Boas-Festas, %",
        ],
        [ # Comments
        "Cante a música da estação na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolverá o favor!",
        "Nossa, este lugar está bem decorado!",
        "Cante a música da estação na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolverá o favor!",
        "Veja só as luzes na árvore! Que maravilha!",
        "Cante a música da estação na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolverá o favor!",
        "Nenhuma criatura está se movendo, a não ser este rato aqui!",
        "Cante a música da estação na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolverá o favor!",
        "Adoro esta época do ano!",
        "Cante a música da estação na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolverá o favor!",
        "Eu estou muito feliz, e voc\xc3\xaa?",
        "Cante a música da estação na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolverá o favor!",
        "Voc\xc3\xaa conhece alguma boa canção de Natal?",
        "Cante a música da estação na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolverá o favor!",
        "Poxa! Eu adoro a época das Festas!",
        "Cante a música da estação na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolverá o favor!",
        "Acho que está na hora de colocar luvas mais quentinhas!",
        ],
        [ # Goodbyes
        "Tenha boas Festas!",
        "Tudo de bom para voc\xc3\xaa!",
        "Que pena que voc\xc3\xaa tem de ir embora. Até logo!",
        "Vou cantar canções de Natal com a Minnie!",
        ]
    )

ValentinesMickeyChatter = (
    [
    "Olá, eu sou o Mickey!",
    "Bem-vindo \xc3\xa0 Dia dos namorados!",
    "Feliz Dia dos namorados!",
    "Feliz Dia dos namorados, %",
    ],
    [
    "O Amor está no ar! E borboletas também!",
    "Aqueles corações são bons para melhorar o Laff!",
    "Espero que a Minnie goste do que eu trouxe para ela!",
    "O Cattlelog tem vários presentes para o Dia dos namorados!",
    "D\xc3\xaa uma festa Dia dos namorados!",
    "Mostre aos Cogs, com uma torta na cara, que voc\xc3\xaa os ama!",
    "Estou levando a Minnie para o Kooky Café!",
    "A Minnie vai querer chocolates ou flores?",
    ],
    [
    "Adorei a sua visita!",
    "Diga \xc3\xa0 Minnie que a pegarei em breve!",
    ]
    )

WinterMickeyDChatter = (
        [ # Greetings specific to Mickey
        'Olá, eu sou o Mickey Noel!',
        'Bem-vindo \xc3\xa0 cidade das estrelas... ou melhor, a Toontown!',
        'Boas-Festas!',
        'Boas-Festas, %',
        ],
        [ # Comments
        'Nossa, este lugar está bem decorado!',
        'Veja só as luzes na árvore! Que maravilha!',
        'Nenhuma criatura está se movendo, a não ser este rato aqui!',
        'Adoro esta época do ano!',
        'Eu estou muito feliz, e voc\xc3\xaa?',
        'Voc\xc3\xaa conhece alguma boa canção de Natal?',
        'Poxa! Eu adoro a época das Festas!',
        'Acho que está na hora de colocar luvas mais quentinhas!',
        ],
        [ # Goodbyes
        'Tenha boas Festas!',
        'Tudo de bom para voc\xc3\xaa!',
        'Que pena que voc\xc3\xaa tem de ir embora. Até logo!',
        'Vou cantar canções de Natal com a Minnie!',
        ]
    )

VampireMickeyChatter = (
        [ # Greetings specific to Vampire Mickey
        "Bem-vindo ao " + lToontownCentral + ".",
        "Oi, meu nome é " + Mickey + ". Qual é o seu?",
        "Feliz Halloween!",
        "Feliz Halloween, %!",
        "Bem-vindo ao Centro da Cidade Assombrada... quero dizer, ao " + lToontownCentral + "!",
        ],
        [ # Comments
        "Se voc\xc3\xaa acha que fazer travessuras é divertido, visite Ralf Desocupado, na Só Diversão, para ganhar uma gostosura!",
        "\xc3\x89 divertido vestir fantasias para o Halloween!",
        "Se voc\xc3\xaa acha que fazer travessuras é divertido, visite Ralf Desocupado, na Só Diversão, para ganhar uma gostosura!",
        "Voc\xc3\xaa gosta da minha fantasia?",
        "Se voc\xc3\xaa acha que fazer travessuras é divertido, visite Ralf Desocupado, na Só Diversão, para ganhar uma gostosura!",
        "%, tome cuidado com os Cogs Vampiros!",
        "Se voc\xc3\xaa acha que fazer travessuras é divertido, visite Ralf Desocupado, na Só Diversão, para ganhar uma gostosura!",
        "As decorações de Halloween ficaram ótimas, né?",
        "Se voc\xc3\xaa acha que fazer Diversões e Jogos, visite Ralf Desocupado, na Só Diversão, para ganhar uma gostosura!",
        "Tome cuidado com os gatos pretos!",
        "Se voc\xc3\xaa acha que fazer Diversões e Jogos, visite Ralf Desocupado, na Só Diversão, para ganhar uma gostosura!",
        "Voc\xc3\xaa viu o Toon com a cabeça de abóbora?",
        "Se voc\xc3\xaa acha que fazer Diversões e Jogos, visite Ralf Desocupado, na Só Diversão, para ganhar uma gostosura!",
        "Bu! Eu assustei voc\xc3\xaa?",
        "Se voc\xc3\xaa acha que fazer Diversões e Jogos, visite Ralf Desocupado, na Só Diversão, para ganhar uma gostosura!",
        "Não se esqueça de escovar as presas!",
        "Se voc\xc3\xaa acha que fazer Diversões e Jogos, visite Ralf Desocupado, na Só Diversão, para ganhar uma gostosura!",
        "Não se assuste, sou um vampiro bonzinho!",
        "Se voc\xc3\xaa acha que fazer Diversões e Jogos, visite Ralf Desocupado, na Só Diversão, para ganhar uma gostosura!",
        "Espero que voc\xc3\xaa esteja gostando da nossa diversão de Halloween!",
        "Se voc\xc3\xaa acha que fazer Diversões e Jogos, visite Ralf Desocupado, na Só Diversão, para ganhar uma gostosura!",
        "Os vampiros estão muito populares este ano!",
        ],
        [ # Goodbyes
        "Vou olhar as decorações curiosas de Halloween.",
        "Vou a Melodilândia fazer uma surpresa \xc3\xa0 " + Minnie + "!",
        "Vou assustar outro Toon! Shhh!",
        "Vou brincar de doces ou travessuras!",
        "Shhh, vem comigo.",
        ]
    )

"""VampireMickeyChatter = (
        [ # Greetings specific to Vampire Mickey
        "Bem-vindo ao "+lToontownCentral+".",
        "Oi, meu nome é "+Mickey+". Qual é o seu?",
        "Feliz Halloween!",
        "Feliz Halloween, %!",
        "Bem-vindo ao Centro da Cidade Assombrada... quero dizer ao "+lToontownCentral+"!",
        ],
        [ # Comments
        "\xc3\x89 divertido se vestir para o Halloween!",
        "Gostou da minha fantasia?",
        "%, cuidado com os  Cogs Sanguessugas!",
        "As decorações de Halloween não são fantásticas?",
        "Cuidado com os gatos pretos",
        "Voc\xc3\xaa viu o Toon com a cabeça de abóbora?",
        "Buu! Assustei voc\xc3\xaa?",
        "Não se esqueça de escovar suas presas",
        "Não tenha medo, sou um vampiro amigável",
        "Gostou da minha capa?",
        "Assustei voc\xc3\xaa? Foi a melhor brincadeira da minha vida!",
        "Espero que esteja curtindo nossa festa de Halloween!",
        "Assombroso, está escuro como a noite!",
        ],
        [ # Goodbyes
        "Vou olhar as decorações curiosas de Halloween.",
        "Vou a Melodilândia fazer uma surpresa \xc3\xa0 "+Minnie+"!",
        "Vou assustar outro Toon! Shhh!",
        "Vou brincar de doces ou travessuras!",
        "Shhh, vem comigo.",
        ]
    )"""

MinnieChatter = (
        [ # Greetings
        "Bem-vindo \xc3\xa0 Melodilândia.",
        "Oi, meu nome é "+ Minnie +". Qual é o seu?"
        ],
        [ # Comments
        "As colinas ganham vida com o som da música!",
        # the merry no longer goes round
        #"Não deixe de tentar andar no carrossel gigante!",
        "Sua roupa é legal, %.",
        "Ei, voc\xc3\xaa viu o "+ Mickey +"?",
        "Se voc\xc3\xaa vir meu amigo "+ Goofy +", d\xc3\xaa um oi para ele por mim.",
        "Uau, há milhares de "+ Cogs +" perto da "+lDonaldsDreamland+".",
        "Ouvi falar que tem neblina no "+lDonaldsDock+".",
        "Não deixe de experimentar o labirinto dos "+lDaisyGardens+".",
        "Acho que vou catar algumas canções.",
        "Ei, %, olha aquilo lá.",
        "Adoro o som da música.",
        "Aposto que voc\xc3\xaa não sabia que a Melodilândia também é chamada de ToadaTown! Ah, ah, ah!",
        "Adoro jogo da memória. E voc\xc3\xaa?",
        "Gosto de fazer as pessoas rirem.",
        "Cara, andar sobre rodas o dia todo não é moleza para os pés!",
        "Bonita camisa, %.",
        "Aquilo no chão é uma balinha?",
        "Ouvi falar que a " + Daisy + " plantou novas flores no jardim.",
        ],
        [ # Goodbyes
        "Caramba, estou atrasada para o meu encontro com o "+ Mickey +"!",
        "Parece que é hora de "+ Pluto +" jantar.",
        "\xc3\x89 hora de tirar um cochilo. Vou para a Sonholândia.",
        ]
    )

WinterMinnieCChatter = (
        [ # Greetings
        "Olá, eu sou a Minnie Noel!",
        "Bem-vindo \xc3\xa0 terra das canções de Natal!",
        "Boas-Festas!",
        "Boas-Festas, %!",
        ],
        [ # Comments
        "Voc\xc3\xaa vai ganhar muito mais do que um corte de cabelo se cantar para Bárbara Sevilha na Um Penteado por Uma Canção!",
        "Solte a voz, Toon!",
        "Voc\xc3\xaa vai ganhar muito mais do que um corte de cabelo se cantar para Bárbara Sevilha na Um Penteado por Uma Canção!",
        "Mostre como se canta, Toon!",
        "Voc\xc3\xaa vai ganhar muito mais do que um corte de cabelo se cantar para Bárbara Sevilha na Um Penteado por Uma Canção!",
        "Voc\xc3\xaa consegue seguir a melodia de Melodilândia?",
        "Voc\xc3\xaa vai ganhar muito mais do que um corte de cabelo se cantar para Bárbara Sevilha na Um Penteado por Uma Canção!",
        "Essas lâmpadas parecem estar bem quentinhas com o cachecol!",
        "Voc\xc3\xaa vai ganhar muito mais do que um corte de cabelo se cantar para Bárbara Sevilha na Um Penteado por Uma Canção!",
        "Cantar é tudo!",
        "Voc\xc3\xaa vai ganhar muito mais do que um corte de cabelo se cantar para Bárbara Sevilha na Um Penteado por Uma Canção!",
        "Sempre vou gostar de voc\xc3\xaa, mesmo cantando mal!",
        "Voc\xc3\xaa vai ganhar muito mais do que um corte de cabelo se cantar para Bárbara Sevilha na Um Penteado por Uma Canção!",
        "Tudo fica mais bonito com flores!",
        ],
        [ # Goodbyes
        "Divirta-se muito durante as Festas!",
        "Caminhos felizes!",
        "Mickey vai me levar para cantar canções de natal!",
        ]
    )

WinterMinnieDChatter = (
        [ # Greetings
        "Olá, eu sou a Minnie Noel!",
        "Bem-vindo \xc3\xa0 terra das canções de Natal!",
        "Boas-Festas!",
        "Boas-Festas, %!",
        ],
        [ # Comments
        "Solte a voz, Toon!",
        "Mostre como se canta, Toon!",
        "Voc\xc3\xaa consegue seguir a melodia de Melodilândia?",
        "Essas lâmpadas parecem estar bem quentinhas com o cachecol!",
        "Cantar é tudo!",
        # Translate
        "You can't go wrong with a song!",
        "Sempre vou gostar de voc\xc3\xaa, mesmo cantando mal!",
        "Tudo fica mais bonito com flores!",
        ],
        [ # Goodbyes
        "Divirta-se muito durante as Festas!",
        "Caminhos felizes!",
        "Mickey vai me levar para cantar canções de natal!",
        ]
    )

ValentinesMinnieChatter = (
    [
    "Olá, eu sou a Minnie!",
    "Feliz Dia dos namorados!",
    "Feliz Dia dos namorados, %",
    ],
    [
    "Espero que o Mickey traga chocolates ou flores para mim!",
    "Aqueles corações são bons para melhorar o Laff!",
    "Eu quero ir a uma festa ValenToon!",
    "Espero que o Mickey me leve ao Kooky Café!",
    "Mickey é um ótimo Dia dos namorados!",
    "O que voc\xc3\xaa trouxe para seu Dia dos namorados ",
    "O Mickey nunca perdeu um Dia dos namorados!",
    ],
    [
    "Espalhe o amor!",
    "Adorei sua visita!",
    ]
)

WitchMinnieChatter = (
        [ # Greetings
        "Bem-vindo a uma terra mágica... ou melhor, \xc3\xa0 Terra da Melodia!",
        "Olá, meu nome é Minnie Mágica! Qual é o seu?",
        "Olá, acho voc\xc3\xaa um encanto!",
        "Feliz Halloween!",
        "Feliz Halloween, %!",
        ],
        [ # Comments
        "Ouvi dizer que Tábata tem gostosuras para aqueles que sabem fazer travessuras lá na Gatinha Bacana!",
        "\xc3\x89 um dia mágico, não acha?",
        "Ouvi dizer que Tábata tem gostosuras para aqueles que sabem fazer travessuras lá na Gatinha Bacana!",
        "Onde eu coloquei meu livro de magia?",
        "Ouvi dizer que Tábata tem gostosuras para aqueles que sabem fazer travessuras lá na Gatinha Bacana!",
        "Abracadabra!",
        "Ouvi dizer que Tábata tem gostosuras para aqueles que sabem fazer travessuras lá na Gatinha Bacana!",
        "Toontown está assustadora hoje!",
        "Ouvi dizer que Tábata tem gostosuras para aqueles que sabem fazer travessuras lá na Gatinha Bacana!",
        "Voc\xc3\xaa também está vendo estrelas?",
        "Ouvi dizer que Tábata tem gostosuras para aqueles que sabem fazer travessuras lá na Gatinha Bacana!",
        "Roxo é a minha cor favorita!",
        "Ouvi dizer que Tábata tem gostosuras para aqueles que sabem fazer travessuras lá na Gatinha Bacana!",
        "Espero que o seu Halloween seja um susto só!",
        "Ouvi dizer que Tábata tem gostosuras para aqueles que sabem fazer travessuras lá na Gatinha Bacana!",
        "Tome cuidado com as aranhas musicais!",
        "Ouvi dizer que Tábata tem gostosuras para aqueles que sabem fazer travessuras lá na Gatinha Bacana!",
        "Espero que voc\xc3\xaa esteja gostando da nossa diversão de Halloween!",
        ],
        [ # Goodbyes
        "Eu vou desaparecer agora!",
        "Está na hora de desaparecer!",
        "Mickey vai me levar para pedir gostosuras!",
        ]
    )

DaisyChatter = (
        [ # Greetings
        "Bem-vindo(a) ao meu Jardim!",
        "Olá, meu nome é "+Daisy+". Qual o seu nome?",
        "\xc3\x89 muito bom ver voc\xc3\xaa, %!",
        ],
        [ # Comments
        "Minha flor premiada está no centro do labirinto do jardim.",
        "Eu adoro andar pelo labirinto.",
        "Eu não v\xc3\xad o "+Goofy+" hoje.",
        "Eu gostaria de saber onde o "+Goofy+" está.",
        "Voc\xc3\xaa viu o "+Donald+"? Eu não consigo encontrá-lo em lugar algum.",
        "Se voc\xc3\xaa vir minha amiga "+Minnie+", por favor diga \"Oi\" por mim.",
        "Quanto melhor as ferramentas de jardinagem que voc\xc3\xaa tem, melhor será seu jardim.",
        "Existem muitos "+Cogs+" perto do "+lDonaldsDock+".",
        "Regando seu jardim diariamente voc\xc3\xaa deixa suas plantas felizes.",
        "Para cultivar uma Margarida Rosa, plante uma balinha amarela e uma vermelha juntas.",
        "\xc3\x89 facil cultivar uma Margarida Amarela. Basta plantar uma balinha amarela.",
        "Se voc\xc3\xaa vir areia embaixo de uma planta, está na hora de regar ou ela morrerá.",
        ],
        [ # Goodbyes
        "Estou indo para Melodilândia para ver %s!" % Minnie,
        "Preciso correr para o meu picnic com %s!" % Donald,
        "Acho que vou nadar no "+lDonaldsDock+".",
        "Oh, estou com sono. Acho que vou para a Sonholândia.",
        ]
    )

ValentinesDaisyChatter = (
    [
    "Olá, eu sou a Margarida!",
    "Feliz Dia dos namorados!",
    "Feliz Dia dos namorados, %"
    ],
    [
    "Espero que o Donald não me traga outro Amore Eel!",
    "O Donald está me levando ao 'Deep-Sea'!",
    "Com certeza, eu tenho rosas suficientes!",
    "Aqueles corações são bons para melhorar o Laff!",
    "Eu adoraria ir a uma festa Dia dos namorados!",
    "Este é um jardim onde o amor cresce!",
    "\xc3\x89 bom que o Donald não durma novamente no Dia dos namorados!",
    "Talvez eu e o Donald possamos sair com o Mickey e a Minnie!",
    ],
    [
    "Diga ao Donald que eu estou esperando por ele!",
    "Feliz Dia dos namorados!",
    ]
)

WinterDaisyCChatter = (
        [ # Greetings
        "Bem-vindo ao único jardim que cresce no inverno!",
        "Boas-Festas!",
        "Boas-Festas, %!",
        ],
        [ # Comments
        "Suzana, da Artesanato P\xc3\xadnus, adora música, então por que não compor uma canção de Natal para ela?",
        "Meu jardim precisa de mais visco!",
        "Suzana, da Artesanato P\xc3\xadnus, adora música, então por que não compor uma canção de Natal para ela?",
        "Preciso plantar azevinho para o ano que vem!",
        "Suzana, da Artesanato P\xc3\xadnus, adora música, então por que não compor uma canção de Natal para ela?",
        "Vou pedir para o Pateta construir uma casa de biscoito de gengibre para mim!",
        "Suzana, da Artesanato P\xc3\xadnus, adora música, então por que não compor uma canção de Natal para ela?",
        "Essas luzes são lindas!",
        "Suzana, da Artesanato P\xc3\xadnus, adora música, então por que não compor uma canção de Natal para ela?",
        "O azevinho deixa o ambiente mais alegre!",
        "Suzana, da Artesanato P\xc3\xadnus, adora música, então por que não compor uma canção de Natal para ela?",
        "Meu boneco de neve sempre derrete!",
        "Suzana, da Artesanato P\xc3\xadnus, adora música, então por que não compor uma canção de Natal para ela?",
        "Que pato mais enfeitado!",
        "Suzana, da Artesanato P\xc3\xadnus, adora música, então por que não compor uma canção de Natal para ela?",
        "Eu mesma que criei todas estas luzes!",
        ],
        [ # Goodbyes
        "Tenha Festas cheias de alegria!",
        "Boa plantação!",
        "Diga a Donald para trazer meus presentes!",
        "Donald vai me levar para cantar canções de natal!",
        ]
    )

WinterDaisyDChatter = (
        [ # Greetings
        "Bem-vindo ao único jardim que cresce no inverno!",
        "Boas-Festas!",
        "Boas-Festas, %!",
        ],
        [ # Comments
        "Meu jardim precisa de mais visco!",
        "Preciso plantar azevinho para o ano que vem!",
        "Vou pedir para o Pateta construir uma casa de biscoito de gengibre para mim!",
        "Essas luzes são lindas!",
        "O azevinho deixa o ambiente mais alegre!",
        "Meu boneco de neve sempre derrete!",
        "Que pato mais enfeitado!",
        "Eu mesma que criei todas estas luzes!",
        ],
        [ # Goodbyes
        "Tenha Festas cheias de alegria!",
        "Boa plantação!",
        "Diga a Donald para trazer meus presentes!",
        "Donald vai me levar para cantar canções de natal!",
        ]
    )

HalloweenDaisyChatter = (
        [ # Greetings
        "Bem-vindo ao jardim fantasma... quer dizer, ao jardim da Margarida!",
        "Feliz Halloween!",
        "Feliz Halloween, %!",
        ],
        [ # Comments
        "Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada Pá de Coisa, para ganhar gostosuras!",
        "Quer dançar?",
        "Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada Pá de Coisa, para ganhar gostosuras!",
        "Sou um pato com uma saia poodle!",
        "Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada Pá de Coisa, para ganhar gostosuras!",
        "A árvore pirata precisa de água.",
        "Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada Pá de Coisa, para ganhar gostosuras!",
        "Gostosuras ou árvores!",
        "Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada Pá de Coisa, para ganhar gostosuras!",
        "Voc\xc3\xaa notou algo estranho nas árvores?",
        "Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada Pá de Coisa, para ganhar gostosuras!",
        "Eu deveria plantar algumas abóboras!",
        "Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada Pá de Coisa, para ganhar gostosuras!",
        "QUEM notou algo diferente nas lâmpadas?",
        "Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada Pá de Coisa, para ganhar gostosuras!",
        "Eu realmente gosto do Halloween!",
        "Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada Pá de Coisa, para ganhar gostosuras!",
        "Gostosuras ou galhos!",
        "Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada Pá de Coisa, para ganhar gostosuras!",
        "Aposto que voc\xc3\xaa não reparou nas lâmpadas assustadoras!",
        "Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada Pá de Coisa, para ganhar gostosuras!",
        "Espero que voc\xc3\xaa esteja gostando da nossa diversão de Halloween!",
        ],
        [ # Goodbyes
        "Donald vai me levar para pedir gostosuras!",
        "Vou dar uma olhada nas decorações divertidas de Halloween."
        ]
    )


ChipChatter = (
        [ # Greetings
        "Boas-vindas a %s!" % lOutdoorZone,
        "Olá, sou " + Chip + ". Qual é o seu nome?",
        "Não, eu sou " + Chip + ".",
        "\xc3\x89 tão bom ver voc\xc3\xaa, %!",
        "Somos Tico e Teco!",
        ],
        [ # Comments
        "Gosto de golfe.",
        "Temos as melhores bolotas de Toontown.",
        "Os buracos de golfe com vulcões são os mais desafiadores para mim.",
        ],
        [ # Goodbyes
        "Vamos até " + lTheBrrrgh +" brincar com %s." % Pluto,
        "Vamos visitar %s e dar um jeito nele." % Donald,
        "Acho que vou nadar no " + lDonaldsDock + ".",
        "Oh, estou com sono. Acho que vou até a Sonholândia.",
        ]
    )

ValentinesChipChatter = (
    [ # Greetings
    "Eu sou o Tico!",
    "Feliz Dia dos namorados!",
    "Feliz Dia dos namorados, %!",
    ],
    [ # Comments
    "O que voc\xc3\xaa trouxe para mim no Dia dos namorados, Teco?",
    "Aqueles corações são bons para melhorar o Laff!",
    "Voc\xc3\xaa será meu ValenToon, Teco?",
    "O que voc\xc3\xaa pegou para os Cogs para o Dia dos namorados, Teco?",
    "Eu amo o Dia dos namorados!",
    ],
    [ # Goodbyes
    "Volte quando quiser!",
    ]
)

WinterChipChatter = (
        [ # Greetings
        "Boas-Festas!",
        "Vestidos como esquilos!",
        "Boas-Festas, %!",
        ],
        [ # Comments
        "Boas-Festas, Teco!",
        "E nós pensávamos que toda esta água congelaria no inverno!",
        "Dever\xc3\xadamos trocar as bolas de golfe por bolas de neve!",
        "Se ao menos os esquilos soubessem cantar!",
        "Eu disse para VOC\xc3\x8a fazer isso!",
        "Eu disse para VOC\xc3\x8a fazer isso!",
        ],
        [ # Goodbyes
        "Tenha Festas cheias de alegria!",
        "Não se esqueça de dar um presente aos Cogs por nós!",
        ]
    )

HalloweenChipChatter = (
        [ # Greetings
        "Jogue um pouco de miniterror... quer dizer, minigolfe!",
        "Feliz Halloween!",
        "Feliz Halloween, %!",
        ],
        [ # Comments
        "Somos malucos por Halloween!",
        "Voc\xc3\xaa está preso.",
        "Voc\xc3\xaa não pode fugir do braço longo da lei.",
        "Sou um Tira!",
        "Espero que esteja curtindo a nossa diversão de Halloween!",
        "Jogue golfe a acerte o Buraco do Medo.",
        "As balinhas são mais doces do que as bolotas.",
        "Espero que voc\xc3\xaa esteja gostando da nossa diversão de Halloween!",
        ],
        [ # Goodbyes
        "%, tome cuidado com os Cogs Vampiros!",
        ]
    )


# Warning Dale's chatter is dependent on on Chip's, they should match up
DaleChatter = (
        [ # Greetings
        "\xc3\x89 tão bom ver voc\xc3\xaa, %!",
        "Olá, sou " + Dale + ". Qual é o seu nome?",
        "Olá, sou " + Chip + ".",
        "Boas-vindas a %s!" % lOutdoorZone,
        "Somos Tico e Teco!",
        ],
        [ # Comments
        "Gosto de piqueniques.",
        "As bolotas são gostosas, experimente.",
        "Aqueles moinhos também são dif\xc3\xadceis.",
        ],
        [ # Goodbyes
        "Hihihi, é divertido brincar com " + Pluto + ".",
        "Sim, vamos dar um jeito em %s." % Donald,
        "Ah, seria refrescante dar uma nadada.",
        "Estou ficando cansado, uma boa soneca cairia bem.",
        ]
    )

ValentinesDaleChatter = (
    [ # Greetings
    "Eu sou o Teco!",
    "Feliz Dia dos namorados!",
    "Feliz Dia dos namorados, %s!",
    ],
    [ # Comments
    "O mesmo do ano passado. NADA!",
    "Eu perdi as nozes!",
    "Voc\xc3\xaa será meu Dia dos namorados, Tico?",
    "Uma torta na cara!",
    "Sim, é legal.",
    ],
    [ # Goodbyes
    "Nós estaremos livres durante todo o Dia dos namorados!",
    ]
)

WinterDaleChatter = (
        [ # Greetings
        "Boas-Festas!",
        "Olá, somos dois elfos do Natal!",
        "Esquilos Noéis!",
        "Boas-Festas, %!",
        ],
        [ # Comments
        "Boas-Festas, Tico!",
        "E nós pensávamos que toda esta água congelaria no inverno!",
        "Dever\xc3\xadamos trocar as bolas de golfe por bolas de neve!",
        "Se ao menos os esquilos soubessem cantar!",
        "Voc\xc3\xaa se lembrou de guardar as nozes para o inverno?",
        "Oh-oh!",
        ],
        [ # Goodbyes
        "Tenha Festas cheias de alegria!",
        "Não se esqueça de dar um presente aos cogs por nós!",
        ]
    )

HalloweenDaleChatter = (
        [ # Greetings
        "Feliz Halloween, %!",
        "Jogue um pouco de miniterror... quer dizer, minigolfe!",
        "Feliz Halloween!",
        ],
        [ # Comments
        "Somos malucos por Halloween!",
        "\xc3\x93timo, posso usar o restante!",
        "Mas seus braços são curtos!",
        "Achei que voc\xc3\xaa fosse uma Lasca!",
        "Jogue golfe a acerte o Buraco do Medo.",
        "As balas de milho são mais doces do que as bolotas.",
        "Espero que esteja curtindo a nossa diversão de Halloween!",
        ],
        [ # Goodbyes
        "%, tome cuidado com os Cogs Vampiros!"
        ]
    )

GoofyChatter = (
        [ # Greetings
        "Bem-vindo aos "+lDaisyGardens+".",
        "Oi, meu nome é "+ Goofy +". Qual é o seu?",
        "Puxa, muito legal ver voc\xc3\xaa %!",
        ],
        [ # Comments
        "Cara, com certeza é fácil se perder no labirinto do jardim!",
        "Não deixe de tentar entrar no labirinto.",
        "Não vi a "+ Daisy +" o dia todo.",
        "Onde será que a "+ Daisy +" está?",
        "Ei, voc\xc3\xaa viu o "+ Donald +"?",
        "Se voc\xc3\xaa vir o meu amigo "+ Mickey +", d\xc3\xaa um oi para ele por mim.",
        "Ah, não! Esqueci de fazer o café da manhã do "+ Mickey +"!",
        "Puxa, com certeza há muitos "+ Cogs +" perto do "+lDonaldsDock+".",
        "Parece que a "+ Daisy +" plantou novas flores no jardim.",
        "Na filial da minha Loja de Piadas no Brrrgh, há \xc3\x93culos hipnóticos em promoção por apenas uma balinha!",
        "As Lojas de piadas do Pateta oferecem as melhores gozações, truques e comédias de toda Toontown!",
        "Nas Lojas de piadas do Pateta, todas as tortas na cara t\xc3\xaam garantia de fazer rir, ou voc\xc3\xaa tem as suas balinhas de volta!",
        ],
        [ # Goodbyes
        "\Vou para Melodilândia para ver a  "+ Minnie +"!",
        "Caramba, estou atrasado para o meu jogo com o  "+ Donald + "!",
        "Acho que vou nadar no Porto do "+lDonaldsDock+".",
        "\xc3\x89 hora de tirar um cochilo. Vou para a Sonholândia.",
        ]
    )

WinterGoofyChatter = (
        [ # Greetings
        "Eu sou o Pateta e adoro a época das Festas!",
        "Bem-vindo ao Circuito Bola de Neve!",
        "Boas-Festas!",
        "Boas-Festas, %!",
        ],
        [ # Comments
        "Quem precisa de renas quando se tem um kart veloz?",
        "Nossa! Já chegaram as Festas?",
        "Eu preciso dos meus protetores de orelha!",
        "Ainda não comecei a comprar os presentes!",
        "Não dirija seu kart no gelo!",
        "Parece que faz apenas um ano que estávamos na época das Festas!",
        "Deixe o seu kart todo enfeitado!",
        "Estes karts são melhores do que qualquer trenó velho!",
        "\xc3\x89 dif\xc3\xadcil dirigir com a cabeça de um boneco de neve?",
        ],
        [ # Goodbyes
        "Tenha Festas muito felizes!",
        "Dirija com cuidado!",
        "Cuidado com as renas aladas!",
        ]
    )

ValentinesGoofyChatter = (
    [
    "Eu sou o Pateta e estou animado para o Dia ValenToon!",
    "Feliz Dia dos namorados!",
    "Feliz Dia dos namorados, %!",
    ],
    [
    "Nossa! Já é o Dia dos namorados?",
    "Eu ADORO corrida de kart!",
    "Seja bacana com os outros!",
    "Mostre ao seu amor o novo kart!",
    "Toons amam seus karts!",
    "Faça alguns novos amigos na pista!",
    ],
    [
    "Dirija com cuidado!",
    "Demonstre um pouco de amor!",
    ]
)

GoofySpeedwayChatter = (
        [ # Greetings
        "Bem-vindo a "+lGoofySpeedway+".",
        "Oi, meu nome é "+Goofy+". Qual é o seu?",
        "Puxa, muito legal ver voc\xc3\xaa %!",
        ],
        [ # Comments
        "Cara, assisti a uma corrida maneira hoje.",
        "Cuidado com as cascas de banana na pista!",
        "Voc\xc3\xaa deu uma incrementada no seu kart?",
        "A gente acabou de pegar uns aros novos na loja do kart.",
        "Oi, voc\xc3\xaa viu "+Donald+"?",
        "Se voc\xc3\xaa vir meu amigo "+Mickey+", diz que eu mandei um alô.",
        "Ah, não! Esqueci de preparar para "+Mickey+" o café da manhã!",
        "Puxa, com certeza há muitos "+Cogs+" perto de "+lDonaldsDock+".",
        "Na filial da minha Loja de Piadas no Brrrgh, há \xc3\x93culos hipnóticos em promoção por apenas uma balinha!",
        "As Lojas de piadas do Pateta oferecem as melhores gozações, truques e comédias de toda Toontown!",
        "Nas Lojas de piadas do Pateta, todas as tortas na cara t\xc3\xaam garantia de fazer rir, ou voc\xc3\xaa tem as suas balinhas de volta!"
        ],
        [ # Goodbyes
        "Vou para Melodilândia para ver %s!" % Mickey,
        "Caramba, estou atrasado para o meu jogo com %s!" % Donald,
        "Acho que vou nadar no "+lDonaldsDock+".",
        "\xc3\x89 hora de tirar um cochilo. Vou para a Sonholândia.",
        ]
    )

SuperGoofyChatter = (
        [ # Greetings
        "Bem-vindo ao Supercircuito!",
        "Olá, eu sou o Superpateta! Qual é o seu nome?",
        "Feliz Halloween!",
        "Feliz Halloween, %!",
        ],
        [ # Comments
        "Estou me sentindo corajoso hoje!",
        "Alguém viu minha capa por a\xc3\xad? Ah, a\xc3\xad está ela!",
        "Nossa! Não conheço a minha própria força!",
        "Alguém chamou um super-herói?",
        "Cuidado, Cogs! Eu salvarei o Halloween!",
        "Não há nada mais assustador do que eu dirigindo um kart!",
        "Aposto que voc\xc3\xaa não está me reconhecendo por trás da máscara!",
        "\xc3\x89 divertido vestir fantasias para o Halloween!",
        "Espero que voc\xc3\xaa esteja gostando da nossa diversão de Halloween!",
        ],
        [ # Goodbyes
        "Preciso ir voando!",
        "Para o alto!",
        "Será que vou voando ou dirigindo até a Doca do Donald?",
        "Nossa, feliz Halloween!",
        ]
    )

DonaldChatter = (
        [ # Greetings
        "Bem-vindo \xc3\xa0 Sonholândia.",
        "Oi, meu nome é "+ Donald +". Qual é o seu?",
        ],
        [ # Comments
        "\xc3\x80s vezes este lugar me dá arrepios.",
        "Não deixe de experimentar o labirinto dos "+lDaisyGardens+".",
        "Nossa, que dia legal!",
        "Ei, voc\xc3\xaa viu o "+ Mickey +"?",
        "Se voc\xc3\xaa vir meu parceiro "+ Goofy +", d\xc3\xaa um oi para ele por mim.",
        "Acho que vou pescar esta tarde.",
        "Uau, há um monte de "+ Cogs +" no "+lDonaldsDock+".",
        "Escuta, eu não levei voc\xc3\xaa ainda para um passeio no "+lDonaldsDock+"?",
        "Não vi a "+ Daisy +" o dia todo.",
        "Ouvi falar que a "+ Daisy +" plantou novas flores no jardim.",
        "Quack.",
        ],
        [ # Goodbyes
        "Vou a Melodilândia para ver a "+ Minnie +"!",
        "Ah não, estou atrasado para o meu encontro com a "+ Daisy +"!",
        "Acho que vou nadar no meu cais.",
        "Acho que vou levar meu barco para um giro no meu cais.",
        ]
    )

WinterDreamlandCChatter = (
        [ # Greetings
        "Olá, eu sou o Donald Sonolento!",
        "Bem-vindo \xc3\xa0 Terra dos Sonhos!",
        "Boas-Festas!",
        "Boas-Festas, %!",
        ],
        [ # Comments
        "Samuel diz que aprender a cantar em Fala Dormindo é um verdadeiro privilégio. Vá até a Escola de Canto, cante uma canção e descubra por qu\xc3\xaa!",
        "Queria estar na minha cama, debaixo do cobertor!",
        "Samuel diz que aprender a cantar em Fala Dormindo é um verdadeiro privilégio. Vá até a Escola de Canto, cante uma canção e descubra por qu\xc3\xaa!",
        "Estou sonhando com uma Toontown toda branquinha!",
        "Samuel diz que aprender a cantar em Fala Dormindo é um verdadeiro privilégio. Vá até a Escola de Canto, cante uma canção e descubra por qu\xc3\xaa!",
        "Eu queria ter deixado leite e biscoitos!",
        "Samuel diz que aprender a cantar em Fala Dormindo é um verdadeiro privilégio. Vá até a Escola de Canto, cante uma canção e descubra por qu\xc3\xaa!",
        "Quando eu acordar, quero ver um monte de presentes!",
        "Samuel diz que aprender a cantar em Fala Dormindo é um verdadeiro privilégio. Vá até a Escola de Canto, cante uma canção e descubra por qu\xc3\xaa!",
        "Espero que eu não durma durante as Festas!",
        "Samuel diz que aprender a cantar em Fala Dormindo é um verdadeiro privilégio. Vá até a Escola de Canto, cante uma canção e descubra por qu\xc3\xaa!",
        "Adoro tirar uma soneca no frio!",
        "Samuel diz que aprender a cantar em Fala Dormindo é um verdadeiro privilégio. Vá até a Escola de Canto, cante uma canção e descubra por qu\xc3\xaa!",
        "As árvores nas ruas estão cobertas de luzes!",
        ],
        [ # Goodbyes
        "Uma boa-noite para todos!",
        "Doces sonhos!",
        "Quando eu acordar, vou cantar canções de Natal!",
        ]
    )

WinterDreamlandDChatter = (
        [ # Greetings
        "Olá, eu sou o Donald Sonolento!",
        "Bem-vindo \xc3\xa0 Terra dos Sonhos!",
        "Boas-Festas!",
        "Boas-Festas, %!",
        ],
        [ # Comments
        "Queria estar na minha cama, debaixo do cobertor!",
        "Estou sonhando com uma Toontown toda branquinha!",
        "Eu queria ter deixado leite e biscoitos!",
        "Quando eu acordar, quero ver um monte de presentes!",
        "Espero que eu não durma durante as Festas!",
        "Adoro tirar uma soneca no frio!",
        "As árvores nas ruas estão cobertas de luzes!",
        ],
        [ # Goodbyes
        "Uma boa-noite para todos!",
        "Doces sonhos!",
        "Quando eu acordar, vou cantar canções de Natal!",
        ]
    )

HalloweenDreamlandChatter = (
        [ # Greetings
        "Feliz Halloween!",
        "Feliz Halloween, %!",
        "Olá, eu sou o FrankenDonald",
        ],
        [ # Comments
        "Se voc\xc3\xaa conseguir fazer uma travessura com o meu amigo Máximo, poderá visitar o Relaxe ao Máximo e saborear uma gostosura!",
        "Meus sonhos estão assustadores hoje!",
        "Se voc\xc3\xaa conseguir fazer uma travessura com o meu amigo Máximo, poderá visitar o Relaxe ao Máximo e saborear uma gostosura!",
        "Acho que estou sonhando. Aquela lâmpada virou uma bruxa!",
        "Se voc\xc3\xaa conseguir fazer uma travessura com o meu amigo Máximo, poderá visitar o Relaxe ao Máximo e saborear uma gostosura!",
        "Estou sonhando ou aquele Toon tem uma cabeça de abóbora?",
        "Se voc\xc3\xaa conseguir fazer uma travessura com o meu amigo Máximo, poderá visitar o Relaxe ao Máximo e saborear uma gostosura!",
        "Quando eu acordar, espero que não esteja tudo tão assustador! ",
        "Se voc\xc3\xaa conseguir fazer uma travessura com o meu amigo Máximo, poderá visitar o Relaxe ao Máximo e saborear uma gostosura!",
        "Espero que eu não durma durante o Halloween!",
        "Se voc\xc3\xaa conseguir fazer uma travessura com o meu amigo Máximo, poderá visitar o Relaxe ao Máximo e saborear uma gostosura!",
        "Espero que voc\xc3\xaa esteja gostando da nossa diversão de Halloween!",
        ],
        [ # Goodbyes
        "Durma com as luzes acesas hoje!",
        "Quando eu acordar, vou pedir gostosuras!",
        ]
    )

ValentinesDreamlandChatter = (
    [
        "Olá, eu sou (bocejo) o Donald!",
        "Feliz Dia dos namorados!",
        "Feliz Dia dos namorados, %!",
    ],
    [
        "Espero não dormir no Dia dos namorados!",
        "Estava sonhando com a Margarida!",
        "Eu tive um pesadelo no qual eu perdia o Dia dos namorados!",
        "Aqueles corações são bons para melhorar o Laff!",
        "D\xc3\xaa uma festa Dia dos namorados!",
        "Mostre aos Cogs, com uma torta na cara, que voc\xc3\xaa os ama!",
        "Eu não poderia sonhar com um feriado melhor do que o Dia dos namorados!",
        "Eu amo dormir!",
    ],
    [
        "Boa-noite!",
        "Acorde-me no Dia dos namorados!",
    ]
)

HalloweenDonaldChatter = (
        [ # Greetings
        "Bem-vindo ao meu porto do Halloween!",
        "Se voc\xc3\xaa tiver gostosuras, poderá subir a bordo!",
        "Feliz Halloween!",
        "Feliz Halloween, %!",
        ],
        [ # Comments
        "Se voc\xc3\xaa não se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ",
        "Mas eu uso roupa de marinheiro todos os dias!",
        "Se voc\xc3\xaa não se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ",
        "Abóboras fazem ótimas lanternas!",
        "Se voc\xc3\xaa não se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ",
        "Nunca vi palmeiras com pernas peludas!",
        "Se voc\xc3\xaa não se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ",
        "Talvez eu me vista de pirata no próximo Halloween!",
        "Se voc\xc3\xaa não se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ",
        "Minhas gostosuras preferidas são as estrelas-do-mar!",
        "Se voc\xc3\xaa não se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ",
        "Vou levar voc\xc3\xaa para pedir gostosuras pelo porto!",
        "Se voc\xc3\xaa não se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ",
        "Espero que essas aranhas continuem nas árvores!",
        "Se voc\xc3\xaa não se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ",
        "Por que os fantasmas não se afogam? Porque eles usam boia!",
        "Se voc\xc3\xaa não se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ",
        "Espero que voc\xc3\xaa esteja gostando da nossa diversão de Halloween!",
        ],
        [ # Goodbyes
        "Vamos partir para levar alguns sustos!",
        "Boa-assombração!",
        "Vou dar uma olhada nas decorações assustadoras de Halloween.",
        ]
    )

ValentinesDonaldChatter = (
    [
    "Olá, eu sou o Donald!",
    "Feliz Dia dos namorados!",
    "Feliz Dia dos namorados, %!",
    ],
    [
    "Eu deveria levar a Margarida para algum lugar no Dia dos namorados?\xe2\x80\x9d",
    "Só mais uma volta no cais e eu pegarei alguma coisa para a Margarida.",
    "O que a Margarida gostaria de ganhar no Dia dos namorados?",
    "Aqueles corações na água são bons para melhorar o Laff!",
    "D\xc3\xaa uma festa no Dia dos namorados!",
    "Mostre aos Cogs, com uma torta na cara, que voc\xc3\xaa os ama!",
    "Eu preciso pegar um Amore Eel para a Margarida!",
    ],
    [
    "Aloha!",
    "Mande minhas lembranças aos Cogs!",
    ]
)

WinterDonaldCChatter = (
        [ # Greetings
        "Bem-vindo \xc3\xa0 Parada de Barcos e Trenós do Donald!",
        "Todos a bordo para o cruzeiro das Festas!",
        "Boas-Festas!",
        "Boas-Festas, %!",
        ],
        [ # Comments
        "Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, dá um presente para aquele que tiver uma canção!",
        "Voc\xc3\xaa gostou da decoração de patinhos?",
        "Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, dá um presente para aquele que tiver uma canção!",
        "Por que há neve nos postes?",
        "Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, dá um presente para aquele que tiver uma canção!",
        "\xc3\x89 bom que esta água não congele!",
        "Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, dá um presente para aquele que tiver uma canção!",
        "Como eles acenderam as luzes nessas árvores?",
        "Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, dá um presente para aquele que tiver uma canção!",
        "Será que este barco é melhor do que um trenó?",
        "Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, dá um presente para aquele que tiver uma canção!",
        "Este barco não precisa ser puxado por renas!",
        "Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, dá um presente para aquele que tiver uma canção!",
        "Fico feliz por não ser um peru nesta época do ano!",
        "Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, dá um presente para aquele que tiver uma canção!",
        "Meu presente para voc\xc3\xaa? Passeios de barco grátis!",
        "Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, dá um presente para aquele que tiver uma canção!",
        "Espero que eu não ganhe carvão de novo!",
        "Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, dá um presente para aquele que tiver uma canção!",
        ],
        [ # Goodbyes
        "Todos a bordo para começar a diversão das Festas!",
        "Lembre-se de dar uma gorjeta para o capitão do barco!",
        "Aproveite as Festas!",
        ]
    )

WinterDonaldDChatter = (
        [ # Greetings
        "Bem-vindo \xc3\xa0 Parada de Barcos e Trenós do Donald!",
        "Todos a bordo para o cruzeiro das Festas!",
        "Boas-Festas!",
        "Boas-Festas, %!",
        ],
        [ # Comments
        "Voc\xc3\xaa gostou da decoração de patinhos?",
        "Por que há neve nos postes?",
        "\xc3\x89 bom que esta água não congele!",
        "Como eles acenderam as luzes nessas árvores?",
        "Será que este barco é melhor do que um trenó?",
        "Este barco não precisa ser puxado por renas!",
        "Fico feliz por não ser um peru nesta época do ano!",
        "Meu presente para voc\xc3\xaa? Passeios de barco grátis!",
        "Espero que eu não ganhe carvão de novo!",
        ],
        [ # Goodbyes
        "Todos a bordo para começar a diversão das Festas!",
        "Lembre-se de dar uma gorjeta para o capitão do barco!",
        "Aproveite as Festas!",
        ]
    )

WesternPlutoChatter = (
        [# Greetings
        "Bu! Não se assuste, sou eu... Pluto!",
        "Feliz Halloween, parceiro!",
        "Feliz Halloween, %!",
        ],
        [ # Comments
        "Fred Cavanhaque, da Não Há Lugar como o Lar, troca gostosuras por travessuras, pois isso o faz se Neve é Doce Neve.",
        "Eu troco travessuras por gostosuras!",
        "Fred Cavanhaque, da Não Há Lugar como o Lar, troca gostosuras por travessuras, pois isso o faz se Neve é Doce Neve.",
        "Mickey vai me levar para pedir gostosuras mais tarde!",
        "Fred Cavanhaque, da Não Há Lugar como o Lar, troca gostosuras por travessuras, pois isso o faz se Neve é Doce Neve.",
        "Estou me sentindo mais nas Festas do que no Halloween!",
        "Fred Cavanhaque, da Não Há Lugar como o Lar, troca gostosuras por travessuras, pois isso o faz se Neve é Doce Neve.",
        "Auau! Esse é o jeito canino de pedir gostosuras!",
        "Fred Cavanhaque, da Não Há Lugar como o Lar, troca gostosuras por travessuras, pois isso o faz se Neve é Doce Neve.",
        "Espero que voc\xc3\xaa esteja gostando da nossa diversão de Halloween!",
        "Fred Cavanhaque, da Não Há Lugar como o Lar, troca gostosuras por travessuras, pois isso o faz se Neve é Doce Neve.",
        "Gosto de perseguir gatos pretos!",
        ],
        [ # Goodbyes
        "Agora vou desenterrar uma gostosura!",
        "Vou procurar Mickey e ver se ele tem alguma gostosura!",
        "Vou assustar o Donald!",
        ]
    )

WinterPlutoCChatter = (
        [# Greetings
        "Olá, eu sou o Pluto!",
        "Bem-vindo a Brrr. Aqui é frio o ano inteiro!",
        "Boas-Festas!",
        "Boas-Festas, %",
        ],
        [ # Comments
        "Abrão o Abominável adoraria uma canção, pois a Terra do Homem de Neve é um lugar solitário para um pé-grande.",
        "Eu mordi um picolé e fiquei com dor de cabeça!",
        "Abrão o Abominável adoraria uma canção, pois a Terra do Homem de Neve é um lugar solitário para um pé-grande.",
        "\xc3\x89 como viver em um globo de neve!",
        "Abrão o Abominável adoraria uma canção, pois a Terra do Homem de Neve é um lugar solitário para um pé-grande.",
        "Queria estar ao lado de uma boa fogueira!",
        "Abrão o Abominável adoraria uma canção, pois a Terra do Homem de Neve é um lugar solitário para um pé-grande.",
        "Au! Au! Eu preciso de um cachecol!",
        "Abrão o Abominável adoraria uma canção, pois a Terra do Homem de Neve é um lugar solitário para um pé-grande.",
        "Pelo menos meu focinho não está vermelho e brilhando!",
        ],
        [ # Goodbyes
        "Divirta-se muito durante as Festas!",
        "Volte sempre que voc\xc3\xaa quiser ver neve!",
        "Mickey vai me levar para cantar canções de natal!",
        ]
    )

WinterPlutoDChatter = (
        [# Greetings
        "Olá, eu sou o Pluto!",
        "Bem-vindo a Brrr. Aqui é frio o ano inteiro!",
        "Boas-Festas!",
        "Boas-Festas, %",
        ],
        [ # Comments
        "Eu mordi um picolé e fiquei com dor de cabeça!",
        "\xc3\x89 como viver em um globo de neve!",
        "Queria estar ao lado de uma boa fogueira!",
        "Au! Au! Eu preciso de um cachecol!",
        "Pelo menos meu focinho não está vermelho e brilhando!",
        ],
        [ # Goodbyes
        "Divirta-se muito durante as Festas!",
        "Volte sempre que voc\xc3\xaa quiser ver neve!",
        "Mickey vai me levar para cantar canções de natal!",
        ]
    )

# April Fools Chatter's
AFMickeyChatter = (
        [ # Greetings specific to Mickey
        "Feliz Semana dos April Toons (Toons de Abril)!",
        "Feliz Semana dos April Toons (Toons de Abril), %!",
        "Oi, meu nome é "+Mickey+". Qual é o seu?",
        ],
        [ # Comments
        "Voc\xc3\xaa viu a Margarida por a\xc3\xad?",
        "Queria desejar uma feliz Semana dos April Toons (Toons de Abril) para a Margarida!",
        "Voc\xc3\xaa ouviu um Rabisco falar?",
        "Oh, essas flores são lindas!",
        "Aposto que a Margarida tem ótimas dicas de Jardinagem!",
        ],
        [ # Goodbyes
        "Oi, estou procurado a Margarida. Voc\xc3\xaa a viu?",
        "\xc3\x89 hora de dar uma cochilada. Vou para a Sonholândia.",
        ]
    )

AFMinnieChatter = (
        [ # Greetings
        "Oi, meu nome é "+Minnie+". Qual é o seu?",
        "Feliz Semana dos April Toons (Toons de Abril)!",
        "Feliz Semana dos April Toons (Toons de Abril), %!",
        ],
        [ # Comments
        "Oi, preciso dar de comer ao Pluto. Voc\xc3\xaa o viu?",
        "Queria desejar uma feliz Semana dos April Toons (Toons de Abril) para o Pluto com um biscoito canino!",
        "Voc\xc3\xaa ouviu um Rabisco falar?",
        ],
        [ # Goodbyes
        "Oi, preciso dar de comer ao Pluto. Voc\xc3\xaa o viu?",
        "Nossa, estou atrasada para meu encontro com o %s!" % Mickey,
        ]
    )

AFDaisyChatter = (
        [ # Greetings
        "Oi, sou a "+Daisy+". Qual é o seu nome?",
        "Feliz Semana dos April Toons (Toons de Abril)!",
        "Feliz Semana dos April Toons (Toons de Abril), %!",
        ],
        [ # Comments
        "Queria saber se o Mickey foi combater alguns Cogs?",
        "Voc\xc3\xaa viu o Mickey por a\xc3\xad?",
        "Queria desejar uma feliz Semana dos April Toons (Toons de Abril) para o Mickey!",
        "Voc\xc3\xaa ouviu um Rabisco falar ou estou ouvindo coisas?",
        ],
        [ # Goodbyes
        "Oi, preciso falar com o Micky (Mickey). Voc\xc3\xaa o viu?",
        "Acho que vou nadar no "+lDonaldsDock+".",
        "Oh, estou com soninho. Acho que vou para a Sonholândia",
        ]
    )

AFGoofySpeedwayChatter = (
        [ # Greetings
        "Feliz Semana da Preguiça, hã, dos April Toons (Toons de Abril)!",
        "Feliz Semana dos April Toons (Toons de Abril), %!",
        "Oi, meu nome é "+Goofy+". Qual é o seu?",
        ],
        [ # Comments
        "Ohoh, voc\xc3\xaa viu o Donald? Acho que ele está sonâmbulo novamente",
        "Queria desejar uma feliz Semana dos April Toons (Toons de Abril) para o Donald!",
        "Voc\xc3\xaa ouviu um Rabisco falar ou estou vendo coisas?",
        "Espero que tudo esteja bem no Autódromo.",
        ],
        [ # Goodbyes
        "Ohoh, estou atrasado para meu jogo com o %s!" % Donald,
        ]
    )

AFDonaldChatter = (
        [ # Greetings
        "Feliz Semana da Preguiça, hã, dos April Toons (Toons de Abril)!",
        "Feliz Semana dos April Toons (Toons de Abril), %!",
        "Oi, meu nome é %s. Qual é o seu?" % Donald,
        ],
        [ # Comments
        "Voc\xc3\xaa viu o Pateta por a\xc3\xad?",
        "Queria desejar uma feliz Semana dos April Toons (Toons de Abril) para o Pateta!",
        "Voc\xc3\xaa ouviu um Rabisco falar ou estou sonhando?",
        "De onde surgiu esse kart?",
        ],
        [ # Goodbyes
        "De onde surgiram repentinamente todos esses carros barulhentos?",
        "Vou para Melodilândia ver a %s!" % Minnie,
        ]
    )

AFDonaldDockChatter = (
        [ # Greetings
        "Feliz Semana Abril Toons!",
        "Feliz Semana Abril Toons, %!",
        ],
        [ # Comments
        "Todo mundo folga na Semana Abril Toons, menos eu!",
        "Eu sou o único que tem de trabalhar nesta semana!",
        "Eu só descanso quando durmo!",
        "Todos os meus amigos estão fingindo ser outras pessoas!",
        "Rodando e rodando neste barco, o dia todo!",
        "Eu ouvi dizer que Margarida está fingindo ser o Mickey!",
        "Estamos na semana mais boba do ano e eu a estou perdendo!",
        "Voc\xc3\xaa já escutou o seu Doodle falar?",
        "A Gravidade tirou férias!",
        ],
        [ # Goodbyes
        "Tenha uma Louca Semana Abril Toons!",
        "Pregue uma peça nos Cogs por mim!",
        ]
    )

AFPlutoChatter = (
        [ # Greetings
        "Feliz Semana Abril Toons!",
        "Feliz Semana Abril Toons, %!",
        ],
        [ # Comments
        "Bem-vindo \xc3\xa0 Terra da Melodia! Eu sou a " + Minnie + "!",
        "Oi, meu nome é " + Minnie + " Mouse!",
        "Eu são tão feliz quanto uma ratinha pode ser!",
        "O qu\xc3\xaa? Voc\xc3\xaa nunca viu uma ratinha com orelhas de cachorro?",
        "Eu adoro quando " + Mickey + " e eu sa\xc3\xadmos para passear!",
        "O qu\xc3\xaa? Voc\xc3\xaa nunca ouviu um rato falar antes?",
        "A Semana Abril Toons é a mais boba do ano!",
        "Voc\xc3\xaa já escutou o seu Doodle falar?",
        "A Gravidade tirou férias!",
        ],
        [ # Goodbyes
        "Tenha uma Louca Semana Abril Toons!",
        "Se voc\xc3\xaa vir " + Pluto + ", diga a ele " + Minnie + " que eu mandei um oi!",
        ]
    )

AFChipChatter = (
    [ # Greetings
    "Feliz Semana Abril Toons!",
    "Feliz Semana Abril Toons, %!",
    ],
    [ # Comments
    "Oi, eu sou o " + Dale + "!",
    "Como voc\xc3\xaa está, " + Chip + "?",
    "Eu sempre achei que voc\xc3\xaa era " + Dale + ", " + Chip + ".",
    "Tem certeza de que voc\xc3\xaa é o " + Chip + " e não o " + Dale + ", " + Chip + "?",
    "A Semana de Abril dos Toons é a mais boba do ano!",
    ],
    [ # Goodbyes
    "Tchau de " + Chip + " e " + Dale + "!",
    ]
)

# Warning Dale's chatter is dependent on on Chip's, they should match up
AFDaleChatter = (
    [ # Greetings
    "Feliz Semana Abril Toons!",
    "Feliz Semana Abril Toons, %!",
    ],
    [ # Comments
    "Oi, eu sou " + Chip + "!",
    "Muito bem " + Dale + "... obrigado!",
    "Não, eu sou o " + Chip + ", " + Dale + ".",
    "Sim, " + Dale + ", eu sou o " + Chip + ", e não o " + Dale + ".",
    "Certamente, " + Chip + "! Quero dizer, " + Dale + ".",
    ],
    [ # Goodbyes
    "Ou " + Dale + " e " + Chip + "!",
    ]
)

CLGoofySpeedwayChatter = (
        [ # Greetings
        "Bem-vindo ao "+lGoofySpeedway+".",
        "Oi, meu nome é "+Goofy+". Qual é o seu?",
        "Ohoh, que bom ver voc\xc3\xaa %!",
        "Olá! Perdoe minhas roupas sujas, estava consertando aquele Quadro de Pontuação quebrado.",
        ],
        [ # Comments
        "\xc3\x89 bom que o Quadro de Pontuação esteja funcionando logo, pois o Fim de Semana do Grande Pr\xc3\xaamio está chegando!",
        "Alguém quer comprar um kart meio usado? Ele já apareceu no Quadro de Pontuação!",
        "O Fim de Semana do Grande do Pr\xc3\xaamio está chegando, é melhor começar a treinar.",
        "O Fim de Semana do Grande Pr\xc3\xaamio será de sexta-feira, 22, a segunda-feira, 25 de maio!",
        "Preciso de uma escada para descer aquele kart.",
        "Aquele Toon realmente queria aparecer no Quadro de Pontuação!",
        "Cara, acabei de ver uma corrida terr\xc3\xadvel.",
        "Cuidado com as cascas de banana na pista!",
        "Voc\xc3\xaa fez algumas melhorias em seu kart ultimamente?",
        "Precisamos adquirir alguns aros novos na loja de kart.",
        "Ei, voc\xc3\xaa viu o "+Donald+"?",
        "Se vir o meu amigo "+Mickey+", mande lembranças a ele por mim.",
        "Puxa! Esqueci de preparar o café da manhã do "+Mickey+"!",
        "Ohoh, tem um monte de "+Cogs+" perto do "+lDonaldsDock+".",
        "Nos galhos do Brrrgh da minha Loja de Brincadeiras, os \xc3\x93culos Hipnotizantes estão \xc3\xa0 venda por apenas 1 balinha!",
        "A Loja de Piadas do Pateta tem as melhores piadas, truques e brincadeiras divertidas de toda Toontown!",
        "Na Loja de Piadas do Pateta, até uma torta na cara é garantia de boas risadas ou voc\xc3\xaa recebe suas balinhas de volta!"
        ],
        [ # Goodbyes
        "\xc3\x89 bom eu fazer uma nova pintura no meu kart antes do Fim de Semana do Grande Pr\xc3\xaamio.",
        "Caramba, é melhor eu dar um jeito nesse Quadro de Pontuação quebrado!",
        "Espero ver todos voc\xc3\xaas no Fim de Semana do Grande Pr\xc3\xaamio! Adeus!",
        "\xc3\x89 hora de dar uma cochilada. Vou para a Sonholândia sonhar com a vitória no Grande Pr\xc3\xaamio.",
        ]
    )


GPGoofySpeedwayChatter = (
        [ # Greetings
        "Bem-vindo ao "+lGoofySpeedway+".",
        "Bem-vindo ao Fim de Semana do Grande Pr\xc3\xaamio!",
        "Oi, meu nome é "+Goofy+". Qual é o seu?",
        "Ohoh, que bom ver voc\xc3\xaa %!",
        ],
        [ # Comments
        "Voc\xc3\xaa está na expectativa do Fim de Semana do Grande Pr\xc3\xaamio?",
        "A boa not\xc3\xadcia é que o Quadro de Pontuação está pronto.",
        "Conseguimos consertar o Quadro de Pontuação bem na hora do Fim de Semana do Grande Pr\xc3\xaamio!",
        "Nunca encontramos aquele Toon!",
        "Cara, acabei de ver uma corrida terr\xc3\xadvel.",
        "Cuidado com as cascas de banana na pista!",
        "Voc\xc3\xaa fez algumas melhorias em seu kart ultimamente?",
        "Precisamos comprar alguns aros novos na loja de kart.",
        "Ohoh, voc\xc3\xaa viu o "+Donald+"? Ele disse que estava vindo para o Grande Pr\xc3\xaamio!",
        "Se vir o meu amigo "+Mickey+", diga a ele que está perdendo uma corrida incr\xc3\xadvel!",
        "Puxa! Esqueci de preparar o café da manhã do "+Mickey+"!",
        "Ohoh, tem um monte de "+Cogs+" perto do "+lDonaldsDock+".",
        "Nos galhos do Brrrgh da minha Loja de Brincadeiras, os \xc3\x93culos Hipnotizantes estão \xc3\xa0 venda por apenas 1 balinha!",
        "A Loja de Piadas do Pateta tem as melhores piadas, truques e brincadeiras divertidas de toda Toontown!",
        "Na Loja de Piadas do Pateta, até uma torta na cara é garantia de boas risadas ou voc\xc3\xaa recebe suas balinhas de volta!"
        ],
        [ # Goodbyes
        "Boa sorte no Grande Pr\xc3\xaamio!",
        "Vou participar da próxima corrida do Grande Pr\xc3\xaamio!",
        "Ohoh, acho que a próxima corrida já vai começar!",
        "Puxa, é melhor verificar o novo Quadro de Pontuação e garantir que esteja funcionando bem!",
        ]
    )

SillyPhase1Chatter = [
        "Se não viu o Medidor de Bobagens, vá para o Salão de Desenhos!",
        "Toontown fica bobinha durante o dia!",
        "Porque as ondas de bobagem na batalha aumentam o n\xc3\xadvel de bobagem de Toontown!",
        "Os objetos da rua estão começando a ganhar vida!",
        "Eu vi um hidrante se movendo na Rua da Bobagem!",
    ]

SillyPhase2Chatter = [
        "O N\xc3\xadvel de Bobagem continua subindo!",
        "O Medidor de Bobagens subiu demais e pirou!",
        "Alguém viu uma lixeira se movendo na Rua do Bordo!",
        "Muitos hidrantes na Rua da Bobagem ganharam vida!",
        "Uma caixa de correio na Travessa do Farol endoidou!",
        "Vá ver o Medidor de Bobagens no Salão de Desenhos!",
        "Continue causando aquelas ondas de bobagem!",
    ]

SillyPhase3Chatter = [
        "Os Cogs odiaram o fato de Toontown ter se tornado tão boba!",
        "Fique de olhos abertos para Invasões de Cogs!",
        "As Invasões de Cogs baixaram o n\xc3\xadvel de bobagem!",
        "O Medidor de Bobagens caiu após as Invasões de Cogs!",
        "Agora todas as ruas de Toontown t\xc3\xaam objetos animados!",
        "Toontown está mais bobinha do que nunca!",
    ]

SillyPhase4Chatter = [
        "Os hidrantes tornam seus Itens de Esguicho mais eficazes!",
        "As caixas de correio fornecem um aperfeiçoamento especial aos seus Itens de Arremesso!",
        "Aquelas Lixeiras doidas podem dar a voc\xc3\xaa um Toonar!",
        "Os objetos da rua podem lhe ajudar na batalha!",
        "Eu sei que vamos recuperar o Medidor de Bobagens logo!",
        "Aproveite a Toontown bobinha!",
    ]

for chatter in [MickeyChatter,DonaldChatter,MinnieChatter,GoofyChatter,DaisyChatter]:
    chatter[0].extend(SharedChatterGreetings)
    chatter[1].extend(SharedChatterComments)
    chatter[2].extend(SharedChatterGoodbyes)

# Toontown dialogues
BoringTopic = "Boring"
EmceeDialoguePhase1Topic = "EmceeDialoguePhase1"
EmceeDialoguePhase2Topic = "EmceeDialoguePhase2"
EmceeDialoguePhase3Topic = "EmceeDialoguePhase3"
EmceeDialoguePhase3_5Topic = "EmceeDialoguePhase3.5"
EmceeDialoguePhase4Topic = "EmceeDialoguePhase4"
EmceeDialoguePhase5Topic = "EmceeDialoguePhase5"
EmceeDialoguePhase6Topic = "EmceeDialoguePhase6"

AprilToonsPhasePreTopTopic = "AprilToonsPhasePreTopTopic"
AprilToonsPhaseTopTopic = "AprilToonsPhaseTopTopic"
AprilToonsExtPhaseTopTopic = "AprilToonsExtPhaseTopTopic"
AprilToonsPhasePostTopTopic = "AprilToonsPhasePostTopTopic"
toontownDialogues = {
   BoringTopic : { \
        (1, 2018)  : ['Olá Albert', 'Parece que o n\xc3\xadvel de bobagem está subindo', ' Sim, e se não esqueça dos April Toons!'],
        (2, 2019) : ['Olá Newton', 'Gostaria de saber o quanto os grupos contribu\xc3\xadram para isso ',],
        (3, 2020) : ['Para que cumprimentar Albert e Newton', 'O Halloween foi bem bobinho também!',],
        },
    AprilToonsPhasePreTopTopic : {
        (1, 2020) : ["Gadzooks! The Silly Meter has come back to life!",
                          "It\'s rising every day, and will reach the top soon!",
                          "When it does, something silly is sure to happen!",
                          "So get ready to get ridiculous!", ],
        },
    AprilToonsPhaseTopTopic : {
        (1, 2020) : ["The Silly Meter has hit the top!",
                          "Doodles are talking, Estates are bouncy!",
                          "There\'s only one thing to say...",
                          "HAPPY APRIL TOONS!", ],
        },
    AprilToonsExtPhaseTopTopic : {
        (1, 2020) : ["The Silly Meter has hit the top!",
                          "Doodles are talking, Estates are bouncy!", ],
        },
    AprilToonsPhasePostTopTopic : {
        (1, 2020) : ["April Toons is over!",
                          "It's time for us to return to our lab.",
                          "But when things get REALLY crazy again...",
                          "The Silly Meter will return!", ],
        },
    EmceeDialoguePhase1Topic : {
        (1, 2020) : [ 'Amigos Toons, este é o Medidor de Bobagens!',
                          'Ele registra a variação do n\xc3\xadvel de bobagem de Toontown...',
                          'Que está causando a animação dos objetos da rua!',
                          'E VOC\xc3\x8a pode ajudar a aumentar esses n\xc3\xadveis!',
                          'Lute com os Cogs para causar Ondas de Bobagem...',
                          'Deixe Toontown mais bobinha do que nunca...',
                          'E vamos observar o mundo ganhando vida!',
                          'Agora vou repetir o que disse, só mais uma vez.', ],
        },
    EmceeDialoguePhase2Topic : {
        (1, 2020) : ['Bom trabalho, Toons!',
                         'Voc\xc3\xaas mantiveram aqueles n\xc3\xadveis em alta...',
                         'E Toontown fica mais bobinha a cada dia que passa!',
                         'Hidrantes, lixeiras e caixas de correio estão adquirindo vida...',
                         'Deixando o mundo mais animado do que nunca!',
                         'Voc\xc3\xaa sabe que os Cogs não ficam felizes com isso...',
                         'Mas com certeza os Toons estão!', ],
        },
    EmceeDialoguePhase3Topic : {
        (1, 2020) : ['Caramba! O Medidor de Bobagens está ainda mais doido do que se esperava!',
                         'Suas Ondas de Bobagem estão fazendo maravilhas...',
                         'E Toontown fica mais animada a cada dia que passa!',
                         'Continue fazendo um bom trabalho...',
                         'E vejamos o quão bobinha Toontown pode ficar!',
                         'Voc\xc3\xaa sabe que os Cogs não estão felizes com o que está acontecendo...',
                         'Mas com certeza os Toons estão!', ],
        },
    EmceeDialoguePhase3_5Topic : {
        (1, 2020) : ['VOC\xc3\x8aS CONSEGUIRAM, TOONS!',
                         'Toontown está cheia de vida!',
                         'As ruas estão repletas de bobagens!',
                         'Vá ver por si mesmo!', ],
                         #'You deserve a reward!', # Probably would require a translation for code redemption
                         #'Enter the code SILLYMETER in your Shticker Book...',
                         #'...to get a Silly Meter T-Shirt!', ],
        },
    EmceeDialoguePhase4Topic : {
        (1, 2020) : ['Atenção Toons!',
                         'As súbitas invasões de Cogs foram lastimáveis.',
                         'Como resultado, o n\xc3\xadvel de bobagem caiu drasticamente...',
                         'E mais nenhum novo objeto ganhou vida.',
                         'Mas os que ganharam estão muito agradecidos... ',
                         'Então, talvez eles achem um jeito de mostrar sua gratidão!',
                         'Fiquem Antenados!', ],
        },
    EmceeDialoguePhase5Topic : {
        (1, 2020) : ['Atenção Toons!',
                         'As invasões de Cogs foram lastimáveis.',
                         'Como resultado, o n\xc3\xadvel de bobagem caiu drasticamente...',
                         'E mais nenhum novo objeto ganhou vida.',
                         'Mas os que ganharam estão muito agradecidos... ',
                         'E estão demonstrando sua gratidão ajudando na batalha!',
                         'Já podemos repelir os Cogs, portanto, continuem lutando!', ],
        },
    EmceeDialoguePhase6Topic : {
        (1, 2020) : ['Parabéns Toons!',
                         'Voc\xc3\xaas eliminaram com sucesso as Invasões de Cogs...',
                         'Com uma ajudinha de nossos novos amigos animados...',
                         'E deixaram novamente Toontown tão bobinha como sempre!',
                         'Esperamos que o Medidor de Bobagens volte a subir em breve...',
                         'Enquanto isso, continuem enfrentando os Cogs...',
                         'E aproveitem o lugar mais bobinho de todos, Toontown!',],
        },
    }

# FriendsListPanel.py
FriendsListPanelNewFriend = "Novo amigo"
FriendsListPanelSecrets = "Segredos"
FriendsListPanelOnlineFriends = "AMIGOS\nON-LINE"
FriendsListPanelAllFriends = "TODOS\nOS AMIGOS"
FriendsListPanelIgnoredFriends = "TOONS\nIGNORADOS"
FriendsListPanelPets = "BICHINHOS\nPR\xc3\x93XIMOS"
FriendsListPanelPlayers = "TODOS OS AMIGOS\nDO JOGADOR"
FriendsListPanelOnlinePlayers = "AMIGOS ONLINE\nDO JOGADOR"

FriendInviterClickToon = "Clique no Toon com o qual voc\xc3\xaa quer fazer amizade.\n\n(Voc\xc3\xaa tem %s amigos)"

# Support DISL account friends
FriendInviterToon = "Toon"
FriendInviterThatToon = "Aquele Toon"
FriendInviterPlayer = "Jogador"
FriendInviterThatPlayer = "Aquele jogador"
FriendInviterBegin = "Que tipo de amigo voc\xc3\xaa quer ter?"
FriendInviterToonFriendInfo = "Um amigo somente em Toontown"
FriendInviterPlayerFriendInfo = "Um amigo em toda a rede Disney.com"
FriendInviterToonTooMany = "Voc\xc3\xaa tem amigos Toons demais para poder acrescentar um agora. Voc\xc3\xaa terá de remover alguns amigos Toons se quiser fazer amizade com %s. Voc\xc3\xaa também pode tentar fazer amizade com seu jogador."
FriendInviterPlayerTooMany = "Voc\xc3\xaa tem amigos jogadores demais para poder acrescentar um agora. Voc\xc3\xaa terá de remover alguns amigos jogadores se quiser fazer amizade com %s. Voc\xc3\xaa também pode tentar fazer amizade com seu Toon."
FriendInviterToonAlready = "%s já é seu amigo Toon."
FriendInviterPlayerAlready = "%s já é seu amigo jogador."
FriendInviterStopBeingToonFriends = "Romper amizade Toon"
FriendInviterStopBeingPlayerFriends = "Romper amizade de jogador"
FriendInviterEndFriendshipToon = "Tem certeza de que quer romper a amizade de Toon com %s?"
FriendInviterEndFriendshipPlayer = "Tem certeza de que quer romper a amizade de jogador com %s?"
FriendInviterRemainToon = "\n(Voc\xc3\xaa vai continuar sendo amigo Toon de %s)"
FriendInviterRemainPlayer = "\n(Voc\xc3\xaa vai continuar sendo amigo jogador de %s)"

# DownloadForceAcknowledge.py
DownloadForceAcknowledgeVerbList = [
    "pintado",
    "desembalar",
    "desdobrado",
    "esticado",
    "inflado",
    "montar",
]

# DownloadForceAcknowledge.py
# phase, percent
DownloadForceAcknowledgeMsg = "Sinto muito, voc\xc3\xaa não pode avançar porque o download de %(phase)s está apenas %(percent)s%% conclu\xc3\xaddo.\n\nTente novamente mais tarde."

# TeaserPanel.py
TeaserTop = "" # "Infelizmente não é poss\xc3\xadvel fazer isto na versão de avaliação gratuita..."
TeaserBottom = "" # "Assine já e aproveite esses recursos incr\xc3\xadveis:"
TeaserDefault = "\nVoc\xc3\xaa precisa ser um associado.\nUna-se!"
TeaserOtherHoods = "Visite os 6 bairros exclusivos!"
TeaserTypeAName = "Digite o seu nome favorito para o seu Toon!"
TeaserSixToons = "Crie até 6 Toons em uma só conta!"
TeaserClothing = "Compre roupas exclusivas para personalizar o seu Toon!"
TeaserCogHQ = "Infiltre-se nas\nperigosas áreas avançadas dos Cogs!"
TeaserSecretChat = "Troque segredos\ncom seus amigos conversando on-line com eles!"
TeaserSpecies = "Crie e jogue com Toons Macacos, Cavalos e Ursos!"
TeaserFishing = "Colecione todas as espécies de peixes!"
TeaserGolf = "Jogue em campos de golfe malucos!"
TeaserParties = "Para planear Partes"
TeaserSubscribe = "Assinar"
TeaserContinue = "Continuar na versão gratuita"
TeaserEmotions = "Para fazer seu Toon mais expressivo"
TeaserKarting = "Aposte corridas com outros Toons em karts maneiros!"
TeaserKartingAccessories = "Personalize seu kart com acessórios incr\xc3\xadveis."
TeaserGardening = "Plante flores, construa estátuas e cultive árvores em seu terreno."
TeaserHaveFun = "Encontre mais diversão!"
TeaserJoinUs = "Una-se!"

TeaserPlantGags = "To plant these gags"
TeaserPickGags = "To pick these gags"
TeaserRestockGags = "To restock these gags"
TeaserGetGags = "To get these gags"
TeaserUseGags = "To use these gags"
#TeaserCardsAndPosters = ""Receba um pacote de boas-vindas e boletins mensais\ncom pôsteres e outras coisas maneiras!""
#TeaserFurniture = "Compre e arrume os móveis da sua própria casa!"
TeaserMinigames = TeaserOtherHoods # "Brinque com os 8 tipos de minijogos!"
#TeaserHolidays = "Participe dos eventos especiais e de datas comemorativas incr\xc3\xadveis!"
TeaserQuests = TeaserOtherHoods # "Complete centenas de Tarefas Toon para salvar Toontown!"
TeaserOtherGags = TeaserOtherHoods # "Passe por 6 n\xc3\xadveis em 6 tipos de piadas diferentes!"
#TeaserRental = "Alugue \xc3\xadtens de festa para seu terreno!"
#TeaserBigger = "Compre \xc3\xadtens Toon maiores e melhores!"
TeaserTricks = TeaserOtherHoods # "Treine seus Rabisocs para que eles façam truques e ajudem na batalha!"

# Launcher.py
LauncherPhaseNames = {
    0   : "Inicialização",
    1   : "Panda",
    2   : "Motor",
    3   : "Fazer um Toon",
    3.5 : "Toontorial",
    4   : "Parque",
    5   : "Ruas",
    5.5 : "Estados",
    6   : "Bairros I",
    7   : Cog + " Edif\xc3\xadcios dos",
    8   : "Bairros II",
    9   : Sellbot + " Quartel dos",
    10  : Cashbot + " Quartel dos",
    11  : Lawbot + " Quartel dos",
    12  : Bossbot + " Quartel dos",
    13  : "Festas",
    }

# Lets make these messages a little more friendly
LauncherProgress = "%(name)s (%(current)s de %(total)s)"
LauncherStartingMessage = "Iniciando Toontown On-line da Disney..."
LauncherDownloadFile = "Fazendo download da atualização de "+ LauncherProgress +"..."
LauncherDownloadFileBytes = "Fazendo download da atualização de "+ LauncherProgress +": %(bytes)s"
LauncherDownloadFilePercent = "Fazendo download da atualização de "+ LauncherProgress +": %(percent)s%%"
LauncherDecompressingFile = "Descompactando atualização de "+ LauncherProgress +"..."
LauncherDecompressingPercent = "Descompactando atualização de "+ LauncherProgress +": %(percent)s%%"
LauncherExtractingFile = "Extraindo atualização de "+ LauncherProgress +"..."
LauncherExtractingPercent = "Extraindo atualização de "+ LauncherProgress +": %(percent)s%%"
LauncherPatchingFile = "Aplicando atualização de "+ LauncherProgress +"..."
LauncherPatchingPercent = "Aplicando atualização de "+ LauncherProgress +": %(percent)s%%"
LauncherConnectProxyAttempt = "Conectando-se a Toontown: %s (proxy: %s) tentativa: %s"
LauncherConnectAttempt = "Conectando-se a Toontown: %s tentativa %s"
LauncherDownloadServerFileList = "Atualizando Toontown..."
LauncherCreatingDownloadDb = "Atualizando Toontown..."
LauncherDownloadClientFileList = "Atualizando Toontown..."
LauncherStartingToontown = "Iniciando Toontown..."
LauncherStartingGame = "Iniciando Toontown..."
LauncherRecoverFiles = "Atualizando Toontown. Recuperando arquivos..."
LauncherCheckUpdates = "Verificando atualizações de "+ LauncherProgress
LauncherVerifyPhase = "Atualizando Toontown..."

# change Downloading Toontorial to Loading Toontorial
LoadingDownloadWatcherUpdate = "Loading %s"

# AvatarChoice.py
AvatarChoiceMakeAToon = "Fazer um\nToon"
AvatarChoicePlayThisToon = "Jogar com\neste Toon"
AvatarChoiceSubscribersOnly = "Assinar\n\n\n\nAgora!"
AvatarChoiceDelete = "Excluir"
AvatarChoiceDeleteConfirm = "Isto fará que %s seja exclu\xc3\xaddo para sempre."
AvatarChoiceNameRejected = "Nome\nrejeitado"
AvatarChoiceNameApproved = "Nome\naprovado!"
AvatarChoiceNameReview = "Em\nrevisão"
AvatarChoiceNameYourToon = "Dar um\nnome ao Toon!"
AvatarChoiceDeletePasswordText = "Cuidado! Isto fará que %s seja exclu\xc3\xaddo para sempre. Para excluir este Toon, insira a sua senha."
AvatarChoiceDeleteConfirmText = "Cuidado! Isto excluirá %(name)s para sempre. Se voc\xc3\xaa tiver certeza de que é isso mesmo que deseja, digite \"%(confirm)s\" e clique em OK."
AvatarChoiceDeleteConfirmUserTypes = "excluir"
AvatarChoiceDeletePasswordTitle = "Excluir Toon?"
AvatarChoicePassword = "Senha"
AvatarChoiceDeletePasswordOK = lOK
AvatarChoiceDeletePasswordCancel = lCancel
AvatarChoiceDeleteWrongPassword = "Esta senha não parece ser a correta. Para excluir este Toon, insira a sua senha."
AvatarChoiceDeleteWrongConfirm = "Voc\xc3\xaa não digitou corretamente. Para excluir %(name)s, digite \"%(confirm)s\" e clique em OK. Não digite as aspas. Clique em Cancelar se desistir."

# AvatarChooser.py
AvatarChooserPickAToon = "Escolha um Toon para jogar"
AvatarChooserQuit = lQuit

# DateOfBirthEntry.py
DateOfBirthEntryMonths = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
                          'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez',]
DateOfBirthEntryDefaultLabel = "Data de nascimento"


# AchievePage.py
AchievePageTitle = "Realizações\n(em breve)"

# PhotoPage.py
PhotoPageTitle = "Foto\n(em breve)" # "\xc3\x81lbum de foto"
PhotoPageCaption = "Legenda"
PhotoPageDelete = "Excluir"
PhotoPagePrint = "Imprimir"
PhotoPageCaptionPhoto = "Foto da legenda"
PhotoPageCancel = lCancel
PhotoPageDeletePhoto = "Excluir foto?"
PhotoPageOK = lOK
PhotoPageDeletePhotoWithName = "Excluir foto?\n%s"
PhotoPageNoName = "Sem nome"
PhotoPageUnknownName = "Desconhecido"

# BuildingPage.py
BuildingPageTitle = "Edif\xc3\xadcios\n(em breve)"

# InventoryPage.py
InventoryPageTitle = "Piadas"
InventoryPageDeleteTitle = "EXCLUIR PIADAS"
InventoryPageTrackFull = "Voc\xc3\xaa possui todas as piadas do tipo %s."
InventoryPagePluralPoints = "Voc\xc3\xaa obterá uma nova piada de\n%(trackName)s quando\nganhar mais %(numPoints)s pontos de %(trackName)s."
InventoryPageSinglePoint = "Voc\xc3\xaa obterá uma nova piada de\n%(trackName)s quando\nganhar mais %(numPoints)s pontos de %(trackName)s."
InventoryPageNoAccess = "Voc\xc3\xaa ainda não tem acesso ao tipo %s."

# NPCFriendPage.py
NPCFriendPageTitle = "SOS Toons"

# EventsPage.py
PartyDateFormat = "%(mm)s %(dd)d, %(yyyy).4d" # Dec 8, 2008
PartyTimeFormat = "%d:%.2d %s" # 1:45 pm
PartyTimeFormatMeridiemAM = "am"
PartyTimeFormatMeridiemPM = "pm"
PartyCanStart = "\xc3\x89 Hora de Festejar! Clique em Start Party (Iniciar Festa) na sua página \xc3\x81lbum Toon Hosting (Hospedando do Livro de Brincadeiras)!"
PartyHasStartedAcceptedInvite = '%s, a festa começou! Clique no anfitrião e em "Ir \xc3\xa0 Festa" na página \xc3\x81lbum Toon Invites (Convites do Livro de Brincadeiras).'
PartyHasStartedNotAcceptedInvite = '%s, a festa começou! Voc\xc3\xaa também pode ir, teletransportando-se para o anfitrião.'

EventsPageName = "Eventos"
EventsPageCalendarTabName = "Calendário"
EventsPageCalendarTabParty = "Festa"
EventsPageToontownTimeIs = "A HORA DE TOONTOWN \xc3\x89"
EventsPageConfirmCancel = "Se cancelar, receberá uma devolução de %d%%. Tem certeza de que quer cancelar sua festa?"
EventsPageCancelPartyResultOk = "Sua festa foi cancelada e voc\xc3\xaa recebeu %d balinhas de volta!"
EventsPageCancelPartyResultError = "Desculpe, sua festa não foi cancelada."
EventsPageCancelPartyAlreadyRefunded = "Your party was never started. Check your mailbox for your refund!"
EventsPageTooLateToStart = "Desculpe, tarde demais para começar a sua festa. Voc\xc3\xaa pode cancelá-la e planejar outra."
EventsPagePublicPrivateChange = "Alterando a sua configuração de privacidade de festa..."
EventsPagePublicPrivateNoGo = "Desculpe, voc\xc3\xaa não pode alterar a sua configuração de privacidade de festa agora."
EventsPagePublicPrivateAlreadyStarted = "Desculpe, a sua festa já começou, e voc\xc3\xaa não pode alterar sua configuração de privacidade de festa."
EventsPageHostTabName = "Hospedando" # displayed on the physical tab
EventsPageHostTabTitle = "Minha Próxima Festa" # banner text displayed across the top
EventsPageHostTabTitleNoParties = "Sem Festas"
EventsPageHostTabDateTimeLabel = "Voc\xc3\xaa tem uma festa em %s \xc3\xa0s %s, Hora de Toontown."
EventsPageHostingTabNoParty = "Vá ao Portão de Festa\nde um pátio para planejar\nsua festa!"
EventsPageHostTabPublicPrivateLabel = "Esta festa é:"
EventsPageHostTabToggleToPrivate = "Particular"
EventsPageHostTabToggleToPublic = "Pública"
EventsPageHostingTabGuestListTitle = "Convidados"
EventsPageHostingTabActivityListTitle = "Atividades"
EventsPageHostingTabDecorationsListTitle = "Decorações"
EventsPageHostingTabPartiesListTitle = "Anfitriões"
EventsPageHostTabCancelButton = "Cancelar Festa"
EventsPageGoButton = "Iniciar\nFesta!"
EventsPageGoBackButton = "Festa\nJá!"
EventsPageInviteGoButton = "Ir para\nFesta!"
EventsPageUnknownToon = "Toon Desconhecido"

EventsPageInvitedTabName = "Convites"
EventsPageInvitedTabTitle = "Convites de Festa"
EventsPageInvitedTabInvitationListTitle = "Convites"
EventsPageInvitedTabActivityListTitle = "Atividades"
EventsPageInvitedTabTime = "%s %s Hora de Toontown"

EventsPageNewsTabName = "Not\xc3\xadcias"
EventsPageNewsTabTitle = "Not\xc3\xadcias"
EventsPageNewsDownloading= "Recuperando Not\xc3\xadcias..."
EventsPageNewsUnavailable = "Tico e Teco brincando com a impressora da gráfica. Not\xc3\xadcias não dispon\xc3\xadveis."
EventsPageNewsPaperTitle = "TOONTOWN TIMES (GAZETA DE TOONTOWN)"
EventsPageNewsLeftSubtitle = "Ainda só por 1 balinha"
EventsPageNewsRightSubtitle = "Tiragem de nove mil toonplares"

# NewsPage.py
NewsPageName = "Not\xc3\xadcias"
NewsPageImportError = 'Não foi poss\xc3\xadvel abrir as not\xc3\xadcias sobre jogos.'

NewsPageDownloadingNewsSubstr = 'Please come back later. Downloading news'
NewsPageDownloadingNews0 = NewsPageDownloadingNewsSubstr + " %s%%."
NewsPageDownloadingNews1 = NewsPageDownloadingNewsSubstr + " %s%%.."
NewsPageDownloadingNews2 = NewsPageDownloadingNewsSubstr + " %s%%..."
NewsPageErrorDownloadingFile = 'Oops, there was a problem downloading\n%s.'
NewsPageErrorDownloadingFileCanStillRead = 'Oops, there was a problem downloading\n%s.\nYou can still read the other pages.'
NewsPageNoIssues = 'Could not find any issues in %s.'

# DirectNewsFrame.py
IssueFrameThisWeek = "this week"
IssueFrameLastWeek = "last week"
IssueFrameWeeksAgo = "%d weeks ago"

# InvitationSelection.py
SelectedInvitationInformation = "%s tem uma festa em %s \xc3\xa0s %s, Hora de Toontown."

# PartyPlanner.py
PartyPlannerNextButton = "Continuar"
PartyPlannerPreviousButton = "Voltar"
PartyPlannerWelcomeTitle = "Planejador de Festas de Toontown"
PartyPlannerInstructions = "Hospedar sua festa é muito divertido!\nComece a planejar com as setas na parte inferior!"
PartyPlannerDateTitle = "Escolha o Dia de Sua Festa"
PartyPlannerTimeTitle = "Escolha a Hora de Sua Festa"
PartyPlannerGuestTitle = "Selecione os Convidados"
PartyPlannerEditorTitle = "Crie Sua Festa\nInsira as Atividades e Decorações"
PartyPlannerConfirmTitle = "Escolha os Convites para Enviar"
PartyPlannerConfirmTitleNoFriends = "Reveja os Detalhes de Sua Festa"
PartyPlannerTimeToontown = "Toontown"
PartyPlannerTimeTime = "Hora"
PartyPlannerTimeRecap = "Dia e Hora da Festa"
PartyPlannerPartyNow = "O Mais Breve Poss\xc3\xadvel"
PartyPlannerTimeToontownTime = "Hora de Toontown:"
PartyPlannerTimeLocalTime = "Hora Local da Festa: "
PartyPlannerPublicPrivateLabel = "A festa será:"
PartyPlannerPublicDescription = "Todos os Toons\npodem vir!"
PartyPlannerPrivateDescription = "Apenas\nToons Convidados\npodem vir!"
PartyPlannerPublic = "Pública"
PartyPlannerPrivate = "Particular"
PartyPlannerCheckAll = "Selecionar\nTudo"
PartyPlannerUncheckAll = "Desmarcar\nTudo"
PartyPlannerDateText = "Data"
PartyPlannerTimeText = "Hora"
PartyPlannerTTTimeText = "Hora de Toontown"
PartyPlannerEditorInstructionsIdle = "Clique na Atividade ou Decoração de Festa que deseja adquirir."
PartyPlannerEditorInstructionsClickedElementActivity = "Clique em Comprar ou Arraste o Ícone da Atividade para o Mapa da Festa"
PartyPlannerEditorInstructionsClickedElementDecoration = "Clique em Comprar ou Arraste o Ícone da Decoração para o Mapa da Festa"
PartyPlannerEditorInstructionsDraggingActivity = "Arraste a Atividade para o Mapa da Festa."
PartyPlannerEditorInstructionsDraggingDecoration = "Arraste a Decoração para o Mapa da Festa."
PartyPlannerEditorInstructionsPartyGrounds = "Clique e Arraste os itens para mov\xc3\xaa-los pelo Mapa da Festa"
PartyPlannerEditorInstructionsTrash = "Arraste uma Atividade ou Decoração até aqui para remov\xc3\xaa-la."
PartyPlannerEditorInstructionsNoRoom = "Não há lugar para colocar essa atividade."
PartyPlannerEditorInstructionsRemoved = "%(removed)s removidos(as) desde que %(added)s foram adicionados(as)."
PartyPlannerBeans = "feijões"
PartyPlannerTotalCost = "Custo Total:\n%d feijões"
PartyPlannerSoldOut = "ESGOTADO"
PartyPlannerBuy = "COMPRAR"
PartyPlannerPaidOnly = "S\xc3\x93 ASSOCIADOS"
PartyPlannerPartyGrounds = "MAPA DA FESTA"
PartyPlannerOkWithGroundsLayout = "Voc\xc3\xaa já terminou de mover suas Atividades e Decorações pelo Mapa da Festa?"
PartyPlannerChooseFutureTime = "Por favor, selecione uma hora futura."
PartyPlannerInviteButton = "Enviar Convites"
PartyPlannerInviteButtonNoFriends = "Planejar Festa"
PartyPlannerBirthdayTheme = "Aniversário"
PartyPlannerGenericMaleTheme = "Estrelas"
PartyPlannerGenericFemaleTheme = "Flores"
PartyPlannerRacingTheme = "Corrida"
PartyPlannerValentoonsTheme = "Dia dos namorados"
PartyPlannerVictoryPartyTheme = "Vitória"
PartyPlannerWinterPartyTheme = "Inverno"
PartyPlannerGuestName = "Nome do Convidado"
PartyPlannerClosePlanner = "Fechar Planejador"
PartyPlannerConfirmationAllOkTitle = "Parabéns!"
PartyPlannerConfirmationAllOkText = "Sua festa foi criada e os convites enviados.\nObrigado!"
PartyPlannerConfirmationAllOkTextNoFriends = "Sua festa foi criada!\nObrigado!"
PartyPlannerConfirmationErrorTitle = "Opa."
PartyPlannerConfirmationValidationErrorText = "Desculpe, ocorreu um problema\ncom essa festa.\nPor favor, volte e tente novamente."
PartyPlannerConfirmationDatabaseErrorText = "Desculpe, não foi poss\xc3\xadvel registrar todas as informações.\nPor favor, tente novamente mais tarde.\nNão se preocupe, nenhum feijão foi perdido."
PartyPlannerConfirmationTooManyText = "Desculpe, voc\xc3\xaa já está dando uma festa.\nSe quiser planejar outra, por favor,\ncancele a atual."
PartyPlannerInvitationThemeWhatSentence = "Voc\xc3\xaa está convidado(a) para minha festa de %s! %s!"
PartyPlannerInvitationThemeWhatSentenceNoFriends = "Estou dando uma festa de %s! %s!"
PartyPlannerInvitationThemeWhatActivitiesBeginning = "Terá "
PartyPlannerInvitationWhoseSentence = "Festa de %s"
PartyPlannerInvitationTheme = "Tema"
PartyPlannerInvitationWhenSentence = "Será em %s,\n\xc3\xa0s %s, Hora de Toontown.\nEspero que voc\xc3\xaa apareça!"
PartyPlannerInvitationWhenSentenceNoFriends = "Será em %s,\n\xc3\xa0s %s, Hora de Toontown.\nToontástico!"
PartyPlannerComingSoon = "Em Breve"
PartyPlannerCantBuy= "Não Pode Comprar"
PartyPlannerGenericName = "Planejador de Festa"

# DistributedPartyJukeboxActivity.py
PartyJukeboxOccupied = "Alguém está usando a jukebox. Tente novamente mais tarde."
PartyJukeboxNowPlaying = "A música que voc\xc3\xaa escolheu já está tocando na jukebox!"

# Jukebox Music
MusicEncntrGeneralBg = "Encontro Com Cogs"
MusicTcSzActivity = "Mistureba de Toontorial"
MusicTcSz = "Passeando Juntos"
MusicCreateAToon = "Novo Toon na Cidade"
MusicTtTheme = "O Tema de Toontown"
MusicMinigameRace = "Devagar e Firme"
MusicMgPairing = "Voc\xc3\xaa se lembra de Mim?"
MusicTcNbrhood = "Centro de Toontown"
MusicMgDiving = "Cantiga do Tesouro"
MusicMgCannonGame = "Disparar os Canhões!"
MusicMgTwodgame = "Toon Cont\xc3\xadnuo"
MusicMgCogthief = "Pegue Aquele Cog!"
MusicMgTravel = "Música para Viagem"
MusicMgTugOWar = "Cabo de Guerra"
MusicMgVine = "O Balanço da Selva"
MusicMgIcegame = "Situação Delicada"
MusicMgToontag = "Mistureba de Minijogo"
MusicMMatchBg2 = "Jazz da Minnie"
MusicMgTarget = "Sobrevoando Toontown"
MusicFfSafezone = "A Fazenda Divertida"
MusicDdSz = "O Caminho Tortuoso"
MusicMmNbrhood = "Melodilândia da Minnie"
MusicGzPlaygolf = "Vamos Jogar Golfe!"
MusicGsSz = "Autódromo do Pateta"
MusicOzSz = "Terras do Tico e Teco"
MusicGsRaceCc = "Dirigindo no Centro"
MusicGsRaceSs = "Preparar, Acionar, Vai!"
MusicGsRaceRr = "Rota 66"
MusicGzSz = "A Polca Puf-Puf"
MusicMmSz = "Dançando nas Ruas"
MusicMmSzActivity = "A\xc3\xad Vem o Soprano"
MusicDdNbrhood = "O Porto do Donald"
MusicGsKartshop = "Sr. Pateta Mãos \xc3\xa0 Obra"
MusicDdSzActivity = "Cabana da Praia"
MusicEncntrGeneralBgIndoor = "Botando pra Quebrar"
MusicTtElevator = "Subindo?"
MusicEncntrToonWinningIndoor = "Toons Unidos!"
MusicEncntrGeneralSuitWinningIndoor = "Cogtástrofe!"
MusicTbNbrhood = "O Brrrgh"
MusicDlNbrhood = "Sonholândia do Donald"
MusicDlSzActivity = "Contando Ovelhas"
MusicDgSz = "Valsa das Flores"
MusicDlSz = "Sonâmbulo"
MusicTbSzActivity = "Nevasca"
MusicTbSz = "Tremendo e Vibrando"
MusicDgNbrhood = "Jardim da Margarida"
MusicEncntrHallOfFame = "A Galeria da Fama"
MusicEncntrSuitHqNbrhood = "Reais e Centavos"
MusicChqFactBg = "Fábrica de Cogs"
MusicCoghqFinale = "Triunfo dos Toons"
MusicEncntrToonWinning = "Pagando \xc3\xa0 Vista!"
MusicEncntrSuitWinning = "Vendendo Seu Short"
MusicEncntrHeadSuitTheme = "O Chefão"
MusicLbJurybg = "O Julgamento Começou"
MusicLbCourtyard = "Balançando"
MusicBossbotCeoV2 = "O Gerente"
MusicBossbotFactoryV1 = "Valsa do Cog"
MusicBossbotCeoV1 = "Rodeado de Chefes"
MusicPartyOriginalTheme = "Hora da Festa"
MusicPartyPolkaDance = "Polca de Festa"
MusicPartySwingDance = "Balanço de Festa"
MusicPartyWaltzDance = "Valsa de Festa"
MusicPartyGenericThemeJazzy = "Jazz de Festa"
MusicPartyGenericTheme = "Jingle de Festa"


# JukeBoxGui
JukeboxAddSong = "Adicionar\nMúsica"
JukeboxReplaceSong = "Trocar\nMúsica"
JukeboxQueueLabel = "Tocar a Seguir:"
JukeboxSongsLabel = "Selecionar Música:"
JukeboxClose = "Pronto"
JukeboxCurrentlyPlaying = "Tocando Agora"
JukeboxCurrentlyPlayingNothing = "Jukebox em pausa."
JukeboxCurrentSongNothing = "Adicionar uma música \xc3\xa0 lista!"

PartyOverWarningNoName = "A festa acabou! Obrigado por ter vindo!"
PartyOverWarningWithName = "A festa %s de acabou! Obrigado por ter vindo!"
PartyCountdownClockText = "Tempo\n\nRestante"
PartyTitleText = "Festa de %s" # what you see when you enter a party

PartyActivityConjunction = ", e "
# Note : This dictionary is used to show the names of the activities in various
#        contexts.  If PartyGlobals.ActivityIds is changed, this list must be
#        updated with new indices.
PartyActivityNameDict = {
    0 : {
        "generic" : "Jukebox\n20 músicas",
        "invite" : "uma Jukebox de 20 músicas",
        "editor" : "Jukebox de 20",
        "description" : "Ouça música com sua própria jukebox de 20 músicas!"
    },
    1 : {
        "generic" : "Canhões de Festa",
        "invite" : "Canhões de Festa",
        "editor" : "Canhões",
        "description" : "Dispare voc\xc3\xaa mesmo os canhões e divirta-se!"
    },
    2 : {
        "generic" : "Trampolim",
        "invite" : "Trampolim",
        "editor" : "Trampolim",
        "description" : "Pegue balinhas e salte o mais alto poss\xc3\xadvel!"
    },
    3 : {
        "generic" : "Pescaria de Festa",
        "invite" : "Pescaria de Festa",
        "editor" : "Pescaria de Festa",
        "description" : "Pegue as frutas para ganhar feijões! Desvie-se das bigornas!"
    },
    4 : {
        "generic" : "Pista de Dança\n10 passos",
        "invite" : "uma Pista de Dança com 10 passos",
        "editor" : "Pista de Dança de 10",
        "description" : "Mostre seus 10 passos de dança ao estilo toon!"
    },
    5 : {
        "generic" : "Cabo de Guerra de Festa",
        "invite" : "Cabo de Guerra de Festa",
        "editor" : "Cabo de Guerra",
        "description" : "Até 4 toons de cada lado puxando loucamente!"
    },
    6 : {
        "generic" : "Fogos de Artif\xc3\xadcio de Festa",
        "invite" : "Fogos de Artif\xc3\xadcio de Festa",
        "editor" : "Fogos de Artif\xc3\xadcio",
        "description" : "Lance seu próprio show de fogos de artif\xc3\xadcio!"
    },
    7 : {
        "generic" : "Relógio de Festa",
        "invite" : "um Relógio de Festa",
        "editor" : "Relógio de Festa",
        "description" : "Faça a contagem regressiva do tempo que resta de sua festa."
    },
    8 : {
        "generic" : "Jukebox\n40 músicas",
        "invite" : "uma Jukebox de 40 músicas",
        "editor" : "Jukebox de 40",
        "description" : "Ouça música com sua própria jukebox de 40 músicas!"
    },
    9 : {
        "generic" : "Pista de Dança\n20 passos",
        "invite" : "uma Pista de Dança de 20 passos",
        "editor" : "Pista de Dança de 20",
        "description" : "Mostre seus 20 passos de dança ao estilo toon!"
    },
    10 : {
        "generic" : "Cog-O-War",
        "invite" : "Cog-O-War",
        "editor" : "Cog-O-War",
        "description" : "O jogo de equipe versus equipe de acertar Cog!"
    },
    11 : {
        "generic" : "Trampolim de Cog",
        "invite" : "Trampolim de Cog",
        "editor" : "Trampolim de Cog",
        "description" : "Pular na cara de um Cog!"
    },
    12 : {
        "generic" : "Pegando Presentes",
        "invite" : "Pegando Presentes",
        "editor" : "Pegando Presentes",
        "description" : "Pegue presentes para ganhar balas! Esquive-se daquelas bigornas!"
    },
    13 : {
        "generic" : "Trampolim de Inverno",
        "invite" : "Trampolim de Inverno",
        "editor" : "Trampolim de Inverno",
        "description" : "Pegue balinhas e salte o mais alto que puder!"
    },
    14 : {
        "generic" : "Cog-O-War de Inverno",
        "invite" : "Cog-O-War de Inverno",
        "editor" : "Cog-O-War de Inverno",
        "description" : "O jogo de equipe versus equipe de acertar Cog!"
    },
    # Translate
    15: {
        "generic" : "Pista de Dança\n10 passos",
        "invite" : " 10 move ValenToons Dance Floor",
        "editor" : "Pista de Dança de 10",
        "description" : "Get your ValenToon Groove On!"
    },
    16: {
        "generic" : "Pista de Dança\n20 passos",
        "invite" : "a 20 move ValenToons Dance Floor",
        "editor" : "Pista de Dança de 20",
        "description" : "Get your ValenToon Groove On!"
    },
    17: {
        "generic" : "Jukebox\n20 músicas",
        "invite" : "a 20 song Valentoons Jukebox",
        "editor" : "Jukebox de 20",
        "description" : "Nothing sets the mood like music!"
    },
    18: {
        "generic" : "Jukebox\n40 músicas",
        "invite" : "a 40 song Valentoons jukebox",
        "editor" : "Jukebox de 40",
        "description" : "Nothing sets the mood like music!"
    },
    19: {
        "generic" : "Trampolim",
        "invite" : "ValenToons Trampolim",
        "editor" : "Trampolim",
        "description" : "Jump to your heart's content!",
    },
}

# Note : This dictionary is used to show the names of the decorations in various
#        contexts.  If PartyGlobals.DecorationIds is changed, this list must be
#        updated with new indices.
PartyDecorationNameDict = {
    0 : {
        "editor" : "Bigorna de Balões",
        "description" : "Tente evitar que a diversão acabe!",
    },
    1 : {
        "editor" : "Palco de Festa",
        "description" : "Balões, estrelas ou qualquer coisa que desejar",
    },
    2 : {
        "editor" : "Arco de Festa",
        "description" : "Torne a diversão envolvente!",
    },
    3 : {
        "editor" : "Bolo",
        "description" : "Delicioso.",
    },
    4 : {
        "editor" : "Castelo de Festa",
        "description" : "A casa de um Toon é seu castelo.",
    },
    5 : {
        "editor" : "Pilha de Presentes",
        "description" : "Presentes para todos os Toons!",
    },
    6 : {
        "editor" : "L\xc3\xadngua de Sogra",
        "description" : "Esse apito é muito estridente! Serpenteante!",
    },
    7 : {
        "editor" : "Portão de Festa",
        "description" : "Multicolorido e doidinho!",
    },
    8 : {
        "editor" : "Itens Barulhentos",
        "description" : "Piiiiiiiiiiii!",
    },
    9 : {
        "editor" : "Cata-vento",
        "description" : "Giros coloridos para todos!",
    },
    10 : {
        "editor" : "Globo Engraçado",
        "description" : "Globo engraçado e de estrelas criado por Olivea",
    },
    11 : {
        "editor" : "Faixa Feijão",
        "description" : "Uma faixa em forma de balinha criada por Cassidy",
    },
    12 : {
        "editor" : "Bolo Engraçado",
        "description" : "Um bolo engraçado e Caótico criado por Fel\xc3\xadcia",
    },
    13 : {
        "editor" : "Corações de Cupidos",
        "description" : "Voc\xc3\xaa na mira no Dia dos namorados, divirta-se!"
    },
    14 : {
        "editor" : "Banner de Coração",
        "description" : "Compartilhe a diversão neste dia dos namorados!"
    },
    15 : {
        "editor" : "Coração Voador",
        "description" : "Flutue com o esp\xc3\xadrito do dia dos namorados!"
    },
    16 : {
        "editor" : "Suporte de palanque",
        "description" : "Todos os nossos novos amigos estão prontos para dançar!"
    },
    17 : {
        "editor" : "Faixa da vitória",
        "description" : "Não é apenas uma faixa comum!"
    },
    18 : {
        "editor" : "Canhões de confete",
        "description" : "BUM! Confete! Diversão!"
    },
    19 : {
        "editor" : "Cog e Doodle",
        "description" : "Ui! Isso vai doer."
    },
    20 : {
        "editor" : "Cog Suspenso",
        "description" : "Um Cog cheio de ar quente, chocante!"
    },
    21 : {
        "editor" : "Cog Sorvete",
        "description" : "Um Cog de boa apar\xc3\xaancia."
    },
    22 : {
        "editor" : "Cog Sorvete",
        "description" : "Um Cog de boa apar\xc3\xaancia."
    },
    23 : {
        "editor" : "Coreto de Natal",
        "description" : "Todos adoram uma Festa de Natal!"
    },
    24 : {
        "editor" : "Cog e Doodle",
        "description" : "Ai! Isso vai doer."
    },
    25 : {
        "editor" : "Boneco de neve",
        "description" : "Tão legal, ele é demais!"
    },
    26 : {
        "editor" : "Doodle de neve",
        "description" : "Seu único truque está esfriando!"
    },
    # Translate
    27: {
        "editor": "ValenToons Anvil",
        "description": "We've got your heart on a string!"
    },
}

ActivityLabel = "Custo – Nome da Atividade"
PartyDoYouWantToPlan = "Deseja planejar uma nova festa agora?"
PartyPlannerOnYourWay = "Divirta-se planejando a sua festa!"
PartyPlannerMaybeNextTime = "Talvez da próxima vez. Tenha um bom-dia!"
PartyPlannerHostingTooMany = "Desculpe, voc\xc3\xaa só pode dar uma festa de cada vez."
PartyPlannerOnlyPaid = "Desculpe, só toons assinantes podem dar uma festa."
PartyPlannerNpcComingSoon = "Em breve surgirão mais festas! Tente novamente mais tarde."
PartyPlannerNpcMinCost = "O custo m\xc3\xadnimo para planejar uma festa é de %d balinhas."

# Party Gates
PartyChapéuPublicPartyChoose = "deseja ir para a primeira festa pública dispon\xc3\xadvel?"
PartyGateTitle = "Festas Públicas"
PartyGateGoToParty = "Ir para\nFesta!"
PartyGatePartiesListTitle = "Anfitriões"
PartyGatesPartiesListToons = "Toons"
PartyGatesPartiesListActivities = "Atividades"
PartyGatesPartiesListMinLeft = "Minutos Restantes"
PartyGateLeftSign = "Venha se Divertir!"
PartyGateRightSign = "Partes público aqui!"
#PartyGateTitle = "Festas Públicas Aqui!"
PartyGatePartyUnavailable = "Desculpe. Essa festa não está mais dispon\xc3\xadvel."
PartyGatePartyFull = "Desculpe. Essa festa está lotada."
PartyGateInstructions = 'Clique em um anfitrião e em "Ir para Festa"'

# DistributedPartyActivity.py
PartyActivityWaitingForOtherPlayers = "Aguardando outros jogadores para se juntarem \xc3\xa0 festa..."
PartyActivityPleaseWait = "Por favor, aguarde..."
DefaultPartyActivityTitle = "T\xc3\xadtulo do Jogo de Festa"
DefaultPartyActivityInstructions = "Instruções do Jogo de Festa"
PartyOnlyHostLeverPull = "Apenas o anfitrião pode iniciar essa atividade. Desculpe."
PartyActivityDefaultJoinDeny = "Voc\xc3\xaa não pode participar dessa atividade no momento. Desculpe."
PartyActivityDefaultExitDeny = "Voc\xc3\xaa não pode sair dessa atividade no momento. Desculpe."

# JellybeanRewardGui.py
PartyJellybeanRewardOK = "OK"

# DistributedPartyCatchActivity.py
PartyCatchActivityTitle = "Atividade Pescaria de Festa"
PartyCatchActivityInstructions = "Pegue o máximo de peças de frutas que puder. Tente não 'pescar' quaisquer %(badThing)s!"
PartyCatchActivityFinishPerfect = "JOGO PERFEITO!"
PartyCatchActivityFinish = "Bom Jogo!"
PartyCatchActivityExit        = 'SAIR'
PartyCatchActivityApples      = 'maçãs'
PartyCatchActivityOranges     = 'laranjas'
PartyCatchActivityPears       = 'peras'
PartyCatchActivityCoconuts    = 'cocos'
PartyCatchActivityWatermelons = 'melancias'
PartyCatchActivityPineapples  = 'abacaxis'
PartyCatchActivityAnvils      = 'bigornas'
PartyCatchStarted = "O jogo começou. Divirta-se."
PartyCatchCannotStart = "O jogo não pode ser iniciado no momento."
PartyCatchRewardMessage = "Peças de frutas coletadas: %s\n\nBalinhas recebidas: %s"
WinterPartyCatchActivityInstructions = "Pegue o máximo de presentes que puder. Tente não 'pegar' nenhum %(badThing)s!"
WinterPartyCatchRewardMessage = "Presentes pegos: %s\n\nBalinhas obtidas: %s"

# DistributedPartyDanceActivity.py
PartyDanceActivityTitle = "Pista de Dança de Festa"
PartyDanceActivityInstructions = "Combine 3 ou mais padrões de SETAS para fazer os passos de dança! Há 10 passos de dança dispon\xc3\xadveis. Voc\xc3\xaa consegue obter todos?"
PartyDanceActivity20Title = "Pista de Dança de festa"
PartyDanceActivity20Instructions = "Combine 3 ou mais padrões de SETAS para fazer os passos de dança! Há 20 passos de dança dispon\xc3\xadveis. Voc\xc3\xaa consegue obter todos?"

DanceAnimRight = "Direita"
DanceAnimReelNeutral = "O Toonpescador"
DanceAnimConked = "O Cabeçamole"
DanceAnimHappyDance = "A Dança Feliz"
DanceAnimConfused = "Vertigem Total"
DanceAnimWalk = "Andando na Lua"
DanceAnimJump = "O Salto!"
DanceAnimFirehose = "O Toonbombeiro"
DanceAnimShrug = "Quem Sabe?"
DanceAnimSlipForward = "A Queda"
DanceAnimSadWalk = "Exaustão"
DanceAnimWave = "Olá, Tchauzinho"
DanceAnimStruggle = "O Pulo Misto"
DanceAnimRunningJump = "O Toon Fugitivo"
DanceAnimSlipBackward = "A Queda de Costas"
DanceAnimDown = "A Descida"
DanceAnimUp = "A Subida"
DanceAnimGoodPutt = "A Tacada"
DanceAnimVictory = "A Dança da Vitória"
DanceAnimPush = "O Toonm\xc3\xadmico"
DanceAnimAngry = "Rock'n'Roll"
DanceAnimLeft = "Esquerda"

# DistributedPartyCannonActivity.py
PartyCannonActivityTitle = "Canhões de Festa"
PartyCannonActivityInstructions = "Acerte as nuvens para mudar sua cor e ricochetear no ar! NO AR, voc\xc3\xaa pode USAR AS SETAS para DESLIZAR."
PartyCannonResults = "Voc\xc3\xaa recebeu %d balinhas!\n\nNuvens Atingidas: %d"

# DistributedPartyFireworksActivity.py
FireworksActivityInstructions = "Pressione a tecla \"Page Up\" para visualizar melhor."
FireworksActivityBeginning = "Os fogos de artif\xc3\xadcio de festa vão ser lançados! Curta o espetáculo!"
FireworksActivityEnding = "Espero que tenha gostado do espetáculo!"
PartyFireworksAlreadyActive = "O espetáculo de fogos de artif\xc3\xadcio já começou."
PartyFireworksAlreadyDone = "O espetáculo de fogos de artif\xc3\xadcio acabou."

# DistributedPartyTrampolineActivity.py
PartyTrampolineJellyBeanTitle = "Trampolim de Balinhas"
PartyTrampolineTricksTitle = "Trampolim de Acrobacias"
PartyTrampolineActivityInstructions = "Use a tecla Control para saltar.\n\nSalte quando seu Toon estiver no ponto mais baixo do trampolim para ir bem alto."
PartyTrampolineActivityOccupied = "O trampolim está sendo usado."
PartyTrampolineQuitEarlyButton = "Saltar"
PartyTrampolineBeanResults = "Voc\xc3\xaa recebeu %d balinhas."
PartyTrampolineBonusBeanResults = "Voc\xc3\xaa recebeu %d balinhas, além de mais %d por conseguir o Big Bean (Grande Feijão)."
PartyTrampolineTopHeightResults = "Seu recorde de altura foi %d ft (mt)."
PartyTrampolineTimesUp = "Acabou o Tempo"
PartyTrampolineReady = "Preparar..."
PartyTrampolineGo = "Já!"
PartyTrampolineBestHeight = "Recorde de Altura Até Agora:\n%s\n%d ft (mt)"
PartyTrampolineNoHeightYet = "Quão alto\nvoc\xc3\xaa pode saltar?"
PartyTrampolineGetHeight = "%d ft"

# DistributedPartyTeamActivity.py
# extra spaces on purpose given the blocky font
PartyTeamActivityForMorePlural = "S"
PartyTeamActivityForMore = "Aguardando %d jogadores%s\não de cada lado..."
PartyTeamActivityForMoreWithBalance = "Aguardando mais %d jogadores%s..."
PartyTeamActivityWaitingForOtherPlayers = "Aguardando outros jogadores..."
PartyTeamActivityWaitingToStart = "Começando em..."
PartyTeamActivityExitButton = "Pular Fora"
PartyTeamActivitySwitchTeamsButton = "Mudar de\nEquipe"
PartyTeamActivityWins = "A equipe %s venceu!"
PartyTeamActivityLocalAvatarTeamWins = "Sua equipe venceu!"
PartyTeamActivityGameTie = "Deu empate!"
PartyTeamActivityJoinDenied = "Voc\xc3\xaa não pode entrar para %s no momento."
PartyTeamActivityExitDenied = "Voc\xc3\xaa não pode sair de %s no momento."
PartyTeamActivitySwitchDenied = "Voc\xc3\xaa não pode mudar de equipe no momento."
PartyTeamActivityTeamFull = "Esta equipe já está completa!"
PartyTeamActivityRewardMessage = "Voc\xc3\xaa tem %d balas de goma. Bom trabalho!"

# DistributedPartyCogActivity/AI.py
PartyCogTeams = ("Azul", "Laranja") # (left, right)
PartyCogRewardMessage = "Sua Pontuação: %d\n" # unused?
PartyCogRewardBonus = "\nVoc\xc3\xaa tem %d balas de goma%s adicionais porque a sua equipe venceu!" # unused?
PartyCogJellybeanPlural = "S" # unused?
PartyCogSignNote = "RECORDE\n%s\n%d"
PartyCogTitle = "Arremesso de Torta nos Cogs"
# These instructions are slightly inaccurate: You want to push the three cogs cumulatively farther
# than the other team. It doesn't matter how many are on each side.
#"When time's up, the team who pushed the cogs farthest wins!"
PartyCogInstructions = \
"Jogue tortas nos cogs para afastá-los de sua equipe. " +\
"Quando acabar o tempo, a equipe com menos cogs ganha!" +\
"\n\nArremesse com a TECLA CTRL. Movimente-se com as SETAS DIRECIONAIS."

# PartyCogActivity.py
PartyCogDistance = "%d ft"
PartyCogTimeUp = "O tempo acabou!"

# PartyCogActivityGui.py
PartyCogGuiScoreLabel = "PONTOS"
PartyCogGuiPowerLabel = "ENERGIA"
PartyCogGuiSpamWarning = "Mantenha pressionada a tecla CONTROL para obter mais força!"
PartyCogBalanceBar = "EQUILÍBRIO"

# DistributedPartyTugOfWarActivity.py
#PartyTugOfWarJoinDenied = "Desculpe. Voc\xc3\xaa não pode participar do cabo de guerra no momento."
#PartyTugOfWarTeamFull = "Desculpe. Essa equipe já está completa."
#PartyTugOfWarExitButton = "Sair"
#PartyTugOfWarWaitingForMore = "Aguardando mais jogadores" # extra spaces on purpose given the blocky font
#PartyTugOfWarWaitingToStart = "Aguardando para começar"
#PartyTugOfWarWaitingForOtherPlayers = "Aguardando outros jogadores"
PartyTugOfWarReady = "Preparar..."
PartyTugOfWarGo = "J\xc3\x81!"
PartyTugOfWarGameEnd = "Bom jogo!"
#PartyTugOfWarGameTie = "Voc\xc3\xaa empatou!"
#PartyTugOfWarRewardMessage = "voc\xc3\xaa conseguiu %d balinhas. Bom trabalho!"
PartyTugOfWarTitle = "Cabo de Guerra de Festa"

# CalendarGuiMonth.py
CalendarShowAll = "Exibir Tudo"
CalendarShowOnlyHolidays = "Exibir Apenas Feriados"
CalendarShowOnlyParties = "Exibir Apenas Feriados"

# CalendarGuiDay.py
CalendarEndsAt = "Termina em "
CalendarStartedOn = "Iniciada em "
CalendarEndDash = "Final-"
CalendarEndOf = "Final de "
CalendarPartyGetReady = "Prepare-se!"
CalendarPartyGo = "Festejar!"
CalendarPartyFinished = "Acabou..."
CalendarPartyCancelled = "Cancelado."
CalendarPartyNeverStarted = "Nunca Aconteceu."

# NPCFriendPanel.py
NPCFriendPanelRemaining = "Restantes %s"
NPCFriendPanelUnavailable = "Indispon\xc3\xadvel"

# PartiesPage.py
#PartiesPageTitle = ""
#PartiesPageHostTab = ""
#PartiesPageInvitedTab = ""
#PartiesPageTitleHost = ""
#PartiesPageTitleInvited = ""

# MapPage.py
MapPageTitle = "Mapa"
MapPageBackToPlayground = "Voltar para o pátio"
MapPageBackToCogHQ = "Voltar para o Quartel de Cogs"
MapPageGoHome = "Ir para casa"
# hood name, street name
MapPageYouAreHere = "Voc\xc3\xaa está em: %s\n%s"
MapPageYouAreAtHome = "Voc\xc3\xaa está em\nsua propriedade"
MapPageYouAreAtSomeonesHome = "Voc\xc3\xaa está na propriedade de %s"
MapPageGoTo = "Ir para\n%s"

# OptionsPage.py
OptionsPageTitle = "Opções"
OptionsTabTitle = "Opções\n& Códigos"
OptionsPagePurchase = "Assine já!"
OptionsPageLogout = "Sair"
OptionsPageExitToontown = "Sair de Toontown"
OptionsPageMusicOnLabel = "A música está ligada."
OptionsPageMusicOffLabel = "A música está desligada."
OptionsPageSFXOnLabel = "Os efeitos sonoros estão ligados."
OptionsPageSFXOffLabel = "Os efeitos sonoros estão desligados."
OptionsPageToonChatSoundsOnLabel = "   Type Chat Sounds are on."
OptionsPageToonChatSoundsOffLabel = "   Type Chat Sounds are off."
OptionsPageFriendsEnabledLabel = "Aceito fazer novas amizades."
OptionsPageFriendsDisabledLabel = "Não aceito fazer amizades."
OptionsPageWhisperEnabledLabel = "Allowing whispers from anyone."
OptionsPageWhisperDisabledLabel = "Allowing whispers from friends only."
OptionsPageSpeedChatStyleLabel = "Cor do Chat rápido"
OptionsPageDisplayWindowed = "com janela"
OptionsPageDisplayEmbedded = "No navegador"
OptionsPageSelect = "Selecionar"
OptionsPageToggleOn = "Ligar"
OptionsPageToggleOff = "Desligar"
OptionsPageChange = "Alterar"
OptionsPageDisplaySettings = "V\xc3\xaddeo: %(screensize)s, %(api)s"
OptionsPageDisplaySettingsNoApi = "V\xc3\xaddeo: %(screensize)s"
OptionsPageExitConfirm = "Sair de Toontown?"

DisplaySettingsTitle = "Configurações de v\xc3\xaddeo"
DisplaySettingsIntro = "As configurações a seguir são usadas para determinar a maneira como Toontown é exibida em seu computador. Provavelmente, não será necessário ajustá-las, a menos que voc\xc3\xaa esteja tendo algum problema."
DisplaySettingsIntroSimple = "Voc\xc3\xaa pode ajustar a resolução da tela com um valor maior para melhorar o contraste do texto e dos gráficos em Toontown, mas, dependendo da placa de v\xc3\xaddeo do seu computador, alguns valores mais altos podem fazer que o jogo fique lento ou trave."

DisplaySettingsApi = "API de gráfico:"
DisplaySettingsResolution = "Resolução:"
DisplaySettingsWindowed = "Em uma janela"
DisplaySettingsFullscreen = "Tela cheia"
DisplaySettingsEmbedded = "No navegador"
DisplaySettingsApply = "Aplicar"
DisplaySettingsCancel = lCancel
DisplaySettingsApplyWarning = "Quando voc\xc3\xaa pressionar OK, as configurações de v\xc3\xaddeo serão alteradas. Se a nova configuração não ficar adequada em seu computador, o v\xc3\xaddeo retornará \xc3\xa0 configuração original após %s segundos."
DisplaySettingsAccept = "Pressione em OK para manter as novas configurações, ou em Cancelar para voltar \xc3\xa0s anteriores. Se voc\xc3\xaa não pressionar nada, as configurações voltarão em %s segundos automaticamente aos valores anteriores."
DisplaySettingsRevertUser = "As configurações de v\xc3\xaddeo anteriores foram restauradas."
DisplaySettingsRevertFailed = "As configurações de v\xc3\xaddeo selecionadas não funcionam em seu computador. As configurações de v\xc3\xaddeo anteriores foram restauradas."

# Code Redemption (resides in the Options Page)
OptionsPageCodesTab = "Inserir um Código"
CdrPageTitle = "Inserir um Código"
CdrInstructions = "Digite o seu código aqui para receber um pr\xc3\xaamio especial na sua caixa de entrada"
CdrResultSuccess = "Parabéns! Verifique a sua caixa de correio para reivindicar o seu pr\xc3\xaamio!"
CdrResultInvalidCode = "Voc\xc3\xaa inseriu um código inválido. Por favor, confira a digitação e tente novamente"
CdrResultExpiredCode = "Lamentamos. Esse código expirou"
CdrResultUnknownError = "Lamentamos. Esse código não pode ser aplicado ao seu Toon"
CdrResultMailboxFull = "Sua caixa de correio está cheia. Por favor, remova um item e, depois, insira o seu código novamente"
CdrResultAlreadyInMailbox = "Voc\xc3\xaa já recebeu esse item. Verifique a sua caixa de correio para confirmar"
CdrResultAlreadyInQueue = "Seu pr\xc3\xaamio está a caminho. Verifique a sua caixa de correio daqui a alguns minutos para receb\xc3\xaa-lo"
CdrResultAlreadyInCloset = "Voc\xc3\xaa já recebeu esse item. Verifique o seu armário para confirmar"
CdrResultAlreadyBeingWorn = "Voc\xc3\xaa já recebeu esse item e o está usando!"
CdrResultAlreadyReceived = "Voc\xc3\xaa já recebeu esse item."
CdrResultTooManyFails = "Lamentamos. Voc\xc3\xaa tentou inserir um código errado repetidamente. Por favor, tente novamente daqui a 30 minutos"
CdrResultServiceUnavailable = "Lamentamos. Esta caracter\xc3\xadstica é temporariamente não dispon\xc3\xadvel. Tente por favor outra vez durante seu in\xc3\xadcio de uma sessão seguinte."

# TrackPage.py
TrackPageTitle = "Treinamento de tipos de piadas"
TrackPageShortTitle = "Treinamento de\npiadas"
TrackPageSubtitle = "Execute as Tarefas Toon para aprender a usar novas piadas!"
TrackPageTraining = "Voc\xc3\xaa está treinando para usar as Piadas de %s.\nQuando executar todas as 16 tarefas,\nestará apto a usar as Piadas de %s nas batalhas."
TrackPageClear = "Voc\xc3\xaa não está treinando nenhum tipo de piadas agora."
TrackPageFilmTitle = "Filme de\ntreinamento\nde %s"
TrackPageDone = "FIM"

# QuestPage.py
QuestPageToonTasks = "Tarefas Toon"
# questName, toNpcName, toNpcBuilding, toNpcStreetName, toNpcLocationName, npcName
#QuestPageDelivery = "%s\nPara: %s\n  %s\n  %s\n  %s\n\nDe: %s"
# questName, toNpcName, toNpcBuilding, toNpcStreetName, toNpcLocationName, npcName
#QuestPageVisit = "%s %s\n  %s\n  %s\n  %s\n\nDe: %s"
# questName, toNpcName, toNpcBuilding, toNpcStreetName, toNpcLocationName
# Choose between trackA and trackB.
#
# To choose, go see:
#   Flippy
#   Town Hall
#   Playground
#   Toontown Central
#QuestPageTrackChoice = "%s\n\nPara escolher, selecione:\n  %s\n  %s\n  %s\n  %s"
# questName, npcName, buildingName, streetName, locationName
QuestPageChoose = "Escolha"
QuestPageLocked = "Travado"
# building name, street name, Npc location
QuestPageDestination = "%s\n%s\n%s"
# npc name, building name, street name, Npc location
QuestPageNameAndDestination = "%s\n%s\n%s\n%s"

QuestPosterHQOfficer = lHQOfficerM
QuestPosterHQBuildingName = lToonHQ
QuestPosterHQStreetName = "Qualquer rua"
QuestPosterHQLocationName = "Qualquer bairro"

QuestPosterTailor = "Costureiro"
QuestPosterTailorBuildingName = "Loja de Roupas"
QuestPosterTailorStreetName = "Qualquer pátio"
QuestPosterTailorLocationName = "Qualquer bairro"
QuestPosterPlayground = "No pátio"
QuestPosterAtHome = "Na sua casa"
QuestPosterInHome = "Em sua casa"
QuestPosterOnPhone = "No seu telefone"
QuestPosterEstate = "Na sua propriedade"
QuestPosterAnywhere = "Qualquer lugar"
QuestPosterAuxTo = "para:"
QuestPosterAuxFrom = "de:"
QuestPosterAuxFor = "para:"
QuestPosterAuxOr = "ou:"
QuestPosterAuxReturnTo = "Retornar\npara:"
QuestPosterLocationIn = ""
QuestPosterLocationOn = ""
QuestPosterFun = "Só de brincadeira!"
QuestPosterFishing = "IR PESCAR"
QuestPosterComplete = "CONCLUIR"

# ShardPage.py
ShardPageTitle = "Regiões"
ShardPageHelpIntro = "Cada Região é uma cópia do mundo de Toontown."
ShardPageHelpWhere = " Voc\xc3\xaa está agora na Região \"%s\"."
ShardPageHelpWelcomeValley = " Voc\xc3\xaa está agora na Região \"Vale Boas-vindas\", em \"%s\"."
ShardPageHelpMove = " Para ir até uma nova Região, clique no nome dela."

ShardPagePopulationTotal = "População Total de Toontown:\n%d"
ShardPageScrollTitle = "Nome População"
ShardPageLow = "Tranquila"
ShardPageMed = "Inteligente"
ShardPageHigh = "Lotada"
ShardPageChoiceReject = "Desculpe, essa Região está lotada. Por favor, tente outra."

# SuitPage.py
SuitPageTitle = "Galeria de Cogs"
SuitPageMystery = DialogQuestion + DialogQuestion + DialogQuestion
SuitPageQuota = "%s de %s"
SuitPageCogRadar = "%s presentes"
SuitPageBuildingRadarS = "%s edif\xc3\xadcio"
SuitPageBuildingRadarP = "%s edif\xc3\xadcios"

# DisguisePage.py
DisguisePageTitle = Cog + "Disfarce"
DisguisePageMeritAlert = "Pronto para a\npromoção!"
DisguisePageCogLevel = "N\xc3\xadvel %s"
DisguisePageMeritFull = "Completo"

# FishPage.py
FishPageTitle = "Pescaria"
FishPageTitleTank = "Balde de peixes"
FishPageTitleCollection = "\xc3\x81lbum de peixes"
FishPageTitleTrophy = "Troféus de pesca"
FishPageWeightStr = "Peso: "
FishPageWeightLargeS = "%d Kg "
FishPageWeightLargeP = "%d Kg "
FishPageWeightSmallS = "%d g"
FishPageWeightSmallP = "%d g"
FishPageWeightConversion = 16
FishPageValueS = "Valor: %d balinha"
FishPageValueP = "Valor: %d balinhas"
#FishPageTotalValue = ""
FishPageCollectedTotal = "Espécies de peixes recolhidas: %d de %d"
FishPageRodInfo = "Vara %s\n%d - %d quilos"
FishPageTankTab = "Balde"
FishPageCollectionTab = "\xc3\x81lbum"
FishPageTrophyTab = "Troféus"

FishPickerTotalValue = "Balde: %s / %s\nValor: %d balinhas"

UnknownFish = DialogQuestion + DialogQuestion + DialogQuestion

FishingRod = "Vara %s"
FishingRodNameDict = {
    0 : "Vareta",
    1 : "Bambu",
    2 : "Madeira de lei",
    3 : "Aço",
    4 : "Dourado",
    }
FishTrophyNameDict = {
    0 : "Peixinhozinho",
    1 : "Peixinho",
    2 : "Peixe",
    3 : "Peixe-voador",
    4 : "Tubarão",
    5 : "Peixe-espada",
    6 : "Baleia assassina",
    }

# GardenPage.py
GardenPageTitle = "Jardinagem"
GardenPageTitleBasket = "Cesto de Flores"
GardenPageTitleCollection = "\xc3\x81lbum de Flores"
GardenPageTitleTrophy = "Troféus de Jardinagem"
GardenPageTitleSpecials = "Especiais de Jardinagem"
GardenPageBasketTab = "Cesto"
GardenPageCollectionTab = "\xc3\x81lbum"
GardenPageTrophyTab = "Troféus"
GardenPageSpecialsTab = "Especiais"
GardenPageCollectedTotal = "Variedades de Flores Colecionadas: %d de %d"
GardenPageValueS = "Valor: %d balinha"
GardenPageValueP = "Valor: %d balinhas"
FlowerPickerTotalValue = "Cesto: %s / %s\nValor: %d balinhas"
GardenPageShovelInfo = "%s Pá: %d / %d\n"
GardenPageWateringCanInfo = "%s Regador: %d / %d"

FlowerPageWeightConversion = 1
FlowerPageWeightLargeP = " Grande P "
FlowerPageWeightLargeS = " GrandeS "
FlowerPageWeightSmallP = " PequenoP "
FlowerPageWeightSmallS = " PequenoS "
FlowerPageWeightStr = " Peso: %s "

# KartPage.py
KartPageTitle = "Karts"
KartPageTitleCustomize = "Personalizador de karts"
KartPageTitleRecords = "Melhores recordes pessoais"
KartPageTitleTrophy = "Troféus de corridas"
KartPageCustomizeTab = "Personalizar"
KartPageRecordsTab = "Recordes"
KartPageTrophyTab = "Troféus"
KartPageTrophyDetail = "Troféus %s : %s"
KartPageTickets = "Bilhetes :"
KartPageConfirmDelete = "Excluir acessório?"

#plural
KartShtikerDelete = "Excluir"
KartShtikerSelect = "Selecionar uma categoria"
KartShtikerNoAccessories = "Não possui acessórios"
KartShtikerBodyColors = "Cores de karts"
KartShtikerAccColors = "Cores de acessórios"
KartShtikerEngineBlocks = "Acessórios de capô"
KartShtikerSpoilers = "Acessórios de mala"
KartShtikerFrontWheelWells = "Acessórios de roda dianteira"
KartShtikerBackWheelWells = "Acessórios de roda traseira"
KartShtikerRims = "Acessórios de aro"
KartShtikerDecals = "Acessórios de decalque"
#singluar
KartShtikerBodyColor = "Cor do kart"
KartShtikerAccColor = "Cor do acessório"
KartShtikerEngineBlock = "Capô"
KartShtikerSpoiler = "Mala"
KartShtikerFrontWheelWell = "Roda dianteira"
KartShtikerBackWheelWell = "Roda traseira"
KartShtikerRim = "Aro"
KartShtikerDecal = "Decalque"

KartShtikerDefault = "Padrão %s"
KartShtikerNo = "Nenhum acessório %s"

# QuestChoiceGui.py
QuestChoiceGuiCancel = lCancel

# TrackChoiceGui.py
TrackChoiceGuiChoose = "Escolher"
TrackChoiceGuiCancel = lCancel
TrackChoiceGuiHEAL = 'Toonar permite que voc\xc3\xaa cure outros Toons que estão na batalha.'
TrackChoiceGuiTRAP = 'Armadilhas são piadas poderosas que devem ser usadas com Iscas.'
TrackChoiceGuiLURE = 'Use Iscas para abalar os Cogs ou faça-os cair em armadilhas.'
TrackChoiceGuiSOUND = 'As piadas Sonoras afetam todos os Cogs, mas não são muito poderosas.'
TrackChoiceGuiDROP = "As piadas Cadentes fazem muitos estragos, mas não são muito precisas."

# EmotePage.py
EmotePageTitle = "Expressões / Emoções"
EmotePageDance = "Voc\xc3\xaa montou a seguinte sequ\xc3\xaancia de dança:"
EmoteJump = "Saltitante"
EmoteDance = "Dançante"
EmoteHappy = "Feliz"
EmoteSad = "Triste"
EmoteAnnoyed = "Aborrecido"
EmoteSleep = "Sonolento"

# TIP Page
TIPPageTitle = "DICA"

# SuitBase.py
SuitBaseNameWithLevel = "%(name)s\n%(dept)s\nN\xc3\xadvel %(level)s"

# HealthForceAcknowledge.py
HealthForceAcknowledgeMessage = "Voc\xc3\xaa não pode sair do parque até que o seu Risômetro esteja sorrindo!"

# InventoryNew.py
InventoryTotalGags = "Total de piadas\n%d / %d"
InventroyPinkSlips = "%s Bilhetes Azuis"
InventroyPinkSlip = "1 Bilhete Azul"
InventoryDelete = "EXCLUIR"
InventoryDone = "OK"
InventoryDeleteHelp = "Clique em uma piada para EXCLUIR."
InventorySkillCredit = "Crédito de habilidades:\n%s"
InventorySkillCreditNone = "Crédito de habilidades:\nNenhum"
InventoryDetailAmount = "%(numItems)s / %(maxItems)s"
# acc, damage_string, damage, single_or_group
InventoryDetailData = "Precisão: %(accuracy)s\n%(damageString)s: %(damage)d\n%(singleOrGroup)s"
InventoryTrackExp = "%(curExp)s / %(nextExp)s"
InventoryUberTrackExp = "Faltam %(nextExp)s!"
InventoryGuestExp = "Limite de Visitantes"
GuestLostExp = " Acima do Limite de Visitantes"
InventoryAffectsOneCog = "Afeta: Um "+ Cog
InventoryAffectsOneToon = "Afeta: Um Toon"
InventoryAffectsAllToons = "Afeta: Todos os Toons"
InventoryAffectsAllCogs = "Afeta: Todos os "+ Cogs
InventoryHealString = "Toonar"
InventoryDamageString = "Dano"
InventoryBattleMenu = "MENU DE BATALHA"
InventoryRun = "CORRER"
InventorySOS = "SOS"
InventoryPass = "PASSAR"
InventoryFire = "Fogo"
InventoryClickToAttack = "Clique em uma\npiada para\natacar"
InventoryDamageBonus = "(+%d)"

# NPCForceAcknowledge.py
NPCForceAcknowledgeMessage = "Voc\xc3\xaa deve pegar o bondinho antes de sair.\n\n\n\n\nVoc\xc3\xaa poderá encontrar o bondinho ao lado da Loja de Piadas do Pateta."
NPCForceAcknowledgeMessage2 = "Muito bem! Voc\xc3\xaa completou a busca pelo bondinho!\nVisite o Quartel dos Toons para solicitar a sua recompensa.\n\n\n\n\n\nO Quartel dos Toons localiza-se próximo ao centro do pátio."
NPCForceAcknowledgeMessage3 = "Lembre-se de pegar o bondinho.\n\n\n\nVoc\xc3\xaa pode encontrar o bondinho ao lado da Loja de Piadas do Pateta."
NPCForceAcknowledgeMessage4 = "Parabéns! Voc\xc3\xaa concluiu a sua primeira Tarefa Toon!\n\n\n\n\n\nVisite o Quartel dos Toons para solicitar a sua recompensa."
NPCForceAcknowledgeMessage5 = "Não se esqueça de sua Tarefa Toon!\n\n\n\n\n\n\n\n\n\n\nVoc\xc3\xaa pode encontrar Cogs para serem derrotados do outro lado de túneis como este."
NPCForceAcknowledgeMessage6 = "Excelente trabalho derrotando esses Cogs!\n\n\n\n\n\n\n\n\nVolte para o Quartel dos Toons o mais rápido poss\xc3\xadvel."
NPCForceAcknowledgeMessage7 = "Não se esqueça de fazer um amigo!\n\n\n\n\n\n\nClique em outro jogador e use o botão Novo amigo."
NPCForceAcknowledgeMessage8 = "\xc3\x93timo! Voc\xc3\xaa fez um novo amigo!\n\n\n\n\n\n\n\n\nAgora, voc\xc3\xaa deve voltar para o Quartel dos Toons."
NPCForceAcknowledgeMessage9 = "Bom trabalho usando o telefone!\n\n\n\n\n\n\n\n\nVolte para o Quartel dos Toons para pedir a sua recompensa."

# Toon.py
ToonSleepString = ". . . ZZZ . . ."

# Movie.py
MovieTutorialReward1 = "Voc\xc3\xaa recebeu 1 ponto de Lançamento! Quando voc\xc3\xaa obtém 10, ganha uma nova piada!"
MovieTutorialReward2 = "Voc\xc3\xaa recebeu 1 ponto de Esguicho! Quando voc\xc3\xaa obtém 10, ganha uma nova piada!"
MovieTutorialReward3 = "Muito bom! Voc\xc3\xaa concluiu a sua primeira Tarefa Toon!"
MovieTutorialReward4 = "Vá para o Quartel dos Toons para pegar a sua recompensa!"
MovieTutorialReward5 = "Divirta-se!"

# ToontownBattleGlobals.py
BattleGlobalTracks = ['toonar', 'armadilha', 'isca', 'sonora', 'lançamento', 'esguicho', 'cadente']
BattleGlobalNPCTracks = ['reabastecer', 'toons atingidos', 'cogs não-atingidos']
BattleGlobalAvPropStrings = (
    ('Pena', 'Megafone', 'Batom', 'Bengala', 'Pó mágico', 'Bolinhas de malabarismo', 'Mergulho Elevado'),
    ('Casca de banana', 'Ancinho', 'Bolas de gude', 'Areia movediça', 'Alçapão', 'TNT', 'Estrada De Ferro'),
    ('Nota de $1', 'Ímã pequeno', 'Nota de $5', 'Ímã grande', 'Nota de $10', '\xc3\x93culos hipnóticos', 'Presentação'),
    ('Buzina de bicicleta', 'Apito', 'Trombeta', 'Foooonnnn!', 'Tromba de elefante', 'Buzina', 'Cantor de \xc3\x93pera'),
    ('Bolinho', 'Fatia de torta de frutas', 'Fatia de torta de creme', 'Torta de frutas inteira', 'Torta de creme inteira', 'Bolo de aniversário', 'Bolo de Casamento'),
    ('Flor com esguicho', 'Copo d\'água', 'Revólver de água', 'Garrafa de água com gás', 'Mangueira de inc\xc3\xaandio', 'Nuvem de chuva', 'G\xc3\xaaiser'),
    ('Vaso de flor', 'Saco de areia', 'Bigorna', 'Peso pesado', 'Cofre', 'Piano de cauda', 'Toontanic')
    )
BattleGlobalAvPropStringsSingular = (
    ('uma Pena', 'um Megafone', 'um Batom', 'uma Bengala', 'um Pó mágico', 'um conjunto de Bolinhas de malabarismo', 'um Mergulho Elevado'),
    ('uma Casca de banana', 'um Ancinho', 'um conjunto de Bolas de gude', 'uma poça de Areia movediça', 'um Alçapão', 'um TNT', 'uma Estrada de Ferro'),
    ('uma Nota de $1', 'um Ímã pequeno', 'uma Nota de $5', 'um Ímã grande', 'uma Nota de $10', 'um par de \xc3\x93culos hipnóticos', 'uma Presentação'),
    ('uma Buzina de bicicleta', 'um Apito', 'uma Trombeta', 'um Foooonnnn!', 'uma Tromba de elefante', 'uma Buzina', 'um Cantor de \xc3\x93pera'),
    ('um Bolinho', 'uma Fatia de torta de frutas', 'uma Fatia de torta de creme', 'uma Torta de frutas inteira', 'uma Torta de creme inteira', 'um Bolo de Casamento'),
    ('uma Flor com esguicho', 'um Copo d\'água', 'um Revólver de água', 'uma Garrafa de água com gás', 'uma Mangueira de inc\xc3\xaandio', 'uma Nuvem de chuva', 'um G\xc3\xaaiser'),
    ('um Vaso de flor', 'um Saco de areia', 'uma Bigorna', 'um Peso pesado', 'um Cofre', 'um Piano de cauda', 'the Toontanic')
    )
BattleGlobalAvPropStringsPlural = (
    ('Penas', 'Megafones', 'Batons', 'Bengalas', 'Pós mágicos', 'conjuntos de Bolinhas de malabarismo', 'Mergulhos Elevados'),
    ('Cascas de banana', 'Ancinhos', 'conjuntos de Bolas de gude', 'poças de Areia movediça', 'Alçapões','TNTs', 'Estradas de Ferro'),
    ('Notas de $1', 'Ímãs pequenos', 'Contas de $5', 'Ímãs grandes','Contas de $10', 'par de \xc3\x93culos hipnóticos', 'Presentação'),
    ('Buzinas de bicicleta', 'Apitos', 'Trombetas', 'Foooonnnns!', 'Trombas de elefante', 'Buzinas', 'Cantor de \xc3\x93pera'),
    ('Bolinhos', 'Fatias de torta de frutas', 'Fatias de torta de creme','Tortas de frutas inteiras', 'Tortas de creme inteiras', 'Bolos de aniversário', 'Bolo de Casamento'),
    ('Flores com esguicho', 'Copos d\'água', 'Revólveres de água','Garrafas de água com gás', 'Mangueiras de inc\xc3\xaandio', 'Nuvens de chuva', 'G\xc3\xaaiser'),
    ('Vasos de flor', 'Sacos de areia', 'Bigornas', 'Pesos pesados', 'Cofres','Pianos de cauda', 'Transatlânticos')
    )
BattleGlobalAvTrackAccStrings = ("Médio", "Perfeito", "Baixo", "Alto", "Médio", "Alto", "Baixo")
BattleGlobalLureAccLow = "Baixo"
BattleGlobalLureAccMedium = "Médio"

AttackMissed = "PERDEU"

NPCCallButtonLabel = 'CHAMAR'

# ToontownLoader.py
LoaderLabel = "Carregando..."

# PlayGame.py
HeadingToHood = "Indo %(to)s %(hood)s..." # hood name
HeadingToYourEstate = "Indo para a sua propriedade..."
HeadingToEstate = "Indo para a propriedade de %s..."  # avatar name
HeadingToFriend = "Indo para a propriedade do amigo de %s..."  # avatar name

# Hood.py
HeadingToPlayground = "Indo para o Pátio..."
HeadingToStreet = "Indo %(to)s %(street)s..." # Street name

# TownBattle.py
TownBattleRun = "Voltar correndo para o pátio?"

# TownBattleChooseAvatarPanel.py
TownBattleChooseAvatarToonTitle = "QUAL TOON?"
TownBattleChooseAvatarCogTitle = "QUAL " + Cog.upper() + "?"
TownBattleChooseAvatarBack = "VOLTAR"

#firecogpanel
FireCogTitle = "BILHETES AZUIS RESTANTES:%s\nQUAL COG DEMITIR?"
FireCogLowTitle = "BILHETES AZUIS RESTANTES:%s\nSEM BILHETES SUFICIENTES!"

# TownBattleSOSPanel.py
TownBattleSOSNoFriends = "Não há amigos para chamar!"
TownBattleSOSWhichFriend = "Chamar qual amigo?"
TownBattleSOSNPCFriends = "Toons resgatados"
TownBattleSOSBack = "VOLTAR"

# TownBattleToonPanel.py
TownBattleToonSOS = "SOS"
TownBattleToonFire = "Disparar"
TownBattleUndecided = "?"
TownBattleHealthText = "%(hitPoints)s/%(maxHit)s"

# TownBattleWaitPanel.py
TownBattleWaitTitle = "Aguardando\noutros jogadores..."
TownSoloBattleWaitTitle = "Aguarde..."
TownBattleWaitBack = "VOLTAR"

# TownBattleSOSPetSearchPanel.py
TownBattleSOSPetSearchTitle = "Procurando rabisco\n%s..."

# TownBattleSOSPetInfoPanel.py
TownBattleSOSPetInfoTitle = "%s está %s"
TownBattleSOSPetInfoOK = lOK

# Trolley.py
TrolleyHFAMessage = "Voc\xc3\xaa não pode embarcar no bondinho até que o seu Risômetro esteja sorrindo."
TrolleyTFAMessage = "\Voc\xc3\xaa não pode embarcar no bondinho até que o " + Mickey +" permita."
TrolleyHopOff = "Descer"

# DistributedFishingSpot.py
FishingExit = "Sair"
FishingCast = "Lançar"
FishingAutoReel = "Molinete automático"
FishingItemFound = "Voc\xc3\xaa pegou:"
FishingCrankTooSlow = "Muito\ndevagar"
FishingCrankTooFast = "Muito\nrápido"
FishingFailure = "Voc\xc3\xaa não pegou nada!"
FishingFailureTooSoon = "Não comece a rebobinar a linha até que voc\xc3\xaa veja uma pequena mordida. Espere a bóia balançar para cima e para baixo rapidamente!"
FishingFailureTooLate = "Rebobine a linha enquanto o peixe ainda está mordendo a isca!"
FishingFailureAutoReel = "O molinete automático não funcionou desta vez. Gire a manivela manualmente, na velocidade certa, para ter mais chance de pegar alguma coisa!"
FishingFailureTooSlow = "Voc\xc3\xaa girou a manivela muito devagar. Alguns peixes são mais rápidos do que outros. Tente manter a barra de velocidade centralizada!"
FishingFailureTooFast = "Voc\xc3\xaa girou a manivela muito rápido. Alguns peixes são mais lentos do que outros. Tente manter a barra de velocidade centralizada!"
FishingOverTankLimit = "O seu balde de pesca está cheio. Vá vender os seus peixes para o Vendedor da Loja de Animais e volte."
FishingBroke = "Voc\xc3\xaa não tem mais balinhas para as iscas! Para ganhar mais balinhas, pegue o bondinho ou venda os peixes para os Vendedores da Loja de Animais."
FishingHowToFirstTime = "Clique e arraste para baixo no botão Lançar. Quanto mais baixo voc\xc3\xaa arrastar, mais forte será o lançamento. Ajuste o ângulo para acertar os alvos dos peixes.\n\nTente agora!"
FishingHowToFailed = "Clique e arraste para baixo no botão Lançar. Quanto mais baixo voc\xc3\xaa arrastar, mais forte será o lançamento. Ajuste o ângulo para acertar os alvos dos peixes.\n\nTente agora de novo!"
FishingBootItem = "Bota velha"
FishingJellybeanItem = "%s balinhas"
FishingNewEntry = "Novas espécies!"
FishingNewRecord = "Novo recorde!"

# FishPoker
FishPokerCashIn = "Morrer\n%s\n%s"
FishPokerLock = "Bloquear"
FishPokerUnlock = "Desbloquear"
FishPoker5OfKind = "5 de um naipe"
FishPoker4OfKind = "4 de um naipe"
FishPokerFullHouse = "Full House"
FishPoker3OfKind = "3 de um naipe"
FishPoker2Pair = "2 pares"
FishPokerPair = "Par"

# DistributedTutorial.py
TutorialGreeting1 = "Oi %s!"
TutorialGreeting2 = "Oi %s!\nVem cá!"
TutorialGreeting3 = "Oi %s!\nVem cá!\nUse as teclas de seta!"
TutorialMickeyWelcome = "Bem-vindo a Toontown!"
TutorialFlippyIntro = "Deixe-me apresentar voc\xc3\xaa ao meu amigo "+ Flippy +"..."
TutorialFlippyHi = "Oi, %s!"
TutorialQT1 = "Voc\xc3\xaa pode conversar usando isto."
TutorialQT2 = "Voc\xc3\xaa pode conversar usando isto.\nClique no item e escolha \"Oi\"."
TutorialChat1 = "Voc\xc3\xaa pode conversar usando qualquer um destes botões."
TutorialChat2 = "O botão azul permite que voc\xc3\xaa converse usando o teclado."
TutorialChat3 = "Cuidado! A maior parte dos outros jogadores não entenderá o que voc\xc3\xaa está dizendo se usar o teclado."
TutorialChat4 = "O botão verde abre o %s."
TutorialChat5 = "Todos entenderão se voc\xc3\xaa usar o %s."
TutorialChat6 = "Tente dizer \"Oi\"."
TutorialBodyClick1 = "Muito bem!"
TutorialBodyClick2 = "Muito prazer! Quer ser meu amigo?"
TutorialBodyClick3 = "Para fazer amizade com "+ Flippy +", clique nele..."
TutorialHandleBodyClickSuccess = "Muito bom!"
TutorialHandleBodyClickFail = "Não é assim. Tente clicar em cima do "+ Flippy +"..."
TutorialFriendsButton = "Agora, clique no botão 'Amigos' abaixo da figura do "+ Flippy +" no canto direito."
TutorialHandleFriendsButton = "Em seguida, clique no botão 'Sim'.."
TutorialOK = lOK
TutorialYes = lYes
TutorialNo = lNo
TutorialFriendsPrompt = "Voc\xc3\xaa quer fazer amizade com o "+ Flippy +"?"
TutorialFriendsPanelMickeyChat = Flippy + " aceitou ser seu amigo. Clique em 'Ok' para concluir."
TutorialFriendsPanelYes = Flippy + " disse sim!"
TutorialFriendsPanelNo = "Isso não foi muito simpático!"
TutorialFriendsPanelCongrats = "Parabéns! Voc\xc3\xaa fez seu primeiro amigo."
TutorialFlippyChat1 = "Venha me ver quando estiver pronto para a sua primeira Tarefa Toon!"
TutorialFlippyChat2 = "Estarei na PrefeiToona!"
TutorialAllFriendsButton = "Voc\xc3\xaa pode ver todos os seus amigos clicando no botão Amigos. Experimente..."
TutorialEmptyFriendsList = "No momento, a sua lista está vazia porque o "+ Flippy +" não é um jogador real."
TutorialCloseFriendsList = "Clique no botão 'Fechar'\npara fazer que a\nlista desapareça"
TutorialShtickerButton = "O botão do canto direito inferior abre o seu \xc3\x81lbum Toon. Experimente..."
TutorialBook1 = "O álbum contém várias informações úteis, como este mapa de Toontown."
TutorialBook2 = "Voc\xc3\xaa também pode verificar o andamento de suas Tarefas Toon."
TutorialBook3 = "Quando voc\xc3\xaa estiver pronto, clique no botão do álbum novamente, para fechá-lo"
TutorialLaffMeter1 = "Voc\xc3\xaa também precisará disto..."
TutorialLaffMeter2 = "Voc\xc3\xaa também precisará disto...\n\xc3\x89 o seu Risômetro."
TutorialLaffMeter3 = "Quando os "+ Cogs +" atacarem voc\xc3\xaa, ele diminui."
TutorialLaffMeter4 = "Quando voc\xc3\xaa está em pátios como este, ele volta a subir."
TutorialLaffMeter5 = "Quando concluir as Tarefas Toon, voc\xc3\xaa obterá recompensas, como o aumento do seu Limite de risadas."
TutorialLaffMeter6 = "Cuidado! Se os "+ Cogs +" derrotarem voc\xc3\xaa, perderá todas as suas piadas."
TutorialLaffMeter7 = "Para obter mais piadas, divirta-se com os jogos no bondinho."
TutorialTrolley1 = "Siga-me até o bondinho!"
TutorialTrolley2 = "Pule nele!"
TutorialBye1 = "Brinque com alguns jogos!"
TutorialBye2 = "Divirta-se com alguns jogos!\nCompre algumas piadas!"
TutorialBye3 = "\Vá encontrar o  "+ Flippy +" quando terminar!"# TutorialForceAcknowledge.py

# TutorialForceAcknowledge.py
TutorialForceAcknowledgeMessage = "\Voc\xc3\xaa está indo na direção errada! \Vá encontrar o  "+ Mickey +"!"# SpeedChat

PetTutorialTitle1 = "O Painel dos Rabiscos"
PetTutorialTitle2 = "Chat rápido dos Rabiscos"
PetTutorialTitle3 = "Gadálogo dos Rabiscos"
PetTutorialNext = "Próxima Página"
PetTutorialPrev = "Página Anterior"
PetTutorialDone = lOK
PetTutorialPage1 = "Clique em um Rabisco para exibir o painel de Rabiscos. Daqui, voc\xc3\xaa pode alimentar, coçar e chamar o Rabisco."
PetTutorialPage2 = "Use a nova área 'Bichinhos' no menu Chat rápido para fazer com que um Rabisco faça um truque. Se ele fizer, recompense-o para ele melhorar ainda mais!"
PetTutorialPage3 = "Compre novos truques de Rabiscos no Gadálogo da Clarabela. Truques melhores produzem Toonar melhores!"
def getPetGuiAlign():
	from toontown.toonbase.ToontownModules import TextNode
	return TextNode.ACenter

GardenTutorialTitle1 = "Jardinagem"
GardenTutorialTitle2 = "Flores"
GardenTutorialTitle3 = "\xc3\x81rvores"
GardenTutorialTitle4 = "Instruções"
GardenTutorialTitle5 = "Estátuas"
GardenTutorialNext = "Próxima Página"
GardenTutorialPrev = "Página Anterior"
GardenTutorialDone = lOK
GardenTutorialPage1 = "Crie o seu próprio jardim botânico! Voc\xc3\xaa pode plantar flores e árvores, e até erguer estátuas."
GardenTutorialPage2 = "As flores são sens\xc3\xadveis, e voc\xc3\xaa precisa descobrir as suas receitas de balinhas. Plante todos os tipos para melhorar as risadas, e venda as flores para ganhar balinhas."
GardenTutorialPage3 = "Use uma piada para plantar uma árvore. Alguns dias depois, essa piada vai melhorar!! Mas cuide bem da saúde dela, ou a melhoria se vai."
GardenTutorialPage4 = "Para plantar, regar, cavar ou fazer a colheita no seu jardim, ande até estes locais."
GardenTutorialPage5 = "Estátuas podem ser compradas no Catálogo da Clarabela. Aumenta suas habilidades para destravar as estátuas mais extravagantes."

# Playground.py
PlaygroundDeathAckMessage = "Os" + Cogs + " levaram todas as suas piadas!\n\nVoc\xc3\xaa está triste. Voc\xc3\xaa não pode sair do pátio até ficar feliz."

# FactoryInterior.py
ForcedLeaveFactoryAckMsg = "O Supervisor da fábrica foi derrotado antes de voc\xc3\xaa alcançá-lo. Voc\xc3\xaa não recuperou nenhuma parte do Cog."

# MintInterior
ForcedLeaveMintAckMsg = "O Supervisor do Andar da Casa da Moeda foi derrotado antes de voc\xc3\xaa alcançá-lo. Voc\xc3\xaa não recuperou nenhuma Grana Cog."

# DistributedFactory.py
HeadingToFactoryTitle = "Dirigindo-se a %s..."
ForemanConfrontedMsg = "%s está lutando com o Supervisor da fábrica!"

# DistributedMint.py
MintBossConfrontedMsg = "%s está lutando com o Supervisor!"

# DistributedStage.py
StageBossConfrontedMsg = "%s está lutando com o Funcionário!"
stageToonEnterElevator = "%s \nentrou no elevador"
ForcedLeaveStageAckMsg = "O Funcionário da Lei foi derrotado antes de voc\xc3\xaa alcançá-lo. Voc\xc3\xaa não recuperou nenhum Aviso de Júri."

# DistributedMinigame.py
MinigameWaitingForOtherPlayers = "Aguardando outros jogadores..."
MinigamePleaseWait = "Aguarde..."
DefaultMinigameTitle = "T\xc3\xadtulo do minijogo"
DefaultMinigameInstructions = "Instruções do minijogo"
HeadingToMinigameTitle = "Dirigindo-se a %s..." # minigame title

# MinigamePowerMeter.py
MinigamePowerMeterLabel = "Medidor de pot\xc3\xaancia"
MinigamePowerMeterTooSlow = "Muito\ndevagar"
MinigamePowerMeterTooFast = "Muito\nrápido"

# DistributedMinigameTemplate.py
MinigameTemplateTitle = "Modelo de minijogo"
MinigameTemplateInstructions = "Este é um modelo de minijogo. Use-o para criar novos minijogos."

# DistributedCannonGame.py
CannonGameTitle = "Jogo do canhão"
CannonGameInstructions = "Atire o seu Toon na torre de água o mais rápido que puder. Use o mouse ou as teclas de seta para mirar o canhão. Seja rápido e ganhe uma grande recompensa para todos!"
CannonGameReward = "RECOMPENSA"

# DistributedTwoDGame.py
TwoDGameTitle = "Fuga dos Cartoons"
TwoDGameInstructions = "Fuja dos " + Cog + " o mais rápido que voc\xc3\xaa puder. Use as setas para correr/pular e Ctrl para esguichar " + Cog + ". Colete " + Cog + " tesouros para ganhar mais pontos."
TwoDGameElevatorExit = "SAÍDA"

# DistributedTugOfWarGame.py
TugOfWarGameTitle = "Cabo de guerra"
TugOfWarInstructions = "Toque alternadamente nas teclas de seta para a esquerda e para a direita rápido o suficiente para alinhar a barra verde com a linha vermelha. Não toque nelas muito devagar, ou voc\xc3\xaa acabará na água!"
TugOfWarGameGo = "COME\xc3\x87AR!"
TugOfWarGameReady = "Pronto..."
TugOfWarGameEnd = "Bom jogo!"
TugOfWarGameTie = "Voc\xc3\xaa empatou!"
TugOfWarPowerMeter = "Medidor"

# DistributedPatternGame.py
PatternGameTitle = "Acompanhe a "+ Minnie
PatternGameInstructions = "A " + Minnie + " mostrará uma sequ\xc3\xaancia de dança." + \
                          "Tente repetir a dança da "+ Minnie +" exatamente como voc\xc3\xaa v\xc3\xaa usando as teclas de seta!"
PatternGameWatch   = "Observe estes passos de dança..."
PatternGameGo      = "COME\xc3\x87AR!"
PatternGameRight   = "Bom, %s!"
PatternGameWrong   = "Ops!"
PatternGamePerfect = "Perfeito, %s!"
PatternGameBye     = "Obrigado por jogar!"
PatternGameWaitingOtherPlayers = "Aguardando outros jogadores..."
PatternGamePleaseWait = "Aguarde..."
PatternGameFaster = "Voc\xc3\xaa foi\nmais rápido!"
PatternGameFastest = "Voc\xc3\xaa foi o\nmais rápido!"
PatternGameYouCanDoIt = "Deixa disso!\nVoc\xc3\xaa consegue!"
PatternGameOtherFaster = "\nfoi mais rápido!"
PatternGameOtherFastest = "\nfoi o mais rápido!"
PatternGameGreatJob = "Muito bom!"
PatternGameRound = "Rodada %s!" # Round 1! Round 2! ..
PatternGameImprov = "Voc\xc3\xaa foi muito bem! Agora Melhore!"

# DistributedRaceGame.py
RaceGameTitle = "Jogo de corrida"
RaceGameInstructions = "Clique em um número. Escolha bem! Voc\xc3\xaa só avançará se ninguém mais escolher o mesmo número."
RaceGameWaitingChoices = "Esperando os outros jogadores escolherem..."
RaceGameCardText = "%(name)s aposta: %(reward)s"
RaceGameCardTextBeans = "%(name)s recebe: %(reward)s"
RaceGameCardTextHi1 = "%(name)s é um Toon fabuloso!"  # this category might eventually have secret game hints, etc

# RaceGameGlobals.py
RaceGameForwardOneSpace    = " avança 1 espaço"
RaceGameForwardTwoSpaces   = " avança 2 espaços"
RaceGameForwardThreeSpaces = " avança 3 espaços"
RaceGameBackOneSpace    = " recua 1 espaço"
RaceGameBackTwoSpaces   = " recua 2 espaços"
RaceGameBackThreeSpaces = " recua 3 espaços"
RaceGameOthersForwardThree = " todos os outros avançam \n3 espaços"
RaceGameOthersBackThree = "todos os outros recuam \n3 espaços"
RaceGameInstantWinner = "Vencedor imediato!"
RaceGameJellybeans2 = "2 balinhas"
RaceGameJellybeans4 = "4 balinhas"
RaceGameJellybeans10 = "10 balinhas!"

# DistributedRingGame.py
RingGameTitle = "Jogo dos anéis"
# color
RingGameInstructionsSinglePlayer = "Tente nadar através do número máximo de anéis %s que conseguir. Para nadar, use as teclas de seta."
# color
RingGameInstructionsMultiPlayer = "Tente nadar através dos anéis %s. Os outros jogadores tentarão nadar através dos outros anéis coloridos. Para nadar, use as teclas de seta."
RingGameMissed = "PERDEU"
RingGameGroupPerfect = "GRUPO\nPERFEITO!!"
RingGamePerfect = "PERFEITO!"
RingGameGroupBonus = "B\xc3\x94NUS DO GRUPO"

# RingGameGlobals.py
ColorRed = "vermelhos"
ColorGreen = "verdes"
ColorOrange = "laranja"
ColorPurple = "lilases"
ColorWhite = "brancos"
ColorBlack = "pretos"
ColorYellow = "amarelos"

# DistributedDivingGame.py #localize
DivingGameTitle = "Mergulho pro Tesouro"
# color
DivingInstructionsSinglePlayer = "Tesouros irão aparecer no fundo do lago. Use as setas para nadar. Evite os peixes e leve os tesouros para o barco!"
# color
DivingInstructionsMultiPlayer = " Tesouros irão aparecer no fundo do lago. Use as setas para nadar. Trabalhem juntos para levar os tesouros para o barco!"
DivingGameTreasuresRetrieved = "Tesouros Recuperados"

#Distributed Target Game
TargetGameTitle = "Estilingue do Toon"
TargetGameInstructionsSinglePlayer = "Acerta na velocidade do alvo"
TargetGameInstructionsMultiPlayer = "Acerta quantos alvos conseguir"
TargetGameBoard = "Rodada %s - Mantendo o Melhor Placar"
TargetGameCountdown = "Lançamento forçado em %s segundos"
TargetGameCountHelp = "Bata nas setas esquerda e direita para conseguir pot\xc3\xaancia, pare para lançar"
TargetGameFlyHelp = "Aperte para baixo para abrir o guarda-chuva"
TargetGameFallHelp = "Use as teclas de seta para aterrissar no alvo"
TargetGameBounceHelp = " Bater e quicar pode tirar voc\xc3\xaa do alvo"

#Distributed Photo Game
PhotoGameScoreTaken = "%s: %s\nVoc\xc3\xaa: %s"
PhotoGameScoreBlank = "Placar: %s"
PhotoGameScoreOther = "\n%s"#"Placar: %s\n%s"
PhotoGameScoreYou = "\nMelhor Bônus!"#"Placar: %s\nMelhor Bônus!"


# DistributedTagGame.py
TagGameTitle = "Jogo de pique"
TagGameInstructions = "Pegue os tesouros. Voc\xc3\xaa não pode pegar os tesouros se o pique estiver com voc\xc3\xaa!"
TagGameYouAreIt = "Está com voc\xc3\xaa!"
TagGameSomeoneElseIsIt = "Está com %s!"

# DistributedMazeGame.py
MazeGameTitle = "Jogo do labirinto"
MazeGameInstructions = "Pegue os tesouros. Tente pegar todos, mas cuidado com os "+ Cogs +"!"# DistributedCatchGame.py

# DistributedCatchGame.py
CatchGameTitle = "Jogo de pegar"
CatchGameInstructions = "Pegue o máximo de %(fruit)s que conseguir. Cuidado com os "+ Cogs +" e tente não 'pegar' nenhuma %(badThing)s!"
CatchGamePerfect = "PERFEITO!"
CatchGameApples      = 'maçãs'
CatchGameOranges     = 'laranjas'
CatchGamePears       = 'p\xc3\xaaras'
CatchGameCoconuts    = 'cocos'
CatchGameWatermelons = 'melancias'
CatchGamePineapples  = 'abacaxis'
CatchGameAnvils      = 'bigornas'

# DistributedPieTossGame.py
PieTossGameTitle = "Jogo de lançamento de tortas"
PieTossGameInstructions = "Lance as tortas nos alvos."

# DistributedPhotoGame.py
PhotoGameInstructions = "Tire fotos de acordo com os Toons mostrados na parte de baixo. Mire a câmera usando o mouse, e clique com o botão esquerdo para tirar uma foto. Aperte Ctrl para aumentar ou reduzir o zoom, e olhe em sua volta com as teclas de seta. Fotos com notas maiores ganham mais pontos!"
PhotoGameTitle = "Diversão Fotográfica"
PhotoGameFilm = "FILME"
PhotoGameScore = "Placar da Equipe: %s\n\nMelhores Fotos: %s\n\nPlacar Total: %s"

# DistributedCogThiefGame.py
CogThiefGameTitle = Cog + " Ladrão"
CogThiefGameInstructions = "Impeça que os " + Cogs + " roubem nossos barris! Aperte a tecla Ctrl para atirar uma torta. Use as teclas de seta para se mover. Dica: voc\xc3\xaa pode andar nas diagonais."
CogThiefBarrelsSaved = "%(num)d Barris\nSalvos!"
CogThiefBarrelSaved = "%(num)d Barril\nSalvo!"
CogThiefNoBarrelsSaved = "Nenhum Barril\nSalvo"
CogThiefPerfect = "PERFEITO!!"

# MinigameRulesPanel.py
MinigameRulesPanelPlay = "JOGAR"

# Purchase.py
GagShopName = "Loja de Piadas do Pateta"
GagShopPlayAgain = "JOGAR\nNOVAMENTE"
GagShopBackToPlayground = "SAIR DE NOVO \nPARA O P\xc3\x81TIO"
GagShopYouHave = "Voc\xc3\xaa tem %s balinhas para gastar"
GagShopYouHaveOne = "Voc\xc3\xaa tem 1 balinha para gastar"
GagShopTooManyProps = "Sinto muito, voc\xc3\xaa tem muitos acessórios"
GagShopDoneShopping = "FIM DAS\nCOMPRAS"
# name of a gag
GagShopTooManyOfThatGag = "Sinto muito, voc\xc3\xaa já tem %s o suficiente"
GagShopInsufficientSkill = "Voc\xc3\xaa não tem muita habilidade para isso ainda"
# name of a gag
GagShopYouPurchased = "Voc\xc3\xaa comprou %s"
GagShopOutOfJellybeans = "Sinto muito, voc\xc3\xaa não tem mais balinhas!"
GagShopWaitingOtherPlayers = "Aguardando outros jogadores..."
# these show up on the avatar panels in the purchase screen
GagShopPlayerDisconnected = "%s desconectou-se"
GagShopPlayerExited = "%s saiu"
GagShopPlayerPlayAgain = "Jogar novamente"
GagShopPlayerBuying = "Comprando"

# MakeAToon.py
GenderShopQuestionMickey = "Para criar um Toon menino, clique em mim!"
GenderShopQuestionMinnie = "Para criar um Toon menina, clique em mim!"
GenderShopFollow = "Siga-me!"
GenderShopSeeYou = "Vejo voc\xc3\xaa depois!"
GenderShopBoyButtonText = "Menino"
GenderShopGirlButtonText = "Menina"

# BodyShop.py
BodyShopHead = "Cabeça"
BodyShopBody = "Corpo"
BodyShopLegs = "Pernas"

# ColorShop.py
ColorShopHead = "Cabeça"
ColorShopBody = "Corpo"
ColorShopLegs = "Pernas"
ColorShopToon = "Toon"
ColorShopParts = "Partes"
ColorShopAll = "Tudo"

# ClothesShop.py
ClothesShopShorts = "Short"
ClothesShopShirt = "Camisa"
ClothesShopBottoms = "Parte de baixo"

# MakeAToon
PromptTutorial = "Parabéns!\nVoc\xc3\xaa é o(a) mais recente morador(a) de Toontown!\n\nDeseja continuar com o Toontorial ou teletransportar-se diretamente para o Centro de Toontown?"
MakeAToonSkipTutorial = "Pular Toontorial"
MakeAToonEnterTutorial = "Acessar Toontorial"
MakeAToonDone = lOK
MakeAToonCancel = lCancel
MakeAToonNext = lNext
MakeAToonLast = 'Voltar'
CreateYourToon = "Clique nas setas para criar o seu Toon."
CreateYourToonTitle = "Crie o seu Toon"
ShapeYourToonTitle = "Selecione o Tipo"
PaintYourToonTitle = "Selecione a Cor"
PickClothesTitle = "Selecione as Roupas"
NameToonTitle = "Selecione o Nome"
CreateYourToonHead = "Clique nas setas da 'cabeça' para escolher animais diferentes."
MakeAToonClickForNextScreen = "Clique na seta abaixo para ir até a próxima tela."
PickClothes = "Clique nas setas para escolher roupas!"
PaintYourToon = "Clique nas setas para pintar o seu toon!"
MakeAToonYouCanGoBack = "Voc\xc3\xaa pode voltar para alterar o corpo também!"
MakeAFunnyName = "Escolha um nome engraçado para o seu Toon com o jogo Escolha um nome!"
MustHaveAFirstOrLast1 = "O seu Toon deve ter um nome ou um sobrenome, não é?"
MustHaveAFirstOrLast2 = "Voc\xc3\xaa não quer que o seu Toon tenha um nome ou um sobrenome?"
ApprovalForName1 = "\xc3\x89 isso a\xc3\xad, o seu Toon merece um nome muito legal!"
ApprovalForName2 = "Os nomes de Toons são os nomes mais legais que existem!"
MakeAToonLastStep = "\xc3\x9altima etapa antes de ir para Toontown!"
PickANameYouLike = "Escolha o nome que quiser!"
TitleCheckBox = "T\xc3\xadtulo"
FirstCheckBox = "Primeiro"
LastCheckBox = "\xc3\x9altimo"
RandomButton = "Aleatório"
ShuffleButton = "Misturar"
NameShopSubmitButton = "Enviar"
TypeANameButton = "Digite um nome"
TypeAName = "Não gostou destes nomes?\nClique aqui -->"
PickAName = "Tente usar o jogo Escolha um nome!\nClique aqui -->"
PickANameButton = "Escolha um nome"
RejectNameText = "Este nome não é permitido. Tente novamente."
WaitingForNameSubmission = "Enviando o seu nome..."

# PetshopGUI.py
PetNameMaster = "PetNameMaster_portuguese.txt"
PetshopUnknownName = "Nome: ???"
PetNameIndexMAX = 2713
PetshopDescGender = "Sexo:\t%s"
PetshopDescCost = "Custo:\t%s balinhas"
PetshopDescTrait = "Caracter\xc3\xadsticas:\t%s"
PetshopDescStandard = "Padrão"
PetshopCancel = lCancel
PetshopSell = "Vender peixes"
PetshopAdoptAPet = "Adotar um Rabisco"
PetshopReturnPet = "Devolver o Rabisco"
PetshopAdoptConfirm = "Adotar %s por %d balinhas?"
PetshopGoBack = "Voltar"
PetshopAdopt = "Adotar"
PetshopReturnConfirm = "Devolver %s?"
PetshopReturn = "Devolver"
PetshopChooserTitle = "RABISCOS DE HOJE"
PetshopGoHomeText = 'Deseja ir \xc3\xa0 sua propriedade para brincar com seu novo Rabisco?'

# NameShop.py
NameShopNameMaster = "NameMaster_portuguese.txt"
NameShopPay = "Assine já!"
NameShopPlay = "Avaliação gratuita"
NameShopOnlyPaid = "Somente usuários pagantes\npodem dar nomes aos seus Toons.\nAté que voc\xc3\xaa se inscreva,\nseu nome será\n"
NameShopContinueSubmission = "Continuar envio"
NameShopChooseAnother = "Escolha outro nome"
NameShopToonCouncil = "O Conselho de Toons\nanalisará o seu\nnome."+ \
                      "A análise pode\nlevar alguns dias.\nEnquanto voc\xc3\xaa espera,\nseu nome será\n"
PleaseTypeName = "Digite o seu nome:"
AllNewNames = "Todos os novos nomes\ndevem ser aprovados\npelo Conselho de Toons."
NameMessages = "Use sua criatividade e lembre-se:\nnada de nomes relacionados\ncom a Disney, por favor."
NameShopNameRejected = "O nome\nenviado foi\nrejeitado."
NameShopNameAccepted = "Parabéns!\nO nome\nenviado foi\naceito!"
NoPunctuation = "Não é permitido usar caracteres de pontuação nos nomes!"
PeriodOnlyAfterLetter = "Voc\xc3\xaa pode usar um ponto no nome, mas apenas depois de uma letra."
ApostropheOnlyAfterLetter = "Voc\xc3\xaa pode usar um apóstrofo no nome, mas apenas depois de uma letra."
NoNumbersInTheMiddle = "D\xc3\xadgitos numéricos podem não aparecer no meio da palavra."
ThreeWordsOrLess = "Seu nome deve ter tr\xc3\xaas palavras ou menos."
CopyrightedNames = (
    "mickey",
    "mickey mouse",
    "mickeymouse",
    "minnie",
    "minnie mouse",
    "minniemouse",
    "donald",
    "donald duck",
    "donaldduck",
    "pato donald",
    "patodonald",
    "pluto",
    "goofy",
    "pateta",
    )
NumToColor = ['Branco', 'P\xc3\xaassego', 'Vermelho vivo', 'Vermelho', 'Castanho',
              'Siena', 'Marrom', 'Canela', 'Coral', 'Laranja',
              'Amarelo', 'Creme', 'C\xc3\xadtrico', 'Limão', 'Verde-água',
              'Verde', 'Azul-claro', 'Verde-azul', 'Azul',
              'Verde-musgo', 'Azul-turquesa', 'Azul cinzento', 'Lilás',
              'Púrpura', 'Rosa']
AnimalToSpecies = {
    'dog'    : 'Cachorro',
    'cat'    : 'Gato',
    'mouse'  : 'Rato',
    'horse'  : 'Cavalo',
    'rabbit' : 'Coelho',
    'duck'   : 'Pato',
    'monkey' : 'Macaco',
    'bear'   : 'Urso',
    'pig'    : 'Porco'
    }
NameTooLong = "Este nome é muito longo. Tente novamente."
ToonAlreadyExists = "Voc\xc3\xaa já tem um Toon com o nome %s!"
NameAlreadyInUse = "Este nome já foi usado!"
EmptyNameError = "Voc\xc3\xaa deve primeiramente inserir um nome."
NameError = "Sinto muito. Este nome não vai funcionar."

# NameCheck.py
NCTooShort = 'Este nome é muito curto.'
NCNoDigits = 'O nome não pode conter números.'
NCNeedLetters = 'Cada palavra do nome deve conter algumas letras.'
NCNeedVowels = 'Cada palavra do nome deve conter algumas vogais.'
NCAllCaps = 'O seu nome não pode estar todo em maiúsculas.'
NCMixedCase = 'Este nome tem muitas letras em maiúsculas.'
NCBadCharacter = "O seu nome não pode conter o caractere '%s'"
NCGeneric = 'Sinto muito, este nome não vai funcionar.'
NCTooManyWords = 'O seu nome não pode ter mais de quatro palavras.'
NCDashUsage = ("H\xc3\xadfens podem ser usados apenas para ligar duas palavras"
               "(como em 'Bu-Bu').")
NCCommaEdge = "O seu nome não pode começar ou terminar com v\xc3\xadrgula."
NCCommaAfterWord = "Voc\xc3\xaa não pode começar uma palavra com v\xc3\xadrgula."
NCCommaUsage = ('Este nome não usa v\xc3\xadrgulas corretamente. As v\xc3\xadrgulas devem'
                'juntar duas palavras, como no nome "Dr. Quack, MD".'
                'As v\xc3\xadrgulas devem também ser seguidas por um espaço.')
NCPeriodUsage = ('Este nome não usa pontos corretamente. Os pontos são'
                 'permitidos somente em palavras como "Sr.", "Sra.", "J.P.", etc.')
NCApostrophes = 'Este nome tem excesso de apóstrofos.'

# DistributedTrophyMgrAI.py
RemoveTrophy = lToonHQ+": "+TheCogs +" dominaram um dos edif\xc3\xadcios que voc\xc3\xaa salvou!"

from panda3d.core import TextProperties
from panda3d.core import TextPrpertiesManager

# toon\DistributedNPCTailor/Clerk/Fisherman.py
STOREOWNER_TOOKTOOLONG = 'Precisa de mais tempo para pensar?'
STOREOWNER_GOODBYE = 'Vejo voc\xc3\xaa depois!'
STOREOWNER_NEEDJELLYBEANS = 'Voc\xc3\xaa precisa pegar o bondinho para conseguir algumas balinhas.'
STOREOWNER_GREETING = 'Escolha o que deseja comprar.'
STOREOWNER_BROWSING = 'Voc\xc3\xaa pode olhar, mas precisará de um bilhete de roupas para comprar.'
STOREOWNER_NOCLOTHINGTICKET = 'Para comprar roupas, voc\xc3\xaa precisa de um bilhete de roupas.'

STOREOWNER_NOFISH = 'Volte aqui para vender peixes para a loja de animais e ganhar balinhas.'
STOREOWNER_THANKSFISH = 'Valeu! A loja de animais vai adorar estes aqui. Tchau!'
STOREOWNER_THANKSFISH_PETSHOP = "Estes tipos são raros! Valeu."
STOREOWNER_PETRETURNED = "Não se preocupe. Acharemos um bom lar para o seu Rabisco."
STOREOWNER_PETADOPTED = "Parabéns pelo novo Rabisco! Voc\xc3\xaa pode brincar com ele em sua propriedade."
STOREOWNER_PETCANCELED = "Lembre-se, caso veja um Rabisco de seu agrado, adote-o antes que alguém o faça!"

STOREOWNER_NOROOM = "Hmm... Voc\xc3\xaa pode precisar arranjar espaço no seu armário antes de comprar roupas novas.\n"
STOREOWNER_CONFIRM_LOSS = "O seu armário está cheio. Voc\xc3\xaa vai perder as roupas que estava vestindo."
STOREOWNER_OK = lOK
STOREOWNER_CANCEL = lCancel
STOREOWNER_TROPHY = "Uau! Voc\xc3\xaa pegou %s de %s peixe. Merece um troféu e um Acréscimo de risadas!"
# end translate

# NewsManager.py
SuitInvasionBegin1 = lToonHQ+": Foi iniciada uma Invasão de Cogs!!!"
SuitInvasionBegin2 = lToonHQ+": %s dominaram Toontown!!!"
SuitInvasionEnd1 = lToonHQ+": A Invasão de %s terminou!!!"
SuitInvasionEnd2 = lToonHQ+": Mais uma vez os Toons salvaram a pátria!!!"
SuitInvasionUpdate1 = lToonHQ+": A Invasão de Cogs está agora em %s Cogs!!!"
SuitInvasionUpdate2 = lToonHQ+": Precisamos derrotar esses %s!!!"
SuitInvasionBulletin1 = lToonHQ+": Há uma Invasão de Cogs em andamento!!!"
SuitInvasionBulletin2 = lToonHQ+": %s dominaram Toontown!!!"

# DistributedHQInterior.py
LeaderboardTitle = "Pelotão Toon"

# QuestScript.txt
QuestScriptTutorialMickey_1 = "Toontown ganhou um novo cidadão! Voc\xc3\xaa tem piadas de reserva?"
QuestScriptTutorialMickey_2 = "Claro, %s!"
QuestScriptTutorialMickey_3 = "O Tutorial Tom vai contar para voc\xc3\xaa tudo sobre os Cogs.\aTchauzinho!"
QuestScriptTutorialMickey_4 = "Vem cá! Use as teclas de seta para mover-se."

# These are needed to correspond to the Japanese gender specific phrases
QuestScriptTutorialMinnie_1 = "Toontown ganhou um novo cidadão! Voc\xc3\xaa tem piadas de reserva?"
QuestScriptTutorialMinnie_2 = "Claro, %s!"
QuestScriptTutorialMinnie_3 = "O Tutorial Tom vai contar para voc\xc3\xaa tudo sobre os Cogs.\aTchauzinho!"

QuestScript101_1 = "Estes são os COGS. Eles são robôs que estão tentando dominar Toontown."
QuestScript101_2 = "Há vários tipos diferentes de COGS e..."
QuestScript101_3 = "...eles transformam os alegres edif\xc3\xadcios dos Toons..."
QuestScript101_4 = "...em horr\xc3\xadveis edif\xc3\xadcios de Cogs!"
QuestScript101_5 = "Mas os COGS não aguentam piadas!"
QuestScript101_6 = "Uma boa piada os deterá."
QuestScript101_7 = "Há milhares de piadas, mas, para começar, use estas aqui."
QuestScript101_8 = "Ah! Voc\xc3\xaa também vai precisar de um Risômetro!"
QuestScript101_9 = "Se o seu Risômetro estiver baixo, é porque voc\xc3\xaa está triste!"
QuestScript101_10 = "Um Toon feliz é um Toon saudável!"
QuestScript101_11 = "OH N\xc3\x83O! Há um COG na porta da minha loja!"
QuestScript101_12 = "AJUDE-ME, POR FAVOR! Derrote este COG!"
QuestScript101_13 = "Esta é a sua primeira Tarefa Toon!"
QuestScript101_14 = "Vamos nessa! Vá derrotar aquele Puxa-saco!"

QuestScript110_1 = "Bom trabalho; voc\xc3\xaa derrotou aquele Puxa-saco. Deixe-me dar a voc\xc3\xaa um \xc3\x81lbum Toon..."
QuestScript110_2 = "O livro é cheio de coisas legais."
QuestScript110_3 = "Abra-o para eu mostrar a voc\xc3\xaa."
QuestScript110_4 = "O mapa mostra o local onde voc\xc3\xaa esteve."
QuestScript110_5 = "Vire a página para ver as suas piadas..."
QuestScript110_6 = "\xc3\x8apa! Voc\xc3\xaa não tem nenhuma piada! Vou passar uma tarefa para voc\xc3\xaa."
QuestScript110_7 = "Vire a página para ver as suas tarefas."
QuestScript110_8 = "D\xc3\xaa uma volta no bondinho para ganhar balinhas e poder comprar piadas!"
QuestScript110_9 = "Para ir até o bondinho, saia pela porta logo atrás de mim e siga até o pátio."
QuestScript110_10 = "Agora, feche o livro e encontre o bondinho!"
QuestScript110_11 = "Volte para o Quartel dos Toons quando já estiver pronto. Tchau!"

QuestScriptTutorialBlocker_1 = "Oi, e a\xc3\xad, pessoal?"
QuestScriptTutorialBlocker_2 = "Alô?"
QuestScriptTutorialBlocker_3 = "Ah! Voc\xc3\xaa não sabe usar o Chat rápido!"
QuestScriptTutorialBlocker_4 = "Clique no botão para dizer algo."
QuestScriptTutorialBlocker_5 = "Muito bom!\aO local para onde voc\xc3\xaa está indo tem um monte de Toons para conversar."
QuestScriptTutorialBlocker_6 = "Se voc\xc3\xaa quiser conversar com seus amigos usando o teclado, há um outro botão que pode ser usado."
QuestScriptTutorialBlocker_7 = "Isso se chama botão de chat. Voc\xc3\xaa precisa para ligar o Chat Rápido Plus usa conta de pais ou assine Seja um Super Toon no Web site do Toontown para usar isso."
QuestScriptTutorialBlocker_8 = "Boa sorte! Vejo voc\xc3\xaa depois!"

"""
GagShopTut

You will also earn the ability to use other types of gags.

"""

QuestScriptGagShop_1 = "Bem-vindo \xc3\xa0 Loja de Piadas!"
QuestScriptGagShop_1a = "Aqui é o lugar onde os Toons v\xc3\xaam comprar piadas para usar contra os Cogs."
#QuestScriptGagShop_2 = "Este pote mostra quantas balinhas voc\xc3\xaa tem."
#QuestScriptGagShop_3 = "Para comprar piadas, clique em botões de piada. Tente pegar umas agora!"
QuestScriptGagShop_3 = "Para comprar piadas, clique em botões de piada. Tente pegar algumas agora!"
QuestScriptGagShop_4 = "Bom! Voc\xc3\xaa pode usar estas piadas nas batalhas contra os Cogs."
QuestScriptGagShop_5 = "D\xc3\xaa uma olhada para ver como são as piadas avançadas de jogar e de esguichar..."
QuestScriptGagShop_6 = "Depois que terminar de comprar piadas, clique neste botão para retornar ao Pátio."
QuestScriptGagShop_7 = "Normalmente, voc\xc3\xaa pode usar este botão para participar de outro Jogo no Bondinho..."
QuestScriptGagShop_8 = "...Mas não há tempo para outro jogo agora. Estão precisando de voc\xc3\xaa no Quartel dos Toons!"

QuestScript120_1 = "Muito bem, voc\xc3\xaa encontrou o bondinho!\aPor falar nisso, voc\xc3\xaa encontrou o Banqueiro Beto?\aEle é bem guloso por doces.\aPor que voc\xc3\xaa não se apresenta e leva para ele este chocolate de presente."
QuestScript120_2 = "O Banqueiro Beto está lá no Banco de Toontown."

QuestScript121_1 = "Mmm, obrigado pelo chocolate.\aOlha só, se voc\xc3\xaa me ajudar, eu dou a voc\xc3\xaa uma recompensa.\aEsses Cogs roubaram as chaves do meu cofre. Derrote os Cogs para encontrar a chave roubada.\aQuando voc\xc3\xaa encontra-la, traga-a para mim."

QuestScript130_1 = "Muito bem, voc\xc3\xaa encontrou o bondinho!\aPor falar nisso, recebi hoje um pacote para o Professor Paulo.\aDeve ser o novo giz que ele encomendou.\aVoc\xc3\xaa pode, por favor, levar para ele?\aEle está lá na escola."

QuestScript131_1 = "Ah, obrigado pelo giz.\aO qu\xc3\xaa?!?\aEsses Cogs roubaram meu quadro-negro. Derrote os Cogs para encontrar meu quadro-negro roubado.\aQuando encontrá-lo, traga de volta para mim."

QuestScript140_1 = "Muito bem, voc\xc3\xaa encontrou o bondinho!\aPor falar nisso, tenho um amigo, o Bibliotecário Bino, que é uma verdadeira traça de livros.\aPeguei este livro para ele da última vez em que estive no Porto do Donald.\aVoc\xc3\xaa podia levar para ele? Em geral, ele fica na Biblioteca."

QuestScript141_1 = "Ah, sim, este livro vai quase completar a minha coleção.\aDeixe-me ver...\a\xc3\x8apa...\aOnde é que eu pus os meus óculos agora?\aEu estava com eles um pouco antes de aqueles Cogs invadirem o meu edif\xc3\xadcio.\aDerrote os Cogs para encontrar meus óculos roubados.\aaQuando encontrá-los, traga de volta para mim para ganhar uma recompensa."

QuestScript145_1 = "Estou vendo que voc\xc3\xaa não teve problemas com o bondinho!\a Olha só, os Cogs roubaram o apagador do nosso quadro-negro.\a Vá para as ruas e lute com os Cogs até recuperar o apagador.\a Para encontrar as ruas, passe por um dos túneis como este:"
QuestScript145_2 = "Quando encontrar nosso apagador, traga-o de volta para cá.\aNão se esqueça, se precisar de piadas, pegue o bondinho.\aE se voc\xc3\xaa precisar recuperar Pontos de risadas, colete casquinhas de sorvete no Pátio."

QuestScript150_1 = "Ah... Esta próxima tarefa talvez seja muito dif\xc3\xadcil para voc\xc3\xaa executar sozinho!"
QuestScript150_2 = "Para fazer amigos, encontre outro jogador e use o botão Novo amigo."
QuestScript150_3 = "Depois que voc\xc3\xaa tiver arrumado um amigo, volte aqui."
QuestScript150_4 = "Algumas tarefas são muito dif\xc3\xadceis de serem executadas sem ajuda!"

# To make sure the language checker is working
# DO NOT TRANSLATE THIS
MissingKeySanityCheck = "Ignore-me"

SellbotBossName = "V. P. S\xc3\xaanior"
CashbotBossName = "Diretor Financeiro"
LawbotBossName = "Juiz-Chefe"
BossCogNameWithDept = "%(name)s\n%(dept)s"
BossCogPromoteDoobers = "Com isto, voc\xc3\xaa está promovido a %s s\xc3\xaanior. Parabéns!"
BossCogDoobersAway = { 's' : "Vai! E faça essa venda!" }
BossCogWelcomeToons = "Bem-vindos, novos Cogs!"
BossCogPromoteToons = "Com isto, voc\xc3\xaa está promovido a %s s\xc3\xaanior. Parab--"
CagedToonInterruptBoss = "Oi! Uhuu! E a\xc3\xad pessoal!"
CagedToonRescueQuery = "Então, galera de Toons, voc\xc3\xaas v\xc3\xaam me salvar?"
BossCogDiscoverToons = "Hã? Toons! Disfarçar!"
BossCogAttackToons = "Atacar!!"
CagedToonDrop = [
    "Bom trabalho! Ele está ficando exausto!",
    "Fique atrás dele! Ele está fugindo!",
    "Pessoal, voc\xc3\xaas estão se saindo muito bem!",
    "Fantástico! Voc\xc3\xaa quase o pegou agora!",
    ]
CagedToonPrepareBattleTwo = "Cuidado, ele está tentando escapar!\aAjudem-me todos! Levantem-se aqui e detenham-no!"
CagedToonPrepareBattleThree = "Maneiro! Estou quase livre!\aAgora, voc\xc3\xaa precisa atacar o Cog V. P. em pessoa.\aTenho um montão de tortas que voc\xc3\xaa pode usar!\aPule e toque na parte inferior da minha cela para que eu lhe d\xc3\xaa algumas tortas.\aPressione a tecla Insert para jogar as tortas quando voc\xc3\xaa as pegar!"
BossBattleNeedMorePies = "Voc\xc3\xaa precisa de mais tortas!"
BossBattleHowToGetPies = "Pule para tocar na cela e pegar mais tortas."
BossBattleHowToThrowPies = "Pressione a tecla Insert para jogar tortas!"
CagedToonYippee = "Iupii!!"
CagedToonThankYou = "\xc3\x89 ótimo estar livre!\aObrigado por toda a sua ajuda!\aTe devo esta.\aSe, por acaso, voc\xc3\xaa estiver em apuros em alguma batalha, é só me chamar!\aBasta clicar no botão SOS para me chamar."
CagedToonPromotion = "\aOlha só! Aquele Cog V.P. acabou deixando aqui os seus documentos de promoção.\aVou arquivá-los para voc\xc3\xaa na sa\xc3\xadda, para que pegue a promoção!"
CagedToonLastPromotion = "\aUau, voc\xc3\xaa atingiu o n\xc3\xadvel %s no processo Cog!\aOs Cogs não t\xc3\xaam promoção maior do que esta.\aVoc\xc3\xaa não pode mais subir no processo Cog, mas certamente pode continuar salvando os Toons!"
CagedToonHPBoost = "\aVoc\xc3\xaa salvou um monte de Toons neste quartel.\aO Conselho de Toons decidiu dar a voc\xc3\xaa outro Ponto de risadas. Parabéns!"
CagedToonMaxed = "\aVi que voc\xc3\xaa tem o n\xc3\xadvel %s no processo Cog. Impressionante!\aEm nome do Conselho de Toons, agradeço por retornar para salvar mais Toons!"
CagedToonGoodbye = "Te vejo por a\xc3\xad!"


CagedToonBattleThree = {
    10: "Belo salto, %(toon)s. Tome aqui algumas tortas!",
    11: "Oi, %(toon)s! Pegue algumas tortas!",
    12: "E a\xc3\xad, %(toon)s? Agora, voc\xc3\xaa tem algumas tortas!",

    20: "Olá, %(toon)s! Pule até a minha cela e pegue algumas tortas para jogar!",
    21: "Oi, %(toon)s! Use a tecla Ctrl para pular e tocar a minha cela!",

    100: "Pressione a tecla Insert para jogar uma torta.",
    101: "O medidor de pot\xc3\xaancia azul mostra a altura que a sua torta atinge.",
    102: "Primeiramente, tente jogar uma torta dentro da lataria dele para melecar seus mecanismos.",
    103: "Espere até que a porta se abra para jogar uma torta bem lá dentro.",
    104: "Quando ele estiver tonto, bata na cara ou no peito dele para empurrá-lo para trás!",
    105: "Voc\xc3\xaa saberá se o seu golpe foi bom quando vir o chão colorido.",
    106: "Se voc\xc3\xaa atingir um Toon com uma torta, ele ganhará um Ponto de risadas!",
    }
CagedToonBattleThreeMaxGivePies = 12
CagedToonBattleThreeMaxTouchCage = 21
CagedToonBattleThreeMaxAdvice = 106

CashbotBossHadEnough = "\xc3\x89 isso a\xc3\xad! Chega desses Toons irritantes!"
CashbotBossOuttaHere = "Tenho que pegar o trem!"
ResistanceToonName = "Mata Rara"
ResistanceToonCongratulations = "Voc\xc3\xaa conseguiu! Parabéns!\aVoc\xc3\xaa é um orgulho para a Resist\xc3\xaancia!\aEsta é uma frase especial que voc\xc3\xaa pode usar quando estiver em apuros:\a%s\aQuando voc\xc3\xaa a pronunciar, %s.\aMas só pode usar uma vez, portanto, escolha a hora certa!"
ResistanceToonToonupInstructions = "todos os Toons próximos a voc\xc3\xaa ganham %s pontos de risadas"
ResistanceToonToonupAllInstructions = "todos os Toons próximos a voc\xc3\xaa ganham pontos de risadas completos"
ResistanceToonMoneyInstructions = "todos os Toons próximos a voc\xc3\xaa ganham %s balinhas"
ResistanceToonMoneyAllInstructions = "todos os Toons próximos a voc\xc3\xaa encherão suas jarras de balinhas"
ResistanceToonRestockInstructions = "todos os Toons próximos a voc\xc3\xaa vão reabastecer suas \"%s\" piadas"
ResistanceToonRestockAllInstructions = "todos os Toons próximos a voc\xc3\xaa vão reabastecer todas as suas piadas"

ResistanceToonLastPromotion = "\aUau, voc\xc3\xaa atingiu o n\xc3\xadvel %s no processo Cog!\aOs Cogs não t\xc3\xaam promoção maior do que esta.\aVoc\xc3\xaa não pode mais subir no processo Cog, mas, certamente, pode continuar trabalhando para a Resist\xc3\xaancia!"
ResistanceToonHPBoost = "\aVoc\xc3\xaa trabalhou muito para a Resist\xc3\xaancia.\aO Conselho de Toons decidiu dar a voc\xc3\xaa outro Ponto de risadas. Parabéns!"
ResistanceToonMaxed = "\aVejo que voc\xc3\xaa tem o n\xc3\xadvel %s no processo Cog. Impressionante!\aEm nome do Conselho de Toons, agradeço por retornar para salvar mais Toons!"

CashbotBossCogAttack = "Peguem-nos!!!"
ResistanceToonWelcome = "Voc\xc3\xaa conseguiu! Siga-me até o cofre-forte antes que o Diretor Financeiro nos ache!"
ResistanceToonTooLate = "Droga! Estamos atrasados demais!"
CashbotBossDiscoverToons1 = "Ah-HAH!"
CashbotBossDiscoverToons2 = "Pensei ter farejado um tooninho por aqui! Impostores!"
ResistanceToonKeepHimBusy = "Mantenha-o ocupado! Vou montar uma armadilha!"
ResistanceToonWatchThis = "Olha isso!"
CashbotBossGetAwayFromThat = "Ei! Afaste-se!"
ResistanceToonCraneInstructions1 = "Controle um \xc3\xadmã subindo no pódio."
ResistanceToonCraneInstructions2 = "Use as teclas de setas para mover o guindaste e pressione a tecla Ctrl para pegar um objeto."
ResistanceToonCraneInstructions3 = "Pegue um cofre com o \xc3\xadmã e arranque o capacete de segurança do Diretor Financeiro."
ResistanceToonCraneInstructions4 = "Depois de fazer zunir o capacete, pegue um brutamontes desativado e d\xc3\xaa uma pancada na cabeça dele!"
ResistanceToonGetaway = "Ih! Tenho que correr!"
CashbotCraneLeave = "Deixar o guindaste"
CashbotCraneAdvice = "Use as teclas de setas para mover o guindaste de pórtico."
CashbotMagnetAdvice = "Mantenha pressionada a tecla Ctrl para pegar os objetos."
CashbotCraneLeaving = "Deixando o guindaste"

MintElevatorRejectMessage = "Não será poss\xc3\xadvel entrar na Casa da Moeda até que a vestimenta de Cog %s esteja completa."
BossElevatorRejectMessage = "Voc\xc3\xaa não pode pegar este elevador até que tenha recebido uma promoção."
NotYetAvailable = "Este elevador ainda não está dispon\xc3\xadvel."

SellbotRentalSuitMessage = 'Use este Traje de Cog Alugado para que possa se aproximar o suficiente do VP para atacá-lo.\n\nVoc\xc3\xaa não receberá méritos ou promoções, mas pode resgatar um Toon para uma recompensa SOS!'
SellbotCogSuitNoMeritsMessage = 'Seu disfarce de Robô Vendedor o levará para dentro, mas uma vez que não tem méritos suficientes, voc\xc3\xaa não será promovido.\n\nSe resgatar o Toon encurralado, voc\xc3\xaa ganhará uma recompensa SOS Toon!'
SellbotCogSuitHasMeritsMessage = '\xc3\x89 a Operação: Robô Vendedor Tempestade!\n\nTraga com voc\xc3\xaa 5 ou mais Toons com Trajes de Cog Alugados para derrotar o VP e ganhe crédito para uma recompensa!'

LawbotRentalSuitMessage = "Wear this Rental Suit so you can get close enough to the CJ to attack.\n\nYou won't earn jury notices or promotions, but you can rescue Bumpy for a summon reward!"
LawbotCogSuitNoMeritsMessage = "Your Lawbot Disguise will get you in, but since you don't have enough jury notices, you won't earn a promotion.\n\nIf you rescue Bumpy, you will earn a summon reward!"
LawbotCogSuitHasMeritsMessage = "It's Operation: Lawbots Lose!\n\nBring 5 or more Rental Suit Toons with you to defeat the CJ and earn credit towards a reward!"

# Types of catalog items--don't translate yet.
FurnitureTypeName = "Mob\xc3\xadlia"
PaintingTypeName = "Pintura"
ClothingTypeName = "Roupas"
ChatTypeName = "Frase do Chat rápido"
EmoteTypeName = "Aulas de representação"
BeanTypeName = "Balinhas"
PoleTypeName = "Vara de pescar"
WindowViewTypeName = "Vista da janela"
PetTrickTypeName = 'Treinamento de Rabiscos'
GardenTypeName = 'Materiais de Jardim'
RentalTypeName = 'Item de Aluguel'
GardenStarterTypeName = 'Kit de Jardinagem'
NametagTypeName = "Crachá"
AccessoryTypeName = "Acessório"


# Make sure numbers match up to CatalogItemTypes.py
CatalogItemTypeNames = {
    0 : "INVALID_ITEM",
    1 : FurnitureTypeName,
    2 : ChatTypeName,
    3 : ClothingTypeName,
    4 : EmoteTypeName,
    5 : "WALLPAPER",
    6 : "Window View",
    7 : "FLOORING",
    8 : "MOULDING",
    9 : "WAINSCOTING",
    10: PoleTypeName,
    11: PetTrickTypeName,
    12: BeanTypeName,
    13: GardenTypeName,
    14: RentalTypeName,
    15: GardenStarterTypeName,
    16: NametagTypeName,
    17: "TOON_STATUE",
    18: "ANIMATED FURNITURE",
    19: AccessoryTypeName,
}


ChapéuStylesDescriptions = {
    'hbb1' : "Boné de Baseball Verde",
    'hbb2' : "Boné de Baseball Azul",
    'hbb3' : "Boné de Baseball Laranja",
    'hsf1' : "Beige Safari Chapéu",
    'hsf2' : "Brown Safari Chapéu",
    'hsf3' : "Green Safari Chapéu",
    'hrb1' : "Pink Bow",
    'hrb2' : "Red Bow",
    'hrb3' : "Purple Bow",
    'hht1' : "Pink Heart",
    'hht2' : "Yellow Heart",
    'htp1' : "Black Top Chapéu",
    'htp2' : "Blue Top Chapéu",
    'hav1' : "Anvil Chapéu",
    'hfp1' : "Flower Chapéu",
    'hsg1' : "Sandbag Chapéu",
    'hwt1' : "Weight Chapéu",
    'hfz1' : "Fez Chapéu",
    'hgf1' : "Golf Chapéu",
    'hpt1' : "Party Chapéu",
    'hpt2' : "Toon Party Chapéu",
    'hpb1' : "Fancy Chapéu",
    'hcr1' : "Crown",
    'hcw1' : "Cowboy Chapéu",
    'hpr1' : "Pirate Chapéu",
    'hpp1' : "Propeller Chapéu",
    'hfs1' : "Fishing Chapéu",
    'hsb1' : "Sombrero Chapéu",
    'hst1' : "Straw Chapéu",
    'hsu1' : "Sun Chapéu",
    'hrb4' : "Yellow Bow",
    'hrb5' : "Checker Bow",
    'hrb6' : "Light Red Bow",
    'hrb7' : "Rainbow Bow",
    'hat1' : "Antenna Thingy",
    'hhd1' : "Beehive Hairdo",
    'hbw1' : "Bowler Chapéu",
    'hch1' : "Chef Chapéu",
    'hdt1' : "Detective Chapéu",
    'hft1' : "Fancy Feathers Chapéu",
    'hfd1' : "Fedora",
    'hmk1' : "Mickey's Band Chapéu",
    'hft2' : "Feather Headband",
    'hhd2' : "Pompadour Hairdo",
    'hpc1' : "Princess Chapéu",
    'hrh1' : "Archer Chapéu",
    'hhm1' : "Roman Helmet",
    'hat2' : "Spider Antenna Thingy",
    'htr1' : "Tiara",
    'hhm2' : "Viking Helmet",
    'hwz1' : "Witch Chapéu",
    'hwz2' : "Wizard Chapéu",
    'hhm3' : "Conquistador Helmet",
    'hhm4' : "Firefighter Helmet",
    'hfp2' : "Anti-Cog Control Chapéu",
    'hhm5' : "Miner Chapéu",
    'hnp1' : "Napoleon Chapéu",
    'hpc2' : "Pilot Cap",
    'hph1' : "Cop Chapéu",
    'hwg1' : "Rainbow Wacky Wig",
    'hbb4' : "Yellow Boné de Baseball",
    'hbb5' : "Red Boné de Baseball",
    'hbb6' : "Aqua Boné de Baseball",
    'hsl1' : "Sailor Chapéu",
    'hfr1' : "Samba Chapéu",
    'hby1' : "Bobby Chapéu",
    'hrb8' : "Pink Dots Bow",
    'hjh1' : "Jester Chapéu",
    'hbb7' : "Boné de Baseball Roxo",
    'hrb9' : "Green Checker Bow",
    'hwt2' : "Winter Chapéu",
    'hhw1' : "Bandana",
    'hhw2' : "Toonosaur Chapéu",
    'hob1' : "Jamboree Chapéu",
    'hbn1' : "Bird Chapéu by Brianna",
    }

GlassesStylesDescriptions = {
    'grd1' : "Round Glasses",
    'gmb1' : "White Mini Blinds",
    'gnr1' : "Purple Narrow Glasses",
    'gst1' : "Yellow Star Glasses",
    'g3d1' : "Movie Glasses",
    'gav1' : "Aviator",
    'gce1' : "Cateye Glasses",
    'gdk1' : "Nerd Glasses",
    'gjo1' : "Celebrity Shades",
    'gsb1' : "Scuba Mask",
    'ggl1' : "Goggles",
    'ggm1' : "Groucho Glasses",
    'ghg1' : "Heart Glasses",
    'gie1' : "Bug Eye Glasses",
    'gmt1' : "Black Secret ID Mask",
    'gmt2' : "Blue Secret ID Mask",
    'gmt3' : "Blue Carnivale Mask",
    'gmt4' : "Purple Carnivale Mask",
    'gmt5' : "Aqua Carnivale Mask",
    'gmn1' : "Monocle",
    'gmo1' : "Smooch Glasses",
    'gsr1' : "Square Frame Glasses",
    'ghw1' : "Skull Eyepatch",
    'ghw2' : "Gem Eyepatch",
    'gag1' : "Alien Eyes by Alexandra",
    }

BackpackStylesDescriptions = {
    'bpb1' : "Blue Backpack",
    'bpb2' : "Orange Backpack",
    'bpb3' : "Purple BackPack",
    'bpd1' : "Red Dot Backpack",
    'bpd2' : "Yellow Dot Backpack",
    'bwg1' : "Bat Wings",
    'bwg2' : "Bee Wings",
    'bwg3' : "DragonFly Wings",
    'bst1' : "Scuba Tank",
    'bfn1' : "Shark Fin",
    'baw1' : "White Angel Wings",
    'baw2' : "Rainbow Angel Wings",
    'bwt1' : "Toys Backpack",
    'bwg4' : "Butterfly Wings",
    'bwg5' : "Pixie Wings",
    'bwg6' : "Dragon Wings",
    'bjp1' : "Jet Pack",
    'blg1' : "Bug Backpack",
    'bsa1' : "Plush Bear Pack",
    'bwg7' : "Bird wings",
    'bsa2' : "Plush Cat Pack",
    'bsa3' : "Plush Dog Pack",
    'bap1' : "Airplane Wings",
    'bhw1' : "Pirate Sword",
    'bhw2' : "Super Toon Cape",
    'bhw3' : "Vampire Cape",
    'bhw4' : "Toonosaur Backpack",
    'bob1' : "Jamboree Pack",
    'bfg1' : "Gag Attack Pack",
    'bfl1' : "Cog Pack by Savanah",
    }

ShoesStylesDescriptions = {
    'sat1' : "Green Athletic Shoes",
    'sat2' : "Red Athletic Shoes",
    'smb1' : "Green Toon Boots",
    'scs1' : "Green Sneakers",
    'swt1' : "Wingtips",
    'smj1' : "Black Fancy Shoes",
    'sdk1' : "Boat Shoes",
    'sat3' : "Yellow Athletic Shoes",
    'scs2' : "Black Sneakers",
    'scs3' : "White Sneakers",
    'scs4' : "Pink Sneakers",
    'scb1' : "Cowboy Boots",
    'sfb1' : "Purple Boots",
    'sht1' : "Green Hi Top Sneakers",
    'smj2' : "Brown Fancy Shoes",
    'smj3' : "Red Fancy Shoes",
    'ssb1' : "Red Super Toon Boots",
    'sts1' : "Green Tennis Shoes",
    'sts2' : "Pink Tennis Shoes",
    'scs5' : "Red Sneakers",
    'smb2' : "Aqua Toon Boots",
    'smb3' : "Brown Toon Boots",
    'smb4' : "Yellow Toon Boots",
    'sfb2' : "Blue Square Boots",
    'sfb3' : "Green Hearts Boots",
    'sfb4' : "Gray Dots Boots",
    'sfb5' : "Orange Stars Boots",
    'sfb6' : "Pink Stars Boots",
    'slf1' : "Loafers",
    'smj4' : "Purple Fancy Shoes",
    'smt1' : "Motorcycle Boots",
    'sox1' : "Oxfords",
    'srb1' : "Pink Rain Boots",
    'sst1' : "Jolly Boots",
    'swb1' : "Beige Winter Boots",
    'swb2' : "Pink Winter Boots",
    'swk1' : "Work Boots",
    'scs6' : "Yellow Sneakers",
    'smb5' : "Pink Toon Boots",
    'sht2' : "Pink Hi Top Sneakers",
    'srb2' : "Red Dots Rain Boots",
    'sts3' : "Purple Tennis Shoes",
    'sts4' : "Violet Tennis Shoes",
    'sts5' : "Yellow Tennis Shoes",
    'srb3' : "Blue Rain Boots",
    'srb4' : "Yellow Rain Boots",
    'sat4' : "Black Athletic Shoes",
    'shw1' : "Pirate Shoes",
    'shw2' : "Toonosaur Feet",
    }

AccessoryNamePrefix = {
    0 : "hat unisex ",
    1 : "glasses unisex ",
    2 : "backpack unisex ",
    3 : "shoes unisex ",
    4 : "hat boy ",
    5 : "glasses boy ",
    6 : "backpack boy ",
    7 : "shoes boy ",
    8 : "hat girl ",
    9 : "glasses girl ",
    10 : "backpack girl ",
    11 : "shoes girl ",
    }

AwardManagerAccessoryNames = {}
AccessoryTypeNames = {}
for accessoryId in list(CatalogAccessoryItemGlobals.AccessoryTypes.keys()):
    accessoryInfo = CatalogAccessoryItemGlobals.AccessoryTypes[accessoryId]
    if accessoryInfo[0] % 4 == 0:
        accessoryStyleDescription = ChapéuStylesDescriptions
    elif accessoryInfo[0] % 4 == 1:
        accessoryStyleDescription = GlassesStylesDescriptions
    elif accessoryInfo[0] % 4 == 2:
        accessoryStyleDescription = BackpackStylesDescriptions
    else:
        accessoryStyleDescription = ShoesStylesDescriptions
    if accessoryInfo[3]:
        AwardManagerAccessoryNames[accessoryId] = AccessoryNamePrefix[accessoryInfo[0]] + accessoryStyleDescription[accessoryInfo[1]]
    AccessoryTypeNames[accessoryId] = accessoryStyleDescription[accessoryInfo[1]]

# Make sure this is in sync with ToonDNA.ShirtStyles
ShirtStylesDescriptions = {
    # -------------------------------------------------------------------------
    # Boy styles
    # -------------------------------------------------------------------------
    'bss1' : "básica",
    'bss2' : "uma listra",
    'bss3' : "colarinho",
    'bss4' : "duas listras",
    'bss5' : "listrada",
    'bss6' : "colarinho com bolso",
    'bss7' : "havaiana",
    'bss8' : "colarinho com 2 bolsos",
    'bss9' : "camisa de boliche",
    'bss10' : "colete (especial)",
    'bss11' : "colarinho com franzidos",
    'bss12' : "camiseta de futebol (especial)",
    'bss13' : "camiseta lightning bolt (especial)",
    'bss14' : "camiseta 19 (especial)",
    'bss15' : "camisa panamá",

    # -------------------------------------------------------------------------
    # Girl styles
    # -------------------------------------------------------------------------
    'gss1' : "básica",
    'gss2' : "uma listra",
    'gss3' : "colarinho",
    'gss4' : "duas listras",
    'gss5' : "colarinho com bolso",
    'gss6' : "estampa de flor",
    'gss7' : "bordado de flor (especial)",
    'gss8' : "colarinho feminino com 2 bolsos ",
    'gss9' : "colete de brim (especial)",
    'gss10' : "camponesa",
    'gss11' : "camponesa com meia listra",
    'gss12' : "camiseta de futebol (especial)",
    'gss13' : "com corações",
    'gss14' : "com estrelas (especial)",
    'gss15' : "com flores",

    # -------------------------------------------------------------------------
    # Special Catalog-only shirts.
    # -------------------------------------------------------------------------
    # yellow hooded - Series 1
    'c_ss1' : "amarela com capuz - Série 1",
    'c_ss2' : "amarela com palmeira - Série 1",
    'c_ss3' : "roxa com estrelas - Série 2",
    'c_bss1' : "listras azuis (masculina) - Série 1",
    'c_bss2' : "laranja (masculina) - Série 1",
    'c_bss3' : "verde-limão com listra (masculina) - Série 2",
    'c_bss4' : "quimono vermelho com xadrez (masculina) - Série 2",
    'c_gss1' : "azul com listras amarelas (feminina) - Série 1",
    'c_gss2' : "rosa e bege com flor (feminina) - Série 1",
    'c_gss3' : "azul e dourado com listras ondulantes (feminina) - Série 2",
    'c_gss4' : "azul e rosa com arco (feminina) - Série 2",
    'c_gss5' : "quimono azul-piscina com listra (feminina) – N\xc3\x83O USADO",
    'c_ss4'  : "Camiseta tingida (unissex) - Série 3",
    'c_ss5' : "azul-claro com azul e listra branca (masculina) - Série 3",
    'c_ss6' : "camisa de vaqueiro 1 : Série 4",
    'c_ss7' : "camisa de vaqueiro 2 : Série 4",
    'c_ss8' : "camisa de vaqueiro 3 : Série 4",
    'c_ss9' : "camisa de vaqueiro 4 : Série 4",
    'c_ss10' : "camisa de vaqueiro 5 : Série 4",
    'c_ss11' : "camisa de vaqueiro 6 : Série 4",

    # Special Holiday-themed shirts.
    'hw_ss1' : "Fantasma de Halloween",
    'hw_ss2' : "Abóbora de Halloween",
    'hw_ss3' : "Vampiro de Halloween",
    'hw_ss4' : "Tartaruga de Halloween",
    'wh_ss1' : "Feriado de Inverno 1",
    'wh_ss2' : "Feriado de Inverno 2",
    'wh_ss3' : "Feriado de Inverno 3",
    'wh_ss4' : "Feriado de Inverno 4",
    # Translate
    'hw_ss5' : "Halloween Bee",
    'hw_ss6' : "Halloween Pirate",
    'hw_ss7' : "Halloween SuperToon",
    'hw_ss8' : "Halloween Vampire NoCape",
    'hw_ss9' : "Halloween Dinosaur",
    "wh_ss1" : "Feriado de Inverno 1",
    "wh_ss2" : "Feriado de Inverno 2",
    "wh_ss3" : "Feriado de Inverno 3",
    "wh_ss4" : "Feriado de Inverno 4",

    'vd_ss1' : "Dia dos namorados, rosa com corações vermelhos (feminina)",
    'vd_ss2' : "Dia dos namorados, vermelha com corações brancos",
    'vd_ss3' : "Dia dos namorados, branca com corações alados (masculina)",
    'vd_ss4' : "Dia dos namorados, rosa com corações flamejantes",
    'vd_ss5' : "Dia dos namorados 2009, branca com cupido vermelho",
    'vd_ss6' : "Dia dos namorados 2009, azul com verde e corações vermelhos",
    'vd_ss7' : "2010 Dia dos namorados, red with white wings", # Todo
    'sd_ss1' : "Dia de São Patr\xc3\xadcio, camisa com trevo-de-quatro-folhas",
    'sd_ss2' : "Dia de São Patr\xc3\xadcio, camisa com pote de ouro",
    'sd_ss3' : "Ides of March greenToon shirt", # Translate
    'tc_ss1' : "Concurso de Camiseta, Colete de Pesca",
    'tc_ss2' : "Concurso de Camiseta, Aquário",
    'tc_ss3' : "Concurso de Camiseta, Pegada 1",
    'tc_ss4' : "Concurso de Camiseta, Pegada 2",
    'tc_ss5' : "Concurso de Camiseta, Shorts de Couro",
    'tc_ss6' : "Concurso de Camiseta, Melancia",
    'tc_ss7' : "Concurso de Camiseta, Camisa de Corrida",
    'tc_ss8' : "T-Shirt Contest, Most Cogs Defeated Shirt", # Translate
    'j4_ss1' : "Bandeira de 4 de julho",
    'j4_ss2' : "Fogos de Artif\xc3\xadcio de 4 de julho",
    'c_ss12' : "Catálogo série 7, Verde com botões de amarelos",
    'c_ss13' : "Catálogo série 7, Roxo com flor grande",

    'pj_ss1' : "Camisa de Pijama de banana azul",
    'pj_ss2' : "Camisa de Pijama de chifre vermelho",
    'pj_ss3' : "Camisa de Pijama de óculos roxos",

    # Special award clothes
    'sa_ss1' : "Camisa Listrada",
    'sa_ss2' : "Camisa de Pesca 1",
    'sa_ss3' : "Camisa de Pesca 2",
    'sa_ss4' : "Camisa de Jardinagem 1",
    'sa_ss5' : "Camisa de Jardinagem 2",
    'sa_ss6' : "Camisa de Festa 1",
    'sa_ss7' : "Camisa de Festa 2",
    'sa_ss8' : "Camisa de Corrida 1",
    'sa_ss9' : "Camisa de Corrida 2",
    'sa_ss10' : "Camisa de Verão 1",
    'sa_ss11' : "Camisa de Verão 2",
    'sa_ss12' : "Camiseta de Golfe 1",
    'sa_ss13' : "Camiseta de Golfe 2",
    'sa_ss14' : "Camiseta de Fantasia de Halloween 1",
    'sa_ss15' : "Camiseta de Fantasia de Halloween 2",
    'sa_ss16' : "Camiseta de Maratona 1",
    'sa_ss17' : "Camiseta de Salvador de Edif\xc3\xadcios 1",
    'sa_ss18' : "Camiseta de Salvador de Edif\xc3\xadcios 2",
    'sa_ss19' : "Camiseta de Tarefa de Toon 1",
    'sa_ss20' : "Camiseta de Tarefa de Toon 2",
    'sa_ss21' : "Camiseta de Bonde 1",
    'sa_ss22' : "Camiseta de Bonde 2",
    'sa_ss23' : "Camiseta de Inverno 1",
    'sa_ss24' : "Camiseta de Fantasia de Halloween 3",
    'sa_ss25' : "Camiseta de Fantasia de Halloween 4",
    'sa_ss26' : "Pr\xc3\xaamio Camiseta Maioria de Cogs Derrotados",
    'sa_ss27' : "Pr\xc3\xaamio Camiseta Maioria de V.P.s Derrotados",
    'sa_ss28' : "Pr\xc3\xaamio Camiseta de Esmagador do Robô Vendedor",
    'sa_ss29' : "Pr\xc3\xaamio Camiseta Maioria de J.C.s Derrotados",
    'sa_ss30' : "Pr\xc3\xaamio Camiseta de Esmagador do Robô da Lei",
    'sa_ss31' : "Camisa de Corrida 3",
    'sa_ss32' : "Camisa de Pesca 4",
    'sa_ss33' : "Camiseta de Golfe 3",
    'sa_ss34' : "Pr\xc3\xaamio Camiseta Maioria de Cogs Derrotados 2",
    'sa_ss35' : "Amisa de Corrida 4",
    'sa_ss36' : "Camiseta de Salvador de Edif\xc3\xadcios 3",
    'sa_ss37' : "Camiseta de Bonde 3",
    'sa_ss38' : "Camisa de Pesca 5",
    'sa_ss39' : "Camiseta de Golfe 4",
    #
    'sa_ss40' : "Award Halloween Witchy Moon Shirt",
    'sa_ss41' : "Award Winter Holiday Sled Shirt",
    'sa_ss42' : "Award Halloween Batty Moon Shirt",
    'sa_ss43' : "Award Winter Holiday Mittens Shirt",
    #
    'sa_ss44' : "Camisa de Pesca 6",
    'sa_ss45' : "Camisa de Pesca 7",
    'sa_ss46' : "Camiseta de Golfe 5",
    'sa_ss47' : "Camisa de Corrida 5",
    'sa_ss48' : "Camisa de Corrida 6",
    'sa_ss49' : "Pr\xc3\xaamio Camiseta Maioria de Cogs Derrotados 3",
    'sa_ss50' : "Pr\xc3\xaamio Camiseta Maioria de Cogs Derrotados 4",
    'sa_ss51' : "Camiseta de Bonde 4",
    'sa_ss52' : "Camiseta de Bonde 5",
    'sa_ss53' : "Camiseta de Salvador de Edif\xc3\xadcios 4",
    'sa_ss54' : "Camiseta de Salvador de Edif\xc3\xadcios 5",
    #
    'sa_ss55' : "Award Anniversary",

    # Scientists
    'sc_1' : "O 1º melhor Cientista ",
    'sc_2' : "O 2º melhor Cientista ",
    'sc_3' : "O 3º melhor Cientista ",

    # Silly Story Shirts
    'sil_1' : "Camiseta Caixa de Correio Engraçadinha",
    'sil_2' : "Camiseta Lixeira Engraçadinha",
    'sil_3' : "Camiseta Laboratório Maluco Engraçadinho",
    'sil_4' : "Camiseta Hidrante Engraçadinho",
    'sil_5' : "Camiseta Buzina Engraçadinha",
    'sil_6' : "Camiseta Esmaga Cog Engraçadinho",
    'sil_7' : "Blusa Festa da Vitória 1",
    'sil_8' : "Blusa Festa da Vitória 2",

    # Placeholder Emblem Shirts
    'emb_us1' : "placeholder emblem shirt 1",
    'emb_us2' : "placeholder emblem shirt 2",
    'emb_us3' : "placeholder emblem shirt 3",

    # Sellbot Icon Shirt
    'sb_1' : "Camiseta Ícone do Robô Vendedor ",

    # Lawbot Icon Shirt
    'lb_1' : "Lawbot Icon Shirt",

    # Jellybean Shirt
    'jb_1' : "Camiseta Balinha",

    # Doodle Shirt
    'jb_2' : "Camiseta Doodle",

    # No longer in use.
    #'cr_1' : "Mailbox Shirt",
    #'cr_2' : "Trashcan Shirt",
    #'cr_3' : "Loony Labs Shirt",
    #'cr_4' : "Hydrant Shirt",

    # Get Connected Shirt
    'ugcms' : "Get Connected Mover & Shaker",

    # name : [ shirtIdx, sleeveIdx, [(ShirtColorIdx, sleeveColorIdx), ... ]]
    }

# Make sure this is in sync with ToonDNA.BottomStyles
BottomStylesDescriptions = {
    # name : [ bottomIdx, [bottomColorIdx, ...]]
    # -------------------------------------------------------------------------
    # Boy styles (shorts)
    # -------------------------------------------------------------------------
    'bbs1' : "básico com bolsos",
    'bbs2' : "cinto",
    'bbs3' : "cargo",
    'bbs4' : "havaiano",
    'bbs5' : "listras laterais (especial)",
    'bbs6' : "shorts de futebol",
    'bbs7' : "chamas laterais (especial)",
    'bbs8' : "brim",
    'vd_bs1' : "Shorts de dia dos namorados",
    'vd_bs2' : "Verde com coração vermelho",
    'vd_bs3' : "Brim azul com coração verde e vermelho",

    # Catalog only shorts
    'c_bs1' : "Laranja com listras laterais azuis",
    'c_bs2' : "Azul com listras e pregas douradas",
    'c_bs5' : 'Listras verdes - série 7',
    'sd_bs1' : 'Shorts de Duende de São Patr\xc3\xadcio',
    # Translate
    'sd_bs2' : "Ides of March greenToon shorts",
    #
    'pj_bs1' : 'Calça de Pijama de banana azul',
    'pj_bs2' : 'Calça de Pijama de chifre vermelho',
    'pj_bs3' : 'Calça de Pijama de óculos roxos',
    'wh_bs1' : 'Shorts de Feriado de Inverno Estilo 1',
    'wh_bs2' : 'Shorts de Feriado de Inverno Estilo 2',
    'wh_bs3' : 'Shorts de Feriado de Inverno Estilo 3',
    'wh_bs4' : 'Shorts de Feriado de Inverno Estilo 4',
    #
    'hw_bs1' : "Halloween Bee Shorts male",
    'hw_bs2' : "Halloween Pirate Shorts male",
    'hw_bs5' : "Halloween SuperToon Shorts male",
    'hw_bs6' : "Halloween Vampire NoCape Shorts male",
    'hw_bs7' : "Halloween Dinosaur Shorts male",

    # Silly Story Shorts
    'sil_bs1' : 'Short Esmaga Cog Engraçadinho',


    # -------------------------------------------------------------------------
    # Girl styles (shorts and skirts)
    # -------------------------------------------------------------------------
    # skirts
    # -------------------------------------------------------------------------
    'gsk1' : 'básica',
    'gsk2' : 'bolinhas (especial)',
    'gsk3' : 'listras verticais',
    'gsk4' : 'listra horizontal',
    'gsk5' : 'estampa de flor',
    'gsk6' : '2 bolsos (especial)',
    'gsk7' : 'saia de brim',

    # shorts
    # -------------------------------------------------------------------------
    'gsh1' : 'básico com bolsos',
    'gsh2' : 'florido',
    'gsh3' : 'shorts de brim',
    # Special catalog-only skirts and shorts.
    'c_gsk1' : 'saia azul com borda bege e botão ',
    'c_gsk2' : 'saia roxa com rosa e fita',
    'c_gsk3' : 'saia violeta com amarelo e estrela',

    # Valentines skirt
    'vd_gs1' : 'Saia vermelha com corações',
    'vd_gs2' : 'Saia rosa com corações',
    'vd_gs3' : 'Saia de brim azul com coração verde e vermelho',
    'c_gsk4' : 'Saia de arco-\xc3\xadris - Série 3',
    'sd_gs1' : 'Shorts de dia de São Patr\xc3\xadcio',
    'sd_gs2' : 'Ides of March greenToon skirt',
    'c_gsk5' : 'Saias de vaqueira 1',
    'c_gsk6' : 'Saias de vaqueira 2',
    # Western shorts
    'c_bs3' : 'Shorts de caubói 1',
    'c_bs4' : 'Shorts de caubói 2',
    'j4_bs1' : 'Shorts de 4 de julho',
    'j4_gs1' : 'Saia de 4 de julho',
    'c_gsk7' : 'Azul com flor - série 7',
    'pj_gs1' : 'Calça de Pijama de banana azul',
    'pj_gs2' : 'Calça de Pijama de chifre vermelho',
    'pj_gs3' : 'Calça de Pijama de óculos roxos',
    'wh_gsk1' : 'Saia de Feriado de Inverno Estilo 1',
    'wh_gsk2' : 'Saia de Feriado de Inverno Estilo 2',
    'wh_gsk3' : 'Saia de Feriado de Inverno Estilo 3',
    'wh_gsk4' : 'Saia de Feriado de Inverno Estilo 4',

    'sa_bs1' : "Shorts de Pesca",
    'sa_bs2' : "Shorts de Jardinagem",
    'sa_bs3' : "Shorts de Festa",
    'sa_bs4' : "Shorts de Corrida",
    'sa_bs5' : "Shorts de Verão",
    'sa_bs6' : "Shorts de Golfe 1",
    'sa_bs7' : "Shorts de Fantasia de Halloween 1",
    'sa_bs8' : "Shorts de Fantasia de Halloween 2",
    'sa_bs9' : "Shorts de Salvador de Edif\xc3\xadcios 1",
    'sa_bs10' : "Shorts de Bonde 1",
    'sa_bs11' : "Shorts de Halloween 3",
    'sa_bs12' : "Shorts de Halloween 4",
    'sa_bs13' : "Pr\xc3\xaamio Shorts Destruidor de Robô Vendedor masculino",
    'sa_bs14' : "Pr\xc3\xaamio Shorts Destruidor de Robô da Lei masculino",
    'sa_bs15' : "Shorts de Corrida 1",
    'sa_bs16' : "Shorts de Golfe 3",
    'sa_bs17' : "Shorts de Corrida 4",
    'sa_bs18' : "Shorts de Golfe 4",
    'sa_bs19' : "Shorts de Golfe 5",
    'sa_bs20' : "Shorts de Corrida 5",
    'sa_bs21' : "Shorts de Corrida 6",

    'sa_gs1' : "Saia de Pesca",
    'sa_gs2' : "Saia de Jardinagem",
    'sa_gs3' : "Saia de Festa",
    'sa_gs4' : "Saia de Corrida",
    'sa_gs5' : "Saia de Verão",
    'sa_gs6' : "Saia de Golfe 1",
    'sa_gs7' : "Award Halloween Bee Skirt",
    'sa_gs8' : "Award Halloween SuperToon Skirt",
    'sa_gs9' : "Award Save Building Skirt 1",
    'sa_gs10' : "Saia de Bonde 1",
    'sa_gs11' : "Saia de Halloween 1",
    'sa_gs12' : "Saia de Halloween 2",
    'sa_gs13' : "Pr\xc3\xaamio Shorts Destruidor de Robô da Lei feminino",
    'sa_gs14' : "Pr\xc3\xaamio Shorts Destruidor de Robô Vendedor feminino",
    'sa_gs15' : "Saia de Corrida 1",
    'sa_gs16' : "Saia de Golfe 2",
    'sa_gs17' : "Saia de Corrida 4",
    'sa_gs18' : "Saia de Golfe 3",
    'sa_gs19' : "Saia de Golfe 4",
    'sa_gs20' : "Saia de Corrida 5",
    'sa_gs21' : "Saia de Corrida 6",

    'sc_bs1' : "O 1º cientista masculino ",
    'sc_bs2' : "O 2º cientista masculino ",
    'sc_bs3' : "O 3º cientista masculino ",

    'sc_gs1' : "O 1º cientista feminino ",
    'sc_gs2' : "O 2º cientista feminino ",
    'sc_gs3' : "O 2º cientista feminino ",

    'sil_bs1' : "Short masculino Esmaga Cog Engraçadinho",
    'sil_gs1' : "Short feminino Esmaga Cog Engraçadinho",

    'hw_bs3' : "Shorts Vampiro de Halloween masculino",
    'hw_gs3' : "Shorts Vampiro de Halloween feminino",
    'hw_bs4' : "Shorts Tartaruga de Halloween masculino",
    'hw_gs4' : "Shorts Tartaruga de Halloween feminino",
    'hw_gs1' : "Shorts Abelha de Halloween feminino",
    'hw_gs2' : "Shorts Pirata de Halloween feminio",
    'hw_gs5' : "Halloween SuperToon Shorts female",
    'hw_gs6' : "Shorts Vampiro Sem Capa de Halloween feminino",
    'hw_gs7' : "Shorts de Dinossauro de Halloween feminino ",
    'hw_gsk1' : "Saia de Pirata de Halloween",
    }

AwardMgrBoy = "masculino"
AwardMgrGirl = "feminino"
AwardMgrUnisex = "unissex"
AwardMgrShorts = "shorts"
AwardMgrSkirt = "saia"
AwardMgrShirt = "camisa"

# Special Event Strings to display in  mailbox screen
SpecialEventMailboxStrings = {
    1 : "Um item especial do conselho Toon",
    2 : "Pr\xc3\xaamio do Torneio de Pesca de Moby",
    3 : "Pr\xc3\xaamio do Torneio de Pesca de Levi Legal",
    4 : "Aqui está seu pr\xc3\xaamio pelo Convite de Abril do Bosque de Bolotas! Parabéns!",
    5 : "Aqui está seu pr\xc3\xaamio do Campeonato no Bosque de Bolotas! Parabéns!",
    6 : "Aqui está seu pr\xc3\xaamio do Festival de Presentes! Parabéns!",
    7 : "Aqui está seu pr\xc3\xaamio da Maratona de Ano-Novo dos Toons! Parabéns!",
    8 : "Aqui está seu pr\xc3\xaamio do Fim de Semana de Jogos no Bonde! Parabéns!",
    9 : "Aqui está seu pr\xc3\xaamio do Festival de Jogos no Bonde! Parabéns!",
   10 : "Aqui está seu pr\xc3\xaamio do Fim de Semana Premiado! Parabéns!",
   11 : "Aqui está seu pr\xc3\xaamio da Corrida de Cavalos dos Toons! Parabéns!",
   12 : "Aqui está seu pr\xc3\xaamio da Maratona de Salvamento de Edif\xc3\xadcios! Parabéns!",
   13 : "A\xc3\xad está seu pr\xc3\xaamio do torneio de 'Maioria dos Cogs Derrotados'! Parabéns!",
   14 : "Aqui está seu pr\xc3\xaamio do Torneio de Maioria de V.P.s Derrotados! Parabéns!",
   15 : "Aqui está seu pr\xc3\xaamio Operação: Robô Vendedor Tempestade! Parabéns!",
   16 : "Here is your Most C.J.s Defeated Tournament prize! Congratulations!",
   17 : "Here is your Operation: Lawbots Lose prize! Congratulations!",
    }

# Rental items"
RentalHours = "Horas de"
RentalOf = "De"
RentalCannon = "Canhões!"
RentalGameTable = "Mesa de Jogo!"
RentalTime = "Horas de"

EstateCannonGameEnd = "O aluguel do Jogo de Canhão acabou."
GameTableRentalEnd = "O aluguel da Mesa de Jogo acabou."

MessageConfirmRent = "Iniciar o aluguel? Cancele para guardar o aluguel para depois"
MessageConfirmGarden = "Voc\xc3\xaa quer mesmo iniciar um jardim?"

#nametag Names
NametagPaid = "Crachá de Cidadão"
NametagAction = "Crachá de Ação"
NametagFrilly = "Crachá Chique"

FurnitureYourOldCloset = "seu armário velho"
FurnitureYourOldBank = "seu banco velho"
FurnitureYourOldTrunk = "your old trunk"

# How to put quotation marks around chat items--don't translate yet.
ChatItemQuotes = '"%s"'

# CatalogFurnitureItem.py
FurnitureNames = {
  100 : "Poltrona",
  105 : "Poltrona",
  110 : "Cadeira",
  120 : "Cadeira de escrivaninha",
  130 : "Cadeira de jardim",
  140 : "Cadeira lagosta",
  145 : "Cadeira salva-vidas",
  150 : "Banco de sela",
  160 : "Cadeira nativa",
  170 : "Cadeira-bolinho",
  200 : "Cama",
  205 : "Cama",
  210 : "Cama",
  220 : "Cama banheira",
  230 : "Cama de folhas",
  240 : "Cama-barco",
  250 : "Rede de cáctus",
  260 : "Cama de sorvete",
  270 : "Olivia Erin & Cat's Bed",
  300 : "Pianola",
  310 : "\xc3\x93rgão de tubo",
  400 : "Lareira",
  410 : "Lareira",
  420 : "Lareira redonda",
  430 : "Lareira",
  440 : "Lareira-maçã",
  450 : "Lareira Irlandesa",
  460 : "Lareira Irlandesa Acesa",
  470 : "Lareira Acesa",
  480 : "Lareira Circular Acesa",
  490 : "Lareira Acesa",
  491 : "Lareira Acesa",
  492 : "Lareira em Forma de Maçã Acesa",
  500 : "Armário",
  502 : "Armário com 15 itens",
  504 : "Armário com 20 itens",
  506 : "Armário com 25 itens",
  508 : "Armário com 50 itens",
  510 : "Armário",
  512 : "Armário com 15 itens",
  514 : "Armário com 20 itens",
  516 : "Armário com 25 itens",
  508 : "Armário com 50 itens",
  600 : "Abajur pequeno",
  610 : "Abajur grande",
  620 : "Abajur de mesa",
  625 : "Abajur de mesa",
  630 : "Abajur da Margarida",
  640 : "Abajur da Margarida",
  650 : "Abajur da \xc3\x81gua-viva",
  660 : "Abajur da \xc3\x81gua-viva",
  670 : "Abajur do vaqueiro",
  680 : "Vela",
  681 : "Vela Acesa",
  700 : "Cadeira estofada",
  705 : "Cadeira estofada",
  710 : "Sofá",
  715 : "Sofá",
  720 : "Sofá de feno",
  730 : "Sofá-torta",
  800 : "Escrivaninha",
  810 : "Mesinha",
  900 : "Porta-guarda-chuva",
  910 : "Cabideiro",
  920 : "Lata de lixo",
  930 : "Cogumelo vermelho",
  940 : "Cogumelo amarelo",
  950 : "Cabideiro",
  960 : "Mesinha-barril",
  970 : "Planta cáctus",
  980 : "Tenda",
  990 : "O Fan (Leque) de Julieta",
  1000 : "Tapete grande",
  1010 : "Tapete redondo",
  1015 : "Tapete redondo",
  1020 : "Tapete pequeno",
  1030 : "Capacho de folha",
  1040 : "Presents",
  1050 : "Sled",
  1100 : "Vitrina",
  1110 : "Vitrina",
  1120 : "Estante alta",
  1130 : "Estante baixa",
  1140 : "Arca-sundae",
  1200 : "Mesinha lateral",
  1210 : "Mesa pequena",
  1215 : "Mesa pequena",
  1220 : "Mesinha de centro",
  1230 : "Mesinha de centro",
  1240 : "Mesa Snorkel",
  1250 : "Mesa-biscoito",
  1260 : "Mesa do quarto",
  1300 : "Banco 1.000 Balas",
  1310 : "Banco 2.500 Balas",
  1320 : "Banco 5.000 Balas",
  1330 : "Banco 7.500 Balas",
  1340 : "Banco 10.000 Balas",
  1350 : "Banco 12.000 Balas",
  1399 : "Telefone",
  1400 : "Toon Cezanne",
  1410 : "Flores",
  1420 : "Mickey Moderno",
  1430 : "Toon Rembrandt",
  1440 : "Toonescape",
  1441 : "Cavalo Assobiador",
  1442 : "Estrela Toon",
  1443 : "Não é Torta",
  1450 : "Mickey é Minnie",
  1500 : "Rádio",
  1510 : "Rádio",
  1520 : "Rádio",
  1530 : "Televisão",
  1600 : "Vasinho",
  1610 : "Vaso alto",
  1620 : "Vasinho",
  1630 : "Vaso alto",
  1640 : "Vasinho",
  1650 : "Vasinho",
  1660 : "Vaso Coral",
  1661 : "Vaso de concha",
  1670 : "Rose Vase",
  1680 : "Rose Watercan",
  1700 : "Carrocinha de pipoca",
  1710 : "Joaninha",
  1720 : "Chafariz",
  1725 : "Lavadora de roupa",
  1800 : "Aquário",
  1810 : "Aquário",
  1900 : "Peixe-espada",
  1910 : "Tubarão-martelo",
  1920 : "Chifres de pendurar",
  1930 : "Sombreiro simples",
  1940 : "Sombreiro elegante",
  1950 : "Apanhador de sonhos",
  1960 : "Ferradura",
  1970 : "Retrato de búfalo",
  2000 : "Balanço de doces",
  2010 : "Escorregada de torta",
  3000 : "Banheira banana split",
  4000 : "Boy Trunk",
  4010 : "Girl Trunk",
  10000 : "Moranga",
  10010 : "Abóbora",
  10020 : "\xc3\x81rvore de Natal",
  10030 : "Guirlanda de Natal"
  }

# these gets shown in the award manager web page, descriptions must be unique
AwardManagerFurnitureNames = {
  100 : "Poltrona A – Série 1",
  105 : "Poltrona A – Série 7",
  110 : "Cadeira – Série 1",
  120 : "Cadeira de Escritório – Série 2",
  130 : "Cadeira de Madeira – Série 2",
  140 : "Cadeira de Lagosta – Série 3",
  145 : "Cadeira Salva-vidas – Série 3",
  150 : "Banco de Sela - Série 4",
  160 : "Cadeira Nativa – Série 4",
  170 : "Cadeira-Bolinho – Série 6",
  200 : "Cama de Menino Sonolento – Mob\xc3\xadlia Inicial",
  205 : "Cama de Menino Sonolento Série – 7",
  210 : "Cama de Menina Sonolenta – Série 1",
  220 : "Cama-Banheira",
  230 : "Cama-Folha",
  240 : "Cama-Barco",
  250 : "Rede-Cacto",
  260 : "Cama-Sorvete",
  270 : "Cama de Olivia Erin e Gato – Cama-Bonde",
  300 : "Piano de Jogador",
  310 : "\xc3\x93rgão",
  400 : "Lareira – Lareira Quadrada Mob\xc3\xadlia Inicial",
  410 : "Lareira – Lareira Feminina Série 1",
  420 : "Lareira Redonda",
  430 : "Lareira – sala de insetos série 2",
  440 : "Lareira-Maçã",
  450 : "Lareira de Erin – coral",
  460 : "Lareira Acesa de Erin - coral",
  470 : "Lareira Acesa – lareira quadrada com fogo",
  480 : "Lareira Redonda Acesa",
  490 : "Lareira Acesa – lareira de menina com fogo",
  491 : "Lareira Acesa – lareira da sala de insetos",
  492 : "Lareira Maçã Acesa",
  500 : "Guarda-roupa de menino – 10 itens iniciais",
  502 : "Guarda-roupa de menino com 15 itens",
  504 : "Guarda-roupa de menino com 20 itens",
  506 : "Guarda-roupa de menino com 25 itens",
  508 : "Guarda-roupa de menino com 50 itens",
  510 : "Guarda-roupa de menina – 10 itens iniciais",
  512 : "Guarda-roupa de menina com 15 itens",
  514 : "Guarda-roupa de menina com 20 itens",
  516 : "Guarda-roupa de menina com 25 itens",
  518 : "Guarda-roupa de menina com 50 itens",
  600 : "Lâmpada Baixa",
  610 : "Lâmpada Alta",
  620 : "Lâmpada de Mesa – Série 1",
  625 : "Lâmpada de Mesa – Série 7",
  630 : "Lâmpada da Margarida 1",
  640 : "Lâmpada da Margarida 2",
  650 : "Lâmpada-\xc3\x81gua-viva 1",
  660 : "Lâmpada-\xc3\x81gua-viva 2",
  670 : "Lâmpada de Cowboy",
  680 : "Vela",
  681 : "Vela Acesa",
  700 : "Cadeira com Almofada – Série 1",
  705 : "Cadeira com Almofada – Série 7",
  710 : "Sofá – série 1",
  715 : "Sofá – série 7",
  720 : "Sofá de Feno",
  730 : "Sofá Bolinho",
  800 : "Escrivaninha",
  810 : "Escrivaninha de Madeira",
  900 : "Suporte para Guarda-chuva",
  910 : "Porta-casaco – Série 1",
  920 : "Lata de Lixo",
  930 : "Cogumelo Vermelho",
  940 : "Cogumelo Amarelo",
  950 : "Porta-casaco - aquático",
  960 : "Suporte para Barril",
  970 : "Cacto",
  980 : "Tenda",
  990 : "Fã de Juliette – fã de brincadeira",
  1000 : "Tapete Grande",
  1010 : "Tapete Redondo – Série 1",
  1015 : "Tapete Redondo – Série 7",
  1020 : "Tapete Pequeno",
  1030 : "Tapete-Folha",
  1040 : "Presentes",
  1050 : "Trenó",
  1100 : "Vitrine – Vermelha",
  1110 : "Vitrine – Amarela",
  1120 : "Estante Alta",
  1130 : "Estante Baixa",
  1140 : "Baú-Sorvete",
  1200 : "Mesinha",
  1210 : "Mesa Pequena – série 1",
  1215 : "Mesa Pequena – série 7",
  1220 : "Mesa de Café quadrada",
  1230 : "Mesa de Café bw",
  1240 : "Mesa-Mergulhador",
  1250 : "Mesa-Biscoito",
  1260 : "Mesa de Quarto",
  1300 : "Banco de 1.000 Balas",
  1310 : "Banco de 2.500 Balas",
  1320 : "Banco de 5.000 Balas",
  1330 : "Banco de 7.500 Balas",
  1340 : "Banco de 10.000 Balas",
  1350 : "Banco de 12.000 Balas",
  1399 : "Telefone",
  1400 : "Toon Cezanne",
  1410 : "Flores",
  1420 : "Mickey Moderno",
  1430 : "Toon Rembrandt",
  1440 : "Fuga dos Toons",
  1441 : "Cavalo do Apitador",
  1442 : "Estrela Toon",
  1443 : "Não é uma Torta",
  1450 : "Mickey e Minnie",
  1500 : "Rádio A série 2",
  1510 : "Rádio B série 1",
  1520 : "Rádio C série 2",
  1530 : "Televisão",
  1600 : "Vaso Baixo A",
  1610 : "Vaso Alto A",
  1620 : "Vaso Baixo B",
  1630 : "Vaso Alto B",
  1640 : "Vaso Baixo C",
  1650 : "Vaso Baixo D",
  1660 : "Vaso Coral",
  1661 : "Vaso-Concha",
  1670 : "Vaso Rosa",
  1680 : "Regador Rosa",
  1700 : "Carrinho de Pipoca",
  1710 : "Joaninha",
  1720 : "Fonte",
  1725 : "Máquina de Lavar",
  1800 : "Caveira de Aquário",
  1810 : "Lagarto de Aquário",
  1900 : "Peixe-espada",
  1910 : "Tubarão-martelo",
  1920 : "Chifres Empalhados",
  1930 : "Sombreiro Simples",
  1940 : "Sobreiro Chique",
  1950 : "Apanhador de Sonhos",
  1960 : "Ferradura",
  1970 : "Retrato de Bisão",
  2000 : "Balanço de Doce",
  2010 : "Escorregador-Bolo",
  3000 : "Banheira-Banana Split",
  4000 : "Boy Trunk",
  4010 : "Girl Trunk",
  10000 : "Abóbora Pequena",
  10010 : "Abóbora Grande",
  10020 : "\xc3\x81rvore de Inverno",
  10030 : "Guirlanda de Inverno"
  }

# CatalogClothingItem.py
ClothingArticleNames = (
    "Camisa",
    "Camisa",
    "Camisa",
    "Bermuda",
    "Bermuda",
    "Saia",
    "Bermuda",
    )

ClothingTypeNames = {
    1001 : "Camiseta de Fantasma",
    1002 : "Camiseta de Abóbora",
    # Translate
    1112 : "Bee Shirt",
    1113 : "Pirate Shirt",
    1114 : "Super Toon Shirt",
    1115 : "Vampire Shirt",
    1116 : "Toonosaur Shirt",
    1117 : "Bee Shorts",
    1118 : "Pirate Shorts",
    1119 : "Super Toon Shorts",
    1120 : "Vampire Shorts",
    1121 : "Toonosaur Shorts",
    1122 : "Bee Shorts",
    1123 : "Pirate Shorts",
    1124 : "Super Toon Shorts",
    1125 : "Vampire Shorts",
    1126 : "Toonosaur Shorts",
    1127 : "Pirate Skirt",
    1304 : "O'Shirt",
    1305 : "O'Shorts",
    1306 : "O'Skirt",
    #
    1400 : "Camisa do Mateus",
    1401 : "Camisa da Jéssica",
    1402 : "Camisa da Marisa",
    1600 : "Traje de Armadilha",
    1601 : "Traje de Som",
    1602 : "Traje de Isca",
    1603 : "Traje de Armadilha",
    1604 : "Traje de Som",
    1605 : "Traje de Isca",
    1606 : "Traje de Armadilha",
    1607 : "Traje de Som",
    1608 : "Traje de Isca",
    1723 : "Camiseta de Abelha",
    1724 : "Camiseta de SuperToon",
    1734 : "Shorts de Abelha",
    1735 : "Shorts de SuperToon",
    1739 : "Saia de Abelha",
    1740 : "Saia de SuperToon",
    1743 : "Camiseta de Esqueleto",
    1744 : "Saia de Aranha",
    1745 : "Shorts de Aranha",
    1746 : "Shorts de Esqueleto",
    1747 : "Saia de Esqueleto",
    1748 : "Saia de Aranha",
    1749 : "Camiseta Caixa de Correio Engraçadinha",
    1750 : "Camiseta Lixeira Engraçadinha",
    1751 : "Camiseta Laboratório Maluco Engraçadinho",
    1752 : "Camiseta Hidrante Engraçadinho",
    1753 : "Camiseta Medidor de bobagens",
    1754 : "Camiseta Esmaga Cog Engraçadinho",
    1755 : "Short Esmaga Cog Engraçadinho",
    1756 : "Short Esmaga Cog Engraçadinho",
    1757 : "Camiseta Festa da Vitória",
    1758 : "Camiseta Festa da Vitória",
    1763 : "Camiseta Robô Vendedor Destru\xc3\xaddo",
    1764 : "Camiseta Maioria de V.P.s Derrotados",
    1765 : "Camiseta Destruidor do Robô Vendedor",
    1766 : "Shorts Destruidor do Robô Vendedor ",
    1767 : "Shorts Destruidor do Robô Vendedor ",
    1768 : "Camiseta Banco de Balinha",
    1769 : "Camiseta Doodle",
    1770 : "Camiseta de Vampiro",
    1771 : "Camiseta de Tartaruga",
    1772 : "Shorts de Vampiro",
    1773 : "Shorts de Vampiro",
    1774 : "Shorts de Tartaruga",
    1775 : "Shorts de Tartaruga",
    # Translate
    1776 : "Get Connected Mover & Shaker Shirt",
    1777 : "Smashed Lawbot Shirt",
    1778 : "Most C.J.s Defeated Shirt",
    1779 : "Lawbot Smasher Shirt",
    1780 : "Lawbot Smasher Shorts",
    1781 : "Lawbot Smasher Shorts",
    1782 : "Racing Shirt 3",
    1783 : "Racing Shorts 1",
    1784 : "Racing Skirt 1",
    1801 : "Batty Moon Shirt",
    1802 : "Mittens Shirt",
    }

AccessoryArticleNames = (
    "Chapéu",
    "Glasses",
    "Backpack",
    "Shoes",
    "Chapéu",
    "Glasses",
    "Backpack",
    "Shoes",
    "Chapéu",
    "Glasses",
    "Backpack",
    "Shoes",
    )

# CatalogSurfaceItem.py
SurfaceNames = (
    "Papel de parede",
    "Moldura do teto",
    "Piso",
    "Lambri",
    "Moldura",
    )

WallpaperNames = {
    1000 : "Pergaminho",
    1100 : "Milão",
    1200 : "Dover",
    1300 : "Vitória",
    1400 : "Newport",
    1500 : "Pastoral",
    1600 : "Arlequim",
    1700 : "Lua",
    1800 : "Estrelas",
    1900 : "Flores",
    2000 : "Jardim de primavera",
    2100 : "Jardim formal",
    2200 : "Dia de corrida",
    2300 : "Gol!",
    2400 : "Nuvem 9",
    2500 : "Trepadeira",
    2600 : "Primavera",
    2700 : "Boneca japonesa",
    2800 : "Arranjo de flores",
    2900 : "Peixe-anjo",
    3000 : "Bolhas",
    3100 : "Bolhas",
    3200 : "Ir pescar",
    3300 : "Parar de pescar",
    3400 : "Cavalo-marinho",
    3500 : "Conchinhas do mar",
    3600 : "Debaixo d'água",
    3700 : "Botinas",
    3800 : "Cáctus",
    3900 : "Chapéu de vaqueiro",
    10100 : "Gatos",
    10200 : "Morcegos",
    11000 : "Flocos de neve",
    11100 : "Folhas de Natal",
    11200 : "Boneco de neve",
    12000 : "Cartão do Dia dos Namorados",
    12100 : "Cartão do Dia dos Namorados",
    12200 : "Cartão do Dia dos Namorados",
    12300 : "Cartão do Dia dos Namorados",
    13000 : "Trevo",
    13100 : "Trevo",
    13200 : "Arco-\xc3\xadris",
    13300 : "Trevo",
    }

FlooringNames = {
    1000 : "Tábua-corrida",
    1010 : "Carpete",
    1020 : "Piso em losangos",
    1030 : "Piso em losangos",
    1040 : "Grama",
    1050 : "Tijolinho bege",
    1060 : "Tijolinho vermelho",
    1070 : "Piso quadrado",
    1080 : "Pedra",
    1090 : "Calçada",
    1100 : "Terra",
    1110 : "Sinteco",
    1120 : "Lajota",
    1130 : "Favo",
    1140 : "\xc3\x81gua",
    1150 : "Piso praiano",
    1160 : "Piso praiano",
    1170 : "Piso praiano",
    1180 : "Piso praiano",
    1190 : "Areia",
    10000 : "Cubo de gelo",
    10010 : "Iglu",
    11000 : "Trevo",
    11010 : "Trevo",
    }

MouldingNames = {
    1000 : "Nós",
    1010 : "Pintado",
    1020 : "Dental",
    1030 : "Flores",
    1040 : "Flores",
    1050 : "Joaninha",
    1060 : "Cartões do Dia dos Namorados",
    1070 : "Praia",
    1080 : "Luzes de Inverno 1",
    1085 : "Luzes de Inverno 2",
    1090 : "Luzes de Inverno 3",
    1100 : "Cupido do Dia dos Namorados",
    1110 : "Coração do Dia dos Namorados 1",
    1120 : "Coração do Dia dos Namorados 2",
    }

WainscotingNames = {
    1000 : "Pintado",
    1010 : "Painel de madeira",
    1020 : "Madeira",
    1030 : "Cartões do Dia dos Namorados",
    1040 : "Subaquático",
    }

# CatalogWindowItem.py--don't translate yet.
WindowViewNames = {
    10 : "Jardim amplo",
    20 : "Jardim selvagem",
    30 : "Jardim grego",
    40 : "Paisagem urbana",
    50 : "Velho Oeste",
    60 : "Fundo do mar",
    70 : "Ilha tropical",
    80 : "Noite estrelada",
    90 : "Piscina Tiki",
    100 : "Fronteira congelada",
    110 : "Fazenda",
    120 : "Campo Nativo",
    130 : "Rua Principal",
    }

SpecialEventNames = {
    1: "Pr\xc3\xaamio Geral",
    2: "Torneio de Pesca de Moby",
    3: "Torneio de Pesca de Levi Legal",
    4: "Convite de Abril do Bosque de Bolotas",
    5: "Campeonato no Bosque de Bolotas",
    6: "Festival de Presentes",
    7: "Maratona de Ano-Novo dos Toons",
    8: "Fim de Semana de Jogos no Bonde",
    9: "Festival de Jogos no Bonde",
   10: "Fim de Semana Premiado",
   11: "Corrida de Cavalos dos Toons",
   12: "Maratona de Salvamento de Edif\xc3\xadcios",
   13: "Maioria dos Cogs Derrotados",
   14: "Maioria dos V.P.s Derrotados",
   15: "Operação Evento Robô Vendedor Tempestade",
   # Translate
   16: "Most C.J.s Defeated",
   17: "Operation Lawbots Lose Event",
}


# don't translate yet
NewCatalogNotify = "Há novos itens dispon\xc3\xadveis para serem encomendados por telefone!"
NewDeliveryNotify = "Chegou correspond\xc3\xaancia nova em sua caixa de correio!"
CatalogNotifyFirstCatalog = "Seu primeiro catálogo chegou! Voc\xc3\xaa pode usá-lo para encomendar novos itens para uso pessoal ou para casa."
CatalogNotifyNewCatalog = "O seu catálogo No. %s chegou! Voc\xc3\xaa pode fazer os pedidos dos itens do catálogo pelo telefone."
CatalogNotifyNewCatalogNewDelivery = "Chegou correspond\xc3\xaancia nova em sua caixa de correio! Além disso, o seu catálogo No. %s chegou!"
CatalogNotifyNewDelivery = "Chegou correspond\xc3\xaancia nova em sua caixa de correio!"
CatalogNotifyNewCatalogOldDelivery = "O seu catálogo No. %s chegou, e ainda há itens aguardando por voc\xc3\xaa em sua caixa de correio!"
CatalogNotifyOldDelivery = "Ainda há itens aguardando por voc\xc3\xaa em sua caixa de correio!"
CatalogNotifyInstructions = "Clique no botão \"Ir para casa\" na Página do mapa em seu \xc3\x81lbum Toon e vá até o telefone que há dentro da sua casa."
CatalogNewDeliveryButton = "Nova\nentrega!"
CatalogNewCatalogButton = "Novo\ncatálogo"
CatalogSaleItem = "\xc3\x80 venda! "

# don't translate yet
DistributedMailboxEmpty = "A sua caixa de correio está vazia no momento. Volte aqui para procurar entregas depois que voc\xc3\xaa fizer um pedido pelo telefone!"
DistributedMailboxWaiting = "A sua caixa de correio está vazia no momento, mas o pacote que voc\xc3\xaa encomendou está a caminho. Verifique mais tarde!"
DistributedMailboxReady = "Sua encomenda chegou!"
DistributedMailboxNotOwner = "Sinto muito, esta não é a sua caixa de correio."
DistributedPhoneEmpty = "Voc\xc3\xaa pode usar qualquer telefone para encomendar itens especiais para uso pessoal ou para sua casa. Em breve, haverá novos itens dispon\xc3\xadveis para pedidos.\n\nNão há nenhum item dispon\xc3\xadvel para pedidos no momento, mas verifique novamente mais tarde!"

# don't translate yet
Clarabelle = "Clarabela"
MailboxExitButton = "Fechar caixa\nde correio"
MailboxAcceptButton = "Pegar este item"
MailBoxDiscard = "Remover este item"
MailboxAcceptInvite = "Aceitar convite"
MailBoxRejectInvite = "Recusar convite"
MailBoxDiscardVerify = "Voc\xc3\xaa quer mesmo Remover %s?"
MailBoxRejectVerify = "Voc\xc3\xaa quer mesmo Recusar %s?"
MailboxOneItem = "Sua caixa postal contém 1 item."
MailboxNumberOfItems = "Sua caixa postal contém %s itens."
MailboxGettingItem = "Pegando %s da caixa postal."
MailboxGiftTag = "Presente De: %s"
MailboxGiftTagAnonymous = "Anônimo"
MailboxItemNext = "Próximo\nitem"
MailboxItemPrev = "Item\nanterior"
MailboxDiscard = "Remover"
MailboxReject = "Recusar"
MailboxLeave = "Guardar"
CatalogCurrency = "balas"
CatalogHangUp = "Desligar"
CatalogNew = "NOVA"
CatalogBackorder = "ENCOMENDA"
CatalogLoyalty = "ESPECIAL"
CatalogEmblem = "EMBLEMA"
CatalogPagePrefix = "Página"
CatalogGreeting = "Olá! Agradecemos sua ligação para o Catálogo da Clarabela. Posso ajudar?"
CatalogGoodbyeList = ["Agora tchau!",
                      "Ligue novamente em breve!",
                      "Agradecemos sua ligação!",
                      "Ok, agora tchau!",
                      "Tchau!",
                      ]
CatalogHelpText1 = "Vire a página para ver os itens \xc3\xa0 venda."
CatalogSeriesLabel = "Série %s"
CatalogGiftFor = "Comprar Presente para:"
CatalogGiftTo = "Para: %s"
CatalogGiftToggleOn = "Parar de\nPresentear"
CatalogGiftToggleOff = "Comprar\nPresentes"
CatalogGiftToggleWait = "Tentando!..."
CatalogGiftToggleNoAck = "Não Dispon\xc3\xadvel"
CatalogPurchaseItemAvailable = "Parabéns pela nova compra! Voc\xc3\xaa já pode usar o seu produto imediatamente."
CatalogPurchaseGiftItemAvailable = "\xc3\x93timo! %s pode começar a usar o seu presente agora mesmo."
CatalogPurchaseItemOnOrder = "Parabéns! O produto será entregue em sua caixa de correio em breve."
CatalogPurchaseGiftItemOnOrder = "\xc3\x93timo! O seu presente para %s será entregue na caixa de correio dele."
CatalogAnythingElse = "Deseja mais alguma coisa hoje?"
CatalogPurchaseClosetFull = "O seu armário está cheio. Apesar disso, voc\xc3\xaa pode comprar este item, mas se comprar, terá que excluir alguma coisa do seu armário para liberar espaço para o novo item, quando ele chegar.\n\nQuer comprar este item mesmo assim?"
CatalogPurchaseNoTrunk = "In order to wear this item, you need to buy a trunk.\n\nDo you still want to purchase this item?"
CatalogPurchaseTrunkFull = "Your trunk is full. If you purchase this item, you'll need to delete another item from your trunk to make more room.\n\nDo you still want to purchase this item?"
CatalogAcceptClosetFull = "O seu armário está cheio. Entre em casa e exclua alguma coisa do seu armário para liberar espaço para o item antes de retirá-lo da caixa de correio."
CatalogAcceptShirt = "Voc\xc3\xaa está vestindo agora a sua nova camisa. O que voc\xc3\xaa estava vestindo antes foi transferido para o seu armário."
CatalogAcceptShorts = "Voc\xc3\xaa está vestindo agora o seu novo short. O que voc\xc3\xaa estava vestindo antes foi transferido para o seu armário."
CatalogAcceptSkirt = "Voc\xc3\xaa está vestindo agora a sua nova saia. A que voc\xc3\xaa estava vestindo antes foi transferida para o seu armário."
CatalogAcceptHat = "Agora você está usando seu novo chapéu. O chapéu que você estava usando antes foi movido para o seu porta-malas."
CatalogAcceptGlasses = "You are now wearing your new glasses. The glasses you were wearing before have been moved to your trunk."
CatalogAcceptBackpack = "You are now wearing your new backpack. The backpack you were wearing before has been moved to your trunk."
CatalogAcceptShoes = "You are now wearing your new shoes. The shoes you were wearing before have been moved to your trunk."
CatalogAcceptPole = "Agora, voc\xc3\xaa está pronto para pescar uns peixes maiores com sua nova vara!"
CatalogAcceptPoleUnneeded = "Voc\xc3\xaa já tem uma vara de pescar melhor do que esta!"
CatalogAcceptChat = "Voc\xc3\xaa ganhou uma nova frase de Chat rápido!"
CatalogAcceptEmote = "Voc\xc3\xaa ganhou uma nova Emoção!"
CatalogAcceptBeans = "Voc\xc3\xaa recebeu algumas balinhas!"
CatalogAcceptRATBeans = "A sua recompensa de recruta Toon chegou!"
CatalogAcceptPartyRefund = "Your party was never started. Here's your refund!"
CatalogAcceptNametag = "Seu novo crachá chegou!"
CatalogAcceptGarden = "Os seus materiais de jardim chegaram!"
CatalogAcceptPet = "Voc\xc3\xaa ganhou um novo Truque de Rabisco!"
CatalogPurchaseHouseFull = "Sua casa está cheia. Apesar disso, voc\xc3\xaa pode comprar este item, mas se comprar, terá que excluir alguma coisa da sua casa para liberar espaço para o novo item, quando ele chegar.\n\nQuer comprar este item mesmo assim?"
CatalogAcceptHouseFull = "Sua casa está cheia. Entre em casa e exclua alguma coisa de lá para liberar espaço para o item antes de retirá-lo da caixa de correio."
CatalogAcceptInAttic = "O seu novo item está agora no sótão. Voc\xc3\xaa pode colocá-lo em casa entrando lá e clicando no botão \"Mover mob\xc3\xadlia\"."
CatalogAcceptInAtticP = "Os seus novos itens estão agora no sótão. Voc\xc3\xaa pode colocá-los em casa entrando lá e clicando no botão \"Mover mob\xc3\xadlia\"."
CatalogPurchaseMailboxFull = "Sua caixa de correio está cheia! Voc\xc3\xaa não poderá comprar este item até retirar alguns itens da caixa de correio para liberar espaço."
CatalogPurchaseGiftMailboxFull = "A caixa de correio de %s está cheia! Voc\xc3\xaa não pode comprar este item."
CatalogPurchaseOnOrderListFull = "Voc\xc3\xaa tem itens demais encomendados no momento. Voc\xc3\xaa não poderá encomendar mais nenhum item até que cheguem alguns já encomendados."
CatalogPurchaseGiftOnOrderListFull = "%s tem \xc3\xadtens demais encomendados."
CatalogPurchaseGeneralError = "Não foi poss\xc3\xadvel encomendar o item devido a um erro interno no jogo: código de erro %s."
CatalogPurchaseGiftGeneralError = "Não foi poss\xc3\xadvel dar o item de presente a %(friend)s por causa de algum erro interno de jogo: código de erro %(error)s."
CatalogPurchaseGiftNotAGift = "Este item não pôde ser enviado para %s porque seria uma vantagem injusta."
CatalogPurchaseGiftWillNotFit = "Este item não pôde ser enviado para %s porque não vai servir."
CatalogPurchaseGiftLimitReached = "Este item não pôde ser enviado para %s porque ele já o possui."
CatalogPurchaseGiftNotEnoughMoney = "Este item não pôde ser enviado para %s porque ele não pode pagar."
CatalogAcceptGeneralError = "Este item não pôde ser exclu\xc3\xaddo da sua caixa de correio por causa de um erro interno do jogo: código do erro %s."
CatalogAcceptRoomError = "Voc\xc3\xaa não tem espaço para isto. Voc\xc3\xaa vai ter que se livrar de alguma coisa."
CatalogAcceptLimitError = "Voc\xc3\xaa já tem o número máximo poss\xc3\xadvel disto. Voc\xc3\xaa vai ter que se livrar de alguma coisa."
CatalogAcceptFitError = "Isto não serve em voc\xc3\xaa! Voc\xc3\xaa o doa para Toons que precisam."
CatalogAcceptInvalidError = "Este item saiu da moda! Voc\xc3\xaa o doa para Toons que precisam."

MailboxOverflowButtonDicard = "Remover"
MailboxOverflowButtonLeave = "Sair"

HDMoveFurnitureButton = "Mover\nmob\xc3\xadlia"
HDStopMoveFurnitureButton = "Mudança\nconclu\xc3\xadda"
HDAtticPickerLabel = "No sótão"
HDInRoomPickerLabel = "Na sala"
HDInTrashPickerLabel = "Na lixeira"
HDDeletePickerLabel = "Excluir?"
HDInAtticLabel = "Sótão"
HDInRoomLabel = "Sala"
HDInTrashLabel = "Lixo"
HDToAtticLabel = "Enviar\npara o sótão"
HDMoveLabel = "Mover"
HDRotateCWLabel = "Girar para a direita"
HDRotateCCWLabel = "Girar para a esquerda"
HDReturnVerify = "Retornar este item para o sótão?"
HDReturnFromTrashVerify = "Retornar este item para o sótão, da lixeira?"
HDDeleteItem = "Clique em OK para enviar este item para a lixeira ou em Cancelar para mant\xc3\xaa-lo."
HDNonDeletableItem = "Voc\xc3\xaa não pode excluir itens deste tipo!"
HDNonDeletableBank = "Voc\xc3\xaa não pode excluir o seu banco!"
HDNonDeletableCloset = "Voc\xc3\xaa não pode excluir o seu armário!"
HDNonDeletablePhone = "Voc\xc3\xaa não pode excluir o seu telefone!"
HDNonDeletableTrunk = "You can't delete your trunk!"
HDNonDeletableNotOwner = "Voc\xc3\xaa não pode excluir as coisas de %s's!"
HDHouseFull = "Sua casa está cheia. Voc\xc3\xaa precisa excluir algo mais de sua casa ou do sótão antes de recuperar este item da lixeira."

HDHelpDict = {
    "DoneMoving" : "Decoração da sala conclu\xc3\xadda.",
    "Attic" : "Mostrar lista de itens do sótão. O sótão armazena itens que não estão na sala.",
    "Room" : "Mostrar lista de itens da sala. \xc3\x9atil para encontrar itens perdidos.",
    "Trash" : "Mostrar itens da lixeira. Os itens mais antigos são exclu\xc3\xaddos após um tempo ou quando a lixeira fica cheia demais.",
    "ZoomIn" : "Tenha uma visão ampliada da sala.",
    "ZoomOut" : "Tenha uma visão reduzida da sala.",
    "SendToAttic" : "Envie o item de mob\xc3\xadlia atual para o sótão, para armazená-lo.",
    "RotateLeft" : "Vire para a esquerda.",
    "RotateRight" : "Vire para a direita.",
    "DeleteEnter" : "Alterne para o modo de exclusão.",
    "DeleteExit" : "Saia do modo de exclusão.",
    "FurnitureItemPanelDelete" : "Envie o item %s para a lixeira.",
    "FurnitureItemPanelAttic" : "Coloque o item %s na sala.",
    "FurnitureItemPanelRoom" : "Voltar o item %s para o sótão.",
    "FurnitureItemPanelTrash" : "Voltar o item %s para o sótão.",
    }

MessagePickerTitle = "Voc\xc3\xaa tem frases demais. Para comprar o item\n\"%s\"\n voc\xc3\xaa precisa escolher um deles para ser removido:"
MessagePickerCancel = lCancel
MessageConfirmDelete = "Tem certeza de que quer remover \"%s\" do menu de Chat rápido?"

CatalogBuyText = "Comprar"
CatalogRentText = "Alugar"
CatalogGiftText = "Presente"
CatalogOnOrderText = "Encomendado"
CatalogPurchasedText = "Já\ncomprado"
CatalogCurrent = "Atual"
CatalogGiftedText = "Presenteado\nPara Voc\xc3\xaa"
CatalogPurchasedGiftText = "Já\nRecebido"
CatalogMailboxFull = "Sem Espaço"
CatalogNotAGift = "Não é um Presente"
CatalogNoFit = "Não\nServe"
CatalogMembersOnly = "Somente para\nUsuários!"
CatalogSndOnText = "Som Ligado"
CatalogSndOffText = "Som Desligado"
CatalogPurchasedMaxText = "Já\ncomprado o máx."
CatalogVerifyRent = "Alugar %(item)s por %(price)s balinhas?"
CatalogVerifyGift = "Comprar %(item)s por %(price)s balinhas de presente para %(friend)s?"
CatalogVerifyPurchase = "Comprar o item %(item)s por %(price)s balinhas?"
CatalogOnlyOnePurchase = "Voc\xc3\xaa só pode ter um destes itens de cada vez. Se comprar este aqui, ele substituirá os itens %(old)s.\n\nTem certeza de que quer comprar o item %(item)s por %(price)s balinhas?"
CatalogExitButtonText = "Desligar"
CatalogCurrentButtonText = "Para itens atuais"
CatalogPastButtonText = "Para itens antigos"

TutorialHQOfficerName = "Haroldo do Quartel"

# NPCToons.py
NPCToonNames = {
    # These are for the tutorial. We do not actually use the zoneId here
    # But the quest posters need to know his name
    20000 : "Tom Tutorial",
    999 : "Costureiro Toon",
    1000 : lToonHQ,
    20001 : Flippy,

    #
    # Toontown Central
    #

    # Toontown Central Playground

    # This Flippy DNA matches the tutorial Flippy
    # He is in Toon Hall
    2001 : Flippy,
    2002 : "Banqueiro Beto",
    2003 : "Professor Paulo",
    2004 : "Cora, a Costureira",
    2005 : "Bibliotecário Bino",
    2006 : "Vendedor Alaor",
    2011 : "Vendedora Isadora",
    2007 : lHQOfficerM,
    2008 : lHQOfficerM,
    2009 : lHQOfficerF,
    2010 : lHQOfficerF,
    # NPCFisherman
    2012 : "Vendedor da Loja de Animais",
    2018 : "Estúpi...doo... Homem-DICA",
    # NPCPetClerks
    2013 : "Vendedor Pop",
    2014 : "Vendedora Elétrica",
    2015 : "Vendedor Molenga",
    # NPCPartyPerson
    2016 : "Planejador de Festa Abóbora",
    2017 : "Planejadora de Festa Polly",
    2018 : "Doutor Surlee",
    2019 : "Doutor Dimm",
    2020 : "Professor Prepostera",

    # Silly Street
    2101 : "Dentista Daniel",
    2102 : "Delegada Délis",
    2103 : "Gatinho Funga-funga",
    2104 : lHQOfficerM,
    2105 : lHQOfficerM,
    2106 : lHQOfficerF,
    2107 : lHQOfficerF,
    2108 : "Canária Mina de carvão",
    2109 : "Gugu Bolha",
    2110 : "Otto D'or",
    2111 : "Diego Dançante",
    2112 : "Dr. Tom",
    2113 : "Rolo, o Incr\xc3\xadvel",
    2114 : "Rosabela",
    2115 : "Pati Papel",
    2116 : "Brutus Crespo",
    2117 : "Dona Putrefata",
    2118 : "Bob Bobo",
    2119 : "Renata Rá Rá",
    2120 : "Professor Pimpão",
    2121 : "Madame Risadinha",
    2122 : "Toni Macacada",
    2123 : "Latônia Lata",
    2124 : "Massinha Mode Lar",
    2125 : "Ralf Desocupado",
    2126 : "Professora Gargalhada",
    2127 : "Nico N\xc3\xadquel",
    2128 : "Duda Doidinho",
    2129 : "Franco Furtado",
    2130 : "Fel\xc3\xadcia Ding-dong",
    2131 : "Espanadora Penas",
    2132 : "Joe Tromundo",
    2133 : "Dr. Fórico",
    2134 : "Simone Sil\xc3\xaancio",
    2135 : "Karla Rossel",
    2136 : "Saulo Risadinha",
    2137 : "Alegria Alegre",
    2138 : "João",
    2139 : "Beb\xc3\xaa Babá",
    2140 : "Gui Pescador",

    # Loopy Lane
    2201 : "Gerente Gil",
    2202 : "Shirley Vocezomba",
    2203 : lHQOfficerM,
    2204 : lHQOfficerM,
    2205 : lHQOfficerF,
    2206 : lHQOfficerF,
    2207 : "Saulo Sabichão",
    2208 : "Lucas Grude",
    2209 : "Rico Risada",
    2210 : "Chazinha",
    2211 : "Cláudia Cuspinho",
    2212 : "Est\xc3\xaavão Estranho",
    2213 : "Luciana da Roda",
    2214 : "Mano da Mancha",
    2215 : "Bob Bujão",
    2216 : "K\xc3\xaania Teviu",
    2217 : "João Tubarão",
    2218 : "Hilária Folha",
    2219 : "Chef Cabeça de Vento",
    2220 : "Carlos Cabeça de Ferro",
    2221 : "Flora Canudinho",
    2222 : "Fus\xc3\xadvel Mirim",
    2223 : "Gláucia Gargalhada",
    2224 : "Fábio Fumacinha",
    2225 : "Corcunda Pescador",

    # Punchline Place
    2301 : "Dr. Puxaperna",
    2302 : "Professor Balanço",
    2303 : "Enfermeira Enferma",
    2304 : lHQOfficerM,
    2305 : lHQOfficerM,
    2306 : lHQOfficerF,
    2307 : lHQOfficerF,
    2308 : "Nancy Veneno",
    2309 : "João Grandão",
    2311 : "Francisco da Graça",
    2312 : "Dra. Sens\xc3\xadvel",
    2313 : "Lucinda Pinta",
    2314 : "Lúcio Lançador",
    2315 : "Tatá Tasco",
    2316 : "Bárbara Bola",
    2318 : "Ronaldo Engraçaldo",
    2319 : "Tiraldo",
    2320 : "Alfredo Nham",
    2321 : "Bartô Pescador",

    #
    # Donald's Dock
    #

    # Donald's Dock Playground
    1001 : "Vendedor Willy",
    1002 : "Vendedor Billy",
    1003 : lHQOfficerM,
    1004 : lHQOfficerF,
    1005 : lHQOfficerM,
    1006 : lHQOfficerF,
    1007 : "Betão Calçalongas",
    # NPCFisherman
    1008 : "Vendedor da Loja de Animais",
    # NPCPetClerks
    1009 : "Vendedor Durão",
    1010 : "Vendedora Ron-ron",
    1011 : "Vendedora Blup",
    # NPCPartyPerson
    1012 : "Planejador de Festa Pickles",
    1013 : "Planejador de Festa Patty",

    # Barnacle Blvd.
    1101 : "Levi Legal",
    1102 : "Capitão Carlão",
    1103 : "Pedro Peixe",
    1104 : "Doutor Alá",
    1105 : "Almirante Gancho",
    1106 : "Dona Goma",
    1107 : "Carlo Caiado",
    1108 : lHQOfficerM,
    1109 : lHQOfficerF,
    1110 : lHQOfficerM,
    1111 : lHQOfficerF,
    1112 : "Gláucio Glubglub",
    1113 : "Adele Adernada",
    1114 : "Carlos Camarada",
    1115 : "Lúcia Lula",
    1116 : "Carla Craca",
    1117 : "Capitão Blargh",
    1118 : "Marinho Crespo",
    1121 : "Linda Terra Firme",
    1122 : "Salgado Pescado",
    1123 : "Enguia Elétrica",
    1124 : "João Farpa do Cais",
    1125 : "Arlene Além-mar",
    1126 : "Zé Silva Pescador",

    # Seaweed Street
    1201 : "Craca Bárbara",
    1202 : "Mário",
    1203 : "Salgado",
    1204 : "Marco Quebra-mar",
    1205 : lHQOfficerM,
    1206 : lHQOfficerF,
    1207 : lHQOfficerM,
    1208 : lHQOfficerF,
    1209 : "Professora Pranchinha",
    1210 : "Aiki Sopa",
    1211 : "Malo Mala",
    1212 : "Tomás L\xc3\xadngua de Trapo",
    1213 : "Bob Botinho",
    1214 : "Kátia Furacão",
    1215 : "Paula Profundeza",
    1216 : "Otto Ostra",
    1217 : "Ciça Caniço",
    1218 : "Toni Pac\xc3\xadfico",
    1219 : "Carlos Encalhado",
    1220 : "Carla Canal",
    1221 : "Alan Abrolhos",
    1222 : "Bob Abordo",
    1223 : "Lula Lulu",
    1224 : "Em\xc3\xadlia Enguia",
    1225 : "Est\xc3\xaavão Estivador",
    1226 : "Pedro Pé na Tábua",
    1227 : "Coral do Recife",
    1228 : "Junqueira Pescador",

    # Lighthouse Lane
    1301 : "Alice",
    1302 : "Moby",
    1303 : "Mário",
    1304 : "Martina",
    1305 : lHQOfficerM,
    1306 : lHQOfficerF,
    1307 : lHQOfficerM,
    1308 : lHQOfficerF,
    1309 : "Esponja do Mar",
    1310 : "Fernando Ferramenta",
    1311 : "Paulinha Ponta Cabeça",
    1312 : "Hélio Hélice",
    1313 : "Wilson Nó",
    1314 : "Fernando Enferrujado",
    1315 : "Doutora Correnteza",
    1316 : "Beth Rodopio",
    1317 : "Paula Poste",
    1318 : "Teófilo Bote",
    1319 : "Estácio Estaleiro",
    1320 : "Caio Calmaria",
    1321 : "Camila Cais",
    1322 : "Rachel Recheio",
    1323 : "Fred Fedido",
    1324 : "Pérola Profunda",
    1325 : "Sérgio Vira-latas",
    1326 : "Fel\xc3\xadcia Batatinha",
    1327 : "C\xc3\xadntia Tábua",
    1328 : "Lucas Linguado",
    1329 : "Conchita Alga Marina",
    1330 : "Porta Dor",
    1331 : "Rudy Rid\xc3\xadquilhas",
    1332 : "Polar Pescador",

    #
    # The Brrrgh
    #

    # The Brrrgh Playground
    3001 : "Frida Freezer",
    3002 : lHQOfficerM,
    3003 : lHQOfficerF,
    3004 : lHQOfficerM,
    3005 : lHQOfficerM,
    3006 : "Vendedor Breno",
    3007 : "Vendedora Brenda",
    3008 : "Paco Pacote",
    # NPCFisherman
    3009 : "Vendedor da Loja de Animais",
    # NPCPetClerks
    3010 : "Vendedor Saltitante",
    3011 : "Vendedora Glub",
    3012 : "Vendedor Kiko",
    # NPCPartyPerson
    3013 : "Planejador de Festa Pedro",
    3014 : "Planejador de Festa Penny",

    # Walrus Way
    3101 : "Seu Leão",
    3102 : "Tia Freezer",
    3103 : "Chicó",
    3104 : "Gorrete",
    3105 : "Fred Cavanhaque",
    3106 : "Pio Arrepio",
    3107 : "Patty Passaporte",
    3108 : "Tobi Tobogã",
    3109 : "Kate",
    3110 : "Franguinho",
    3111 : "Cão de Bico",
    3112 : "Pequeno Grande Ancião",
    3113 : "Américo Histérico",
    3114 : "Rico Arriscado",
    3115 : lHQOfficerM,
    3116 : lHQOfficerF,
    3117 : lHQOfficerM,
    3118 : lHQOfficerM,
    3119 : "Carlos K. B. Loempé",
    3120 : "Kiko Quiprocó",
    3121 : "João Eletrochoque",
    3122 : "Luci Lugar",
    3123 : "Francis Quebra Gelo",
    3124 : "Estileto Iceberg",
    3125 : "Coronel Mastiga",
    3126 : "João Jornada",
    3127 : "Aérea Inflada",
    3128 : "Jorge Palitinho",
    3129 : "Fátima Fôrma",
    3130 : "Sandy",
    3131 : "Patr\xc3\xadcio Preguiça",
    3132 : "Maria Cinza",
    3133 : "Dr. Congelado",
    3134 : "V\xc3\xadtor Vest\xc3\xadbulo",
    3135 : "\xc3\x8ania Sopada",
    3136 : "Susana Nimada",
    3137 : "Sr. Freezer",
    3138 : "Chefe Sopa Rala",
    3139 : "Vovó Ceroulas",
    3140 : "Luci Pescadora",

    # Sleet Street
    3201 : "Tia \xc3\x81rtica",
    3202 : "Tremendão",
    3203 : "Walter",
    3204 : "Dra. Vai C. V.",
    3205 : "Cabeção Kika",
    3206 : "Vidália VaVum",
    3207 : "Dr. Ban Guela",
    3208 : "Felipe Nervosinho",
    3209 : "Marcos Cem Graça",
    3210 : "\xc3\x81lvaro Asno",
    3211 : "Hilária Freezer",
    3212 : "Rogério Gélido",
    3213 : lHQOfficerM,
    3214 : lHQOfficerF,
    3215 : lHQOfficerM,
    3216 : lHQOfficerM,
    3217 : "Consuelo Suada",
    3218 : "Lu Lazul",
    3219 : "Bob BikeDupla",
    3220 : "Sr. Espirro",
    3221 : "Neli Neve",
    3222 : "Vera Vento Cortante",
    3223 : "Chapa",
    3224 : "Rita Raspadinha",
    3225 : "Foca Fofoca",
    3226 : "Papai Nó El",
    3227 : "Raiomundo de Sol",
    3228 : "Frida Calafrio",
    3229 : "Herm\xc3\xadnia Cinta",
    3230 : "Pedro Pedreira",
    3231 : "G. Lopicado",
    3232 : "Pescador Alberto",

    # Polar Place
    3301 : "Remendo Tecidos",
    3302 : "Pedro Urso",
    3303 : "Dr. Olhadelas",
    3304 : "Abrão o Abominável",
    3305 : "Mick Eimei",
    3306 : "Paula \xc3\x9arsula",
    # NPC Fisherman
    3307 : "Pescadora Frederica",
    3308 : "Roberto Injustus",
    3309 : "Botinha",
    3310 : "Professor Floco",
    3311 : "Connie Feras",
    3312 : "Haroldo Marcha",
    3313 : lHQOfficerM,
    3314 : lHQOfficerF,
    3315 : lHQOfficerM,
    3316 : lHQOfficerF,
    3317 : "Bete Beijoqueira",
    3318 : "João Caxemira",
    3319 : "Reinaldo Retifica",
    3320 : "Ester Espuma",
    3321 : "Paulo Picareta",
    3322 : "Luis Fluis",
    3323 : "Aurora Borealis",
    3324 : "Otto Dentetorto",
    3325 : "Dercy Balançalves",
    3326 : "Blanche",
    3327 : "Cacá Sado",
    3328 : "Sônia Sombria",
    3329 : "Edu Pisada",

    #
    # Minnie's Melody Land
    #

    # Minnie's Melody Land Playground
    4001 : "Mel Odia",
    4002 : lHQOfficerM,
    4003 : lHQOfficerF,
    4004 : lHQOfficerF,
    4005 : lHQOfficerF,
    4006 : "Vendedora Do-ré-mi",
    4007 : "Vendedor Fá-sol-lá-si",
    4008 : "Costureira Harmonia",
    # NPCFisherman
    4009 : "Vendedor da Loja de Animais",
    # NPCPetClerks
    4010 : "Vendedor Caco",
    4011 : "Vendedor Nilton",
    4012 : "Vendedora Flor do Nordeste",
    # NPCPartyPerson
    4013 : "Planejador de Festa Preston",
    4014 : "Planejadora de Festa Penélope",

    # Alto Ave.
    4101 : "Tom",
    4102 : "Fifi",
    4103 : "Dr. Triturador",
    4104 : lHQOfficerM,
    4105 : lHQOfficerF,
    4106 : lHQOfficerF,
    4107 : lHQOfficerF,
    4108 : "Clave",
    4109 : "Carlos",
    4110 : "Métrica Anã",
    4111 : "Tom Tum",
    4112 : "Fá",
    4113 : "Madame Boa Maneira",
    4114 : "Bino Desafino",
    4115 : "Bárbara de Sevilha",
    4116 : "Flávio Flautim",
    4117 : "Banda Lyn",
    4118 : "Faxineiro Abel",
    4119 : "Moz Arte",
    4120 : "Violante Almofada",
    4121 : "Geg\xc3\xaa Menor",
    4122 : "Mentolada do Baixo",
    4123 : "André Raio",
    4124 : "Renato Refrão",
    4125 : "Ondina Musical",
    4126 : "Melô Canto",
    4127 : "Fel\xc3\xadcia Podos",
    4128 : "Luciano Furo",
    4129 : "Carla Cad\xc3\xaancia",
    4130 : "Miguel Metal",
    4131 : "Abraão Armário",
    4132 : "Marta Marrom",
    4133 : "Paulo Popeline",
    4134 : "Davi Disco",
    4135 : "Carlo Canoro",
    4136 : "Patr\xc3\xadcia Pausa",
    4137 : "Toni Surdo",
    4138 : "Agudo Clave",
    4139 : "Harmonia Decrescente",
    4140 : "Daniel Desajeitado",
    4141 : "Pet Pescador",

    # Baritone Blvd.
    4201 : "Tina",
    4202 : "Barry",
    4203 : "Al\xc3\xaa Nhador",
    4204 : lHQOfficerM,
    4205 : lHQOfficerF,
    4206 : lHQOfficerF,
    4207 : lHQOfficerF,
    4208 : "Heidi",
    4209 : "Brega Galopante",
    4211 : "Carlo Concerto",
    4212 : "Detetive Marcha Fúnebre",
    4213 : "Franca Foley",
    4214 : "Paula Meia-ponta",
    4215 : "Mário Marcha a ré",
    4216 : "Bob Buzina",
    4217 : "Toni Bonitão",
    4218 : "Sônia Soprano",
    4219 : "Bruno Bar\xc3\xadtono",
    4220 : "D\xc3\xaanis Dedus",
    4221 : "Marcos Madrigal",
    4222 : "João da Silva",
    4223 : "Pâmela Ponto",
    4224 : "Jim das Selvas",
    4225 : "Vânia Vaia",
    4226 : "Samantha Garganta",
    4227 : "Cláudia Calada",
    4228 : "Augusto de Sopro",
    4229 : "Júnia Bombom",
    4230 : "Marcelo Martelo",
    4231 : "Stefanie Acordes",
    4232 : "Helder Hino",
    4233 : "Enzo Enjoado",
    4234 : "Mestre Guitarra",
    4235 : "Lauro Pescador",

    # Tenor Terrace
    4301 : "Cavaca",
    4302 : "Ana",
    4303 : "Léo",
    4304 : lHQOfficerM,
    4305 : lHQOfficerF,
    4306 : lHQOfficerF,
    4307 : lHQOfficerF,
    4308 : "Tábata",
    4309 : "Punk Ecas",
    4310 : "Mezza Soprana",
    4311 : "Chica Shake",
    4312 : "Paulo Palheta",
    4313 : "Mário Mudo",
    4314 : "Danuza Uza",
    4315 : "Maritza Tique Ataque",
    4316 : "Toni Tango",
    4317 : "Dedo Curto",
    4318 : "Bob Marlin",
    4319 : "Cátia Zuza",
    4320 : "Roberta P. Rock",
    4321 : "Edinho Verde",
    4322 : "Antoniota Musical",
    4323 : "Bárbara Balado",
    4324 : "Elen",
    4325 : "Ralf Rádio",
    4326 : "K\xc3\xadria Irrita",
    4327 : "Arm\xc3\xadnia Arranca Pele",
    4328 : "Wagner",
    4329 : "Teles Prompter",
    4330 : "Quarentino",
    4331 : "Mello Costello",
    4332 : "Ziggy",
    4333 : "Ubaldo",
    4334 : "Est\xc3\xaavão Expresso",
    4335 : "S\xc3\xadlvia Pescadora",

    #
    # Daisy Gardens
    #

    # Daisy Gardens Playground
    5001 : lHQOfficerM,
    5002 : lHQOfficerM,
    5003 : lHQOfficerF,
    5004 : lHQOfficerF,
    5005 : "Vendedora Moranguinho",
    5006 : "Vendedor Herbal",
    5007 : "Florinda Flores",
    # NPCFisherman
    5008 : "Vendedor da Loja de Animais",
    # NPCPetClerks
    5009 : "Vendedora Buba Tânica",
    5010 : "Vendedor Tony Grana",
    5011 : "Vendedor Duda Madeira",
    # NPCPartyPerson
    5012 : "Planejador de Festa Pierce",
    5013 : "Planejadora de Festa Peggy",

    # Elm Street
    5101 : "Sérgio",
    5102 : "Susana",
    5103 : "Flor\xc3\xaancio",
    5104 : "Borba Oleta",
    5105 : "João",
    5106 : "Barbeiro Tosque Ador",
    5107 : "Carteiro Felipe",
    5108 : "Funcionária Janete",
    5109 : lHQOfficerM,
    5110 : lHQOfficerM,
    5111 : lHQOfficerF,
    5112 : lHQOfficerF,
    5113 : "Dra. \xc3\x81lia e \xc3\x93lea",
    5114 : "Al Fácio Murcho",
    5115 : "Lua de Melão",
    5116 : "V\xc3\xadtor Vegetal",
    5117 : "Pétala",
    5118 : "Pipo K.",
    5119 : "João Medalhão",
    5120 : "Toupeira",
    5121 : "Em\xc3\xadlia Ervilha",
    5122 : "J. Jardim",
    5123 : "Diana Uva",
    5124 : "Olavo Orvalho",
    5125 : "Chu Chuá",
    5126 : "Madame Calado",
    5127 : "Poliana Pólen",
    5128 : "Suzana Seiva",
    5129 : "Salgueira Pescadora",

    # Maple Street
    5201 : "Joãozinho",
    5202 : "C\xc3\xadntia",
    5203 : "Lisa",
    5204 : "Ubaldo",
    5205 : "Maur\xc3\xadcio Leão",
    5206 : "Branco Vinho",
    5207 : "Sofia Seiva",
    5208 : "Samanta Pá",
    5209 : lHQOfficerM,
    5210 : lHQOfficerM,
    5211 : lHQOfficerF,
    5212 : lHQOfficerF,
    5213 : "Nabo Bobo",
    5214 : "Empolada Alérgica",
    5215 : "Clara Caules",
    5216 : "Fernando Fedido",
    5217 : "V\xc3\xadtor do Dedo Verde",
    5218 : "Francisco Framboesa",
    5219 : "Bi Ceps",
    5220 : "Luci Calçola",
    5221 : "Rosinha Flamingo",
    5222 : "Sandra Samambaia",
    5223 : "Paulo Ensopado",
    5224 : "Tio Campon\xc3\xaas",
    5225 : "Pâmela Pântana",
    5226 : "Mauro Musgo",
    5227 : "Begônia Malte",
    5228 : "Drago Di Lama",
    5229 : "Lili Pescadora",

    # Oak street
    5301 : lHQOfficerM,
    5302 : lHQOfficerM,
    5303 : lHQOfficerM,
    5304 : lHQOfficerM,
    5305 : "Cristal",
    5306 : "C. Postal",
    5307 : "Mo Fus",
    5308 : "Nely Nervo",
    5309 : "Rô Mann",
    5310 : "Timóteo",
    5311 : "Ju\xc3\xadza Gala",
    5312 : "Eug\xc3\xaanio",
    5313 : "Treinador Abobrinha",
    5314 : "Tia Miga",
    5315 : "Tio Lama",
    5316 : "Tio Batatinha",
    5317 : "Detetive Linda",
    5318 : "César",
    5319 : "Rose",
    5320 : "Márcia",
    5321 : "Professora Uva",
    5322 : "Rose Pescadora",

    #
    # Goofy's Speedway
    #

    #default  area
    #kart clerk
    8001 : "Grandep R\xc3\xaamio",
    8002 : "Keruk Orr\xc3\xaa",
    8003 : "Precisuv Encer",
    8004 : "En Chaela",

    #
    # Dreamland
    #

    # Dreamland Playground
    9001 : "Susana Pestana",
    9002 : "Dor Minhoco",
    9003 : "Sono Lento",
    9004 : lHQOfficerF,
    9005 : lHQOfficerF,
    9006 : lHQOfficerM,
    9007 : lHQOfficerM,
    9008 : "Vendedora Resona",
    9009 : "Vendedor Kisono",
    9010 : "Ultraje Velho",
    # NPCFisherman
    9011 : "Vendedor da Loja de Animais",
    # NPCPetClerks
    9012 : "Vendedora Sara Soneca",
    9013 : "Vendedora Gata na Lata",
    9014 : "Vendedor Cara Mujo",
    # NPCPartyPerson
    9015 : "Planejador de Festa Pedregulho",
    9016 : "Planejadora de Festa Pérola",

    # Lullaby Lane
    9101 : "Marcelo",
    9102 : "Mama",
    9103 : "Py Jama",
    9104 : "Dulce Lombra",
    9105 : "Professor Bocejo",
    9106 : "Máximo",
    9107 : "Aurora Ninho",
    9108 : "Pedro Pestana",
    9109 : "Dafne Sonolinda",
    9110 : "Gatária Soneca",
    9111 : "Elle \xc3\x89trica",
    9112 : "Denis Nar",
    9113 : "Tique Eustáquio",
    9114 : "Máki Agem",
    9115 : "Nen\xc3\xaa Crespo",
    9116 : "Dança com Carneirinhos",
    9117 : "Aurora Extra",
    9118 : "Celeste Estrelada",
    9119 : "Pedro",
    9120 : "Lúcia Lenta",
    9121 : "Serena Lençol Curto",
    9122 : "Paulo Pregado",
    9123 : "Ursolino de P. Lúcia",
    9124 : "Nana de Nina",
    9125 : "Dr. Turvo",
    9126 : "Jatha Cordada",
    9127 : "Tati U. Nidos",
    9128 : "Pedro Fuso",
    9129 : "Cátia Colcha",
    9130 : "Nico Penico",
    9131 : "Célia Sesta",
    9132 : lHQOfficerF,
    9133 : lHQOfficerF,
    9134 : lHQOfficerF,
    9135 : lHQOfficerF,
    9136 : "Tainha Pescador",

    # Pajama Place
    9201 : "Bernardo",
    9202 : "Carneiro",
    9203 : "Zezé",
    9204 : "Clara da Lua",
    9205 : "Bob Bocão",
    9206 : "Petra Pétala",
    9207 : "Denise Dreno",
    9208 : "Solano Sonolento",
    9209 : "Dr. Sedoso",
    9210 : "Mestre Mário",
    9211 : "Aurora",
    9212 : "Raio de Lua",
    9213 : "Gustavo Galo",
    9214 : "Dr. Soneca",
    9215 : "Dedé Descanso",
    9216 : "Cuca",
    9217 : "Linda Legal",
    9218 : "Matilda Madruga",
    9219 : "Condessa",
    9220 : "Ney Nervoso",
    9221 : "Zéfiro",
    9222 : "Vaqueiro George",
    9223 : "Vado Levado",
    9224 : "Cuca P. Gol",
    9225 : "Henriqueta Inquieta",
    9226 : "Guilherme Sonoleve",
    9227 : "Carlos Cabeceira",
    9228 : "Samuel Suspiro",
    9229 : "Rosa Sonada",
    9230 : "Lel\xc3\xaa",
    9231 : "Régis Rede",
    9232 : "Lua de Mel",
    9233 : lHQOfficerM,
    9234 : lHQOfficerM,
    9235 : lHQOfficerM,
    9236 : lHQOfficerM,
    9237 : "Jung Pescador",

    #
    # Funny Farm / Field Office
    #

    9301 : "Phil Bettur",
    9302 : "Emma Phatic",
    9303 : "GiggleMesh",
    9304 : "Anne Ville",
    9305 : "Bud Erfingerz",
    9306 : "J.S. Bark",
    9307 : "Bea Sharpe",
    9308 : "Otto Toon",
    9309 : "Al Capella",
    9310 : "Des Traction",
    9311 : "Dee Version",
    9312 : "Bo Nanapeel",
    7001 : "N. Prisoned",
    7002 : "R.E. Leaseme",
    7003 : "Lemmy Owte",
    7004 : "T. Rapped",
    7005 : "Little Helphere",
    7006 : "Gimmy Ahand",
    7007 : "Dewin Tymme",
    7008 : "Ima Cagedtoon",
    7009 : "Jimmy Thelock",

    # Tutorial IDs start at 20000, and are not part of this table.
    # Don't add any Toon id's at 20000 or above, for this reason!
    # Look in TutorialBuildingAI.py for more details.

    }

# These building titles are output from the DNA files
# Run ppython $TOONTOWN/src/dna/DNAPrintTitles.py to generate this list
# DO NOT EDIT THE ENTRIES HERE -- EDIT THE ORIGINAL DNA FILE
zone2TitleDict = {
    # titles for: phase_4/dna/toontown_central_sz.dna
    2513 : ("PrefeiToona", ""),
    2514 : ("Banco de Toontown", ""),
    2516 : ("Escola de Toontown", ""),
    2518 : ("Biblioteca de Toontown", ""),
    2519 : (lGagShop, ""),
    2520 : (lToonHQ, ""),
    2521 : (lClothingShop, ""),
    2522 : (lPetShop, ""),
    # titles for: phase_5/dna/toontown_central_2100.dna
    2601 : ("Restaurações Dentárias Todo Sorrisos", ""),
    2602 : ("", ""),
    2603 : ("Mineradores Espirituosos", ""),
    2604 : ("Lavanderia Lavou está Novo", ""),
    2605 : ("Fábrica de Sinalização de Toontown", ""),
    2606 : ("", ""),
    2607 : ("Feijões Saltadores", ""),
    2610 : ("Dr. Tom Besteira", ""),
    2611 : ("", ""),
    2616 : ("Loja de Disfarces Bigode Bizarro", ""),
    2617 : ("Feitos Idiotas", ""),
    2618 : ("A Encarnação Deve Continuar", ""),
    2621 : ("Aviões de Papel", ""),
    2624 : ("Brutamontes Felizes", ""),
    2625 : ("Casa da Torta Azeda", ""),
    2626 : ("Restauração de Piadas do Bob", ""),
    2629 : ("A Casa da Risada", ""),
    2632 : ("Curso de Palhaços", ""),
    2633 : ("Casa de Chá Chapinha", ""),
    2638 : ("Casa de Brinquedos de Toontown", ""),
    2639 : ("Truques e Macaquices", ""),
    2643 : ("Conservas Conservadas", ""),
    2644 : ("Pregadinhas de Peça", ""),
    2649 : ("Loja de Diversões e Jogos", ""),
    2652 : ("", ""),
    2653 : ("", ""),
    2654 : ("Curso de Risada", ""),
    2655 : ("Financeira Dinheiro Feliz", ""),
    2656 : ("Carros de Palhaço Usados", ""),
    2657 : ("Pegadinhas do Franco", ""),
    2659 : ("Campainhas Ding-dong para o Mundo", ""),
    2660 : ("Máquinas de Cosquinhas", ""),
    2661 : ("Doces Joe", ""),
    2662 : ("Dr. E. U. Fórico", ""),
    2663 : ("Cinerama de Toontown", ""),
    2664 : ("M\xc3\xadmicas Divertidas", ""),
    2665 : ("Ag\xc3\xaancia de Viagens K. Rossel", ""),
    2666 : ("Posto de Gás Hilariante", ""),
    2667 : ("A Folha da Alegria", ""),
    2669 : ("Balões do João", ""),
    2670 : ("Sopa no Garfo", ""),
    2671 : ("", ""),
    # titles for: phase_5/dna/toontown_central_2200.dna
    2701 : ("", ""),
    2704 : ("Cinemas Multiplex", ""),
    2705 : ("Instrumentos Barulhentos do Sabichão", ""),
    2708 : ("Cola Azul", ""),
    2711 : ("Correio de Toontown", ""),
    2712 : ("Café do Risada", ""),
    2713 : ("Café da Madrugargalhada", ""),
    2714 : ("CinePlex Lesado", ""),
    2716 : ("Sopas e Surtos", ""),
    2717 : ("Latas engarrafadas", ""),
    2720 : ("Oficina do Chilique", ""),
    2725 : ("", ""),
    2727 : ("Garrafas e Conservas do Gasoso", ""),
    2728 : ("Sorvete Sumiço", ""),
    2729 : ("Peixinhos Dourados Ki-late", ""),
    2730 : ("Not\xc3\xadcias Divertidas", ""),
    2731 : ("", ""),
    2732 : ("Espaguete Maluquete", ""),
    2733 : ("Pipas de Ferro", ""),
    2734 : ("Copos de Leite Chupa-chupa", ""),
    2735 : ("Casa do Cabum", ""),
    2739 : ("Restauração de Gargalhadas", ""),
    2740 : ("Rojões Usados", ""),
    2741 : ("", ""),
    2742 : ("", ""),
    2743 : ("Lavagem a Seco Beca", ""),
    2744 : ("", ""),
    2747 : ("Tinta Vis\xc3\xadvel", ""),
    2748 : ("Zombarias para Gargalhadas", ""),
    # titles for: phase_5/dna/toontown_central_2300.dna
    2801 : ("Estofados Iupii", ""),
    2802 : ("Bolas de Ferro Infláveis", ""),
    2803 : ("Karnaval Kid", ""),
    2804 : ("Dr. Puxaperna, Ortopedista", ""),
    2805 : ("", ""),
    2809 : ("Academia Graça da Piada", ""),
    2814 : ("Teatro de Toontown", ""),
    2818 : ("A Torta Voadora", ""),
    2821 : ("", ""),
    2822 : ("Sandu\xc3\xadches de Frango de Borracha", ""),
    2823 : ("Sorvetes e Sundaes Divertidos", ""),
    2824 : ("Cinema Palácio do Auge da Graça", ""),
    2829 : ("Truques e Trocadilhos", ""),
    2830 : ("Tiradas Rápidas", ""),
    2831 : ("Casa do Sorriso Amarelo do Professor Balanço", ""),
    2832 : ("", ""),
    2833 : ("", ""),
    2834 : ("Sala de Emerg\xc3\xaancia Osso Bom", ""),
    2836 : ("", ""),
    2837 : ("Centro de Estudos Rá Rá Rá", ""),
    2839 : ("Grude Massas", ""),
    2841 : ("", ""),
    # titles for: phase_6/dna/donalds_dock_sz.dna
    1506 : (lGagShop, ""),
    1507 : (lToonHQ, ""),
    1508 : (lClothingShop, ""),
    1510 : (lPetShop, ""),
    # titles for: phase_6/dna/donalds_dock_1100.dna
    1602 : ("Salva-vidas Usados", ""),
    1604 : ("Lavagem a Seco Roupa de Mergulho", ""),
    1606 : ("Conserto de Relógios do Gancho", ""),
    1608 : ("Bugigangas a Vela", ""),
    1609 : ("Iscas e Petiscos", ""),
    1612 : ("Banco Moedinha no Convés", ""),
    1613 : ("Lula Ki Pro Quo, Advogados", ""),
    1614 : ("Butique Unha Afiada", ""),
    1615 : ("E a\xc3\xad, Galera?", ""),
    1616 : ("Salão de Beleza Barba Azul", ""),
    1617 : ("\xc3\x93tica Olha Lá", ""),
    1619 : ("Arboristas Desembarcar!", ""),
    1620 : ("Da Proa \xc3\xa0 Popa", ""),
    1621 : ("Academia Castelo de Popa", ""),
    1622 : ("Artigos Elétricos Isca Interruptora", ""),
    1624 : ("Reparos de Pescadas na Hora", ""),
    1626 : ("Roupas de Gala Salmão Encantado", ""),
    1627 : ("Atacado de Bússolas do Levi Legal", ""),
    1628 : ("Pianos Atum", ""),
    1629 : ("", ""),
    # titles for: phase_6/dna/donalds_dock_1200.dna
    1701 : ("Creche Peixinho Feliz", ""),
    1703 : ("Restaurante China Prancha", ""),
    1705 : ("Velas \xc3\xa0 Venda", ""),
    1706 : ("Pasta de Amendoim e \xc3\x81gua-viva", ""),
    1707 : ("Presentes Golfinho Fofinho", ""),
    1709 : ("Veleiros e Gelatinas", ""),
    1710 : ("Liquidação das Cracas", ""),
    1711 : ("Restaurante Fundo do Mar", ""),
    1712 : ("Academia da Geração Saúde", ""),
    1713 : ("Mercado Carta Marinha do Mário", ""),
    1714 : ("Hotel do Otto", ""),
    1716 : ("Roupas de Banho Sereias", ""),
    1717 : ("Curso de Navegação \xc3\x81guas do Pac\xc3\xadfico", ""),
    1718 : ("Serviços de Táxi Banco de Areia", ""),
    1719 : ("Empresas Correntes do Sul", ""),
    1720 : ("A Loja do Molinete", ""),
    1721 : ("Armarinho Marinho", ""),
    1723 : ("Alga Marinha do Lula", ""),
    1724 : ("A Enguia Moderna", ""),
    1725 : ("Centro de Caranguejos Pré-fabricados do Salgado", ""),
    1726 : ("Cerveja Preta Flutuante", ""),
    1727 : ("Rema aqui, Rema lá", ""),
    1728 : ("Caranguejos-ferradura Boa Sorte", ""),
    1729 : ("", ""),
    # titles for: phase_6/dna/donalds_dock_1300.dna
    1802 : ("Nada como Náutica", ""),
    1804 : ("Ginásio Mexilhão da Praia", ""),
    1805 : ("Caixa de Ferramentas Lanches", ""),
    1806 : ("Loja de Chapéus Emborcado", ""),
    1807 : ("Loja do Hélice", ""),
    1808 : ("Nós Samãe", ""),
    1809 : ("Balde Enferrujado", ""),
    1810 : ("Administração de Âncoras", ""),
    1811 : ("Canoa para Lá, Canoa para Cá?", ""),
    1813 : ("Pressão do Pier Consultoria", ""),
    1814 : ("Parada do \xc3\x93", ""),
    1815 : ("Qual é, galerinha?", ""),
    1818 : ("Café dos Sete Mares", ""),
    1819 : ("Restaurante Cais", ""),
    1820 : ("Loja de Pegadinhas Linha e Anzol", ""),
    1821 : ("Conservas Rei Netuno", ""),
    1823 : ("Assados Ostra", ""),
    1824 : ("Remo Cachorrinho", ""),
    1825 : ("Mercado de Peixes Cavala Trotante!", ""),
    1826 : ("Armários Embutidos do Mário Metido", ""),
    1828 : ("Mansão da Alice Cascalhão", ""),
    1829 : ("Loja de Esculturas Piscicultura", ""),
    1830 : ("Linguados e Perdidos", ""),
    1831 : ("Alga Mais em sua Casa", ""),
    1832 : ("Hipermercado Mastro do Moby", ""),
    1833 : ("Alfaiataria sob Medida Seu Mastro", ""),
    1834 : ("Rid\xc3\xadquilhas!", ""),
    1835 : ("", ""),
    # titles for: phase_6/dna/minnies_melody_land_sz.dna
    4503 : (lGagShop, ""),
    4504 : (lToonHQ, ""),
    4506 : (lClothingShop, ""),
    4508 : (lPetShop, ""),
    # titles for: phase_6/dna/minnies_melody_land_4100.dna
    4603 : ("Baterias do Tomtom", ""),
    4604 : ("A Quatro Mãos", ""),
    4605 : ("Violinos da Fifi", ""),
    4606 : ("Casa da Castanhola", ""),
    4607 : ("Trajes de Gala Toon", ""),
    4609 : ("Teclas de Piano Dó-ré-mi", ""),
    4610 : ("O Bom Refrão", ""),
    4611 : ("Faqueiros Diapasão", ""),
    4612 : ("Cl\xc3\xadnica Dentária Dr. Triturador", ""),
    4614 : ("Barbearia Musical", ""),
    4615 : ("Pizza do Flautim", ""),
    4617 : ("Bandolins Animados", ""),
    4618 : ("Banheiros Públicos", ""),
    4619 : ("Mar Cação", ""),
    4622 : ("Travesseiros Descanso de Queixo", ""),
    4623 : ("Afiação Bemol", ""),
    4625 : ("Pasta de Dente Tuba", ""),
    4626 : ("Notas Musicais", ""),
    4628 : ("Seguradora Acidental", ""),
    4629 : ("Pratos de Papel Refrão", ""),
    4630 : ("A Música é o nosso Forte", ""),
    4631 : ("Aux\xc3\xadlio Canto Neiras", ""),
    4632 : ("Loja do Rock", ""),
    4635 : ("Not\xc3\xadcias do Tenor", ""),
    4637 : ("A Boa Escala", ""),
    4638 : ("Loja do Heavy Metal", ""),
    4639 : ("Antiguidades Oitenta", ""),
    4641 : ("Jornal dos Blues", ""),
    4642 : ("Lavagem a Seco Beca", ""),
    4645 : ("Clube 88", ""),
    4646 : ("", ""),
    4648 : ("Mudanças Carregando Toons", ""),
    4649 : ("", ""),
    4652 : ("Loja de Conveni\xc3\xaancia Ponto Final", ""),
    4653 : ("", ""),
    4654 : ("Telhados Volume Perfeito", ""),
    4655 : ("Escola de Culinária do Terr\xc3\xadvel Chef Agudo", ""),
    4656 : ("", ""),
    4657 : ("Barbearia Quarteto", ""),
    4658 : ("Pianos Submersos", ""),
    4659 : ("", ""),
    # titles for: phase_6/dna/minnies_melody_land_4200.dna
    4701 : ("Escola de Dança Jumento Sentimento", ""),
    4702 : ("Timbre! Artigos para Lenhadores", ""),
    4703 : ("A Mala Madeus", ""),
    4704 : ("Concertos de Concertina da Tina", ""),
    4705 : ("Zarpou fora", ""),
    4707 : ("Estúdio de Efeitos Sonoros Doppler", ""),
    4709 : ("Artigos de Montanhismo Pli\xc3\xaa", ""),
    4710 : ("Auto-escola Pouca Polca", ""),
    4712 : ("Borracharia Dó do Murcho", ""),
    4713 : ("Moda Fina Masculina Desafina", ""),
    4716 : ("Gaitas de Quatro Segmentos", ""),
    4717 : ("Seguradora de Automóveis Barateira Bar\xc3\xadtono", ""),
    4718 : ("Peças para Chopp-in e Outros Artigos para Cozinha", ""),
    4719 : ("Casas-móveis Madrigal", ""),
    4720 : ("D\xc3\xaa um Nome a este Toon", ""),
    4722 : ("Substitutos Abertura", ""),
    4723 : ("Artigos para Parquinhos Infantis Ex-condesconde", ""),
    4724 : ("Moda Infantil Inci Dental", ""),
    4725 : ("O Barbeiro Bar\xc3\xadtono", ""),
    4727 : ("Bordados Corda Vocal", ""),
    4728 : ("Solo Vocal Não dá pra Ouvir", ""),
    4729 : ("Livraria Oboé", ""),
    4730 : ("Sebo de Letras de Músicas", ""),
    4731 : ("Tons dos Toons", ""),
    4732 : ("Companhia Teatral Prega Peça", ""),
    4733 : ("", ""),
    4734 : ("", ""),
    4735 : ("Acorde Não!", ""),
    4736 : ("Planejamento Matrimonial Casal Hino Esperado", ""),
    4737 : ("Lonas Harpa", ""),
    4738 : ("Presentes Cantata do Tatá", ""),
    4739 : ("", ""),
    # titles for: phase_6/dna/minnies_melody_land_4300.dna
    4801 : ("Ponto do Punk", ""),
    4803 : ("Serviços de Governança Que Mezza!", ""),
    4804 : ("Curso de Barman Shake Shake Shake", ""),
    4807 : ("Não Quebre o Braço", ""),
    4809 : ("Não Com Verso!", ""),
    4812 : ("", ""),
    4817 : ("Loja de Animais Trin Canário", ""),
    4819 : ("Cavaquinhos da Cavaca", ""),
    4820 : ("", ""),
    4821 : ("Cruzeiros da Ana", ""),
    4827 : ("Relógios Ritmo Cadente", ""),
    4828 : ("Sapatos Masculinos Rima", ""),
    4829 : ("Bolas de Canhão Vaga Ner", ""),
    4835 : ("Fundamentos Musicais para Felinos Felizes", ""),
    4836 : ("Regalias do Reggae", ""),
    4838 : ("Escola de Música K. Zuza", ""),
    4840 : ("Bebidas Musicais Pop Rock", ""),
    4841 : ("Bandoleiro Bandolins!", ""),
    4842 : ("Corporação Sincopação", ""),
    4843 : ("", ""),
    4844 : ("Motocicletas Com Notação", ""),
    4845 : ("Elegias Elegantes da Elen", ""),
    4848 : ("Financeira Cordas de Dinheiro", ""),
    4849 : ("", ""),
    4850 : ("Hipoteca Cordas Emprestadas", ""),
    4852 : ("Arranca-peles Flauta Florida", ""),
    4853 : ("Para-choques do Léo Guitarra", ""),
    4854 : ("V\xc3\xaddeos de Violinos Vocacionais Wagner", ""),
    4855 : ("Rede de Televisão Teleouvisa", ""),
    4856 : ("", ""),
    4862 : ("Quatrilhos Quintessenciais do Quarentino", ""),
    4867 : ("Celos Amarelos do Costello", ""),
    4868 : ("", ""),
    4870 : ("Zoológico de Ziriguidum do Ziggy", ""),
    4871 : ("Humbuckers \xc3\x9anicos do Ubaldo", ""),
    4872 : ("Braços sem Estresse do Estevão Expresso", ""),
    4873 : ("", ""),
    # titles for: phase_8/dna/daisys_garden_sz.dna
    5501 : (lGagShop, ""),
    5502 : (lToonHQ, ""),
    5503 : (lClothingShop, ""),
    5505 : (lPetShop, ""),
    # titles for: phase_8/dna/daisys_garden_5100.dna
    5601 : ("Exames de Vista Olho do Alho", ""),
    5602 : ("Gravatas do Sérgio Sufocado", ""),
    5603 : ("Verde que te Quero Verdura", ""),
    5604 : ("Loja de Noivas Mel e Lão", ""),
    5605 : ("Sobre Mesas e Cadeiras", ""),
    5606 : ("Pétalas", ""),
    5607 : ("Correios Adubo Expresso", ""),
    5608 : ("Toca da Pipoca", ""),
    5609 : ("Tesouro dos Dentes de Alho de Ouro", ""),
    5610 : ("Aulas de Boxe da Susana Olhos Negros", ""),
    5611 : ("Piadas do Toupeira", ""),
    5613 : ("Barbeiros Tosa Completa", ""),
    5615 : ("Ração para Pássaros do Flor\xc3\xaancio", ""),
    5616 : ("Pousada Pouso da Coruja", ""),
    5617 : ("Borboletas do Borba Oleta", ""),
    5618 : ("Ervilhas e Milhas", ""),
    5619 : ("Pés de feijão do João", ""),
    5620 : ("Pousada Pá de Coisa", ""),
    5621 : ("Uvinhas da Ira", ""),
    5622 : ("Loja de Bicicletas Bem-me-quer", ""),
    5623 : ("Banheiras para Pássaros Bolhinhas Aladas", ""),
    5624 : ("Bico Calado", ""),
    5625 : ("Os Abelhudos", ""),
    5626 : ("Artesanato P\xc3\xadnus", ""),
    5627 : ("", ""),
    # titles for: phase_8/dna/daisys_garden_5200.dna
    5701 : ("Do In\xc3\xadcio ao Figo", ""),
    5702 : ("Ancinho do Joãozinho", ""),
    5703 : ("Fotos C\xc3\xadntia", ""),
    5704 : ("Carros Usados Lisa Lima", ""),
    5705 : ("Móveis Urtigas", ""),
    5706 : ("Joalheiros 14 Ki Latas", ""),
    5707 : ("Fruta Musical", ""),
    5708 : ("Ag\xc3\xaancia de Viagens Erva da Ninha", ""),
    5709 : ("Cortadores de Grama Ré U. Vassintética", ""),
    5710 : ("Academia Durão", ""),
    5711 : ("Roupas Íntimas Jardim de Inverno", ""),
    5712 : ("Estátuas Idiotas", ""),
    5713 : ("Mãos \xc3\xa0 Obra", ""),
    5714 : ("\xc3\x81gua Mineral Chuva de Verão", ""),
    5715 : ("Not\xc3\xadcias do Campo", ""),
    5716 : ("Hipotecas Folhas Ca\xc3\xaddas", ""),
    5717 : ("Seivas Florais", ""),
    5718 : ("Animais Exóticos Mauricinho Leão", ""),
    5719 : ("Investigadores Particulares Cara que Manchão!", ""),
    5720 : ("Moda Masculina Bran Covinho", ""),
    5721 : ("Restaurante Rota 66", ""),
    5725 : ("Cervejaria da Cevada", ""),
    5726 : ("Terra Adubada do Ubaldo", ""),
    5727 : ("Financeira Toupeira Encurralada", ""),
    5728 : ("", ""),
    # titles for: phase_8/dna/daisys_garden_5300.dna
    5802 : (lToonHQ, ""),
    5804 : ("Vazar ou não Vazar?", ""),
    5805 : ("Correio da Lesma", ""),
    5809 : ("Escola de Palhaços Fungos", ""),
    5810 : ("Mela o Melado", ""),
    5811 : ("Pousada Al Face a Face", ""),
    5815 : ("Rural", ""),
    5817 : ("Maçãs e Laranjas", ""),
    5819 : ("Jeans Vagem Verde", ""),
    5821 : ("Academia Amassado e Esticado", ""),
    5826 : ("Artigos para o Cultivo de Formigas", ""),
    5827 : ("Promoção de Aterrar", ""),
    5828 : ("Móveis Batatinha Quando Nasce", ""),
    5830 : ("Espalhado o Babado", ""),
    5833 : ("Restaurante Saladas", ""),
    5835 : ("Café Colonial Flores do Campo", ""),
    5836 : ("Tubulações e \xc3\x81guas de Márcia", ""),
    5837 : ("Curso de Enólogo", ""),
    # titles for: phase_8/dna/donalds_dreamland_sz.dna
    9501 : ("Biblioteca da Canção de Ninar", ""),
    9503 : ("O Bar da Soneca", ""),
    9504 : (lGagShop, ""),
    9505 : (lToonHQ, ""),
    9506 : (lClothingShop, ""),
    9508 : (lPetShop, ""),
    # titles for: phase_8/dna/donalds_dreamland_9100.dna
    9601 : ("Pousada A. Ninho", ""),
    9602 : ("Dois Dedos de Prosa com Morfeu pelo Preço de Um", ""),
    9604 : ("Sofá-cama Amarelo do Marcelo", ""),
    9605 : ("Travessa da Canção de Ninar, 323", ""),
    9607 : ("Pijamas Bahamas da Mama", ""),
    9608 : ("Erva-de-gato para Tirar um Cochilo", ""),
    9609 : ("Sono de Pedra por uma Bagatela", ""),
    9613 : ("Relojoeiros das Alturas", ""),
    9616 : ("Companhia Elétrica Luzes Apagadas", ""),
    9617 : ("Travessa da Canção de Ninar, 212", ""),
    9619 : ("Relaxe ao Máximo", ""),
    9620 : ("Serviços de Táxi Py Jama", ""),
    9622 : ("Relógios Sono Atrasado", ""),
    9625 : ("Salão de Beleza Enrolado Crespo", ""),
    9626 : ("Travessa da Canção de Ninar, 818", ""),
    9627 : ("A Tenda dos Sonhos", ""),
    9628 : ("Calendários Já Chega por Hoje", ""),
    9629 : ("Travessa da Canção de Ninar, 310", ""),
    9630 : ("Pedreira Sono de Pedra", ""),
    9631 : ("Conserto de Relógios Inatividade", ""),
    9633 : ("Sala de Projeção da Sonholândia", ""),
    9634 : ("Colchões Descanso da Mente", ""),
    9636 : ("Seguradora Insônia", ""),
    9639 : ("Casa de Hibernação", ""),
    9640 : ("Travessa da Canção de Ninar, 805", ""),
    9642 : ("Serraria Lombeira da Madeira", ""),
    9643 : ("Exames de Vista Olho Fechado", ""),
    9644 : ("Guerras de Travesseiro Noturnas", ""),
    9645 : ("Pousada Unidos Venceremos", ""),
    9647 : ("Loja de Ferragens Faça a sua Cama", ""),
    9649 : ("Ranking do Ronco", ""),
    9650 : ("Travessa da Canção de Ninar, 714", ""),
    9651 : ("Com Muito ou com Ronco", ""),
    9652 : ("", ""),
    # titles for: phase_8/dna/donalds_dreamland_9200.dna
    9703 : ("Ag\xc3\xaancia de Viagens Vôo Noturno", ""),
    9704 : ("Loja de Animais Coruja Noturna", ""),
    9705 : ("Oficina Dormindo ao Volante", ""),
    9706 : ("Cl\xc3\xadnica Dentária Fada do Dente", ""),
    9707 : ("Centro de Jardinagem Bocejo Matutino", ""),
    9708 : ("Floricultura Leito de Rosas", ""),
    9709 : ("Encanamentos Sonho do Bombeiro", ""),
    9710 : ("Exames de Vista REM", ""),
    9711 : ("Companhia Telefônica Despertador", ""),
    9712 : ("Contagem de Ovelhas - Nós Contamos para Voc\xc3\xaa!", ""),
    9713 : ("Pisca-duro, Pestana e Cabeçada, Advogados", ""),
    9714 : ("Artigos Mar\xc3\xadtimos Barco dos Sonhos", ""),
    9715 : ("Banco A Fraldinha de Dormir", ""),
    9716 : ("Pipi na Cama Festas", ""),
    9717 : ("Padaria Sonho \xc3\xa0 Dúzia", ""),
    9718 : ("Sandu\xc3\xadches A Cuca Vai Pegar", ""),
    9719 : ("Fábrica de Travesseiros Tatu", ""),
    9720 : ("Fala Dormindo Fonoaudiólogos", ""),
    9721 : ("Tapetes Aconchego", ""),
    9722 : ("Ag\xc3\xaancia de Talentos Sonho de Menina", ""),
    9725 : ("Pijamas Saco de Gato", ""),
    9727 : ("Cochilou, Dançou", ""),
    9736 : ("Ag\xc3\xaancia de Empregos Trabalho dos Sonhos", ""),
    9737 : ("Escola de Dança Matilda Madruga", ""),
    9738 : ("Casa de Zzzzzs", ""),
    9740 : ("Escola de Esgrima Naná", ""),
    9741 : ("Deu Pulga na Cama Exterm\xc3\xadnio de Insetos", ""),
    9744 : ("Creme para Rugas Chega de Insônia", ""),
    9752 : ("Petroleira Meia-Noite", ""),
    9753 : ("Sorveteria Luar Gelado", ""),
    9754 : ("Passeios de Pônei Cavalgada Noturna", ""),
    9755 : ("Cinemas Cama Voadora", ""),
    9756 : ("", ""),
    9759 : ("Salão de Beleza Bela Adormecida", ""),
    # titles for: phase_8/dna/the_burrrgh_sz.dna
    3507 : (lGagShop, ""),
    3508 : (lToonHQ, ""),
    3509 : (lClothingShop, ""),
    3511 : (lPetShop, ""),
    # titles for: phase_8/dna/the_burrrgh_3100.dna
    3601 : ("Companhia Elétrica Esplendor do Norte", ""),
    3602 : ("Gorros do Pólo Norte", ""),
    3605 : ("", ""),
    3607 : ("Mago do Lago Congelado", ""),
    3608 : ("Existe um Lugar", ""),
    3610 : ("Hipermercado de Sapatos de Esquimó Quiprocó", ""),
    3611 : ("Rodinho do Leão Marinho", ""),
    3612 : ("Design de Iglus", ""),
    3613 : ("Cicle Geloso", ""),
    3614 : ("Indústria de Cereais Flocos de Neve", ""),
    3615 : ("Pastéis de Forno Lindo Alasca", ""),
    3617 : ("Passeios de Balão Vento Frio", ""),
    3618 : ("Consultoria de Gestão de Crises Grande Coisa!", ""),
    3620 : ("Cl\xc3\xadnica do Esqui", ""),
    3621 : ("Sorveteria Gelo Derretido", ""),
    3622 : ("", ""),
    3623 : ("Indústria de Pães Torradinha", ""),
    3624 : ("Sanduicheria Abaixo de Zero", ""),
    3625 : ("Aquecedores Tia Freezer", ""),
    3627 : ("Canil São Bernardo", ""),
    3629 : ("Restaurante Sopa de Ervilhas", ""),
    3630 : ("Ag\xc3\xaancia de Viagens Com Gelo em Londres, Com Gelo na França", ""),
    3634 : ("Teleférico Boa Vista", ""),
    3635 : ("Lenha Usada", ""),
    3636 : ("Promoção de Arrepios", ""),
    3637 : ("Skates da Kate", ""),
    3638 : ("Tobogã da Lã", ""),
    3641 : ("Trenó do Chicó", ""),
    3642 : ("\xc3\x93tica Olho do Furacão", ""),
    3643 : ("Salão Bola de Neve", ""),
    3644 : ("Cubos de Gelo Derretidos", ""),
    3647 : ("Loja de Smokings Pinguim Animado", ""),
    3648 : ("Sorvete Instantâneo", ""),
    3649 : ("Hambrrrgers", ""),
    3650 : ("Antiguidades Antárctica", ""),
    3651 : ("Salsichas Congeladas do Fred Barbicha", ""),
    3653 : ("Joalheria Cristal do Gelo", ""),
    3654 : ("", ""),
    # titles for: phase_8/dna/the_burrrgh_3200.dna
    3702 : ("Armazém do Inverno", ""),
    3703 : ("", ""),
    3705 : ("Cicle Pingo Congelado para Dois", ""),
    3706 : ("Fábrica de Refrigerantes Treme-treme", ""),
    3707 : ("Neve Doce Neve", ""),
    3708 : ("Loja do Pluto", ""),
    3710 : ("Temperatura em Queda Refeições", ""),
    3711 : ("", ""),
    3712 : ("Vai por Gelo Abaixo", ""),
    3713 : ("Dentista Abaixo de Zero Tiritante", ""),
    3715 : ("Casa de Sopas Tia \xc3\x81rtica", ""),
    3716 : ("Estrada de Sal e Pimenta", ""),
    3717 : ("A Lasca Verbal", ""),
    3718 : ("Designer de Câmaras de Ar", ""),
    3719 : ("Cubo de Gelo no Palitinho", ""),
    3721 : ("Liquidação de Tobogãs Cabeção", ""),
    3722 : ("Loja de Esquis Coelhinho de Neve", ""),
    3723 : ("Bolas de Neve Tremendão", ""),
    3724 : ("Fatos e Fofocas", ""),
    3725 : ("O Nó do Trenó", ""),
    3726 : ("Cobertores com Energia Solar", ""),
    3728 : ("Tratores de Neve Anta Lenta", ""),
    3729 : ("", ""),
    3730 : ("Compra e Venda de Bonecos de Neve", ""),
    3731 : ("Lareiras Portáteis", ""),
    3732 : ("O Nariz Congelado", ""),
    3734 : ("Exames de Vista C. V. Gelo", ""),
    3735 : ("Capas de Gelo Polar", ""),
    3736 : ("Cubos de Gelo com Zelo", ""),
    3737 : ("Restaurante Montanha Abaixo", ""),
    3738 : ("Aquecimento - Aproveite Enquanto está Quente", ""),
    3739 : ("", ""),
    # titles for: phase_8/dna/the_burrrgh_3300.dna
    3801 : (lToonHQ, ""),
    3806 : ("Linha de Comida Alpina", ""),
    3807 : ("Sombras de Marmota Usadas", ""),
    3808 : ("A Cabana Suadoura", ""),
    3809 : ("Elvira Tão Bem", ""),
    3810 : ("O Bom Edredom", ""),
    3811 : ("Seu Anjo de Neve", ""),
    3812 : ("Gatinhos de Luvas", ""),
    3813 : ("Botas de Neve Essenciais", ""),
    3814 : ("Banca de Refrigerantes Gás-na-Boca", ""),
    3815 : ("O Chalé da Peruca", ""),
    3816 : ("Viste o Visco", ""),
    3817 : ("Clube de Trilha de Inverno do Pa\xc3\xads das Maravilhas", ""),
    3818 : ("A Barraca das Pás", ""),
    3819 : ("Serviço de Chaminés Sopro Limpo", ""),
    3820 : ("Brancura de Neve", ""),
    3821 : ("Férias Hibernantes", ""),
    3823 : ("Fundações e Precipitações", ""),
    3824 : ("Nozes Assadas na Fogueira", ""),
    3825 : ("Chapéus do Gato Legal", ""),
    3826 : ("Ai, Minhas Galochas!", ""),
    3827 : ("Grinaldas Corais", ""),
    3828 : ("Terra do Boneco de Neve", ""),
    3829 : ("\xc3\x81rea dos Pinheiros", ""),
    3830 : ("Desembaçamento de \xc3\x93culos Espere-e-Veja", ""),
    }

# DistributedCloset.py
ClosetTimeoutMessage = "Sinto muito, o tempo\n acabou."
ClosetNotOwnerMessage = "Este não é o seu armário, mas voc\xc3\xaa pode experimentar as roupas."
ClosetPopupOK = lOK
ClosetPopupCancel = lCancel
ClosetDiscardButton = "Remover"
ClosetAreYouSureMessage = "Voc\xc3\xaa excluiu algumas roupas. Deseja mesmo exclu\xc3\xad-las?"
ClosetYes = lYes
ClosetNo = lNo
ClosetVerifyDelete = "Excluir mesmo %s?"
ClosetShirt = "esta camisa"
ClosetShorts = "este short"
ClosetSkirt = "esta saia"
ClosetDeleteShirt = "Excluir\ncamisa"
ClosetDeleteShorts = "Excluir\nshort"
ClosetDeleteSkirt = "Excluir\nsaia"

# EstateLoader.py
EstateOwnerLeftMessage = "Sinto muito, o dono desta propriedade saiu. Voc\xc3\xaa será enviado ao pátio em %s segundos"
EstatePopupOK = lOK
EstateTeleportFailed = "Não foi poss\xc3\xadvel ir para casa. Tente novamente!"
EstateTeleportFailedNotFriends = "Sinto muito, %s fica na propriedade de um toon com o qual voc\xc3\xaa não fez amizade."
EstatePlaneBanner = "Invasão de Cog!!!"
EstateHalloweenBanner = "Feliz Dia das Bruxas!!!"

# DistributedTarget.py
EstateTargetGameStart = "O jogo do Alvo de Toonar começou!"
EstateTargetGameInst = "Quanto mais acertar no alvo vermelho, mais Toonar voc\xc3\xaa vai receber."
EstateTargetGameEnd = "O jogo de Alvo de Toonar acabou..."

# DistributedHouse.py
AvatarsHouse = "Casa de\n %s"

# BankGui.py
BankGuiCancel = lCancel
BankGuiOk = lOK

# DistributedBank.py
DistributedBankNoOwner = "Sinto muito, este não é o seu banco."
DistributedBankNotOwner = "Sinto muito, este não é o seu banco."

# FishSellGui.py
FishGuiCancel = lCancel
FishGuiOk = "Vender tudo"
FishTankValue = "Oi, %(name)s! Voc\xc3\xaa tem %(num)s peixe(s) em seu balde, que vale(m) o total de %(value)s balinhas. Deseja vender todos eles?"

#FlowerSellGui.py
FlowerGuiCancel = lCancel
FlowerGuiOk = "Vender Tudo"
FlowerBasketValue = "%(name)s, voc\xc3\xaa tem %(num)s flores no seu cesto que valem um total de %(value)s balinhas. Voc\xc3\xaa quer vender todas?"


def GetPossesive(name):
    if name[-1:] == 'de':
        possesive = name + "'"
    else:
        possesive = name + ""
    return possesive

# PetTraits
# VERY_BAD, BAD, GOOD, VERY_GOOD
PetTrait2descriptions = {
    'hungerThreshold': ('Sempre faminto', 'Muito faminto',
                        '\xc3\x80s vezes faminto', 'Raramente faminto',),
    'boredomThreshold': ('Sempre chateado', 'Muito chateado',
                         '\xc3\x80s vezes chateado', 'Raramente chateado',),
    'angerThreshold': ('Sempre irritado', 'Muito irritado',
                       '\xc3\x80s vezes irritado', 'Raramente irritado'),
    'forgetfulness': ('Sempre esquecido', 'Muito esquecido',
                      '\xc3\x80s vezes esquecido', 'Raramente esquecido',),
    'excitementThreshold': ('Muito calmo', 'Bem calmo',
                            'Bem animado', 'Muito animado',),
    'sadnessThreshold': ('Sempre triste', 'Muitas vezes triste',
                         '\xc3\x80s vezes triste', 'Raramente triste',),
    'restlessnessThreshold': ('Sempre inquieto', 'Muito inquieto',
                         '\xc3\x80s vezes inquieto', 'Raramente inquieto',),
    'playfulnessThreshold': ('Raramente brincalhão', '\xc3\x80s vezes brincalhão',
                         'Muito brincalhão', 'Sempre brincalhão',),
    'lonelinessThreshold': ('Sempre solitário', 'Muito solitário',
                         '\xc3\x80s vezes solitário', 'Raramente solitário',),
    'fatigueThreshold': ('Sempre cansado', 'Muito cansado',
                         '\xc3\x80s vezes cansado', 'Raramente cansado',),
    'confusionThreshold': ('Sempre confuso', 'Muito confuso',
                         '\xc3\x80s vezes confuso', 'Raramente confuso',),
    'surpriseThreshold': ('Sempre surpreso', 'Muito surpreso',
                         '\xc3\x80s vezes surpreso', 'Raramente surpreso',),
    'affectionThreshold': ('Raramente carinhoso', '\xc3\x80s vezes carinhoso',
                         'Muito carinhoso', 'Sempre carinhoso',),
    }

# end translate

# DistributedFireworkShow.py
FireworksInstructions = lToonHQ+": Pressione a tecla \"Page Up\" para ver melhor."
startFireworksResponse = "Usage: startFireworksShow [\'num\']\n \
                                        \'num\' = %s - New Years\n \
                                        %s - Party Summer \n \
                                        %s - 4th of July"

FireworksValentinesBeginning = ""
FireworksValentinesEnding = ""
FireworksJuly4Beginning = lToonHQ+": Bem-vindo \xc3\xa0 queima de fogos de verão! Divirta-se com o show!"
FireworksJuly4Ending = lToonHQ+": Espero que tenha gostado do show! Um ótimo verão para voc\xc3\xaa!"
FireworksJuly14Beginning = lToonHQ+""
FireworksJuly14Ending = lToonHQ+""
FireworksOctober31Beginning = ""
FireworksOctober31Ending = ""
FireworksNewYearsEveBeginning = lToonHQ+": Feliz Ano Novo!!!!"
FireworksNewYearsEveEnding = lToonHQ+": Gostou dos Fogos? Logo tem mais!"
FireworksBeginning = lToonHQ+": Bem-vindo \xc3\xa0 queima de fogos de verão! Divirta-se com o show!"
FireworksEnding = lToonHQ+": Espero que tenha gostado do show! Um ótimo verão para voc\xc3\xaa!"

# ToontownLoadingBlocker.py
BlockerTitle = "CARREGANDO TOONTOWN..."
BlockerLoadingTexts = [
    "Esfregando latas de torta",
    "Assando crostas de torta",
    "Aquecendo recheio de torta",
    "Carregando Doodle chow",
    "Alinhando cipós da Selva",
    "Soltando as aranhas que rastejam pelas cipós da Selva",
    "Plantando sementes de flores que esguicham",
    "Esticando trampolins",
    "Reunindo porcos",
    "Ajustando sons de 'SPLAT'",
    "Limpando óculos de hipnose",
    "Desengarrafando tinta para as Not\xc3\xadcias Toon",
    "Cortando estopins de TNT",
    "Colocando a placa 'Em construção' no Bosque de Bolotas",
    "Andando como o Pato Donald",
    "Ensinando novos passos a hidrantes dançantes",
    "Amarrando \xc3\x81lbum Toons",
    "Analyzing quacks",
    "Colhendo balinhas",
    "Esvaziando baldes de peixe",
    "Encurralando lixo de lixeira",
    "Espalhando graxa de Cog",
    "Polindo troféus de kart",
    "Balança para pesar uma tonelada",
    "Praticando Danças da Vitória",
    "Preparando maluquices",
    "Mostrando a placa de 'cinco minutos' ao Mickey Mouse",
    "Testando luvas brancas",
    "Tocando sinos submersos",
    "Bobinando fita vermelha",
    "Congelando, brrr, gelo",
    "Afiando pianos que caem",
    ]

# ToontownLoadingScreen.py

TIP_NONE = 0
TIP_GENERAL = 1
TIP_STREET = 2
TIP_MINIGAME = 3
TIP_COGHQ = 4
TIP_ESTATE = 5
TIP_KARTING = 6
TIP_GOLF = 7

# As of 8/5/03, ToonTips shouldn't exceed 130 characters in length
TipTitle = "DICA TOON:"
TipDict = {
    TIP_NONE : (
    "",
    ),

    TIP_GENERAL : (
    "Verifique com rapidez o andamento da Tarefa Toon mantendo pressionada a tecla \"End\".",
    "Verifique com rapidez a sua Página de piadas mantendo pressionada a tecla \"Home\".",
    "Abra a sua Lista de amigos pressionando a tecla \"F7\".",
    "Abra ou feche o seu \xc3\x81lbum Toon pressionando a tecla \"F8\".",
    "Voc\xc3\xaa pode procurar acima pressionando a tecla \"Page Up\" e abaixo pressionando a tecla \"Page Down\".",
    "Pressione a tecla \"Control\" para pular.",
    "Pressione a tecla \"F9\" para capturar a tela, que será salva na pasta Toontown do seu computador.",
    # This one makes me nervous without mentioning Parent Passwords - but that would be too long
    # "Voc\xc3\xaa pode trocar Códigos de Amigo secreto com alguém conhecido que não seja de Toontown, para permitir um chat aberto com essa pessoa em Toontown.",
    "Voc\xc3\xaa pode alterar a resolução de seu v\xc3\xaddeo, ajustar o áudio e controlar outras opções na Página de opções do \xc3\x81lbum Toon.",
    "Experimente as roupas de seus amigos no armário da casa deles.",
    "Voc\xc3\xaa pode ir para casa usando o botão \"Ir para casa\" em seu mapa.",
    "Toda vez que voc\xc3\xaa conclui uma Tarefa Toon, seus Pontos de risadas são automaticamente recarregados.",
    "Voc\xc3\xaa pode procurar a seleção nas lojas de roupas mesmo sem ter um bilhete de roupas.",
    "As recompensas para algumas Tarefas Toon permitem que voc\xc3\xaa carregue mais piadas e balinhas.",
    "Voc\xc3\xaa pode ter até 50 amigos na sua Lista de amigos.",
    "Algumas recompensas das Tarefas Toon permitem que voc\xc3\xaa se teletransporte para os pátios de Toontown usando a Página do mapa do \xc3\x81lbum Toon.",
    "Aumente os seus Pontos de risadas nos pátios, catando tesouros como estrelas e casquinhas de sorvete.",
    "Se voc\xc3\xaa precisar se recuperar rápido após uma batalha dif\xc3\xadcil, vá para a sua propriedade e recolha casquinhas de sorvete.",
    "Alterne entre os diversos modos de exibição de seu Toon pressionando a tecla Tab.",
    "Algumas vezes, voc\xc3\xaa poderá encontrar várias Tarefas Toon diferentes com a mesma recompensa. Faça sua pesquisa de mercado!",
    "Encontrar amigos com Tarefas Toon semelhantes é uma maneira divertida de progredir no jogo.",
    "Voc\xc3\xaa nunca precisa salvar o seu progresso em Toontown. Os servidores de Toontown salvam continuamente todas as informações necessárias.",
    "Voc\xc3\xaa pode cochichar com outros Toons clicando neles ou selecionando-os em sua Lista de amigos.",
    "Algumas frases do Chat rápido t\xc3\xaam animações para indicar o estado de esp\xc3\xadrito do seu Toon.",
    "Se a área em que voc\xc3\xaa está se encontra lotada, tente mudar de região. Vá para a Página de região do \xc3\x81lbum Toon e selecione uma diferente.",
    "Se voc\xc3\xaa estiver em plena atividade de salvamento de edif\xc3\xadcios, ganhará uma estrela de bronze, prata ou ouro, que ficará acima de seu Toon.",
    "Se voc\xc3\xaa salvar um número suficiente de edif\xc3\xadcios para obter uma estrela acima da cabeça, seu nome pode estar no quadro-negro de um Quartel Toon.",
    "Os edif\xc3\xadcios salvos, \xc3\xa0s vezes, são recuperados pelos Cogs. A única maneira de manter a sua estrela é sair em campo e salvar mais edif\xc3\xadcios!",
    "Os nomes dos seus Amigos secretos aparecerão na cor azul.",
    # Fishing
    "Veja se voc\xc3\xaa consegue pegar todos os peixes de Toontown!",
    "Há peixes diferentes nos diversos lagos. Tente todos!",
    "Quando o seu balde de pesca estiver cheio, venda os peixes para os pescadores dos pátios.",
    "Venda os peixes para o pescador ou dentro das Lojas de Animais.",
    "As varas de pescar mais fortes conseguem pegar peixes mais pesados, mas custam mais balinhas.",
    "Voc\xc3\xaa pode comprar varas de pescar mais fortes no Gadálogo.",
    "Os peixes mais pesados valem mais balinhas na Loja de animais.",
    "Os peixes raros valem mais balinhas na Loja de animais.",
    "\xc3\x80s vezes, voc\xc3\xaa consegue encontrar bolsas de balinhas durante a pesca.",
    "Algumas Tarefas Toon exigem que voc\xc3\xaa pesque itens fora dos lagos.",
    "Os lagos de pesca dos pátios possuem peixes diferentes dos lagos das ruas.",
    "Alguns peixes são realmente raros. Continue pescando até pegar todos!",
    "O lago da sua propriedade possui peixes que só podem ser encontrados lá.",
    "Para cada dez espécies pescadas, voc\xc3\xaa ganhará um troféu de pesca!",
    "Voc\xc3\xaa pode ver qual peixe pescou no \xc3\x81lbum Toon.",
    "Alguns troféus de pesca o recompensam com um Acréscimo de risadas.",
    "A pesca é uma boa maneira de ganhar mais balinhas.",
    # Doodles
    "Adote um Rabisco na Loja de Animais!",
    "As lojas de animais t\xc3\xaam Rabiscos novos para vender todos os dias.",
    "Visite as lojas de animais todos os dias para ver que Rabiscos novos elas t\xc3\xaam.",
    "Há diferentes Rabiscos para adoção nos diferentes bairros.",
    # Karting
    "Mostre o seu carrão e d\xc3\xaa uma turbinada no seu limite de Risadas no Autódromo do Pateta. ",
    "Entre no Autódromo do Pateta pelo túnel em forma de pneu no pátio do Centro de Toontown.",
    "Ganhe pontos de Risada no Autódromo do Pateta.",
    "O Autódromo do Pateta tem seis pistas de corrida diferentes. "
   ),

  TIP_STREET : (
    "Há quatro tipos de Cogs: Robôs da Lei, Robôs Mercenários, Robôs Vendedores e Robôs-chefe.",
    "Cada Método de piadas possui diferentes intensidades de precisão e dano.",
    "As piadas sonoras afetam todos os Cogs, mas acordam qualquer Cog iscado.",
    "Derrotar os Cogs em ordem estratégica pode aumentar bastante as suas chances de vencer as batalhas.",
    "O Método de piadas Toonar permite que voc\xc3\xaa atinja outros Toons na batalha.",
    "Os pontos de experi\xc3\xaancia das piadas são dobrados durante uma Invasão de Cogs!",
    "Vários Toons podem se reunir em equipes e usar o mesmo Método de piadas na batalha para conseguir danos extras aos Cogs.",
    "Na batalha, as piadas são usadas na ordem de cima para baixo, conforme exibido no Menu de piadas.",
    "A fileira de luzes circulares sobre os elevadores do Edif\xc3\xadcio dos Cogs mostram quantos andares haverá lá dentro.",
    "Clique em um Cog para ver mais detalhes.",
    "Usar piadas de alto n\xc3\xadvel contra Cogs de baixo n\xc3\xadvel não lhe renderá nenhum ponto de experi\xc3\xaancia.",
    "As piadas que rendem experi\xc3\xaancia possuem um fundo azul no Menu de piadas da batalha.",
    "A experi\xc3\xaancia de piadas é multiplicada quando usada dentro dos Edif\xc3\xadcios dos Cogs. Os andares mais altos t\xc3\xaam multiplicadores maiores.",
    "Quando um Cog é derrotado, cada Toon daquela rodada recebe créditos de Cogs depois que a batalha termina.",
    "Cada rua de Toontown possui n\xc3\xadveis e tipos diferentes de Cogs.",
    "As calçadas são locais seguros, sem Cogs.",
    "Nas ruas, as portas laterais contam piadas do tipo toc-toc quando voc\xc3\xaa se aproxima delas.",
    "Algumas Tarefas Toon treinam voc\xc3\xaa em novos Métodos de piadas. Voc\xc3\xaa só pode escolher seis dos sete métodos, portanto, escolha direito!",
    "As armadilhas só terão utilidade se voc\xc3\xaa ou seus amigos coordenarem o uso de iscas na batalha.",
    "As iscas de alto n\xc3\xadvel t\xc3\xaam menos probabilidade de falhar.",
    "As piadas de n\xc3\xadvel baixo oferecem menor precisão contra os Cogs de alto n\xc3\xadvel.",
    "Os Cogs não podem atacar depois que forem \"iscados\" para a batalha.",
    "Quando voc\xc3\xaa e seus amigos dominam um Edif\xc3\xadcio de Cogs, voc\xc3\xaas são recompensados com retratos dentro do Edif\xc3\xadcio dos Toons recuperado.",
    "Usar uma piada Toonar em um Toon que possua um Risômetro cheio não renderá nenhuma experi\xc3\xaancia de Toonar.",
    "Os Cogs ficarão atordoados por uns momentos quando atingidos por alguma. Assim, aumentam as chances de outras piadas da mesma rodada os atingirem.",
    "As Piadas cadentes t\xc3\xaam menos chance de atingir alguém, mas sua precisão aumenta quando os Cogs já tiverem sido atingidos por outra piada na mesma rodada.",
    "Quando voc\xc3\xaa já tiver derrotado um número suficiente de Cogs, use o \"Radar de Cogs\" clicando nos \xc3\xadcones de Cogs da página Galeria de Cogs do seu \xc3\x81lbum Toon.",
    "Durante uma batalha, voc\xc3\xaa tem como saber qual Cog os seus companheiros de equipe estão atacando; basta olhar para os travessões (-) e para os X.",
    "Durante uma batalha, os Cogs carregam uma luz que mostra sua saúde: o verde significa saudável e o vermelho, quase destru\xc3\xaddo.",
    "No máximo, quatro Toons podem guerrear ao mesmo tempo.",
    "Na rua, os Cogs t\xc3\xaam mais probabilidade de entrar em uma briga contra vários Toons do que contra apenas um Toon.",
    "Os dois tipos de Cogs mais dif\xc3\xadceis de cada tipo só são encontrados nos edif\xc3\xadcios.",
    "As Piadas cadentes nunca funcionam contra Cogs iscados.",
    "Os Cogs tendem a atacar o Toon que lhes causou danos maiores.",
    "As piadas sonoras não rendem danos extras contra Cogs iscados.",
    "Se voc\xc3\xaa esperar muito para atacar um Cog iscado, ele acordará. As iscas de n\xc3\xadvel mais alto t\xc3\xaam duração maior.",
    "Há lagos de pesca em cada rua de Toontown. Algumas ruas possuem peixes exclusivos.",
    ),

  TIP_MINIGAME : (
    "Depois que voc\xc3\xaa preenche a sua jarra de balinhas, qualquer balinha que ganhar nos Jogos no bondinho cairão direto no seu banco.",
    "Voc\xc3\xaa pode usar as teclas de seta em vez de o mouse no Jogo no bondinho \"Acompanhe a Minnie\".",
    "No Jogo do canhão, voc\xc3\xaa pode usar as teclas de seta para mover o seu canhão e pressionar a tecla \"Control\" para atirar.",
    "No Jogo dos anéis, voc\xc3\xaa ganha pontos extras quando todo o grupo consegue nadar com sucesso através dos anéis.",
    "Um jogo perfeito de Acompanhe a Minnie dobrará seus pontos.",
    "No Cabo de guerra, voc\xc3\xaa ganha mais balinhas se jogar contra um Cog forte.",
    "A dificuldade dos Jogos no bondinho varia conforme o bairro; os do Centro de Toontown são os mais fáceis, e os da Sonholândia do Donald são os mais dif\xc3\xadceis.",
    "Certos Jogos no bondinho só podem ser em grupo.",
    ),

  TIP_COGHQ : (
    "Voc\xc3\xaa deve completar o seu Disfarce de Robô Vendedor antes de visitar o VP.",
    "Voc\xc3\xaa deve completar o seu Disfarce de Robô Mercenário antes de visitar o Diretor Financeiro.",
    "Voc\xc3\xaa deve completar o seu Disfarce de Robô da Lei antes de visitar o Juiz-chefe.",
    "Voc\xc3\xaa deve completar o seu Disfarce de Robô-chefe antes de visitar o Presidente.",
    "Voc\xc3\xaa pode pular em cima de cogs Brutamontes para desativá-los por um tempo.",
    "Ganhe Méritos de cogs ao derrotar Robôs Vendedores em batalha.",
    "Ganhe Cograna ao derrotar Robôs Mercenários em batalha.",
    "Ganhe Avisos de Júri ao derrotar Robôs da Lei em batalha.",
    "Voc\xc3\xaa ganha mais Méritos, Cogranas ou Avisos de Júri de Cogs de n\xc3\xadvel maior.",
    "Quando conseguir juntar Méritos o suficiente para merecer uma promoção, vá ver o VP dos Robôs Vendedores!",
    "Quando conseguir juntar Cogranas o suficiente para merecer uma promoção, vá ver o Diretor Financeiro dos Robôs Mercenários!",
    "Quando conseguir juntar Avisos de Júri o suficiente para merecer uma promoção, vá ver o Juiz-chefe dos Robôs da Lei!",
    "Voc\xc3\xaa pode falar como um Cog quando estiver usando o seu Disfarce de Cog.",
    "Até oito Toons podem lutar juntos contra o VP dos Robôs Vendedores.",
    "Até oito Toons podem lutar juntos contra o Diretor Financeiro dos Robôs Mercenários.",
    "Até oito Toons podem lutar juntos contra o Juiz-chefe dos Robôs da Lei.",
    "Até oito Toons podem lutar juntos contra o Presidente dos Robôs-chefe.",
    "Dentro do Quartel dos Cogs, o caminho é subindo as escadas.",
    "Cada vez que lutar numa fábrica do Quartel dos Robôs Vendedores, voc\xc3\xaa vai ganhar uma peça do seu Disfarce de Robô Vendedor.",
    "Voc\xc3\xaa pode verificar o progresso do seu Disfarce no seu \xc3\x81lbum Toon.",
    "Voc\xc3\xaa pode verificar o progresso da sua promoção na Página de Disfarce do seu \xc3\x81lbum Toon.",
    "Certifique-se de estar com as piadas cheias e com o Risômetro cheio antes de ir até um Quartel dos Cogs.",
    "Quando for promovido, seu disfarce de Cog será atualizado.",
    "Voc\xc3\xaa terá que derrotar o "+Foreman+" para recuperar uma peça do Disfarce de Robô Vendedor.",
    "Ganhe peças de disfarce de Robô Mercenário como recompensa de Tarefas Toon na Sonholândia do Donald.",
    "Os Robôs Mercenários produzem e distribuem o seu próprio dinheiro, as Cogranas, de tr\xc3\xaas maneiras - Moeda, Dólar e Barra.",
    "Espere até que o Diretor Financeiro esteja tonto para lançar um cofre, senão ele vai usá-lo como capacete! Acerte o capacete com outro cofre para derrubá-lo.",
    "Ganhe peças de disfarce de Robô da Lei como recompensa de Tarefas Toon pelo Professor Floco.",
    "Vale a pena a confusão: os Cogs virtuais no Quartel dos Robôs da Lei não dão Avisos de Júri de recompensa.",
    "Robô Mercenário produz e distribui a sua própia moeda, Cogbucks, em tr\xc3\xaas formas diferentes: Moedas, Dólar, e lingotes.",
    "Aguarde até que o Diretor Financeiro fique doido para lançar um seguro ou o utilize-o como um capacete! Acerte no capacete com outro seguro para pegá-lo.",
    "O Robô da Lei obtém as partes do traje como recompensa ao concluir a TarefaToon para o Professor Floco.",
    ),
  TIP_ESTATE : (
    # Doodles
    "Os Rabiscos entendem algumas frases do Chat rápido. Experimente!",
    "Use o menu \"Bichinho\" do Chat rápido para pedir a seu Rabisco que faça truques.",
    "Voc\xc3\xaa pode ensinar aos Rabiscos truques com as lições de treinamento do Gadálogo da Clarabela.",
    "Recompense o seu Rabisco pelos truques.",
    "Se voc\xc3\xaa visitar a propriedade de um amigo, o seu Rabisco lhe fará companhia.",
    "Alimente o seu Rabisco com uma balinha quando ele estiver com fome.",
    "Clique em um Rabisco para ver um menu no qual voc\xc3\xaa poderá Alimentar, Coçar e Chamá-lo.",
    "Os Rabiscos adoram companhia. Convide os amigos para brincar!",
    "Todos os Rabiscos possuem personalidades próprias.",
    "Voc\xc3\xaa pode devolver o seu Rabisco e adotar outro nas Lojas de Animais.",
    "Quando um Rabisco faz um truque, os Toons que o cercam se recuperam.",
    "Os Rabiscos ficam ainda melhores nos truques com a prática. Continue assim!",
    "Os truques mais avançados dos Rabiscos recuperam os Toons com mais rapidez.",
    "Rabiscos com mais experi\xc3\xaancia podem fazer mais truques sem ficar tão cansados.",
    "Veja uma lista de Rabiscos próximos em sua Lista de amigos.",
    # Furniture / Cattlelog
    "Compre móveis usando o Gadálogo da Clarabela e decore a sua casa.",
    "O banco da casa tem mais balinhas.",
    "O armário da casa tem mais roupas.",
    "Vá até a casa do seu amigo e experimente as roupas dele.",
    "Compre varas de pescar melhores no Gadálogo da Clarabela.",
    "Compre bancos maiores no Gadálogo da Clarabela.",
    "Ligue para a Clarabela usando o telefone da casa.",
    "A Clarabela vende um armário maior em que cabem mais roupas.",
    "Reserve espaço no seu armário antes de usar o bilhete de roupas.",
    "A Clarabela vende tudo o que é preciso para decorar a sua casa.",
    "Verifique a sua caixa de correio para ver se há entregas antes de fazer seus pedidos com a Clarabela.",
    "As roupas do Gadálogo da Clarabela levam uma hora para serem entregues.",
    "Os papéis de parede e pisos do Gadálogo da Clarabela levam uma hora para serem entregues.",
    "Os móveis do Gadálogo da Clarabela levam um dia inteiro para serem entregues.",
    "Armazene móveis de reserva no sótão.",
    "Voc\xc3\xaa será avisado pela Clarabela quando um novo Gadálogo estiver dispon\xc3\xadvel.",
    "Voc\xc3\xaa será avisado pela Clarabela quando uma entrega do Gadálogo chegar.",
    "Novos Gadálogos são entregues toda semana.",
    "Procure os produtos promocionais de estoque limitado no Gadálogo.",
    "Mova os móveis indesejados para a lata de lixo.",
    # Fish
    "Alguns peixes, como a Cavala Trotante, são mais comuns nas propriedades de Toons.",
    # Misc
    "Voc\xc3\xaa pode convidar os seus amigos para a sua propriedade usando o Chat rápido.",
    "Voc\xc3\xaa sabia que a cor da sua casa combina com a cor do seu painel Pegar um Toon?",
    ),
   TIP_KARTING : (
    # Goofy Speedway zone specific
    "Compre um Convers\xc3\xadvel, Utilitário Toon ou Cruzeiro na Loja do Kart do Pateta.",
    "Personalize o seu kart com decalques, calotas e muito mais na Loja do Kart do Pateta.",
    "Ganhe bilhetes correndo de kart no Autódromo do Pateta.",
    "Os bilhetes são a única moeda aceita na Loja do Kart do Pateta.",
    "São necessários bilhetes como depósito antes das corridas.",
    "Uma página especial do seu \xc3\x81lbum Toon permite que voc\xc3\xaa personalize o seu kart.",
    "Uma página especial do seu \xc3\x81lbum Toon permite que voc\xc3\xaa veja os recordes de cada pista.",
    "Uma página especial do seu \xc3\x81lbum Toon permite que voc\xc3\xaa veja seus troféus.",
    "O Estádio dos Nerds é a pista mais fácil do Autódromo do Pateta.",
    "A Pista de Pulos tem o maior número de inclinações e rampas do Autódromo do Pateta.",
    "A Avenida da Neve é a pista mais dif\xc3\xadcil do Autódromo do Pateta.",
    ),
   TIP_GOLF: (
    # Golfing specific
    "Aperte a tecla Tab para ver de cima o percurso de golfe.",
    "Aperte a tecla de Seta para Cima para se colocar na direção do buraco de golfe.",
    "Balançar o taco é como atirar uma torta.",
    ),
    }

FishGenusNames = {
    0 : "Baiacu",
    2 : "Peixe-gato",
    4 : "Peixe-palhaço",
    6 : "Peixe congelado",
    8 : "Estrela-do-mar",
    10 : "Cavala Trotante!",
    12 : "Cachorra",
    14 : "Enguia Amore",
    16 : "Tubarão-enfermeira",
    18 : "Caranguejo-rei",
    20 : "Peixe-lua",
    22 : "Cavalo-marinho",
    24 : "Tubarão Fera",
    26 : "Barra Cursa",
    28 : "Truta Cicuta",
    30 : "Piano Atum",
    32 : "Manteiga de Amendoim e \xc3\x81gua-viva",
    34 : "Raia Jamanta",
    }

FishSpeciesNames = {
    0 : ( "Baiacu",
          "Baiacu Balão de Ar",
          "Baiacu Balão Meteorológico",
          "Baiacu Balão de \xc3\x81gua",
          "Baiacu Balão Vermelho",
          ),
    2 : ( "Peixe-gato",
          "Peixe-gato Siam\xc3\xaas",
          "Peixe-gato de Rua",
          "Peixe-gato Rajado",
          "Peixe-gato Tonto",
          ),
    4 : ( "Peixe-palhaço",
          "Peixe-palhaço Triste",
          "Peixe-palhaço de Festa",
          "Peixe-palhaço de Circo",
          ),
    6 : ( "Peixe congelado",
          ),
    8 : ( "Estrela-do-mar",
          "Cinco Estrelas-do-mar",
          "Estrela-do-mar do Rock",
          "Estrela-do-mar Cintilante",
          "Estrela-do-mar All Star",
          ),
    10 : ( "Cavala Trotante!",
           ),
    12 : ( "Cachorra",
           "Cachorra Buldogue",
           "Cachorra-quente",
           "Cachorra Dálmata",
           "Cachorrinha",
           ),
    14 : ( "Enguia Amore",
           "Enguia Amore Elétrica",
           ),
    16 : ( "Tubarão-enfermeira",
           "Tubarão-enfermeira Clara",
           "Tubarão-enfermeira Flora",
           ),
    18 : ( "Caranguejo-rei",
           "Caranguejo-rei do Alasca",
           "Caranguejo-rei Velho",
           ),
    20 : ( "Peixe-lua",
           "Peixe-lua Cheia",
           "Peixe Meia-lua",
           "Peixe-lua Nova",
           "Peixe-lua Crescente",
           "Peixe-lua da Colheita",
           ),
    22 : ( "Cavalo-marinho",
           "Cavalo-marinho de Pau",
           "Cavalo-marinho Clydesdale",
           "Cavalo-marinho \xc3\x81rabe",
           ),
    24 : ( "Tubarão-Fera",
           "Tubarãozinho Fera",
           "Tubarão-Fera da Piscina",
           "Tubarão-Fera da Piscina Ol\xc3\xadmpica",
           ),
    26 : ( "Barra Cursa Marrom",
           "Barra Cursa Preto",
           "Barra Cursa Coala",
           "Barra Cursa de Mel",
           "Barra Cursa Polar",
           "Barra Cursa Panda",
           "Barra Cursa Kodiac",
           "Barra Cursa Grizzly",
           ),
    28 : ( "Truta",
           "Capitão Truta Cicuta",
           "Truta Cicuta Escorbuta",
           ),
    30 : ( "Piano Atum",
           "Grande Piano Atum",
           "Grande Piano Atum Baby",
           "Piano Atum Ereto",
           "Músico de Piano Atum",
           ),
    32 : ( "Manteiga de Amendoim e \xc3\x81gua-viva",
           "MA & \xc3\x81gua-viva de Uva",
           "MA & \xc3\x81gua-viva Crocante",
           "MA & \xc3\x81gua-viva de Morango",
           "Concord Grape PB&J Fish",
           ),
    34 : ( "Raia Jamanta",
           ),
    }

CogPartNames = (
    "Perna superior esquerda", "Perna inferior esquerda", "Pé esquerdo",
    "Perna superior direita", "Perna inferior direita", "Pé direito",
    "Ombro esquerdo",  "Ombro direito", "Peito", "Medidor de saúde", "Quadril",
    "Braço superior esquerdo",  "Braço inferior esquerdo", "Mão esquerda",
    "Braço superior direito", "Braço inferior direito", "Mão direita",
    )

CogPartNamesSimple = (
    "Busto superior",
    )

FishFirstNames = (
    "",
    "Anjo",
    "\xc3\x81rtico",
    "Beb\xc3\xaa",
    "Bermuda",
    "Grande",
    "Bruna",
    "Bolhas",
    "Detuna",
    "Docinho",
    "Capitão",
    "Tico",
    "Cacho",
    "Coral",
    "Doutor",
    "Arenoso",
    "Imperador",
    "Canino",
    "Gordo",
    "Peixinho",
    "Flipper",
    "Linguado",
    "Sardinha",
    "Mel",
    "João",
    "Rei",
    "Pequeno",
    "Marlin",
    "Senhorita",
    "Senhor",
    "P\xc3\xaassego",
    "Rosado",
    "Pr\xc3\xadncipe",
    "Princesa",
    "Professor",
    "Inchadinho",
    "Rainha",
    "Arco-\xc3\xadris",
    "Raio",
    "Rosinha",
    "Ferrugem",
    "Salgado",
    "Samuca",
    "Sandy",
    "Caspa",
    "Tutubarão",
    "Cavalheiro",
    "Saltador",
    "Chinela",
    "Guaiúba",
    "Malhado",
    "Espinho",
    "Pintado",
    "Estrela",
    "Doce",
    "Súper",
    "Tigre",
    "Miúdo",
    "Bigode",
    )

FishLastPrefixNames = (
    "",
    "Praia",
    "Preto",
    "Azul",
    "Porcão",
    "Machão",
    "Gato",
    "Fundo",
    "Duplo",
    "Leste",
    "Chique",
    "Escamoso",
    "Chato",
    "Fresco",
    "Gigante",
    "Ouro",
    "Dourado",
    "Cinza",
    "Verde",
    "Presunto",
    "Mané",
    "Geléia",
    "Dama",
    "Couro",
    "Limão",
    "Comprido",
    "Nordeste",
    "Oceano",
    "Octo",
    "\xc3\x93leo",
    "Pérola",
    "Cachimbo",
    "Vermelho",
    "Faixa",
    "Rio",
    "Pedra",
    "Rubi",
    "Leme",
    "Sal",
    "Mar",
    "Prata",
    "Snorkel",
    "Só",
    "Sudeste",
    "Espinhoso",
    "Surfe",
    "Espada",
    "Tigre",
    "Triplo",
    "Tropical",
    "Atum",
    "Onda",
    "Fraco",
    "Oeste",
    "Branco",
    "Amarelo",
    )

FishLastSuffixNames = (
    "",
    "bola",
    "baixo",
    "barriga",
    "besouro",
    "gatuno",
    "manteiga",
    "garra",
    "sapateiro",
    "caranguejo",
    "rosnador",
    "tambor",
    "barbatana",
    "peixe",
    "batedor",
    "flipper",
    "fantasma",
    "roncador",
    "cabeça",
    "coroa",
    "saltador",
    "cavala",
    "lua",
    "boca",
    "tainha",
    "pescoço",
    "nariz",
    "galho",
    "bruto",
    "corredor",
    "vela",
    "tubarão",
    "concha",
    "seda",
    "limo",
    "mordedora",
    "fedido",
    "rabo",
    "sapo",
    "truta",
    "água",
    )

# SellbotLegFactorySpec.py

SellbotLegFactorySpecMainEntrance = "Entrada principal"
SellbotLegFactorySpecLobby = "Salão"
SellbotLegFactorySpecLobbyHallway = "Corredor do salão"
SellbotLegFactorySpecGearRoom = "Sala de engrenagens"
SellbotLegFactorySpecBoilerRoom = "Sala da caldeira"
SellbotLegFactorySpecEastCatwalk = "Passarela leste"
SellbotLegFactorySpecPaintMixer = "Misturador de tinta"
SellbotLegFactorySpecPaintMixerStorageRoom = "Depósito do Misturador de tinta"
SellbotLegFactorySpecWestSiloCatwalk = "Passarela do Silo Oeste"
SellbotLegFactorySpecPipeRoom = "Sala de tubulações"
SellbotLegFactorySpecDuctRoom = "Sala de dutos"
SellbotLegFactorySpecSideEntrance = "Entrada lateral"
SellbotLegFactorySpecStomperAlley = "Beco sinistro"
SellbotLegFactorySpecLavaRoomFoyer = "Antecâmara do Salão de lava"
SellbotLegFactorySpecLavaRoom = "Salão de lava"
SellbotLegFactorySpecLavaStorageRoom = "Depósito de lava"
SellbotLegFactorySpecWestCatwalk = "Passarela oeste"
SellbotLegFactorySpecOilRoom = "Sala de óleo"
SellbotLegFactorySpecLookout = "Vigilância"
SellbotLegFactorySpecWarehouse = "Armazém"
SellbotLegFactorySpecOilRoomHallway = "Corredor da Sala de óleo"
SellbotLegFactorySpecEastSiloControlRoom = "Sala de controle do Silo Leste"
SellbotLegFactorySpecWestSiloControlRoom = "Sala de controle do Silo Oeste"
SellbotLegFactorySpecCenterSiloControlRoom = "Sala de controle do Silo Central"
SellbotLegFactorySpecEastSilo = "Silo Leste"
SellbotLegFactorySpecWestSilo = "Silo Oeste"
SellbotLegFactorySpecCenterSilo = "Silo Central"
SellbotLegFactorySpecEastSiloCatwalk = "Passarela do Silo Leste"
SellbotLegFactorySpecWestElevatorShaft = "Eixo do Elevador Oeste"
SellbotLegFactorySpecEastElevatorShaft = "Eixo do Elevador Leste"

#FISH BINGO
FishBingoBingo = "BINGO!"
FishBingoVictory = "VIT\xc3\x93RIA!!"
FishBingoJackpot = "GRANDE PR\xc3\x8aMIO!"
FishBingoGameOver = "FIM DO JOGO"
FishBingoIntermission = "Intervalo\nTermina em:"
FishBingoNextGame = "Próximo jogo\nComeça em:"
FishBingoTypeNormal = "Clássico"
FishBingoTypeCorners = "Quatro cantos"
FishBingoTypeDiagonal = "Diagonais"
FishBingoTypeThreeway = "Tr\xc3\xaas vias"
FishBingoTypeBlockout = "BLOQUEADO!"
FishBingoStart = "Está na hora do Bingo dos Peixes! Vá para qualquer p\xc3\xader dispon\xc3\xadvel para jogar!"
FishBingoOngoing = "Bem-vindo! O Bingo dos Peixes já está rolando."
FishBingoEnd = "Espero que tenha se divertido no jogo Bingo dos Peixes."
FishBingoHelpMain = "Bem-vindo ao Bingo dos Peixes de Toontown! Todo mundo trabalha em conjunto no lago para preencher a cartela antes de acabar o tempo."
FishBingoHelpFlash = "Quando voc\xc3\xaa pegar um peixe, clique em um dos quadrados piscantes para marcar a cartela."
FishBingoHelpNormal = "\xc3\x89 uma cartela de Bingo Clássico. Para ganhar, complete qualquer linha vertical, horizontal ou na diagonal."
FishBingoHelpDiagonals = "Complete as duas diagonais para ganhar."
FishBingoHelpCorners = "Uma cartela de Cantos fácil. Complete todos os quatro cantos para ganhar."
FishBingoHelpThreeway = "Tr\xc3\xaas vias. Complete ambas as diagonais e a linha do meio para ganhar. Esta não é fácil não!"
FishBingoHelpBlockout = "Bloqueado! Complete a cartela inteira para ganhar. Voc\xc3\xaa está competindo contra todos os outros lagos e a bolada é grande!"
FishBingoOfferToSellFish = "O seu balde de pesca está cheio. Quer vender os seus peixes?"
FishBingoJackpotWin = "Ganhe %s balinhas!"
FishBingoJackpot = "Ganhe %s balinhas!"

# ResistanceSCStrings: SpeedChat phrases rewarded for defeating the CFO.
# It is safe to remove entries from this list, which will disable them
# for use from any toons who have already purchased them.  Note that the
# index numbers are stored directly in the database, so once assigned
# to a particular phrase, a given index number should never be
# repurposed to any other phrase.
ResistanceToonupMenu = "Toonar"
ResistanceToonupItem = "%s toonar"
ResistanceToonupItemMax = "Máx."
ResistanceToonupChat = "Toons de todo o mundo: vamos toonar!"
ResistanceRestockMenu = "Doar Piadas"
ResistanceRestockItem = "Doar Piadas %s"
ResistanceRestockItemAll = "Tudo"
ResistanceRestockChat = "Toons de todo o mundo: vamos piadar!"
ResistanceMoneyMenu = "Balinhas"
ResistanceMoneyItem = "%s balinhas"
ResistanceMoneyChat = "Toons de todo o mundo: gastem com consci\xc3\xaancia!"

# Resistance Emote NPC chat phrases
ResistanceEmote1 = NPCToonNames[9228] + ": Bem-vindo \xc3\xa0 Resist\xc3\xaancia!"
ResistanceEmote2 = NPCToonNames[9228] + ": Use a sua nova expressão para se identificar com outros membros."
ResistanceEmote3 = NPCToonNames[9228] + ": Boa sorte!"

# Kart racing
KartUIExit = "Deixar o kart"
KartShop_Cancel = lCancel
KartShop_BuyKart = "Comprar kart"
KartShop_BuyAccessories = "Comprar acessórios"
KartShop_BuyAccessory = "Comprar acessório"
KartShop_Cost = "Custo: %d bilhetes"
KartShop_ConfirmBuy = "Comprar %s por %d bilhetes?"
KartShop_NoAvailableAcc = "Não há acessórios deste tipo"
KartShop_FullTrunk = "A mala está cheia."
KartShop_ConfirmReturnKart = "Tem certeza de que quer devolver o seu kart atual?"
KartShop_ConfirmBoughtTitle = "Parabéns!"
KartShop_NotEnoughTickets = "Não há bilhetes suficientes!"

KartView_Rotate = "Girar"
KartView_Right = "Direita"
KartView_Left = "Esquerda"

# starting block
StartingBlock_NotEnoughTickets = "Voc\xc3\xaa não tem bilhetes suficientes! Experimente participar de um treino."
StartingBlock_NoBoard = "O embarque para esta corrida terminou. Espere o in\xc3\xadcio da próxima corrida."
StartingBlock_NoKart = "Primeiramente, voc\xc3\xaa precisa de um kart! Por que voc\xc3\xaa não pergunta a um dos funcionários da Loja do kart?"
StartingBlock_Occupied = "Este bloco já está ocupado! Procure outro ponto."
StartingBlock_TrackClosed = "Desculpe, esta pista está fechada para reformas."
StartingBlock_EnterPractice = "Deseja participar do treino?"
StartingBlock_EnterNonPractice = "Deseja participar de uma corrida %s por %s bilhetes?"
StartingBlock_EnterShowPad = "Deseja estacionar o seu carro aqui?"
StartingBlock_KickSoloRacer = "As corridas Batalha dos Toons e Grande Pr\xc3\xaamio requerem dois ou mais participantes."
StartingBlock_Loading = "Indo para a corrida!"

#stuff for leader boards
LeaderBoard_Time = "Tempo"
LeaderBoard_Name = "Nome do piloto"
LeaderBoard_Daily = "Pontuação diária"
LeaderBoard_Weekly = "Pontuação semanal"
LeaderBoard_AllTime = "Melhor pontuação de todos os tempos"

RecordPeriodStrings = [
    LeaderBoard_Daily,
    LeaderBoard_Weekly,
    LeaderBoard_AllTime,
    ]

KartRace_RaceNames = [
    "Treino",
    "Batalha dos Toons",
    "Torneio",
    ]

from toontown.racing import RaceGlobals

KartRace_Go = "Largar!"
KartRace_Reverse = " Rev"

#needed for leader boards
KartRace_TrackNames = {
  RaceGlobals.RT_Speedway_1     : "Estádio dos Nerds",
  RaceGlobals.RT_Speedway_1_rev : "Estádio dos Nerds" + KartRace_Reverse,
  RaceGlobals.RT_Rural_1        : "Autódromo Rústico",
  RaceGlobals.RT_Rural_1_rev    : "Autódromo Rústico" + KartRace_Reverse,
  RaceGlobals.RT_Urban_1        : "Circuito da Cidade",
  RaceGlobals.RT_Urban_1_rev    : "Circuito da Cidade" + KartRace_Reverse,
  RaceGlobals.RT_Speedway_2     : "Coliseu Saca-Rolhas",
  RaceGlobals.RT_Speedway_2_rev : "Coliseu Saca-Rolhas" + KartRace_Reverse,
  RaceGlobals.RT_Rural_2        : "Pista de Pulos",
  RaceGlobals.RT_Rural_2_rev    : "Pista de Pulos" + KartRace_Reverse,
  RaceGlobals.RT_Urban_2        : "Avenida da Neve",
  RaceGlobals.RT_Urban_2_rev    : "Avenida da Neve" + KartRace_Reverse,
 }

KartRace_Unraced = "N/D"

KartDNA_KartNames = {
    0:"Cruzeiro",
    1:"Convers\xc3\xadvel",
    2:"Utilitário Toon"
    }

KartDNA_AccNames = {
    #engine block accessory names
    1000: "Filtro de ar",
    1001: "Carburador quádruplo",
    1002: "\xc3\x81guia",
    1003: "Chifres",
    1004: "Seis cilindros",
    1005: "Aerofólio pequeno",
    1006: "Válvulas simples",
    1007: "Aerofólio médio",
    1008: "Carburador simples",
    1009: "Corneta",
    1010: "Aerofólio simétrico",
    #spoiler accessory names
    2000: "Asa",
    2001: "Peça recondicionada",
    2002: "Gaiola",
    2003: "Aleta",
    2004: "Asa dupla",
    2005: "Asa simples",
    2006: "Peça sobressalente padrão",
    2007: "Aleta",
    2008: "ps9",
    2009: "ps10",
    #front wheel well accessory names
    3000: "Buzina dupla",
    3001: "Para-choques do Joe",
    3002: "Estribos de cobalto",
    3003: "Descarga lateral cobra",
    3004: "Descarga lateral reta",
    3005: "Para-choques vazados",
    3006: "Estribos de carbono",
    3007: "Estribos de madeira",
    3008: "fw9",
    3009: "fw10",
    #rear wheel well accessory names (twisty twisty)
    4000: "Canos de descarga traseiros curvos",
    4001: "Para-lamas",
    4002: "Escapamento duplo",
    4003: "Aletas duplas lisas",
    4004: "Para-lamas lisos",
    4005: "Escapamento quadrado",
    4006: "Acabamento duplo",
    4007: "Megaescapamento",
    4008: "Aletas duplas simétricas",
    4009: "Aletas duplas redondas",
    4010: "Para-lamas simétricos",
    4011: "Para-lamas do Mickey",
    4012: "Para-lamas vazados",
    #rim accessory names
    5000: "Turbo",
    5001: "Lua",
    5002: "Emendado",
    5003: "Tr\xc3\xaas raios",
    5004: "Pintura da tampa",
    5005: "Coração",
    5006: "Mickey",
    5007: "Cinco raios",
    5008: "Margarida",
    5009: "Basquete",
    5010: "Hipnótico",
    5011: "Tribal",
    5012: "Diamante",
    5013: "Cinco raios",
    5014: "Roda",
    #decal accessory names
    6000: "Número cinco",
    6001: "Respingo",
    6002: "Quadriculado",
    6003: "Chamas",
    6004: "Corações",
    6005: "Bolhas",
    6006: "Tigre",
    6007: "Flores",
    6008: "Raio",
    6009: "Anjo",
    #paint accessory names
    7000: "Verde-limão",
    7001: "P\xc3\xaassego",
    7002: "Vermelho vivo",
    7003: "Vermelho",
    7004: "Castanho",
    7005: "Siena",
    7006: "Marrom",
    7007: "Canela",
    7008: "Coral",
    7009: "Laranja",
    7010: "Amarelo",
    7011: "Creme",
    7012: "C\xc3\xadtrico",
    7013: "Limão",
    7014: "Verde-água",
    7015: "Verde",
    7016: "Azul-claro",
    7017: "Verde-azulado",
    7018: "Azul",
    7019: "Verde-musgo",
    7020: "Azul-turquesa",
    7021: "Azul-cinzento",
    7022: "Lilás",
    7023: "Púrpura",
    7024: "Rosa",
    7025: "Ameixa",
    7026: "Preto",
    }

RaceHoodSpeedway = "Autódromo"
RaceHoodRural = "Rural"
RaceHoodUrban = "Urbano"
RaceTypeCircuit = "Torneio"
RaceQualified = "classificado"
RaceSwept = "varrido"
RaceWon = "venceu"
Race = "corrida"
Races = "corridas"
Total = "total"
GrandTouring = "Gran Turismo"

def getTrackGenreString(genreId):
    genreStrings = [ "Autódromo",
                     "Pa\xc3\xads",
                     "Cidade" ]
    return genreStrings[genreId].lower()

def getTunnelSignName(trackId, padId):
    # hack for bad naming!
    if trackId == 2 and padId == 0:
        return "tunne1l_citysign"
    elif trackId == 1 and padId == 0:
        return "tunnel_countrysign1"
    else:
        genreId = RaceGlobals.getTrackGenre(trackId)
        return "tunnel%s_%ssign" % (padId + 1, RaceGlobals.getTrackGenreString(genreId))

# Kart Trophy Descriptions
KartTrophyDescriptions = [
    # qualified race trophies
    RaceHoodSpeedway + " " + str(RaceGlobals.QualifiedRaces[0]) + " " + Race + " " + RaceQualified,
    RaceHoodSpeedway + " " + str(RaceGlobals.QualifiedRaces[1]) + " " + Races + " " + RaceQualified,
    RaceHoodSpeedway + " " + str(RaceGlobals.QualifiedRaces[2]) + " " + Races + " " + RaceQualified,
    RaceHoodRural + " " + str(RaceGlobals.QualifiedRaces[0]) + " " + Race + " " + RaceQualified,
    RaceHoodRural + " " + str(RaceGlobals.QualifiedRaces[1]) + " " + Races + " " + RaceQualified,
    RaceHoodRural + " " + str(RaceGlobals.QualifiedRaces[2]) + " " + Races + " " + RaceQualified,
    RaceHoodUrban + " " + str(RaceGlobals.QualifiedRaces[0]) + " " + Race + " " + RaceQualified,
    RaceHoodUrban + " " + str(RaceGlobals.QualifiedRaces[1]) + " " + Races + " " + RaceQualified,
    RaceHoodUrban + " " + str(RaceGlobals.QualifiedRaces[2]) + " " + Races + " " + RaceQualified,
    str(RaceGlobals.TotalQualifiedRaces) + " " + Total + " " + Races + " " + RaceQualified,
    # won race trophies
    RaceHoodSpeedway + " " + str(RaceGlobals.WonRaces[0]) + " " + Race + " " + RaceWon,
    RaceHoodSpeedway + " " + str(RaceGlobals.WonRaces[1]) + " " + Races + " " + RaceWon,
    RaceHoodSpeedway + " " + str(RaceGlobals.WonRaces[2]) + " " + Races + " " + RaceWon,
    RaceHoodSpeedway + " " + str(RaceGlobals.WonRaces[0]) + " " + Race + " " + RaceWon,
    RaceHoodRural + " " + str(RaceGlobals.WonRaces[1]) + " " + Races + " " + RaceWon,
    RaceHoodRural + " " + str(RaceGlobals.WonRaces[2]) + " " + Races + " " + RaceWon,
    RaceHoodUrban + " " + str(RaceGlobals.WonRaces[0]) + " " + Race + " " + RaceWon,
    RaceHoodUrban + " " + str(RaceGlobals.WonRaces[1]) + " " + Races + " " + RaceWon,
    RaceHoodUrban + " " + str(RaceGlobals.WonRaces[2]) + " " + Races + " " + RaceWon,
    str(RaceGlobals.TotalWonRaces) + " " + Total + " " + Races + " " + RaceWon,
    #qualified circuit races
    str(RaceGlobals.WonCircuitRaces[0]) + " " + RaceTypeCircuit + " " + Race + " " + RaceQualified,
    str(RaceGlobals.WonCircuitRaces[1]) + " " + RaceTypeCircuit + " " + Races + " " + RaceQualified,
    str(RaceGlobals.WonCircuitRaces[2]) + " " + RaceTypeCircuit + " " + Races + " " + RaceQualified,
    # won circuit race trophies
    str(RaceGlobals.WonCircuitRaces[0]) + " " + RaceTypeCircuit + " " + Race + " " + RaceWon,
    str(RaceGlobals.WonCircuitRaces[1]) + " " + RaceTypeCircuit + " " + Races + " " + RaceWon,
    str(RaceGlobals.WonCircuitRaces[2]) + " " + RaceTypeCircuit + " " + Races + " " + RaceWon,
    # swept circuit races
    str(RaceGlobals.SweptCircuitRaces[0]) + " " + RaceTypeCircuit + " " + Race + " " + RaceSwept,
    str(RaceGlobals.SweptCircuitRaces[1]) + " " + RaceTypeCircuit + " " + Races + " " + RaceSwept,
    str(RaceGlobals.SweptCircuitRaces[2]) + " " + RaceTypeCircuit + " " + Races + " " + RaceSwept,
    # NOTE: to be added
    GrandTouring,
    # cups (+1 laff each)
    str(RaceGlobals.TrophiesPerCup) + " Troféus de corrida de kart recebidos! Mais acréscimo de pontos de risada!",
    str(RaceGlobals.TrophiesPerCup * 2) + " Troféus de corrida de kart recebidos! Mais acréscimo de pontos de risada!",
    str(RaceGlobals.TrophiesPerCup * 3) + " Troféus de corrida de kart recebidos! Mais acréscimo de pontos de risada!",
    ]

KartRace_TitleInfo = "Preparar para a corrida"
KartRace_SSInfo = "Bem-vindo ao Estádio dos Nerds!\nPé na tábua e segure firme!"
KartRace_CoCoInfo = "Bem-vindo ao Coliseu Saca-Rolhas!\nUse as curvas inclinadas para manter a velocidade!\n"
KartRace_RRInfo = "Bem-vindo ao Autódromo Rústico!\nPreserve os animais e permaneça na pista!\n"
KartRace_AAInfo = "Bem-vindo \xc3\xa0 Pista de Pulos!\nSegure firme! O caminho parece acidentado...\n"
KartRace_CCInfo = "Bem-vindo ao Circuito da Cidade!\nCuidado com os pedestres quando passar pelo centro da cidade!\n"
KartRace_BBInfo = "Bem-vindo \xc3\xa0 Avenida da Neve!\nCuidado com a velocidade. Pode ter gelo na pista.\n"
KartRace_GeneralInfo = "Use Ctrl para lançar as piadas que pegar na pista, e as teclas de setas, para controlar o kart."

KartRace_TrackInfo = {
  RaceGlobals.RT_Speedway_1     : KartRace_SSInfo + KartRace_GeneralInfo,
  RaceGlobals.RT_Speedway_1_rev : KartRace_SSInfo + KartRace_GeneralInfo,
  RaceGlobals.RT_Speedway_2     : KartRace_CoCoInfo + KartRace_GeneralInfo,
  RaceGlobals.RT_Speedway_2_rev : KartRace_CoCoInfo + KartRace_GeneralInfo,
  RaceGlobals.RT_Rural_1        : KartRace_RRInfo + KartRace_GeneralInfo,
  RaceGlobals.RT_Rural_1_rev    : KartRace_RRInfo + KartRace_GeneralInfo,
  RaceGlobals.RT_Rural_2        : KartRace_AAInfo + KartRace_GeneralInfo,
  RaceGlobals.RT_Rural_2_rev    : KartRace_AAInfo + KartRace_GeneralInfo,
  RaceGlobals.RT_Urban_1        : KartRace_CCInfo + KartRace_GeneralInfo,
  RaceGlobals.RT_Urban_1_rev    : KartRace_CCInfo + KartRace_GeneralInfo,
  RaceGlobals.RT_Urban_2        : KartRace_BBInfo + KartRace_GeneralInfo,
  RaceGlobals.RT_Urban_2_rev    : KartRace_BBInfo + KartRace_GeneralInfo,
  }

KartRecordStrings = {
    RaceGlobals.Daily : 'diariamente',
    RaceGlobals.Weekly : 'semanalmente',
    RaceGlobals.AllTime : 'o tempo todo',
    }

KartRace_FirstSuffix = 'o'
KartRace_SecondSuffix = ' o'
KartRace_ThirdSuffix = ' o'
KartRace_FourthSuffix = ' o'
KartRace_WrongWay = 'Direção\nerrada!'
KartRace_LapText = "Volta %s"
KartRace_FinalLapText = "Volta final!"
KartRace_Exit = "Sair da corrida"
KartRace_NextRace = "Próxima Corrida"
KartRace_Leave = "Deixar a corrida"
KartRace_Qualified = "Classificado!"
KartRace_Record = "Recorde!"
KartRace_RecordString = 'Voc\xc3\xaa bateu um novo recorde %s para %s! Seu bônus é %s bilhetes.'
KartRace_Tickets = "Bilhetes"
KartRace_Exclamations = "!"
KartRace_Deposit = "Depósito"
KartRace_Winnings = "Vitórias"
KartRace_Bonus = "Bônus"
KartRace_RaceTotal = "Total da corrida"
KartRace_CircuitTotal = "Total do Circuito"
KartRace_Trophies = "Troféus"
KartRace_Zero = "0"
KartRace_Colon = ":"
KartRace_TicketPhrase = "%s" + KartRace_Tickets
KartRace_DepositPhrase = KartRace_Deposit + KartRace_Colon + "\n" + KartRace_Tickets
KartRace_QualifyPhrase = "Classificar:\n"
KartRace_RaceTimeout = "Tempo esgotado nesta corrida. Seus bilhetes foram reembolsados. Continue tentando!"
KartRace_RaceTimeoutNoRefund = "O tempo da corrida esgotou. Seus bilhetes não foram reembolsados porque o Grande Pr\xc3\xaamio já começou. Continue tentando!"
KartRace_RacerTooSlow = "Voc\xc3\xaa demorou demais para terminar a corrida. Seus bilhetes não foram reembolsados. Continue tentando!"
KartRace_PhotoFinish = "Foto da chegada!"
KartRace_CircuitPoints = 'Pontos do Circuito'

CircuitRaceStart = "O Grande Pr\xc3\xaamio de Toontown está prestes a começar! Para vencer, ganhe o maior número de pontos em tr\xc3\xaas corridas consecutivas!"
CircuitRaceOngoing = "Olá! O Grande Pr\xc3\xaamio de Toontown está acontecendo agora."
CircuitRaceEnd = "E por hoje é só do Grande Pr\xc3\xaamio de Toontown no Autódromo do Pateta. Vejo voc\xc3\xaa na próxima segunda-feira!"

# Trick-or-Treat holiday
TrickOrTreatMsg = 'Voc\xc3\xaa já encontrou\nesta gostosura!'

WinterCarolingMsg = 'Voc\xc3\xaa já cantou aqui!'

#temp lawbot boss dialog text
LawbotBossTempIntro0 = "Humm, o que temos na pauta de casos hoje?"
LawbotBossTempIntro1 = "Arrá, temos o julgamento de um Toon!"
LawbotBossTempIntro2 = "O caso da promotoria é forte."
LawbotBossTempIntro3 = "E aqui estão os defensores públicos."
LawbotBossTempIntro4 = "Espere um pouco... Voc\xc3\xaas são Toons!"
LawbotBossTempJury1 = "A seleção do júri vai começar agora."
LawbotBossHowToGetEvidence = "Toque na tribuna da testemunha para pegar a evid\xc3\xaancia."
LawbotBossTrialChat1 = "A sessão da Corte está aberta"
LawbotBossHowToThrowPies = "Aperte a tecla Insert para arremessar a evid\xc3\xaancia\n nos advogados ou na balança!"
LawbotBossNeedMoreEvidence = "Voc\xc3\xaa precisa de mais evid\xc3\xaancias!"
LawbotBossDefenseWins1 = "Imposs\xc3\xadvel! A defesa venceu?"
LawbotBossDefenseWins2 = "Não. Eu declaro este julgamento nulo! Um novo julgamento será agendado."
LawbotBossDefenseWins3 = "Humpf. Estarei na minha sala."
LawbotBossProsecutionWins = "Eu julgo em favor do querelante"
LawbotBossReward = "O pr\xc3\xaamio é uma promoção e a habilidade de evocar Cogs"
LawbotBossLeaveCannon = "Deixar canhão"
LawbotBossPassExam = "Bah, e da\xc3\xad que voc\xc3\xaa passou no exame da ordem dos advogados?"
LawbotBossTaunts = [
    "%s, eu julgo voc\xc3\xaa em desacato desta corte!",
    "Objeção aceita!",
    "Apague isso dos registros.",
    "Sua apelação foi rejeitada. A sua sentença é a tristeza!",
    "Ordem na corte!",
    ]
LawbotBossAreaAttackTaunt = "Voc\xc3\xaas todos estão em desacato da corte!"

WitnessToonName = "Abel Abelhudo"
WitnessToonPrepareBattleTwo = "Oh, não! Eles estão colocando apenas Cogs no júri!\aRápido, use os canhões e atire alguns jurados Toons nas cadeiras do júri.\aPrecisamos de %d para ter uma balança justa."
WitnessToonNoJuror = "Oh-oh, sem jurados Toons. Vai ser um julgamento dif\xc3\xadcil."
WitnessToonOneJuror = "Legal! Tem 1 Toon no júri!"
WitnessToonSomeJurors = "Legal! Tem %d Toons no júri!"
WitnessToonAllJurors = "Irado! Todos os jurados são Toons!"
WitnessToonPrepareBattleThree = "Rápido, toque na tribuna da testemunha para pegar evid\xc3\xaancias.\aAperte a tecla Insert para arremessar a evid\xc3\xaancia nos advogados, ou no prato da defesa."
WitnessToonCongratulations = "Voc\xc3\xaa conseguiu! Obrigado por uma defesa espetacular!\aAqui ,fique com estes papéis deixados pelo Juiz-chefe.\aCom isto voc\xc3\xaa será capaz de evocar Cogs da sua página Galeria de Cogs."

WitnessToonLastPromotion = "\aUau, voc\xc3\xaa atingiu o n\xc3\xadvel %s do seu Disfarce de Cog!\aOs Cogs não são promovidos mais que isso.\aVoc\xc3\xaa não pode mais atualizar o seu Disfarce de Cog, mas ainda pode continuar trabalhando pela Resist\xc3\xaancia!"
WitnessToonHPBoost = "\aVoc\xc3\xaa fez muito pela Resist\xc3\xaancia.\aO Conselho de Toons decidiu lhe dar mais um ponto de Risada. Parabéns!"
WitnessToonMaxed = "\aVejo que tem um Disfarce de Cog n\xc3\xadvel %s. Impressionante!\aEm nome de todo o Conselho de Toons, obrigado por voltar para defender mais Toons!"
WitnessToonBonus = "Maravilhoso! Todos os advogados estão atordoados. O peso da sua evid\xc3\xaancia foi %s vezes mais denso por %s segundos"

WitnessToonJuryWeightBonusSingular = {
  6: 'Este caso é dif\xc3\xadcil. Voc\xc3\xaa sentou %d jurado Toon, então a sua evid\xc3\xaancia tem um peso-bônus de %d.',
  7: 'Este caso é muito dif\xc3\xadcil. Voc\xc3\xaa sentou %d jurado Toon, então a sua evid\xc3\xaancia tem um peso-bônus de %d.',
  8: 'Este caso é o mais dif\xc3\xadcil. Voc\xc3\xaa sentou %d jurado Toon, então a sua evid\xc3\xaancia tem um peso-bônus de %d.',
}

WitnessToonJuryWeightBonusPlural = {
  6: 'Este caso é dif\xc3\xadcil. Voc\xc3\xaa sentou %d jurados Toon, então a sua evid\xc3\xaancia tem um peso-bônus de %d.',
  7: 'Este caso é muito dif\xc3\xadcil. Voc\xc3\xaa sentou %d jurados Toon, então a sua evid\xc3\xaancia tem um peso-bônus de %d.',
  8: 'Este caso é o mais dif\xc3\xadcil. Voc\xc3\xaa sentou %d jurados Toon, então a sua evid\xc3\xaancia tem um peso-bônus de %d.',
}

# Cog Summons stuff
IssueSummons = "Evocar"
SummonDlgTitle = "Evocar um Cog"
SummonDlgButton1 = "Evocar um Cog"
SummonDlgButton2 = "Evocar um Prédio Cog"
SummonDlgButton3 = "Evocar uma Invasão Cog"
SummonDlgSingleConf = "Gostaria de evocar um %s?"
SummonDlgBuildingConf = "Gostaria de evocar um %s para um prédio Toon próximo?"
SummonDlgInvasionConf = "Gostaria de evocar uma invasão de %s?"
SummonDlgNumLeft = "Voc\xc3\xaa tem %s sobrando."
SummonDlgDelivering = "Evocando..."
SummonDlgSingleSuccess = "Voc\xc3\xaa evocou o Cog com sucesso."
SummonDlgSingleBadLoc = "Desculpe, mas cogs são proibidos aqui. Tente em outro lugar."
SummonDlgBldgSuccess = "Voc\xc3\xaa evocou os Cogs com sucesso. %s concordou em deixá-los tomar %s por um tempo!"
SummonDlgBldgSuccess2 = "Voc\xc3\xaa evocou os Cogs com sucesso. Um Dono de Loja concordou em deixá-los tomar o prédio dele por um tempo!"
SummonDlgBldgBadLoc = "Desculpe, não há prédios Toon por perto para os Cogs tomarem."
SummonDlgInvasionSuccess = "Voc\xc3\xaa evocou os Cogs com sucesso. \xc3\x89 uma invasão!"
SummonDlgInvasionBusy = "Um %s não pôde ser encontrado. Tente novamente quando a invasão dos Cogs terminar."
SummonDlgInvasionFail = "Desculpe, a invasão dos Cogs fracassou."
SummonDlgShopkeeper = "O Dono da Loja "

# Polar Place cheesy effect chat phrases
PolarPlaceEffect1 = NPCToonNames[3306] + ": Bem-vindo ao Lugar Polar!"
PolarPlaceEffect2 = NPCToonNames[3306] + ": Tente isto."
PolarPlaceEffect3 = NPCToonNames[3306] + ": A sua nova apar\xc3\xaancia só vai funcionar em " + lTheBrrrgh + "."

# LaserGrid game Labels
LaserGameMine = "Caça-Caveiras!"
LaserGameRoll = "Combinando"
LaserGameAvoid = "Evite as Caveiras"
LaserGameDrag = "Arraste tr\xc3\xaas da mesma cor em uma fileira"
LaserGameDefault = "Jogo Desconhecido"

# Pinball text
#PinballHiScore = "Maior Pontuação: %d %s\n"
#PinballYourBestScore = "Sua Melhor Pontuação: %d\n"
#PinballScore = "Pontuação: %d x %d : %d"
PinballHiScore = "Maior Pontuação: %s\n"
PinballHiScoreAbbrev = "..."
PinballYourBestScore = "Sua Melhor Pontuação:\n"
PinballScore = "Pontuação:        %d x %d = "
PinballScoreHolder = "%s\n"


# Gardening text
GagTreeFeather = "\xc3\x81rvore de Piada de Pena"
GagTreeJugglingBalls = "\xc3\x81rvore de Piada de Bolinhas de Malabarismo"
StatuaryFountain = "Fonte"
StatuaryToonStatue = "Estátua de Toon"
StatuaryDonald = "Estátua do Donald"
StatuaryMinnie = "Estátua da Minnie"
StatuaryMickey1 = "Estátua do Mickey"
StatuaryMickey2 = "Fonte do Mickey"
StatuaryToon = "Estátua de Toon"
StatuaryToonWave = "Estátua da Onda Toon"
StatuaryToonVictory = "Estátua da Vitória Toon"
StatuaryToonCrossedArms = 'Estátua da Autoridade Toon'
StatuaryToonThinking = 'Estátua do Abraço Toon'
StatuaryMeltingSnowman =' Boneco de neve Derretendo'
StatuaryMeltingSnowDoodle = "Estátua de Doodle de neve"
StatuaryGardenAccelerator = "Fertilizante Instantâneo"
AnimatedStatuaryFlappyCog = "Cog Suspenso"
#see GardenGlobals.py for corresponding FlowerColors
FlowerColorStrings = ['Vermelha','Laranja','Violeta','Azul','Rosa','Amarela','Branca','Verde']
#see GardenGlobals.py for PlantAttributes, keys must match
FlowerSpeciesNames = {
    49: 'Margarida',
    50: 'Tulipa',
    51: 'Cravo',
    52: 'L\xc3\xadrio',
    53: 'Narciso',
    54: 'Tilápia',
    55: 'Petúnia',
    56: 'Rosa',
    }
#see GardenGlobals.py for PlantAttributes, keys must match, varieties must match
FlowerFunnyNames = {
    49: ('Margarida Lida',
         'Margarida Sumida',
         'Margarida Querida',
         'Margarida Lambida',
         'Margarida Ca\xc3\xadda',
         'Margarida Subida',
         'Margarida Enlouquecida',
         'Margarida Esclarecida',
         ),
    50:  ('Eulipa',
          'Tulipas',
          'Elelipa',
          ),
    51:  ('Encravou',
          'Cravado',
          'Cravo H\xc3\xadbrido',
          'Cravo de Lado',
          'Cravo Modelo',
          ),
    52: ('De L\xc3\xadrio',
         'Co L\xc3\xadrio',
         'L\xc3\xadrio Selvagem',
         'L\xc3\xadrio Figueiro',
         'L\xc3\xadrio Pimenta',
         'L\xc3\xadrio Bobo',
         'Ecl\xc3\xadrio',
         'L\xc3\xadrio D\xc3\xadlio',
         ),
    53: ('Nar-sorriso',
         'Nariz Ciso',
         'Narcisudo',
         'Ante Narciso',
         ),
    54: ('Tilápia Pudo',
         'Ene-A-O-Tilápia',
         'Tilapiano',
         'Tilapiada',
         'Tilápia Sábia',
         ),
    55: ('Car Petúnia',
         'Platúnia',
         ),
    56: ("\xc3\x9altima Rosa do Verão",
         'Choque de Rosa',
         'Rosa Tinta',
         'Rosa Fedida',
         'Rosa Aindarrosa',
         ),
    }
FlowerVarietyNameFormat = "%s %s"
FlowerUnknown = "????"
ShovelNameDict = {
    0 : "Latão",
    1 : "Bronze",
    2 : "Prata",
    3 : "Ouro",
    }
WateringCanNameDict = {
    0 : "Pequeno",
    1 : "Médio",
    2 : "Grande",
    3 : "Enorme",
    }
GardeningPlant = "Plantar"
GardeningWater = "Regar"
GardeningRemove = "Remover"
GardeningPick = "Colher"
GardeningFull = "Encher"
GardeningSkill = "Habilidade"
GardeningWaterSkill = "Habilidade na \xc3\x81gua"
GardeningShovelSkill = "Habilidade com a Pá"
GardeningNoSkill = "Nenhuma Habilidade"
GardeningPlantFlower = "Plantar\nFlor"
GardeningPlantTree = "Plantar\n\xc3\x81rvore"
GardeningPlantItem = "Plantar\nItem"
PlantingGuiOk = "Plantar"
PlantingGuiCancel = lCancel
PlantingGuiReset = "Restaurar"
GardeningChooseBeans = "Escolha as balinhas que deseja plantar."
GardeningChooseBeansItem  = "Escolha as balinhas / item que deseja plantar."
GardeningChooseToonStatue = "Escolha o Toon do qual deseja criar uma estátua."
GardenShovelLevelUp = "Parabéns, voc\xc3\xaa ganhou uma nova pá!"
GardenShovelSkillLevelUp = "Parabéns! Voc\xc3\xaa atingiu %(oldbeans)d violetas! Para progredir, voc\xc3\xaa deve coletar %(newbeans)d violetas."
GardenShovelSkillMaxed = "Incr\xc3\xadvel! Voc\xc3\xaa superou sua habilidade com a pá!"

GardenWateringCanLevelUp = "Parabéns, voc\xc3\xaa ganhou um novo regador!"
GardenMiniGameWon = "Parabéns, voc\xc3\xaa regou a planta!"
ShovelTin = "Pá de Latão"
ShovelSteel = "Pá de Aço"
ShovelSilver = "Pá de Prata"
ShovelGold = "Pá de Ouro"
WateringCanSmall = "Regador Pequeno"
WateringCanMedium = "Regador Médio"
WateringCanLarge = "Regador Grande"
WateringCanHuge = "Regador Enorme"
#make sure it matches GardenGlobals.BeanColorLetters
BeanColorWords = ('vermelha', 'verde', 'laranja','lilás','azul','rosa','amarela',
                  'ciano','prata')
PlantItWith = " Plante com %s."
MakeSureWatered = " Primeiramente, certifique-se de que todas as plantas foram regadas."
UseFromSpecialsTab = " Use por meio da guia de especiais na página do jardim."
UseSpecial = "Usar Especial"
UseSpecialBadLocation = 'Voc\xc3\xaa só pode usar isso no seu jardim.'
UseSpecialSuccess = 'Sucesso! Suas plantas regadas acabaram de crescer.'
ConfirmWiltedFlower = "%(plant)s murchou. Tem certeza de que quer remov\xc3\xaa-la? Ela não irá para o seu cesto de flores, e voc\xc3\xaa também não receberá aumento na sua habilidade."
ConfirmUnbloomingFlower = "%(plant)s não está desabrochando. Tem certeza de que quer remov\xc3\xaa-la? Ela não irá para o seu cesto de flores, e voc\xc3\xaa também não receberá aumento na sua habilidade."
ConfirmNoSkillupFlower = "Tem certeza de que quer remover %(plant)s? Ela não irá para o seu cesto de flores, e voc\xc3\xaa também não receberá aumento na sua habilidade."
ConfirmSkillupFlower = "Tem certeza de que quer colher %(plant)s? Ela irá para o seu cesto de flores. Voc\xc3\xaa vai receber um aumento de habilidade."
ConfirmMaxedSkillFlower = "Tem certeza que quer colher as %(plant)s? Elas irão para sua cesta de flores. Suas habilidades N\xc3\x83O aumentarão pois voc\xc3\xaa já atingiu o máximo."
ConfirmBasketFull = "Seu cesto de flores está cheio. Venda algumas flores primeiro."
ConfirmRemoveTree = "Tem certeza de que quer remover %(tree)s?"
ConfirmWontBeAbleToHarvest = " Se voc\xc3\xaa remover esta árvore, voc\xc3\xaa não colherá piadas das árvores mais altas."
ConfirmRemoveStatuary = "Tem certeza de que quer apagar para sempre %(item)s?"
ResultPlantedSomething  = "Parabéns! Voc\xc3\xaa acaba de plantar %s."
ResultPlantedSomethingAn  = "Parabéns! Voc\xc3\xaa acaba de plantar %s."
ResultPlantedNothing = "Isso não funcionou. Por favor, tente uma combinação diferente de balinhas."

GardenGagTree = " \xc3\x81rvore de Brincadeira"
GardenUberGag = "Brincadeira de Uber"

def getRecipeBeanText(beanTuple):
    """
    dado um múltiplo de balinhas, ex. (0,6), retorna uma versão de texto para
    ser exibida para o usuário. (ex: uma balinha vermelha e amarela)
    """
    #first check if all the beans are the same, so we can say something
    #like 7 red jellybeans
    retval = ""
    if not beanTuple:
        return retval
    allTheSame = True
    for index in range(len( beanTuple)):
        if index + 1 < len(beanTuple):
            if not beanTuple[index] == beanTuple[index+1]:
                allTheSame = False
                break

    if allTheSame:
        if len(beanTuple) > 1:
            retval = "%d %s balinhas" % (len(beanTuple),
                                           BeanColorWords[beanTuple[0]])
        else:
            retval = "uma balinha %s" % BeanColorWords[beanTuple[0]]
    else:
        retval += 'a'
        maxBeans = len(beanTuple)
        for index in range(maxBeans):
            if index == maxBeans - 1:
                retval += " e balinha %s" % BeanColorWords[beanTuple[index]]
            elif index == 0:
                retval += " %s" % BeanColorWords[beanTuple[index]]
            else:
                retval += ", %s" % BeanColorWords[beanTuple[index]]

    return retval

GardenTextMagicBeans = "Balas Mágicas"
GardenTextMagicBeansB = "Outras Balas"
GardenSpecialDiscription = "Este texto deveria explicar como usar certo especial do jardim"
GardenSpecialDiscriptionB = "Este texto deveria explicar como usar certo especial do jardim, podicr\xc3\xaa!"
GardenTrophyAwarded = "Uau! Voc\xc3\xaa tem %s de %s flores. Isso merece um troféu e uma melhora na Risada!"
GardenTrophyNameDict = {
    0 : "Carrinho de Mão",
    1 : "Pás",
    2 : "Flor",
    3 : "Regador",
    4 : "Tubarão",
    5 : "Peixe-Espada",
    6 : "Baleia Assassina",
    }
SkillTooLow = "Habilidade\nBaixa Demais"
NoGarden = "Nenhum \nJardim"

def isVowelStart(str):
    """
    A utility function to return true if the first letter in the str is a vowel
    """
    retval = False
    if str and len(str)>0:
        vowels = ['A','E','I','O','U']
        firstLetter = str.upper()[0:1]
        if firstLetter in vowels:
            retval = True
    return retval

def getResultPlantedSomethingSentence( flowerName):
    """
    Returns a gramatically correct sentence when you've successfully planted something
    """
    if isVowelStart(flowerName):
        retval = ResultPlantedSomethingAn % flowerName
    else:
        retval = ResultPlantedSomething % flowerName

    return retval


#Stuff for trolley metagame
TravelGameTitle = "Trilhos de Bonde"
TravelGameInstructions = "Clique para cima ou para baixo para definir seu número de votos. Clique no botão votar para lançar os votos. Chegue ao seu objetivo secreto para conseguir balinhas extras. Ganhe mais votos quando se der bem nos outros jogos."
TravelGameRemainingVotes = "Votos Restantes:"
TravelGameUse = "Usar"
TravelGameVotesWithPeriod = "votos."
TravelGameVotesToGo = "votos restantes"
TravelGameVoteToGo = "voto restante"
TravelGameUp = "PARA CIMA."
TravelGameDown = "PARA BAIXO."
TravelGameVoteWithExclamation = "Vote!"
TravelGameWaitingChoices = "Esperando que outros jogadores votem..."
# cross the bridge later when the first choice is different for each node,
# e.g. NorthWest, NorthEast, etc.
TravelGameDirections = ['PARA CIMA', 'PARA BAIXO']
TravelGameTotals = 'Totais '
TravelGameReasonVotes = 'O bonde está indo para %(dir)s, vencendo por %(numVotes)de votos.'
TravelGameReasonVotesPlural = 'O bonde está indo para %(dir)s, vencendo por %(numVotes)de votos.'
TravelGameReasonVotesSingular = 'O bonde está indo para %(dir)s, vencendo por %(numVotes)de voto.'
TravelGameReasonPlace = '%(name)s desempatou. O bonde está indo para %(dir)s.'
TravelGameReasonRandom = 'O bonde está indo aleatoriamente para %(dir)s.'
TravelGameOneToonVote =   "%(name)s usou %(numVotes)s votos para ir para %(dir)s\n"
TravelGameBonusBeans = "%(numBeans)de Balinhas"
TravelGamePlaying = 'A seguir, o jogo do bonde de %(game)s.'
TravelGameGotBonus = '%(name)s ganhou um bônus de %(numBeans)s balinhas!'
TravelGameNoOneGotBonus = "Ninguém chegou ao seu objetivo secreto. Todos ganham 1 balinha."
TravelGameConvertingVotesToBeans = "Convertendo alguns votos em balinhas..."
TravelGameGoingBackToShop ="Só resta 1 jogador. Indo para a Loja de Piadas do Pateta."

PairingGameTitle = "Jogo de Memória Toon"
PairingGameInstructions = "Aperte Delete para virar uma carta. Combine 2 cartas iguais para marcar um ponto. Combine cartas com o brilho de bônus e ganhe um ponto extra. Ganhe mais pontos virando poucas vezes."
PairingGameInstructionsMulti = "Aperte Delete para virar uma carta. Aperte Ctrl para fazer o sinal para outro jogador virar uma carta. Combine 2 cartas iguais para marcar um ponto. Combine cartas com o brilho de bônus e ganhe um ponto extra. Ganhe mais pontos virando poucas vezes."
PairingGamePerfect = 'PERFEITO!!'
PairingGameFlips = 'Viradas:'
PairingGamePoints = 'Pontos:'

TrolleyHolidayStart = "Vamos começar com os Trilhos de Bonde! Para jogar, embarque em qualquer bonde com 2 ou mais Toons."
TrolleyHolidayOngoing = ""
TrolleyHolidayEnd = "Isso é tudo nos Trilhos de Bonde por hoje. Até a próxima semana!"

TrolleyWeekendStart = "O Fim de Semana dos Trilhos de Bonde vai começar! Para jogar, embarque em qualquer bonde com 2 ou mais Toons."
TrolleyWeekendEnd = "Terminamos com o Fim de Semana dos Trilhos de Bonde."

VineGameTitle = "Cipós da Selva"
VineGameInstructions = "Chegue ao cipó mais \xc3\xa0 direita a tempo. Aperte para Cima ou para Baixo para escalar o cipó. Aperte para Esquerda ou Direita para mudar de direção e pular. Quanto mais baixo voc\xc3\xaa estiver no cipó, mais rápido poderá saltar dele. Colete as bananas se puder, mas evite os morcegos e aranhas."

ValentinesDayStart = "Feliz Dia dos namorados!"
ValentinesDayEnd = "Aquele é todo para Dia dos namorados!"

# Make sure the golf text matches up with GolfGlobals.py
GolfCourseNames = {
    0: "Tacada e Caminhada",
    1: "Tacadas Divertidas",
    2: "Todas as Tacadas"
    }

GolfHoleNames = {
    0: 'Vitória-em-Uma',
    1: 'Sem Dúvida até o Buraco',
    2: 'Só na Descida',
    3: 'Só Vejo Verde',
    4: 'Tacadas Quentes',
    5: '\xc3\x89 na Manteiga',
    6: 'Balanço do Taco',
    7: 'Na Tacada das Cinco Horas',
    8: 'Diversão no Gramadão',
    9: 'A Bola Cai e a Gente Vibra',
    10: 'Nada de Bogey',
    11: 'Hora do Taco',
    12: 'Santa Tacada!',
    13: 'Só um Birdie, Vai',
    14: 'Correndo para o Buraco',
    15: 'Hora da Tacada',
    16: 'Buraco ao Alcance',
    17: 'Mais um Vento e Chega',
    18: 'Vitória-em-Uma-2',
    19: 'Sem Dúvida, até o Buraco-2',
    20: 'Só na Descida-2',
    21: 'Só Vejo Verde-2',
    22: 'Tacadas Quentes-2',
    23: '\xc3\x89 na Manteiga-2',
    24: 'Balanço do Taco-2',
    25: 'Na Tacada das Cinco Horas-2',
    26: 'Diversão no Gramadão-2',
    27: 'A Bola Cai e a Gente Vibra-2',
    28: 'Nada de Bogey-2',
    29: 'Hora do Taco-2',
    30: 'Santa Tacada!-2',
    31: 'Só um Birdie, Vai-2',
    32: 'Correndo para o Buraco-2',
    33: 'Hora da Tacada-2',
    34: 'Buraco ao Alcance-2',
    35: 'Mais um Vento e Chega-2',
    }

GolfHoleInOne = "Buraco-em-Uma"
GolfCondor = "Condor" # four Under Par
GolfAlbatross = "Albatroz" # three under par
GolfEagle = "\xc3\x81guia" # two under par
GolfBirdie = "Passarinho" # one under par
GolfPar = "Par"
GolfBogey = "Bogey" # one over par
GolfDoubleBogey = "Bogey Duplo" # two over par
GolfTripleBogey = "Bogey Triplo" # three over par

GolfShotDesc = {
    -4: GolfCondor,
    -3: GolfAlbatross,
    -2: GolfEagle,
    -1: GolfBirdie,
    0: GolfPar,
    1: GolfBogey,
    2: GolfDoubleBogey,
    3: GolfTripleBogey,
    }


from toontown.golf import GolfGlobals

CoursesCompleted = "Percursos Conclu\xc3\xaddos"
CoursesUnderPar = "Percursos Abaixo do Par"
HoleInOneShots = "Jogadas de Buraco-em-Uma"
EagleOrBetterShots = "Jogadas de Eagle ou Melhor"
BirdieOrBetterShots = "Jogadas de Birdie ou Melhor"
ParOrBetterShots = "Jogadas de Par ou Melhor"
MultiPlayerCoursesCompleted = "Concursos Multiplayer Conclu\xc3\xaddos"
TwoPlayerWins = "Vitórias com Dois Jogadores"
ThreePlayerWins = "Jogadas com Tr\xc3\xaas Jogadores"
FourPlayerWins = "Jogadas com Quatro Jogadores"
CourseZeroWins = GolfCourseNames[0] + " Vitórias"
CourseOneWins = GolfCourseNames[1] + " Vitórias"
CourseTwoWins = GolfCourseNames[2] + " Vitórias"

GolfHistoryDescriptions = [
    CoursesCompleted,
    CoursesUnderPar,
    HoleInOneShots,
    EagleOrBetterShots,
    BirdieOrBetterShots,
    ParOrBetterShots,
    MultiPlayerCoursesCompleted,
    CourseZeroWins,
    CourseOneWins,
    CourseTwoWins,
    ]

GolfTrophyDescriptions = [
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][0]) + ' ' + CoursesCompleted,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][1]) + ' ' + CoursesCompleted,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][2]) + ' ' + CoursesCompleted,

    str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][0]) + ' ' + CoursesUnderPar,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][1]) + ' ' + CoursesUnderPar,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][2]) + ' ' + CoursesUnderPar,

    str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][0]) + ' ' + HoleInOneShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][1]) + ' ' + HoleInOneShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][2]) + ' ' + HoleInOneShots,

    str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][0]) + ' ' + EagleOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][1]) + ' ' + EagleOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][2]) + ' ' + EagleOrBetterShots,



    str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][0]) + ' ' + BirdieOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][1]) + ' ' + BirdieOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][2]) + ' ' + BirdieOrBetterShots,

    str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][0]) + ' ' + ParOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][1]) + ' ' + ParOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][2]) + ' ' + ParOrBetterShots,

    str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][0]) + ' ' + MultiPlayerCoursesCompleted,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][1]) + ' ' + MultiPlayerCoursesCompleted,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][2]) + ' ' + MultiPlayerCoursesCompleted,

    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][0]) + ' ' + CourseZeroWins,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][1]) + ' ' + CourseZeroWins,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][2]) + ' ' + CourseZeroWins,

    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][0]) + ' ' + CourseOneWins,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][1]) + ' ' + CourseOneWins,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][2]) + ' ' + CourseOneWins,

    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][0]) + ' ' + CourseTwoWins,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][1]) + ' ' + CourseTwoWins,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][2]) + ' ' + CourseTwoWins,

]

GolfCupDescriptions = [
    str(GolfGlobals.TrophiesPerCup) + " Troféus ganhos",
    str(GolfGlobals.TrophiesPerCup * 2) + " Troféus ganhos",
    str(GolfGlobals.TrophiesPerCup * 3) + " Troféus ganhos",
]

GolfAvReceivesHoleBest = "%(name)s marcou um novo recorde de tacadas em %(hole)s!"
GolfAvReceivesCourseBest = "%(name)s marcou um novo recorde de percurso em %(course)s!!"
GolfAvReceivesCup = "%(name)s ganhou a taça %(cup)s!! Bônus em pontos de risada!"
GolfAvReceivesTrophy = "%(name)s ganhou o troféu %(award)s!!"
GolfRanking = "Posição: \n"
GolfPowerBarText = "%(power)s%%"
GolfChooseTeeInstructions = "Aperte para Esquerda ou Direita para mudar a posição do taco.\nAperte Ctrl para selecionar."
GolfWarningMustSwing = "Atenção: voc\xc3\xaa precisa apertar Ctrl na sua próxima tacada."
GolfAimInstructions = "Aperte para a Esquerda ou Direita para mirar.\nAperte e segure Ctrl para balançar o taco."
GolferExited = "%s saiu do percurso de golfe."
GolfPowerReminder = "Segure Ctrl por Mais Tempo para\nMandar a Bola Mais Longe"


# GolfScoreBoard.py
GolfPar = "Par"
GolfHole = "Buraco"
GolfTotal = "Total"
GolfExitCourse = "Sair do Percurso"
GolfUnknownPlayer = "???"

# GolfPage.py
GolfPageTitle = "Golfe"
GolfPageTitleCustomize = "Personalizador de Golfe"
GolfPageTitleRecords = "Recordes Pessoais"
GolfPageTitleTrophy = "Troféus de Golfe"
GolfPageCustomizeTab = "Personalizar"
GolfPageRecordsTab = "Recordes"
GolfPageTrophyTab = "Troféu"
GolfPageTickets = "Bilhetes: "
GolfPageConfirmDelete = "Apagar Acessório?"
GolfTrophyTextDisplay = "Troféu %(number)s : %(desc)s"
GolfCupTextDisplay = "Taça %(number)s : %(desc)s"
GolfCurrentHistory = "%(historyDesc)s Atual: %(num)s"
GolfTieBreakWinner = "%(name)s venceu o desempate aleatório!"
GolfSeconds = " -  %(time).2f segundos"
GolfTimeTieBreakWinner = "%(name)s venceu o desempate por tempo total de mira!!!"



RoamingTrialerWeekendStart = "Está começando a Tour por Toontown! Jogadores podem entrar em qualquer vizinhança de graça!"
RoamingTrialerWeekendOngoing = "Boas-vindas ao Tour por Toontown! Jogadores podem entrar gratuitamente em qualquer vizinhança!"
RoamingTrialerWeekendEnd = "Terminamos com o Tour por Toontown."

# change double if ToontownBattleGlobals.getMoreXpHolidayMultiplier() changes
MoreXpHolidayStart = "Boas novas! Começou o per\xc3\xadodo de Teste Toon, com o dobro de experi\xc3\xaancia em piadas."
MoreXpHolidayOngoing = "Olá! Estamos no per\xc3\xadodo de Teste Toon, com o dobro de experi\xc3\xaancia em piadas."
MoreXpHolidayEnd = "Terminou o per\xc3\xadodo exclusivo de Teste Toon, com o dobro de experi\xc3\xaancia em piadas. Obrigado por nos ajudar a Testar!"

JellybeanDayHolidayStart = "\xc3\x89 Dia das Balinhas! Ganhe pr\xc3\xaamios de Balinhas em dobro nas Festas!"
JellybeanDayHolidayEnd = "Acabou o Dia das Balinhas. Vejo voc\xc3\xaa no ano que vem."
PartyRewardDoubledJellybean = "Balinhas em Dobro!"

GrandPrixWeekendHolidayStart = "\xc3\x89 o Fim de Semana do Grande Pr\xc3\xaamio no Autódromo do Pateta! Quem jogar gratuitamente ou pagando pode obter a maioria dos pontos em tr\xc3\xaas corridas consecutivas."
GrandPrixWeekendHolidayEnd = "O Fim de Semana do Grande Pr\xc3\xaamio acabou. Vejo voc\xc3\xaa no ano que vem."

KartRace_DoubleTickets = "Double Tickets"

SellbotNerfHolidayStart = "A Operação: Robô Vendedor Tempestade está acontecendo agora! Batalhe contra o VP hoje!"
SellbotNerfHolidayEnd = "A Operação: Robô Vendedor Tempestade terminou. \xc3\x93timo trabalho, Toons!"

LawbotNerfHolidayStart = "Operation: Lawbots Lose is happening now! Battle the CJ today!"
LawbotNerfHolidayEnd = "Operation: Lawbots Lose has ended. Great work, Toons!"

JellybeanTrolleyHolidayStart = "Os Dias de Balinha em Dobro para Jogos de Bonde começaram!"
JellybeanTrolleyHolidayEnd = "Os Dias de Balinha em Dobro para Jogos de Bonde terminaram!"

JellybeanFishingHolidayStart = "Os Dias de Balinha em Dobro para Pescaria começaram!"
JellybeanFishingHolidayEnd = "Os Dias de Balinha em Dobro para Pescaria terminaram!"

JellybeanPartiesHolidayStart = "Os Dias de Balinha em Dobro para Jogos de Grupo começaram!"
JellybeanPartiesHolidayEnd = "Os Dias de Balinha em Dobro para Jogos de Grupo terminaram!"

BankUpgradeHolidayStart = "Aconteceu Algo Toontástico com seu Banco de Balinha!"

HalloweenPropsHolidayStart = "\xc3\x89 Halloween em Toontown!"
HalloweenPropsHolidayEnd = "O Halloween terminou. Bu!"

SpookyPropsHolidayStart = "The Silly Meter spins Toontown into spooky mode!"

BlackCatHolidayStart = "Crie um Gato Preto - Só Hoje!"
BlackCatHolidayEnd = "O Dia do Gato Preto terminou!"

SpookyBlackCatHolidayStart = "Friday 13th means a Black Cat blast!"

TopToonsMarathonStart = "A Maratona de Ano-Novo dos Toons começou!"
TopToonsMarathonEnd = "A Maratona de Ano-Novo dos Toons terminou!"

WinterDecorationsStart = "\xc3\x89 hora da Festa de Natal em Toontown!"
WinterDecorationsEnd = "A Festa de Natal acabou - Feliz Ano-Novo!"

WackyWinterDecorationsStart = "Brrr! The Silly Meter goes from silly to chilly!"

WinterCarolingStart = "As Canções de Natal começaram em Toontown. Cante para a sua Cabeça de Boneco de Neve!"

ExpandedClosetsStart = "Attention Toons: For a limited time, Members can purchase the new 50 item Closet from the Cattlelog for the low price of 50 jellybeans!"

KartingTicketsHolidayStart = "Get double tickets from Practice races at Goofy Speedway today!"

IdesOfMarchStart = "Toons go GREEN!"

LogoutForced = "Voc\xc3\xaa fez algo errado\n e estamos fazendo seu logout automaticamente,\n sua conta também pode estar congelada.\n Experimente dar uma volta lá fora, é divertido."

# DistributedCountryClub.py
CountryClubToonEnterElevator = "%s \nentrou no carrinho de golfe."
CountryClubBossConfrontedMsg = "%s está lutando com o Presidente do Clube!"

# DistributedElevatorFSM.py
ElevatorBlockedRoom = "Todos os desafios devem ser vencidos antes disso."

# DistributedMolefield.py
MolesLeft = "Toupeiras Restantes: %d"
MolesInstruction = "Pisão nas Toupeiras!\nPule nas toupeiras vermelhas!"
MolesFinished = "Pisão nas Toupeiras vencido!"
MolesPityWin = 'Erro ao Pisotear! Mas as toupeiras sa\xc3\xadram.'
MolesRestarted = "Perdeu no Pisão! Recomeçando..."

# DistributedGolfGreenGame.py
BustACogInstruction = "Remova a bola Cog!"
BustACogExit = "Sair por Enquanto"
BustACogHowto = "Como Jogar"
BustACogFailure = "Acabou o Tempo!"
BustACogSuccess = "Sucesso!"

# bossbot golf green games
GolfGreenGameScoreString = "Quebra-Cabeças Restantes: %s"
GolfGreenGamePlayerScore = "Resolveu %s"
GolfGreenGameBonusGag = "Voc\xc3\xaa ganhou %s!"
GolfGreenGameGotHelp = "%s resolveu um Quebra-Cabeça!"

GolfGreenGameDirections = "D\xc3\xaa tacadas nas bolas usando o mouse\n\n\nCombinar tr\xc3\xaas bolas de uma mesma cor as faz cair\n\n\nRemova todas as bolas Cog da tela"

# DistributedMaze.py
enterHedgeMaze = "Corra pela Sebe-Labirinto\n para ganhar bônus de risadas!"
toonFinishedHedgeMaze = "%s \n  terminou em %s lugar!"
hedgeMazePlaces = ["primeiro","segundo","terceiro","quarto"]
mazeLabel = "Corrida no Labirinto!"

# Boarding Group
BoardingPartyReadme = 'Grupo de Abordagem?'
BoardingGroupHide = 'Ocultar'
BoardingGroupShow = 'Exibir Grupo de Abordagem'
BoardingPartyInform = 'Crie um Grupo de Abordagem para o elevador clicando em outro Toon e fazendo um convite.\nNessa área, os Grupos de Abordagem não podem ter mais de %s Toons.'
BoardingPartyTitle = 'Grupo de Abordagem'
QuitBoardingPartyLeader = 'Dispensar'
QuitBoardingPartyNonLeader = 'Deixar'
QuitBoardingPartyConfirm = 'Tem certeza de que quer sair desse Grupo de Abordagem?'
BoardcodeMissing = 'Aconteceu algum erro; tente mais tarde.'
BoardcodeMinLaffLeader = 'Não é poss\xc3\xadvel fazer abordagem com seu grupo porque voc\xc3\xaa tem menos de %s pontos de risada.'
BoardcodeMinLaffNonLeaderSingular = 'Seu grupo não pode fazer abordagem porque %s tem menos de %s pontos de risada.'
BoardcodeMinLaffNonLeaderPlural = 'Seu grupo não pode fazer abordagem porque %s tem menos de %s pontos de risada.'
BoardcodePromotionLeader = 'Seu grupo não pode fazer abordagem porque voc\xc3\xaa não tem méritos de promoção suficientes.'
BoardcodePromotionNonLeaderSingular = 'Seu grupo não pode fazer abordagem porque %s não tem méritos de promoção suficientes.'
BoardcodePromotionNonLeaderPlural = 'Seu grupo não pode fazer abordagem porque %s não tem méritos de promoção suficientes.'
BoardcodeSpace = 'Seu grupo não pode fazer abordagem porque não tem espaço suficiente.'
BoardcodeBattleLeader = 'Seu grupo não pode fazer abordagem porque voc\xc3\xaa está combatendo.'
BoardcodeBattleNonLeaderSingular = 'Seu grupo não pode fazer abordagem porque %s está combatendo.'
BoardcodeBattleNonLeaderPlural = 'Seu grupo não pode fazer abordagem porque %s está combatendo.'
BoardingInviteMinLaffInviter = 'Voc\xc3\xaa precisa de %s Pontos de Risada antes de se tornar associado desse Grupo de Abordagem.'
BoardingInviteMinLaffInvitee = '%s precisa de %s Pontos de Risada antes de se tornar associado desse Grupo de Abordagem.'
BoardingInvitePromotionInviter = 'Voc\xc3\xaa precisa receber uma promoção antes de se tornar associado desse Grupo de Abordagem.'
BoardingInvitePromotionInvitee = '%s precisa receber uma promoção antes de se tornar associado desse Grupo de Abordagem.'
BoardingInviteNotPaidInvitee = '%s precisa ser um Assinante para fazer parte do seu Grupo de Abordagem.'
BoardingInviteeInDiffGroup = '%s já está em outro Grupo de Abordagem.'
BoardingInviteeInKickOutList = '%s foi removido por seu l\xc3\xadder. Apenas o l\xc3\xadder pode reconvidar associados removidos.'
BoardingInviteePendingIvite = '%s tem um convite pendente; tente novamente mais tarde.'
BoardingInviteeInElevator = '%s está ocupado(a) no momento; tente novamente mais tarde.'
BoardingInviteGroupFull = 'Seu Grupo de Abordagem já está completo'
BoardingAlreadyInGroup = 'Voc\xc3\xaa não pode aceitar esse convite porque já está em outro Grupo de Abordagem.'
BoardingGroupAlreadyFull = 'Voc\xc3\xaa não pode aceitar esse convite porque o grupo já está completo.'
BoardingKickOutConfirm = 'Tem certeza de que quer remover %s?'
BoardingPendingInvite = 'Primeiro voc\xc3\xaa tem de resolver\n o convite pendente.'
BoardingCannotLeaveZone = 'Voc\xc3\xaa não pode deixar essa área porque voc\xc3\xaa faz parte de um Grupo de Abordagem.'
BoardingInviteeMessage = "%s gostaria de se juntar ao seu Grupo de Abordagem."
BoardingInvitingMessage = "Convidando %s para seu Grupo de Abordagem."
BoardingInvitationRejected = "%s recusou se juntar ao seu Grupo de Abordagem."
BoardingMessageKickedOut = "Voc\xc3\xaa foi removido do Grupo de Abordagem."
BoardingMessageInvited = "%s convidou %s para o Grupo de Abordagem."
BoardingMessageLeftGroup = "%s deixou o Grupo de Abordagem."
BoardingMessageGroupDissolved = "Seu Grupo de Abordagem foi dispensado pelo l\xc3\xadder do grupo."
BoardingMessageGroupDisbandedGeneric = "Seu Grupo de Abordagem foi dispensado."
BoardingMessageInvitationFailed = "%s tentou convidar voc\xc3\xaa para seu Grupo de Abordagem."
BoardingMessageGroupFull = "%s tentou aceitar seu convite, mas seu grupo estava completo."
BoardingGo = 'IR'
BoardingCancelGo = 'Clique Novamente para\nCancelar o comando Ir'
And = 'e'
BoardingGoingTo = 'Indo Para:'
BoardingTimeWarning = 'Abordando o elevador em '
BoardingMore = 'mais'
BoardingGoShow = 'Indo para\n%s em '
BoardingGoPreShow = 'Confirmando...'

# DistributedBossbotBoss.py
BossbotBossName = "Presidente"
BossbotRTWelcome = "Seus Toons vão precisar de disfarces diferentes."
BossbotRTRemoveSuit = "Primeiramente, tire suas roupas de Cog..."
BossbotRTFightWaiter = "e, então, lute com estes garçons."
BossbotRTWearWaiter = "Bom Trabalho! Agora, coloque as roupas de garçom."
BossbotBossPreTwo1 = "Por que está demorando tanto? "
BossbotBossPreTwo2 = "Vamos, sirva meu banquete!"
BossbotRTServeFood1 = "Hehe, sirva a comida que eu coloco nestas esteiras."
BossbotRTServeFood2 = "Se voc\xc3\xaa servir um Cog tr\xc3\xaas vezes seguidas, ele vai explodir."
BossbotResistanceToonName = "A velha e boa Risada"
BossbotPhase3Speech1 = "O que está acontecendo aqui?!"
BossbotPhase3Speech2 = "Esses garçons são Toons!"
BossbotPhase3Speech3 = "Peguem-nos!!!"
BossbotPhase4Speech1 = "Humpf. Se quero um trabalho bem feito..."
BossbotPhase4Speech2 = "tenho de fazer eu mesmo."
BossbotRTPhase4Speech1 = "Bom Trabalho! Agora, esguiche água no Presidente nas mesas..."
BossbotRTPhase4Speech2 = "ou use bolas de golfe para atrasá-lo."
BossbotPitcherLeave = "Deixar Garrafa"
BossbotPitcherLeaving = "Deixando Garrafa"
BossbotPitcherAdvice = "Use as teclas para esquerda e direita se quiser girar.\nSegure Ctrl para aumentar a força.\nSolte Ctrl para disparar."
BossbotGolfSpotLeave = "Deixar Bola de Golfe"
BossbotGolfSpotLeaving = "Deixando Bola de Golfe"
BossbotGolfSpotAdvice = "Use as teclas para esquerda e direita se quiser girar.\nCtrl dispara."
BossbotRewardSpeech1 = "Não! O Presidente do Conselho não vai gostar disso."
BossbotRewardSpeech2 = "Arrrggghhh!!!!"
BossbotRTCongratulations = "Voc\xc3\xaa conseguiu! Voc\xc3\xaa rebaixou o Presidente!\aPegue estes bilhetes azuis que o Presidente deixou para trás.\aCom eles, voc\xc3\xaa vai poder disparar contra Cogs em batalha."""
BossbotRTLastPromotion = "\aUau, voc\xc3\xaa chegou ao n\xc3\xadvel %s com sua Roupa de Cog!\aOs Cogs não conseguem promoções maiores do que essa.\aVoc\xc3\xaa não pode mais atualizar sua Roupa de Cog, mas, certamente, poderá continuar trabalhando para a Resist\xc3\xaancia!"
BossbotRTHPBoost = "\aVoc\xc3\xaa trabalhou bastante para a Resist\xc3\xaancia.\aO Conselho Toon decidiu lhe dar mais um ponto de Risada. Parabéns!"
BossbotRTMaxed = "\aVejo que voc\xc3\xaa tem uma Roupa de Cog de n\xc3\xadvel %s. Impressionante!\aEm nome do Conselho Toon, agradeço por voltar para defender mais Toons!"
GolfAreaAttackTaunt = "Bola!"
OvertimeAttackTaunts = [ "\xc3\x89 hora de reorganizar.",
                        "Temos gente para demitir."]

#ElevatorDestination Names
ElevatorBossBotBoss = "Batalha do Presidente."
ElevatorBossBotCourse = "Campo de Golfe Cog"
ElevatorBossBotCourse0 = "O Tr\xc3\xaas da Frente"
ElevatorBossBotCourse1 = "O Seis do Meio"
ElevatorBossBotCourse2 = "O Nove dos Fundos"
ElevatorCashBotBoss = "Batalha do Diretor Financeiro"
ElevatorCashBotMint0 = "Casa da Moeda"
ElevatorCashBotMint1 = "Casa da Moeda de Dólar"
ElevatorCashBotMint2 = "Casa da Moeda de Barras de Ouro"
ElevatorSellBotBoss = "Batalha do V. P. S\xc3\xaanior"
ElevatorSellBotFactory0 = "Entrada Principal"
ElevatorSellBotFactory1 = "Entrada Lateral"
ElevatorLawBotBoss = "Batalha do Juiz-Chefe"
ElevatorLawBotCourse0 = "Escritório A"
ElevatorLawBotCourse1 = "Escritório B"
ElevatorLawBotCourse2 = "Escritório C"
ElevatorLawBotCourse3 = "Escritório D"

# CatalogNameTagItem.py
DaysToGo = "Espere\n%s Dias"

# DistributedIceGame.py
IceGameTitle = "Escorregador de Gelo"
IceGameInstructions = "Chegue o mais perto do centro ao final da segunda rodada. Use as teclas de seta para mudar a direção e a força. Aperte Ctrl para lançar seu Toon. Acerte os barris para ganhar mais pontos, e evite a dinamite!"
IceGameInstructionsNoTnt = "Chegue o mais perto do centro ao final da segunda rodada. Use as teclas de seta para mudar a direção e a força. Aperte Ctrl para lançar seu Toon. Acerte os barris para ganhar mais pontos."
IceGameWaitingForPlayersToFinishMove = "Esperando outros jogadores..."
IceGameWaitingForAISync = "Esperando outros jogadores..."
IceGameInfo= "Partida %(curMatch)d/%(numMatch)d, Rodada %(curRound)d/%(numRound)d"
IceGameControlKeyWarning="Lembre-se de apertar a tecla Ctrl!"


#DistributedPicnicTable.py
PicnicTableJoinButton = "Entrar"
PicnicTableObserveButton = "Observar"
PicnicTableCancelButton = "Cancelar"
PicnicTableTutorial = "Como Jogar"
PicnicTableMenuTutorial = "Qual jogo voc\xc3\xaa quer aprender?"
PicnicTableMenuSelect = "Qual jogo voc\xc3\xaa quer jogar?"

#DistributedChineseCheckers.py
ChineseCheckersGetUpButton = "Levantar-se"
ChineseCheckersStartButton = "Iniciar Jogo"
ChineseCheckersQuitButton = "Sair do Jogo"
ChineseCheckersIts = "\xc3\x89 a "

ChineseCheckersYourTurn = "Sua Vez"
ChineseCheckersGreenTurn = "Vez do Verde"
ChineseCheckersYellowTurn = "Vez do Amarelo"
ChineseCheckersPurpleTurn = "Vez do Roxo"
ChineseCheckersBlueTurn = "Vez do Azul"
ChineseCheckersPinkTurn = "Vez do Rosa"
ChineseCheckersRedTurn = "Vez do Vermelho"

ChineseCheckersColorG = "Voc\xc3\xaa é o Verde"
ChineseCheckersColorY = "Voc\xc3\xaa é o Amarelo"
ChineseCheckersColorP = "Voc\xc3\xaa é o Roxo"
ChineseCheckersColorB = "Voc\xc3\xaa é o Azul"
ChineseCheckersColorPink = "Voc\xc3\xaa é o Rosa"
ChineseCheckersColorR = "Voc\xc3\xaa é o Vermelho"
ChineseCheckersColorO = "Voc\xc3\xaa está Observando"

ChineseCheckersYouWon = "Voc\xc3\xaa acaba de ganhar uma partida de Xadrez Chin\xc3\xaas!"
ChineseCheckers = "Xadrez Chin\xc3\xaas."
ChineseCheckersGameOf = " acaba de ganhar uma partida de "

#GameTutorials.py
ChineseTutorialTitle1 = "Objetivo"
ChineseTutorialTitle2 = "Como Jogar"
ChineseTutorialPrev = "Página Anterior"
ChineseTutorialNext = "Próxima Página"
ChineseTutorialDone = "Pronto"
ChinesePage1 = "O objetivo do Xadrez Chin\xc3\xaas é ser o primeiro jogador a mover todas as suas peças do triângulo de baixo do tabuleiro até o triângulo do outro lado. O primeiro jogador a conseguir isso vence!"
ChinesePage2 = "Os jogadores se alternam movendo qualquer pedra de sua própria cor. Uma pedra pode se mover para um buraco ao lado, ou pode saltar por outras pedras. Os saltos devem passar por um mármore e cair em um buraco livre. \xc3\x89 poss\xc3\xadvel combinar saltos para andar mais longe!"

CheckersPage1 = "O objetivo das Damas é deixar o oponente sem poder fazer jogadas. Para isso, voc\xc3\xaa pode capturar todas as suas peças, ou bloqueá-las para que não ele não possa mov\xc3\xaa-las."
CheckersPage2 = "Os jogadores se alternam movendo qualquer pedra de sua própria cor. Uma peça pode se mover para um quadrado diagonal \xc3\xa0 frente. Uma peça só pode se mover para um quadrado que não esteja ocupado por outra peça. As damas seguem as mesmas regras, mas podem se mover para trás."
CheckersPage3 = "Para capturar uma peça do oponente, voc\xc3\xaa deve saltar sobre ela diagonalmente para o quadrado vazio depois dela. Se voc\xc3\xaa puder fazer alguma captura em sua vez, terá de faz\xc3\xaa-la. Voc\xc3\xaa pode combinar capturas, desde que seja com a mesma peça."
CheckersPage4 = "Uma peça se torna dama quando chegar \xc3\xa0 última linha do tabuleiro. Uma peça que acaba de se tornar dama não pode saltar de novo até o próximo turno. Além disso, damas podem se mover para todas as direções e podem mudar de direção ao saltar."



#DistributedCheckers.py
CheckersGetUpButton = "Levantar-se"
CheckersStartButton = "Iniciar Jogo"
CheckersQuitButton = "Sair do Jogo"
CheckersIts = "\xc3\x89 a "
CheckersYourTurn = "Sua Vez"
CheckersWhiteTurn = "Vez do Branco"
CheckersBlackTurn = "Vez do Preto"
CheckersColorWhite = "Voc\xc3\xaa é o Branco"
CheckersColorBlack = "Voc\xc3\xaa é o Preto"
CheckersObserver = "Voc\xc3\xaa está Observando"
RegularCheckers = "Damas."
RegularCheckersGameOf = " acaba de ganhar uma partida de "
RegularCheckersYouWon = "Voc\xc3\xaa acaba de ganhar uma partida de Damas!"

#DistributedFindFour.py
FindFourGetUpButton = "Levantar-se"
FindFourStartButton = "Iniciar Jogo"
FindFourQuitButton = "Sair do Jogo"
FindFourIts = "\xc3\x89 a "

FindFourYourTurn = "Sua Vez"
FindFourYellowTurn = "Vez do Amarelo"
FindFourRedTurn = "Vez do Vermelho"

FindFourColorY = "Voc\xc3\xaa é o Amarelo"
FindFourColorR = "Voc\xc3\xaa é o Vermelho"
FindFourObserver = "Voc\xc3\xaa está Observando"

FindFourYouWon = "You just won a game of Find Four!"
FindFourTie = "This Find Four game has resulted in a Tie!"
FindFour = "Connect 4" # TODO?
FindFourGameOf = " acaba de ganhar uma partida de "

MailNotifyNewItems = "Chegou correio para voc\xc3\xaa!"
MailNewMailButton = "Correio"
MailSimpleMail = "Bilhete"
MailFromTag = "Bilhete de: %s"

# MailboxScreen.py
InviteInvitation = "o convite"
InviteAcceptInvalidError = "O convite não é mais válido."
InviteAcceptPartyInvalid = "Sua festa foi cancelada."
InviteAcceptAllOk = "O anfitrião recebeu sua resposta."
InviteRejectAllOk = "O anfitrião recebeu sua recusa do convite."


# Note Months is 1 based, to correspond to datetime
Months = {
 1: "JANEIRO",
 2: "FEVEREIRO",
 3: "MAR\xc3\x87O",
 4: "ABRIL",
 5: "MAIO",
 6: "JUNHO",
 7: "JULHO",
 8: "AGOSTO",
 9: "SETEMBRO",
10: "OUTUBRO",
11: "NOVEMBRO",
12: "DEZEMBRO"
}

# Note 0 for Monday to match datetime
DayNames = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo")
DayNamesAbbrev = ("SEG", "TER", "QUA", "QUI", "SEX", "S\xc3\x81B", "DOM")

# numbers must match holiday ids in ToontownGlobals
HolidayNamesInCalendar = {
    1: ("Fogos de Artif\xc3\xadcio de Verão", "Comemore o Verão com um espetáculo de fogos de artif\xc3\xadcio a cada hora em cada pátio!"),
    2: ("Fogos de Artif\xc3\xadcio de Ano Novo", "Feliz Ano Novo! Curta um espetáculo de fogos de artif\xc3\xadcio a cada hora em cada pátio!"),
    3: ("Invasão Sanguessuga", "Feliz Halloween! Impeça que os Cogs Sanguessugas invadam Toontown!"),
    4: ("Decoração de Feriados de Inverno", "Comemore os Feriados de Inverno com árvores e postes de iluminação Toontásticos!"),
    5: ("Invasão Esqueletocog", "Impeça que os Esqueletocogs invadam Toontown!"),
    6: ("Invasão Dr. Celebridade ", "Impeça que os Cogs do Dr. Celebridade invadam Toontown!"),
    7: ("Bingo de Peixe", "Quarta-feira do Bingo de Peixe! Todos no lago trabalhando juntos para completar a cartela antes de o tempo esgotar."),
    8: ("Eleição de Espécie de Toon", "Vote na nova espécie de Toon! Será uma Cabra? Será um Porco?"),
    9: ("Dia do Gato Preto", "Feliz Halloween! Crie um Toon Gato Preto Toontástico – Só Hoje!"),
   13: ("Doces ou Travessuras", "Feliz Halloween! Vá atrás das guloseimas por toda Toontown para ganhar uma linda cabeça de abóbora de pr\xc3\xaamio!"),
   14: ("Grande Pr\xc3\xaamio", "Segunda-feira do Grande Pr\xc3\xaamio no autódromo do Pateta! Para vencer, conquiste o maior número de pontos em tr\xc3\xaas corridas consecutivas!"),
   16: ("Fim de Semana do Grande Pr\xc3\xaamio", "Quem jogar gratuitamente ou pagando compete nas corridas do Autódromo do Pateta!"),
   17: ("Trilhas do Bondinho", "Quinta-feira das Trilhas do Bondinho! Embarque em qualquer Bondinho para jogar com dois ou mais Toons."),
   19: ("Sábados Engraçados", "Os sábados são engraçados com o Bingo de Peixe, Grande Pr\xc3\xaamio e  Trilhas do Bondinho o dia todo!"),
   24: ("Idos de Março", "Cuidado com os Idos de Março! Impeça que os Cogs Golpe Sujo invadam Toontown!"),
   26: ("Decoração de Halloween", "Comemore o Halloween deixando as árvores e  postes de iluminação de Toontown assustadores!"),
   28: ("Invasão de Inverno", "Os Robôs Vendedores estão \xc3\xa0 solta espalhando suas táticas de vendas frias!"),
   29: ("Semana Abril Toons", "Comemore o Semana Abril Toons - um feriado construido por Toons para Toons!"),
   33: ("Surpresa de Robô Vendedor 1", "Surpresa de Robô Vendedor! Impeça que os Cogs Reis da Incerta invadam Toontown!"),
   34: ("Surpresa de Robô Vendedor 2", "Surpresa de Robô Vendedor! Impeça que os Cogs Sabe-com-quem-está-falando invadam Toontown!"),
   35: ("Surpresa de Robô Vendedor 3", "Surpresa de Robô Vendedor! Impeça que os Cogs Amigos da Onça invadam Toontown!"),
   36: ("Surpresa de Robô Vendedor 4", "Surpresa de Robô Vendedor! Impeça que os Cogs Agitadores invadam Toontown!"),
   37: ("Enigma de Robô Mercenário 1", "Enigma de Robô Mercenário. Impeça que os Cogs Farsantes invadam Toontown!"),
   38: ("Enigma de Robô Mercenário 2", "Enigma de Robô Mercenário. Impeça que os Cogs Mão de Vaca invadam Toontown!"),
   39: ("Enigma de Robô Mercenário 3", "Enigma de Robô Mercenário. Impeça que os Cogs Conta-moedinhas invadam Toontown!"),
   40: ("Enigma de Robô Mercenário 4", "Enigma de Robô Mercenário. Impeça que os Cogs Destruidores de Números invadam Toontown!"),
   41: ("A Estratégia do Robô da Lei 1", "A Estratégia do Robô da Lei. Impeça que os Cogs Comensais invadam Toontown!"),
   42: ("A Estratégia do Robô da Lei 2", "A Estratégia do Robô da Lei. Impeça que os Cogs Duplo Sentido invadam Toontown!"),
   43: ("A Estratégia do Robô da Lei 3", "A Estratégia do Robô da Lei. Impeça que os Cogs Perseguidores de Ambulância invadam Toontown!"),
   44: ("A Estratégia do Robô da Lei 4", "A Estratégia do Robô da Lei. Impeça que os Cogs Golpe Sujo invadam Toontown!"),
   45: ("O Problema Com Robôs Chefes 1", "O Problema Com Robôs Chefes. Impeça que os Cogs Puxa-sacos invadam Toontown!"),
   46: ("O Problema Com Robôs Chefes 2", "O Problema Com Robôs Chefes. Impeça que os Cogs Ratos de Escritório invadam Toontown!"),
   47: ("O Problema Com Robôs Chefes 3", "O Problema Com Robôs Chefes. Impeça que os Cogs Microempresários invadam Toontown!"),
   48: ("O Problema Com Robôs Chefes 4", "O Problema Com Robôs Chefes. Impeça que os Cogs Facões invadam Toontown!"),
   49: ("Dia da Balinha", "Comemore o Dia da Balinha ganhando Balinhas em dobro nas festas!"),
   53: ("Invasão Reis da Incerta", "Impeça que os Cogs Reis da Incerta invadam Toontown!"),
   54: ("Invasão Conta-moedinha", "Impeça que os Cogs Conta-moedinhas invadam Toontown!"),
   55: ("Invasão Duplo Sentido", "Impeça que os Cogs Duplo Sentido invadam Toontown!"),
   56: ("Invasão de Facão", "Impeça que os Cogs Facões invadam Toontown!"),
   57: ("Toon Cantando", "Comemore as Férias de Inverno cantando por todo o redor de Toontown para uma recompensa \"gelada\"!"),
   59: ("Dia dos namorados dos Toons", "Comemore Dia dos namorados dos Toons de Junho 05 a Junho 14!"),
   72: ("Invasão de Vaquinha de Presépio", "Impeça que os Cogs Vaquinhas de Presépio invadam Toontown!"),
   73: ("Invasão de Pão-duro", "Impeça que os Cogs Pães-duros invadam Toontown!"),
   74: ("Invasão de Operador ", "Impeça que os Cogs Telemarqueteiros invadam Toontown!"),
   75: ("Invasão de Caça-\x04talentos", "Impeça que os Cogs Caça-\x04talentos invadam Toontown!"),
   76: ("Invasão de Relações Públicas", "Impeça que os Cogs Relações Públicas invadam Toontown!"),
   77: ("Invasão de Sacos de Dinheiro", "Impeça que os Cogs Sacos de Dinheiro invadam Toontown!"),
   78: ("Invasão de Duas Caras", "Impeça que os Cogs Duas Caras invadam Toontown!"),
   79: ("Invasão de Amizade Fácil", "Impeça que os Cogs Amizades Fáceis invadam Toontown!"),
   80: ("Invasão de Agiotas", "Impeça que os Cogs Agiotas invadam Toontown!"),
   81: ("Invasão de Aventureiro Corporativo", "Impeça que os Cogs Aventureiros Corporativos invadam Toontown!"),
   82: ("Invasão de Barão Ladrão", "Impeça que os Cogs Barões Ladrões invadam Toontown!"),
   83: ("Invasão de Macaco Velho", "Impeça que os Cogs Macacos Velhos invadam Toontown!"),
   84: ("Invasão de Perucões", "Impeça que os Cogs Perucões invadam Toontown!"),
   85: ("Invasão de Queijões", "Impeça que os Cogs Queijões invadam Toontown!"),
   86: ("Invasão de Diminuidores", "Impeça que os Cogs Diminuidores invadam Toontown!"),
   87: ("Invasão de Agitador", "Impeça que os Cogs Agitadores invadam Toontown!"),
   88: ("Invasão de Duplo Sentido", "Impeça que os Cogs Duplos Sentidos invadam Toontown!"),
   89: ("Invasão de Mão de Vaca", "Impeça que os Cogs Mãos de Vaca invadam Toontown!"),
   90: ("Invasão de Dr. Sabe-com-\x04quem-está-\x04falando", "Impeça que os Cogs Drs. Sabe-com-\x04quem-está-\x04falando invadam Toontown!"),
   91: ("Invasão de Perseguidor de Ambulância", "Impeça que os Cogs Perseguidores de Ambulância invadam Toontown!"),
   92: ("Invasão de Micro\x04empresário", "Impeça que os Cogs Micro\x04empresários invadam Toontown!"),
   93: ("Invasão de Destruidor de Números", "Impeça que os Cogs Destruidores de Números invadam Toontown!"),
   95: ("Festas da vitória", "Comemore nosso triunfo histórico contra os Cogs!"), # placeholder
   96: ("Operação: Robô Vendedor Tempestade!", "Quartel do Robô Vendedor está aberto para todos. Vamos lutar com o VP"),
   97: ("Dias de Balinha em Dobro - Jogos de Bonde", ""),
   98: ("Dias de Balinha em Dobro - Pescaria", ""),
   99: ("Semana da Balinha", "Comemore Semana da Balinha com recompensa de Balinha em dobro!"),
   #105: ("Idos de Março", "Os Idos de Março estão aqui"),
   105: ("Toons vai VERDE!", "Toons faz uma cena verde com Balinhas Verdes na Rua dos Carvalhos nos Jardins da Margarida"),
    }

UnknownHoliday = "Feriado Desconhecido %d"
HolidayFormat = "%m/%d "

# parties/ToontownTimeManager.py
TimeZone = "Brazil/West"

# Cogdo Memos
CogdoMemoGuiTitle = "Memos:"
CogdoMemoNames = "Barrel-Destruction Memos"

# Cogdo Stomper Game
CogdoStomperName = "Stomp-O-Matic"

# Cogdo Boardroom Game
BoardroomGameTitle = "Boardroom Hijinks"
BoardroomGameInstructions = ("The COGS are having a meeting to decide what to do with stolen gags. "
                             "Slide on through and grab as many gag-destruction memos as you can!")

# Cogdo Crane Game
CogdoCraneGameTitle = "Vend-A-Stomper"
CogdoCraneGameInstructions = ("The COGS are using a coin-operated machine to destroy laff barrels. "
                              "Use the cranes to pick up and throw money bags, in order to prevent "
                              "barrel destruction!")

# Cogdo Maze Game
CogdoMazeGameTitle = "Mover & Shaker\nField Office"
CogdoMazeGameInstructions = "The big Mover & Shaker Cogs have the code to open the door. Defeat them with your water balloons in order to get it!"
CogdoMazeIntroMovieDialogue = (("This is the Toon Resistance! The Movers & Shakers\nhave our Jokes, and they've locked the exit!",),
                               ("Grab water balloons at coolers, and throw them at Cogs!\nSmall Cogs drop Jokes, BIG COGS open the exit.",),
                               ("The more Jokes you rescue, the bigger your Toon-Up\nat the end. Good luck!",),
                               )
CogdoMazeGameDoorOpens = "THE EXIT IS OPEN FOR 60 SECONDS!\nGET THERE FAST FOR A BIGGER TOON-UP!"
CogdoMazeGameLocalToonFoundExit = "The exit will open when\nyou've busted all four BIG COGS!"
CogdoMazeGameWaitingForToons = "Waiting for other Toons..."
CogdoMazeGameTimeOut = "Oh no, time ran out! You lost your jokes."
CogdoMazeGameTimeAlert = "Hurry up! 60 seconds to go!"
CogdoMazeGameBossGuiTitle = "BIG COGS:"
CogdoMazeFindHint = "Find a Water Cooler!"
CogdoMazeThrowHint = "Press 'Ctrl' to throw your water balloon!"
CogdoMazeSquashHint = "Falling objects pop your balloon!"
CogdoMazeBossHint = "Big Cogs take TWO hits to defeat!"
CogdoMazeMinionHint = "Smaller Cogs drop jokes!"

# Cogdo Flying Game
CogdoFlyingGameTitle = "Legal Eagle Offices"
CogdoFlyingGameInstructions = "Fly through the Legal Eagles' lair. Watch out for obstacles and cogs along the way, and don't forget to refuel your helicopter!"
CogdoFlyingIntroMovieDialogue = (("You won't ruffle our feathers, Toons! We're destroying barrels of your Laff, and you cannot stop us!",
                                  "A flock of Toons! We're crushing barrels of your Laff in our %s, and there's nothing you can do about it!" % CogdoStomperName,
                                  "You can't egg us on, Toons! We're powering our offices with your Laff, and you're powerless to stop us!"),
                                 ("This is the Toon Resistance! A little bird told me you can use propellers to fly around, grab Barrel Destruction Memos, and keep Laff from being destroyed! Good luck, Toons!",
                                  "Attention Toons! Wing it with a propeller and collect Barrel Destruction Memos to keep our Laff from being stomped! Toon Resistance out!",
                                  "Toon Resistance here! Cause a flap by finding propellers, flying to the Barrel Destruction Memos, and keeping our Laff from being smashed! Have fun!"),
                                 ("Squawk! I'm a Silver Sprocket Award winner, I don't need this!",
                                  "Do your best, Toons! You will find us to be quite talon-ted!",
                                  "We'll teach you to obey the pecking order, Toons!"),
                                  )
CogdoFlyingGameWaiting = "Waiting for other Toons%s"
CogdoFlyingGameFuelLabel = "Fuel"
CogdoFlyingGameLegalEagleTargeting = "A Legal Eagle has noticed you!"
CogdoFlyingGameLegalEagleAttacking = "Incoming Eagle!"
CogdoFlyingGamePickUpAPropeller = "You need a propeller to fly!"
CogdoFlyingGamePressCtrlToFly = "Press 'Ctrl' to fly up!"
CogdoFlyingGameYouAreInvincible = "Red Tape protects you!"
CogdoFlyingGameTimeIsRunningOut = "Time is running out!"
CogdoFlyingGameMinimapIntro = "This meter shows your progress!\nX marks the finish line."
CogdoFlyingGameMemoIntro = "Memos prevent Laff Barrels in\nthe Stomper Room from being destroyed!"
CogdoFlyingGameOutOfTime = "Oh No! You ran out of time!"
CogdoFlyingGameYouMadeIt = "You made it on time!"
CogdoFlyingGameYouMadeIt = "Good work, you made it on time!"
CogdoFlyingGameTakingMemos = "The legal eagles took all your memos!"

# Cogdo Elevator Reward
CogdoElevatorRewardLaff = "Great job, Toons!\nYou get a Toon-Up from the jokes you saved!"

# Cogdo Executive Suite
CogdoExecutiveSuiteTitle = "Executive Suite"
CogdoExecutiveSuiteIntroMessage = "Oh no, they've got the shop keeper!\nDefeat the Cogs and free the captive."
CogdoExecutiveSuiteToonThankYou = "Thanks for the rescue!\nIf you need help in a fight, use this SOS card to call my friend %s."
CogdoExecutiveSuiteToonBye = "Bye!"

# Silly Surge Terms
SillySurgeTerms = {
    1:  "Ascensão Divertida!",
    2:  "Onda de Bobagem!",
    3:  "Aumento Rid\xc3\xadculo!",
    4:  "Crescimento de Risadinha!",
    5:  "Est\xc3\xadmulo Engraçado!",
    6:  "Impulso Raro!",
    7:  "Escalada Doida!",
    8:  "Salto Feliz!",
    9:  "Levantamento Insano!",
    10: "Caminhada Alegre!",
    11: "Aumento Insano!",
    12: "Aumento Forçado!"
    }
# Interactive Prop Text
InteractivePropTrackBonusTerms = {
    0:  "Super Toonar",
    1:  "",
    2:  "",
    3:  "",
    4:  "Superarremesso",
    5:  "Superesguicho!",
    6:  ""
}

PlayingCardUnknown = "Nome de Cartão desconhecido"
