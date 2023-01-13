import copy
import random

from roulette.character import Character
from roulette.player import Player, SPOON, DEREK, HAN, JIN, GRETER, JOHN

CLOWN_GROUP_SIZE = 4


def _print_players(players):
    for _player in players:
        print(_player)


def _print_characters(characters):
    for _character in characters:
        print(_character)


def _get_support_players(players: [Player]):
    _result = []
    for player in players:
        if player.has_supports():
            _result.append(player)
    return _result


def _get_support_characters(players):
    _result = []
    for _player in players:
        for _character in _player.characters:
            if _character.is_support():
                _result.append(_character)
    return _result


def _get_random_character(player: Player, is_support=False):
    character_pool = []
    for character in player.characters:
        if character.is_support() == is_support:
            character_pool.append(character)

    if len(character_pool) == 0:
        return None
    return random.choice(character_pool)


def _is_same_player(players, character1, character2):
    if character1 == character2:
        return True

    for _player in players:
        if _player.characters.count(character1) == 1:
            return _player.characters.count(character2) == 1

    return False


def _character_group_has_player(group: [Character], character: Character, players: [Player]):
    for _char in group:
        if _is_same_player(players, character, _char):
            return True
    return False


def randomize_groups(players: [Player]):
    _working_player_list = copy.deepcopy(players)
    groups: [[Character]] = []

    # 1. We want no more than 1 support per group, so minimum number of groups is the number of support characters.
    support_characters = _get_support_characters(_working_player_list)

    # 2. Randomize the order of these supports. These will each be the start of a new group.
    random.shuffle(support_characters)
    for _character in support_characters:
        groups.append([_character])

    # 3. Remove support characters from each player's character list
    for _player in _working_player_list:
        _characters = []
        for _character in _player.characters:
            if not _character.is_support():
                _characters.append(_character)
        _player.characters = _characters

    while len(_working_player_list) >= CLOWN_GROUP_SIZE - 1:
        # 4. Get the players with the highest number of characters
        max_character_count = 0
        poll_list = []
        for _player in _working_player_list:
            _count = len(_player.characters)
            if _count > max_character_count:
                max_character_count = _count
                poll_list = [_player]
            elif _count == max_character_count:
                poll_list.append(_player)

        # 5. Shuffle player order
        random.shuffle(poll_list)

        # 6. For each player, select a random character and add to the first group where:
        #        - group is not full
        #        - group does not contain player
        #    Also remove character from that player's list.
        for _player in poll_list:
            _character = _get_random_character(_player)
            _player.characters.remove(_character)
            for _group in groups:
                if len(_group) < CLOWN_GROUP_SIZE and not _character_group_has_player(_group, _character, players):
                    _group.append(_character)
                    break
            else:
                # 7. If no existing groups satisfy those criteria, create a new group.
                groups.append([_character])

            # 8. If this player has no more characters, remove them from the pool.
            if len(_player.characters) == 0:
                _working_player_list.remove(_player)
        # 9. Repeat until fewer than required players remain.

    print(f"\nGroup list:")
    for _group in groups:
        _print_characters(_group)
        print("\n")


player_pool = [SPOON, DEREK, HAN, JIN, GRETER, JOHN]
randomize_groups(player_pool)
