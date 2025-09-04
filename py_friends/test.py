from friends import Friends   # project is the folder name
from typing import Dict, Set, List, Tuple

def make_friends_directory(friend_list: List[Tuple[str, str]]) -> Dict[str, Set[str]]:
    """
    Construct a dictionary mapping each person to a set of their friends.
    Args:
        friend_list: List of tuples representing friendships, e.g. [("x", "y"), ("x", "z")]
    Returns:
        Dictionary where keys are person names and values are sets of their friends.
    """
    friends_dir: Dict[str, Set[str]] = {}
    
    for a, b in friend_list:
        # Add b to a's friends
        if a not in friends_dir:
            friends_dir[a] = set()
        friends_dir[a].add(b)
        
        # Add a to b's friends
        if b not in friends_dir:
            friends_dir[b] = set()
        friends_dir[b].add(a)
    
    return friends_dir
# Example usage
#-------------------------------------------------------
friends_dir = {
    "a": {"b", "c"},
    "b": {"a", "c"},
    "c": {"a", "b"}
}
#-------------------------------------------------------
for pair in Friends(friends_dir):
    print(pair)
# Call make_friends_directory with a sample friend list
friend_list = [("x", "y"), ("x", "z"), ("y", "z")]
friends_dir1 = make_friends_directory(friend_list)
#print(friends_dir1)

result = list(Friends(friends_dir1))
print(result)