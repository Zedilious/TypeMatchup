class Input:

    type_dict = {
        "types": ["fire", "water", "grass"],
        "fire": {
            "weakness": ["water"],
            "resistance": ["fire", "grass"]
        },
        "water": {
            "weakness": ["grass"],
            "resistance": ["water", "fire"]
        },
        "grass": {
            "weakness": ["fire"],
            "resistance": ["grass", "water"]
        },
    }

    def __init__(self):
        self.get_input()

    def get_input(self):
        poke_type = raw_input("Please enter one or two types( fire OR water!electric ):")
        self.check_type_count(poke_type)

    def check_type_count(self, poke_type):

        if "!" in poke_type:
            poke_type = poke_type.replace("!", " ").split()

            if not len(poke_type) == 2:
                print("Two types were not selected! Please try again")
                self.get_input()
                return

            valid = True
            for i in poke_type:
                if i not in self.type_dict["types"]:
                    print("%s is not a valid type" % i)
                    valid = False

            if not valid:
                self.get_input()
                return

            print("You chose - %s and %s" % (poke_type[0], poke_type[1]))
            self.two_type_info(poke_type[0], poke_type[1])

        else:

            poke_type = poke_type.split()
            if not poke_type[0] in self.type_dict["types"]:
                print("Not a valid type, please try again")
                self.get_input()
            else:
                print("You chose: %s" % poke_type[0])
                self.one_type_info(poke_type[0])

    def one_type_info(self, p_type):
        strong = []
        weak = []

        for k, v in self.type_dict.items():
            if not k == "types":
                if p_type in self.type_dict[k]["weakness"]:
                    strong.append(k)

                if p_type in self.type_dict[k]["resistance"]:
                    weak.append(k)

        print("\t%s is strong against:" % p_type)
        for i in strong:
            print("\t - %s" % i)

        print("\n\t%s is weak against:" % p_type)
        for i in weak:
            print("\t - %s" % i)

    def two_type_info(self, f_type, s_type):
        s_strong = []
        s_weak = []
        strong = []
        weak = []

        for k, v in self.type_dict.items():
            if not k == "types":
                if f_type in self.type_dict[k]["weakness"]:
                    strong.append(k)

                if f_type in self.type_dict[k]["resistance"]:
                    weak.append(k)


if __name__ == "__main__":
    Input()
