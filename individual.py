from random import randint
"""
A single individual in "the specie". One schedule of a day that describes what will each
worker do.

Attributes:
workers_set: list(worker)
    list of all workers in the day 
products_set: list(product)
    list of all possible products
hours: int
    number of working hours
workers_nr: int
    number of workers
schedule: list(list(product))
    each row represents a worker and each element one working our. If it's none, the worker does nothing.
    Else there should be a product which worker is producing at the hour. 
"""
class Schedule:
    def __init__(self, workers_set, products_set, hours):
        """

        :param workers_set: list(worker)
            set of all workers in the day
        :param products_set: list(product)
            list of all possible products
        :param hours: int
            number of working hours
        """
        self.workers_set = workers_set.copy()
        self.products_set = products_set.copy()
        self.hours = hours
        self.workers_nr = len(workers_set)
        self.schedule = [[None] * hours] * self.workers_nr
    def randomize(self):
        """
        Creates a completely random schedule, and saves it into the self.schedule. Used for
        generating the first generation.
        """
        for i, worker in enumerate(self.workers_set):
            attempts = 0
            # trying to put random products in a worker shchedule. In case when there's no room for
            # any product, the randomizer will stop after 10 attemps.
            while attempts <= 10:
                job = randint(0, len(worker.can_produce) - 1)
                while True:
                    start = randint(0, self.hours - 1)
                    hours_needed = worker.can_produce[job].time
                    if start + hours_needed < self.hours:
                        break
                free = True
                for j in range(start, start + hours_needed):
                    if self.schedule[i][j] is not None:
                        free = False
                        break
                if free:
                    for j in range(start, start + hours_needed):
                        self.schedule[i][j] = worker.can_produce[job]
                attempts += 1

    def evaluate_fitness(self):
        """
        Evaluates the schedule fitness score.
        :return: int
            Fitness score of the schedule
        """
        # some products require components
        ready_products = []
        score = 0.0
        new_schedule = self.schedule.copy()
        # removing the duplicates. Products in schedule represents what the worker does in the specific hour.
        # we want to calculate only which product they produce, not how long
        for worker in new_schedule:
            for i in range(len(worker) - 1):
                if worker[i] is not None and worker[i + 1] is not None and worker[i].name == worker[i + 1].name:
                    worker[i] = None
            for hour in worker:
                if hour is not None:
                    done = True
                    for component in hour.needed:
                        if component in ready_products:
                            ready_products.remove(component)
                        else:
                            done = False
                    if done:
                        ready_products.append(hour)
        for product in ready_products:
            score += product.value
        return score
    def print(self):
        """
        For debuging. Prints random and fitness score
        """
        for worker in self.schedule:
            line = " "
            for hour in worker:
                if hour is not None:
                    line += hour.name
            print(line)
            print(self.evaluate_fitness())