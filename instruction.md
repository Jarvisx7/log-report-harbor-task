Analyze the Apache-style access log at `/app/access.log` and write a JSON report
to `/app/report.json`.

The report must be a JSON object with exactly these fields:

- `total_requests`: the number of log entries.
- `unique_ips`: the number of distinct client IP addresses.
- `top_path`: the request path that occurs most often.

For the supplied log, the required values are `6`, `3`, and `/index.html`,
respectively. Do not add any other fields.
