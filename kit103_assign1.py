"""
KIT103/KMA155 Programming Assignment 1: Sets
Submission script

Name: Replace with your name
ID: Replace with your student ID

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

ans['Q1 a'] = None
ans['Q1 b'] = None
ans['Q1 c'] = None

# Question 2: Set comprehensions

ans['Q2 a'] = None
ans['Q2 b'] = None
ans['Q2 c'] = None

# Question 3: Relationships

# Given these definitions provide code to answer the questions from the assignment sheet.
mammals = {'cow', 'gorilla', 'human', 'kangaroo'}
aves = {'cormorant', 'eagle', 'emu'}
quadrupeds = {'cow', 'lizard'}
bipeds = {'cormorant', 'eagle', 'emu', 'gorilla', 'human', 'kangaroo'}
can_swim = {'cormorant', 'cow', 'human', 'kangaroo', 'lizard'}
can_fly = {'aeroplane', 'cormorant', 'eagle'}

ans['Q3 a'] = None
ans['Q3 b'] = None
ans['Q3 c'] = None

# Question 4: Set membership

ans['Q4 a'] = None
ans['Q4 b'] = None
ans['Q4 c'] = None

# Question 5: Combinations

# Given these definitions, generate the combinations requested in the assignment sheet.
colours = {'red', 'green', 'blue', 'yellow'}
vehicles = {'car', 'boat', 'rocket'}
speeds = {'slow', 'fast'}

ans['Q5 a'] = None
ans['Q5 b'] = None
ans['Q5 c'] = None

# Question 6: Bags & Bitsets
# When checking these, note that parts (b)-(e) will look like normal decimal numbers,
# even though you will have entered binary literals in your answers to (b)-(d).
# A binary literal is just another way of expressing an integer value.

ans['Q6 a'] = None
ans['Q6 b'] = None
ans['Q6 c'] = None
ans['Q6 d'] = None
ans['Q6 e'] = None

# End of answers
