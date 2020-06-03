import helper

import typer


app = typer.Typer()


@app.command()
def get_word(char_code: str):
    word = helper.get_word(char_code)
    typer.echo(f"{word}")


@app.command()
def get_code(word: str):
    code = helper.get_code(word)
    typer.echo(f"{code}")


@app.command()
def get_phrase(olc: str, single: bool = False):
    try:
        phrase = helper.olc_to_phrase(olc, single)
        typer.echo(f"{phrase}")
    except KeyError:
        error = typer.style("Not a valid plus code.", fg=typer.colors.RED)
        typer.echo(error)


@app.command()
def get_single_phrase(olc: str):
    get_phrase(olc, True)


@app.command()
def get_double_phrase(olc: str):
    get_phrase(olc, False)


@app.command()
def get_plus_code(phrase: str):
    try:
        olc = helper.phrase_to_olc(phrase)
        typer.echo(f"{olc}")
    except KeyError:
        error = typer.style("Plus code not found.", fg=typer.colors.RED)
        typer.echo(error)


if __name__ == "__main__":
    app()
