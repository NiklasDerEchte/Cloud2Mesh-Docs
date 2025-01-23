Mesh Algorithms
===============

ROSPointCloudMeshify supports the following algorithms:

1. Poisson Surface Reconstruction:
##################################

- **Description**: Generates smooth surfaces from point clouds by solving a Poisson equation.
- **Use Case**: Ideal for continuous objects with detailed surfaces.
- **Advantages**: High-quality, smooth meshes.
- **Disadvantages**: Is computationally intensive and only works for closed surfaces.

2. Greedy Triangulation:
########################

- **Description**: Incrementally builds a mesh by connecting neighboring points.
- **Use Case**: Suitable for dense point clouds.
- **Advantages**: Fast and efficient.
- **Disadvantages**: May produce uneven results on sparse clouds.

.. raw:: html

   <video width="640" height="360" controls>
       <source src="_static/GreedyMesh.mp4" type="video/mp4">
       Ihr Browser unterstützt das Video-Tag nicht.
   </video>


3. Fast Organized Triangle Reconstruction:
##########################################

- **Description**: Quickly reconstructs meshes by leveraging the organized structure of point clouds.
- **Use Case**: Best for realtime processing of structured point clouds, such as those from depth sensors.
- **Advantages**: Extremely fast.
- **Disadvantages**: Limited to organized data.

.. raw:: html

   <video width="640" height="360" controls>
       <source src="_static/FastMesh.mp4" type="video/mp4">
       Ihr Browser unterstützt das Video-Tag nicht.
   </video>
