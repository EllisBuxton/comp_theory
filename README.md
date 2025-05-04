# Computational Theory Implementations

This repository contains implementations of various computational theory concepts and algorithms in Python, organized as a series of tasks in a Jupyter notebook.

## Context and Purpose

This project was created to demonstrate fundamental concepts in computational theory, cryptography, and computer science algorithms through practical Python implementations. The tasks progress from basic bit manipulations to more complex implementations like Turing machines and cryptographic principles.

These implementations serve as educational resources for:
- Computer Science students studying algorithms and theoretical foundations
- Developers interested in cryptography fundamentals
- Anyone looking to understand computational complexity through hands-on examples
- Those studying the mathematical underpinnings of modern computing

## Overview

The tasks.ipynb notebook implements several key algorithms and concepts from computer science theory, cryptography, and computational mathematics:

### Task 1: Binary Representations
- `rotl`: Rotate bits left in 32-bit unsigned integers
- `rotr`: Rotate bits right in 32-bit unsigned integers
- `ch`: Choose bits based on selector
- `maj`: Majority vote of bits

### Task 2: Hash Functions
- Implementation of the hash function from The C Programming Language (K&R)
- Analysis of collision rates and hash distribution

### Task 3: SHA256 Padding
- Calculation and visualization of the padding applied in SHA256 hashing
- Implementation follows the NIST Federal Information Processing Standards 

### Task 4: Prime Numbers
- Sieve of Eratosthenes for efficiently finding all primes up to a limit
- Trial Division method for primality testing
- Performance comparison between the two approaches

### Task 5: Binary Representations of Irrational Numbers
- Calculation of binary fractional parts of square roots of prime numbers
- Analysis of bit distribution patterns

### Task 6: Proof of Work
- Finding English words with maximum leading zero bits in their SHA256 hash
- Implementation of the core concept behind cryptocurrency mining

### Task 7: Turing Machine
- Implementation of a binary incrementer as a Turing Machine
- Visualization of the step-by-step execution process
- Covers state transitions, tape manipulation, and halting conditions

### Task 8: Computational Complexity
- Analysis of bubble sort complexity through empirical testing
- Distribution of comparison counts across all possible input permutations
- Verification of theoretical best, worst, and average case complexities

## Educational Value

Each task is extensively documented with:
- Theoretical background and explanations
- Step-by-step implementation details
- Visualizations and test cases
- Performance analysis where applicable

The code is written to be readable and educational rather than optimized for production use.

## Research References

The implementations reference several academic resources, including:
- The Handbook of Applied Cryptography
- The Art of Computer Programming by Donald Knuth
- NIST Standards for Secure Hash Algorithms
- Introduction to the Theory of Computation by Michael Sipser
- Introduction to Algorithms (CLRS)

## Getting Started

To run these implementations:

1. Clone this repository
2. Open `tasks.ipynb` in Jupyter Notebook or Jupyter Lab
3. Execute the cells in order to see the implementations and their analyses

## Requirements

- Python 3.6+
- Jupyter Notebook
- Standard Python libraries (hashlib, itertools, etc.)