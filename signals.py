def score_stock(row):
    return int(row.get("momentum", 0) > 0) + int(row.get("quality", 0) > 0) + int(row.get("valuation", 0) > 0)

def should_buy(row, min_score=3):
    return score_stock(row) >= min_score
