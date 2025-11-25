def create_film():
    titre = input("Entrez le titre du film : ")
    description = input("Entrez la description du film : ")
    note = input("Entrez la note du film : ")
    return {"titre": titre, "description": description, "note": note}

def main():
    bibliotheque = []
    film = create_film()
    bibliotheque.append(film)

if __name__ == "__main__":
    main()





main()