from enum import Enum

class Penetration(str, Enum):
    LIGHT       = "light"
    MEDIUM      = "medium"
    HEAVY       = "heavy"
    TANK_2      = "Tank II"
    UNARMORED_1 = "Unarmored I"
    ANTI_TANK_1 = "Anti-Tank I"
    ANTI_TANK_2 = "Anti-Tank II"
    ANTI_TANK_3 = "Anti-Tank III"
    ANTI_TANK_4 = "Anti-Tank VI"
    ANTI_TANK_5 = "Anti-Tank V"


class War_Bond(str, Enum):
    BASE                  = "base"
    STEELED_VETERANS      = "Steeled Veterans"
    HELLDIVERS_MOBILIZE   = "Helldivers Mobilize"
    KILLZONE_CROSSOVER    = "Helldivers x Killzone Crossover"
    VIPER_COMMANDOS       = "Viper Commandos"
    POLAR_PATRIOTS        = "Polar Patriots"
    DEMOCRATIC_DETONATION = "Democratic Detonation"
    FORCE_OF_LAW          = "Force of Law"
    MASTERS_OF_CEREMONY   = "Masters of Ceremony"
    FREEDOMS_FLAME        = "Freedom's Flame"
    ODST                  = "Obedient Democracy Support Troopers"
    DUST_DEVILS           = "Dust Devils"
    CONTROL_GROUP         = "Control Group"
    BORDERLINE_JUSTICE    = "Borderline Justice"
    SOF                   = "Servants of Freedom"
    TRUTH_ENFORCERS       = "Truth Enforcers"
    URBAN_LEGENDS         = "Urban Legends"
    CUTTING_EDGE          = "Cutting Edge"
    SUPER_STORE           = "Super Store"
    SUPER_CITIZEN_EDITION = "Super Citizen Edition"
    SERVANTS_OF_FREEDOM   = "Servants of Freedom"
    CHEMICAL_AGENTS       = "Chemical Agents"

class Style(str, Enum):
    SPECOPS =   "spec_ops"
    DEFAULT =   "default"
    EXPLOSIVE = "explosive"
