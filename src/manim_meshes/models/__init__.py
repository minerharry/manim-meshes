"""
all the model classes
"""

from manim_meshes.models.manim_models.basic_mesh import ManimMesh,Manim2DMesh
from manim_meshes.models.manim_models.opengl_mesh import FastManimMesh
from manim_meshes.models.manim_models.triangle_mesh import TriangleManim2DMesh

from manim_meshes.models.data_models.mesh import Mesh

__all__ = ["ManimMesh","Manim2DMesh","FastManimMesh","TriangleManim2DMesh","Mesh"]