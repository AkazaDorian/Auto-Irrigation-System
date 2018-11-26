import subprocess

def command(command):
# run a bash command inside python
    process = subprocess.Popen(command.split(), stdout = subprocess.PIPE)
    output, error = process.communicate() # save output and error
    return output, error