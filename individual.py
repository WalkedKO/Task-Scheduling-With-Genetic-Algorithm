from random import randint, sample
from productTag import ProductTag
"""
A single individual in "the specie". One schedule of a day that describes what will each
worker do.

Attributes:
workers_set: list(worker)
    list of all workers in the day 
products_set: list(product)
    list of all possible products
hours: int
    number of time units
workers_nr: int
    number of workers
schedule: list(list(product))
    each row represents a worker and each element one time unit. If it's none, the worker does nothing.
    Else there should be a product which worker is producing at the time unit. 
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
        self.schedule = [[None for i in range(hours)] for j in range(self.workers_nr)]
        self.schedule_tags =  [[ProductTag.NORMAL for i in range(hours)] for i in range(self.workers_nr)]

    def place_in_schedule(self, prod_id, start, worker, worker_id):
        """
        Places product of id prod_id, to start hour, at worker, at worker_id
        :param prod_id: id of product to be placed
        :param start: start hour
        :param worker: worker which will receive the product to its schedule
        :param worker_id: id of worker from previous parameter
        :return:
        """
        worker_schedule = self.schedule[worker_id]
        product = worker.can_produce[prod_id]
        free = True
        hours_needed = product.time
        for j in range(start, start + hours_needed):
            if worker_schedule[j] is not None:
                free = False
                break
        if free:
            for j in range(start, start + hours_needed):
                worker_schedule[j] = worker.can_produce[prod_id]
            self.schedule_tags[worker_id][start] = ProductTag.START
            self.schedule_tags[worker_id][start + hours_needed - 1] = ProductTag.STOP


    def randomize(self, stop):
        """
                    Creates a completely random schedule, and saves it into the self.schedule. Used for
                    generating the first generation.
                    :param stop: (int) numbers of attempts to stop randomizing
            """
        for i, worker in enumerate(self.workers_set):
            attempts = 0
            # trying to put random products in a worker shchedule. In case when there's no room for
            # any product, the randomizer will stop after 10 attemps.
            while attempts <= stop:
                job = randint(0, len(worker.can_produce) - 1)
                while True:
                    start = randint(0, self.hours - 1)
                    hours_needed = worker.can_produce[job].time
                    if start + hours_needed < self.hours:
                        break
                self.place_in_schedule(job, start, worker, i)
                attempts += 1
    def crossover_inside(self, father_schedule, mother_schedule, father_tags, mother_tags):
        """
        Creates a schedule for a single worker from two other schedules.
        Selects a random part of father's schedule which starts with start tag and ends with stop tag
        and injects it into random position on mother's schedule.
        :param father_schedule: schedule of one parent's (called father) worker
        :param mother_schedule: schedule of another parent's (called mother) worker, but must be the same worker type as in first
        :param father_tags: list of tags in father's schedule
        :param mother_tags: list of tags in mother's schedule

        :return: tuple, combined schedule for the worker and combined tag schedule
        """

        starts = [i for i, tag in enumerate(father_tags) if tag == ProductTag.START]
        start = sample(starts, 1)[0]
        stops = [i for i in range(start, len(father_tags)) if father_tags[i] == ProductTag.STOP]
        stop = sample(stops, 1)[0] + 1
        block_len = stop - start
        to_replace = father_schedule[start:stop]
        to_replace_tag = father_tags[start:stop]

        mother_start = randint(0, (len(mother_schedule) - block_len))
        mother_stop = mother_start + block_len
        result = mother_schedule[:mother_start] + to_replace + mother_schedule[mother_stop:]
        tag_result = mother_tags[:mother_start] + to_replace_tag + mother_tags[mother_stop:]
        return result, tag_result
    def crossover(self, father, mother):
        """
            Creates the schedule from combining schedules of two parents.
            Chooses some of the workers to copy father schedule and some to crossover mother and father schedule.
            :param father: (Schedule) one parent
            :param mother: (Schedule) second parent

        """
        from_father = sample(range(self.workers_nr), int(self.workers_nr / 2))
        for i in range(self.workers_nr):
            father_schedule = father.schedule[i].copy()
            father_tags = father.schedule_tags[i].copy()
            if i in from_father:
                self.schedule[i], self.schedule_tags[i] = father_schedule, father_tags
            else:
                self.schedule[i], self.schedule_tags[i] = self.crossover_inside(father_schedule, mother.schedule[i].copy(), father_tags, mother.schedule_tags[i].copy())
    def evaluate_fitness(self):
        """
        Evaluates the schedule fitness score.
        :return: int
            Fitness score of the schedule
        """
        # some products require components
        ready_products = []
        to_remove_products = []
        score = 1.0
        timers = [0 for i in self.schedule]
        for hour in range(self.hours):
            for i, worker in enumerate(self.schedule):
                product_current = worker[timers[i]]
                tag_current = self.schedule_tags[i][timers[i]]
                if product_current is None:
                    timers[i] += 1
                elif tag_current == ProductTag.NORMAL:
                    timers[i] += 1
                elif tag_current == ProductTag.STOP:
                    ready_products.append(worker[timers[i]])
                    timers[i] += 1
                elif tag_current == ProductTag.START:
                    done = True
                    for needed in product_current.needed:
                        if needed in ready_products:
                            ready_products.remove(needed)
                            to_remove_products.append(needed)
                        else:
                            done = False
                            for prod in to_remove_products:
                                ready_products.append(prod)
                            break
                    if done:
                        timers[i] += 1
                    to_remove_products.clear()
        for prod in ready_products:
            score += prod.value
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
                    line += "|"
                else:
                    line += "   |"
            print(line)
        print(self.evaluate_fitness())