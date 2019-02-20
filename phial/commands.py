from typing import TYPE_CHECKING, cast
from phial.utils import parse_help_text

if TYPE_CHECKING:
    from phial import Phial  # noqa


def help_command(bot: 'Phial') -> str:
    help_text = cast(str, bot.config.get('baseHelpText', ""))
    if help_text:
        help_text += "\n"
    for command in bot.commands:
        command_doc = command.help_text
        if not command_doc:
            # If no help text default to blank string
            command_doc = ""
        command_help_text = parse_help_text(command_doc)
        help_text += "*{0}* - {1}\n".format(command.pattern_string,
                                            command_help_text)
    return help_text
