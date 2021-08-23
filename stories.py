class Story:

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    "Christmas",
    "A Christmas Tale",
    ["Place", "Noun", "Verb", "Adjective", "PluralNoun"],
    """One time, my dad waited till my three {PluralNoun}, and I had gone to bed on Christmas Eve in {Place}, then he shouted, "I don't care who you are, {Adjective} man, get that {Noun} off my roof." We were all up telling Dad not to {Verb} at Santa."""
)

story2 = Story(
    "College",
    "The Send Off",
    ["Place", "Noun", "Exclamation", "Adjective", "PluralNoun"],
    """When I walked out to the {Noun} to leave for {Place}, my dad yelled "{Exclamation}" from the front door.

    I turn around.

    He takes this {Adjective} box of magnum-sized {PluralNoun} and throws them at me as hard as he can. They hit me in the nose as he yells, "CARE PACKAGE" and then ran inside laughing.

    That is very flattering dad, but I don't have much use for them."""
)

story3 = Story(
    "Matinee",
    "The Show",
    ["Clothing", "Noun", "Adjective", "Adjective2"],
    """One day, my dad answered the door in his {Clothing} at 8 am. The salesman was obviously {Adjective}. After he left, my mom was {Adjective2} and asked why he did that. My dad said, "If these "people" don't want a {Noun}, they shouldn't of come for the matinee."""
)

story4 = Story(
    "Blender",
    "The Blender",
    ["Adjective", "Place", "Noun", "Verb", "Noun2", "TypeOfLiquid", "GenderPlural", "Noun3", "Noun4"],
    """Before I graduated high school, my dad sat me down to have a serious conversation about socializing in {Place}. It turned into him telling me a bunch of crazy {Adjective} stories. Suggesting that the best way to make friends is to own a {Noun2} with a 100ft extension cord because his friends would go outside to {Verb} basketball. He'd bring his {Noun} out with them and make {TypeOfLiquid}.
    "We met so many {GenderPlural} because of that {Noun3}, people like the guy with the {Noun4}." """
)

story5 = Story(
    "Movie Rental",
    "Amnesia",
    ["MovieTitle", "MovieTitle2", "Place", "Letter"],
    """One time, I asked my dad to rent {MovieTitle} for me from the good ol' {Place} up the street. He rented {MovieTitle2} because he could only remember it started with a {Letter}."""
)

story6 = Story(
    "Taking Candy From A Baby",
    "Candy Theft",
    ["Food", "Noun", "Food2", "VerbEndingIn_ING", "Noun2", "Verb"],
    """One time, my dad literally took {Food} from a {Noun}. A two year old held up a {Food2} and my dad assumed the kid was {VerbEndingIn_ING} it to him. After taking it and walking away, he realized the {Noun2} probably just wanted to {Verb} it to him"""
)

story7 = Story(
    "Plane, Trains, And Plantains",
    "Plane Crash",
    ["Device", "PluralNoun", "Vehicle", "PartOfBody", "Verb", "Adjective", "PluralNoun2"],
    """One time, my dad took my brother's {Device} and had us and about ten {PluralNoun} in the neighborhood convinced that we had picked up a signal from a {Vehicle} that was crashing towards the Earth. We were running up and down the streets for an hour with our {PartOfBody} on the sky, listening as the "pilot" tried to {Verb} someone for help. Dad's windows were open, so we eventually caught on to the {Adjective} laughter echoing between the {PluralNoun2} after every mayday."""
)

story8 = Story(
    "Da Birdy Bird Man",
    "Ornithologist",
    ["Number", "Place", "Animal", "AnimalPlural", "Verb", "VerbEndingIn_ING", "PluralNoun", "Adjective"],
    """One time, my dad made me drive {Number} hours from home to visit a {Place}. He then began taking pics of the {Animal} there. Just one problem, the {AnimalPlural} were plastic. Turns out the flocks had stopped {VerbEndingIn_ING}. They put up plastic birds for {PluralNoun}. The funniest part was how long it took him to listen to me telling him they were {Adjective}."""
)




stories = {s.code: s for s in [story1, story2, story3, story4, story5, story6, story7, story8]}