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

The training dataset comprises 50000 synthetically generated entries. Each entry includes columns representing the parameters used to calculate the volumetric flow rate. The flow rate (Q) values were computed for each set of parameters. To review the data or create additional samples, refer to the file:

``` sh
    dataGen.py
``` 
The evaluation dataset contains 4000 synthetic samples designed to assess the model's performance.

### Clone the repository

To clone this repository, copy and paste the code

```sh
git clone https://github.com/Abdulrahman0044/poise-experiment.git
```

### Install the requirements

Install the requirements in the `requirements.txt` file

### Run the model

Copy and paste the code below to run the model

```sh
python model.py
```

### Evaluate the model's performance

To evaluate the performance of the model, run

```sh
python evaluation.py
```
  