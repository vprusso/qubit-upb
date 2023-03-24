"""Test for UPB functions."""
import pytest
from src.orth_graph import (
    is_product_basis,
    is_unextendible,
)


@pytest.mark.parametrize(
    "graphs, expected_value",
    [
        ("product_state_graph", True),
        ("non_product_state_graph", False),
    ]
)
def test_is_product_basis(graphs, expected_value, request):
    graphs = request.getfixturevalue(graphs)
    assert is_product_basis(graphs) == expected_value


@pytest.mark.parametrize(
    "graphs, expected_value",
    [
        ("product_state_graph", False),
        ("non_product_state_graph", False),
    ]
)
def test_is_unextendible(graphs, expected_value, request):
    graphs = request.getfixturevalue(graphs)
    assert is_unextendible(graphs) == expected_value
