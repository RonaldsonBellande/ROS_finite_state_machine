from header_imports import *

if __name__ == "__main__":
    
    rospy.init_node('robot functionality')
    state_machine = smach.StateMachine(outcomes=['', ''])


    with state_machine_detection:
        smach.StateMachine.add('computer_vision', computer_vision_2d(), 
                               transitions={'target':'BAR', 
                                            'outcome2':'outcome4'})

        smach.StateMachine.add('computer_vision', computer_vision_2d(), 
                               transitions={'target':'BAR', 
                                            'outcome2':'outcome4'})

        smach.StateMachine.add('speech_recognition', speech_detection(), 
                               transitions={'target':'BAR', 
                                            'outcome2':'outcome4'})

        smach.StateMachine.add('speech_output', speech_output(), 
                               transitions={'goal':'BAR', 
                                            'outcome2':'outcome4'})


        smach.StateMachine.add('navigation', navigation(), 
                               transitions={'goal':'BAR', 
                                            'outcome2':'outcome4'})

        smach.StateMachine.add('manipulation', manipulation(), 
                                transitions={'goal':'BAR', 
                                            'outcome2':'outcome4'})

        smach.StateMachine.add('mimicking', mimicking(), 
                                transitions={'goal':'BAR', 
                                            'outcome2':'outcome4'})

        smach.StateMachine.add('speech_output', mimicking(), 
                               transitions={'target':'BAR', 
                                            'outcome2':'outcome4'})


    state_machine_server = smach_ros.IntrospectionServer('state_machine_server', state_machine, '/SM_ROOT')
    state_machine.start()

    outcome = state_machine.execute()
    
    rospy.spin()
    state_machine.stop()




    
