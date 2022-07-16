import logging

from trees.binary_search_tree import BinarySearchTree

logger = logging.getLogger(name=__name__)

if __name__ == '__main__':
    try:
        tree = BinarySearchTree()
        tree.lookup(5)
        tree.insert(9)
        tree.insert(4)
        tree.insert(6)
        tree.insert(20)
        tree.insert(170)
        tree.insert(15)
        tree.insert(1)
        tree.lookup(5)
        tree.lookup(9)
        tree.remove(20)
        print(tree.to_json())
    except Exception as ex:
        logger.error(str(ex), exc_info=True)
