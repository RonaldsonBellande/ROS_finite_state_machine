#!/usr/bin/env python3
from functionalities.header_imports import *

class manipulation(smach.State):
    def __init__(self, val):
        smach.State.__init__(self, outcomes=['goal_found', 'goal_not_found', 'memory', 'error'], input_keys=['pose_index', 'look_poses'], output_keys=['pose_index'])
        
        self.outcome = None
        self.goal = None
        self.memory = None
    
    def execute(self, userdata):
        rospy.sleep(0.5)
        rospy.Subscriber('/goal', ,self.destination)
        rospy.sleep(0.5)
        rospy.Subscriber('/memory', ,self.memory)
        return self.outcome


    def destination(self):
        pass


    def memory(self):
        pass

