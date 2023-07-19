import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
d0_=5
C_=15
mu_=6
alpha_=0.7
def load_eqs(omega_d,omega):
    def eqs(y,t,R):
        d,g = y
        dydt = [omega_d*(C_+mu_*np.log(R(t)) - alpha_*g - d), 
                omega*(d/d0_-1), 
                ]
        return dydt
    return eqs
eqs=load_eqs(9,3);
def get_y0(r0=1,tmax = 100):
    t = np.arange(1, tmax,0.01)
    sol = odeint(eqs, [1,1], t,args=(lambda t: r0,))
    return sol[-1]
def run(r,t,r0=1):
    return odeint(eqs, get_y0(r0), t,args=(r,),rtol=1e-12,atol=1e-12)
def generate_stim_reward(tcue = 1,treward = None,tmax = 4.5,
                         reward_baseline = 1,reward_size=5,give_reward=1):
    t = np.arange(0, tmax,0.01)
    if treward==None:
        # if treward is none, cue and reward happen at the same time
        r = lambda t: reward_baseline if (t<tcue) else give_reward*reward_size + (1-give_reward)*0.1*reward_baseline
        rdashed = r
    else:
        r = lambda t: reward_baseline if (t<tcue) else 0.5*reward_size if (t<treward) else give_reward*reward_size + (1-give_reward)*0.1*reward_baseline
        rdashed = lambda t: r(t) if t<treward else 0.1*reward_baseline 
    return run(r,t,reward_baseline),r,t,rdashed
tcue = 1
treward = 2
tmax = 4.5
reward_baseline = 1
reward_size = 5
give_reward = 1
# Generate the simulation results
solution, r, t, rdashed = generate_stim_reward(tcue, treward, tmax, reward_baseline, reward_size, give_reward)
# Plot the simulation results
plt.figure(figsize=(10, 6))

# Plot the stimulus/reward values over time
plt.plot(t, [r(ti) for ti in t], label='Stimulus/Reward (r)', color='blue')
plt.plot(t, [rdashed(ti) for ti in t], label='Modified Reward (rdashed)', color='green')

# Plot the variable 'd' from the simulation results
plt.plot(t, solution[:, 0], label='Dopamine', color='red')

# Plot the variable 'g' from the simulation results
plt.plot(t, solution[:, 1], label='GABAergic', color='orange')

plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Reward-Based Learning Model')
plt.legend()
plt.grid(True)
plt.show()

