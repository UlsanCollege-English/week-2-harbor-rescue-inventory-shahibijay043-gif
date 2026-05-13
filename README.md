[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/HYC1dWeQ)
# Week 2 README Template
## Summary
The Harbor Rescue Inventory assignment practices basic Python list operations and problem-solving skills.  
The functions work with inventory data by searching, slicing, counting, and updating lists.  
This assignment helped build understanding of indexing, loops, conditions, and edge-case handling.  
The stretch challenge also practiced creating new lists without changing the original data.

## Approach
Use bullets to explain how each function works.

- `mission_snapshot`:
  - Returns the first and last item from the list.
  - Returns `(None, None)` if the list is empty.

- `cargo_window`:
  - Returns a section of the list using slicing.
  - Checks for invalid start positions or invalid sizes.

- `first_supply_index`:
  - Loops through the list to find the first matching target.
  - Returns `-1` if the target is not found.

- `supply_report`:
  - Counts how many times the target appears.
  - Tracks the first index where the target is found.

- `priority_load` (stretch):
  - Creates a new list with the urgent item added to the front.
  - Does not modify the original list.

## Complexity reasoning

| Function | Time complexity | Why |
|---|---|---|
| `mission_snapshot` | O(1) | Directly accesses the first and last elements |
| `cargo_window` | O(k) | Copies up to `size` elements into a new list |
| `first_supply_index` | O(n) | May need to check every item in the list |
| `supply_report` | O(n) | Iterates through the entire list once |
| `priority_load` (stretch) | O(n) | Creates a new list containing all original items |

## Edge-case checklist
Mark the cases you tested.

- [x] empty list
- [x] one-item list
- [x] target missing
- [x] repeated values
- [x] slice goes past end
- [x] size is zero
- [x] size is negative
- [x] original list unchanged in `priority_load`

## Assistance / Sources
List any help you used and what kind of help it gave.

- Person / tool / website:
  - ChatGPT
  - Help received:
    - Helped improve code readability, formatting, and documentation.

- Person / tool / website:
  - Python Documentation
  - Help received:
    - Used for understanding Python list slicing and loop behavior.