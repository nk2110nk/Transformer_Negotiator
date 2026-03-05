#!/bin/bash

set -e  # エラーが出たら停止

# 1. general
python3 ./train.py -a Boulware Conceder Linear -i Laptop ItexvsCypress IS_BT_Acquisition Grocery thompson Car EnergySmall_A

# 2. expert
issues=(
  Laptop
  ItexvsCypress
  IS_BT_Acquisition
  Grocery
  thompson
  Car
  EnergySmall_A
)

agent_sets=(
  "Boulware"
  "Boulware Conceder"
  "Boulware Linear"
  "Conceder Linear"
  "Conceder"
  "Linear"
)

for agents in "${agent_sets[@]}"
do
  for issue in "${issues[@]}"
  do
    echo "Running: -a $agents -i $issue"
    python3 ./train.py -a $agents -i $issue
  done
done