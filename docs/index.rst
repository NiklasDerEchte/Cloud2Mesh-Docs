Cloud2Mesh Documentation
========================

Welcome to the documentation for **Cloud2Mesh**, a solution designed for capturing point clouds from a Zivid camera, converting objects into meshes in real-time, and streaming the resulting meshes to an AR HoloLens for visualization.

**Cloud2Mesh** is composed of two software projects:

* `ROSPointCloudMeshify <https://github.com/NiklasDerEchte/ROSPointCloudMeshify>`_: Converts PointCloud2 into meshes using state-of-the-art surface reconstruction algorithms.
* `ROSUnityRenderer <https://github.com/NiklasDerEchte/ROSUnityRenderer>`_: Visualizes and streams the generated meshes to Microsoft HoloLens.

This documentation covers the architecture, installation, usage, and technical details of both components.

.. toctree::

   self
   ros_point_cloud_meshify
   ros_unity_renderer
   installation
   usage
   mesh_algorithms
   architecture
   gpu
   contributing
   references

