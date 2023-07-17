# Represent the following information in knowledge base and ask the questions is ram smiles?
# 1. All people who are graduating are happy
# 2. Happy people smile.
# 3. Ram is graduating .

# Represent the following information in knowledge base and ask the questions "Is angle B is equal to angle C"
# 1. If triangle is equilateral then it is isosceles.
# 2. If traingle is isosceles then two sides AB and AC are equal.
# 3. If AB and AC are equal then angle B and C are equal.
# 4. ABC is an equilateral triangle


# Here, prolog is used for knowledge representation
# symbol used in prolog
# ,   meaning and
# ;  meaning or
# :-  meaning only if
# not  meaning  not
# code for 2nd questions.
# isos(ABC):-euqi(ABC).
# equal(ab,ac):-isos(ABC).
# equal(b,c):-equal(ab,ac).
# euqi(ABC).

#swi prolog code for this is

#graduating(ram).
#happy(x):-gradudating(x).
#smile(x):-happy(x).

# equilateral(ABC).
# isosceles(x):- equilateral(x).
# equal_sides(AB, AC):- isosceles (_).
# equal_angles(B,C):- equal_sides(_,_).

# to check the condition the code is 
# smile(ram).
# equal_angles(B,C).
