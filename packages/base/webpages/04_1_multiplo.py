# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    def main_root(self,root,**kwargs):
        table = root.table(margin='20px',border_collapse='collapse',width='600px').tbody()
        self.blocco(table.tr(datapath='riga_1'))
        self.blocco(table.tr(datapath='riga_2'))

    
        
        
    def parametri(self,tr):
        fb = tr.td(width='200px').formbuilder()
        fb.textbox(value='^.colore',lbl='Colore')
        fb.textbox(value='^.etichetta',lbl='Etichetta bottone')
        fb.textbox(value='^.messaggio',lbl='Messaggio')
    
    def rettangolo(self,tr):
        box = tr.td(background='^.colore')
        box.button('^.etichetta',action='alert(msg);',msg='=.messaggio',margin='20px')

    def blocco(self,tr):
        self.parametri(tr)
        self.rettangolo(tr)