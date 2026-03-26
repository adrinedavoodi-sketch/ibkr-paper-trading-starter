def score_stock(row):
    score = 0

    # Momentum: positive 3-month return
    if row.get("momentum_pct") is not None and row["momentum_pct"] > 0:
        score += 1

    # Quality: positive profit margin
    if row.get("profit_margin") is not None and row["profit_margin"] > 0.10:
        score += 1

    # Valuation: P/E under 40 (reasonable growth stock threshold)
    pe = row.get("pe_ratio")
    if pe is not None and 0 < pe < 40:
        score += 1

    # Low leverage: debt-to-equity under 150
    dte = row.get("debt_to_equity")
    if dte is not None and dte < 150:
        score += 1

    return score

def should_buy(row, min_score=3):
    return score_stock(row) >= min_score
