from game.components.powers.power import Power
from game.utils.constants import SHIELD, SHIELD_TYPE

class Shield(Power):
    
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)