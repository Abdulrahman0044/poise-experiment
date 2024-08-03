# poise-experiment

Poiseuille's law describes the volumetric flow rate (\(Q\)) of an incompressible and Newtonian fluid through a long cylindrical pipe with laminar flow. The formula is given by:

\[ Q = \frac{\Delta P \pi r^4}{8 \mu L} \]

where:
- \( Q \) is the volumetric flow rate.
- \(\Delta P\) is the pressure drop across the length of the pipe.
- \( r \) is the radius of the pipe.
- \(\mu\) is the dynamic viscosity of the fluid.
- \( L \) is the length of the pipe.

## Getting started

### Training and evaluation data

The training data consist of 3000 data created synthetically. The data consist of columns indicating the parameters used in calculating volumetric flow rate. The values of the flow rate (Q) were calculated for each values of the parameters. If you would like to check the data or generate more samples, check the file:

``` sh
    dataGen.py
``` 
The evaluation data consist of 10 samples to evaluate the model and this is geerated synthetically.

## Clone the repository

To clone this repository, copy and paste the code

```sh
git clone https://github.com/Abdulrahman0044/poise-experiment.git
```
