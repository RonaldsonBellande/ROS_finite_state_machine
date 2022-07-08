cmake_minimum_required(VERSION 3.0.2)
project(casm_state_machine_msgs)

find_package(catkin REQUIRED COMPONENTS actionlib_msgs)


add_message_files(
  FILES
  Casm_Command.msg
  Casm_Event.msg
  Casm_Event_Generator.msg
  Casm_Event_Update.msg
  Casm_Object.msg
  Casm_State.msg
  Casm_State_Behavior.msg
  Casm_State_Update.msg
  Casm_StateMachine.msg
  Casm_Fruits.msg
  Casm_Utensils.msg
  Casm_Cube_Color.msg
)

add_service_files(
  FILES
  CasmTransitionHistory.srv
)
## Generate actions in the 'action' folder
add_action_files(
  FILES
  Test.action
)
## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  actionlib_msgs  # Or other packages containing msgs
)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need

catkin_package(
  #  INCLUDE_DIRS include
  #  LIBRARIES lib
  #  CATKIN_DEPENDS packages
  #  DEPENDS system_lib
)

## mark examples for installation
install(
  DIRECTORY functionalities
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS
  FILES_MATCHING PATTERN "*.py"
  PATTERN ".svn" EXCLUDE
)
