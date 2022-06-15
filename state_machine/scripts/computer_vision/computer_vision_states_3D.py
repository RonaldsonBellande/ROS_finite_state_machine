#!/usr/bin/env python3
from functionalities.header_imports import *


class computer_vision_3D(smach.State):
    def __init__(self, val):
        smach.State.__init__(self, outcomes=['target_found', 'target_not_found', 'memory', 'error'], input_keys=['pose_index', 'look_poses'], output_keys=['pose_index'])
        
        self.outcome = None
        self.target = None
        self.memory = None
    
    def execute(self, userdata):
        rospy.sleep(0.5)
        rospy.Subscriber('/target', ,self.detection)
        rospy.sleep(0.5)
        rospy.Subscriber('/memory', ,self.memory)
        return self.outcome


    def detection(self):
        pass


    def memory(self):
        pass
