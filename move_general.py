import os
import shutil
import re

SRC_CSV = [
    "results_case1/Laptop-ItexvsCypress-IS_BT_Acquisition-Grocery-thompson-Car-EnergySmall_A_Boulware-Conceder-Linear-Atlas3/20260321-184856-TA/csv",
    "results_case2/Laptop-ItexvsCypress-IS_BT_Acquisition-Grocery-thompson-Car-EnergySmall_A_Boulware-Conceder-Linear-Atlas3/20260305-145820-TA/csv",
    "results_case3/Laptop-ItexvsCypress-IS_BT_Acquisition-Grocery-thompson-Car-EnergySmall_A_Boulware-Conceder-Linear-Atlas3/20260308-045604-TA/csv",
    "results_case4/Laptop-ItexvsCypress-IS_BT_Acquisition-Grocery-thompson-Car-EnergySmall_A_Boulware-Conceder-Linear-Atlas3/20260305-150959-TA/csv",
    "results_case5/Laptop-ItexvsCypress-IS_BT_Acquisition-Grocery-thompson-Car-EnergySmall_A_Boulware-Conceder-Linear-Atlas3/20260418-055509-TA/csv",
    "results_case6/Laptop-ItexvsCypress-IS_BT_Acquisition-Grocery-thompson-Car-EnergySmall_A_Boulware-Conceder-Linear-Atlas3/20260414-143137-TA/csv",
]
DST_BASE = "data/general"

def detect_case_name(path):
    """
    results_case2 なら case2
    results_case3 なら case3
    のように自動判定する
    """
    m = re.search(r"results_case(\d+)", path)
    if not m:
        raise ValueError("パスから case 番号を判定できません。results_case2 のような名前にしてください。")
    return f"case{m.group(1)}"

for src_csv in SRC_CSV:
    case_name = detect_case_name(src_csv)

    for matchup in os.listdir(src_csv):
        matchup_path = os.path.join(src_csv, matchup)

        if not os.path.isdir(matchup_path):
            continue

        for domain in os.listdir(matchup_path):
            domain_path = os.path.join(matchup_path, domain)

            if not os.path.isdir(domain_path):
                continue

            dst_dir = os.path.join(DST_BASE, matchup, domain, case_name)
            os.makedirs(dst_dir, exist_ok=True)

            # domain_path の下を全部探索して .tsv だけコピー
            for root, dirs, files in os.walk(domain_path):
                for f in files:
                    if not f.endswith(".tsv"):
                        continue

                    src_file = os.path.join(root, f)
                    dst_file = os.path.join(dst_dir, f)

                    if os.path.exists(dst_file):
                        print(f"Skip existing: {dst_file}")
                        continue

                    print(f"Copy: {src_file} -> {dst_file}")
                    shutil.copy2(src_file, dst_file)

    print(f"完了: {case_name} に振り分けました")
