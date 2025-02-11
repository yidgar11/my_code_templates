__author__ = 'yidgar'
import subprocess
import json
import ConfigParser
import shlex
import getpass



##########################
# Note, that Popen is low-level function and it's recommended by Python docs to use subprocess.run:
#    The recommended approach to invoking subprocesses is to use the run() function for all use cases it can handle.
#    For more advanced use cases, the underlying Popen interface can be used directly.
# 
#    For instance you'd need to use only capture_output=True and won't need to wait till completion of curl using process.communicate()....
##########################



## https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module

subprocess.run(["ls", "-l"])  # doesn't capture output
CompletedProcess(args=['ls', '-l'], returncode=0)

subprocess.run("exit 1", shell=True, check=True)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n', stderr=b'')






def runBashCommandSimple(cmd):
    process = subprocess.Popen(cmd, shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    # wait for the process to terminate
    out, err = process.communicate()



# Cooamd with pipe
##mvn dependency:tree -DoutputType=dot -f /Users/yidgar/work/akamai/csi-core/csi-pulsar/pom.xml -DskipTests  | grep -v WARNING
def runBashCommand1(cmd):
    commandOut=""
    commandStr="None"

    cmd = ['ls', '-l']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              stdin=subprocess.PIPE)
    out, err = p.communicate('foo\nfoofoo\n')
    print out


def runBashCommand2(mainCmd,pipeCmd ):

    proc1 = subprocess.Popen(shlex.split(mainCmd),stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(shlex.split(pipeCmd),stdin=proc1.stdout,
    stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    proc1.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.
    out, err = proc2.communicate()
    print out

cmd = ['ls', '-l']
runBashCommandSimple(cmd)
runBashCommand1(cmd)

mainCmd = "ls -l"
pipeCmd= "grep mvn"
runBashCommand2()


