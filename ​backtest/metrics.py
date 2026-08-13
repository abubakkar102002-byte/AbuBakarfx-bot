# backtest/metrics.py

class PerformanceMetrics:
    @staticmethod
    def calculate_win_rate(trades: list) -> float:
        if not trades:
            return 0.0
        wins = sum(1 for t in trades if t.get('pnl', 0) > 0)
        return round((wins / len(trades)) * 100, 2)

