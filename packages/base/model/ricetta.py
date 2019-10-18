# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('ricetta', pkey='nome', name_long='Ricetta')
        tbl.column('nome',name_long='Nome',unique=True)
        tbl.column('minuti',dtype='L',name_long='Minuti')
        tbl.column('ingredienti',dtype='X',name_long='Ingredienti') #campo bag