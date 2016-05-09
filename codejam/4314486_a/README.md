https://code.google.com/codejam/contest/4314486/dashboard#s=p0&a=0

Problem A. Senate Evacuation
-----------------------

#### Problem
A small fire started in the senate room, and it needs to be evacuated!

There are some senators in the senate room, each of whom belongs to of one of N political parties. Those parties are named after the first N (uppercase) letters of the English alphabet.

The emergency door is wide enough for up to two senators, so in each step of the evacuation, you may choose to remove either one or two senators from the room.

The senate rules indicate the senators in the room may vote on any bill at any time, even in the middle of an evacuation! So, the senators must be evacuated in a way that ensures that no party ever has an absolute majority. That is, it can never be the case after any evacuation step that more than half of the senators in the senate room belong to the same party.

Can you construct an evacuation plan? The senate is counting on you!

#### Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of two lines. The first line contains a single integer N, the number of parties. The second line contains N integers, P1, P2, ..., PN, where Pi represents the number of senators of the party named after the i-th letter of the alphabet.

#### Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the evacuation plan. The plan must be a space-separated list of instructions, in the order in which they are to be carried out, where each instruction is either one or two characters, representing the parties of the senators to evacuate in each step.

It is guaranteed that at least one valid evacuation plan will exist. If multiple evacuation plans are valid, you may output any of them.

#### Limits

1 ≤ T ≤ 50.
No party will have an absolute majority before the start of the evacuation.
1 ≤ Pi ≤ 1000, for all i.

**Small dataset**

2 ≤ N ≤ 3.
sum of all Pi ≤ 9.

**Large dataset**

2 ≤ N ≤ 26.
sum of all Pi ≤ 1000.

#### Sample

```
Input:
4
2
2 2
3
3 2 2
3
1 1 2
3
2 3 1

Output:
Case #1: AB BA
Case #2: AA BC C BA
Case #3: C C AB
Case #4: BA BB CA
```
