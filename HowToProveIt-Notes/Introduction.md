---
title: "Chapter 1: Introduction"
author: "Chayce"
date: "/today"
geometry: margin=1in
fontsize: 11pt
header-includes:
  - \usepackage{amsmath}
  - \usepackage{amssymb}
---
What is Mathematics? How Cliche...

- In High School, most problems focus on finding a solution to a __numerical__ question (i.e. solve for x)

- College math expands this to dealing with sets of solutions, functions, and grander mathematical objects 
The connective tissue of these endeavors is **deductive reasoning**. 

**Deductive Reasoning** is usually showcased with a proof. This book and these notes will help develop the skill of writing and reading proofs and understanding mathematical reasoning.

Here a few popular examples using prime numbers

- Recall: An Integer greater than 1 is said to be **prime** if it cannot be written as a product of two smaller positive integers. If it *can* be written as a product of two prime integers, then it is **composite** 
->  EX: 6 is composite, since 6 = 2 * 3, but 7 is prime (has no other divisors besides itself and 1)
Figure 1.1 (Table of showing if numbers, n are Prime AND 2^n - 1 are prime)

| n   | Is n prime?   | 2^n - 1 | Is 2^n - 1 prime? |
| :-- | ------------- | ------- | ----------------- |
| 2   | Y             | 3       | Y                 |
| 3   | Y             | 7       | Y                 |
| 4   | N: 4 = 2 * 2  | 15      | N: 15 = 3 * 5     |
| 5   | Y             | 31      | Y                 |
| 6   | N: 6 = 2 * 3  | 63      | N: 63 = 7 * 9     |
| 7   | Y             | 127     | Y                 |
| 8   | N: 8 = 2 * 4  | 255     | N: 255 = 15 * 17  |
| 9   | N: 9 = 3 * 3  | 511     | N: 511 = 7 * 73   |
| 10  | N: 10 = 2 * 5 | 1023    | N: 1023 = 31 * 33 |
We see a pattern than appears as than 2^n - 1 is prime in precisely the cases in which n is prime!

We do not know if this pattern is the rule or just an observation from our (extremely) sample n's. Since this is still a guess, we call these guesses: **Conjectures**.
For this example we establish these two Conjectures:

1. Conjecture 1: Suppose n is an integer larger than 1 and n is prime. Then 2^n - 1 is prime
2. Conjecture 2: Suppose n is an integer larger than 1 and n is not prime. Then 2^n -1 is not prime (composite)

Immediately following for n = 11, provides a counterexample to our conjecture 1.

11 is prime but 2^11 - 1 = 2047 = 23 * 89, so 2^11 - 1 is composite.
The EXISTENCE of even just one counterexample shatters correctedness.
Even so, both n = 23 and n = 29 are other counterexamples as can be seen below

| n   | is n prime? | 2^n - 1   | is 2^n - 1 prime?            |
| --- | ----------- | --------- | ---------------------------- |
| 23  | Y           | 8388607   | No: 8388607 = 47 * 178481     |
| 29  | Y           | 536870911 | No: 536870911 = 2089 * 256999 |
For Future Conventions, we will utilize LaTeX where applicable
$$ A \cdot B = 0 $$
However, no number up to 30 serves as a counter to conjecture 2.
Could this mean its true? it could be the case that a counterexample is a number greater then 30 but this is tedious and inefficient. Therefore we must *prove* it to be true. (And it turns out to be true)

<u>Proof of Conjecture 2</u> 
Since n is not prime, there are positive integers a and b such that $a < n$, $b < n$, and $n = ab$.
Let
$$ x = 2^b - 1 $$ 
and 
$$ y = 1 + 2^b + 2^{2b} + ... + 2^{(a-1)b}. $$ 
Then 
$$ xy = (2^b - 1) \cdot (1 + 2^b + 2^{2b} + \dots + 2^{(a-1)b}) $$ 
$$ = 2b \cdot (1 + 2^b + 2^{2b}+ \dots + 2^{(a-1)b}) - (1 + 2^b + 2^{2b}+ \dots + 2^{(a-1)b})$$
$$ = (2b + 2^{2b} + 2^{3b}+ \dots + 2^{ab}) - (1 + 2^b + 2^{2b}+ \dots + 2^{(a-1)b}) $$
$$ = 2^{ab} - 1 $$
$$ = 2^n - 1. $$

Since b < n, we can conclude that $x = 2^b-1  < 2^n- 1$.
Also, since $ab = n > a$, it follows that $b > 1$. Therefore, $x = 2^b - 1 > 2^1 - 1 = 1$, so $y < xy = 2^n - 1$. Thus, we have shown that $2^n - 1$ can be written as the product of two positive integers x and y, both of which are smaller than $2^n -1$, so $2^n - 1$ is not prime.

Since the conjecture has been proven, we can call it a theorem.

The 'secret' to this proof, lies with the notion that if n is any integer larger than 1 that can be written as a product of two smaller positive integers a and b, then the proof fives a method of writing 2^n - 1 as a product of two smaller positive integers x and y. This, if n is not prime, then $2^n - 1$ must also not be prime.
