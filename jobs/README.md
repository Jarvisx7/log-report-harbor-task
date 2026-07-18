# Validation artifacts

This directory records verifier evidence from local Harbor runs.

- `oracle-pass/`: `harbor run -p . -a oracle` produced reward `1` and all four tests passed.
- `nop-fail/`: `harbor run -p . --agent nop` produced reward `0` and all four tests failed because no report was produced.

The current verifier also emits `/logs/verifier/ctrf.json` on each run.
