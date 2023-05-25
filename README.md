# folder-sync-python
Small python program periodically keeping 2 folders in sync. Interview task.

Tested on Windows only

## Setup

Clone repo:
```
git clone https://github.com/antlionbug/folder-sync-python.git
```
Prepare virtualenv
```
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
```
Install requirements.txt
```
pip install -r requirements.txt
```

## Run

Arguments:

- Mandatory
  - "--source_path" => path to source directory
  - "--replica_path" => path to the replica directory
- Optional(have default values)
  - "--daily_sync" => defined times of the day when to sync, default None and sync_period if defined beats daily_sync
  - "--sync_period" => period in minutes between each sync, default 360min
  - "--log_path" => path to save logs, default in the "./logger" dir

Example initialization command
```
python main.py --source_path G:\test_source\ --replica_path G:\test_replica\ --daily_sync 16:00,13:18,06:25
```