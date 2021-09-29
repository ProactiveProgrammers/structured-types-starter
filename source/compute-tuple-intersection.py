from typing import Any
from typing import Tuple


def compute_intersection(tuple_one: Tuple[Any, ...], tuple_two: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """Return a tuple containing the elements in both input tuples."""
    # TODO: Add the source code lines from page 91 of the textbook
    # TODO: The following line is a placeholder you should delete it
    return ()


# create two distinct tuples with some overlapping values
first_tuple = (1, "a", 2)
second_tuple = ("b", 2, "a")

# display the contents of the tuples
print(f"The first tuple: {first_tuple}")
print(f"The second tuple: {second_tuple}")

# compute the set intersection of the two tuples
# --> first_tuple intersects with second_tuple
intersection_tuple_one = compute_intersection(first_tuple, second_tuple)
# --> second_tuple intersects with first_tuple
intersection_tuple_two = compute_intersection(second_tuple, first_tuple)

# display a blank line
print()

# display the two different set intersections
print(f"The first intersection tuple: {intersection_tuple_one}")
print(f"The second intersection tuple: {intersection_tuple_two}")
