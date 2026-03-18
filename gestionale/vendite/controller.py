import ft

from gestionale.gestoreOrdini import GestoreOrdini


class Controller:
    def __init__(self, v):
        self._view = v
        self._model = GestoreOrdini()
    def add_ordine(self, e): #!!I METODI ASSOCIATI AI PULSANTI HANNO SEMPRE COME ARGOMENTO IL SELF E ANCHE "E" DI EVENTO
        #INSERISCO I DATI DELL'ORDINE

        #DATI PRODOTTO
        nomeProdotto = self._view.txtInNomeP.value
        try:
            prezzoProdotto = float(self._view.txtInPrezzo.value)
        except ValueError:
            self._view.lvOut.controls.append(ft.Text("Attenzione! il prezzo deve essere un numero"), color = "red")
            self._view.update_page()
            return
        try:
            quantità = int(self._view.txtInQuantità.value)
        except ValueError:
            self._view.lvOut.controls.append(ft.Text("Attenzione! la quantità deve essere un numero"), color="red")
            self._view.update_page()
            return

        #DATI CLIENTE
        nomeC = self._view.txtNomeC.value
        mailC = self._view.txtMailC.value
        categoriaC = self._view.txtCategoriaC.value

        #ORDINE
        ordine = self._model.crea_ordine(nomeProdotto, prezzoProdotto, quantità, nomeC,mailC,categoriaC)

        self._model.add_ordine(ordine)



    def gestisci_ordine(self, e):
        pass

    def gestisci_all_ordini(self, e):
        pass

    def stampa_sommario(self, e):
        pass
