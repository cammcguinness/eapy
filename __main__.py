from examples.basicstring.Tournament import Tournament
from examples.basicstring.StringMember import StringMember
from eapy.EA import EA
selection = Tournament()
selection.setSize(4)

ea = EA(selection, StringMember,100)
ea.run(500)


