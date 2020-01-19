import schedule
import time
import os

INTERVAL = 10

def start_script():
    cmd = "python meditate.py"
    os.system(cmd)

def runTask():
    try:
        schedule.every(INTERVAL).minutes.do(start_script)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    runTask()