# Tuples are also collection of various data types.
# Only the difference is that they cannot be updated. New edited tuple out of the existing one can be created.

animals = ("monkey", "cat", "dog", "parrot", "snake", "elephant")
pets = animals[1:4]
sounds = ("meow", "bark", "squawk")

# Two tuples also can be zipped using zip() function.

how_pets_sound = zip(pets, sounds)

for number, (pet, sound) in enumerate(how_pets_sound, 1):
    print(str(number) + ")", pet, sound + "s")
