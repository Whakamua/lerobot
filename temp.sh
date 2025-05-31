#!/bin/bash

# Set HF_USER from Hugging Face CLI
HF_USER=$(huggingface-cli whoami | head -n 1)

# Get current timestamp
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

repo_id=${HF_USER}/so100_test_${TIMESTAMP}

echo "Repo ID: ${repo_id}"
python lerobot/scripts/control_robot.py \
  --robot.type=so100 \
  --control.type=record \
  --control.fps=30 \
  --control.single_task="Grasp seal plushy and put it in the white box" \
  --control.repo_id=${repo_id} \
  --control.tags='["so100","tutorial"]' \
  --control.warmup_time_s=5 \
  --control.episode_time_s=30 \
  --control.reset_time_s=30 \
  --control.num_episodes=50 \
  --control.push_to_hub=false

echo "Repo ID: ${repo_id}"

# 50 episodes Repo ID: Whakamua/so100_test_20250531_090814