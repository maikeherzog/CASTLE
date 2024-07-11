from typing import List, Optional


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


def is_leaf_node(tree, node_name):
    # Sucht nach dem Knoten mit dem gegebenen Namen im Baum
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
        return f'Knoten {node_name} nicht gefunden im Baum.'

    if 'children' in node:
        return False
    else:
        return True

def find_generalization(tree, node_list):
    def find_path(node, target):
        if node['name'] == target:
            return [node['name']]

        for child in node.get('children', []):
            path = find_path(child, target)
            if path:
                return [node['name']] + path

        return None

    """def find_common_ancestor(paths):
        common_ancestor = paths[0]
        for path in paths[1:]:
            i = 0
            while i < min(len(common_ancestor), len(path)) and common_ancestor[i] == path[i]:
                i += 1
            common_ancestor = common_ancestor[:i]
        return common_ancestor[-1] if common_ancestor else None

    paths = [find_path(tree, node) for node in node_list]
    common_ancestor = find_common_ancestor(paths)

    return common_ancestor if common_ancestor else 'Not Found'"""