#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome',width='20em')
        r.fieldcell('minuti')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')



class Form(BaseComponent):
    def th_form(self,form):
        bc = form.center.borderContainer(datapath='.record')
        self.dati_ricetta(bc.contentPane(region='top'))
        self.ingredienti(bc.contentPane(region='center'))

    def dati_ricetta(self,pane):
        fb = pane.formbuilder(cols=2)
        fb.textbox(value='^.nome',lbl='Nome ricetta')
        fb.numberTextbox(value='^.minuti',lbl='Minuti',width='4em')

    def ingredienti(self,pane):
        grid = pane.quickGrid('^.ingredienti',height='200px',border='1px solid silver')
        grid.tools('delrow,addrow',title='Lista ingredienti')
        grid.column('ingrediente',edit=True,name='Ingrediente',width='100%')
        grid.column('quantita',edit=True,name='Qt',width='5em',dtype='N')


    

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
