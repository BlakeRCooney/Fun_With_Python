from random import choice

questions = ["Why do farts stink?: ", "Where do babies come from?: ", "Why do you look like doo-doo?: ", "Why is the sky blue?: ", "Where are all the Dinosaurs?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()

print("Oh... Okay")

# This was a funny program to show the way user input can determine various outcomes. 
# There is so much more that can be done with this, but I wanted to keep it short and simple.
