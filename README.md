# IBKR Paper Trading Starter

A simple stock research + paper trading workflow using Python and Interactive Brokers.

## Workflow
1. Research and shortlist symbols in Perplexity.
2. Commit strategy code to GitHub.
3. Run the script locally against IBKR paper trading.
4. Review results before any real-money use.

## Files
- `config.py`
- `ibkr_client.py`
- `scanner.py`
- `signals.py`
- `trade.py`

## Setup
1. Create an IBKR paper account.
2. Enable the IBKR API / Client Portal.
3. Install dependencies from `requirements.txt`.
4. Update `config.py`.
5. Run `python trade.py`.
