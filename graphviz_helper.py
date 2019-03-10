# def render_table(variable, values, grids):
def render_table(players, types, beliefs, strategies, payoffs):

    span = 1
    prefix = '<<FONT POINT-SIZE="7"><TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD COLSPAN="' + str(span) +'">' + 'xyz' + '</TD></TR>'
    header = "<TR><TD></TD>"
    body = ""

    # for ll, label in values['legend'].items():
    #     header = header + '<TD>'  + label + ' (' + variable.lower() + '_' + str(ll)  + ')</TD>'
    header = header + '</TR>'


    # loop_row = len(grids)
    # loop_col = len(grids[0])
    # body = ""

    # if loop_row > 1:
    #     for row in range(loop_row):
    #         body = body + "<TR>"
    #         for col in range(loop_col):
    #             body = body + "<TD>" + str(grids[row][col]) + "</TD>"
    #         body = body + "</TR>"
    #
    # else:
    #     body = "<TR><TD>" + str(variable).lower() + "</TD>"
    #     for col in range(loop_col-1):
    #         body = body + '<TD>' + str(grids[0][col+1]) + '</TD>'
    #     body = body + "</TR>"

    footer = '</TABLE></FONT>>'
    return prefix + header + body + footer


def render_game(players, types, beliefs, strategies, payoffs):
    try:
        from graphviz import Graph
    except:
        print("Python Dependency: pip install graphviz")
        print("Graphviz also needs to be installed on the host: brew install graphviz")

    h = Graph('html_table')
    table = render_table(players, types, beliefs, strategies, payoffs)
    h.node('tab', label=table)

    return h
