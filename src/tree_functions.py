"""
This module provides functions for working with tree structures.
"""
def get_leaf_nodes(tree):
    """
    Returns a list of all leaf nodes in the tree.
    :param tree (dict): the tree
    :return: a list of all leaf nodes in the tree
    """
    leaf_nodes = []

    if 'children' not in tree:
        return [tree['name']]

    for child in tree['children']:
        leaf_nodes.extend(get_leaf_nodes(child))

    return leaf_nodes

def count_all_leaves(tree):
    """
    Gets the number of all leaf nodes in the tree.
    :param tree (dict): the tree
    :return: the number of all leaf nodes in the tree
    """
    return len(get_leaf_nodes(tree))

def get_subtree(tree, root_name):
    """
    Gets the subtree with the given root name.
    :param tree (dict): the tree
    :param root_name (str): the name of the root node of the subtree
    :return: the subtree with the given root name
    """
    if tree['name'] == root_name:
        return tree

    if 'children' in tree:
        for child in tree['children']:
            subtree = get_subtree(child, root_name)
            if subtree:
                return subtree

    return None


def is_leaf_node(tree, node_name):
    """
    Checks if the given node is a leaf node.
    :param tree (dict): the tree
    :param node_name (str): the name of the node to check
    :return: True if the node is a leaf node, False otherwise
    """
    def search_node(tree, node_name):
        if tree['name'] == node_name:
            return tree
        if 'children' in tree:
            for child in tree['children']:
                result = search_node(child, node_name)
                if result is not None:
                    return result
        return None

    node = search_node(tree, node_name)

    if node is None:
        return f'Node {node_name} not found in tree.'

    if 'children' in node:
        return False
    else:
        return True

def find_generalization(tree, node_list):
    """
    Finds the common ancestor of the given nodes in the tree.
    :param tree (dict): the tree
    :param node_list (list): the list of nodes to find the common ancestor for
    :return (str): the common ancestor of the given nodes
    """
    def find_path(node, target):
        """
        Finds the path from the root node to the target node.
        :param node (dict): the current node
        :param target (str): the target node
        :return (list): the path from the root node to the target node
        """
        if node['name'] == target:
            return [node['name']]

        for child in node.get('children', []):
            path = find_path(child, target)
            if path:
                return [node['name']] + path

        return None

    def find_common_ancestor(paths):
        """
        Finds the common ancestor of the given paths.
        :param paths (list): the list of paths
        :return (str): the common ancestor of the given paths
        """
        common_ancestor = paths[0]
        for path in paths[1:]:
            i = 0
            while i < min(len(common_ancestor), len(path)) and common_ancestor[i] == path[i]:
                i += 1
            common_ancestor = common_ancestor[:i]
        return common_ancestor[-1] if common_ancestor else None

    paths = [find_path(tree, node) for node in node_list]
    common_ancestor = find_common_ancestor(paths)

    return common_ancestor if common_ancestor else 'Not Found'