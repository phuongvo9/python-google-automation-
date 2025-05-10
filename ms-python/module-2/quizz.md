1. Conditional Logic (if/elif/else)  
   – Principle: Branching lets your program choose one of several mutually‐exclusive paths at runtime.  
   – Why it matters: Using `if` / `elif` / `else` ensures every temperature range (below 0, 0–30, above 30) is handled exactly once, preventing gaps or overlaps.

2. Repeat‐Until Loops (while)  
   – Principle: A `while` loop repeats as long as a condition stays true, ideal for “try until success” scenarios.  
   – Why it matters: When you don’t know in advance how many guesses the player will need, a `while guess != secret:` loop keeps prompting until the correct answer.

3. Decision‐Per‐Event Handling (single if)  
   – Principle: Use a simple `if` to react once to a condition (e.g. obstacle encountered) before moving on.  
   – Why it matters: For one‐off checks (“is there an obstacle right here?”), a single `if` is clearer and more efficient than wrapping it in a loop.

4. Inspecting State (print statements & debugger)  
   – Principle: Observing program state is key to understanding and fixing behavior.  
   – Why it matters:  
     • Print statements are quick and language-agnostic—sprinkle them to log variable values.  
     • A debugger lets you pause execution, step line-by-line, and watch variables evolve without code changes.

5. Defensive Error Handling (try/except)  
   – Principle: Anticipate runtime errors and handle them gracefully so your program can continue.  
   – Why it matters: Wrapping division in `try: … except ZeroDivisionError:` catches the error, avoids a crash, and lets you recover or report it.

6. List Versatility (heterogeneous storage)  
   – Principle: Python lists can hold any mix of types—integers, strings, objects, even other lists.  
   – Why it matters: A game inventory can store swords (objects), potion counts (ints), and quest keys (strings) all in one structure.

7. Direct Access by Position (indexing)  
   – Principle: `my_list[i]` retrieves the element at zero-based position `i` in constant time.  
   – Why it matters: To fetch the third purchased item, simply do `order[2]`—no loops required.

8. Subset Extraction (slicing)  
   – Principle: `my_list[start:end]` returns a new list spanning positions `start` up to `end-1`.  
   – Why it matters: When analyzing large datasets, slicing lets you focus on a contiguous segment (e.g. reviews[100:200]) for batch processing or sampling.

9. Declarative Transformations (list comprehensions)  
   – Principle: `[expr(item) for item in my_list]` creates a new list by applying `expr` to each element.  
   – Why it matters: To standardize name formatting, you can write  
     ```python
     cleaned = [name.title() for name in raw_names]
     ```  
     which is shorter and often faster than a manual loop.

10. Queue‐Style Operations (append & pop)  
    – Principle: `append()` adds to the list’s end; `pop(0)` or `pop()` removes from front or back. Together they implement FIFO or LIFO behavior.  
    – Why it matters: For a task queue where new jobs go on the back and you process (pop) from the front, `append(job)` + `pop(0)` models real‐world queues simply with built-in methods.
