
import pygame 
import csv
import os
from teams import *
import pandas as pd
from time import gmtime, strftime
from openpyxl import Workbook

date = strftime("%Y-%m-%d", gmtime())
file_csv = "Registro CSV " 
file_csv = file_csv + date +".csv"


def listToString(s):  
    str1 = ""
    for sub_s in s:
        str1 = str1 +''.join((str(e)+" ") for e in sub_s) 
        str1 = str1 + " | "    
    return str1

#print(list_teams)
def change_assistance(var,list_teams):
    str(var)
    for one_list in list_teams:
        ##if one_list.assistance == 'NO':
        if one_list.find_DNI(var):
            one_list.change_assistance()
            one_list.change_date()
            return True
    return False
def change_endTime(var,list_teams):
    var = str(var)
    for one_list in list_teams:
            if one_list.find_DNI(var):
                one_list.change_endT()
                return True
    return False
def write_assitance(list_teams,file_csv):
    
    with open(file_csv, 'w', newline='') as file:
                    fieldnames = ['Nombre del emprendimiento', 'Asistencia','Integrantes presentes DNI Telefono','Dia','Hora Entrada']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    #people = ""
                    for one_list in list_teams:
                        writer.writerow({'Nombre del emprendimiento': one_list.name, 
                                            'Asistencia': one_list.assistance,
                                            'Integrantes presentes DNI Telefono':listToString([(p.name,p.dni,p.cellphone) for p in one_list.list_people if p.came == True]),#people,
                                            #'Integrantes presentes DNI Telefono':listToString([(p.name,p.dni,p.cellphone) for p in one_list.list_people if p.came == True]),#people,
                                            #'Integrantes presentes DNI Telefono':one_list.list_peole[0].name,
                                            'Dia':one_list.date,
                                            'Hora Entrada':one_list.startTime,
                                            })

def write_assitance2_0(list_teams,file_csv):
    
    with open(file_csv, 'w', newline='') as file:
                    fieldnames = ['Emprendimiento','Integrante: Apellidos & Nombres','DNI','Celular','Dia','Hora Entrada','Hora Salida','Firma']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    #people = ""
                    for one_list in list_teams:
                        #list_p = one_list.list_people
                        for p in one_list.list_people:
                            if p.came == True:
                                writer.writerow({'Emprendimiento': one_list.name, 
                                                    #'Asistencia': one_list.assistance,
                                                    'Integrante':p.name,
                                                    'DNI':p.dni,
                                                    'Celular':p.cellphone,
                                                    'Dia':one_list.date,
                                                    'Hora Entrada':one_list.startTime,
                                                    'Hora Salida':one_list.endTime,
                                                    'Firma':" ",
                                                    })


#GUI

pygame.init()
screen = pygame.display.set_mode((900, 600))
COLOR_INACTIVE = pygame.Color('black')
COLOR_ACTIVE = pygame.Color('blue')
font_path = "Fipps-Regular.otf"
FONT = pygame.font.Font(font_path, 32)


class InputBox: 
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.message = ""
        self.showPerson = ""


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    temp = self.text
                    if change_assistance(temp,list_teams):
                        self.message = "REGISTRADO"
                    else:
                        self.message="DESCONOCIDO"
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)
    def handle_event_end(self, event):## function for endtime
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    temp = self.text
                    if change_endTime(temp,list_teams):
                        self.message = "Listo"
                    else:
                        self.message="No existe"
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

def main():
    #write_alldata(list_teams)
    clock = pygame.time.Clock()
    #print(clock)
    input_box_assistance = InputBox(400, 300, 800, 50)
    input_box_exit = InputBox(400, 400, 800, 50)
    #input_boxes = [input_box_assistance]
    done = False
    unsa_image = pygame.image.load("Imagenes_logos/unsa.png")
    jaku_image = pygame.image.load("Imagenes_logos/JAKU_full_color.png")
    unsa_image = pygame.transform.scale(unsa_image, (250, 100))
    jaku_image = pygame.transform.scale(jaku_image, (250, 100))
    text = "Control de Asistencia PEM"
    entrada = "Entrada :"
    salida = "Salida :"
    fuente = pygame.font.Font(None, 85)
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #for box in input_boxes:
            #    box.handle_event(event)
            input_box_assistance.handle_event(event)
            input_box_exit.handle_event_end(event)

        #for box in input_boxes:
        #    box.update()
        input_box_assistance.update()
        input_box_exit.update()

        screen.fill((200, 200, 200))

        screen.blit(unsa_image,(50,50))
        screen.blit(jaku_image,(600,50))
        #for box in input_boxes:
        #    box.draw(screen)
        input_box_assistance.draw(screen)
        input_box_exit.draw(screen)
        
        mensaje = fuente.render(text, 2, (0, 0, 0))
        mensaje_E = fuente.render(entrada, 2, (0, 0, 0))
        mensaje_S = fuente.render(salida, 2, (0, 0, 0))
        if input_box_assistance.message == "REGISTRADO":
            verificacion = fuente.render(input_box_assistance.message,4,(0,0,255))
        else:
            verificacion = fuente.render(input_box_assistance.message,4,(255,0,0))
        if input_box_exit.message == "Listo":
            verificacion2 = fuente.render(input_box_exit.message,4,(0,255,0))
        else:
            verificacion2 = fuente.render(input_box_exit.message,4,(255,0,0))
        screen.blit(verificacion2,(620,400))
        screen.blit(verificacion, (250, 500))
        screen.blit(mensaje, (100, 200))
        screen.blit(mensaje_E, (100, 300))
        screen.blit(mensaje_S, (100, 400))
        pygame.display.flip()
        clock.tick(60)
        write_assitance2_0(list_teams,file_csv)

if __name__ == '__main__':
    main()
    workbook = Workbook()
    worksheet = workbook.active
    with open(file_csv, 'r') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                for idx, val in enumerate(col.split(',')):
                    cell = worksheet.cell(row=r+1, column=c+1)
                    cell.value = val
    excel = "Registro EXCEL "+strftime("%Y-%m-%d", gmtime())+".xlsx"
    workbook.save(excel)
    pygame.quit()
