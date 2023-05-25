import os
import sys
import argparse

sys.path.append(".")
root_path = os.getcwd()
sys.path.insert(0, root_path)

import logger.logger as log

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--source_path",
            help="Path of the source folder to sync.",
            required=True)
        parser.add_argument(
            "--replica_path",
            help="Path to the replica folder.",
            required=True)
        # Define EITHER set hours of the day when to sync, OR define period of sync in minutes
        parser.add_argument(
            "--daily_sync",
            help="Define hours of the day when to sync.",
            required=False)
        parser.add_argument(
            "--sync_period",
            help="Define how often the sync should occur in minutes.",
            required=False)
        # Optional set log path
        parser.add_argument(
            "--log_path",
            help="Path to save log file.",
            required=False)

        args = parser.parse_args()
        source_path = args.source_path
        replica_path = args.replica_path
        daily_sync = args.daily_sync
        sync_period = int(args.sync_period)
        log_path = args.log_path

        assert os.path.isdir(
            source_path
        ), "Invalid Source path {} not found.".format(source_path)
        assert os.path.isdir(
            replica_path
        ), "Invalid Replica path {} not found.".format(replica_path)

        if daily_sync and sync_period:
            daily_sync = None
        elif daily_sync or sync_period:
            pass
        else:
            sync_period = 360

        try:
            os.path.isdir(log_path)
        except TypeError:
            log_path = "./logger"

        log_file_path = log.generate_name(log_path)
        log.initial_configuration(log_file_path)
        logger = log.setup(__name__)




    except Exception as e:
        print("ERROR OCCURRED : {}".format(e))

    finally:
        sys.exit()
