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
        Armor("Pyrogale Gauntlets", "Solar", "Burning Maul"),
        Armor("Arbor Warden"),
        Armor("Cadmus Ridge Lancecap", ("Stasis", "Prismatic"), "Glacial Quake"),
        Armor("Abeyant Leap"),
        Armor("Point-Contact Cannon Brace", ("Arc", "Prismatic")),
        Armor("Second Chance", ("Void", "Prismatic")),
        Armor("Loreley Splendor Helm", ("Solar, Prismatic"), "Hammer of Sol"),
        Armor("Hoarfrost-Z", ("Stasis", "Prismatic"), "Glacial Quake"),
        Armor("No Backup Plans"),
        Armor("The Path of Burning Steps"),
        Armor("Cuirass of the Falling Star"),
        Armor("Precious Scars"),
        Armor("Icefall Mantle", ("Stasis", "Prismatic"), "Glacial Quake"),
        Armor("Citan\'s Ramparts"),
        Armor("Severance Enclosure"),
        Armor("An Insurmountable Skullfort", ("Arc", "Prismatic")),
        Armor("Eternal Warrior"),
        Armor("Helm of Saint-14", "Void", ("Ward of Dawn", "Sentinel Shield")),
        Armor("Khepri's Horn"),
        Armor("Mask of the Quiet One"),
        Armor("One-Eyed Mask"),
        Armor("ACD/0 Feedack Fence"),
        Armor("Aeon Safe"),
        Armor("Ashen Wake", "Solar"),
        Armor("Doom Fang Pauldron"),
        Armor("Stronghold"),
        Armor("Synthoceps"),
        Armor("Ursa Furiosa", "Void", "Sentinel Shield"),
        Armor("Wormgod Caress"),
        Armor("Actium War Rig", None, None, None, ("Machine Gun", "Auto Rifle"))
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