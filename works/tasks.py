import random
import time

from works.models import Work

from celery import shared_task


@shared_task
def task_process_work() -> None:

    def f(n: int) -> object:
        return 1 if n <= 1 else f(n-1) + f(n-2)

    tick = time.time()
    n = random.randrange(35, 42)

    work = Work.objects.create(
        n=n,
        result=f(n),
        elapsed_time=str(time.time() - tick),
    )

    work.save()

    print(f'{work.id}')
    print(f'Processed work with n={n} in {time.time() - tick} seconds')