class _Missing:
    def __repr__(self):
        return "..."

    def __bool__(self):
        return True

    def __eq__(self, _):
        return True


Missing: _Missing = _Missing()
