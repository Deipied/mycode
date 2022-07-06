#!/usr/bin/env python3

classinfo = {
    "all": [
        {
            "name": "Zach",
            "skill level": "wondrous",
            "spirit animal": "Alpaca",
            "super power": "Structure Weakening",
        },
        {
            "name": "Aaron",
            "skill level": "admirable",
            "spirit animal": "Donkey",
            "super power": "Super Strength",
        },
        {
            "name": "Andy",
            "skill level": "amazing",
            "spirit animal": "Goat",
            "super power": "Weather Control",
        },
        {
            "name": "Asif",
            "skill level": "astonishing",
            "spirit animal": "Guinea pig",
            "super power": "Flight",
        },
        {
            "name": "Brent",
            "skill level": "awesome",
            "spirit animal": "Horse",
            "super power": "X-ray Vision",
        },
        {
            "name": "Christopher",
            "skill level": "brilliant",
            "spirit animal": "Pig",
            "super power": "Helicopter Propulsion",
        },
        {
            "name": "Cory",
            "skill level": "cool",
            "spirit animal": "Rabbit",
            "super power": "Invisibility",
        },
        {
            "name": "Ebrima",
            "skill level": "enjoyable",
            "spirit animal": "Water buffalo",
            "super power": "Immobility",
        },
        {
            "name": "Franco",
            "skill level": "excellent",
            "spirit animal": "Chicken",
            "super power": "Immutability",
        },
        {
            "name": "Frank",
            "skill level": "fabulous",
            "spirit animal": "Duck",
            "super power": "Invulnerability",
        },
        {
            "name": "Greg",
            "skill level": "fantastic",
            "spirit animal": "Goose",
            "super power": "Jet Propulsion",
        },
        {
            "name": "Hoon",
            "skill level": "fine",
            "spirit animal": "Pigeon",
            "super power": "Matter Ingestion",
        },
        {
            "name": "JC",
            "skill level": "incredible",
            "spirit animal": "Turkey",
            "super power": "Mobile Invulnerability",
        },
        {
            "name": "Joey",
            "skill level": "magnificent",
            "spirit animal": "Aardvark",
            "super power": "Muscle Manipulation",
        },
        {
            "name": "Jordan",
            "skill level": "marvelous",
            "spirit animal": "Aardwolf",
            "super power": "Nail Manipulation",
        },
        {
            "name": "LB",
            "skill level": "outstanding",
            "spirit animal": "Elephant",
            "super power": "Needle Projection",
        },
        {
            "name": "Mabel",
            "skill level": "phenomenal",
            "spirit animal": "Leopard",
            "super power": "Organic Constructs",
        },
        {
            "name": "Pat",
            "skill level": "pleasant",
            "spirit animal": "Albatross",
            "super power": "Prehensile Hair",
        },
        {
            "name": "Shon",
            "skill level": "pleasing",
            "spirit animal": "Alligator",
            "super power": "Prehensile Tail",
        },
    ]
}

name = classinfo['all'][11]['name']
print(name)
spirit= classinfo['all'][11]['spirit animal']



def part2():
    print("My name is "+name+" and my spirit animal is "+spirit)

part2()

def part3():
    vowel = ['a','e','i','o','u']
    aan = ''
    for person in classinfo['all']:
        if person['skill level'][0] in vowel:
            aan = 'an'
        else:
            aan = 'a'
        print(f"{person['name']}, {aan} {person['skill level']} {person['spirit animal']} of a programmer, possesses a {person['super power']} factor for moonlighting as a superhero!")

part3()
