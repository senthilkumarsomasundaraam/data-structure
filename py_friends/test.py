from friends import Friends   # project is the folder name

friends_dir = {
    "a": {"b", "c"},
    "b": {"a", "c"},
    "c": {"a", "b"}
}

for pair in Friends(friends_dir):
    print(pair)
