"""
AWS dramatiq actors entrypoint
"""

# test
import math
import os
import time

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

RMQ_URL = os.getenv("RMQ_URL", "amqp://localhost")

rabbitmq_broker = RabbitmqBroker(url=RMQ_URL)
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor
def do_work():
    for id in range(10000):
        do_some_more_work.send(id)


@dramatiq.actor
def do_some_more_work(id: int):
    light_cpu_workload(id)


def light_cpu_workload(id: int):
    start = time.time()
    total = 0
    for i in range(1, 100_000):  # small loop
        total += math.sqrt(i)
    duration = time.time() - start
    print(f"CPU task {id} done in {duration:.3f}s, result={total:.2f}")
