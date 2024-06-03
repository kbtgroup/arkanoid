# Arkanoid in Python

Questo è un semplice gioco di Arkanoid realizzato in Python utilizzando la libreria Pygame. Al primo livello, i mattoni formano la scritta "Simone Teodori" e ogni "pixel" della scritta è un mattone che può essere distrutto dalla pallina.

## Funzionalità

- **Livelli**: Il primo livello contiene la scritta "Simone Teodori" formata da mattoni. Ulteriori livelli possono essere aggiunti facilmente.
- **Punteggio**: Un contatore del punteggio in alto a destra che aumenta ogni volta che un mattone viene distrutto.
- **Game Over**: Quando la pallina non viene presa dalla barra e tocca la parte inferiore dello schermo, il gioco si ferma e mostra "Game Over!". Per riprendere, l'utente deve premere "Invio".
- **Oggetti speciali**: Colpendo i mattoni, c'è una probabilità del 30% che cada un oggetto speciale che può aumentare la vita, allungare il paddle o togliere una vita.

## Requisiti

- Python 3.x
- Pygame

## Installazione

1. Clona il repository:
   ```sh
   git clone https://github.com/kbtgroup/arkanoid.git
   Naviga nella directory del progetto:

sh

cd arkanoid-python
Installa le dipendenze:

sh

pip install pygame
Esecuzione
Esegui lo script principale:

sh

python arkanoid.py
Controlli
Muovi il paddle a sinistra: Freccia sinistra
Muovi il paddle a destra: Freccia destra
Riprendi il gioco dopo il Game Over: Invio
Struttura del Codice
arkanoid.py: Contiene il codice principale del gioco.
Screenshot

Autore
Simone Teodori
Licenza
Questo progetto è rilasciato sotto la licenza MIT. Per ulteriori dettagli, consulta il file LICENSE.

Questo README fornisce una descrizione completa del progetto, includendo le funzionalità, i requisiti, le istruzioni per l'installazione e l'esecuzione, e le informazioni sull'autore e sulla licenza.
