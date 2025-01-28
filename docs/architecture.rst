Architecture
============

coming soon...

..
   System Overview
   ---------------

   The Cloud2Mesh architecture includes the following components:

   - **Zivid Camera**: Captures point clouds and publishes PointCloud2 data via `ROS2 <https://github.com/ros2/ros2>`__.
   - **ROSPointCloudMeshify**: Processes the point cloud and generates meshes.
   - **ROSUnityBIRPMeshViz**: Visualizes and streams the meshes in AR.

   **Data Flow Diagram**:

   .. code-block::

      Zivid Camera --> PointCloud2 (ROS) --> ROSPointCloudMeshify --> Mesh Topic --> ROSUnityBIRPMeshViz --> HoloLens