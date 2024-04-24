from src.edit_data import attribute_properties
from src.tree_functions import *


def Enlargement(cluster, tupel):
    """
      This function calculates the enlargement of a cluster C with respect to a tuple t.

      Args:
          cluster: A cluster represented as a list of tuples.
          tupel: A tuple.

      Returns:
          A list representing the enlargement of C with respect to t.
      """
    n = len(cluster[0])  # Assuming all tuples in C have the same length
    result = [0] * n

    # Calculate VInfoLoss for each attribute
    for i in range(n):
        # TODO: Implement VInfoLoss function here
        pass
        #vi_loss_c = VInfoLoss(C, i)
        #vi_loss_t = VInfoLoss([t], i)
        #result[i] = vi_loss_c - vi_loss_t

    return result
    pass

def VInfoLoss(attribut, pos) -> int:
    enlargement = 0
    if attribute_properties[pos]['type'] == 'continuous':
        enlargement=VInfoLoss_continuos(attribut, attribute_properties[pos]['interval'])
    elif attribute_properties[pos]['type'] == 'cathegorical':
        enlargement= VInfoLoss_cathegorical(attribut, attribute_properties[pos]['hierarchy_tree'])
    return enlargement

def VInfoLoss_continuos(attribut_range, domain_range):
    if len(attribut_range) == 1:
        # TODO: hier nochmal schauen ob das stimmt
        return (attribut_range[0])/(domain_range[1]-domain_range[0])
    return (attribut_range[1]- attribut_range[0])/(domain_range[1]-domain_range[0])

def VInfoLoss_cathegorical(attribut_range, domain_tree):
    enlargement = 0
    domain_range = count_all_leaves(domain_tree)
    attribute_range_generalized = find_generalization(domain_tree, attribut_range)
    generalized_range = count_all_leaves(get_subtree(domain_tree, attribute_range_generalized))
    return generalized_range/domain_range

