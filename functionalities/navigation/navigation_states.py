#!/usr/bin/env python3

from functionalities.header_imports import *

class navigation(smach.State):
    def __init__(self, val):
        smach.State.__init__(self, outcomes = ['set_it'], output_keys = ['x'])
        self._val = val
    
    def execute(self, ud):
        # Set the data
        ud.x = self._val
        rospy.loginfo('>>> Set data: %s' % str(self._val))
        return 'set_it'
