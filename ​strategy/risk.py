# strategy/risk.py

class RiskManager:
    def __init__(self, account_balance=10000, risk_per_trade_pct=1.0):
        self.account_balance = account_balance
        self.risk_per_trade_pct = risk_per_trade_pct

    def calculate_position_size(self, entry_price: float, stop_loss: float, pip_value=10.0) -> float:
        risk_amount = self.account_balance * (self.risk_per_trade_pct / 100.0)
        sl_pips = abs(entry_price - stop_loss)
        
        if sl_pips == 0:
            return 0.0

        lot_size = risk_amount / (sl_pips * pip_value)
        return round(lot_size, 2)

    def calculate_tp(self, entry_price: float, stop_loss: float, rr_ratio=3.0) -> float:
        risk = abs(entry_price - stop_loss)
        if entry_price > stop_loss: # Buy Trade
            return entry_price + (risk * rr_ratio)
        else: # Sell Trade
            return entry_price - (risk * rr_ratio)

