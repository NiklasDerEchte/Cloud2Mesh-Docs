Installation Guide
==================

Prerequisites
-------------

To get started, ensure you have the following:

- **Zivid Camera** with `drivers <https://support.zivid.com/en/latest/getting-started/software-installation.html>`__ installed.
- **Microsoft HoloLens** (HoloLens 2 recommended).
- `ROS2 <https://github.com/ros2/ros2>`__: `Humble <https://docs.ros.org/en/humble/index.html>`__.
- **Unity 2021 or higher** with AR Foundation.

**ROSPointCloudMeshify Requirements**:

- A **C++ compiler** (GCC, Clang, or MSVC).
- `ROS2 <https://github.com/ros2/ros2>`__ installation with support for `sensor_msgs`.
- PointCloud Library (**PCL**) installed.

**ROSUnityRenderer Requirements**:

- Unity Editor.
- Mixed Reality Toolkit (**MRTK**) for HoloLens.
- AR Foundation.

Installation Steps
------------------

**1. ROSPointCloudMeshify**:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/NiklasDerEchte/ROSPointCloudMeshify
      cd ROSPointCloudMeshify

2. Install dependencies:

   .. code-block:: bash

      sudo apt-get install libpcl-dev ros-noetic-pcl-ros

3. Build the project:

   .. code-block:: bash

      mkdir build
      cd build
      cmake ..
      make

4. Run the `ROS2 <https://github.com/ros2/ros2>`__ node:

   .. code-block:: bash

      roslaunch ROSPointCloudMeshify pointcloud_to_mesh.launch

**2. ROSUnityRenderer**:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/NiklasDerEchte/ROSUnityRenderer
      cd ROSUnityRenderer

2. Open the project in Unity Editor.

3. Import required Unity packages:
   - Mixed Reality Toolkit (**MRTK**)
   - **AR Foundation**

4. Build the project for HoloLens:
   - Switch platform to UWP.
   - Configure project settings for HoloLens.

5. Deploy the app to the HoloLens.