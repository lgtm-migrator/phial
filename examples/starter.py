from phial import Phial, command, Response, Attachment
import os

slackbot = Phial(os.getenv("SLACK_TOKEN"))


@slackbot.command('ping')
def ping():
    '''Simple command which replies with a message'''
    return "Pong"


@slackbot.command('pong')
def pong():
    '''
    Simple command which replies with a message. Has a mutiline
    docstring.
    '''
    return "Ping"


@slackbot.command('hi <name>')
def hi(name):
    '''Simple command with argument which replies to a message'''
    return Response(text="Hello {0}".format(name), channel=command.channel)


@slackbot.command('hello <name> <from_>')
def hello(name, from_):
    '''Simple command with two arguments which replies to a message'''
    return Response(text="Hi {0}, from {1}".format(name, from_),
                    channel=command.channel)


@slackbot.command('react')
def react():
    '''Simple command that reacts to the original message'''
    return Response(reaction="x",
                    channel=command.channel,
                    original_ts=command.timestamp)


@slackbot.command('upload')
def upload():
    '''Simple command that uploads a set file'''
    project_dir = os.path.dirname(__file__)
    file_path = os.path.join(project_dir, 'phial.png')
    return Attachment(channel=command.channel,
                      filename='example.txt',
                      content=open(file_path, 'rb'))


@slackbot.command('reply')
def reply():
    '''Simple command that replies to the original message in a thread'''
    return Response(text="this is a thread",
                    channel=command.channel,
                    original_ts=command.timestamp)


@slackbot.command('caseSensitive', case_sensitive=True)
def case_sensitive():
    '''Simple command which replies with a message'''
    return "You typed caseSensitive"


@slackbot.command('messageWithAttachment')
def get_message_with_attachment():
    '''
        A command that posts a message with a Slack attachment.
        Read more: https://api.slack.com/docs/message-attachments
    '''
    attachments = [{
        "title": "Here's the title of the attachment",
        "text": "...and here's the text",
        "footer": "Teeny tiny footer text"
    }]
    return Response(channel=command.channel, attachments=attachments)


@slackbot.command('hidden', hide_from_help_command=True)
def hidden():
    '''
        A command that is hidden from the default help command
    '''
    return "Suprise"


@slackbot.fallback_command()
def fallback_command(command):
    return "Thats not a command"


if __name__ == '__main__':
    slackbot.run()
