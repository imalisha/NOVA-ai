from datetime import datetime


class HistoryService:

    def __init__(self):
        self.history = []

    # =========================================================
    # ADD HISTORY
    # =========================================================

    def add(
        self,
        command,
        response,
        success=True
    ):

        item = {
            "command": command,
            "response": response,
            "success": success,
            "time": datetime.now()
        }

        self.history.insert(
            0,
            item
        )

        # Keep latest 100 commands
        self.history = self.history[:100]

    # =========================================================
    # GET ALL
    # =========================================================

    def get_all(self):

        return self.history

    # =========================================================
    # CLEAR
    # =========================================================

    def clear(self):

        self.history.clear()

    # =========================================================
    # COUNT
    # =========================================================

    def count(self):

        return len(self.history)