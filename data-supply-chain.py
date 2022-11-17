
from transitions import Machine

import random

class DataSupplyChain(object):

    # Define some states. Most of the time, narcoleptic superheroes are just like
    # everyone else. Except for...

    states = ['point of origin','ingested','normalized', 'deduplicated', 'deidentified', 'prepped for distribution','downloaded']

    def __init__(self, name):


        # a name. Any name at all. 
        self.name = name

        # What have we accomplished today?
        self.kittens_rescued = 0

        # Initialize the state machine
        self.machine = Machine(model=self, states=DataSupplyChain.states, initial='point of origin')

        # Add some transitions. We could also define these using a static list of
        # dictionaries, as we did with states above, and then pass the list to
        # the Machine initializer as the transitions= argument.

        self.machine.add_transition(trigger='data_ingestion_process', source='point of origin', dest='ingested')
        self.machine.add_transition('data_normalization_process', 'ingested', 'normalized')
        self.machine.add_transition('deduplication_process', 'normalized', 'deduplicated')
        #self.machine.add_transition('distress_call', '*', 'saving the world', before='change_into_super_secret_costume')
        self.machine.add_transition('deidentification_process', 'deduplicated', 'deidentified')
        #self.machine.add_transition('complete_mission', 'saving the world', 'sweaty', after='update_journal')
        self.machine.add_transition('prep_for_distribution', 'deidentified', 'prepped for distribution')
        #self.machine.add_transition('clean_up', 'sweaty', 'asleep', conditions=['is_exhausted'])
        self.machine.add_transition('download', 'prepped for distribution', 'downloaded')

        # Our NarcolepticSuperhero can fall asleep at pretty much any time.
        #self.machine.add_transition('nap', '*', 'asleep')
        
    def update_journal(self):
        self.kittens_rescued += 1

    @property
    def is_exhausted(self):
        """ Basically a coin toss. """
        return random.random() < 0.5

    def change_into_super_secret_costume(self):
        print("Beauty, eh?")
print
print
print("--------------------------------------")
print("National Police Agency Big Data Portal")
print("Data Supply Chain proof-of-concept with Apache NiFi V0.1 June 2022")
print("Example state transitions using Finite State Machine")
print("--------------------------------------")
big_data_system = DataSupplyChain("National Police Agency Big Data System")
print("big_data_system.state = %s" % (big_data_system.state) )

big_data_system.data_ingestion_process()
print("big_data_system.state = %s" % (big_data_system.state) )

big_data_system.data_normalization_process()
print("big_data_system.state = %s" % (big_data_system.state) )

#big_data_system.clean_up()

big_data_system.deduplication_process()
print("big_data_system.state = %s" % (big_data_system.state) )

big_data_system.deidentification_process()
print("big_data_system.state = %s" % (big_data_system.state) )

big_data_system.prep_for_distribution()
print("big_data_system.state = %s" % (big_data_system.state) )

# Back to the crib.
big_data_system.download()
print("big_data_system.state = %s" % (big_data_system.state) )

#big_data_system.clean_up()
#print("big_data_system.kittens_rescued = %s" % (big_data_system.kittens_rescued) )
print("--------------------------------------")
print("Endpoint reached in data supply chain")
print("--------------------------------------")
print
print

