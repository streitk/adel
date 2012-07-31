
# This file has been generated at Fri Oct 29 11:39:23 2010

from openalea.core import *


__name__ = 'alinea.adel.stand'

__editable__ = True
__description__ = 'Build a crop of plant using simple rules'
__license__ = 'CECILL'
__url__ = ''
__alias__ = ['adel.stand']
__version__ = '0.0.1'
__authors__ = 'C. Pradal, C. Fournier'
__institutes__ = 'CIRAD, INRA, INRIA'
__icon__ = ''


__all__ = ['stand_agronomicplot', 'stand_agronomicplotwithdistribution', 'stand_sample_selection', 'stand_regularband', 'stand_planter', 'stand_concentric', 'stand_regular', 'CanMTGPlanter_CanMTGPlanter']



stand_agronomicplot = Factory(name='agronomic plot',
                authors='C. Pradal, C. Fournier (wralea authors)',
                description='Compute positions of plants for a standard agronomic row-based stand',
                category='Unclassified',
                nodemodule='stand',
                nodeclass='agronomicplot',
                inputs=[{'interface': IFloat, 'name': 'Plot length (m)', 'value': 1, 'desc': 'plot dimension along row direction'}, 
                        {'interface': IFloat, 'name': 'Plot width (m)', 'value': 1, 'desc': 'plot dimension across row direction'}, 
                        {'interface': IFloat, 'name': 'sowing density (pl/m2)', 'value': 150, 'desc': ''}, 
                        {'interface': IFloat, 'name': 'actual plant density (pl/m2)', 'value': 150, 'desc': ''}, 
                        {'interface': IFloat, 'name': 'inter row (m)', 'value': 0.125, 'desc': 'Distance between ranks'},
                        {'interface': IFloat, 'name': 'noise (%)', 'value': 0, 'desc': ''},
                        {'interface': IInt, 'name': 'conversion factor from m to output unit', 'value': 100, 'desc': ''},
                        {'interface': IFloat, 'name': 'pcentral', 'value': 0.6, 'desc': 'proportion of plant per row kept in the central zone'}],
                outputs=[{'interface': IInt, 'name': 'number of plants', 'desc': ''}, 
                         {'interface': ISequence, 'name': 'positions', 'desc': 'List of plant positions'}, 
                         {'interface': ISequence, 'name': 'domain', 'desc': '2D bounding box of the stand'},
                         {'interface': IFloat, 'name': 'domain area (m2)', 'desc': 'area of the simulated plot'},
                         {'interface': ISequence, 'name': 'central domain', 'desc': '2D bounding box of the central zone of the stand'},],
                widgetmodule=None,
                widgetclass=None,
               )

stand_agronomicplotwithdistribution = Factory(name='agronomic plot with distributions',
                authors='C. Pradal, C. Fournier (wralea authors)',
                description='Returns the number of plants, the positions, azmuthal orientations, and the domain of a plot specified with agronomical variables',
                category='Unclassified',
                nodemodule='stand',
                nodeclass='agronomicplotwithdistributions',
                inputs=[{'interface': IFloat, 'name': 'Plot length (m)', 'value': 1, 'desc': 'plot dimension along row direction'}, 
                        {'interface': IFloat, 'name': 'Plot width (m)', 'value': 1, 'desc': 'plot dimension across row direction'}, 
                        {'interface': IFloat, 'name': 'sowing density (pl/m2)', 'value': 150, 'desc': ''}, 
                        {'interface': IFloat, 'name': 'actual plant density (pl/m2)', 'value': 150, 'desc': ''}, 
                        {'interface': IFloat, 'name': 'inter row (m)', 'value': 0.125, 'desc': 'Distance between ranks'}, 
                        {'interface': IFloat, 'name': 'mu (-)', 'value': 0.0, 'desc': 'von Mises parameter -> mean'}, 
                        {'interface': IFloat, 'name': 'kappa (-)', 'value': 3.0, 'desc': 'von Mises parameter -> concentration'},
                        {'interface': IFloat, 'name': 'noise (%)', 'value': 0, 'desc': ''}, 
                        {'interface': IInt, 'name': 'conversion factor from m to output unit', 'value': 100, 'desc': ''}],
                outputs=[{'interface': IInt, 'name': 'number of plants', 'desc': ''}, 
                         {'interface': ISequence, 'name': 'positions', 'desc': 'List of plant positions'}, 
                         {'interface': ISequence, 'name': 'azimuths', 'desc': 'List of plant azimuths'}, 
                         {'interface': ISequence, 'name': 'domain', 'desc': '2D bounding box of the stand'},
                         {'interface': IInt, 'name': 'simulated density', 'desc': 'density of the simulated plot'}],
                widgetmodule=None,
                widgetclass=None,
               )



stand_sample_selection = Factory(name='sample selection',
                authors='C. Pradal, C. Fournier (wralea authors)',
                description='Choose a sample from a list of points.',
                category='scene',
                nodemodule='stand',
                nodeclass='sample_selection',
                inputs=[{'interface': ISequence, 'name': 'points', 'desc': 'List of points'}, {'interface': IFloat(min=0, max=99, step=1.000000), 'name': 'gap fraction', 'value': 10, 'desc': 'Gap fraction'}],
                outputs=[{'interface': ISequence, 'name': 'positions', 'desc': 'List of plant positions'}],
                widgetmodule=None,
                widgetclass=None,
               )




stand_regularband = Factory(name='regularband',
                authors='C. Pradal, C. Fournier (wralea authors)',
                description='Returns a regular distribution of points within band to build a stand.',
                category='scene.distribution',
                nodemodule='stand',
                nodeclass='regularband',
                inputs=[{'interface': IInt, 'name': 'nb_plants', 'value': 1, 'desc': 'Number of plants'}, {'interface': IInt, 'name': 'nb_rank', 'value': 1, 'desc': 'Number of ranks'}, {'interface': IFloat, 'hide': True, 'name': 'dx', 'value': 0.012500000000000001, 'desc': 'Distance between plants in a rank'}, {'interface': IFloat, 'hide': True, 'name': 'dy', 'value': 0.17499999999999999, 'desc': 'Distance between ranks'}],
                outputs=[{'interface': ISequence, 'name': 'positions', 'desc': 'List of plant positions'}, {'interface': ISequence, 'name': 'domain', 'desc': '2D bounding box of the stand'}],
                widgetmodule=None,
                widgetclass=None,
               )




stand_planter = Factory(name='planter',
                authors='C. Pradal, C. Fournier (wralea authors)',
                description='',
                category='scene',
                nodemodule='stand',
                nodeclass='planter',
                inputs=[{'interface': IDict, 'name': 'scene', 'value': {}, 'desc': 'CanestraScene'}, {'interface': ISequence, 'name': 'positions', 'value': [], 'desc': 'List of plant positions'}],
                outputs=[{'interface': IDict, 'name': 'scene', 'desc': 'The transformed scene'}],
                widgetmodule=None,
                widgetclass=None,
               )




stand_concentric = Factory(name='concentric',
                authors='C. Pradal, C. Fournier (wralea authors)',
                description='Returns a regular distribution of points to build a stand.',
                category='scene.distribution',
                nodemodule='stand',
                nodeclass='concentric',
                inputs=[{'interface': IInt, 'name': 'nb_plants', 'value': 1, 'desc': 'Number of plants'}, {'interface': IFloat, 'name': 'distance', 'value': 0.125, 'desc': 'Distance between plants'}],
                outputs=[{'interface': ISequence, 'name': 'positions', 'desc': 'List of plant positions'}],
                widgetmodule=None,
                widgetclass=None,
               )




stand_regular = Factory(name='regular',
                authors='C. Pradal, C. Fournier (wralea authors)',
                description='Returns a regular distribution of points to build a stand.',
                category='scene.distribution',
                nodemodule='stand',
                nodeclass='regular',
                inputs=[{'interface': IInt, 'name': 'nb_plants', 'value': 1, 'desc': 'Number of plants'}, {'interface': IInt, 'name': 'nb_rank', 'value': 1, 'desc': 'Number of ranks'}, {'interface': IFloat, 'name': 'dx', 'value': 0.125, 'desc': 'Distance between plants in a rank'}, {'interface': IFloat, 'name': 'dy', 'value': 0.80000000000000004, 'desc': 'Distance between ranks'}],
                outputs=[{'interface': ISequence, 'name': 'positions', 'desc': 'List of plant positions'}, {'interface': ISequence, 'name': 'domain', 'desc': '2D bounding box of the stand'}],
                widgetmodule=None,
                widgetclass=None,
               )

stand_sample_regular_gaps = Factory(name='regular gaps',
                authors='C. Pradal, C. Fournier (wralea authors)',
                description='Choose a regular sample from a list of points.',
                category='scene',
                nodemodule='stand',
                nodeclass='sample_regular_gaps',
                inputs=[{'interface': ISequence, 'name': 'points', 'desc': 'List of points'}, 
                {'interface': ISequence, 'name': 'pattern', 'value': [0,1],'desc': 'selection pattern (0=gap)'}],
                outputs=[{'interface': ISequence, 'name': 'positions', 'desc': 'List of plant positions'},
                {'interface': ISequence, 'name': 'positions', 'desc': 'List of gap positions'}],
                widgetmodule=None,
                widgetclass=None,
               )
__all__.append('stand_sample_regular_gaps')

CanMTGPlanter_CanMTGPlanter = Factory(name='CanMTGPlanter',
                authors='C. Pradal, C. Fournier (wralea authors)',
                description='arrange Alinea CanMTG plants in a stand',
                category='scene design',
                nodemodule='CanMTGPlanter',
                nodeclass='CanMTGPlanter',
                inputs=[{'interface': None, 'name': 'CanMTG', 'value': None, 'desc': ''},
                        {'interface': ISequence, 'name': 'Positions', 'value': [(0, 0, 0)], 'desc': ''},
                        {'interface': IInt, 'name': 'random_seed', 'value': 0, 'desc': 'Rotate each plant with a random rotation around z axis if random_seed > 0'},
                        {'interface': ISequence, 'name': 'Azimuts', 'value': None, 'desc': 'Rotate each plant according to the specified azimuth in the sequence'}],
                outputs=[{'interface': None, 'name': 'StandMTG', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




