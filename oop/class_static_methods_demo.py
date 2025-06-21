class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Performs addition without accessing class or instance state."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Performs multiplication while accessing a class-level attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

