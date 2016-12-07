__version__ = (0, 0, 0)


class Version(object):
    """
    Creates version according to https://www.python.org/dev/peps/pep-0440/
    """
    CURRENT_COMMIT_HASH_CMD = 'git rev-parse --short HEAD'
    DEVELOP_BRANCHES = ['dev', 'develop']
    RELEASE_BRANCHES = ['release']
    PRODUCTION_BRANCHES = ['master']

    SPEC_DEV = 'dev'
    SPEC_RC = 'rc'
    SPEC_FINAL = ''
    SPEC_POST = 'post'

    __version_base__ = None
    __branch__ = None
    __build_id__ = None
    __tag__ = None

    def __init__(self, base=__version__, branch=None, build_id=None, tag=None):
        """
        :type base: tuple[int]
        :type build_id: int
        :type branch: str
        """
        self.is_prerelease = False
        self.is_postrelease = False
        self.is_final = False
        self.is_production = False
        self.set_state(branch, tag)

        self.set_base(base)
        self.set_tag(tag)
        self.set_branch(branch)
        self.set_build_id(build_id)

    def set_base(self, val):
        self.__version_base__ = [str(s) for s in val]

    def set_build_id(self, val):
        if not val or (self.is_final and self.is_production):
            val = ''
        self.__build_id__ = str(val)

    def set_tag(self, val):
        """ consider tagged state as Final work """
        self.__tag__ = val

    def set_state(self, branch, tag):
        if branch:
            if any([s in branch for s in self.RELEASE_BRANCHES]):
                self.is_prerelease = True
            elif any([s in branch for s in self.PRODUCTION_BRANCHES]):
                self.is_production = True
                if not self.is_final:
                    self.is_postrelease = True
        if tag:
            self.is_final = True

    def set_branch(self, val):
        if self.is_prerelease:
            val = self.SPEC_RC
        elif self.is_production and self.is_final:
            val = self.SPEC_FINAL
        elif self.is_production and self.is_postrelease:
            val = self.SPEC_POST
        else:
            val = self.SPEC_DEV

        self.__branch__ = val 

    def get_base(self):
        return self.__version_base__

    def get_build_id(self):
        return self.__build_id__

    def get_branch(self):
        return self.__branch__

    @classmethod
    def get_last_commit_hash(cls):
        from subprocess import check_output
        import shlex
        out = check_output(shlex.split(cls.CURRENT_COMMIT_HASH_CMD))
        """ :type: str"""
        return out.split()

    def generate(self):
        """
        :rtype: str

        see https://www.python.org/dev/peps/pep-0440/#pre-release-separators
        https://www.python.org/dev/peps/pep-0440/#development-release-separators

        """
        parts = self.get_base()
        tail = self.get_branch() + self.get_build_id()

        if self.is_prerelease:
            version = ''.join(['.'.join(parts), tail])
        else:
            if tail:
                parts.append(tail)
            version = '.'.join(parts)
        return version
