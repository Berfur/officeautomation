# Script Espanso per l'Office Automation

Ho scritto questi script per sollevarmi dal peso di compiti monotoni e ripetitivi.
Il suo utilizzo è molto semplice, si accoppia un trigger (solitamente una formula di testo breve) a un testo più lungo e e quando si digita il trigger questa viene espansa automaticamente.

Per esempio:

.bf -> "Buongiorno sig.ra,"  
.cell -> "555 876523"

Il programma è semplice e gli script possono diventare più complessi, creando anche semplici GUI.
Cosa ancora più importante: funziona in ogni area di testo: **programmi**, **web**, **gadget**. È universale (attenzione alle note in fondo).

![Esempio](./sampletxt.gif)

per chi ama le GUI invece:

![Esempio](./sampleGUI.gif)

## Installazione e dipendenze
1. Hai bisogno di [Espanso](https://espanso.org). Io uso la versione portatile, quindi molto semplice su Windows. Decomprimi l'archivio e segui le istruzioni per avere il sistema attivo e funzionante. Su Linux utilizzo uno snap ("snap install Espanso"), ma magari c'è già il pacchetto rpm o apt per il tuo sistema.
2. Scarica gli script che ti interessano (ricorda che alcuni script dipendono da altri script, ad esempio la maggior parte dipende dal file "variable.yml") e inseriscili nella directory "match" all'interno dell'installazione di Espanso.
3. Personalizza il file "variable.yml" con i tuoi dati (altrimenti ti verrà fuori il mio nome in molte scorciatorie di testo :) )
* FACOLTATIVO: le scorciatoie .bf e .bm dipendono da un'installazione Python utilizzabile. Se li vuoi devi installare Python.

## Casi d'uso

Utilizzo questi script per comporre testi: e-mail, profili, testi professionali e quasi tutto ciò che necessita di template (utile anche quando scrivi documenti Pandoc e formule Excel).
È utile anche quando solitamente scrivi cose che non ricordi, ad esempio la pagina carriere della tua azienda (se devi inviarla via whatsapp, email, LinkedIn è più facile scrivere ".carpage" che "https:// mydomain/work/carreers/" ed è meno soggetto a errori.

Lavoro con Word, Outlook e (qualsiasi altro programma) ma la verità è che è molto dispendioso in termini di tempo impostare un set completo di modelli per ogni programma (con la propria sintassi e peculiarità). Trovo questo sistema migliore perché hai tutto a portata di mano. E tutto quello che devi fare per averlo pronto è copiare alcuni file. Imbattibile.

### Cosa posso trovare qui pronto per l'uso:

Per avere un help completo, ti basta aprire un editor di testo (notepad, word, quello che vuoi) e digitare ".help". Ti fornirà una lista dettagliata. In sintesi:

* autocorrezioni (scorciatoie per avere la vocale È accentata maiuscola, caratteri speciali, guarda il file per espandere)
* varie tipologie di auguri per avviare email (due si adattano automaticamente all'ora del giorno: Buongiorno/Buonasera, se hai installato anche Python)
* markdown (alcune scorciatoie utili, sopratutto boylerplate per tabelle e headers)
* maschere: alcune GUI utili per scrivere email a candidati e clienti
* alcuni template per chi lavora nella Ricerca e Selezione


# Il potere dell'automazione e dei modelli

*Il templating* è una strategia semplice per creare modelli di informazioni. È principalmente un compito intellettuale e molto personale. Alcuni modelli possono essere presi in prestito, ma non è possibile utilizzarli senza capirli. Ad esempio, puoi copiare un modello markdown o todo.txt. Ma non puoi usarli se non conosci la sintassi markdown o il sistema todo.txt.
*Automazione* è la pratica di svolgere un compito ripetitivo (ad esempio, fornire il modello corretto) nel modo più semplice possibile. Non importa se automatizzi elettronicamente, meccanicamente, umanamente o informaticamente. Fai come preferisci, nel modo migliore per te.

Lavoro principalmente in ambiente d'ufficio (Windows, posta elettronica, elaborazione testi, ecc.). Ho *molte* attività ripetitive, quindi cerco di automatizzare la maggior parte delle attività più banali e a basso valore aggiunto senza perdere di qualità e di tocco personale.

## Modelli vecchi e nuovi
Se lavori molto con i computer capisci quanto sia utile avere modelli per qualsiasi cosa coinvolga la scrittura. Programmazione (scheletri o frammenti) o elaborazione testi. Un modello è una cosa molto utile da configurare.
Il problema è che, come ho affermato prima, devi configurarlo ogni volta che cambi sistema (Word; ambiente di programmazione e così via). Perché ogni strumento ha il proprio sistema di gestione dei modelli a volte diventa una fatica inutile.

Espanso invece ti consente di sfruttare la potenza dei modelli di testo in ogni ambiente, e con tutta la portabilità di una cartellina di file txt.

##Riconoscimenti Dovuti
La maggior parte del lavoro è eseguita da [Espanso](https://espanso.org/), una meravigliosa applicazione multipiattaforma per l'espansione del testo di [Federico Terzi](https://federicoterzi.com/).
Espanso ha il vantaggio di non essere vincolato a *una* piattaforma (Lo uso sia su Windows che Linux). Funziona in: Word; Excel; browsers come Chrome, Firefox, Edge; Shell; ovunque sia possibile digitare.
Una parte dei miei script viene eseguita tramite Python (Espanso non dispone di flussi condizionali), ma sono molto banali. Potrebbe essere usato molto meglio, sentiti libero di cambiare tutto ciò che vuoi e per favore condividi.

# I problemi
A volte i trigger non funzionano se scrivi all'inizio del campo di testo.
Questo è vero ad esempio per Outlook, se inizi la mail con un trigger non funziona. Basta aggiungere uno spazio all'inizio e il gioco è fatto.
Spesso infatti non inizio con ".bm" ma " .bm"

