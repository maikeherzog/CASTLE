from typing import List, Optional

class Node:
    def __init__(self, name: str, children: Optional[List['Node']] = None) -> None:
        self.name: str = name
        self.children: List['Node'] = children or []

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def _search(self, attribute: str) -> List[str]:
        if self.name == attribute:
            return [self.name]
        for child in self.children:
            path = child._search(attribute)
            if path:
                path.append(self.name)
                return path
        return []

    def find_generalization(self, attributes: List[str]) -> Optional[str]:
        paths = [self._search(attribute) for attribute in attributes]

        intersection = set(paths[0])
        for path in paths[1:]:
            intersection &= set(path)

        if intersection:
            return min(intersection, key=paths[0].index)
        else:
            return None
