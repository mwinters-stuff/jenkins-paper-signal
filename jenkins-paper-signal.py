import jenkins
import time

JENKINS_SERVER = 'http://gonzalas:9090'
JENKINS_USERNAME = 'jj'
JENKINS_PASSWORD = 'jjp'
JENKINS_JOB = 'test_jenkins_notify'

SERVO_NUMBER = 0
SERVO_DEVICE = '/dev/servoblaster'

if __name__ == '__main__':
    print("Using Jenkins Server %s" % JENKINS_SERVER)

    last_position = 33

    server = jenkins.Jenkins(JENKINS_SERVER, JENKINS_USERNAME, JENKINS_PASSWORD)
    while True:
        job = server.get_job_info(JENKINS_JOB)
        status = job['color']

        arrow_position = 50
        if status.startswith('red'):
            arrow_position = 5
        if status.startswith('blue'):
            arrow_position = 100

        servo_command = "%d=%d%%\n" % (SERVO_NUMBER, arrow_position)

        print("Status colour %s position %d%% command %s" % (status, arrow_position, servo_command))

        if arrow_position != last_position:
            dev = open(SERVO_DEVICE, 'wb')
            dev.write(servo_command)
            dev.close()
            last_position = arrow_position
        time.sleep(15)



