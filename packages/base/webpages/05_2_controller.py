# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    def main_root(self,root,**kwargs):
        table = root.table(margin='20px',border_collapse='collapse',width='600px').tbody()
        for i in range(2):
            self.blocco(table.tr(datapath=f'riga_{i}'))

    def parametri(self,tr):
        fb = tr.td(width='200px').formbuilder()
        fb.textbox(value='^.colore',lbl='Colore')
        fb.textbox(value='^.etichetta',lbl='Etichetta bottone',default='Click')
        fb.horizontalSlider(value='^.size',lbl='FontSize bottone',
                            width='16em',min=3,max=30,default=11,
                            intermediateChanges=True)
        fb.dataFormula('.font_size',"size+'px'",size='^.size')
        fb.textbox(value='^.messaggio',lbl='Messaggio')
    
    def rettangolo(self,tr):
        box = tr.td(background='^.colore')
        box.button('^.etichetta',action='alert(msg);',font_size='^.font_size',msg='=.messaggio',margin='20px')

    def blocco(self,tr):
        self.parametri(tr)
        self.rettangolo(tr)