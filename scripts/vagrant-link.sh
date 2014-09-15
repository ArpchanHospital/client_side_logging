#!/bin/sh -x

PATH_OF_CURRENT_SCRIPT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source $PATH_OF_CURRENT_SCRIPT/vagrant/vagrant_functions.sh

run_in_vagrant -c "sudo rm -rf /var/www/client-side-logging"
run_in_vagrant -c "sudo rm -rf /usr/lib/python2.6/site-packages/client_side_logging.py"
run_in_vagrant -c "sudo ln -s /Project/client-side-logging /var/www/client-side-logging"
run_in_vagrant -c "sudo ln -s /Project/client-side-logging/client_side_logging.py /usr/lib/python2.6/site-packages/client_side_logging.py"
run_in_vagrant -c "sudo chown -h jss:jss /var/www/client-side-logging"
run_in_vagrant -c "sudo chown -h jss:jss /usr/lib/python2.6/site-packages/client_side_logging.py"