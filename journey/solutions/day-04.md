# Day 4 solution: Turn logs into observations



## Reasoning and expected result

The observed sample has two search failures. Health success does not prove the search dependency path is healthy. Hypotheses include an unavailable upstream and route-specific configuration. Request correlated upstream evidence or route configuration history. Without timezone and collection coverage, even the apparent timeline is incomplete.

## Acceptance

Four records, two 503s, three search requests and two failed searches. Your report distinguishes 2/4 across the sample from 2/3 within search. Do not infer a database failure or a service-wide rate from four lines.

[Return to lesson](../days/day-04.md)
