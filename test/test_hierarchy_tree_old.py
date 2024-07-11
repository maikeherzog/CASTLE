from src.hierarchy_tree import *
from src.tree_functions import find_generalization, is_leaf_node


def test_generalization_romantic_partner():
    attributes = ["Wife", "Husband"]
    generalization = find_generalization(relationship_tree, attributes)
    assert generalization == "Romantic-partner"

def test_generalization_any_relationship():
    attributes = ["Wife", "Own-child"]
    generalization = find_generalization(relationship_tree, attributes)
    assert generalization == "Any Relationship"

def test_generalization_own_child():
    attributes = ["Own-child"]
    generalization = find_generalization(relationship_tree, attributes)
    assert generalization == "Own-child"

def test_generalization_duplicate_attributes():
    attributes = ["Wife", "Husband", "Wife"]
    generalization = find_generalization(relationship_tree, attributes)
    assert generalization == "Romantic-partner"

def test_generalization_all_family():
    attributes = ["Own-child", "Other-relative"]
    generalization = find_generalization(relationship_tree, attributes)
    assert generalization == "Family-member"

def test_generalization_non_unique_match():
    attributes = ["Wife", "Husband", "Own-child"]
    generalization = find_generalization(relationship_tree, attributes)
    assert generalization == "Any Relationship"

def test_generalization_with_ancor():
    attributes = ['Any Relationship', 'Family-member', 'Own-child']
    generalization = find_generalization(relationship_tree, attributes)
    assert generalization == "Any Relationship"

def test_if_leaf_node():
    assert(is_leaf_node(relationship_tree, "Wife"), True)
    assert (is_leaf_node(relationship_tree, "Any Relationship"), False)
    assert (is_leaf_node(relationship_tree, "Family-member"), False)

