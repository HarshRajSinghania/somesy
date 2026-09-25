"""Regression tests for [project.urls] serialization spacing."""

from somesy.pyproject.writer import Pep621


def test_inserted_project_urls_has_blank_line_before_next_section(tmp_path):
    """Newly created [project.urls] must not be glued to the next table."""
    pyproject_str = """\
[project]
name = \"realuv\"
version = \"0.1.0\"
description = \"A test\"
authors = [{ name = \"Jane Doe\", email = \"jane@example.com\" }]

[build-system]
requires = [\"uv_build>=0.12.13,<0.13.0\"]
build-backend = \"uv_build\"
"""
    path = tmp_path / \"pyproject.toml\"
    path.write_text(pyproject_str)

    writer = Pep621(path)
    writer._set_property([\"urls\", \"homepage\"], \"https://example.com/\")
    writer._set_property([\"urls\", \"repository\"], \"https://github.com/example/realuv\")
    writer.save()

    text = path.read_text()
    assert (
        'repository = \"https://github.com/example/realuv\"\\n\\n[build-system]\\n' in text
    )
    assert (
        'repository = \"https://github.com/example/realuv\"\\n[build-system]' not in text
    )
