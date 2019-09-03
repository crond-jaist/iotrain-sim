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
            ('Routing Protocol Introduction', 'routing_introduction.pdf'),
            ('Security Training Introduction', 'training_introduction.pdf'),
            ('Flooding Attack', OrderedDict([
                ('Flooding Attack Tutorial', 'flooding_attack.pdf'),
                ('Reference Scenario Simulation', 'flooding_attack-reference.csc'),
                ('Flooding Attack Simulation', 'flooding_attack-simulation.csc')
            ])),
            ('DODAG Version Attack', OrderedDict([
                ('DODAG Version Attack Tutorial', 'dodag_attack.pdf'),
                ('Reference Scenario Simulation', 'dodag_attack-reference.csc'),
                ('DODAG Version Attack Simulation', 'dodag_attack-simulation.csc')
            ])),
            ('Blackhole Attack', OrderedDict([
                ('Blackhole Attack Tutorial', 'blackhole_attack.pdf'),
                ('Reference Scenario Simulation', 'blackhole_attack-reference.csc'),
                ('Blackhole Attack Simulation', 'blackhole_attack-simulation.csc')
            ])),
            ('Decreased Rank Attack', OrderedDict([
                ('Decreased Rank Attack Tutorial', 'rank_attack.pdf'),
                ('Reference Scenario Simulation', 'rank_attack-reference.csc'),
                ('Decreased Rank Attack Simulation', 'rank_attack-simulation.csc')
            ]))
        ]))
    ])
