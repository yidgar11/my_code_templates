        retries=0
        while [ $retries -le 5 ] ; do
            if [ $(docker ps | grep ${container} | wc -l) -eq 1 ]; then
                sleep 5
                ((retries++))
            fi
