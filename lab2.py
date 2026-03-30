import base64
from urllib.parse import urlparse

class BrowserHistoryRecord:
    
    def __init__(self,url,time,flag):
        self.url=url
        self.time=time
        self.flag=flag
      
class BrowserHistory:

    def __init__(self):
        self._history = []
        self._current_index = -1
        
    def add_record(self, url, time, flag):
        new_record = BrowserHistoryRecord(url, time, flag)
        if self._current_index < len(self._history) - 1:
            self._history = self._history[:self._current_index + 1]
        self._history.append(new_record)
        self._current_index = len(self._history) - 1
        
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
        
    def _get_domain(self, url):
        parsed = urlparse(url)
        return parsed.netloc or parsed.path
        
    def top_n_transitions(self, n):
        if len(self._history) < 2 or n <= 0:
            return []   
        transitions = {}
        for i in range(len(self._history) - 1):
            from_domain = self._get_domain(self._history[i].url)
            to_domain = self._get_domain(self._history[i + 1].url)
            if from_domain == to_domain:
                continue
            transition = (from_domain, to_domain)
            transitions[transition] = transitions.get(transition, 0) + 1
        sorted_transitions = sorted(transitions.items(), key=lambda x: x[1], reverse=True)
        return sorted_transitions[:n]
        
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            for record in self._history:
                line = f"{record.url}|{record.time}|{record.flag}"
                encoded = base64.b64encode(line.encode()).decode()
                f.write(encoded + "\n")
                
    def search_by_domain(self, domain):
        result = []
        for record in self._history:
            if self._get_domain(record.url) == domain:
                result.append(record)
        return result
