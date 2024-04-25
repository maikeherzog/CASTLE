from src.edit_data import attribute_properties, attribute_properties_test
from src.tree_functions import *


def Enlargement(cluster, tupel):
    """
      This function calculates the enlargement of a cluster C with respect to a tuple t.

      Args:
          cluster: A cluster represented as a list of tuples.
          tupel: A tuple.

      Returns:
          A number representing the enlargement of a cluster with respect to t.
      """
    n = len(cluster)  # Assuming all tuples in C have the same length
    enlarged_cluster = add_tupel(cluster, tupel)
    sum_iloss_cluster = 0
    sum_iloss_enlarged_cluster = 0

    # Calculate VInfoLoss for each attribute
    for i in range(n):
        info_loss_cluster = VInfoLoss_cluster(cluster[i], i)
        sum_iloss_cluster += info_loss_cluster
        info_loss_together = VInfoLoss(enlarged_cluster[i], i)
        sum_iloss_enlarged_cluster += info_loss_together

    return 1/n * sum_iloss_enlarged_cluster - 1/n * sum_iloss_cluster

def add_tupel(cluster, tupel):
    new_cluster = list(cluster)
    for i in range(len(cluster)-1):
        if attribute_properties_test[i]['type'] == 'continuous':
            new_cluster[i] = adjust_interval(tupel[i], cluster[i])

        elif attribute_properties_test[i]['type'] == 'cathegorical':
            new_cluster[i] = add_unique_string_to_list(tupel[i], cluster[i])

    return tuple(new_cluster)

def adjust_interval(value, interval):
    lower_bound, upper_bound = interval

    if value < lower_bound:
        lower_bound = value
    elif value > upper_bound:
        upper_bound = value

    return [lower_bound, upper_bound]

def add_unique_string_to_list(value, value_list):
    if value not in value_list:
        value_list.append(value)
def is_in_interval(value, interval):
    lower_bound, upper_bound = interval
    return lower_bound <= value <= upper_bound
def VInfoLoss(attribut, pos) -> int:
    enlargement = 0
    if attribute_properties_test[pos]['type'] == 'continuous':
        enlargement=VInfoLoss_continuos(attribut, attribute_properties_test[pos]['interval'])
    elif attribute_properties_test[pos]['type'] == 'cathegorical':
        enlargement= VInfoLoss_cathegorical(attribut, attribute_properties_test[pos]['hierarchy_tree'])
    return enlargement

def VInfoLoss_cluster(attribut, pos) -> int:
    enlargement = 0
    if attribute_properties_test[pos]['type'] == 'continuous':
        enlargement=VInfoLoss_continuos(attribut, attribute_properties_test[pos]['interval'])
    elif attribute_properties_test[pos]['type'] == 'cathegorical':
        enlargement= VInfoLoss_cathegorical_cluster(attribut, attribute_properties_test[pos]['hierarchy_tree'])
    return enlargement

def VInfoLoss_continuos(attribut_range, domain_range):
    if len(attribut_range) == 1:
        # TODO: hier nochmal schauen ob das stimmt
        return (attribut_range[0])/(domain_range[1]-domain_range[0])
    return (attribut_range[1]- attribut_range[0])/(domain_range[1]-domain_range[0])

def VInfoLoss_cathegorical(attribut_range, domain_tree):
    domain_range = count_all_leaves(domain_tree)
    attribute_range_generalized = find_generalization(domain_tree, attribut_range)
    generalized_range = count_all_leaves(get_subtree(domain_tree, attribute_range_generalized))
    erg = (generalized_range - 1) /(domain_range - 1)
    return erg

def VInfoLoss_cathegorical_cluster(attribut_range, domain_tree):
    domain_range = count_all_leaves(domain_tree)
    generalized_range = len(attribut_range)
    erg = (generalized_range - 1) /(domain_range - 1)
    return erg

