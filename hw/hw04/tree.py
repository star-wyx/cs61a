## Tree Class ##

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()


def generate_paths(t, x):
    res = []

    def foo(tmp, a, y):
        nonlocal res
        if a.label == y:
            # tmp.append(a.label)
            res.append(tmp[:])
            # tmp.pop(len(tmp) - 1)
            return
        for branch in a.branches:
            tmp.append(branch.label)
            foo(tmp, branch, y)
            tmp.pop(len(tmp) - 1)

    foo([t.label], t, x)
    for i in res:
        yield i

t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
t2 = Tree(0, [Tree(2, [t1])])
generate_paths(t2, 2)
