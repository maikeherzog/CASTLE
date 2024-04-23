def get_leaf_nodes(tree):
    leaf_nodes = []

    if 'children' not in tree:
        return [tree['name']]

    for child in tree['children']:
        leaf_nodes.extend(get_leaf_nodes(child))

    return leaf_nodes

def count_all_leaves(tree):
    return len(get_leaf_nodes(tree))

def get_subtree(tree, root_name):
    if tree['name'] == root_name:
        return tree

    if 'children' in tree:
        for child in tree['children']:
            subtree = get_subtree(child, root_name)
            if subtree:
                return subtree

    return None