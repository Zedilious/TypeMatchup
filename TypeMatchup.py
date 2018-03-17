class Input:

    type_dict = {
        "types": ["normal", "fire", "water", "electric", "grass",
                  "ice", "fighting", "poison", "ground", "flying",
                  "psychic", "bug", "rock", "ghost", "dragon",
                  "dark", "steel", "fairy"
                  ],
        "normal": {
            "weakness": ["fighting"],
            "resistance": [],
            "immune": ["ghost"]
        },
        "fire": {
            "weakness": ["water", "ground", "rock"],
            "resistance": ["fire", "grass", "ice", "bug", "steel", "fairy"],
            "immune": []
        },
        "water": {
            "weakness": ["grass", "electric"],
            "resistance": ["water", "fire", "Ice", "steel"],
            "immune": []
        },
        "grass": {
            "weakness": ["fire", "ice", "poison", "flying", "bug"],
            "resistance": ["grass", "water", "electric", "ground"],
            "immune": []
        },
        "ice": {
            "weakness": ['fire', 'fighting', 'rock', 'steel'],
            "resistance": ['ice'],
            "immune": []
        },
        "fighting": {
            "weakness": ['flying', 'psychic', 'fairy'],
            "resistance": ['bug', 'rock', 'dark'],
            "immune": []
        },
        "poison": {
            "weakness": ['ground', 'psychic'],
            "resistance": ['grass', 'fighting', 'poison', 'bug', 'fairy'],
            "immune": []
        },
        "ground": {
            "weakness": ["water grass ice"],
            "resistance": [""],
            "immune": []
        },
        "flying": {
            "weakness": [],
            "resistance": [],
            "immune": []
        },
        "psychic": {
            "weakness": [],
            "resistance": [],
            "immune": []
        },
        "bug": {
            "weakness": [],
            "resistance": [],
            "immune": []
        },
        "rock": {
            "weakness": [],
            "resistance": [],
            "immune": []
        },
        "ghost": {
            "weakness": [],
            "resistance": [],
            "immune": []
        },
        "dragon": {
            "weakness": [],
            "resistance": [],
            "immune": []
        },
        "dark": {
            "weakness": [],
            "resistance": [],
            "immune": []
        },
        "steel": {
            "weakness": [],
            "resistance": [],
            "immune": []
        },
        "fairy": {
            "weakness": [],
            "resistance": [],
            "immune": []
        },
    }

    def __init__(self):
        self.get_type()

    def get_type(self):
        poke_type = raw_input("Please enter one or two types( fire OR water!electric ):")

        self.check_type_count(poke_type)

    """
        Get required stance of type, attacking defending or both
    """
    def get_stance(self, f_type, s_type=None):
        att_def = raw_input("Please choose from the following options [Attack | Defend | Both]: ")

        if att_def.lower() not in ["attack", "defend", "both"]:
            print("Incorrect input, please try again.")
            self.get_stance(f_type, s_type)
            return

        elif att_def.lower() == "attack":
            if not s_type:
                self.one_type_att(f_type)
            else:
                self.two_type_att(f_type, s_type)

        elif att_def.lower() == "defend":
            if not s_type:
                self.one_type_def(f_type)
            else:
                self.two_type_def(f_type, s_type)

        else:
            if not s_type:
                self.one_type_att(f_type)
                self.one_type_def(f_type)
            else:
                self.two_type_def(f_type, s_type)
                self.two_type_att(f_type, s_type)

        self.again()

    """
        validate the users input
    """
    def check_type_count(self, poke_type):

        if "!" in poke_type:
            poke_type = poke_type.replace("!", " ").split()

            if not len(poke_type) == 2:
                print("Two types were not selected! Please try again")
                self.get_type()
                return

            valid = True
            for i in poke_type:
                if i not in self.type_dict["types"]:
                    print("%s is not a valid type" % i)
                    valid = False

            if not valid:
                self.get_type()
                return

            print("You chose - %s and %s" % (poke_type[0], poke_type[1]))
            self.get_stance(poke_type[0], poke_type[1])

        else:

            poke_type = poke_type.split()
            if not poke_type[0] in self.type_dict["types"]:
                print("Not a valid type, please try again")
                self.get_type()
            else:
                print("You chose: %s" % poke_type[0])
                self.get_stance(poke_type[0])

    """
        Calculate single type attacking strengths and weaknesses
    """
    def one_type_att(self, p_type):
        strong = []
        weak = []

        for k, v in self.type_dict.items():
            if not k == "types":
                if p_type in self.type_dict[k]["weakness"]:
                    strong.append(k)

                if p_type in self.type_dict[k]["resistance"]:
                    weak.append(k)

        print("\nATTACK")

        if not strong:
            print("\t%s is not strong against anything" % p_type)
        else:
            print("\t%s is strong against:" % p_type)
            for i in strong:
                print("\t - %s" % i)

        if not weak:
            print("\n\t%s is not weak against anything" % p_type)
        else:
            print("\n \t%s is weak against:" % p_type)
            for i in weak:
                print("\t - %s" % i)

        return

    """
        Calculate single type defending strengths and weaknesses
    """
    def one_type_def(self, p_type):
        strong = []
        weak = []

        for k, v in self.type_dict.items():
            if k == p_type:
                for i in self.type_dict[p_type]["resistance"]:
                    strong.append(i)
                for i in self.type_dict[p_type]["weakness"]:
                    weak.append(i)

        print("\nDEFENDING")

        if not strong:
            print("\t%s is not resistant to anything" % p_type)
        else:
            print("\t%s is resistant to:" % p_type)
            for i in strong:
                print("\t - %s" % i)

        if not weak:
            print("\n\t%s is not weak to anything" % p_type)
        else:
            print("\n \t%s is weak to:" % p_type)
            for i in weak:
                print("\t - %s" % i)

        return

    """
        Calculate dual type attacking strengths and weaknesses
    """
    def two_type_att(self, f_type, s_type):
        s_strong = []
        s_weak = []
        strong = []
        weak = []


    """
        Calculate dual type defending strengths and weaknesses
    """
    def two_type_def(self, f_type, s_type):
        s_strong = []
        s_weak = []
        strong = []
        weak = []

        return

    """ 
        Check if the user would like to check another matchup
    """
    def again(self):
        i = False

        while not i:

            text = raw_input("\nWould you like to check more types? [y/n]: ")

            if text not in ["y", "n"]:
                print("\nnot a valid response, use 'y' or 'n'")

            else:

                if text == "y":
                    self.get_type()
                else:
                    print("\nThank you for using TypeMatchup, goodbye!")

                i = True


if __name__ == "__main__":
    Input()
