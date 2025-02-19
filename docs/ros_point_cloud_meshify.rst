ROSPointCloudMeshify Overview
=============================

The `ROSPointCloudMeshify <https://github.com/NiklasDerEchte/ROSPointCloudMeshify>`_ module handles the following:

- **Receives PointCloud2 data** via `ROS2 <https://github.com/ros2/ros2>`__ topic <points/xyzrgba>, for example, from a `Zivid <https://github.com/zivid/zivid-ros>`__ camera.
- **Processes point clouds** and converts them into meshes using advanced algorithms.
- **Supports multiple meshing techniques**, including:

  - Poisson Surface Reconstruction `(mode=poisson)`
  - Greedy Triangulation `(mode=greedy)`
  - Fast Organized Triangle Reconstruction `(mode=fast)`

- **Publish the generated mesh** to the `/object_markers` topic as **MarkerArray**.

Features
--------

- Real-time meshing of point cloud data.
- Integration with `ROS2(Humble) <https://docs.ros.org/en/humble/index.html>`__ for seamless communication.
- Built with **C++** and relies on the `PointCloud Library <https://github.com/PointCloudLibrary/pcl>`__.

Repository: `GitHub - ROSPointCloudMeshify <https://github.com/NiklasDerEchte/ROSPointCloudMeshify>`_

