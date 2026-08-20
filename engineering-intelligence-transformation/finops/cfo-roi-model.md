# CFO-Ready ROI Model

## Productivity Formula
Monthly recovered hours = engineers * minutes_saved_per_day / 60 * working_days.
FTE equivalent = monthly_recovered_hours / 168.
Monthly value = FTE equivalent * loaded_monthly_engineer_cost.

## Example
300 engineers saving 30 minutes/day over 20 workdays = 3,000 hours/month.
3,000 / 168 = 17.85 FTE equivalent.
At $18,000 loaded monthly cost, this is about $321,300/month or $3.85M/year of capacity value.

## Incident Formula
Incident savings = incidents_per_month * avg_hours_reduced * engineers_involved * loaded_hourly_cost.

## Cost Controls
- Model tiering.
- Context compression.
- Retrieval top-N limits.
- Embedding dedupe and incremental indexing.
- Redis/cache for common queries.
- Quotas by user/team/repo/agent.
- Showback dashboard by cost center.