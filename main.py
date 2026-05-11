import random
from pool.armor import armor
from pool.classes import classes
from pool.guns import legendary, exotic

Result = {"class": None, "armor": None, "subclass": None, "aspect_1": None, "aspect_2": None, "super": None, "exotic_slot": None,
          "fixed_slot": None, "kinetic": None, "energy": None, "power": None }

def main():
    print("Destiny 2 Loadout Randomizer by TaniksB - updated for S28")
    Result["class"] = gen_class()
    print(f'Class:           {Result["class"]}')
    Result["armor"] = gen_armor()
    print(f'Exotic Armor:    {Result["armor"].name}')
    Result["subclass"] = gen_subclass()
    print(f'Subclass:        {Result["subclass"]}')
    Result["aspect_1"] = gen_aspect()
    Result["aspect_2"] = gen_aspect()
    print(f'Aspects:         {Result["aspect_1"]} & {Result["aspect_2"]}')
    Result["super"] = gen_super()
    print(f'Super:           {Result["super"]}')
    Result["exotic_slot"] = random.randint(0, 2)
    Result["fixed_slot"] = random.randint(0, 2)
    # These will be rerolled in gen_weapons() if the combination is impossible
    slots = gen_weapons(Result["exotic_slot"], Result["fixed_slot"])
    Result["kinetic"], Result["energy"], Result["power"] = slots[0], slots[1], slots[2]
    print(f'Kinetic Weapon:  {Result["kinetic"]}')
    print(f'Energy Weapon:   {Result["energy"]}')
    print(f'Power Weapon:    {Result["power"]}')




def gen_class():
   return random.choice(["Titan", "Hunter", "Warlock"])


def gen_armor():
    # returns a random Armor object from whichever class occupies Result["class"] (see pools.armor)
    return random.choice(armor[Result["class"]])


def gen_subclass():
    if isinstance(Result["armor"].subclass, tuple):
        # If the armor object has a tuple as .subclass attribute (= multiple subclasses), returns one of them at random
        return random.choice(Result["armor"].subclass)
    
    if Result["armor"].subclass is None:
        # returns a random subclass if the armor object has no .subclass attribute (see pools.classes)
        subclass_chosen = random.choice(list(classes[Result["class"]]))
        return subclass_chosen
    
    # returns the .subclass attribute; if this part of the function is reached, then there is exactly one subclass set as the attribute
    return Result["armor"].subclass


def gen_aspect():
    if Result["aspect_1"] is None:
        # This is the first aspect, need to check Armor.aspect!
        if isinstance(Result["armor"].aspect, tuple):
            # If the armor object has a tuple as .aspect attribute (= multiple aspects), returns one of them at random
            return random.choice(Result["armor"].aspect)
        
        if Result["armor"].aspect != None:
            # returns the aspect set as the .aspect attribute, since there is exactly one
            return Result["armor"].aspect
        
    # Either this is Aspect 2, or Aspect 1 with no Aspect requirement!
    aspect_chosen = random.choice(list(classes[Result["class"]][Result["subclass"]][1]))
    if Result["aspect_1"] is None:
        # This is the first aspect, so no duplicate check is needed
        return aspect_chosen
    
    # Checks if the aspects are duplicate (which is not allowed in the actual game)
    # Recursively calls gen_aspect() to get a new result until aspect_1 and aspect_2 are different
    while Result["aspect_1"] == aspect_chosen:
        aspect_chosen = gen_aspect()
    # returns the chosen aspect (which is guaranteed to be saved as aspect_2 by main() if this part of the function is reached)
    return aspect_chosen


def gen_super():
    if isinstance(Result["armor"].super, tuple):
        # If the armor object has a tuple as .super attribute (= multiple supers), returns one of them at random
        return random.choice(Result["armor"].super)
    
    if Result["armor"].super is None:
        if len(classes[Result["class"]][Result["subclass"]][0][0]) == 1:
            # sets super_chosen as the first super found, if there is only super (Stasis & Strand subclasses)
            super_chosen = classes[Result["class"]][Result["subclass"]][0]

        else:
            # sets super_chosen as a random selection of the supers found in the subclass if there are multiple
            # I guess this would crash if there are somehow 0 Supers? Too bad!
            super_chosen = random.choice(list(classes[Result["class"]][Result["subclass"]][0]))
        return super_chosen
    
    # returns the .super set as the attribute of .armor (must be exactly one if this part of the function is reached)
    return Result["armor"].super


def gen_weapons(exotic_slot, fixed_slot):
    slots = [None, None, None]
    # Later corresponds to kinetic, energy, power slots

    if Result["armor"].weapon is not None:
        # If the armor has a weapon attribute, the function tries to fill the slot at fixed_slot with that one before moving on

        while slots[fixed_slot] is None:
            if len(Result["armor"].weapon[0]) > 1:
                # Randomly decide that Schroedinger's cat is either dead or alive and save that to gun (might change our mind later)
                # ...Randomly chooses a weapon type from the .weapon attribute if there are multiple and save that to gun
                gun = random.choice(Result["armor"].weapon)
                
            else:
                # Save the weapon type set as the .weapon attribute to gun (exactly one weapon type if the previous if didn't trigger)
                gun = Result["armor"].weapon

            if exotic_slot == fixed_slot:
                if Result["armor"].weapon in exotic[fixed_slot]:
                    if len(exotic[fixed_slot][gun]) == 1:
                        # If the fixed_slot has a single exotic of the desired type, saves that one to slots[fixed_slot]
                        slots[fixed_slot] = exotic[fixed_slot][gun]

                    else:
                        # If the fixed_slot has multiple exotics of the desired type, saves a random one to slots[fixed_slot]
                        slots[fixed_slot] = random.choice(list(exotic[fixed_slot][gun]))

                else:
                    # Rerolls exotic slot if it does not have an exotic of the desired type
                    Result["exotic_slot"] = random.randint(0, 2)
                    exotic_slot = Result["exotic_slot"]

            else:
                if gun in legendary[fixed_slot]:
                    # Sets slots[fixed_slot] to the desired type if it exists as a legendary type in that slot
                    slots[fixed_slot] = gun

                else:
                    # Rerolls fixed slot if it does not have a legendaries of the desired type
                    Result["fixed_slot"] = random.randint(0, 2)
                    fixed_slot = Result[fixed_slot]

    for index, slot in enumerate(slots):
        if slot is None:
            # Iterates through the slots and fills the two that are not filled (= the two besides fixed_slot)

            if index == exotic_slot:
                # Builds a list out of the relevant slot from the exotic weapon dictionary in pools.guns through suspicious means
                crime = []
                for key in exotic[exotic_slot]:
                    if len(exotic[exotic_slot][key][0]) == 1:
                        crime.append(exotic[exotic_slot][key])
                    else:
                        for gun in exotic[exotic_slot][key]:
                            crime.append(gun)

                # Sets the slot to a random exotic from the list
                slots[index] = random.choice(crime)

            else:
                # Sets the slot to a random legenary from that slot
                slots[index] = random.choice(list(legendary[index]))

    return slots


main()
