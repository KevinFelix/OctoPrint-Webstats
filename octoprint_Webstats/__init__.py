# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin

class WebstatsPlugin(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info("Hello Stats!")

__plugin_name__ = "Webstats"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = WebstatsPlugin()
