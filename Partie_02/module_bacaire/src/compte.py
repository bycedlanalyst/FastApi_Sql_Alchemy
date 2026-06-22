from .exceptions import MontantInvalideError, SoldeInsuffisantError


class CompteBancaire:
    def __init__(self, titulaire: str, solde: float = 0):
        if solde < 0:
            raise MontantInvalideError("Le solde initial ne peut pas être négatif")
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant: float):
        if not isinstance(montant, (int, float)) or montant <= 0:
            raise MontantInvalideError("Le dépôt doit être strictement positif")
        self.solde += montant

    def retirer(self, montant: float):
        if not isinstance(montant, (int, float)) or montant <= 0:
            raise MontantInvalideError("Le retrait doit être strictement positif")
        if montant > self.solde:
            raise SoldeInsuffisantError("Le retrait dépasse le solde disponible")
        self.solde -= montant

    def consulter_solde(self):
        return self.solde

    def afficher(self):
        return {
            "titulaire": self.titulaire,
            "solde": self.solde
        }