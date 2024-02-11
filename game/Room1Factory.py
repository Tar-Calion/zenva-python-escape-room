from game.Room import Room
from game.RoomObject import RoomObject


class Room1Factory:
    def create_room(self):
        return Room("379", [
            # The objects are: a painting, a statue of an angel, a fireplace, a comfy chair and a plant.

            # There are six clues, one for each digit of the code and one for the position of the digit in the code.
            # 1. Touching the comfy chair reveals a peculiar coin with value of 3 pesos. (hints at the digit "3")
            # 2. Looking at the painting reveals a small plaque with the inscription "The three primal gods" (hints at "3" being the first digit).
            # 3. Touching the angel statue reveals a roman numeral "VII" at its back. (hints at the digit "7")
            # 4. Looking at the fireplace reveals a book with the title "After the gods came the angels" (hints at "7" being the second digit).
            # 5. Smelling the plant makes the player sneeze and a small piece of paper falls from the pot. The paper has the number "9" written on it. (hints at the digit "9")
            # 6. Looking at the chair reveals a prominent plague with the inscription "Use to wind down after 9 p.m. before going to bed" (hints at "9" being the last digit).
            RoomObject("painting",
                       "A majestic painting depicts three imposing figures, their gazes stern and unyielding. A plaque whispers their forgotten title: 'The Three Primal Gods'",
                       "The canvas yields slightly under your touch, the subtle texture of brushstrokes hinting at the artist's hand",
                       "The faint scent of aged oil and pigments lingers in the air, a testament to the artwork's passage through time"),

            RoomObject("statue of an angel",
                       "Graceful and serene, the angel's marble form seems to emanate a quiet peace. Yet, something about its posture feels subtly... expectant",
                       "The cool touch of the statue sends a slight shiver down your spine. As you turn it, a hidden detail catches your eye: the Roman numeral 'VII' etched onto its back",
                       "A whiff of ancient dust stirs as you move the statue, a timeless scent that speaks of long-forgotten corridors"),

            RoomObject("fireplace",
                       "The fireplace crackles, its warmth a defiant contrast to the room's chill. On the mantle lies a leather-bound book, its title worn but still legible: 'After the Gods Came the Angels'",
                       "The heat radiates intensely. You withdraw your hand quickly",
                       "The room smells of wood and ash, a comforting and familiar scent"),

            RoomObject("comfy chair",
                       "This chair beckons with its plush cushions and worn upholstery. A faded inscription adorns its back: 'Use to wind down after 9 p.m. before going to bed'",
                       "The fabric yields luxuriously beneath your touch, inviting you to sink in. As you do, something hard jabs into your side - a peculiar coin embossed with the value of 3 pesos",
                       "The scent of old fabric and a hint of something sweeter, perhaps vanilla or old pipe tobacco, fills your nostrils"),

            RoomObject("plant",
                       "A vibrant splash of green against the room's muted tones, this plant seems strangely out of place. Its broad leaves unfurl languidly",
                       "The leaves rustle against your skin, their textures surprisingly varied. Some feel smooth, others almost velvety",
                       "A sharp, peppery scent tickles your nose, making you want to sneeze. And as you do, a small piece of paper flutters from the pot, the number '9'  boldly scrawled upon it")


        ])
