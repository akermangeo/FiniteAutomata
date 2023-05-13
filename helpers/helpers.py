from IPython.core.display import SVG
from automata.fa.fa import FA


def get_automaton_display(automaton: FA):
    diagram = automaton.show_diagram()
    img = diagram.create_svg()
    return SVG( data=img )