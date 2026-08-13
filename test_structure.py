# test_structure.py
import pandas as pd
from strategy.structure import StructureAnalyzer

def test():
    data = {
        'open': [10, 12, 11, 15, 14, 18],
        'high': [11, 13, 12, 16, 15, 19],
        'low': [9, 11, 10, 14, 13, 17],
        'close': [12, 11, 15, 14, 18, 17]
    }
    df = pd.DataFrame(data)
    analyzer = StructureAnalyzer(swing_window=1)
    res = analyzer.analyze_structure(df)
    print("Structure Test Result:", res)

if __name__ == "__main__":
    test()
