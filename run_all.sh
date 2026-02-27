#!/bin/bash

set -e  # エラーが出たら停止

# 1. 全部まとめて実行
python3 ./train.py -a Boulware Conceder Linear -i Laptop ItexvsCypress IS_BT_Acquisition Grocery thompson Car EnergySmall_A

# 2. Boulware
python3 ./train.py -a Boulware -i Laptop
python3 ./train.py -a Boulware -i ItexvsCypress
python3 ./train.py -a Boulware -i IS_BT_Acquisition
python3 ./train.py -a Boulware -i Grocery
python3 ./train.py -a Boulware -i thompson
python3 ./train.py -a Boulware -i Car
python3 ./train.py -a Boulware -i EnergySmall_A

# 3. Conceder
python3 ./train.py -a Conceder -i Laptop
python3 ./train.py -a Conceder -i ItexvsCypress
python3 ./train.py -a Conceder -i IS_BT_Acquisition
python3 ./train.py -a Conceder -i Grocery
python3 ./train.py -a Conceder -i thompson
python3 ./train.py -a Conceder -i Car
python3 ./train.py -a Conceder -i EnergySmall_A

# 4. Linear
python3 ./train.py -a Linear -i Laptop
python3 ./train.py -a Linear -i ItexvsCypress
python3 ./train.py -a Linear -i IS_BT_Acquisition
python3 ./train.py -a Linear -i Grocery
python3 ./train.py -a Linear -i thompson
python3 ./train.py -a Linear -i Car
python3 ./train.py -a Linear -i EnergySmall_A