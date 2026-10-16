"""Check the dialogue files cover every action, event and deed, and follow STYLE.md."""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
ALLOWED = {"A", "B", "town", "lord", "lady", "steward", "hamlet", "band", "calamity", "guild", "good", "player", "dead", "hall", "site"}
CONDS = {"state", "time", "place", "news", "standing", "hold", "mood", "attitude"}
MIN = {"activity": 3, "event": 5, "deed": 6, "squad": 5}

actions = json.loads((HERE / "src" / "actions.json").read_text())
need = {
    "activity": {a["activity"] for a in actions["activities"]},
    "event": {e["event"] for e in actions["events"]},
    "deed": set(actions["player_deeds"]),
}
squad = json.loads((HERE / "src" / "squad.json").read_text())
need["squad"] = {k for part in squad.values() for k, _ in part}

have = {k: set() for k in need}
ids, problems, lines, exchanges = set(), [], 0, 0
for f in sorted(HERE.glob("*.json")):
    for s in json.loads(f.read_text()):
        kind, action = s.get("kind"), s.get("action")
        if kind not in need:
            problems.append(f"{f.name}: {action}: unknown kind {kind!r}")
            continue
        have[kind].add(action)
        ex = s.get("exchanges", [])
        exchanges += len(ex)
        if len(ex) < MIN[kind]:
            problems.append(f"{f.name}: {action}: only {len(ex)} exchanges")
        fallback = False
        for e in ex:
            if e["id"] in ids:
                problems.append(f"{f.name}: duplicate id {e['id']}")
            ids.add(e["id"])
            when = e.get("when") or {}
            extra = set(when) - CONDS
            if extra:
                problems.append(f"{f.name}: {e['id']}: unknown conditions {extra}")
            if all(v is None for k, v in when.items() if not (kind == "event" and k == "news")):
                fallback = True
            for ln in e["lines"]:
                lines += 1
                for ph in re.findall(r"\{(\w+)\}", ln["text"]):
                    if ph not in ALLOWED:
                        problems.append(f"{f.name}: {e['id']}: bad placeholder {{{ph}}}")
        if not fallback:
            problems.append(f"{f.name}: {action}: no fallback exchange")

for kind in need:
    for missing in sorted(need[kind] - have[kind]):
        problems.append(f"missing {kind}: {missing}")

print(f"{sum(len(v) for v in have.values())} sets, {exchanges} exchanges, {lines} lines")
for p in problems:
    print("PROBLEM:", p)
sys.exit(1 if problems else 0)
