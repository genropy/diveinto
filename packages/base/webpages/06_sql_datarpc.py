# -*- coding: utf-8 -*-
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        box = root.div(width='400px',datapath='ricette')
        for i in range(2):
            self.ricetta(box.div(datapath=f'.riga_{i}',margin='10px'))

    def dati_ricetta(self,pane):
        fb = pane.formbuilder(cols=2)
        fb.textbox(value='^.record.nome',lbl='Nome ricetta')
        fb.numberTextbox(value='^.record.minuti',lbl='Minuti',width='4em')
        fb.button('Salva ricetta',fire='.salva')
        pane.dataRpc(None,self.salvaRicetta,dati_ricetta='=.record',
                    _fired='^.salva',_onResult='alert("Salvata")')
                    
        pane.dataRpc('.record',self.caricaRicetta,
                    nome_ricetta='^.record.nome',
                    _userChanges=True)

    def ingredienti(self,pane):
        grid = pane.quickGrid('^.record.ingredienti',height='200px',border='1px solid silver')
        grid.tools('delrow,addrow',title='Lista ingredienti')
        grid.column('ingrediente',edit=True,name='Ingrediente',width='100%')
        grid.column('quantita',edit=True,name='Qt',width='5em',dtype='N')

    def ricetta(self,pane):
        self.dati_ricetta(pane)
        self.ingredienti(pane)
    
    @public_method
    def salvaRicetta(self,dati_ricetta=None,**kwargs):
        self.db.table('base.ricetta').insert(dati_ricetta)
        self.db.commit()

    @public_method
    def caricaRicetta(self,nome_ricetta=None,**kwargs):
        result = self.db.table('base.ricetta').record(nome=nome_ricetta,ignoreMissing=True).output('record')
        return result or Bag(dict(nome=nome_ricetta))
