# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW1/Lab A/.

Setup.
Create the environment for a given lap:

conda env create -f PW1/Lab /environment.yml 
conda activate cspc

PW1 - Lab A: Reproducible Foundations

What I built:

Created a reproducible Conda environment with Python 3.11, NumPy, and pytest.
Implemented and tested a radioactive decay simulation.
Used Git for version control and GitHub for remote backup.
Added tests for invalid input and the analytical decay law.
Compared a pure-Python loop with a vectorised NumPy implementation.

Speed comparison (loop vs NumPy):

loop: 0.167497 s
NumPy: 0.000232 s
speed-up: 721.71 x

Tests: all passing (3/3)

Conclusion:

The NumPy implementation was much faster than the pure-Python loop in this benchmark.
The tests confirm that the simulation starts at N0, rejects negative decay rates, and agrees with the an
