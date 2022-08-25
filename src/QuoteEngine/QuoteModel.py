"""Class that implements a quote."""


class QuoteModel:
    """Class that implements a quote."""

    def __init__(self, body, author):
        """Initialize the QuoteModel. arguments: body and author."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return str repr of Quote."""
        return f'"{self.body}" - {self.author}'
