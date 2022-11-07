import sys

from datetime import datetime
import typer

sys.path.append('./') 

from tec_mlops_mod2.todos.list_methods import check_list_exists
from tec_mlops_mod2.todos.list_methods import create_list
from tec_mlops_mod2.todos.list_methods import get_existing_lists
from tec_mlops_mod2.todos.list_methods import load_list
from tec_mlops_mod2.todos.list_methods import add_to_list
from tec_mlops_mod2.todos.list_methods import update_task_in_list

app = typer.Typer(add_completion=False)

@app.command("create")
def create(name: str = typer.Option("Unnamed", "-ln", "--listname")):
    r""" Creates a new list with the given name.

    Creates a new empty list using the given listname or assignes it as "Unnamed".

    Parameters
    ----------
    name : string
        The name of the list as it will be saved without the extention.

    """
    if check_list_exists(name):
        print("There is already a todo list with this name.")
        return
    create_list(name)
    print(f"Todo list {name} successfully created!")

@app.command("list")
def list_lists():
    r""" Lists all existing todo lists.

    It prints the a lists of all the todo lists available.
    """
    existing_lists = get_existing_lists()
    for ls in existing_lists:
        print(ls)

@app.command("show")
def show_list(list_name: str = typer.Option(..., "-ln", "--listname")):
    r""" Shows Task in one list.

    Checks if the listname entered exists, and if not, it prints a message
    to notify that the given list does not exist.
    If the list exists, it loads the list and prints it as markdown.

    Parameters
    ----------
    listname : string
        The name of the list as it will be saved without the extention.

    """
    if not check_list_exists(list_name):
        print("The list does not exist. Use create list first.")
        return
    df = load_list(list_name)
    print(df.to_markdown())

@app.command("add")
def add_task(
    list_name: str = typer.Option(..., "-ln", "--listname"),
    task_name: str = typer.Option(..., "-tn", "--taskame"),
    summary: str = typer.Option(None, "-d", "--description"),
    owner: str = typer.Option(..., "-o", "--owner"),
):
    r""" Add a task to a given todo list.

    Checks if the listname entered exists, and if not, it prints a message
    to notify that the given list does not exist.
    If the list exists, it creates a new row with the following fields:
        created: Assinges the datime.now() function.
        task: Assigns the -tn or --taskname given.
        summary: Assigns the -d or --description if given or None if not.
        status: Assings "todo".
        owner: Assigns it to the -o or --owner given.

    Parameters
    ----------
    listname : string
        The name of the list as it will be saved without the extention.
    taskname : string
        The name of the new task that will be enterned in the list.
    summary: string
        Description of the thask added to the list.
    owner: string
        Name of the person that the task is assigned to.
    """
    if not check_list_exists(list_name):
        print("The list does not exist. Use create list first.")
        return
    new_row = {
        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        "task": task_name,
        "summary": summary if summary else None,
        "status": "todo",
        "owner": owner,
    }
    add_to_list(list_name, new_row)
    print("Task successfully added")

@app.command("update")
def update_task(
    list_name: str = typer.Option(..., "-ln", "--listname"),
    task_id: int = typer.Option(..., "-i", "--taskid"),
    field: str = typer.Option(..., "-f", "--field"),
    change: str = typer.Option(..., "-c", "--change"),
):
    r""" Update a task in a given todo list.

    Checks if the listname entered exists, and if not, it prints a message
    to notify that the given list does not exist.
    If the list exists, it updates the task using the update_task_in_list()
    function using as parameters the list_name, task_id, field and 
    parameters.
        
    Parameters
    ----------
    listname : string
        The name of the list as it will be saved without the extention.
    task_id : int
        Index of the task that will be updated.
    field: string
        Name of the column that will be updated.
    change: string
        New value that will replace the previous one in the task.
    """
    if not check_list_exists(list_name):
        print("The list does not exist. Use create list first.")
        return
    update_task_in_list(list_name, task_id, field, change)
    print("Task successfully updated")

if __name__ == "__main__":
    app()