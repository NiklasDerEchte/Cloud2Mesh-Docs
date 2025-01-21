Mesh Algorithms
===============

ROSPointCloudMeshify supports the following algorithms:

**1. Poisson Surface Reconstruction**:

- **Description**: Generates smooth surfaces from point clouds by solving a Poisson equation.
- **Use Case**: Ideal for continuous objects with detailed surfaces.
- **Advantages**: High-quality, smooth meshes.
- **Disadvantages**: Computationally intensive.

**2. Greedy Triangulation**:

- **Description**: Incrementally builds a mesh by connecting neighboring points.
- **Use Case**: Suitable for dense point clouds.
- **Advantages**: Fast and efficient.
- **Disadvantages**: May produce uneven results on sparse clouds.

**3. Fast Organized Triangle Reconstruction**:

- **Description**: Quickly reconstructs meshes by leveraging the organized structure of point clouds.
- **Use Case**: Best for structured light cameras like Zivid.
- **Advantages**: Extremely fast.
- **Disadvantages**: Limited to organized data.