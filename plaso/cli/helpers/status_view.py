# -*- coding: utf-8 -*-
"""The status view CLI arguments helper."""

from __future__ import unicode_literals

import sys

from plaso.cli import status_view
from plaso.cli import tools
from plaso.cli.helpers import interface
from plaso.cli.helpers import manager
from plaso.lib import errors


class StatusViewArgumentsHelper(interface.ArgumentsHelper):
  """Status view CLI arguments helper."""

  NAME = 'status_view'
  DESCRIPTION = 'Status view command line arguments.'

  # The window status-view mode has an annoying flicker on Windows,
  # hence we default to linear status-view mode instead.
  if sys.platform.startswith('win'):
    _DEFAULT_STATUS_VIEW_MODE = status_view.StatusView.MODE_LINEAR
  else:
    _DEFAULT_STATUS_VIEW_MODE = status_view.StatusView.MODE_WINDOW

  @classmethod
  def AddArguments(cls, argument_group):
    """Adds command line arguments to an argument group.

    This function takes an argument parser or an argument group object and adds
    to it all the command line arguments this helper supports.

    Args:
      argument_group (argparse._ArgumentGroup|argparse.ArgumentParser):
          argparse group.
    """
    argument_group.add_argument(
        '--status_view', '--status-view', dest='status_view_mode',
        choices=['linear', 'none', 'window'], action='store',
        metavar='TYPE', default=cls._DEFAULT_STATUS_VIEW_MODE, help=(
            'The processing status view mode: "linear", "none" or "window".'))

  @classmethod
  def ParseOptions(cls, options, configuration_object):
    """Parses and validates options.

    Args:
      options (argparse.Namespace): parser options.
      configuration_object (CLITool): object to be configured by the argument
          helper.

    Raises:
      BadConfigObject: when the configuration object is of the wrong type.
    """
    if not isinstance(configuration_object, tools.CLITool):
      raise errors.BadConfigObject(
          'Configuration object is not an instance of CLITool')

    status_view_mode = cls._ParseStringOption(
        options, 'status_view_mode',
        default_value=cls._DEFAULT_STATUS_VIEW_MODE)

    setattr(configuration_object, '_status_view_mode', status_view_mode)


manager.ArgumentHelperManager.RegisterHelper(StatusViewArgumentsHelper)
