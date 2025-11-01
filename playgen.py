import random
import json

#x,y
route_library = {
    "Slant": [(0, 0), (0, 3), (-10, 10)],
    "Corner": [(0, 0), (0, 8), (5, 15)],
    "Flat": [(0, 0),(0, 2), (5, 2)],
    "Verts": [(0, 0), (0, 30)],
    "Post": [(0, 0), (0, 8), (5, 15)],
    "Out": [(0, 0), (0, 5), (10, 5)],
    "Dig": [(0, 0), (0, 10), (10, 10)],
    "Bubble": [(0, 0), (2, -1), (7, 0)],
    "Hitch": [(0, 0), (0, 6), (1, 5)],
    "Comeback": [(0, 0), (0, 10), (-1, 9)],
    "Drag": [(0, 0), (-5, 3), (-15, 5)],
    "Step": [(0, 0), (0, 1)],
    "Stick": [(0,0), (0, 8), (-1, 7)]
}
concept_routs = {
    "Mesh" : ["Out", "Drag", "Drag", "Out"],
    "China": ["Hitch", "Corner"],
    "Drive": ["Drag","Seam",],
    "Dagger": ["Dig", "Fade", "Out"],
    "Verts": ["Verts", "Verts", "Verts", "Verts"],
    "Captain": ["Comeback", "Comeback", "Comeback" "Comeback"],
    "Hiker ": ["Hitch", "Hitch", "Hitch", "Hitch"],
    "Pinto": ["Post", "Dig", "Out"],
    "Pipes": ["Drag", "Post", ],
    "Twig": ["Fade", "Stick"],
    "Dragon": ["Verts", "Verts", "Verts", "Verts"],#noch nicht fertig \/
    "Captain": ["Comeback", "Comeback", "Comeback" "Comeback"]
}
def generate_playcall():
    Formation_num = random.randint(1, 6)
    Play_num = random.randint(1, 6)
    Playone_num = random.randint(1, 15)
    Playtwo_num = random.randint(1, 36)
    Playthree_num = random.randint(1, 35)
    Playall_num = random.randint(1, 4)

    # Directionsr_num= random.randint(1,8)
    # Directionsl_num = random.randint(1,8)
    # Hmotion_num = random.randint(1,4)
    # Wmotion_num = random.randint(1,3)
    # Smotion_num = random.randint(1,3)
    # Zmotion_num = random.randint(1,4)
    Direction = "-"
    # Playmotion_num = random.randint(1,6)

    Number = list(range(1, 37))

    Formations = {
        1: "Split",
        2: "Angle",
        3: "Lunch",
        4: "Spread",
        5: "Tri",
        6: "Brunch",
    }

    Playone = {
        1: "Slave",
        2: "Post",
        3: "Verts",
        4: "Corner",
        5: "Out",
        6: "Dig",
        7: "Hook",
        8: "Hitch",
        9: "Ouick Out",
        10: "Flat",
        11: "Slant",
        12: "Drag",
        13: "Bubble",
        14: "Seam",
        15: "Fade",
    }

    Playstwo = {  # Welche nur links und nur rechts
        1: "China",
        2: "Hiker",
        3: "Verts",
        4: "Pinto",
        5: "Pipes",
        6: "Twig",  # just two man
        7: "Mesh",  # full field concept?
        8: "Dragon",
        9: "Ohio",
        10: "Drive",
        11: "Slants",
        12: "Whip",
        13: "Whack",
        14: "Dagger",
        15: "Captain",
        16: "Dublin",
        17: "Verts Stop",
        18: "Outlaw",
        19: "Hit Em Up",  # 2 man possible??
        20: "Pylon",  # just 2 man ??
        21: "Ringo",
        22: "Ringo Pump",
        23: "Zander",
        24: "Zander Pump",
        25: "Murrey",
        26: "Murrey Pump",
        27: "Wilma",
        28: "Wilma Pump",
        29: "Linda",
        30: "Linda Pump",
        31: "Melody",
        32: "Melody Pump",
    }

    Playsthree = {
        1: "Hiker",
        2: "Verts",
        3: "Stick",  # as iso possible?
        4: "Pipes",
        5: "Mesh",  # full field concept?
        6: "Green Flip",  # just 3 man concept ??
        7: "Dagger",
        8: "Captain",
        9: "Dublin",
        10: "Verts Stop",
        11: "China Flip",  # same question as green flip??
        12: "Hit Em Up",  # 2 man possible??
        13: "Ringo",
        14: "Ringo Pump",
        15: "Zander",
        16: "Zander Pump",
        17: "Murrey",
        18: "Murrey Pump",
        19: "Wilma",
        20: "Wilma Pump",
        21: "Linda",
        22: "Linda Pump",
        23: "Melody",
        24: "Melody Pump",
    }

    Playall = {
        1: "Mesh",
        2: "Captain",
        3: "Verts",
        4: "Verts Stop",
        5: "",
    }
    dictionaries = {
        "Formations": Formations,
        "Playone": Playone,
        "Playstwo": Playstwo,
        "Playsthree": Playsthree,
        "Playall": Playall
    }
    for name, dic in dictionaries.items():
        with open(f"{name}.json", "w") as f:
            json.dump(dic, f, indent=4)


    Playconcept = [Playone, Playstwo, Playsthree, Playall]
    Conceptweight = [1, 1, 1, 1]
    Concept_num = random.choices(Playconcept, weights=Conceptweight, k=1)[0]

    Directions = {
        1: "31",
        2: "35",
        3: "49",
        4: "61",
        5: "51",
        6: "32",
        7: "36",
        8: "48",
        9: "62",
    }

    Hmotion = {
        1: "Hoop",
        2: "Hobbit",
        3: "Hammer",
        4: "",

    }
    hweights = [1, 1, 1, 10]
    Hmotion_num = random.choices(Number[:4], weights=hweights, k=1)[0]

    Wmotion = {
        1: "Wax",
        2: "Wap",
        3: "",
    }
    wweights = [1, 1, 10]
    Wmotion_num = random.choices(Number[:3], weights=wweights, k=1)[0]

    Smotion = {
        1: "Sail",
        2: "Sax",
        3: "",
    }
    sweights = [1, 1, 10]
    Smotion_num = random.choices(Number[:3], weights=sweights, k=1)[0]

    Zmotion = {
        1: "Zap",
        2: "Zip",
        3: "Zulu",
        4: "",
    }
    zweights = [1, 1, 1, 10]
    Zmotion_num = random.choices(Number[:4], weights=zweights, k=1)[0]

    Playmotion = {
        1: "Sugar",
        2: "S Jet",
        3: "W Jet",
        4: "Wunder",
        5: "Hexit",
        6: ""
    }
    playweights = [1, 1, 1, 1, 1, 10]
    Playmotion_num = random.choices(Number[:6], weights=playweights, k=1)[0]

    if Formation_num < 4:  # Left Playside
        while Playtwo_num > 30:  # if Linda etc.
            Playtwo_num = random.randint(1, 29)  # rechose numb
    Directions_num = random.randint(1, 9)
    Direction = Direction.replace("-", Directions[Directions_num])

    if Formation_num > 3:  # Right Playside
        while Playtwo_num < 31 & Play_num > 24:  # if Ringo etc.
            Playtwo_num = random.randint(1, 29)  # rechose numb
    Directions_num = random.randint(1, 9)  # directionsr_num zu directon wechseln möglich?
    Direction = Direction.replace("-", Directions[Directions_num])

    # \/ only one motion per rec( keep )
    # while (Hmotion[Hmotion_num] != "" and Playmotion[Playmotion_num].startswith("H"))or(Wmotion[Wmotion_num]!= "" and Playmotion[Playmotion_num].startswith("W"))or(Smotion[Smotion_num] != "" and Playmotion[Playmotion_num].startswith("S"))or(Zmotion[Zmotion_num] != "" and Playmotion[Playmotion_num].startswith("Z")):
    #   Playmotion_num = random.randint(1,6)

    Playdivision = random.choices(Number[:2], k=1)[0]

    if Playdivision == 1:
        if Formations[Formation_num] == "Tri" or "Angle" or "Lunch" or "Brunch":
            Playthree_num = random.choices(Number[:24], k=1)[0]
        Playone_num = random.choices(Number[:15], k=1)[0]
        Firstplay = Playsthree[Playthree_num]
        Secondplay = Playone[Playone_num]

        if Formations[Formation_num] == "Split" or "Spread":
            Playstwo_num1 = random.choices(Number[:32], k=1)[0]
        Firstplay = Playstwo[Playstwo_num1]
        Playstwo_num2 = random.choices(Number[:32], k=1)[0]
        Secondplay = Playstwo[Playstwo_num2]
    else:
        Playsall_num = random.choices(Number[:4], k=1)[0]
        Firstplay = Playall[Playall_num]
        Secondplay = ""
    Finalcall = [Formations[Formation_num], Direction, Hmotion[Hmotion_num], Smotion[Smotion_num], Wmotion[Wmotion_num],
                 Zmotion[Zmotion_num], Playmotion[Playmotion_num], Firstplay, Secondplay]
    Finalcall = " ".join(Finalcall)
    Final_call = Finalcall

    return Final_call
    return ["Slant","Corner","Flat"]

