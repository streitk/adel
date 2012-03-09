
# This file has been generated at Fri Mar  9 11:40:15 2012

from openalea.core import *


__name__ = 'alinea.adel.leaf'

__editable__ = True
__description__ = 'Leaf functions (PMA 2012)'
__license__ = ''
__url__ = ''
__alias__ = []
__version__ = '1.0'
__authors__ = 'C. Pradal, C.Fournier'
__institutes__ = 'INRA, CIRAD, INRIA'
__icon__ = ''


__all__ = ['curve_dicretizer_curve_discretizer', '_66071632', '_65976528', 'stress_sr_stress_sr', 'curve_dicretizer_points2curve']



curve_dicretizer_curve_discretizer = Factory(name='curve discretizer',
                authors='C. Pradal, C.Fournier (wralea authors)',
                description='Discretize a 2D curve into a polyline',
                category='geometry',
                nodemodule='curve_dicretizer',
                nodeclass='curve_discretizer',
                inputs=[{'interface': None, 'name': 'curve', 'value': None, 'desc': ''}, {'interface': IInt, 'name': 'n', 'value': 15, 'desc': ''}],
                outputs=[{'interface': ISequence, 'name': 'x', 'desc': ''}, {'interface': ISequence, 'name': 'y', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




_66071632 = CompositeNodeFactory(name='1. animated leaf',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('vplants.plantgl.edition', 'Curve2D'),
   3: ('vplants.plantgl.edition', 'Curve2D'),
   4: ('alinea.adel.fitting', 'fit'),
   5: ('alinea.adel.leaf', 'curve discretizer'),
   6: ('alinea.adel.leaf', 'curve discretizer'),
   7: ('alinea.adel.geometry', 'leaf to mesh'),
   8: ('vplants.plantgl.visualization', 'plot3D'),
   9: ('vplants.plantgl.objects', 'Shape'),
   10: ('vplants.plantgl.objects', 'Material'),
   11: ('openalea.data structure', 'int'),
   12: ('openalea.flow control', 'iter'),
   13: ('openalea.numpy.creation', 'linspace'),
   14: ('openalea.data structure', 'int'),
   15: ('openalea.color', 'color')},
                             elt_connections={  39720696: (11, 0, 4, 4),
   39720720: (14, 0, 7, 1),
   39720744: (2, 0, 6, 0),
   39720768: (4, 0, 7, 0),
   39720792: (15, 0, 10, 1),
   39720816: (13, 0, 12, 0),
   39720840: (6, 1, 4, 1),
   39720864: (5, 1, 4, 3),
   39720888: (6, 0, 4, 0),
   39720912: (9, 0, 8, 0),
   39720936: (12, 0, 7, 2),
   39720960: (7, 0, 9, 2),
   39720984: (14, 0, 13, 1),
   39721008: (10, 0, 9, 1),
   39721032: (5, 0, 4, 2),
   39721056: (3, 0, 5, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'Curve2D',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x704e6d0> : "Curve2D"',
         'hide': True,
         'id': 2,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -17.925846797545866,
         'posy': -44.73407182461934,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'Curve2D',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x704e6d0> : "Curve2D"',
         'hide': True,
         'id': 3,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': 64.01232902005644,
         'posy': -46.654637961859756,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': 'fit',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x7f7d190> : "fit"',
         'hide': True,
         'id': 4,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 29.065398359836543,
         'posy': 50.424062306080046,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': 'sr',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x59f1e10> : "curve discretizer"',
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 50.10669582883208,
         'posy': -6.994362639335627,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': 'xy',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x59f1e10> : "curve discretizer"',
         'hide': True,
         'id': 6,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -25.15165670621674,
         'posy': -1.6994362639335634,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   7: {  'block': False,
         'caption': 'leaf to mesh',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x7a34450> : "leaf to mesh"',
         'hide': True,
         'id': 7,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 36.121197545354434,
         'posy': 83.72137836350781,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   8: {  'block': False,
         'caption': 'plot3D',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x68d1ad0> : "plot3D"',
         'hide': True,
         'id': 8,
         'lazy': False,
         'minimal': False,
         'port_hide_changed': set(),
         'posx': 56.55748969660428,
         'posy': 166.38440953899993,
         'priority': 0,
         'use_user_color': False,
         'user_application': False,
         'user_color': None},
   9: {  'block': False,
         'caption': 'Shape',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x7a15290> : "Shape"',
         'hide': True,
         'id': 9,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 50.40056801719055,
         'posy': 125.75725350872702,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   10: {  'block': False,
          'caption': 'Material',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x7a14850> : "Material"',
          'hide': True,
          'id': 10,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -66.6005367473584,
          'posy': 77.14974380365686,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   11: {  'block': False,
          'caption': '18',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x5d12d90> : "int"',
          'hide': True,
          'id': 11,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 153.1168456308165,
          'posy': -3.3775162564883665,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   12: {  'block': False,
          'caption': 'iter',
          'delay': 1,
          'factory': '<openalea.core.node.NodeFactory object at 0x855a7d0> : "iter"',
          'hide': True,
          'id': 12,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 231.75515248517,
          'posy': 63.39954790315112,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   13: {  'block': False,
          'caption': 'linear space',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x5b7ca50> : "linspace"',
          'hide': True,
          'id': 13,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 210.17510115613732,
          'posy': 28.466337745031126,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   14: {  'block': False,
          'caption': '10',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x5d12d90> : "int"',
          'hide': True,
          'id': 14,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 230.45989505798838,
          'posy': -31.762100921453527,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   15: {  'block': False,
          'caption': ' ',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x5699350> : "color"',
          'hide': True,
          'id': 15,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -53.89352859780767,
          'posy': 36.22219959794419,
          'priority': 0,
          'use_user_color': True,
          'user_application': None,
          'user_color': 14},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [  (0, 'None'),
         (  1,
            "'copenalea.plantgl.scenegraph._pglsg\\nPoint3Array\\np1\\n((lp2\\ncopenalea.plantgl.math._pglmath\\nVector3\\np3\\n(F0.010374363511800766\\nF0.023077333346009254\\nF1\\ntRp4\\nag3\\n(F0.80732631683349609\\nF0.31614789366722107\\nF1\\ntRp5\\nag3\\n(F0.23109914362430573\\nF0.87061011791229248\\nF1\\ntRp6\\nag3\\n(F0.92518693208694458\\nF0.84084248542785645\\nF1\\ntRp7\\nag3\\n(F0.90239661931991577\\nF0.60353833436965942\\nF1\\ntRp8\\nag3\\n(F0.62708628177642822\\nF0.48039713501930237\\nF1\\ntRp9\\nag3\\n(F0.55964523553848267\\nF0.721515953540802\\nF1\\ntRp10\\natRp11\\n.'")],
   3: [  (  0,
            'NurbsCurve2D(Point3Array([Vector3(-0.00110079,0.696903,1),Vector3(0.0956529,0.807176,1),Vector3(0.233191,0.881227,1),Vector3(0.413802,0.847923,1),Vector3(0.734068,0.688942,1),Vector3(0.91814,0.570216,1),Vector3(0.998286,0.313748,1),Vector3(1,0,1)]), width = 2)'),
         (  1,
            "'copenalea.plantgl.scenegraph._pglsg\\nPoint3Array\\np1\\n((lp2\\ncopenalea.plantgl.math._pglmath\\nVector3\\np3\\n(F-0.0011007854482159019\\nF0.69690322875976562\\nF1\\ntRp4\\nag3\\n(F0.095652863383293152\\nF0.80717611312866211\\nF1\\ntRp5\\nag3\\n(F0.23319114744663239\\nF0.88122701644897461\\nF1\\ntRp6\\nag3\\n(F0.4138018786907196\\nF0.84792298078536987\\nF1\\ntRp7\\nag3\\n(F0.73406821489334106\\nF0.68894219398498535\\nF1\\ntRp8\\nag3\\n(F0.91814041137695312\\nF0.57021600008010864\\nF1\\ntRp9\\nag3\\n(F0.99828648567199707\\nF0.31374838948249817\\nF1\\ntRp10\\nag3\\n(F1\\nF0\\nF1\\ntRp11\\natRp12\\n.'")],
   4: [],
   5: [(1, '15')],
   6: [(1, '15')],
   7: [(3, '1.0')],
   8: [],
   9: [(0, "''"), (3, '138269408'), (4, '4294967295')],
   10: [  (0, "''"),
          (2, '2.0'),
          (3, 'Color3(0,0,0)'),
          (4, '1.0'),
          (5, '(0, 0, 0)'),
          (6, '0.0')],
   11: [(0, '18')],
   12: [],
   13: [(0, '1.0'), (2, '100.0'), (3, 'True'), (4, 'True')],
   14: [(0, '10')],
   15: [(0, '(14, 94, 5)')],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {  'position': [-17.925846797545866, -44.73407182461934],
         'useUserColor': False,
         'userColor': None},
   3: {  'position': [64.01232902005644, -46.654637961859756],
         'useUserColor': False,
         'userColor': None},
   4: {  'position': [29.065398359836543, 50.424062306080046],
         'useUserColor': False,
         'userColor': None},
   5: {  'position': [50.10669582883208, -6.994362639335627],
         'useUserColor': False,
         'userColor': None},
   6: {  'position': [-25.15165670621674, -1.6994362639335634],
         'useUserColor': False,
         'userColor': None},
   7: {  'position': [36.121197545354434, 83.72137836350781],
         'useUserColor': False,
         'userColor': None},
   8: {  'position': [56.55748969660428, 166.38440953899993],
         'useUserColor': False,
         'userColor': None},
   9: {  'position': [50.40056801719055, 125.75725350872702],
         'useUserColor': False,
         'userColor': None},
   10: {  'position': [-66.6005367473584, 77.14974380365686],
          'useUserColor': False,
          'userColor': None},
   11: {  'position': [153.1168456308165, -3.3775162564883665],
          'useUserColor': False,
          'userColor': None},
   12: {  'position': [231.75515248517, 63.39954790315112],
          'useUserColor': False,
          'userColor': None},
   13: {  'position': [210.17510115613732, 28.466337745031126],
          'useUserColor': False,
          'userColor': None},
   14: {  'position': [230.45989505798838, -31.762100921453527],
          'useUserColor': False,
          'userColor': None},
   15: {  'position': [-53.89352859780767, 36.22219959794419],
          'useUserColor': True,
          'userColor': [14, 94, 5]},
   '__in__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None},
   '__out__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None}},
                             lazy=True,
                             eval_algo='DiscreteTimeEvaluation',
                             )




_65976528 = CompositeNodeFactory(name='2. leaf with stress sr',
                             description='',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('vplants.plantgl.edition', 'Curve2D'),
   3: ('vplants.plantgl.edition', 'Curve2D'),
   4: ('alinea.adel.fitting', 'fit'),
   5: ('alinea.adel.leaf', 'curve discretizer'),
   6: ('alinea.adel.leaf', 'curve discretizer'),
   7: ('alinea.adel.geometry', 'leaf to mesh'),
   8: ('vplants.plantgl.objects', 'Translated'),
   9: ('openalea.data structure', 'int'),
   11: ('openalea.data structure', 'int'),
   12: ('openalea.flow control', 'iter'),
   13: ('openalea.numpy.creation', 'linspace'),
   14: ('openalea.data structure', 'int'),
   16: ('alinea.adel.leaf', 'stress sr'),
   17: ('openalea.data structure.dict', 'dict'),
   18: ('alinea.adel.fitting', 'fit'),
   19: ('vplants.plantgl.visualization', 'plot3D'),
   20: ('vplants.plantgl.objects', 'Shape'),
   21: ('vplants.plantgl.objects', 'Material'),
   22: ('alinea.adel.geometry', 'leaf to mesh'),
   23: ('openalea.color', 'color'),
   24: ('openalea.data structure.tuple', 'tuple3'),
   25: ('openalea.data structure', 'int'),
   26: ('vplants.plantgl.objects', 'Group')},
                             elt_connections={  10466632: (16, 1, 18, 3),
   10466656: (5, 0, 4, 2),
   10466680: (6, 1, 18, 1),
   10466704: (24, 0, 8, 2),
   10466728: (8, 0, 26, 1),
   10466752: (4, 0, 7, 0),
   10466776: (23, 0, 21, 1),
   10466800: (25, 0, 24, 1),
   10466824: (6, 0, 4, 0),
   10466848: (14, 0, 7, 1),
   10466872: (17, 0, 16, 2),
   10466896: (16, 0, 18, 2),
   10466920: (12, 0, 22, 2),
   10466944: (12, 0, 7, 2),
   10466968: (11, 0, 4, 4),
   10466992: (14, 0, 13, 1),
   10467016: (22, 0, 8, 1),
   10467040: (9, 0, 24, 0),
   10467064: (6, 1, 4, 1),
   10467088: (13, 0, 12, 0),
   10467112: (20, 0, 19, 0),
   10467136: (18, 0, 22, 0),
   10467160: (3, 0, 5, 0),
   10467184: (5, 1, 16, 1),
   10467208: (6, 0, 18, 0),
   10467232: (11, 0, 18, 4),
   10467256: (7, 0, 26, 1),
   10467280: (5, 0, 16, 0),
   10467304: (9, 0, 24, 2),
   10467328: (2, 0, 6, 0),
   10467352: (26, 0, 20, 2),
   10467376: (5, 1, 4, 3),
   10467400: (21, 0, 20, 1),
   10467424: (14, 0, 22, 1)},
                             elt_data={  2: {  'block': False,
         'caption': 'Curve2D',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x5df1510> : "Curve2D"',
         'hide': True,
         'id': 2,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': -17.925846797545866,
         'posy': -44.73407182461934,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'Curve2D',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x5df1510> : "Curve2D"',
         'hide': True,
         'id': 3,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': 64.01232902005644,
         'posy': -46.654637961859756,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': 'fit',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x61cf4d0> : "fit"',
         'hide': True,
         'id': 4,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 17.539002172046196,
         'posy': 49.88875385478977,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': 'sr',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x3eeb910> : "curve discretizer"',
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 50.10669582883208,
         'posy': -6.994362639335627,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': 'xy',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x3eeb910> : "curve discretizer"',
         'hide': True,
         'id': 6,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 13.25560285868179,
         'posy': -7.137632308520967,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   7: {  'block': False,
         'caption': 'leaf to mesh',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x4f306d0> : "leaf to mesh"',
         'hide': True,
         'id': 7,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 70.99351790648076,
         'posy': 192.08549860591867,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   8: {  'block': False,
         'caption': 'Translated',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x4ead550> : "Translated"',
         'hide': True,
         'id': 8,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -107.22976283672548,
         'posy': 233.03004325969948,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   9: {  'block': False,
         'caption': '0',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x413a050> : "int"',
         'hide': True,
         'id': 9,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 24.37717490548274,
         'posy': 163.35653232514926,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   11: {  'block': False,
          'caption': '18',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x413a050> : "int"',
          'hide': True,
          'id': 11,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 153.1168456308165,
          'posy': -3.3775162564883665,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   12: {  'block': False,
          'caption': 'iter',
          'delay': 1,
          'factory': '<openalea.core.node.NodeFactory object at 0x686da50> : "iter"',
          'hide': True,
          'id': 12,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 231.75515248517,
          'posy': 63.39954790315112,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   13: {  'block': False,
          'caption': 'linear space',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x4055cd0> : "linspace"',
          'hide': True,
          'id': 13,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 210.17510115613732,
          'posy': 28.466337745031126,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   14: {  'block': False,
          'caption': '10',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x413a050> : "int"',
          'hide': True,
          'id': 14,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 230.45989505798838,
          'posy': -31.762100921453527,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   16: {  'block': False,
          'caption': 'stress sr',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x3f02c10> : "stress sr"',
          'hide': True,
          'id': 16,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -77.70156873617182,
          'posy': 93.43082473101005,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   17: {  'block': False,
          'caption': 'dict',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x563bf10> : "dict"',
          'hide': True,
          'id': 17,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -67.28377294498065,
          'posy': 8.790685700057857,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   18: {  'block': False,
          'caption': 'fit',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x61cf4d0> : "fit"',
          'hide': True,
          'id': 18,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -122.38981892132027,
          'posy': 132.8050356509985,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   19: {  'block': False,
          'caption': 'plot3D',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x60bdd50> : "plot3D"',
          'hide': True,
          'id': 19,
          'lazy': False,
          'minimal': False,
          'port_hide_changed': set(),
          'posx': -8.6293708906423,
          'posy': 322.2730920771706,
          'priority': 0,
          'use_user_color': False,
          'user_application': True,
          'user_color': None},
   20: {  'block': False,
          'caption': 'Shape',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x4ead510> : "Shape"',
          'hide': True,
          'id': 20,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -93.86075455021115,
          'posy': 325.97555867213606,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   21: {  'block': False,
          'caption': 'Material',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x4ea4ad0> : "Material"',
          'hide': True,
          'id': 21,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -221.64474049387215,
          'posy': 233.03842634182752,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   22: {  'block': False,
          'caption': 'leaf to mesh',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x4f306d0> : "leaf to mesh"',
          'hide': True,
          'id': 22,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -116.39932937736916,
          'posy': 188.6271592749888,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   23: {  'block': False,
          'caption': ' ',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x39875d0> : "color"',
          'hide': True,
          'id': 23,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -217.92346666024812,
          'posy': 178.33275618502714,
          'priority': 0,
          'use_user_color': True,
          'user_application': None,
          'user_color': 14},
   24: {  'block': False,
          'caption': 'tuple3',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x3c34ad0> : "tuple3"',
          'hide': True,
          'id': 24,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -22.763860267014344,
          'posy': 210.8652319470803,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   25: {  'block': False,
          'caption': '10',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x413a050> : "int"',
          'hide': True,
          'id': 25,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -11.980979087902288,
          'posy': 170.1299030482125,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   26: {  'block': False,
          'caption': 'Group',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x4ea4d10> : "Group"',
          'hide': True,
          'id': 26,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': -58.1077485763261,
          'posy': 282.1520575200988,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [  (0, 'None'),
         (  1,
            "'copenalea.plantgl.scenegraph._pglsg\\nPoint3Array\\np1\\n((lp2\\ncopenalea.plantgl.math._pglmath\\nVector3\\np3\\n(F0.010374363511800766\\nF0.023077333346009254\\nF1\\ntRp4\\nag3\\n(F0.3521442711353302\\nF0.26626491546630859\\nF1\\ntRp5\\nag3\\n(F0.23109914362430573\\nF0.87061011791229248\\nF1\\ntRp6\\nag3\\n(F0.92518693208694458\\nF0.84084248542785645\\nF1\\ntRp7\\nag3\\n(F0.90239661931991577\\nF0.60353833436965942\\nF1\\ntRp8\\nag3\\n(F1.0261499881744385\\nF0.43674954771995544\\nF1\\ntRp9\\nag3\\n(F0.69370567798614502\\nF0.35986444354057312\\nF1\\ntRp10\\natRp11\\n.'")],
   3: [  (  0,
            'NurbsCurve2D(Point3Array([Vector3(0.0127763,0.221764,1),Vector3(0.0989327,0.958049,1),Vector3(0.337108,0.982034,1),Vector3(0.567297,0.999171,1),Vector3(0.847653,0.959089,1),Vector3(0.928497,0.687595,1),Vector3(0.998286,0.313748,1),Vector3(1,0,1)]), width = 2)'),
         (  1,
            "'copenalea.plantgl.scenegraph._pglsg\\nPoint3Array\\np1\\n((lp2\\ncopenalea.plantgl.math._pglmath\\nVector3\\np3\\n(F0.012776285409927368\\nF0.22176407277584076\\nF1\\ntRp4\\nag3\\n(F0.098932698369026184\\nF0.95804876089096069\\nF1\\ntRp5\\nag3\\n(F0.33710849285125732\\nF0.98203438520431519\\nF1\\ntRp6\\nag3\\n(F0.56729722023010254\\nF0.99917083978652954\\nF1\\ntRp7\\nag3\\n(F0.8476526141166687\\nF0.95908874273300171\\nF1\\ntRp8\\nag3\\n(F0.92849737405776978\\nF0.68759512901306152\\nF1\\ntRp9\\nag3\\n(F0.99828648567199707\\nF0.31374838948249817\\nF1\\ntRp10\\nag3\\n(F1\\nF0\\nF1\\ntRp11\\natRp12\\n.'")],
   4: [],
   5: [(1, '15')],
   6: [(1, '15')],
   7: [(3, '1.0')],
   8: [(0, "''")],
   9: [(0, '0')],
   11: [(0, '18')],
   12: [],
   13: [(0, '1.0'), (2, '100.0'), (3, 'True'), (4, 'True')],
   14: [(0, '10')],
   16: [],
   17: [(0, '{(0.8, 1): 1, (0.3, 0.6): 1}')],
   18: [],
   19: [],
   20: [(0, "''"), (3, '138269408'), (4, '4294967295')],
   21: [  (0, "''"),
          (2, '2.0'),
          (3, 'Color3(0,0,0)'),
          (4, '1.0'),
          (5, '(0, 0, 0)'),
          (6, '0.0')],
   22: [(3, '1.0')],
   23: [(0, '(14, 94, 5)')],
   24: [],
   25: [(0, '10')],
   26: [(0, "''"), (2, 'None')],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {'position': [-17.925846797545866, -44.73407182461934], 'userColor': None, 'useUserColor': False},
   3: {'position': [64.01232902005644, -46.654637961859756], 'userColor': None, 'useUserColor': False},
   4: {'position': [17.539002172046196, 49.88875385478977], 'userColor': None, 'useUserColor': False},
   5: {'position': [50.10669582883208, -6.994362639335627], 'userColor': None, 'useUserColor': False},
   6: {'position': [13.25560285868179, -7.137632308520967], 'userColor': None, 'useUserColor': False},
   7: {'position': [70.99351790648076, 192.08549860591867], 'userColor': None, 'useUserColor': False},
   8: {'position': [-107.22976283672548, 233.03004325969948], 'userColor': None, 'useUserColor': False},
   9: {'position': [24.37717490548274, 163.35653232514926], 'userColor': None, 'useUserColor': False},
   10: {  'position': [-66.6005367473584, 77.14974380365686],
          'useUserColor': False,
          'userColor': None},
   11: {'position': [153.1168456308165, -3.3775162564883665], 'userColor': None, 'useUserColor': False},
   12: {'position': [231.75515248517, 63.39954790315112], 'userColor': None, 'useUserColor': False},
   13: {'position': [210.17510115613732, 28.466337745031126], 'userColor': None, 'useUserColor': False},
   14: {'position': [230.45989505798838, -31.762100921453527], 'userColor': None, 'useUserColor': False},
   15: {  'position': [-53.89352859780767, 36.22219959794419],
          'useUserColor': True,
          'userColor': [14, 94, 5]},
   16: {'position': [-77.70156873617182, 93.43082473101005], 'userColor': None, 'useUserColor': False},
   17: {'position': [-67.28377294498065, 8.790685700057857], 'userColor': None, 'useUserColor': False},
   18: {'position': [-122.38981892132027, 132.8050356509985], 'userColor': None, 'useUserColor': False},
   19: {'position': [-8.6293708906423, 322.2730920771706], 'userColor': None, 'useUserColor': False},
   20: {'position': [-93.86075455021115, 325.97555867213606], 'userColor': None, 'useUserColor': False},
   21: {'position': [-221.64474049387215, 233.03842634182752], 'userColor': None, 'useUserColor': False},
   22: {'position': [-116.39932937736916, 188.6271592749888], 'userColor': None, 'useUserColor': False},
   23: {'useUserColor': True, 'position': [-217.92346666024812, 178.33275618502714], 'userColor': [14, 94, 5]},
   24: {'position': [-22.763860267014344, 210.8652319470803], 'userColor': None, 'useUserColor': False},
   25: {'position': [-11.980979087902288, 170.1299030482125], 'userColor': None, 'useUserColor': False},
   26: {'position': [-58.1077485763261, 282.1520575200988], 'userColor': None, 'useUserColor': False},
   '__in__': {'position': [0, 0], 'userColor': None, 'useUserColor': True},
   '__out__': {'position': [0, 0], 'userColor': None, 'useUserColor': True}},
                             lazy=True,
                             eval_algo='DiscreteTimeEvaluation',
                             )




stress_sr_stress_sr = Factory(name='stress sr',
                authors='C. Pradal, C.Fournier (wralea authors)',
                description='',
                category='geometry',
                nodemodule='stress_sr',
                nodeclass='stress_sr',
                inputs=[{'interface': ISequence, 'name': 's', 'value': None, 'desc': ''}, {'interface': ISequence, 'name': 'r', 'value': None, 'desc': ''}, {'interface': None, 'name': 'd', 'value': None, 'desc': 'dictionary of interval'}],
                outputs=[{'interface': ISequence, 'name': 's', 'desc': ''}, {'interface': ISequence, 'name': 'r', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




curve_dicretizer_points2curve = Factory(name='points2curve',
                authors='C. Pradal, C.Fournier (wralea authors)',
                description='Discretize a 2D curve into a polyline',
                category='geometry',
                nodemodule='curve_dicretizer',
                nodeclass='points2curve',
                inputs=[{'interface': ISequence, 'name': 'x', 'desc': ''}, {'interface': ISequence, 'name': 'y', 'desc': ''}],
                outputs=[{'name': 'curve'}],
                widgetmodule=None,
                widgetclass=None,
               )



