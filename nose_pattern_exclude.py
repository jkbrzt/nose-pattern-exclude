import os
import logging
from fnmatch import fnmatch

from nose.plugins import Plugin


class NosePatternExclude(Plugin):

    def options(self, parser, env=os.environ):
        super(NosePatternExclude, self).options(parser, env)
        parser.add_option(
            '--exclude-path',
            action='append',
            dest="excludes",
            help=(
                'Directory or file path or a pattern glob to exclude '
                'from test discovery. May be specified multiple times.'
            )
        )

    def configure(self, options, conf):
        if not options.excludes:
            self.enabled = False
            return
        self.enabled = True
        self.excludes = list(map(os.path.abspath, options.excludes))
        self.logger = logging.getLogger(
            '%s.%s' % (__name__, type(self).__name__))
        self.logger.info('exclude patterns: %r' % self.excludes)

    def _include(self, path):
        for pattern in self.excludes:
            if fnmatch(path, pattern):
                self.logger.info("excluded path: '%s' (pattern '%s')",
                                 path, pattern)
                return False

    wantFile = _include
    wantDirectory = _include
