import datetime
import os


class SystemInfo():
    def __init__(self):
        pass



    @staticmethod
    def get_horas ():
        now = datetime.datetime.now()
        horario = "São {} horas e {} minutos".format(now.hour, now.minute)
        return horario        


    @staticmethod
    def get_dia():
        now = datetime.datetime.now()
        data = "Hoje são {} do {} de {}".format(now.day, now.month, now.year)
        return data

    @staticmethod
    def get_niver():
        niver = 'O aniversário de meu pai é 17 de maio'
        return niver

    @staticmethod
    def get_google():
        google = os.startfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe')

    
    @staticmethod
    def get_vscode():
        vscode = os.startfile(r'C:\Users\SERGIO\AppData\Local\Programs\Microsoft VS Code\Code.exe')