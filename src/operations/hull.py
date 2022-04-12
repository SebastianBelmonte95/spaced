from queue import Queue
from threading import Thread, Lock
from src.modules.hull import Hull
from src.utils.utils import logger


lock = Lock()


def repair_hull(hull: Hull, repair_queue: Queue) -> None:
    while True:
        _object = repair_queue.get()
        logger("Repairing " + _object)
        _object
        repair_queue.task_done()

    return
