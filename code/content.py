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
        ('System Introduction', OrderedDict([
            ('IoTrain-Sim Overview', 'iotrain-sim_overview.pdf'),
            ('Background on IoT', 'background_iot.pdf')
        ])),
        ('Fundamental Training', OrderedDict([
            ('Single Node', OrderedDict([
                ('Basics of Contiki & Cooja', OrderedDict([
                    ('Contiki Tutorial', 'contiki_tutorial.pdf'),
                    ('Hello World Simulation', 'hello-world.csc'),
                    ('Cooja Tutorial', 'cooja_tutorial.pdf')
                ])),
                ('Actuation & Control', OrderedDict([
                    ('Overview', 'actuation_control_overview.pdf'),
                    ('LED Tutorial', 'led_tutorial.pdf'),
                    ('LED Simulation', 'led.csc'),
                    ('Button Tutorial', 'button_tutorial.pdf'),
                    ('Button Simulation', 'button.csc'),
                    ('Timer Tutorial', 'timer_tutorial.pdf'),
                    ('Timer Simulation', 'timer.csc')
                ])),
                ('Sensing', OrderedDict([
                    ('Sensor Tutorial', 'sensor_tutorial.pdf'),
                    ('Sensor Simulation', 'sensor.csc')
                ]))
            ])),
            ('Networking', OrderedDict([
                ('Communication', OrderedDict([
                    ('Broadcast Tutorial', 'broadcast_tutorial.pdf'),
                    ('Broadcast Simulation', 'broadcast.csc')
                ]))
            ]))
        ])),
        ('Security Training', OrderedDict([
            ('Introduction', OrderedDict([
                ('Security Training Tutorial', 'security_training_tutorial.pdf'),
                ('Routing Protocol Overview', 'routing_protocol_overview.pdf')
            ])),
            ('Resource Attacks', OrderedDict([
                ('Direct Attacks', OrderedDict([
                    ('Flooding Attack Tutorial', 'flooding_attack_tutorial.pdf'),
                    ('Reference Scenario Simulation', 'flooding_attack-reference.csc'),
                    ('Flooding Attack Simulation', 'flooding_attack-simulation.csc')
                ])),
                ('Indirect Attacks', OrderedDict([
                    ('DODAG Version Attack Tutorial', 'dodag_attack_tutorial.pdf'),
                    ('Reference Scenario Simulation', 'dodag_attack-reference.csc'),
                    ('DODAG Version Attack Simulation', 'dodag_attack-simulation.csc')
                ])),
            ])),
            ('Topology Attacks', OrderedDict([
                ('Isolation Attacks', OrderedDict([
                    ('Blackhole Attack Tutorial', 'blackhole_attack_tutorial.pdf'),
                    ('Reference Scenario Simulation', 'blackhole_attack-reference.csc'),
                    ('Blackhole Attack Simulation', 'blackhole_attack-simulation.csc')
                ]))
            ])),
            ('Traffic Attacks', OrderedDict([
                ('Misappropriation Attacks', OrderedDict([
                    ('Decreased Rank Attack Tutorial', 'rank_attack_tutorial.pdf'),
                    ('Reference Scenario Simulation', 'rank_attack-reference.csc'),
                    ('Decreased Rank Attack Simulation', 'rank_attack-simulation.csc')
                ]))
            ]))
        ]))
    ])
