# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    def main_root(self,root,**kwargs):
        box = root.div(margin='20px', width='400px', border='1px solid silver')
        r1 = box.div(background='pink')
        r1.button('Click me',action='alert("Hello");',margin='20px')
        r2 = box.div(background='lime')
        r2.button('Do not click me',action='alert("Ouch");',margin='20px')
        