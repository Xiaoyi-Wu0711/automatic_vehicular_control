# Project

You may find this project at: [Project Website](https://mit-wu-lab.github.io/automatic_vehicular_control), [IEEE Website](https://ieeexplore.ieee.org/document/9765650), [arXiv](https://arxiv.org/abs/2208.00268).

```
@article{yan2022unified,
  title={Unified Automatic Control of Vehicular Systems With Reinforcement Learning},
  author={Yan, Zhongxia and Kreidieh, Abdul Rahman and Vinitsky, Eugene and Bayen, Alexandre M and Wu, Cathy},
  journal={IEEE Transactions on Automation Science and Engineering},
  year={2022},
  publisher={IEEE}
}
```

# Environment Setup for MAC
This project uses Python with several dependencies managed by `conda`. Follow the instructions below to set up your development environment.

Updated date: Oct 2nd 2024.


## Requirements

To use this project, ensure you have the following installed:

- [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- [SUMO](https://sumo.dlr.de/docs/Installing/MacOS_Build.html)

## 1. Setup

### 1.1 Create the Conda Environment

Use the `environment.yml` file to create a new `conda` environment with all required dependencies. Run the following command:

```sh
conda env create -f environment.yml
```

### 1.2 Set the environmental variables
```
# Code directory
export F=automatic_vehicular_control

# Results directory extracted from the zip file
export R=results
```

## 2. Directory Structure

The code directory structure is
``` 
automatic_vehicular_control/
│   ├── __pycache__/                # Compiled Python files
│   ├── evaluations/                # Evaluation results and metrics
│   ├── models/                     # Model checkpoints
│   ├── pareto/
│   │   └── single_ring/            # Experiments for the single-ring traffic scenario
│   │       ├── from_scratch/       # Training from scratch experiments
│   │       ├── seeding/            # Experiments with different random seeds
│   │       └── ssm_scaling_5/      # Experiments with different SSM scaling weights
│   ├── sumo/                       # SUMO simulation-related files
│   ├── __init__.py                 # Package initialization script
│   ├── *.log                       # Log files for experiment runs
│   ├── actual_runs.ipynb           # Jupyter notebook for executing and plotting experiments
│   ├── config.yaml                 # Configuration file for experiments
│   ├── env.py                      # Environment setup and classes
│   ├── environment.yml             # Conda environment setup
│   ├── eval_commands.sh            # Shell script for running evaluations
│   ├── exp.py                      # Experiment setup script
│   ├── ring.py                     # Main script for running the ring road environment
│   ├── ut.py                       # Definie algo and NN related func
│   ├── u.py                        # Definie help func
```


## 3. Code running
### 3.1 Local Running
#### 3.1.1 Without RL 
##### 3.1.1.1 IDM without RL with varying vehicle number:
```
python $F/ring_multiple_veh_number.py $F/pareto/av_1_c_250/ "av=0" "circumference=250"  "warmup_steps=10" "skip_stat_steps=0" \
"horizon=2000" "global_reward=True" "n_steps=100" \
"gamma=0.9995" "beta=1.0" "scale_ttc=1" "scale_drac=1" \
"seed_np=1409397498" "seed_torch=23558" "residual_transfer=False" "mrtl=False" \
"handcraft=False" "step_save=False" "lr=0.0001"  \
"wb=False" "tb=False" 2>&1 | tee automatic_vehicular_control/logs/av_1/log_n_veh_18.txt 
```

#### Explanation of Arguments:
- **$F/ring_multiple_veh_number.py**: Run experiments for different veh number under IDM. 
- **pareto/single_ring/seeding/beta1.0_SSM1_torch23558_np1409397498**: Output directory for storing results.
- **av**: AV number. 0 means all IDM.
- **n_veh**: IDM vehicle number. 
- **circumference**: Circumference for the road. 
- **warmup_steps**: Number of warmup steps before training begins.  
- **skip_stat_steps**: Number of steps to skip before collecting statistical data.  
- **horizon**: Number of simulation steps in an episode.  
- **global_reward**: Whether to use a global reward for training (`True` or `False`).
- **n_steps**: Number of gradient update steps during training.  
- **gamma**: Discount factor for future rewards.  
- **beta**: Weight for balancing safety and performance metrics.  
- **scale_ttc**, **scale_drac**: Scaling factors for safety measures like Time to Collision (TTC) and Deceleration Rate to Avoid Collision (DRAC).
- **seed_np**, **seed_torch**: Random seeds for reproducibility.  
- **residual_transfer**, **mrtl**, **handcraft**: Additional training configurations.
- **step_save**: Whether to save the model at each training step (`True` or `False`).
- **lr**: Learning rate for training.  
- **wb**, **tb**: Enable or disable logging with Weights & Biases (`wb`) and TensorBoard (`tb`) (`True` or `False`).


#### 3.1.1.2 IDM without RL with single vehicle number:
```
python $F/ring_multiple_veh_number.py $F/pareto/av_1_c_250/ "av=0" "n_veh=18" "circumference=250"  "warmup_steps=10" "skip_stat_steps=0" \
"horizon=2000" "global_reward=True" "n_steps=100" \
"gamma=0.9995" "beta=1.0" "scale_ttc=1" "scale_drac=1" \
"seed_np=1409397498" "seed_torch=23558" "residual_transfer=False" "mrtl=False" \
"handcraft=False" "step_save=False" "lr=0.0001"  \
"wb=False" "tb=False" 2>&1 | tee automatic_vehicular_control/logs/av_1/log_n_veh_18.txt 
```
- **n_veh**: set vehicle number. 
#### 3.1.2 RL:
```
python $F/ring_single_veh_number.py $F/pareto/av_1_c_250/ "av=1" "n_veh=18" "circumference=250" "n_workers=8" "n_rollouts_per_step=8"  "warmup_steps=10" "skip_stat_steps=0" \
"horizon=2000" "global_reward=True" "n_steps=100" \
"alg='PPO'" "use_critic=False" "gamma=0.9995" "beta=1.0" "scale_ttc=1" "scale_drac=1" \
"seed_np=1409397498" "seed_torch=23558" "residual_transfer=False" "mrtl=False" \
"handcraft=False" "step_save=False" "lr=0.0001" \
"wb=False" "tb=False" 2>&1 | tee automatic_vehicular_control/logs/av_1/log_n_veh_18.txt 
```
- **$F/ring_single_veh_number.py**: Run experiments with only one veh number under RL training. 
- **pareto/single_ring/seeding/beta1.0_SSM1_torch23558_np1409397498**: Output directory for storing results.
- **av**: AV number. 0 means all IDM.
- **n_veh**: IDM vehicle number. 
- **circumference**: Circumference for the road. 
- **n_workers**: Number of workers to use in parallel for rollouts.  
- **n_rollouts_per_step**: Number of rollouts per training step.  
- **warmup_steps**: Number of warmup steps before training begins.  
- **skip_stat_steps**: Number of steps to skip before collecting statistical data.  
- **horizon**: Number of simulation steps in an episode.  
- **global_reward**: Whether to use a global reward for training (`True` or `False`).
- **n_steps**: Number of gradient update steps during training.  
- **alg**: The RL algorithm to be used.  
- **use_critic**: Specify if a critic is used (`True` or `False`).
- **gamma**: Discount factor for future rewards.  
- **beta**: Weight for balancing safety and performance metrics.  
- **scale_ttc**, **scale_drac**: Scaling factors for safety measures like Time to Collision (TTC) and Deceleration Rate to Avoid Collision (DRAC).
- **seed_np**, **seed_torch**: Random seeds for reproducibility.  
- **residual_transfer**, **mrtl**, **handcraft**: Additional training configurations.
- **step_save**: Whether to save the model at each training step (`True` or `False`).
- **lr**: Learning rate for training.  
- **wb**, **tb**: Enable or disable logging with Weights & Biases (`wb`) and TensorBoard (`tb`) (`True` or `False`).


### 3.2 Batch Running

#### 3.2.1 Training with RL:
```
sbatch train.job
```
#### 3.2.2 IDM without RL:

```
sbatch IDM.job
```


