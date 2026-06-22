class MontantInvalideError(Exception):
    """
    Levée quand un montant n'est pas numérique, est nul ou est négatif.
    Hérite de Exception (demandé par le sujet) plutôt que de ValueError,
    pour que le code appelant puisse intercepter précisément CETTE erreur
    métier, sans risquer d'attraper aussi d'autres ValueError sans rapport
    avec la logique bancaire.
    """
    def __init__(self, message="Le montant doit être un nombre positif"):
        self.message = message
        super().__init__(self.message)


class SoldeInsuffisantError(Exception):
    """
    Levée quand un retrait dépasse le solde disponible.
    """
    def __init__(self, message="Solde insuffisant pour effectuer ce retrait"):
        self.message = message
        super().__init__(self.message)