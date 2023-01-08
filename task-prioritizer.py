from functools import cmp_to_key
import click
import colorama

def cursor_up_and_clear(times):
    for i in range(times):
        print(colorama.Cursor.UP() + colorama.ansi.clear_line() + colorama.Cursor.UP())

def compare(item1, item2):
    click.secho('Prioritize', fg='green')
    click.secho(f'a: "{item2}"', fg="red")
    click.secho('or', fg='green')
    click.secho(f'b: "{item1}"', fg="blue")
    click.secho('or', fg='green')
    click.secho('c: "both or none"', fg='yellow')
    choice = click.prompt(click.style('?', fg='green'), type=click.Choice(['a', 'b', 'c']), show_choices=False)
    cursor_up_and_clear(7)
    lookup = {'a':1, 'b':-1, 'c':0}
    return lookup[choice]

def print_task_list(task_list):
    for num, task in enumerate(task_list):
        click.secho(f'{num+1}: "{task}"', fg='yellow')

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    colorama.init()
    task_list = list()
    with open(filename, 'r', encoding='UTF-8') as f:
        task_list = [line.rstrip() for line in f]
    try:
        sorted_task_list = sorted(task_list, key=cmp_to_key(compare))
        click.secho('Prioritized Task List', fg='green')
        print_task_list(sorted_task_list)
    except:
        print('exiting...')

if __name__ == '__main__':
    main()
