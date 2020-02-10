import os
import csv
from time import gmtime, strftime
class Team:
    def __init__(self,name,list_dni):
        self.name = name   
        self.listDNI = list_dni
        self.assistance = "NO"
        self.date = ""
        self.startTime = ""
        self.endTime = ""
    def __repr__(self):
        return  str(self.listDNI)
    def change_assistance(self):
        self.assistance = "SI"
    
    def find_DNI(self,var):
        try:
          if float(var) in self.listDNI:
            return True
        except ValueError:
            return 
        return False
    def change_endT(self):
        hour = strftime("%H", gmtime())
        hour = int(hour) - 5
        self.endTime = strftime(str(hour)+":%M:%S", gmtime())
    def change_date(self):
        self.date = strftime("%Y-%m-%d", gmtime())
        hour = strftime("%H", gmtime())
        hour = int(hour) - 5
        self.startTime = strftime(str(hour)+":%M:%S", gmtime())

list_teams = []

team1 = Team("academia pre  universitaria  virtual ALTO NIVEL",[41860420,41265182,41860420,72640448])
team2 = Team("TOGO",[70326247])
team3 = Team("t-mensajeo",[43185022,42273812])
team4 = Team("SocialTEC",[72417249,70321701,74092883])
team5 = Team("ALTERNATIVAS SOSTENIBLES PARA EL TRATAMIENTO DE AGUAS RESIDUALES INDUSTRIALES MEDIANTE EL USO DE HUMEDALES CONSTRUIDOS",[72463147])
team6 = Team("PapayaHR",[74170429,74586845,74585249])
team7 = Team("Green Car Simulator",[74170429,22995555])
team8 = Team("YucaO2",[46498771])
team9 = Team("AllynCose",[76738097,70552749,71498374,70553164])
team10 = Team("Sculptor.cc",[46847148,46933133])
team11 = Team("TURISMO VIVENCIAL",[74220497,45353939,29683967,71429983])
team12 = Team("29683967",[72618879,71768688,70774633])
team13 = Team("cucharas y tazas comestibles",[71635622,73707270,72966797])
team14 = Team("AirNova",[71624415,73451618,73451618,74049024])
team15 = Team("DR: GREEN PHAMPA",[29730413])
team16 = Team("Grupo Geagreen",[75781967,76216312,72117672,44303131])
team17 = Team("Gemelas MPH",[43041056,43041056])
team18 = Team("TECNOLOGÍA E INNOVACIÓN EN LA CONSTRUCCIÓN",[47490812,74050861,77328325])
team19 = Team("TARWIN, Antojos que Alimentan",[70178866,72427687])
team20 = Team("VIVE TU CARRERA AHORA",[45318880])
team21 = Team("TUTU",[71477929,73640513,75971979])
team22 = Team("Myco-ladrillos",[71532701,76723146])
team23 = Team("lowprovider.com",[76189211])
team24 = Team("Safe Paths",[71581717,72205691])
team25 = Team("Melenia",[29583636])
team26 = Team("Aceites esenciales Olimpo",[42904635,43053791,43002066])
team27 = Team("SCENTINET INNOVACIÓN Y PROSPECTIVA",[42172094])
team28 = Team("Renuevate",[45632840])
team29 = Team("GII MEDICAL TECHNOLOGIES",[76581850,47750093])
team30 = Team("Anonidioma",[72302148,47543778])
team31 = Team("Chocolates Caplina",[10798156])
team32 = Team("Galletas de Chaco",[70558493,72150448,71432281,72648872])
team33 = Team("Cápsulas de vida",[73940090,48568249,48055715,71217127])
team34 = Team("Moda,diseño y sublimacion VALERO",[76881193])
team35 = Team("Sticks ICE",[47042574,71305993,73112838,70512739])
team36 = Team("JÚPITER",[77057953,71496460,71568556,76339639])
team37 = Team("PADIS",[44474667])
team38 = Team("Abono Green Peace",[75197207,72518750,76227413,73764719])
team39 = Team("NUTRIALIVIO",[73872052,72539101,71459230,71438768])
team40 = Team("IMPORTACION, VENTA Y APLICACION DE RECUBRIMIENTOS POLIMERICOS APLICABLES EN INDUSTRIA ",[47430591,46926535])
team41 = Team("HOGAR LIMPIO JAM",[45878018,48678743,75470859,45878018])
team42 = Team("Centro de Flotación Sensory",[43613645,74039250])
team43 = Team("Alimentacion saludable y nutritiva del Colca para ti",[29601104,29567371])
team44 = Team("HealthyWorld",[75693117,73193491,63193495])
team45 = Team("C.N.E.(Creando un Nuevo Ecosistema)",[77799217,76421124,77799217,77231660])
##team44 = Team("Inge",[40534343,2,3])
team46 = Team("JAKU",[11,22,33,44])



list_teams.append(team1)
list_teams.append(team2)
list_teams.append(team3)
list_teams.append(team4)
list_teams.append(team5)
list_teams.append(team6)
list_teams.append(team7)
list_teams.append(team8)
list_teams.append(team9)
list_teams.append(team10)
list_teams.append(team11)
list_teams.append(team12)
list_teams.append(team13)
list_teams.append(team14)
list_teams.append(team15)
list_teams.append(team16)
list_teams.append(team17)
list_teams.append(team18)
list_teams.append(team19)
list_teams.append(team20)
list_teams.append(team21)
list_teams.append(team22)
list_teams.append(team23)
list_teams.append(team24)
list_teams.append(team25)
list_teams.append(team26)
list_teams.append(team27)
list_teams.append(team28)
list_teams.append(team29)
list_teams.append(team30)
list_teams.append(team31)
list_teams.append(team32)
list_teams.append(team33)
list_teams.append(team34)
list_teams.append(team35)
list_teams.append(team36)
list_teams.append(team37)
list_teams.append(team38)
list_teams.append(team39)
list_teams.append(team40)
list_teams.append(team41)
list_teams.append(team42)
list_teams.append(team43)
list_teams.append(team44)
list_teams.append(team45)
list_teams.append(team46)

def write_alldata(list_teams):

    fname = "asistencia.csv"
    if os.path.isfile(fname):
        return 
    else:
        with open('asistencia.csv', 'a', newline='') as file:
                    fieldnames = ['Nombre del emprendimiento', 'Asistencia','Dia','Hora Entrada']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    for one_list in list_teams:
                        writer.writerow({'Nombre del emprendimiento': one_list.name, 
                                        'Asistencia': one_list.assistance,
                                        'Dia':one_list.date,
                                        'Hora Entrada':one_list.startTime})
