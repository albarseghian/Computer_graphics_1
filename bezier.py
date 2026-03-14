import numpy as np
from math import comb

def bezier_point(control_points, t):
    """
    Compute a single point on a Bézier curve at parameter t.
    control_points: list of 2D or 3D points (numpy arrays)
    t: float between 0 and 1
    """
    n = len(control_points) - 1
    point = np.zeros(3)
    for i, P in enumerate(control_points):
        bern = comb(n, i) * (t ** i) * ((1 - t) ** (n - i))
        point += bern * P
    return point

def sample_bezier(control_points, segments):
    """
    Sample points along a Bézier curve.
    segments: number of segments (int)
    returns: list of points
    """
    points = []
    for i in range(segments + 1):
        t = i / segments
        points.append(bezier_point(control_points, t))
    return np.array(points, dtype=np.float32)

import numpy as np
from itertools import product

def sample_bezier_surface(control_grid, u_segments=20, v_segments=20):
    """
    control_grid: 2D array of shape (n, m, 3)
    Returns: surface points (positions) and normals
    """
    n, m, _ = control_grid.shape
    u_vals = np.linspace(0, 1, u_segments)
    v_vals = np.linspace(0, 1, v_segments)

    def bernstein_poly(i, n, t):
        from math import comb
        return comb(n, i) * (t**i) * ((1-t)**(n-i))

    # Compute surface points
    surface_points = []
    for u in u_vals:
        for v in v_vals:
            p = np.zeros(3)
            for i in range(n):
                bu = bernstein_poly(i, n-1, u)
                for j in range(m):
                    bv = bernstein_poly(j, m-1, v)
                    p += bu * bv * control_grid[i,j]
            surface_points.append(p)
    surface_points = np.array(surface_points, dtype=np.float32)

    # Compute normals using finite difference (approximate)
    normals = np.zeros_like(surface_points)
    du = 1.0 / (u_segments - 1)
    dv = 1.0 / (v_segments - 1)

    for ui, u in enumerate(u_vals):
        for vi, v in enumerate(v_vals):
            # Neighbor indices for derivative
            ip = min(ui + 1, u_segments-1)
            im = max(ui - 1, 0)
            jp = min(vi + 1, v_segments-1)
            jm = max(vi - 1, 0)
            idx = ui * v_segments + vi

            dpdu = surface_points[ip * v_segments + vi] - surface_points[im * v_segments + vi]
            dpdv = surface_points[ui * v_segments + jp] - surface_points[ui * v_segments + jm]
            n = np.cross(dpdu, dpdv)
            n /= np.linalg.norm(n) + 1e-8
            normals[idx] = n

    return surface_points, normals