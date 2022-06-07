from header_imports import *

if __name__ == "__main__":
    
    rospy.init_node('robot functionality')
    state_machine = smach.StateMachine(outcomes=['', ''])


    with state_machine:
        smach.StateMachine.add('computer vision', computer_vision(), 
                               transitions={'outcome1':'BAR', 
                                            'outcome2':'outcome4'})


        smach.StateMachine.add('speech recognition', speech_detection(), 
                               transitions={'outcome2':'FOO'})


        smach.StateMachine.add('navigation', navigation(), 
                               transitions={'outcome1':'BAR', 
                                            'outcome2':'outcome4'})


        smach.StateMachine.add('manipulation', manipulation(), 
                               transitions={'outcome2':'FOO'})


        smach.StateMachine.add('mimicking', mimicking(), 
                               transitions={'outcome2':'FOO'})

         smach.StateMachine.add('speech_output', mimicking(), 
                               transitions={'outcome2':'FOO'})


    state_machine_server = smach_ros.IntrospectionServer('state_machine_server', state_machine, '/SM_ROOT')
    state_machine.start()

    outcome = state_machine.execute()
    
    rospy.spin()
    state_machine.stop()




    
