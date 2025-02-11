#!/bin/bash


function usage {
	echo "usage $(basename $0) TBD "
    	exit 1
}


# read variables
    while getopts "c:t:b:" arg; do
      case ${arg} in
        c)
                CLUSTER="$OPTARG"
                ;;
        t)
                THRESHOLD="$OPTARG"
                ;;
        b)
                BW_PER_SEC="$OPTARG"
                ;;
        *)
		usage
               ;;
      esac
    done
shift $((OPTIND-1))

## Handle defaults
[[ -z ${CLUSTER} ]] && CLUSTER="mr"
if  [[ ! ${CLUSTER} =~ ^(mr|'int')$ ]]; then
	echo -e "ERROR: CLUSTER name ${CLUSTER} is not acceptable . It can be \'int\' or \'mr\' \n"
	usage
fi
[[ -z ${THRESHOLD} ]] && THRESHOLD=5
[[ -z ${BW_PER_SEC} ]] && BW_PER_SEC=268435456

function check_balancer_run()
{
	echo -e "\nChecking if Previous HDFS Balancer is running : "
	if [[ ${RESULT} == 0 ]] ; then {
		echo -e "\nPrevious HDFS Balancer is running , cannot run another one ... \nPlease handle the current balancer which is running ."
		exit 1
		}
	else
		echo -e "\nPrevious HDFS Balancer is not running . Starting now ... "
	fi
}


###### MAIN ####

check_balancer_run

run_balancer

exit 0
