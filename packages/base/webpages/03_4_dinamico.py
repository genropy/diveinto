# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    def main_root(self,root,**kwargs):
        box = root.div(margin='20px', width='400px', border='1px solid silver')
        self.parametri(box.div(border_bottom='1px solid silver',datapath='primo'))
        self.parametri(box.div(border_bottom='1px solid silver',datapath='secondo'))

        self.rettangoli(box)
        
    def rettangoli(self,pane):
        r1 = pane.div(background='^primo.colore')
        r1.button('^primo.etichetta',action='alert(msg);',msg='=primo.messaggio',margin='20px')
        r2 = pane.div(background='^secondo.colore')
        r2.button('^secondo.etichetta',action='alert(msg);',msg='=primo.messaggio',margin='20px')
        
        
    def parametri(self,pane):
        fb = pane.formbuilder()
        fb.textbox(value='^.colore',lbl='Colore')
        fb.textbox(value='^.etichetta',lbl='Etichetta bottone')
        fb.textbox(value='^.messaggio',lbl='Messaggio')
