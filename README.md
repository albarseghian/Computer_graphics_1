# Computer_graphics_1
Interactive Bézier Curves and Surfaces with OpenGL (Python)

This project implements an interactive OpenGL application for visualizing parametric Bézier curves and surfaces in real time using Python.

The implementation follows concepts from the LearnOpenGL guide and was developed as part of a Computer Graphics project.

Features
Bézier Curves (Mandatory)

Implementation of parametric Bézier curve discretization

Uniform sampling of the parameter space t ∈ [0,1]

Visualization of:

Bézier curve

Control points

Control polygon

Interactive movement of control points

Curve Example

Yellow line → Bézier curve

Green points → Control points

Red lines → Control polygon

Bézier Surface (Bonus)

A Bézier surface is implemented using a 4×4 control grid and discretized in parametric coordinates (u,v).

Each vertex contains:

Position (x,y,z)

Normal vector (nx,ny,nz)

Parametric coordinates (u,v)

Visualization Modes

Lambertian shading

Diffuse lighting with a single light source

Surface normals visualization

Cyan vectors show interpolated normals

Parametric space visualization

Vertex colors depend on (u,v)

Real-Time Rendering

The project also demonstrates basic real-time rendering concepts:

Rendering of a simple mesh (triangle or cube)

Phong lighting model

Basic material and light setup

Light parameters:

Light position: (3,3,3)

Light color: (1,1,1)

Screenshots
Bézier Curve

Shows control points and the generated curve.

Bézier Surface – Lambertian Shading

Surface rendered with diffuse lighting.

Surface Normals Visualization

Interpolated normals displayed as cyan vectors.

Parametric Surface Coloring

Surface colored using parametric coordinates (u,v).

Phong Shaded Mesh

Simple mesh rendered using Phong shading.

Project Structure
computer-graphics/
│
├── main.py
├── bezier.py
│
├── shaders/
│   ├── vertex.glsl
│   ├── fragment.glsl
│   ├── simple_vertex.glsl
│   └── simple_fragment.glsl
│
├── docs/
│   ├── bezier_curve.png
│   ├── bezier_surface_lambert.png
│   ├── bezier_normals.png
│   ├── bezier_parametric.png
│   └── phong_triangle.png
│
└── README.md
Installation
1. Clone the repository
git clone https://github.com/albarseghian/computer-graphics.git
cd computer-graphics
2. Install dependencies
pip install numpy PyOpenGL glfw PyGLM
Running the Program
python main.py

This will open an OpenGL window showing the Bézier curve and surface.

Controls
Key	Action
1–4	Select control point
Arrow keys	Move selected control point
M	Switch surface visualization mode
Mathematical Background

A cubic Bézier curve is defined as:

B(t)=∑i=03(3i)(1−t)3−itiPi
B(t)=
i=0
∑
3
	​

(
i
3
	​

)(1−t)
3−i
t
i
P
i
	​


where:

P_i are control points

t is the parameter in [0,1]

The Bézier surface is computed using Bernstein polynomials in both (u,v) directions.

References

https://learnopengl.com

https://pyopengl.sourceforge.net

https://en.wikipedia.org/wiki/Bézier_curve

Author

Aleksandr Barseghyan
French University in Armenia
Faculty of Computer Science and Applied Mathematics

License

This project is developed for educational purposes as part of a university course.
