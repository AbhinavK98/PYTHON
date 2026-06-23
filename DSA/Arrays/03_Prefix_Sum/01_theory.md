# Prefix Sum Pattern Theory

    This note explains the core idea behind **Prefix Sum Pattern** in beginner-friendly language.

    ## Why this pattern matters

    Interviewers test whether you can reduce repeated work.
    This pattern helps turn nested loops into linear scans in many cases.

    ## Core mental model

    - Start with a brute-force thought.
    - Identify repeated calculations.
    - Replace repetition using memory (hash map/prefix) or pointer movement.

    ## Recognition clues

    - Pair search, sum constraints, duplicate checks
    - Sorted array with left/right opportunities
    - Subarray or range query requests

    ## Questions in this folder

    - Running Sum of 1D Array (#1480)
- Find Pivot Index (#724)
- Range Sum Query - Immutable (#303)

    ## How to explain in interview

    1. Mention brute force first.
    2. State the bottleneck.
    3. Present optimized idea and invariant.
    4. Walk through one dry run.
    5. Share complexity with reason.
