from enum import Enum


class CharacterClass(Enum):
    BERSERKER = "Berserker"
    GUNLANCER = "Gunlancer"
    DESTROYER = "Destroyer"
    PALADIN = "Paladin"
    STRIKER = "Striker"
    WARDANCER = "Wardancer"
    SCRAPPER = "Scrapper"
    SOULFIST = "Soulfist"
    GLAIVIER = "Glaivier"
    MACHINIST = "Machinist"
    ARTILLERIST = "Artillerist"
    DEADEYE = "Deadeye"
    SHARPSHOOTER = "Sharpshooter"
    GUNSLINGER = "Gunslinger"
    SORCERESS = "Sorceress"
    ARCANIST = "Arcanist"
    SUMMONER = "Summoner"
    BARD = "Bard"
    REAPER = "Reaper"
    SHADOWHUNTER = "Shadowhunter"
    DEATHBLADE = "Deathblade"


class Character:
    character_class: CharacterClass
    character_name: str

    def __init__(self, character_class, character_name=""):
        self.character_class = character_class
        self.character_name = character_name

    def __str__(self):
        if len(self.character_name) > 0:
            return f"{self.character_name} {self.character_class.value}"
        return f"{self.character_class.value}"

    def __eq__(self, other):
        if isinstance(other, Character):
            return self.character_class == other.character_class and self.character_name == other.character_name
        return False

    def is_support(self):
        return self.character_class == CharacterClass.PALADIN or self.character_class == CharacterClass.BARD
