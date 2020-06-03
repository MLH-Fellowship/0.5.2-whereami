from functools import reduce

import typer

from web.mappings import map


app = typer.Typer()


@app.command()
def get_word(char_code: str):
    word = map[char_code]
    typer.echo(f"{word}")


@app.command()
def get_phrase(code: str):
    try:
        if len(code) < 8:
            error = typer.style("OLC is too short.", fg=typer.colors.RED)
            typer.echo(error)
            return
        # Split string into array of 2 char elements.
        char_arr = [code[i: i+2] for i in range(0, len(code), 2)]
        # Convert coded array to word phrase.
        phrase = reduce(lambda acc, x: acc + "." + map[x], char_arr, "")[1:]
        typer.echo(f"{phrase}")
    except KeyError:
        error = typer.style("Not a valid OLC.", fg=typer.colors.RED)
        typer.echo(error)


if __name__ == "__main__":
    app()
