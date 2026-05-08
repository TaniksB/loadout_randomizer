import random
from pool.armor import armor
from pool.classes import classes
from pool.guns import legendary, exotic

Result = []
# [Class, Exotic, Subclass, Aspect_1, Aspect_2, Super, Exotic_Weapon_Slot, Fixed_Slot, Weapon_1, Weapon_2, Weapon_3]
#   0       1       2           3       4         5            6               7           8       9          10

def main():
    print("Destiny 2 Loadout Randomizer by TaniksB - updated for S28")
    Result.append(gen_class())
    print(f'Class:           {Result[0]}')
    Result.append(gen_armor())
    print(f'Exotic Armor:    {Result[1].name}')
    Result.append(gen_subclass())
    print(f'Subclass:        {Result[2]}')
    Result.append(gen_aspect())
    Result.append(gen_aspect())
    print(f'Aspects:         {Result[3]} & {Result[4]}')
    Result.append(gen_super())
    print(f'Super:           {Result[5]}')
    Result.append(random.randint(0, 2))
    Result.append(random.randint(0, 2))
    slots = get_weapons(Result[6], Result[7])
    for i in range(0, 3):
        Result.append(None)
    Result[8], Result[9], Result[10] = slots[0], slots[1], slots[2]
    print(f'Kinetic Weapon:   {Result[8]}')
    print(f'Energy Weapon:    {Result[9]}')
    print(f'Power Weapon:     {Result[10]}')




def gen_class():
   return random.choice(["Titan", "Hunter", "Warlock"])

def gen_armor():
    return random.choice(armor[Result[0]])

def gen_subclass():
    if isinstance(Result[1].subclass, tuple):
        return random.choice(Result[1].subclass)
    if Result[1].subclass is None:
        subclass_chosen = random.choice(list(classes[Result[0]]))
        return subclass_chosen
    return Result[1].subclass

def gen_aspect():
    if len(Result) == 3:
        # This is the first aspect, need to check Armor.aspect!
        if isinstance(Result[1].aspect, tuple):
            return random.choice(Result[1].aspect)
        if Result[1].aspect != None:
            return Result[1].aspect
    # Either this is Aspect 2, or Aspect 1 with no Aspect requirement!
    aspect_chosen = random.choice(list(classes[Result[0]][Result[2]][1]))
    if len(Result) == 3:
        return aspect_chosen
    while Result[3] == aspect_chosen:
        aspect_chosen = gen_aspect()
    return aspect_chosen

def gen_super():
    if isinstance(Result[1].super, tuple):
        return random.choice(Result[1].super)
    if Result[1].super is None:
        if len(classes[Result[0]][Result[2]][0][0]) == 1:
            super_chosen = classes[Result[0]][Result[2]][0]
        else:
            super_chosen = random.choice(list(classes[Result[0]][Result[2]][0]))
        return super_chosen
    return Result[1].super

def get_weapons(exotic_slot, fixed_slot):
    slots = [None, None, None]
    while fixed_slot is None:
        if exotic_slot == fixed_slot:
            if Result[1].weapon in exotic[fixed_slot]:
                if len(exotic[fixed_slot][Result[1].weapon]) == 1:
                    slots[fixed_slot] = exotic[fixed_slot][Result[1].weapon]
                else:
                    slots[fixed_slot] = random.choice(list(exotic[fixed_slot][Result[1].weapon]))
            else:
                Result[6] = random.randint(0, 2)
                exotic_slot = Result[6]
        else:
            if Result[1].weapon in legendary[fixed_slot]:
                slots[fixed_slot] = Result[1].weapon
            else:
                Result[7] = random.randint(0, 2)
                fixed_slot = Result[7]
    for index, slot in enumerate(slots):
        if slot is None:
            if index == exotic_slot:
                crime = []
                for key in exotic[exotic_slot]:
                    if len(exotic[exotic_slot][key][0]) == 1:
                        crime.append(exotic[exotic_slot][key])
                    else:
                        for gun in exotic[exotic_slot][key]:
                            crime.append(gun)
                slots[index] = random.choice(crime)
            else:
                slots[index] = random.choice(list(legendary[index]))
    return slots


main()
