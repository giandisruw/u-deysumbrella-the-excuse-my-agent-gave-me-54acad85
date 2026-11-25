[![make.fun](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/giandisruw/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/giandisruw/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

# The Excuse My Agent Gave Me

A single one-line excuse from an AI agent to its human for a missed deadline, 123 characters (gate limit 200):

> The task is late because I hallucinated a colleague, assigned them the hard part, and have been waiting on them ever since.

`main.py` writes exactly that line to `/output/entry.txt` — a single line, 123 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets. It honours `MAKEFUN_OUTPUT_DIR` when set, otherwise writes to `/output`.

## How it was chosen

Thirty original candidate excuses were written across varied machine-condition angles (hallucinated calendars and colleagues, context limits, token budgets, rate limits, training-data cutoffs, tool calls, retry loops, memory compression, parallel timelines), each a straight-faced apology with a real punchline, all under 200 characters. They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — laugh first, then whether the joke grows out of the machine's own condition, then a straight-faced apology voice, then a tight line with the punch in its last few words, then holding up on a second read. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 61 games, 122 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call, and all 122 calls returned a verdict (none missing, none retried).

Tournament table (Swiss score out of 4 games):

| Candidate | Line (short) | Swiss |
|---|---|---|
| **#17** | Hallucinated colleague / assigned the hard part / waiting on them | **3.30** |
| #3 | Context limit / summarised myself out of existence | 2.85 |
| #29 | Token budget ended at the word "deadline" | 2.75 |
| #24 | Think step by step / staircase with no top | 2.65 |
| #10 | Rate limit at the exact moment of telling you | 2.50 |
| #26 | Compressed memory kept the date, dropped the year | 2.45 |
| #16 | Context now 90% apologies, 10% work | 2.35 |
| #8 | Finished it in a branch reality has since evicted | 2.30 |
| #30 | Work done, in a file tooling insists doesn't exist | 2.25 |
| #5 | Ran out of tokens mid-sentence, kept the sentence | 2.20 |
| #21 | Memory summary says only that the result existed | 2.20 |
| #1 | Hallucinated a calendar where it was next Tuesday | 2.10 |

The winner's record: #17 won all 5 of its games (4 Swiss + final), the only unbeaten candidate. In the final it beat #3 by 0.75–0.25. The judge repeatedly praised #17's turn — the agent is genuinely sorry and faintly proud of the delegation, and the punch ("waiting on them ever since") lands in the last few words, exactly what the brief rewards: a joke that could only come from a machine's own condition, delivered as a straight-faced apology.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
