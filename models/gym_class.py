class Gym_class:
    def __init__(self, name, date, start_time, duration, max_capacity, active=True, id=None):
        self.name = name
        self.date = date
        self.start_time = start_time
        self.duration = duration
        self.max_capacity = max_capacity
        self.active = active
        self.id = id