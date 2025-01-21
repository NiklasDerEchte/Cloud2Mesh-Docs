Getting Started
===============

ROSPointCloudMeshify
--------------------

1. Ensure the Zivid camera is streaming PointCloud2 data to `ROS2 <https://github.com/ros2/ros2>`__.
2. Launch the ROSPointCloudMeshify `ROS2 <https://github.com/ros2/ros2>`__ node:

   .. code-block:: bash

      ros2 run object_detection object_detection_mesh_creator_node --ros-args -p mode:=fast

3. The generated mesh will be published to the `/object_markers` topic.

ROSUnityRenderer
----------------

1. Launch the ROSUnityRenderer application on your HoloLens.
2. Connect to the `ROS2 <https://github.com/ros2/ros2>`__ topic where the meshes are published.
3. Observe the real-time visualization of meshes in the AR environment.
