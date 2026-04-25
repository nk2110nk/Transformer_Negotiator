#!/bin/bash

set -e  # エラーが出たら停止

# 1. general


# 2. expert
issues=(
  # Laptop
  # ItexvsCypress
  # IS_BT_Acquisition
  # Grocery
  thompson
  Car
  EnergySmall_A
)

agent_sets=(
  # "Boulware Linear"
  # "Conceder Linear"
  # "Boulware Atlas3"
  # "Conceder Atlas3"
  # "Linear Atlas3"
  # "Atlas3"
  # "Boulware"
  # "Conceder"
  # "Linear"
  "Boulware Conceder"
)

for agents in "${agent_sets[@]}"
do
  for issue in "${issues[@]}"
  do
    echo "Running: -a $agents -i $issue"
    python3 ./train.py -a $agents -i $issue
  done
done

python3 ./train.py -a Boulware Conceder Linear Atlas3 -i Laptop ItexvsCypress IS_BT_Acquisition Grocery thompson Car EnergySmall_A
