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
    try:
        if not os.path.exists(lf):
            os.mknod(lf)
    except OSError as LOG_ERR:
        raise LOG_ERR
def get_log_file_name() -> str:
    try:
        return LOG_PRE+get_formatted_time_now()+LOG_EXT
    except OSError as LFN_ERR:
        raise LFN_ERR
def get_log_file_path() -> str:
    try:
        dir_ = pathlib.PurePath(get_project_root(), 'LOGS')
        if os.path.exists(dir_):
            return str(pathlib.PurePath(dir_, get_log_file_name()))
    except OSError as PATH_ERR:
        raise PATH_ERR
def get_project_root() -> str:
    try:
        return str(pathlib.PurePath(os.getcwd()).parent)
    except OSError as PTH_ERR:
        raise PTH_ERR
def get_formatted_time_now() -> str:
    try:
        return datetime.datetime.now().strftime(TS)
    except ValueError as DT_ERR:
        raise DT_ERR
def initialize_logger_for_package(lf):
    try:
        logging.basicConfig(filename=lf, filemode='w', level=logging.DEBUG)
        logging.Formatter(fmt=LF)
    except IOError as LOG_ERR:
        raise LOG_ERR
def log(event_msg):
    print(event_msg + " logged")
    logging.debug(event_msg)
def main():
    pass
if __name__ == '__main__':
    main()
lf = get_log_file_path()
initialize_logger_for_package(lf)
log(event_msg)
