import time
import pytest
from tasks import add


def test_celery_basic_1():
    r = add.delay(999, 999)
    assert r.get(timeout=1) == 999 + 999


def do_wait():
    add.apply_async(args=[4, 4]).get()


# @pytest.mark.benchmark(
#     group="group-name",
#     min_time=0.1,
#     max_time=0.5,
#     min_rounds=100,
#     timer=time.time,
#     disable_gc=False,
#     warmup=True,
# )
def test_bench_do_wait(benchmark):
    benchmark(do_wait)


def forget_work():
    add.apply_async(args=[4, 4], ignore_result=True)


def test_bench_forget(benchmark):
    benchmark(forget_work)


def no_wait():
    add.apply_async(args=[4, 4])


def test_bench_no_wait(benchmark):
    benchmark(no_wait)
