from CONSTANTS.FORMAT import *
from CONSTANTS.NAMES import *
import datetime
import logging
import os
import pathlib
event_msg = "importing board_interface.."
def cleanup_logs():
    pass
def create_log(lf):
    if not os.path.exists(lf):
        os.mknod(lf)
def get_log_file_name() -> str:
    return LOG_PRE+get_formatted_time_now()+LOG_EXT
def get_log_file_path() -> str:
    dir_ = pathlib.PurePath(get_project_root(), 'LOGS')
    try:
        if os.path.exists(dir_):
            return str(pathlib.PurePath(dir_, get_log_file_name()))
    except OSError as PATH_ERR:
        raise PATH_ERR
def get_project_root() -> str:
    return str(pathlib.PurePath(os.getcwd()).parent)
def get_formatted_time_now() -> str:
    return datetime.datetime.now().strftime(TS)
def initialize_logger_for_package(lf):
    logging.basicConfig(filename=lf, filemode='w', level=logging.DEBUG)
    logging.Formatter(fmt=LF)
def log(event_msg):
    print(event_msg + " logged")
    logging.debug(event_msg)
def main():
    lf = get_log_file_path()
    initialize_logger_for_package(lf)
    log(event_msg)
if __name__ == '__main__':
    main()
