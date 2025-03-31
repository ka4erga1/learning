class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        if "." in path:
            for i in range(path.count(".")):
                path.remove(".")
        if "" in path:
            for i in range(path.count("")):
                path.remove("")
        if ".." in path:
            for i in range(path.count("..")):
                if path.index("..") == 0:
                    path.remove("..")
                    continue
                path.pop(path.index("..") - 1)
                path.remove("..")
        path ="/" + "/".join(path)
        return path

    print(simplifyPath(1, "/a/../../b/../c//.//"))