import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
from strategy import StructureAnalyzer, LiquidityAnalyzer, OrderBlockAnalyzer, FVGAnalyzer, ConfluenceScorer

def run_bot():
    print("🚀 Starting AbuBakar FX Trading Bot...")
    
    data = {
        'open': [1900, 1902, 1901, 1905, 1904],
        'high': [1903, 1906, 1904, 1908, 1907],
        'low': [1898, 1900, 1899, 1903, 1902],
        'close': [1902, 1901, 1905, 1904, 1906]
    }
    df = pd.DataFrame(data)

    struct = StructureAnalyzer().analyze_structure(df)
    liq = LiquidityAnalyzer().find_liquidity_pools(df)
    ob = OrderBlockAnalyzer().find_order_blocks(df)
    fvgs = FVGAnalyzer().find_fvgs(df)

    score = ConfluenceScorer().calculate_score(struct, liq, ob, fvgs)

    print("📊 Analysis Result:")
    print(f"Signal: {score['signal']} | Score: {score['score']}/{score['max_score']}")
    print(f"Reasons: {score['reasons']}")

if __name__ == "__main__":
    run_bot()
