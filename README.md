# Project

This project uses RL for autonomous vehicle control in mixed autonomy env within two focuses:

1. Generalization: Robust-RL under different road densities; 

2. Multi-objective optimization: Effictive balance between safe and speed. 

You may find the original project at: [Project Website](https://mit-wu-lab.github.io/automatic_vehicular_control), [IEEE Website](https://ieeexplore.ieee.org/document/9765650), [arXiv](https://arxiv.org/abs/2208.00268).

```
@article{yan2022unified,
  title={Unified Automatic Control of Vehicular Systems With Reinforcement Learning},
  author={Yan, Zhongxia and Kreidieh, Abdul Rahman and Vinitsky, Eugene and Bayen, Alexandre M and Wu, Cathy},
  journal={IEEE Transactions on Automation Science and Engineering},
  year={2022},
  publisher={IEEE}
}
```

# Environment Setup

This project uses Python with several dependencies managed by `conda`. Follow the instructions below to set up your development environment.

Updated date: Dec 4th 2024.


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

- **pareto/**
  - **2_av_1/c_250/**
  - **beta_0/**
    - **seed_0/**
      - **veh_2/** - Results for 2 vehicles
        - **commit/** - Commit metadata for reproducibility
        - **models/** - Trained models for this configuration
        - **sumo/** - SUMO simulation-related files
        - `2024-11-27T02_52_53.log` - Log file for this run
        - `config.yaml` - Experiment configuration
        - `eval_from_veh_2.csv` - Evaluation results for 2 vehicles
        - `events.out.tfevents.*` - TensorBoard logs for monitoring
        - `train_results.csv` - Training results summary

- **statistics/** - Analysis tools and notebooks
  - `FD.ipynb` - Notebook for flow-density analysis
  - `trajectory.ipynb` - Notebook for analyzing vehicle trajectories
- `init.py` - Package initialization script
- `.gitignore` - Git ignore file
- `actual_runs.ipynb` - Notebook for running experiments and visualizations
- `config.yaml` - Main configuration for experiments
- `env.py` - Environment setup and related classes
- `environment.yml` - Conda environment file
- `eval.job` - SLURM job script for evaluation
- `exp.py` - Experiment setup script
- `figure_eight.py` - Script for figure-eight scenario simulations
- `IDM.job` - SLURM job script for IDM model evaluation
- `README.md` - Documentation for the project
- `ring_multiple_veh_number.py` - Script for multiple vehicle number experiments
- `ring_single_veh_number.py` - Script for single vehicle number experiments
- `runs.ipynb` - Notebook for managing experiment runs
- `train_multi_nodes.job` - SLURM job script for multi-node training(multiple vehicle number scenarios)
- `train_single_node.job` - SLURM job script for single-node training(single vehicle number scenarios)
- `train.job` - SLURM job script for main training
- `u.py` - Helper functions for utilities
- `ut.py` - Functions for defining algorithms and neural networks



## 3. Code running
### 3.1 Training Command:
```
python $F/ring.py $F/pareto/single_ring/seeding/beta1.0_SSM1_torch23558_np1409397498 \
"av=1" "circumference=200" "n_workers=45" "n_rollouts_per_step=45" \
"warmup_steps=2000" "skip_stat_steps=5000" "horizon=5000" "global_reward=True" "n_steps=400" \
"alg='TRPO'" "use_critic=False" "gamma=0.9995" "beta=1.0" "scale_ttc=1" "scale_drac=1" \
"seed_np=1409397498" "seed_torch=23558" "residual_transfer=False" "mrtl=False" \
"handcraft=False" "step_save=False" "lr=0.0001" "wb=False" "tb=False" 
```

#### Explanation of Arguments:
<!-- - **$F/ring.py**: Path to the main running script.
- **pareto/single_ring/seeding/beta1.0_SSM1_torch23558_np1409397498**: Output directory for storing results.
- **worker_kwargs**: Configuration details for workers
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
- **wb**, **tb**: Enable or disable logging with Weights & Biases (`wb`) and TensorBoard (`tb`) (`True` or `False`). -->

Each parameter has a specific role in controlling the training process, and modifying them can lead to different training outcomes, depending on the training scenario and requirements.

### 3.2 Evaluation Command:
```
python "$F/ring_single_veh_number.py" "$F/pareto/2_av_1/c_250/beta_0/seed_1/veh_4/" "device='cpu'"  \
"n_veh=2" "e=100"  "av=1"  "beta=0"  "circumference=250"  "n_rollouts_per_step=1" "skip_vehicle_info_stat_steps=False" "full_rollout_only=True" \
"warmup_steps=2000"  "skip_stat_steps=5000"  "horizon=5000"  "n_steps=10"  "scale_ttc=1"  "scale_drac=1"  "result_save=$F/pareto/2_av_1/c_250/   \
beta_0/seed_1/veh_2/eval_from_veh_4.csv" "vehicle_info_save=$F/pareto/2_av_1/c_250/beta_0/seed_1/veh_2/trajectory_from_veh_4"  "save_agent=$F/ \
pareto/2_av_1/c_250/beta_0/seed_1/veh_2/agent_from_veh_4" "render=True"

```

### 3.3 Running IDM without RL 
```
python $F/ring.py $F/pareto/single_ring/IDM/different_veh \
"av=0" "circumference=200" "n_workers=45" "n_rollouts_per_step=45" \
"warmup_steps=2000" "skip_stat_steps=5000" "horizon=5000" "global_reward=True" "n_steps=400" \
"alg='TRPO'" "use_critic=False" "gamma=0.9995" "beta=1.0" "scale_ttc=1" "scale_drac=1" \
"seed_np=1409397498" "seed_torch=23558" "residual_transfer=False" "mrtl=False" \
"handcraft=False" "step_save=False" "lr=0.0001" "wb=False" "tb=False" 

- **av**: set to 0.

```

### 3.4 Batch Running with Slurm:
Training:
```
sbatch train_multi_nodes.job
```

Evaluation:
```
sbatch eval.job
```

# Parameters Explanation for Evaluation and Training Scripts

This document explains the various parameters used in the evaluation and training scripts for automatic vehicular control.

---

## General SLURM Parameters

| **Parameter**               | **Description**                                                                                          |
|-----------------------------|----------------------------------------------------------------------------------------------------------|
| `--job-name`                | Name of the job. Helps identify it in the queue and logs.                                               |
| `--ntasks-per-core`         | Number of tasks to be executed per core. Typically set to 1.                                            |
| `--ntasks-per-node`         | Number of tasks per compute node. For distributed jobs, this controls task distribution.                |
| `--exclusive`               | Ensures the compute node is reserved exclusively for this job.                                          |
| `--array`                   | Defines the range of tasks for a job array. Allows execution of multiple tasks with different parameters. |
| `--output`/`--error`        | File paths for standard output and error logs. `%j` is replaced with the job ID and `%i` with the array index. |
| `--time`                    | Maximum allowed runtime for the job in HH:MM:SS format.                                                |
| `--partition`               | Specifies the cluster partition or queue to use (e.g., `gpuq`, `rome`, etc.).                          |

---

## Evaluation Parameters

| **Parameter**                   | **Description**                                                                                               |
|---------------------------------|---------------------------------------------------------------------------------------------------------------|
| `transferred_dir/output_dir`(aka input policy path)               | Path to policies pre-trained/trained on the source vehicle configuration.                     |
| `e`                             |   number of gradient update steps of the trained model                                       |
| `result_save` (for reward/speed plots)                  | File path to save evaluation results as a CSV file.                                                           |
| `vehicle_info_save` (for Time-Space plots)            | (Optional) Path to save vehicle trajectory in as a `.npz` file.    |
| `save_agent`                    | Whether to save the agent's state or policy after evaluation.                                      |

---

## Training Parameters

| **Parameter**                   | **Description**                                                                                               |
|---------------------------------|---------------------------------------------------------------------------------------------------------------|
| `alg`                           | Reinforcement learning algorithm to use (e.g., `TRPO`).                                                       |
| `output_dir`     | Directory where trained policies and logs are stored.                                                        |
| `gamma`                         | Discount factor for future rewards. Determines the agent's long-term planning horizon.                        |
| `lr`                            | Learning rate for training the agent.                                                                         |
| `n_workers`                     | Number of parallel workers to use for collecting rollouts.                                                    |
| `n_rollouts_per_step`           | Number of rollouts performed per training step.                                                               |
| `warmup_steps`                  | Steps before starting to collect training statistics.                                                         |
| `skip_stat_steps`               | Steps to skip after warmup before collecting training statistics.                                              |
| `horizon`                       | Total number of steps per rollout during training.                                                            |
| `n_steps`                       | Total number of training steps.                                                                               |
| `global_reward`                 | Whether to use a global reward for the system (e.g., optimizing overall traffic flow).                        |
| `seed_np`/`seed_torch`          | Seeds for reproducibility in NumPy and PyTorch computations.                                                  |
| `residual_transfer`             | If `True`, uses residual learning for policy transfer.                                                        |
| `mrtl`                          | If `True`, uses Multi-Task Reinforcement Learning (MTRL) for policy training.                                  |
| `handcraft`                     | If `True`, uses handcrafted rules in training or evaluation.                                                  |
| `step_save`                     | If `True`, saves the agent’s state or checkpoint at each step.                                                |
| `tb`                            | Enables TensorBoard logging for training metrics visualization.                                               |
| `wb`                            | Enables Weights and Biases (if integrated) for monitoring experiments.                                        |
| `eval_dir`                  | Directory where evaluation result                              |
---



## Default Parameter Values in Scripts

| **Parameter**          | **Default Value**                  | **Notes**                                                                 |
|------------------------|------------------------------------|---------------------------------------------------------------------------|
| `circumference`        | 250                                | Set to 250 meters in the default configuration.                          |
| `beta`                 | 0 or 0.5                           | tradeoff between safety and performance             |
| `warmup_steps`         | 2000                               | Provides sufficient stabilization time for simulations.                  |
| `horizon`              | 5000                               | Ensures long enough simulation runs for meaningful statistics.           |
| `alg`                  | `TRPO`                             | Can be replaced with other algorithms (e.g., PPO, TRPO).                  |
| `gamma`                | 0.9995                             | A high discount factor for long-term reward optimization.                |
| `lr`                   | 1e-4                               | Can be adjusted for faster/slower convergence.                           |
| `tb`                   | `True`                             | Enables TensorBoard logging by default.                                  |
| `seed`                          | Random seed for reproducibility of simulations and experiments.                                               |
| `n_veh`               | Total vehicle number       | 22|
| `av`               | av number       | 1 or 0 |
| `n_steps`                          | Number of gradient updates number                   |  100                             |
| `skip_stat_steps`               | Steps to skip after warmup before collecting statistics, ensuring the simulation reaches a steady state.       | 5000 |
| `horizon`                       | Total number of simulation steps for the evaluation.    | 5000             |                                  |
| `n_rollouts_per_step`           | Number of simulation rollouts to perform per evaluation step.                                      | 45    |
| `scale_ttc`/`scale_drac`        | Scaling factors for reward components related to time-to-collision (TTC) and deceleration rates (DRAC).        |
| `render`    | SUMO GUI render       | False or True |
