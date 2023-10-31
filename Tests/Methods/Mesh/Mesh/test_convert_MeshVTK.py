# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.MeshVTK import MeshVTK
from numpy.testing import assert_array_almost_equal

from Tests import TEST_DATA_DIR
import numpy as np
from os.path import join


@pytest.mark.MeshSol
def test_convert_MeshVTK():
    """test convert method of MeshVTK with some vtu file"""
    mesh = MeshVTK(
        path=join(TEST_DATA_DIR, "StructElmer"), name="case_t0001", format="vtu"
    )

    meshmat = mesh.convert(meshtype="MeshMat", scale=1)

    nodes_pv = mesh.get_node_coordinate()
    nodes = meshmat.get_node_coordinate()
    assert_array_almost_equal(nodes_pv, nodes, decimal=6)

    elements_pv, _, _ = mesh.get_element()
    elements, _, _ = meshmat.get_element()
    assert_array_almost_equal(elements_pv["quad9"], elements["quad9"], decimal=1)


if __name__ == "__main__":
    test_convert_MeshVTK()
