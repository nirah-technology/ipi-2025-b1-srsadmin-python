class Film:
    def __init__(self, title: str, year: int, kinds: list[str]):
        self.__title: str = title
        self.__year: int = year
        self.__kinds: list[str] = kinds
    
    def get_title(self) -> str:
        return self.__title
    
    def get_year(self) -> int:
        return self.__year

    def get_kinds(self) -> list[str]:
        return self.__kinds.copy()

film = Film("Terminator", 1991, ["Action", "Sci-Fi"])
film.get_kinds().append("Thriller")

print(film.get_kinds())