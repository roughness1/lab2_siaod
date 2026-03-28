class browser_history_record:
    def __init__(self,url,time,flag):
        self.url=url
        self.time=time
        self.flag=flag
      
class BrowserHistory:
    def __init__(self):
        self._history = []
        self._current_index = -1
    def clear_history(self):
        self._history.clear()
        self._current_index = -1
    def print_all(self):
        for record in self._history:
            print(record.url, record.time, record.flag)
    def forward(self):
        if not self._history:
            return None
        if self._current_index < len(self._history) - 1:
            self._current_index += 1
            return self._history[self._current_index]
        return None
    def back(self):
        if not self._history:
            return None
        if self._current_index > 0:
            self._current_index -= 1
            return self._history[self._current_index]
        return None
