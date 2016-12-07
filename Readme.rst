Version-flow
============

This is a tool for version generation.
It's generally meets PEP-440 https://www.python.org/dev/peps/pep-0440/

a code example::

  from version_flow import Version
  __version__ = (1, 5, 10)

  def get_version(build_id=None, branch=None, tag=None):
      return Version(__version__, build_id=build_id,
                     branch=branch, tag=tag).generate()


