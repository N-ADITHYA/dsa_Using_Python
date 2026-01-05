# Leetcode Practice Repository

This repository contains my structured and test-driven solutions to LeetCode problems.
Each problem is solved locally, validated with custom test cases, and then pushed to GitHub.

## Why this Repository?
We solve problems on LeetCode that's fine. But for me, I wanted to go beyond just getting “Accepted”.
I got curious about How LeetCode tests our code, how do they validate test cases.
So I started writing solutions locally, creating my own driver code, creating custom test cases, verifying correctness.

This repository is the result of that curiosity, combining problem solving with real-world testing habits.

# Basic folder structure is 

Each LeetCode problem follows a consistent and minimal structure.

```text
problem-name/
└── problem-name/
    ├── solution.py        # Core solution logic
    ├── driver_code.py     # Executes the solution locally
    └── test_cases.json    # Custom test cases
```

### File Description

- **`solution.py`**  
  Contains the main solution implementation, focused only on logic.

- **`driver_code.py`**  
  Imports the solution and runs it against the test cases to validate correctness.

- **`test_cases.json`**  
  Stores multiple input–output test cases, including edge cases, in a structured format.

## Data Structure Construction

Some LeetCode problems require complex data structures as input rather than simple arrays or values.

For such cases, additional helper logic is used to:
- Convert lists into **Linked Lists**
- Convert lists into **Trees** (Binary Trees, BSTs, etc.)

These utilities help replicate how LeetCode internally constructs inputs, enabling accurate local testing and validation of solutions.

---

This repository is a work in progress and will continue to evolve as I solve more problems, explore edge cases, and improve code quality.

Consistent learning, one problem at a time. 
Happy coding!

