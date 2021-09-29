from typing import Callable
from typing import List


def apply_to_each(values: List[int], function: Callable) -> None:
    """Mutate the input list by applying the provided function to each of its elements."""
    # TODO: Add the source code lines from page 105 of the textbook


# create the list of values
values = [1, -2, 3.33]

# display the list before any transformation
print(f"Values before transformations: {values}")

# apply the abs function
apply_to_each(values, abs)

# display the list after abs transformation
print(f"Values after applying abs: {values}")

# apply the int function
apply_to_each(values, int)

# display the list after int transformation
print(f"Values after applying int: {values}")

# apply the int function
apply_to_each(values, lambda x: x*x)

# display the list after int transformation
print(f"Values after applying squaring: {values}")
