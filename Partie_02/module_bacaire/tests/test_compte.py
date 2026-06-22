import pytest

from src.compte import CompteBancaire
from src.exceptions import MontantInvalideError, SoldeInsuffisantError


def test_deposer_augmente_le_solde():
    compte = CompteBancaire("Alice", 100)
    compte.deposer(50)
    assert compte.consulter_solde() == 150


def test_retirer_diminue_le_solde():
    compte = CompteBancaire("Alice", 100)
    compte.retirer(30)
    assert compte.consulter_solde() == 70


def test_retirer_trop_leve_solde_insuffisant():
    compte = CompteBancaire("Alice", 100)
    with pytest.raises(SoldeInsuffisantError):
        compte.retirer(200)


def test_deposer_montant_negatif_leve_erreur():
    compte = CompteBancaire("Alice", 100)
    with pytest.raises(MontantInvalideError):
        compte.deposer(-10)


def test_deposer_montant_nul_leve_erreur():
    compte = CompteBancaire("Alice", 100)
    with pytest.raises(MontantInvalideError):
        compte.deposer(0)


def test_creation_compte_solde_negatif_leve_erreur():
    with pytest.raises(MontantInvalideError):
        CompteBancaire("Alice", -50)


@pytest.mark.skip(reason="Gestion multi-devises pas encore implémentée")
def test_conversion_devises():
    pass