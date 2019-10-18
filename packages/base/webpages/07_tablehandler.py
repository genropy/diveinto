# -*- coding: utf-8 -*-
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    py_requires='th/th:TableHandler'
    def main(self,root,**kwargs):
        root.stackTableHandler(table='base.ricetta',datapath='ricette',
                                view_store_onStart=True)