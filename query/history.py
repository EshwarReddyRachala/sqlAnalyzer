class QueryHistory:
    def __init__(self):
        self.history = []

    def add_query(self, query):
        if query not in self.history:
            self.history.append(query)

    def get_history(self):
        return self.history
