# def __init__(self, name, subclass=None, super=None, aspect=None, weapon=None):
class Armor:
    def __init__(self, name, subclass=None, super=None, aspect=None, weapon=None):
        self.name = name
        self.subclass = subclass
        self.super = super
        self.aspect = aspect
        self.weapon = weapon

armor = {
    "Titan": [
        Armor("Praxic Vestment"),
        Armor("Melas Panoplia", "Solar"),
        Armor("Blastwave Striders"),
        Armor("Wishful Ignorance", ("Strand", "Prismatic")),
        Armor("Hazardous Propulsion"),
        Armor("Stoicism", "Prismatic"),
        Armor("Pyrogale Gauntlets", "Solar", "Burning Maul")
    ],
    "Hunter": [
        Armor("Fortune's Favor"),
        Armor("Moirai", ("Strand", "Prismatic")),
        Armor("Mask of Fealty", ("Stasis", "Prismatic")),
        Armor("Gifted Conviction"),
        Armor("Balance of Power", ("Strand", "Prismatic"), None, "Threaded Specter"),
        Armor("Relativism", "Prismatic"),
        Armor("Mothkeeper's Wraps")
    ],
    "Warlock": [
        Armor("Deimosuffusion", ("Strand", "Prismatic"), "Needlestorm"),
        Armor("Eunoia", ("Solar", "Prismatic"), None, "Hellion"),
        Armor("Rime-Coat Raiment", ("Prismatic", "Stasis"), None, "Bleak Watcher"),
        Armor("Speaker's Sight", ("Prismatic", "Solar")),
        Armor("Mataiodoxia", ("Strand", "Prismatic")),
        Armor("Solipsism", "Prismatic"),
        Armor("Briarbinds", "Void"),
        Armor("Cenotaph Mask", None, None, None, "Trace Rifle")
    ]
}