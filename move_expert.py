import os
import shutil
import re

BASE_SRCS = ["results_case1"]
BASE_DST = "data/expert"

DOMAINS = [
    "Laptop",
    "ItexvsCypress",
    "IS_BT_Acquisition",
    "Grocery",
    "thompson",
    "Car",
    "EnergySmall_A",
]

def get_case_name(base_src):
    """
    results       -> case1
    results_case2 -> case2
    results_case3 -> case3
    """
    if base_src == "results":
        return "case1"

    m = re.match(r"results_case(\d+)$", base_src)
    if m:
        return f"case{m.group(1)}"

    raise ValueError(f"case名を判定できません: {base_src}")

def get_matchup(agent_str):
    agents = agent_str.split()
    if len(agents) == 1:
        return f"{agents[0]}-{agents[0]}"
    elif len(agents) == 2:
        return f"{agents[0]}-{agents[1]}"
    else:
        raise ValueError(f"Agent数がおかしい: {agent_str}")

for base_src in BASE_SRCS:
    if not os.path.isdir(base_src):
        print(f"Skip: {base_src} が存在しません")
        continue

    case_name = get_case_name(base_src)

    for folder in os.listdir(base_src):
        for domain in DOMAINS:
            if not folder.startswith(domain + "_"):
                continue

            src_domain_path = os.path.join(base_src, folder)

            if not os.path.isdir(src_domain_path):
                continue

            agent_part = folder[len(domain) + 1:]
            agent_part = agent_part.replace("-", " ")
            matchup = get_matchup(agent_part)

            subdirs = sorted([
                d for d in os.listdir(src_domain_path)
                if os.path.isdir(os.path.join(src_domain_path, d))
            ])

            if not subdirs:
                continue

            run_dir = os.path.join(src_domain_path, subdirs[-1])
            csv_dir = os.path.join(run_dir, "csv")

            if not os.path.isdir(csv_dir):
                continue

            for root, dirs, files in os.walk(csv_dir):
                # 末端フォルダだけ
                if len(dirs) == 0:
                    for f in files:
                        if f.endswith(".tsv"):
                            src_file = os.path.join(root, f)

                            dst_dir = os.path.join(
                                BASE_DST,
                                matchup,
                                domain,
                                case_name
                            )
                            os.makedirs(dst_dir, exist_ok=True)

                            dst_file = os.path.join(dst_dir, f)

                            print(f"Copy: {src_file} -> {dst_file}")
                            shutil.copy2(src_file, dst_file)
