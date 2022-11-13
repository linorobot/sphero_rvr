# spherorvr-ros2
Minimal implementation of a ROS2 node for the Sphero RVR robot. See hardware description at [ROS2 Robot (Sphero RVR) with Localization, Navigation, AI, and a Thermal Imager](https://youtu.be/RVCkEL206kc).

## Installation

    git clone https://github.com/sphero-inc/sphero-sdk-raspberrypi-python
    cd sphero-sdk-raspberrypi-python
    pip install .
    cd <your_ws>
    git clone https://github.com/linorobot/sphero_rvr src/sphero_rvr
    colcon build

## PI Configuration
### Remove console logging:

    sudo nano /boot/firmware/cmdline.txt 

* Once open, remove `console=serial0, 115200`

### Install udev rules:

    bash install_udev_rule.sh

* Reboot computer once done.
