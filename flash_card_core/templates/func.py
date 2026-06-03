import math
import time
from pyscript import document
#ADDINGF TO AN LIST IN ORDER TO CREATE ELEMENET FOR STUDYING
def add_to_flash(x):
    mlist = []
    elinp = document.querySelector("#item_input")
    user = elinp.value

    if user.strip() != "":
        mlist.append(user)

        elinp.value = ""
        out ="<ul>"
        for i in mlist:
            our += f"<li>{i}</li>"
        out += "</ul>"
        document.querySelector("#out").inerHTML = out





def counter():
    pass


def check_rigth():
    pass

def agian():
    pass

def values():
    pass


