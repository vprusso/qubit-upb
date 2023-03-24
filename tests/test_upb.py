"""Test for UPB functions."""
import pytest
from src.orthogonality_graph import is_product_basis


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
