from msgspec import Struct, field


class JumperConfig(Struct):
    """
    Configuration for the 'jumper' tool, used to refactor code by moving functions and class definitions between files.

    Attributes:
        source_file (str): The path to the source file containing the code element to be moved.
        destination_file (str): The path to the destination file where the code element will be moved.
        element_type (str): The type of the code element to be moved, either 'function' or 'class'.
        element_name (str): The name of the function or class to be moved.
        overwrite (bool, optional): Whether to overwrite the destination file if it already exists. Defaults to False.
    """

    source_file: str
    destination_file: str
    element_type: str
    element_name: str
    overwrite: bool = field(default=False)
