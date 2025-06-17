from collections import deque, Counter
from typing import List, Dict

class LogSystem:
    def __init__(self, capacity: int = 10):
        self.logs_per_user: Dict[str, List[Dict]] = {}
        self.recent_logs: deque = deque(maxlen=capacity)
        self.log_levels: Counter = Counter()

    def add_log(self, line: str) -> None:
        parts = line.split(" ", 3)
        timestamp, level, user_id, message = parts[0].strip("[]"), parts[1], parts[2].strip(":"), parts[3]

        log_entry = {"timestamp": timestamp, "level": level, "user": user_id, "message": message}

        if user_id not in self.logs_per_user:
            self.logs_per_user[user_id] = []
        self.logs_per_user[user_id].append(log_entry)

        self.recent_logs.append(log_entry)

        self.log_levels[level] += 1

    def get_user_logs(self, user_id: str) -> List[Dict]:
        return self.logs_per_user.get(user_id, [])

    def count_levels(self) -> Dict[str, int]:
        return dict(self.log_levels)

    def filter_logs(self, keyword: str) -> List[Dict]:
        keyword = keyword.lower()
        return [log for log in self.recent_logs if keyword in log["message"].lower()]

    def get_recent_logs(self) -> List[Dict]:
        return list(self.recent_logs)
logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]

log_system = LogSystem(capacity=5)

for log in logs:
    log_system.add_log(log)

print(log_system.get_user_logs("user1"))
print(log_system.count_levels())
print(log_system.filter_logs("Timeout"))
print(log_system.get_recent_logs())