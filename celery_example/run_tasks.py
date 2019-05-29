from celery_example.tasks import hello_world
import time

if __name__ == '__main__':
    result = hello_world.delay()

    print(f'Task finished: {result.ready()}')
    print(f'Task result: {result.result}')

    time.sleep(5)

    print(f'fTask finished: {result.ready}')
    print(f'Task result: {result.result}')
