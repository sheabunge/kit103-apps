"""
KIT103/KMA155 Programming Assignment 1: Sets
Submission script

Name: Shea Bunge
ID: 407095

Enter your answers to each question below, replacing None with the
code requested. Question 1 part a should be stored in ans['Q1 a']
and so on. You can use the show_answers() function from inside the
IPython console to show the result of your answers when you run
this script to evaluate all your answers.
A suggestion: Run the script first, then work out the answers in
the IPython interactive console before pasting them back here.
"""

ans = {}  # an empty dictionary of answers


def show_answers(show_all=True):
    """Prints the calculated answers to all questions.
    This function is included because it may be useful to you in
    checking your answers, but you are not required to use it.
    """
    for a in sorted(ans):
        if show_all or ans[a] is not None:
            print('%s: %s' % (a, str(ans[a]) if ans[a] is not None else 'unanswered'))


# Question 1: Set literals

ans['Q1 a'] = {2, 4, 6, 8, 10, 12}
ans['Q1 b'] = {'Bob', 'Alice', 'Donna', 'Charlie'}
ans['Q1 c'] = {'a', 'e', 'i', 'o', 'u'}

# Question 2: Set comprehensions

ans['Q2 a'] = {n * 4 for n in range(2, 11, 2)}
ans['Q2 b'] = {i ** 3 for i in range(1, 7)}
ans['Q2 c'] = {l for l in 'abracadabra'}

# Question 3: Relationships

# Given these definitions provide code to answer the questions from the assignment sheet.
mammals = {'cow', 'gorilla', 'human', 'kangaroo'}
aves = {'cormorant', 'eagle', 'emu'}
quadrupeds = {'cow', 'lizard'}
bipeds = {'cormorant', 'eagle', 'emu', 'gorilla', 'human', 'kangaroo'}
can_swim = {'cormorant', 'cow', 'human', 'kangaroo', 'lizard'}
can_fly = {'aeroplane', 'cormorant', 'eagle'}

ans['Q3 a'] = bipeds < mammals
ans['Q3 b'] = bipeds <= can_swim
ans['Q3 c'] = aves <= bipeds

# Question 4: Set membership

ans['Q4 a'] = mammals - can_swim
ans['Q4 b'] = can_fly & can_swim
ans['Q4 c'] = bipeds & can_swim - mammals

# Question 5: Combinations

# Given these definitions, generate the combinations requested in the assignment sheet.
colours = {'red', 'green', 'blue', 'yellow'}
vehicles = {'car', 'boat', 'rocket'}
speeds = {'slow', 'fast'}

ans['Q5 a'] = {(speed, vehicle) for speed in speeds for vehicle in vehicles}
ans['Q5 b'] = {(vehicle1, vehicle2) for vehicle1 in vehicles for vehicle2 in vehicles}
ans['Q5 c'] = {(speed, colour, vehicle) for speed in speeds for colour in colours for vehicle in vehicles}

# Question 6: Bags & Bitsets
# When checking these, note that parts (b)-(e) will look like normal decimal numbers,
# even though you will have entered binary literals in your answers to (b)-(d).
# A binary literal is just another way of expressing an integer value.

ans['Q6 a'] = {'cat': 2, 'hat': 1, 'sat': 3}
ans['Q6 b'] = 0b11000
ans['Q6 c'] = 0b01011
ans['Q6 d'] = 0b10011
ans['Q6 e'] = 0b11011

# End of answers
