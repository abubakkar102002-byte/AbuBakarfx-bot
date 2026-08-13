# strategy/hard_filters.py
from datetime import datetime

class HardFilters:
    def __init__(self, allowed_sessions=["LONDON", "NEW_YORK"]):
        self.allowed_sessions = allowed_sessions

    def check_session(self, current_time: datetime) -> bool:
        hour = current_time.hour
        # London Session: 8:00 - 16:00 UTC
        # New York Session: 13:00 - 21:00 UTC
        if 8 <= hour <= 21:
            return True
        return False

    def is_news_time(self, current_time: datetime) -> bool:
        # Placeholder for Economic News Filter Logic
        return False

    def can_trade(self, current_time: datetime) -> bool:
        session_valid = self.check_session(current_time)
        news_valid = not self.is_news_time(current_time)
        return session_valid and news_valid

