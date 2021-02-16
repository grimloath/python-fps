from time import perf_counter as current_time, sleep

class Fps():
    def __init__(self, target_fps):
        self.estimated_fps = 0
        self.on_time = True
        self.max_sleep_amount = 1 / target_fps
        self.time_marker = current_time()

    def tick(self):
        external_process_time = current_time() - self.time_marker
        sleep(max(0, self.max_sleep_amount - external_process_time)) 
        self.update_status(external_process_time)
        self.time_marker = current_time()

    def update_status(self, external_process_time):
        self.on_time = True
        if self.max_sleep_amount - external_process_time < 0:
            self.on_time = False 
        self.estimated_fps = 1 / (current_time() - self.time_marker)

    def status(self):
        return [round(self.estimated_fps), self.on_time]
