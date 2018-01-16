import add_task

if __name__ == '__main__':
    result = add_task.add.delay(5, 5)
    print(result.ready())
    print(result.get(timeout=2))
