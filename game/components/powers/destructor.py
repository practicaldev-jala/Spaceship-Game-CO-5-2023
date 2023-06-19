from game.components.powers.power import Power
from game.utils.constants import FIRE, DESTRUCTOR_TYPE

class Destructor(Power):
    
    def __init__(self):
        super().__init__(FIRE, DESTRUCTOR_TYPE)