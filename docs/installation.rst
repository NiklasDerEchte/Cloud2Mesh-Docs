Installation Guide
==================

Prerequisites
-------------

To get started, ensure you have the following:

..
   - **Microsoft HoloLens** (HoloLens 2 recommended).
   - **Zivid Camera** with `drivers <https://support.zivid.com/en/latest/getting-started/software-installation.html>`__ installed.

- A source with PointCloud2 data via ROS2. 
   - For example, from a 3D camera or a ROS2 bag file. 
   - I use `Zivid-ROS <https://github.com/zivid/zivid-ros>`__ with `drivers <https://support.zivid.com/en/latest/getting-started/software-installation.html>`__.
- `ROS2 <https://github.com/ros2/ros2>`__ version: `Humble <https://docs.ros.org/en/humble/Installation.html>`__.
- **Unity 2021 or higher**.
- For debug
   - rqt (ROS2 GUI tool).
   - rviz (ROS2 visualization tool).
   - ParaView (3D visualization tool).

**ROSPointCloudMeshify Requirements**:

- A **C++ compiler** (GCC, Clang, or MSVC).
- `ROS2 Humble installation <https://docs.ros.org/en/humble/Installation.html>`__ installation with support for `sensor_msgs`.
- `PointCloud Library <https://pointclouds.org/downloads/>`__ (**PCL**) installed.

You also need the following ROS packages:

.. code-block:: bash

   sudo apt install ros-humble-pcl-conversions ros-humble-pcl-ros

.. code-block:: bash

   sudo apt install ros-humble-visualization-msgs

.. code-block:: bash

   sudo apt install libpcap-dev

**ROSUnityRenderer Requirements**:

..
   - Mixed Reality Toolkit (**MRTK**) for HoloLens.
   - AR Foundation.

- `Unity <https://unity.com/de/download>`__ Editor 2021 or higher.
- `Unity-Robotics-Hub <https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/README.md>`_ needs an `endpoint to the ros environment <https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/setup.md#-ros2-environment>`_

..
   Unity-Robotics-Hub


Installation Steps
------------------

**1. ROSPointCloudMeshify**:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/NiklasDerEchte/ROSPointCloudMeshify

2. Build the project:

   .. code-block:: bash

      colcon build
      source install/setup.bash

**2. ROSUnityRenderer**:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/NiklasDerEchte/ROSUnityRenderer

2. Open the project in Unity Editor.

3. Import required Unity packages:
   - `ROS-TCP-Connector <https://github.com/Unity-Technologies/ROS-TCP-Connector>`__

..
   - Mixed Reality Toolkit (**MRTK**)
   - **AR Foundation**

.. 
   4. Build the project for HoloLens:
      - Switch platform to UWP.
      - Configure project settings for HoloLens.
   5. Deploy the app to the HoloLens.