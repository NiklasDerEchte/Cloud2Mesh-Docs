Installation Guide
==================

Prerequisites
-------------

To get started, ensure you have the following:

..
   - **Microsoft HoloLens** (HoloLens 2 recommended).
   - **Zivid Camera** with `drivers <https://support.zivid.com/en/latest/getting-started/software-installation.html>`__ installed.

- A PointCloud2 source for ROS2. In my example: `zivid-ros <https://github.com/zivid/zivid-ros>`__ with `drivers <https://support.zivid.com/en/latest/getting-started/software-installation.html>`__.
   - Make sure that the Zivid camera is on the same network as the ROS2 driver. You can test this with Zivid Studio. (Default IP: 172.28.60.XXX/24)
- `ROS2 <https://github.com/ros2/ros2>`__ version: `Humble <https://docs.ros.org/en/humble/Installation.html>`__.
- `Unity 2021 or higher <https://unity.com/de/download>`__.

- For debug
   - rqt (ROS2 GUI tool).
   - rviz (ROS2 visualization tool).
   - ParaView (3D visualization tool).

**ROSPointCloudMeshify Requirements**:

- A **C++ compiler** (GCC, Clang, or MSVC).
- `ROS2 Humble installation <https://docs.ros.org/en/humble/Installation.html>`__ installation with support for `sensor_msgs`.
- `PointCloud Library <https://pointclouds.org/downloads/>`__ installed.

You also need the following ROS packages:

.. code-block:: bash

   sudo apt install ros-humble-pcl-conversions ros-humble-pcl-ros

.. code-block:: bash

   sudo apt install ros-humble-visualization-msgs

.. code-block:: bash

   sudo apt install libpcap-dev

**ROSUnityBIRPMeshViz Requirements**:

..
   - Mixed Reality Toolkit (**MRTK**) for HoloLens.
   - AR Foundation.

- `Unity <https://unity.com/de/download>`__ Editor 2021 or higher.
- `Unity-Robotics-Hub <https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/README.md>`_
   - ``ROS-TCP-Connector``: The Unity package with the C# API.
   - ``ROS-TCP-Endpoint``: ROS environment endpoint node for the TCP connection. `How to set up the endpoint <https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/setup.md#-ros2-environment>`__


Installation Steps
------------------

**1. ROSPointCloudMeshify**:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/NiklasDerEchte/ROSPointCloudMeshify

2. Build the project in `object_detection/`:

   .. code-block:: bash

      colcon build
      source install/setup.bash

**2. ROSUnityBIRPMeshViz**:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/NiklasDerEchte/ROSUnityBIRPMeshViz

2. Open the project in Unity Editor.

3. Import required Unity packages:

   - `GitHub ROS-TCP-Connector <https://github.com/Unity-Technologies/ROS-TCP-Connector>`__ [1]_


.. [1] Currently, there is a bug in version ``0.7.0`` of ``ROS-TCP-Connector``. 
   Therefore, it is better to use my fork for the connector: `ROS-TCP-Connector (fork) <https://github.com/NiklasDerEchte/ROS-TCP-Connector/tree/bugfix/deserializer>`__	
   For more informations, see `here <https://github.com/Unity-Technologies/ROS-TCP-Connector/pull/322>`__



..
   - Mixed Reality Toolkit (**MRTK**)
   - **AR Foundation**

.. 
   4. Build the project for HoloLens:
      - Switch platform to UWP.
      - Configure project settings for HoloLens.
   5. Deploy the app to the HoloLens.