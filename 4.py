friends = set()
friends.add("Viivi")
friends.add("Ville")
print(friends)
friends.add("Viivi")
print(friends)
if not "Mary" in friends:
    friends.add("Olga")
else:
    friends.add("Ahmed")
print(friends)