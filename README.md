# SoS
# Dopamine Transmission Modeling with Reward-Based Learning

## Overview

This Python code presents a simulation of a system that models dopamine transmission in neurons, specifically focusing on reward-based learning. The simulation explores how dopamine levels change concerning expected rewards and inhibition. The model takes into account several parameters that influence dopamine activity and neurotransmitter interactions.

## Requirements

To run the simulation and visualize the results, you need the following libraries:

- `matplotlib`: For plotting the simulation results.
- `numpy`: For numerical computations.
- `scipy`: For solving ordinary differential equations (ODEs).

## Parameters

1. `d0_`: Homeostatic activity level of dopamine.
2. `C_`: Baseline level of dopamine.
3. `mu_`: Gain parameter, influencing dopamine response to reward signals.
4. `alpha_`: Effectiveness of inhibition by the GABAergic output.

## Differential Equations

The core of the simulation is a set of coupled ordinary differential equations (ODEs) describing the dynamics of the system:

```
dy/dt = [omega_d * (C_ + mu_ * ln(R(t)) - alpha_ * g - d),
         omega * (d / d0_ - 1)]
```

Where:
- `d`: Represents dopamine levels.
- `g`: Variable influencing dopamine inhibition.
- `t`: Time variable.
- `R(t)`: Stimulus/reward function, modulated over time.
- `omega_d`: Parameter influencing dopamine dynamics concerning reward signals.
- `omega`: Parameter influencing dopamine dynamics concerning homeostatic levels.

## Functions

The code defines several functions to support the simulation and data generation:

1. `load_eqs`: Creates the system of differential equations based on the given `omega_d` and `omega`.
2. `get_y0`: Initializes the system with appropriate initial conditions.
3. `run`: Performs the ODE integration for the given time points and reward values.
4. `generate_stim_reward`: Generates the stimulus/reward values over time and corresponding dopamine dynamics.

## Simulation Parameters

The following parameters are used to set up the simulation and generate the results:

- `tcue`: The time of stimulus cue onset.
- `treward`: The time of reward presentation (optional; if not provided, reward occurs simultaneously with the cue).
- `tmax`: The maximum time for the simulation.
- `reward_baseline`: The baseline level of the reward.
- `reward_size`: The size of the reward signal.
- `give_reward`: A parameter to control the reward level.

## Results

The simulation results are plotted to visualize the dynamics of the system over time. The plot includes:

1. The stimulus/reward values (`r`) and modified reward values (`rdashed`) over time, influenced by cue onset and reward presentation.
2. The variables `d` and `g` representing dopamine levels and inhibition, respectively, as they evolve over time.

## Usage

To use the code and generate simulation results, follow these steps:

1. Ensure you have the required libraries installed: `matplotlib`, `numpy`, and `scipy`.
2. Set the desired parameters for the simulation (e.g., `tcue`, `treward`, etc.).
3. Run the script to generate the simulation results.
4. The plot will display the changes in stimulus/reward, dopamine levels, and inhibition over time.

Note: The initial conditions for dopamine and inhibition are automatically calculated using the `get_y0` function.

## Citation

If you use this code or simulation in your work, please consider citing the source or providing appropriate acknowledgment.

---

*This code provides a comprehensive yet concise implementation of a dopamine transmission model with reward-based learning. The simulation and visualization enable insights into how dopamine levels respond to reward signals and inhibitory influences. Feel free to experiment with different parameters and scenarios to gain a deeper understanding of the system's dynamics.*
