import os
import shutil
import logger.logger as log


def remove_file(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)  # remove the file
    else:
        raise ValueError("file {} is not a file.".format(path))


class FileSyncer:
    def __init__(self, source, replica, log_path):
        self.source_path = source
        self.replica_path = replica
        self.log_path = log_path
        self.source_files = None
        self.replica_files = None
        self.update_file_lists()

        log_file_path = log.generate_name(self.log_path)
        log.initial_configuration(log_file_path)
        self.logger = log.setup(__name__)

    def update_file_lists(self):
        self.source_files = os.listdir(self.source_path)
        self.source_files.sort()
        self.replica_files = os.listdir(self.replica_path)
        self.replica_files.sort()

    def sync_files(self):
        self.update_file_lists()
        print(self.source_files)
        self.logger.info(f"Synchronizing {self.source_path} and {self.replica_path}...")
        delete_list = []
        for f in self.replica_files:
            if f not in self.source_files:
                delete_list.append(f)

        for f in delete_list:
            tmp_path = self.replica_path + f
            remove_file(tmp_path)
            self.logger.info(f"{tmp_path} deleted.")

        for f in self.source_files:
            src = self.source_path + f
            dst = self.replica_path + f
            if f in self.replica_files and (os.path.getmtime(src) == os.path.getmtime(dst)):
                pass
            else:
                shutil.copy2(src, dst)
                self.logger.info(f"{src} has been copied to {dst}.")

