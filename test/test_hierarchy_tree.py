from src.hierarchy_tree import *

def test_generalization_romantic_partner():
    attributes = ["Wife", "Husband"]
    generalization = relationship_tree.find_generalization(attributes)
    assert generalization == "Romantic-partner"

def test_generalization_any_relationship():
    attributes = ["Wife", "Own-child"]
    generalization = relationship_tree.find_generalization(attributes)
    assert generalization == "Any Relationship"

def test_generalization_own_child():
    attributes = ["Own-child"]
    generalization = relationship_tree.find_generalization(attributes)
    assert generalization == "Own-child"

def test_generalization_non_existent():
    attributes = ["Wife", "Brother"]
    generalization = relationship_tree.find_generalization(attributes)
    assert generalization is None

def test_generalization_duplicate_attributes():
    attributes = ["Wife", "Husband", "Wife"]
    generalization = relationship_tree.find_generalization(attributes)
    assert generalization == "Romantic-partner"

def test_generalization_all_family():
    attributes = ["Own-child", "Other-relative"]
    generalization = relationship_tree.find_generalization(attributes)
    assert generalization == "Family-member"

def test_generalization_non_unique_match():
    attributes = ["Wife", "Husband", "Own-child"]
    generalization = relationship_tree.find_generalization(attributes)
    assert generalization == "Any Relationship"


