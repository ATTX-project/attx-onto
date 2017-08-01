import ontospy
from ontodocs.viz.viz_html_multi import KompleteViz
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

g = ontospy.Ontospy("attx-onto_v2.0.owl")

v = KompleteViz(g, theme="paper")  # => instantiate the visualization object
v.build(dir_path+"/new")  # => render visualization. You can pass an 'output_path' parameter too
# v.preview()  # => open in browser
