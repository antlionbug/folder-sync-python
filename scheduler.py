import schedule
import time
import threading
from FileSyncer import FileSyncer


def parse_daily(daily_sync):
    return ",".split(daily_sync)


class SyncScheduler:
    def __init__(self, source, replica, daily_sync, sync_period, log_path):
        self.source = source
        self.replica = replica
        self.file_syncer = FileSyncer(source, replica, log_path)
        # self.run_thread()
        if daily_sync:
            self.daily_sync = parse_daily(daily_sync)
            self.run_daily()
        else:
            self.sync_period = sync_period
            self.run_periodically()

    def run_thread(self):
        job_thread = threading.Thread(target=self.file_syncer.sync_files)
        job_thread.start()

    def run_daily(self):
        for t in self.daily_sync:
            schedule.every().day.at(t).do(self.run_thread)

        while True:
            schedule.run_pending()
            time.sleep(10)

    def run_periodically(self):
        schedule.every(self.sync_period).minutes.do(self.run_thread)

        while True:
            schedule.run_pending()
            time.sleep(10)
