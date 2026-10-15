# Map simulation tests

These scripts run `Stewards_Living_World_Map.html` headless for its full 364-day world run, with optional player deeds, and save the results as JSON. The results are written up in [../../story/08-simulation-tests.md](../../story/08-simulation-tests.md).

* `run.js` loads the map in Playwright, injects a scenario through `window.__acts` and saves the summary.
* `guardian.json`, `outlaw.json` and `redeemed.json` are the life-path scenarios.

```bash
NODE_PATH=$(npm root -g) node run.js <map.html> <scenario.json or ""> <out.json>
```
