numbers = [1, 3, 5]
squares = [x * 2 for x in numbers]

# -- Dealing with strings --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)


# -- Can make a new list of friends whose name starts with S --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)

# -- List comprehension creates a _new_ list --

friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]  # same as above

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), " starts_s: ", id(starts_s))


# -- Can make a new list of friends whose name not starts with S -- @Roxana

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S") == False]

print(starts_s)


# Other method
song = "cold, cold heart"

# replacing 'cold' with 'hurt'
print(song.replace("cold", "hurt"))

song = "Let it be, let it be, let it be, let it be"

# replacing only of 'let'
print(song.replace("let", "don't let", 2))

ls = ["Let it be", "let it be", "let it be", "let it be"]
l_new = [l.replace("let", "don't let") for l in ls]
print(l_new)
print(",".join(l_new))
