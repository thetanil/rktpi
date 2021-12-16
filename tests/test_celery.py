import psutil
import pytest
from tasks import add


@pytest.fixture(autouse=True)
def rabbit_running():
    assert "rabbitmq-server" in (
        p.name() for p in psutil.process_iter()
    ), "rabbitmq not running"
    assert "celery" in (
        p.name() for p in psutil.process_iter()
    ), "celery not running"


def test_celery_basic_1(rabbit_running):
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
def test_bench_do_wait(benchmark, rabbit_running):
    benchmark(do_wait)


def forget_work():
    add.apply_async(args=[4, 4], ignore_result=True)


def test_bench_forget(benchmark, rabbit_running):
    benchmark(forget_work)


def no_wait():
    add.apply_async(args=[4, 4])


def test_bench_no_wait(benchmark, rabbit_running):
    benchmark(no_wait)
