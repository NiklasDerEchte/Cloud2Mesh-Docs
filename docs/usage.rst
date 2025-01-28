Getting Started
===============

ROSPointCloudMeshify
--------------------

Launch the `ROSPointCloudMeshify <https://github.com/NiklasDerEchte/ROSPointCloudMeshify>`_ `ROS2 <https://github.com/ros2/ros2>`__ node:

   .. code-block:: bash

      ros2 run object_detection object_detection_mesh_creator_node --ros-args -p mode:=fast
   
   -  The `mode` parameter can be set to `fast`, `greedy`, or `poisson` to select the surface reconstruction algorithm.

- The generated mesh will be published to the `/object_markers` topic as MarkerArray.
- The PointCloud2 data is received from the `/points/xyzrgba` topic.

ROSUnityMeshViz
----------------

Start the `ROS-TCP-Endpoint <https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/setup.md#-ros2-environment>`__

.. code-block:: bash

   ros2 run ros_tcp_endpoint default_server_endpoint --ros-args -p ROS_IP:=0.0.0.0

Launch the ROSUnityMeshViz application on Unity and connect to the endpoint.


..
   1. Launch the ROSUnityBIRPMeshViz application on your HoloLens.
   2. Connect to the `ROS2 <https://github.com/ros2/ros2>`__ topic where the meshes are published.
   3. Observe the real-time visualization of meshes in the AR environment.


Streaming PointCloud2 Data
--------------------------

Ensure you have a source with PointCloud2 data via ROS2, for example from a 3D camera or a ROS2 bag file.
In my example, I use the Zivid camera with `zivid-ros <https://github.com/zivid/zivid-ros>`__.