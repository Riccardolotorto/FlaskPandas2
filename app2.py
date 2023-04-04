from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
dati_regioni = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv')
    
@app.route('/')
def home():
    nomi_regioni = dati_regioni.drop_duplicates(subset=['denominazione_regione'])   #drop_duplicates: elimina i duplicati da una DataFrame
    return render_template('ricercaSelect.html', list= list(nomi_regioni['denominazione_regione'])) #creo una lista che contiene i nomi delle regioni

@app.route('/search', methods = ['GET'])
def search():
    regione = request.args['regione']
    risultato = dati_regioni[dati_regioni['denominazione_regione']==regione.capitalize()]   
    if len(risultato) == 0:
        table = 'Regione non trovata'
    else:
        table = risultato.to_html()   #to_html(): trasforma il dataframe di pandas in una tabella di html
    return render_template('tabella.html', tabella = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)