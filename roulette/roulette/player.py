from character import Character, CharacterClass


class Player:
    player_name: str
    characters: [Character]

    def __init__(self, player_name, characters=[]):
        self.player_name = player_name
        self.characters = characters
        for character in self.characters:
            if character.character_name == "":
                character.character_name = self.player_name

    def __str__(self):
        result = f"PLAYER: {self.player_name}\nCHARACTERS:\n"
        for character in self.characters:
            result += f"    {character}\n"
        return result

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.player_name == other.player_name
        return False

    def has_supports(self):
        for char in self.characters:
            if char.is_support():
                return True
        return False

    def has_dps(self):
        for char in self.characters:
            if not char.is_support():
                return True
        return False


SPOON = Player(
    player_name="Spoon",
    characters=[
        Character(CharacterClass.BERSERKER, "Spoonski"),
        Character(CharacterClass.BARD, "Spooneroni"),
        Character(CharacterClass.WARDANCER, "Fruttapunch"),
        Character(CharacterClass.DEATHBLADE),
        Character(CharacterClass.SORCERESS),
        Character(CharacterClass.STRIKER),
        Character(CharacterClass.DEADEYE)
    ]
)

DEREK = Player(
    player_name="Derek",
    characters=[
        Character(CharacterClass.BARD),
        Character(CharacterClass.DEATHBLADE),
        Character(CharacterClass.GUNSLINGER),
        Character(CharacterClass.SHADOWHUNTER),
        Character(CharacterClass.SORCERESS),
        Character(CharacterClass.SCRAPPER),
        Character(CharacterClass.REAPER)
    ]
)

HAN = Player(
    player_name="Han",
    characters=[
        Character(CharacterClass.GLAIVIER),
        Character(CharacterClass.STRIKER),
        Character(CharacterClass.SORCERESS),
        Character(CharacterClass.REAPER),
    ]
)

JIN = Player(
    player_name="Jin",
    characters=[
        Character(CharacterClass.DESTROYER),
        Character(CharacterClass.GLAIVIER)
    ]
)

GRETER = Player(
    player_name="Greter",
    characters=[
        Character(CharacterClass.PALADIN),
        Character(CharacterClass.BARD),
        Character(CharacterClass.WARDANCER),
        Character(CharacterClass.DEADEYE),
        Character(CharacterClass.BERSERKER),
        Character(CharacterClass.SHADOWHUNTER)
    ]
)

JOHN = Player(
    player_name="John",
    characters=[
        Character(CharacterClass.PALADIN),
        Character(CharacterClass.STRIKER)
    ]
)
