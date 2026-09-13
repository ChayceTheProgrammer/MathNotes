PREFACE

Mathematical Proofs are what bind **theory** to the **structure** of mathematics. Early proof techniques are used in a high school geometry course where proofs are structured as a numbered list of statements and reasons which deemed to be very restrictive for proper use cases with non-geometric studies.

Early computer science researchers proposed a similar sequential of instructions for computer programs i.e. a numbered list of instructions.
-> Currently, computer scientists use programming languages to encourage 'structured programming'

This book (How To Prove It - A Structured Approach 3rd Edition), will serve as a way to learn 'structured proving'

<u>Structured Programming</u> is a method of instructing a computer how to complete a specified task with pieces of syntax like 'if-else' conditionals or '(do) while loops'. These structures are combined not only sequentially but *nested* within another.

1. For Example: \
do ( \
If -**Condition**- \
	{Instruction}\
else\
	{Alternative Instruction} \
) while -**Loop Condition**-

Using **Indentation** is a convention used in CS to display the underlying structure of a program.
Thus method display where the structure is relaxed in favor of clarity is called **Pseudocode**.

Proofs in Math, are similarly:

1. For Example: a statement of the form: "If P then Q" is noted as a 'suppose-until' which means 'suppose P as true *until* we are able to reach the conclusion that Q is true'. Once that is accomplished, we retract the supposition of : 'assuming P is true' and conclude the original statement 'If P then Q' is in fact true.
2. Consider the example: "For all x, P(x)". Declare x as an arbitrary object and then prove P(x). Once we show that P(x) is true, we retract the declaration of x and reduce the final statement to simply: "For all x, P(x)" is true.
More complex statements, these type of arguments are combined in one after each other or nesting as well, similar to programming languages
3. Final Example: Prove the statement: "For all x, if P(x), then Q(x)", works most structurally when nesting a 'suppose until' struct within a 'for arbitrary x prove' structure 

Let x be arbitrary \
$\quad$ Sps P(x) is true \
 $\qquad$ {Proof of Q(x) } \
$\quad$ Thus, if P(x) then Q(x) \
Thus, for all x, if P(x) then Q(x)

Indentation here shows the structure of the proof but the semantics are flexible
Mathematicians don't conventionally structure proofs as such but they are effective at showing how an argument flows.

To stop the use of indentation and the rigidity, we use the conventions "Let x be arbitrary" and "Suppose P" as way to introduce the 'for arbitrary x prove' and 'suppose-until' proof structures.

Early Chapters focus more on forms these mathematical statements take to familiarize the student with working with these structures.
Ch1 discusses logical connectives
Ch2 goes over quantifiers
Ch1 + Ch2 motivate the foundation of set theory 
Ch3 covers proving techniques in a systematic way, by showing various forms math statements can take and the appropriate proof structure of each form. Early on, the proofs will seem trivial but will become more mathematically interesting
Ch4 + Ch5 focuses on relations and functions, and serves as the practice for utilizing ch3 tech, and showcases fundamental concepts used in all branches in mathematics
Ch6 goes over the usage of *mathematical induction* which is used advanced math and computer science
Ch7 introduces number theory
Ch8 discussed infinite cardinalities

Every Section ends with a set of exercises where the asterisk* marked have solutions and hints in the appendix.
- Problems marked with P.D can be completed with Proof Designer Software

This 3rd Edition includes the new chapter on number theory and 150 more exercises. Section on reflexive, symmetric, and transitive closures of relations are moved from Ch4 (still given in exercises in section 4.4) to Ch5 where they are used when concluding closures on sets under functions.

