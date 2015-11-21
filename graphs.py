import graphlab as gl

from graphlab import SFrame, SGraph, Vertex, Edge
edge_data = SFrame.read_csv(
    'http://s3.amazonaws.com/dato-datasets/bond/bond_edges.csv')

g = SGraph()
g = g.add_edges(edge_data, src_field='src', dst_field='dst')
print g

g.save('james_bond')
new_graph = gl.load_sgraph('james_bond')

g.show(vlabel='id', highlight=['James Bond', 'Moneypenny'], arrows=True)
