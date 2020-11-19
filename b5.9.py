import time

class Timing:
    def __init__(self, function_to_run):
        self.num_runs = 10
        self.func_to_run = function_to_run

    def __call__(self, *args, **kwargs):
        avg = 0
        for i in range(self.num_runs):
            t0 = time.time()
            self.func_to_run(*args, **kwargs)
            t1 = time.time()
            avg += (t1 - t0)
        avg /= self.num_runs
        print("Среднее время выполнения: %.5f секунд" % avg)
        return self.func_to_run(*args, **kwargs)

@Timing
def f():
    for j in range(1000000):
        pass

f()