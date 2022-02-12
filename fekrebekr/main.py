from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT
import argparse
from random import randint
import json

# IMPORT TYPING
from typing import Final, Literal

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

"""
Game FekreBekr - Console Guessing Game
Have Fun :)
"""

# CONST
_NAME: Final = 'Fekre Bekr'
_VERSION: Final = '0.2'
_DESCRIPTION: Final = 'Some Gussing Game !!'

# TYPE ALIASES
T_STATE = list[Literal[0, 1, 2]]    # 0: Wrong Value, 1: True Value & True Sit, 2: True Value But Wrong Sit

# GAME GLOBAL
LEVEL = []
GUESS = {}
DETAIL_PATH = './detail.json'

def state(target: str, guess: str) -> T_STATE:
    """
    function state:
        Analyse Guess
    args:
        target [str]: [Target Value].
        guess [str]: [Guess Value].

    return:
        [T_STATE]: [State of Value].

    STATE VALUE MEAN:
        `0`: Value Not Exists in Sit.
        `1`: True val & True sit.
        `2`: Value in Target But Wrong Sit.
    """
    # Define State List - Result
    _state = []

    # Target & Guess Convert To Dictionary `Key`: `Value` - Key is Sit Value Position `index`
    # Map Target, Map Guess
    mp_tt, mp_gs = {i:c for i, c in enumerate(target)}, {i:c for i, c in enumerate(guess)}

    # Index Check Value
    idx = 0

    # State Loop - Condition [while mp_gs]: Loop Runing Until Guess Dict is Empty
    while mp_gs:

        # [True Value & True Index] - True & True Sit
        if mp_gs[idx] == mp_tt.get(idx, False):
            _state.append(1)
            # Remove Value From Both Dict
            del mp_gs[idx], mp_tt[idx]

        # [True Value & False Index] - True & False Sit
        elif mp_gs[idx] in mp_tt.values():
            _state.append(2)
            # Find Key For Removing Value
            get_key = [k for k, v in mp_tt.items() if v == mp_gs[idx]]
            # Remove Value From Both Dict
            del mp_gs[idx], mp_tt[get_key[0]]

        # [False Value]
        else:
            _state.append(0)
            # Remove Value From Guess Dict
            del mp_gs[idx]

        # Next Character - Update Key
        idx += 1

    # Return State
    return _state

def status(state: T_STATE) -> str:
    """
    function status:
        Humanize State
    args:
        state [T_STATE]: [Need State Value].

    return:
        [str]: [Information of State].
    """

    # True Val & True Sit
    fix = 0

    # True Val & False Sit
    nfix = 0

    # Status Result
    res = []

    # Loop In State Value
    for i in state:
        # Switch
        match i:

            # True Val & True Sit
            case 1:
                fix += 1

            # True Val & False Sit
            case 2:
                nfix += 1

    # Check if All Value True & True Means Win
    if fix == len(state):
        return "*** You Win ***"

    # How Many True & True
    if fix > 0:
        res.append(f'[{fix}] True and True `Sit`')

    # How Many True & False
    if nfix > 0:
        res.append(f'[{nfix}] True But False `Sit`')

    # Check If Result Not Empty Join To Gether & Return
    if res:
        return ' , '.join(res)

    return 'All is Wrong !'

def make_target(length: int = 5) -> str:
    """
    function make_target:
        Create New Target
    args:
        length [int]: [Return Target With Ordered Length] default is `5`.

    return:
        [str]: [Created Target]
    """
    # Make New Target - Iterable Randint & joining To gether
    mk = ''.join((f"{randint(0, 9)}" for _ in range(length)))

    # Check if Created Value Exists - Create New Value [Recursively Return make_target]
    if mk in LEVEL:
        return make_target(length)

    # Return Created Value
    return mk

def length_validate(length: int) -> int:
    """
    function length_validate:
        Update Length if Need
    args:
        length [int]: [Length Target]

    return:
        [int]: [Validate Length]
    """

    # Get Level Number With Size Of Passed Level in LEVEL
    l_lvl = len(LEVEL)

    # Check bigger or Equal 50
    if l_lvl >= 50:
        if length == 5:
            return length + 1

    # Check bigger or Equal 100
    elif l_lvl >= 100:
        if length == 6:
            return length + 1

    # Check bigger or Equal 150
    elif l_lvl >= 150:
        return length + 1

    return length

def new_level(length: int = 5) -> tuple[str, T_STATE]:
    """
    function new_level:
        Create New Level
    args:
        length [int]: [Length of Target]
    return:
        [tuple[str, T_STATE]] : [Target and Win State].
    """

    # Create New Target - Call make_target
    new_target = make_target(length)

    # Get Win State
    win_state = state(new_target, new_target)

    # Retrun Target & Win State
    return new_target, win_state

def save_detail() -> None:
    """
    function save_detail:
        Save Some Detail in Json File to Global `DETAIL_PATH`
    """
    res = {}

    # To Detail Format
    for lvl, item in enumerate(GUESS.values()):
        target = LEVEL[lvl]

        record = {guess:state for guess, state in item}

        res[target] = {
            'level': (lvl + 1),
            'guesses': len(item),
            'record': record,
            }

    with open(DETAIL_PATH, 'w') as f:
        json.dump(res, f, indent=6)

def new_game(length: int, limit: int) -> int:
    """
    function new_game:
        Start New Game
    args:
        length [int]: [Target Length].
        limit [int]: [Guess Limit].
    """

    # Game Stuff Must Be Here
    # Create Level
    _tmp_length = length
    length = length_validate(length)

    # Level Counter
    lvl_count = 1

    # Level Stuff - Target, Win State
    lvl, win = new_level(length)

    # Added To Global Level List
    LEVEL.append(lvl)

    # Initialize Level To Global Dict
    GUESS[lvl_count] = []

    print(f"LEVEL < {lvl_count} >")

    _runing = True

    while _runing:
        # Get Input
        print(f'LVL <{lvl_count}> - CHAR [{length}]')
        inp = str(input(f"GUESS [{limit - len(GUESS[lvl_count])}]/[{limit}] />: "))
        if inp == 'exit':
            print("- EXIT FROM GAME -")
            _runing = False
            break

        # This is Cheat Code
        elif inp == '&&>CHEAT>&&':
            print(f"{LEVEL=}\n{GUESS=}")
            continue

        if not len(inp) == length:
            print("ERR [Invalid Input]: Length Your Guess Must Be Equal Target Please Try Again.")
            continue

        get_state = state(lvl, inp)
        get_status = status(get_state)

        GUESS[lvl_count].append((inp, get_state))

        if get_state == win:
            print(get_status)
            print(f"Target : [{lvl}] - Your Guess [{inp}]\n")
            nxt_lvl = str(input(f'Continue [Y]/N: '))

            if nxt_lvl.lower() == 'n':
                print("- EXIT FROM GAME -")
                _runing = False
                break

            else:
                length = length_validate(length)
                lvl_count += 1
                lvl, win = new_level(length)

                LEVEL.append(lvl)
                GUESS[lvl_count] = []

                print('\n\n')
                print(f"LEVEL < {lvl_count} >")

        else:
            if len(GUESS[lvl_count]) >= limit:
                print("!! GAME OVER !!")
                print(f"- YOU PASSED [{lvl_count}] LEVEL WELL DONE :)\n")

                start_again = input(f'## Start Again [Y]/N? ')

                if start_again.lower() == 'n':
                    _runing = False
                    print("- EXIT FROM GAME -")
                    break

                else:
                    print(f"- Save Detail to [{DETAIL_PATH}] -")

                    save_detail()

                    print("- CLEAR CURRENT DATA -")

                    LEVEL.clear()
                    GUESS.clear()

                    print('\n\n')
                    return new_game(_tmp_length, limit)

            else:
                print(get_status)
                continue

    print(f"- Save Detail to [{DETAIL_PATH}] -")
    save_detail()
    return 0

def main() -> int:
    global DETAIL_PATH, LEVEL, GUESS, _NAME, _DESCRIPTION, _VERSION

    # Create ArgumentParser Object
    parser = argparse.ArgumentParser(_NAME, description=_DESCRIPTION)

    # Add Version Option
    parser.add_argument(
        '--version',
        '-V',
        action= "version",
        version=f'%(prog)s {_VERSION}',
        )

    # -- Initialize Game Options

    # Target Length
    parser.add_argument(
        '--length',
        type=int,
        default= 5,
        help = "Length Of Generated Target",
    )

    # Guess Limit - Game Over
    parser.add_argument(
        '--guess',
        type=int,
        default=6,
        help="Level Guess Limit",
    )

    # Save Detail Path
    parser.add_argument(
        '--detail',
        type=str,
        default=DETAIL_PATH,
        help="Path For Save Detail",
    )

    # Parse Arguments
    arguments = vars(parser.parse_args())
    DETAIL_PATH = arguments['detail']

    # Start New Game
    return new_game(arguments['length'], arguments['guess'])


# Python Execute Statement - Only if This File Execute This Block Run
if __name__ == '__main__':
    raise SystemExit(main())    # This Line Means `sys.exit(main())`
