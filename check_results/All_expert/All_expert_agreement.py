import os
import pandas as pd

ISSUE_NAMES = [
    'Laptop','ItexvsCypress','IS_BT_Acquisition',
    'Grocery','thompson','Car','EnergySmall_A'
]

AGENT_LIST = ['Boulware','Conceder','Linear']
path = './results/All_expert'

PAIR_LIST = [f"{AGENT_LIST[i]}-{AGENT_LIST[j]}"
             for i in range(len(AGENT_LIST))
             for j in range(i, len(AGENT_LIST))]

results_all = pd.DataFrame(index=ISSUE_NAMES, columns=PAIR_LIST, dtype=float)

for i, agent0 in enumerate(AGENT_LIST):
    for j in range(i, len(AGENT_LIST)):
        agent1 = AGENT_LIST[j]
        pair = f"{agent0}-{agent1}"

        for issue in ISSUE_NAMES:
            file_path = f"{path}/{pair}/csv/{pair}/{issue}/det=False_noise=False/{issue}-{agent0}-{agent1}-dF-nF.tsv"

            if not os.path.exists(file_path):
                print("missing:", file_path)
                continue

            df = pd.read_csv(file_path, delimiter='\t')

            # ===== 合意成功率 =====
            success = (df['my_util'] > 0).sum()
            total = len(df)

            agreement_rate = (success / total) * 100 if total > 0 else 0

            results_all.loc[issue, pair] = agreement_rate

# 見やすく整形
results_all = results_all.T
results_all['Average'] = results_all.mean(axis=1)
results_all.loc['Average'] = results_all.mean(axis=0)
results_all = results_all.round(3)

print(results_all)
results_all.to_csv("summary_agreement_rate_expert.csv")
