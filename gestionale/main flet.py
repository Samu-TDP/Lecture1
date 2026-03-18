import flet as ft

from gestionale.vendite.controller import Controller
from gestionale.vendite.view import View


def main(page: ft.Page):
    #devo far parlare View e Controller
    v = View(page)#quando il view si costruisce saprà in che pagina costruirsi
    c = Controller(v)
    v.set_controller(c)#Qua vi è il collegamento tra controller e view
    v.caric_interfaccia()

ft.app(target = main)