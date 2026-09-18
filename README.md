# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
    conda env create -f PW<n>/Lab\ <X>/environment.yml
    conda activate cspc
---

## PW1 - Lab A: Reproducible Foundations
**What I built:**
- I made tests for atomic decay simulation functions given to me and made a program that checks how much faster the faster function is than the slower one.

**Speed comparison (loop vs NumPy):**
- loop : 22.9911 s
- numpy : 0.0266 s
- speed-up: 865.62 x faster

**Tests:** all passing? (yes / no)
- Yes

**Conclusion:**
- I learned that the speed of the numpy version of the algorithm is highly variable compared to the loop based one. In the runs I made, the loop based algorithm takes anywhere from 22.8 to 24.1 seconds, the difference between the two values being around 5%, while the numpy algorithm ranges from 0.016 to 0.028 seconds, a whopping 75% difference.