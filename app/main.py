def format_linter_error(error: dict) -> dict:
    return {("line" if key == "line_number" else
             "column" if key == "column_number" else
             "message" if key == "text" else
             "name" if key == "code" else key): value
            for key, value in list(error.items()) + [("source", "flake8")]
            if key in ["line_number", "column_number",
                       "text", "code", "source"]}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {
                {
                    "line_number": "line",
                    "column_number": "column",
                    "text": "message",
                    "code": "name",
                    "source": "source",
                }[k]: v
                for k, v in list(erro.items()) + [("source", "flake8")]
                if k in [
                    "line_number", "column_number", "text", "code", "source"]
            }
            for erro in errors
        ],
        "path": file_path,
        "status": "failed" if errors else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    {
                        "line_number": "line",
                        "column_number": "column",
                        "text": "message",
                        "code": "name",
                        "source": "source",
                    }[k]: v
                    for k, v in list(erro.items()) + [("source", "flake8")]
                    if k in [
                        "line_number", "column_number",
                        "text", "code", "source"
                    ]
                }
                for erro in lista_erros
            ],
            "path": caminho_arquivo,
            "status": "failed" if lista_erros else "passed"
        }
        for caminho_arquivo, lista_erros in linter_report.items()
    ]
