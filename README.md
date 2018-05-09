This repo is about generating 3,4,5,6 cycles for the centers of a 5x5.
The wings of a 5x5 can be solved easily by just using basic commutator knowledge, and they are fast to execute if r2 is used frequently.
But the centers (+ centers and the x centers) cannot be solved in efficient manner.

The solver will be different from a normal brute force 5x5 solver, as I do not wish to pair up the edges while making the center.
Instead I want to cube state to be unchanged except for the 3,4,5,6 pieces(of 1 or 2 kinds) under the consideration.

The ultimate goal is to train a human blindfold solver to solve a 5x5 blindfolded under 2 minutes.
