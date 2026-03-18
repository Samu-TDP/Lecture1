

import flet as ft
import ft


class View:
    def __init__(self, page):
        self._page = page
        self._controller = None
        self._page.title = "TdP 2026 - Software Gestionale"
        self._page.horizontal_alignment = "CENTER"#centra il testo rispetto alla mezzeria
        self._page.theme_mode = ft.ThemeMode.LIGHT

    def caric_interfaccia(self):#Ciò che vedrò nella pagina di interfaccia grafica
        #CREO RIGA 1 CON I DATI DEL PRODOTTO
        #!!TEXT FIELD CREA NELLA GUI UNA CASELLA DI TESTO IN CUI AL SUO INTERNO SI PUO SCRIVERE TESTO, Inserisci dell'input
        self._txtInNomeP = ft.TextField(label="Nome Prodotto", width=200)
        self._txtInPrezzo = ft.TextField(label="Prezzo", width=200)
        self._txtInQuantità = ft.TextField(label = "Quantità", width=200)
        row1 = ft.Row(controls = [self._txtInNomeP, self._txtInPrezzo, self._txtInQuantità], alignment= ft.MainAxisAlignment.CENTER)
        self._page.add(row1)#aggiungo la riga all'interfaccia grafica

        #CREO RIGA 2 CON I DATI DEL CLIENTE
        self._txtInNomeC =ft.TextField(label="Nome Cliente", width=200)
        self._txtInMail = ft.TextField(label="Mail", width=200)
        self._txtInCategoria = ft.TextField(label="Categoria", width=200)
        row2 = ft.Row(controls=[self._txtInNomeC, self._txtInMail, self._txtInCategoria],alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)  # aggiungo la riga all'interfaccia grafica

        #CREO I BOTTONI: CIOE I TASTI CLICCABILI NELL'INTERFACCIA GRAFICA
        self._btnAddOrdine = ft.ElevatedButton(text = "Aggiungi ordine", on_click = self._controller.add_ordine, width = 200) #aggiungero SOLO IL NOME del metodo del controller per la funzione on-click)
        self._btnGestisciOrdine = ft.ElevatedButton(text = "Gestisci Prossimo Ordine", on_click = self._controller.gestisci_ordine, width = 200)
        self._btnGestisciallOrdini = ft.ElevatedButton(text = "Gestisci tutti gli Ordini", on_click = self._controller.gestisci_all_ordini, width = 200)
        self._btnStampaInfo = ft.ElevatedButton(text = "Stampa Sommario", on_click = self._controller.stampa_sommario, width = 200)
        row3 = ft.Row(controls= [self._btnAddOrdine, self._btnGestisciOrdine, self._btnGestisciallOrdini, self._btnStampaInfo], alignment=ft.MainAxisAlignment.CENTER )

        #ORA SCRIVO LA CASELLA DI TESTO CHE VEDRO NELL'INTERFACCIA GRAFICA IN CUI VEDRO' L'OUTPUT
        self._lvOut = ft.ListView(expand=True)
        self._page.add(row3)
        self._page.add(self._lvOut)

    def set_controller(self, c):
        self._controller = c

    def update_page(self):
        self._page.update()#permettere di scrivere sull'interfaccia grafica