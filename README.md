DSC 395T – Algorithms and Data Structures
Programming Assignment #1: Friend of a Friend Group Project

This project practices Python sequence types (list, dict, tuple, set, str) and programming constructs by analyzing a dataset of friendship relations (pairs of characters appearing together in Star Wars scenes). Only the Python standard library and pytest may be used.

Tasks
---------------
1) Load Pairs
2) Implement load_pairs() to read a text file of friendship pairs.
3) Returns a list of 2-tuples (may include duplicates).

Friendship Directory
---------------
1) Implement make_friends_directory() to convert the list of tuples into a dictionary.
2) Keys = person, Values = set of that person’s friends.
3) Friendships are bidirectional, and self-pairs (x, x) are ignored.

Friend Counts
---------------
1) Implement find_all_number_of_friends() to return a sorted list of (person, number_of_friends).
2) Sorted by descending number of friends, ties broken by ASCII order.

Team Roster
---------------
1) Implement make_team_roster() to compute a person’s team = friends + friends-of-friends.
2) Return a team roster string (names joined with _).
----------------------------------------------------------------------------------------------
Smallest Team

1) Implement find_smallest_team() to return the roster string of the smallest team.
2) If tied, return ASCII-order first.

Iterator Class
1) Fix the provided Friends class (py_friends/friends.py) to correctly iterate (ASCII order) over unique friendship relations.

Optional Karma
1) Implement generate_friends() (a generator) that replicates the iterator functionality.

Testing

Run tests with:
1) pytest tests/test_friends.py::test_load_pairs_simple

---- End ---