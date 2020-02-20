import os
import csv
from time import gmtime, strftime

class Person:
    def __init__(self,name,dni,cellphone=""):
        self.name = name
        self.dni = dni
        self.cellphone = cellphone
        self.came = False

    def get_DNI(self):
        return self.name
    def set_came(self):
        self.came = True

class Team:
    def __init__(self,name,list_person):
        self.name = name   
        self.list_people = list_person
        self.assistance = ""
        self.date = ""
        self.startTime = ""
        self.endTime = ""
    def __repr__(self):
        return  str(self.list_people)
    def change_assistance(self):
        self.assistance = "SI"
    
    def find_DNI(self,var):
        try:
            for obj in self.list_people:
                if float(var) == obj.dni:
                    obj.set_came()
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


personA1 = Person("ARAUJO SALAS WALTER HENRY",41860420)
personA2 = Person("CHAVEZ CASTILLO DONY GUILLERMO",41265182)
personA3 = Person("HIGINIO GOMEZ JENNIFER SHEILA",72640448)
personA4 = Person("MACHACO CATARI JUAN",46694937)
personB1 = Person("CHALCO ORTEGA GIANCARLO ANDRES",70326247)
personC1 = Person("HINOJOSA CARDENA EDWARD",43185022,963720589)
personC2 = Person("TAPIA CANAZA RICARDO",42273812,958191549)
personD1 = Person("MOLLEAPAZA FLORES OSCAR MANASES",72417249)
personD2 = Person("MAMANI CANAZA CESAR WILLY",70321701)
personD3 = Person("FLORES CHAMBILLA FREMY",74092883)
personE1 = Person("PINEDA ZAPANA JENYFER STEYSI",72463147)
personE2 = Person("CACERES QUICÑO LIZ",70521771,959094857)

personF1 = Person("CCAHUANA ROJAS FRANKLYN",74170429)
personF2 = Person("VILCA SOTOMAYOR ROSELIN MILAGROS",74586845)
personF3 = Person("SANTAMARIA SANTISTEBAN DINA FIORELA",74585249)
personG1 = Person("CCAHUANA ROJAS FRANKLYN",74170429)
personG2 = Person("AURA YUPANQUI OCTAVIO",22995555)
personH1 = Person("CCOAQUIRA ENRIQUEZ HARRY ELVIS",46498771)
personI0 = Person("HUMPIRE CUTIPA HAYDE LUZMILA",76738097)
personI1 = Person("CHOQUECOTA SOTO ANA CECILIA",70552749)
personI2 = Person("HUAMAN CANQUI JAIR FRANCESCO",71498374)
personI3 = Person("SALCEDO ALMIRON MELVIN DAVID",70553164)
personJ0 = Person("RAMOS HUMPIRE ALESSANDRO FRANCISCO",46847148)
personJ1 = Person("FLORES BELLIDO ANGEL JOSE",46933133)
personJ2 = Person("VELAYARCE RIVEROS JESSENIA",47588161,951761495)

personK0 = Person("MACHACA ARCEDA MIGUEL ANGEL",74220497,993001938)
personK1 = Person("CHAVEZ LOPEZ CAROLINA BONIEE",45353939,958536680)
personK2 = Person("SOCOLICH FERNANDEZ RENZO IVAN",29683967,959526685)
personK3 = Person("BARRIOS BELLIDO NINO",71429983)###########

personJ0 = Person("ROSAS AROTAYPE OSCAR EUGENIO",72618879)
personJ1 = Person("SUBIA HUAMAN EDGAR ANDRE",71768688)
personJ2 = Person("LAZO QUEVEDO JESUS",70774633)
personL0 = Person("CHICYA USCA KAREN CAMILA",71635622)
personL1 = Person("MAMANI CCAMA ORLANDO",73707270)
personL2 = Person("CONDESO DIAZ SASHENKA ANTUANET",72966797)
personM1 = Person("CHARCA MOROCCO HERNAN WILSON",71624415,983132663)
personM2 = Person("JUAREZ CHAVEZ BILLY STEVE",73451618,989389866)
personM3 = Person("MOLLEAPAZA HUANACO JULIAN ERNESTO",74049024)
personN1 = Person("SUAREZ CHAVEZ, TEOBALDO",29730413)

personO1 = Person("MOLLINEDO CANDIA RODRIGO",75781967,928012453)
personO2 = Person("ATENCIO VILCARANA ROSELY MILAGROS",76216312,944523360)
personO3 = Person("QUISPE APAZA SUSAN STEPHANY",72117672,972139325)
personO4 = Person("CHOQUEHUAYTA GUILLEN MIGUEL ANGEL",44303131,44303131)
person05 = Person("Tovar Vargas Juber Caleb",76370291,992118250)

personP1 = Person("HUSCA BARRIENTOS LUZGARDO GUILMAR",43041056)
personQ1 = Person("PAYEHUANCA VEGA PATRICIO RUIZ",47490812)
personQ2 = Person("PAYEHUANCA VEGA PATRICIO ROSSELL",74050861)
personQ3 = Person("CACERES LLAZA PERCY",77328325)
personR1 = Person("VELASQUEZ HUANCACHOQUE AMBAR XIOMARA",70178866)
personR2 = Person("ARROYO PALACIOS GRACE SHABELY",72427687)

personS1 = Person("GUTIERREZ LINARES EDWIN",45318880,946648774)
personS2 = Person("SUPO CHALCO WILSON",44032629,97855012)
personS3 = Person("SALCEDO GRADO ELSA",45311147,924737594)

personT1 = Person("ANCASI HUISA, HENRRY ABEL",71477929)
personT2 = Person("PAUCAR NUÑEZ, JOSEPH CLINTHON",73640513)
personT3 = Person("-",75971979)
personU1 = Person("DIAZ ALCAZAR OSCAR RENAUD",71532701)
personU2 = Person("CARLOS MENDOZA JUAN ADRIEL",76723146)
personV1 = Person("GUZMAN VIZARRETA JOSE ANTONIO",76189211)
personW1 = Person("ANCCASI FIGUEROA GUADALUPE PAULINA",71581717)
personW2 = Person("PEREZ VIZCARRA ALDO ALEXIS",72205691,968575730)
personX1 = Person("AQUISE ESCOBEDO SILVIA MELENIA",29583636,959663699)
personY1 = Person("YANCAPALLO VILCA ENRIQUE JAVIER",42904635)
personY2 = Person("HUACCA AROHUILLCA ELIZABETH ZAYDA",43053791)
personY3 = Person("MAMANI VILCA FRANCISCO MIGUEL",43002066,953706566)
personZ1 = Person("MEDINA CARPIO OSCAR CHRISTIAN",42172094)
personAA1 = Person("ESTREMADOYRO CUMPA ALBA GUADALUPE",45632840,962957208)
personAB1 = Person("CHALCO ORDOÑEZ JOSE CARLOS",76581850)
personAB2 = Person("PUMA PILLCO JEAN PIERRE",47750093,969784886)
personAC1 = Person("IQUIRA BECERRA DIEGO ALONSO",72302148)
personAC2 = Person("RODRÍGUEZ URQUIAGA ROBERTO JOSUÉ",47543778)
personAD1 = Person("PEREZ YUPANQUI ENRIQUE DANIEL",10798156)
personAE1 = Person("MEDINA ORTIZ JAFETH ENRIQUE",70558493)
personAE2 = Person("BUTRON MONTEROLA DIEGO MARTIN",72150448)
personAE3 = Person("VERAPINTO SALAS ANA GABRIELA",71432281)
personAE4 = Person("MENDOZA PALMA PATRICK EDSON",72648872)
personAF1 = Person("VALDIVIA TICONA ELVA MARIA",73940090)
personAF2 = Person("PEÑALOZA CABANA ESTEFHANY",48568249,951204457)
personAF3 = Person("LAYME PONCE ISABEL MARIA",48055715)
personAF4 = Person("QUECCAÑO QUISPE AYDE ROXANA",71217127,937352192)
personAG1 = Person("CHITE VALERO DIANA CAROLINA",76881193)
personAH1 = Person("ALVARADO PURIHUAMAN GUINMER CARLOMAN",47042574,965832448)
personAH2 = Person("TRUJILLO LUCIANO ROYER WALTER",71305993,921041242)
personAH3 = Person("MENDOZA PINEDA TERRY ANDRE",73112838,987581774)
personAH4 = Person("CHACON ZAPATA GERARDO ENRIQUE",70512739,900672434)
personAI1 = Person("ITO ADCO FERNANDO JOSE",77057953)
personAI2 = Person("DE LA CRUZ GONZALES JOSE CARLOS",71496460)
personAI3 = Person("-",71568556)
personAI4 = Person("SALAZAR VENTURA FABRICIO DAVID",76339639)
personAJ1 = Person("ARAGONES ALFARO MARTIN RAUL",44474667)
personAK1 = Person("TACCA MAMANI LIZBETH MARILUZ",75197207)
personAK2 = Person("PINEDA ALCCAHUAMAN LIZBETH",72518750)
personAK3 = Person("CUTIPA PUMA JUDITH SARA",76227413)
personAK4 = Person("BENITEZ CONSUELO HEIDY",73764719)
personAL1 = Person("CHACON ARRATIA RODOLFO VICENTE",73872052)
personAL2 = Person("SILVA LANCHIPA ALESSANDRA CECILIA",72539101)
personAL3 = Person("MATTOS CUBAS VALERIA CHRISTINA",71459230)
personAL4 = Person("CHACON ARRATIA ANGEL",71438768)
personAM1 = Person("VILLANUEVA ROQUE OSCAR MANUEL",47430591)
personAM2 = Person("YABAR DE LA CRUZ ANA LUZ",46926535)
personAN1 = Person("HERRERA JORGE JOEL EFRAIN",45878018)
personAN2 = Person("CAMA JAVIER ANTHONY",48678743)
personAN3 = Person("PUMA SURCO MARY ROXANA",75470859)
personAN4 = Person("HERRERA JORGE JOEL EFRAIN",45878018)
personAO1 = Person("ALARCON CHIPANA RICHARD MIGUEL",43613645,972794953)
personAO2 = Person("MONTESINOS AGUILAR DE ALARCON CLAUDIA HASSEL",74039250,980993307)
personAP1 = Person("ISUIZA PRADO JOSE FERNANDO",29601104)
personAP2 = Person("CONDORI AROTAYPE MARIA ELENA",29567371)
personAQ1 = Person("QUISPE TOTOCAYO RAUL EDGAR",75693117)
personAQ2 = Person("ALVARO TOTOCAYO CESAR JULIAN",73193491)
personAQ3 = Person("-",63193495)
personAR1 = Person("CAYO CHURA LUIS HERNANDO",77799217)
personAR2 = Person("TORRES CONDORI CESAR AUGUSTO",76421124)
personAR3 = Person("CAYO CHURA LUIS HERNANDO",77799217)
personAR4 = Person("HUARCA COSI FIORELA",77231660)
#EMPRENDEDORES LIBRES
perEmpre01 = Person("ZARATE LUNA WALBERTO",73790636,62760089)
perEmpre02 = Person("ITO APAZA FRIDA LESLY",71022102,928475941)
perEmpre03 = Person("MAMANI CALCINA SANDRA",47810811,928070323)
perEmpre04 = Person("CONCHA LUNA VALERIA",73641297,936210349)
perEmpre05 = Person("GONZALES DIAZ JOEL FABRICIO",73287541,950781859)
perEmpre06 = Person("ZAMATA TEVES ISACAC FRANCO",76156270,978649868)

#DOCENTES
perDoc01 = Person("LOVON LUQUE CINTHYA JEYMI",42012737,959549646)
perDoc02 = Person("MELGAR PAUCA ZAIDA",29490190,959416616)


#Registro de prueba
personJAKU01 = Person("CHAVEZ FRANCO",22,999999)
personJAKU02 = Person("CAIRA AGUILAR",33,988888)
personJAKU03 = Person("Lopez Juan José",44)


team1 = Team("TEACH PERU",[personA1,personA2,personA3])
team2 = Team("TOGO",[personB1])
team3 = Team("t-mensajeo",[personC1,personC2])
team4 = Team("SocialTEC",[personD1,personD2,personD3])
team5 = Team("ALTERNATIVAS SOSTENIBLES PARA EL TRATAMIENTO DE AGUAS RESIDUALES INDUSTRIALES MEDIANTE EL USO DE HUMEDALES CONSTRUIDOS",[personE1])
team6 = Team("Academia Competitiva (PapayaHR)",[personF1,personF2,personF3])
team7 = Team("Green Car Simulator",[personG1,personG2])
team8 = Team("YucaO2",[personH1])
team9 = Team("AllynCose",[personI0,personI1,personI2,personI3])
team10 = Team("Sculptor.cc",[personJ0,personJ1])
team11 = Team("TURISMO VIVENCIAL",[personK0,personK1,personK2,personK3])
team12 = Team("Yala",[personJ0,personJ1,personJ2])
team13 = Team("cucharas y tazas comestibles",[personL0,personL1,personL2])
team14 = Team("AirNova",[personM1,personM2,personM3])
team15 = Team("DR: GREEN PHAMPA",[personN1])
team16 = Team("Grupo Geagreen",[personO1,personO4,personO2,personO3,personO5])
team17 = Team("Gemelas MPH",[personP1])
team18 = Team("TECNOLOGÍA E INNOVACIÓN EN LA CONSTRUCCIÓN",[personQ1,personQ2,personQ3])
team19 = Team("TARWIN, Antojos que Alimentan",[personR1,personR2])
team20 = Team("VIVE TU CARRERA AHORA",[personS1,personS2,personS3])
team21 = Team("TUTU",[personT1,personT2,personT3])
team22 = Team("Myco-ladrillos",[personU1,personU2])
team23 = Team("lowprovider.com",[personV1])
team24 = Team("Safe Paths",[personW1,personW2])
team25 = Team("Melenia",[personX1])
team26 = Team("Aceites esenciales Olimpo",[personY1,personY2,personY3])
team27 = Team("SCENTINET INNOVACIÓN Y PROSPECTIVA",[personZ1])
team28 = Team("Renuevate",[personAA1])
team29 = Team("GII MEDICAL TECHNOLOGIES",[personAB1,personAB2])
team30 = Team("Anonidioma",[personAC1,personAC2])
team31 = Team("Chocolates Caplina",[personAD1])
team32 = Team("Galletas de Chaco",[personAE1,personAE2,personAE3,personAE4])
team33 = Team("Cápsulas de vida",[personAF1,personAF2,personAF3,personAF4])
team34 = Team("Moda,diseño y sublimacion VALERO",[personAG1])
team35 = Team("Sticks ICE",[personAH1,personAH2,personAH3,personAH4])
team36 = Team("JÚPITER",[personAI1,personAI2,personAI3,personAI4])
team37 = Team("PADIS",[personAJ1])
team38 = Team("Abono Green Peace",[personAK1,personAK2,personAK3,personAK4])
team39 = Team("NUTRIALIVIO",[personAL1,personAL2,personAL3,personAL4])
team40 = Team("IMPORTACION VENTA Y APLICACION DE RECUBRIMIENTOS POLIMERICOS APLICABLES EN INDUSTRIA ",[personAM1,personAM2])
team41 = Team("HOGAR LIMPIO JAM",[personAN1,personAN2,personAN3,personAN4])
team42 = Team("Centro de Flotación Sensory",[personAO1,personAO2])
team43 = Team("Alimentacion saludable y nutritiva del Colca para ti",[personAP1,personAP2])
team44 = Team("HealthyWorld",[personAQ1,personAQ2,personAQ3])
team45 = Team("C.N.E.(Creando un Nuevo Ecosistema)",[personAR1,personAR2,personAR3,personAR4])



teamLibre = Team("Emprendedor",[perEmpre01,perEmpre02,perEmpre03,perEmpre04,perEmpre05,perEmpre06])
teamProfe = Team("Docente",[perDoc01,perDoc02])

#equipo de pruebas
team100 = Team("Equipo JAKU",[personJAKU01,personJAKU02,personJAKU03])

list_teams = []

#for one_list in list_teams:
#    print([(p.name,p.dni,p.cellphone) for p in one_list.list_people if p.came == True])
#    x = lambda x: for p in one_list.list_people: if p.came == True: print(x)
#     print((one_list.list_people).dni) 

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
list_teams.append(teamLibre)
list_teams.append(teamProfe)

#equipo de pruebas
list_teams.append(team100)

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
