#!/usr/bin/env bash

from optparse import OptionParser
import logging
import traceback
import sys

logger = logging.getLogger()


# ###########################################################
# ##################### General methods  ####################
# ###########################################################

# ####################################
# # Set the logger
# ####################################
def set_logger(options):

    if options.LOG_LEVEL is not None:
        log_level = options.LOG_LEVEL
    else:
        log_level = "INFO"

    log_numeric_level = getattr(logging, log_level.upper())

    if not isinstance(log_numeric_level, int):
        raise ValueError('ERROR : Invalid log level: {}'.format(log_level))

    logger.setLevel(level=log_numeric_level)
    # formatter = logging.Formatter('%(levelname)s:\t%(asctime)s\t%(message)s')

    # create formatter and add it to the handlers
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Set console handler
    logger.addHandler(logging.StreamHandler(sys.stdout))

    return logger



# ######################################################
# Get the cli parameters
# ######################################################
def get_cli_params():
    parser = OptionParser()
    parser.add_option('-l', '--loglevel', dest='LOG_LEVEL', help='Log level : DEBUG, ERROR, WARNING, INFO ')
    parser.add_option('-t', '--tarfile', dest='TAR_FILE', help='Tar file location')
    parser.add_option('-p', '--p4user', dest='P4_USER', help='P4 User')
    parser.add_option('-v', '--csi_ver', dest='CSI_VER', help='CSI Version (i.e 5.0.0)')
    parser.add_option('-r', '--release_num', dest='RELEASE_NUM', help='Release number in BaRT (i.e 10897)')
    parser.add_option('-f', '--csi_full_ver', dest='CSI_FULL_VER', help='CSI Full Version number')

    ## BOOLEAN
    parser.add_option('-c', '--changed_components_only', action="store_true" , dest='CHANGED_COMPONENTS_ONLY', default=False , help='run the p4pushall only on changed components')

    ## DEFALUT LIST
    parser.add_option('-e', '--exclude_components_list', dest='EXCLUDE_COMPONENTS_LIST' , default=[], type=str, action='append', help='Exclude components list (will not sync them though there is a diff)')
    parser.add_option('-u', '--users_list', dest='USERS_LIST', help='users list (send mail)')
    (options, args) = parser.parse_args()
    return options




# #################################
#
#
#           M A I N
#
#
# #################################
def main():
    options = get_cli_params()
    set_logger(options)



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Exception traceback:")
        print(traceback.print_exc())
        # logger.exception("Could not finish cloudera configuration phase, please check log and rerun.")
        print("Exception message")
        print(e.message)
        exit(1)
