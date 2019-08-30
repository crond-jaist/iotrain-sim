# coding: utf-8

#############################################################################
# Define training content for IoTrain-Sim
#############################################################################

# Standard library imports
from collections import OrderedDict

# NOTE: We use the 'OrderedDict' form of 'dict' collection below in order to 
# preserve insertion order, so that menu items are shown in the same order
# in which they are defined in this file. For initialization details, see:
# https://www.georgevreilly.com/blog/2017/02/21/OrderedDictInitialization.html 

# Define training content class
class Content():

    # Initialize training content as an 'OrderedDict' structure
    training_content = OrderedDict([
        ('System Introduction', 'system_introduction.pdf'),
        ('Fundamental Training', OrderedDict([
            ('Single Node', OrderedDict([
                ('Basics of Contiki & Cooja', OrderedDict([
                    ('Contiki Tutorial', 'basics_contiki.pdf'),
                    ('Hello World Simulation', 'hello-world.csc'),
                    ('Cooja Tutorial', 'basics_cooja.pdf')
                ])),
                ('Actuation & Control', OrderedDict([
                    ('Actuation & Control Introduction', 'actuation_control_introduction.pdf'),
                    ('LED Tutorial', 'led.pdf'),
                    ('LED Simulation', 'led.csc'),
                    ('Button Tutorial', 'button.pdf'),
                    ('Button Simulation', 'button.csc'),
                    ('Timer Tutorial', 'timer.pdf'),
                    ('Timer Simulation', 'timer.csc')
                ])),
                ('Sensing', OrderedDict([
                    ('Sensor Tutorial', 'sensor.pdf'),
                    ('Sensor Simulation', 'sensor.csc')
                ]))
            ])),
            ('Networking', OrderedDict([
                ('Broadcast Tutorial', 'broadcast.pdf'),
                ('Broadcast Simulation', 'broadcast.csc')
            ]))
        ])),
        ('Security Training', OrderedDict([
            ('Security Introduction', 'security_introduction.pdf'),
            ('Flooding Attack', 'flooding_attack.pdf'),
            ('DODAG Version Attack', 'dodag_attack.pdf'),
            ('Blackhole Attack', 'blackhole_attack.pdf'),
            ('Decreased Rank Attack', 'rank_attack.pdf'),
        ]))
    ])
