# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    def main_root(self,root,**kwargs):
        box = root.div(margin='20px', width='400px', border='1px solid silver')
        self.parametri(box.div(border_bottom='1px solid silver'))
        self.rettangoli(box)
        
    def rettangoli(self,pane):
        r1 = pane.div(background='^primo_colore')
        r1.button('^primo_etichetta',action='alert("Hello");',margin='20px')
        r2 = pane.div(background='lime')
        r2.button('Do not click me',action='alert("Ouch");',margin='20px')
        
        
    def parametri(self,pane):
        fb = pane.formbuilder()
        fb.textbox(value='^primo_colore',lbl='Primo colore')
        fb.textbox(value='^primo_etichetta',lbl='Etichetta primo bottone')
